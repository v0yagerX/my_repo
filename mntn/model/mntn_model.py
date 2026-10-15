"""
MNTN, Inc. (NYSE: MNTN) - driver-based model, FY2026E-FY2030E, three scenarios + stress tests.  (v3)

Run:  python3 mntn/model/mntn_model.py
      -> writes mntn/model/output/model_output.md, scenario_*.csv, summary.json

Conventions
- $M unless noted. Revenue is NET of media cost (MNTN reports as an agent; 10-K FY2025 Note 2).
- Every assumption below is an [estimate] unless tagged [reported]/[guidance]/[consensus].
- Revenue build = sum over customer-size segments of
      (TTM active Performance TV customers) x (net revenue per TTM customer)
  + creative/QuickFrame services + QuickFrame AI subscription monetization.
  MNTN discloses only TOTAL TTM active customers (3,632 at FY25 [reported]) and the small-business share of
  PTV revenue (~6% FY24 -> 12% Q1'25 [reported, 424B4] -> ~15% Q3'25 [CEO via AdExchanger]); SMBs were ~92%
  of FY24 PTV revenue [reported]. The FY25 count split below is therefore an [estimate]. Segments are by
  advertiser size (MNTN's own SMB definitions), not by spend band; segment averages are means over a highly
  skewed distribution (top-10 customers = ~17% of FY25 revenue [reported]).
- Costs are modeled on a cash basis (ex-SBC, ex-D&A); GAAP lines are rebuilt by adding SBC (by function) and
  D&A (capitalized-software amortization in cost of revenue; acquired-intangible amortization separately).
- Adjusted EBITDA follows the company definition (adds back SBC, D&A, fair-value marks, acquisition-related
  legal, restructuring).
- Adjusted EPS (ours; MNTN reports none) = (GAAP pre-tax income + SBC + amortization of acquired intangibles
  + one-off items) x (1 - 25% normalized tax) / diluted shares.
  "Street-style" EPS (to compare with the 2-analyst 'normalized' consensus) also adds back capitalized-software
  amortization.
- FCF = operating cash flow - capitalized internal-use software (MNTN reports ~no other capex).
"""
from __future__ import annotations

import copy
import csv
import json
import os
from dataclasses import dataclass, field

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
YEARS = [2026, 2027, 2028, 2029, 2030]

PRICE = 10.25             # 2026-10-15 intraday (IBKR last $10.24-10.34) [market data]
PRICE_PRIOR_CLOSE = 9.40  # 2026-10-14 close [market data]
CASH_JUN26 = 237.3        # [reported] Q2'26; no debt
FCF_1H26 = 27.0           # [reported] OCF 34.0 - capitalized software 7.0
BASIC_JUL26 = 74.80       # [reported] 61,892,533 Class A + 12,910,630 Class B (10-Q cover, Jul 31 2026)
DILUTIVE_Q2 = 4.72        # [reported] dilutive securities in Q2'26 diluted EPS
EXCLUDED_SHARES = 1.5     # [estimate] prob.-weighted: ~1.97M note-restricted shares + 1.57M contingent earnout shares
VALUATION_SHARES = BASIC_JUL26 + DILUTIVE_Q2 + EXCLUDED_SHARES   # ~81.0M
BASIC_YE25 = 74.0         # [estimate] (Q4'25 basic WASO 73.84M; Jun-30-26 balance sheet 74.21M [reported])

FY25 = dict(revenue=290.1, cash_ye=210.2, cap_sw=12.5)   # [reported]
CAP_SW_EXISTING_AMORT = {2026: 7.5, 2027: 6.2, 2028: 3.6, 2029: 0.5, 2030: 0.0}  # [reported] 10-K schedule

# FY2025 segment split [estimate] -- PTV $281.9M: small ~14%, mid-sized ~78%, larger/non-SMB ~8%
SEG0 = {
    "small": dict(cust=2600, arpc=15.2),    # ~$39.5M  (CEO: small businesses spend "~$15K a year")
    "mid":   dict(cust=970,  arpc=226.6),   # ~$219.8M (skewed: includes most top-10 customers)
    "upper": dict(cust=62,   arpc=364.5),   # ~$22.6M  (larger / non-SMB)
}


@dataclass
class Scenario:
    name: str
    label: str
    prob: float
    cust_g: dict
    arpc_g: dict
    creative_other: list
    qf_ai: list
    cash_cogs: list               # cost of revenue ex-SBC, ex-amortization, % revenue
    td_cash: list
    sm_cash: list
    ga_cash: list                 # G&A ex-SBC/one-offs, net of other small adj.-EBITDA add-backs
    sbc_pct: list
    buyback_usd: list             # $M; None => payout x FCF
    buyback_payout: float
    buyback_price: list
    ev_ebitda: float
    ev_sales: float
    pe: float
    gross_issuance_m: float = 2.1
    dilution_addon_m: list = field(default_factory=lambda: [4.7, 4.8, 5.2, 5.6, 6.0])
    sbc_split: dict = field(default_factory=lambda: dict(cogs=0.01, td=0.18, sm=0.40, ga=0.41))
    one_offs: list = field(default_factory=lambda: [1.9, 0.5, 0.5, 0.5, 0.5])
    cap_sw_pct: float = 0.043
    wc_pct_of_delta_rev: float = 0.22   # calibrated: OCF/(adj. EBITDA + interest) ran ~79-81% FY25-1H26
    cash_tax_rate: list = field(default_factory=lambda: [0.07, 0.22, 0.25, 0.26, 0.26])  # 1H26 current tax ~18%
    book_tax_rate: float = 0.26
    interest_yield: list = field(default_factory=lambda: [0.035, 0.032, 0.030, 0.030, 0.030])


def run(s: Scenario, no_buyback=False, rev_shock=None, margin_shock=None):
    segs = copy.deepcopy(SEG0)
    rows, prev_rev, basic_end, cash = [], FY25["revenue"], BASIC_YE25, FY25["cash_ye"]
    vintages = {}
    intang_left = 12.7  # acquired intangibles at YE25 [estimate: $11.4M at Jun-26 + ~$1.3M 1H amortization]
    for i, y in enumerate(YEARS):
        seg_out = {}
        for k in segs:
            segs[k]["cust"] *= 1 + s.cust_g[k][i]
            segs[k]["arpc"] *= 1 + s.arpc_g[k][i]
            seg_out[k] = dict(cust=segs[k]["cust"], arpc=segs[k]["arpc"], rev=segs[k]["cust"] * segs[k]["arpc"] / 1000)
        ptv = sum(v["rev"] for v in seg_out.values())
        if rev_shock and y in rev_shock:
            ptv *= 1 + rev_shock[y]
        rev = ptv + s.creative_other[i] + s.qf_ai[i]
        cust = sum(v["cust"] for v in seg_out.values())

        # capitalized software & amortization (half-year convention, 3-year life)
        cap_sw = rev * s.cap_sw_pct
        vintages[y] = cap_sw
        sw_amort = CAP_SW_EXISTING_AMORT[y] + sum(
            (v / 6 if y == vy else v / 3 if vy < y <= vy + 2 else v / 6 if y == vy + 3 else 0.0)
            for vy, v in vintages.items())
        intang_amort = min(2.63, intang_left)
        intang_left -= intang_amort
        d_and_a = sw_amort + intang_amort + 0.3

        margin = 1 - s.cash_cogs[i] - s.td_cash[i] - s.sm_cash[i] - s.ga_cash[i]
        if margin_shock and y in margin_shock:
            margin += margin_shock[y]
        adj_ebitda = rev * margin
        sbc = rev * s.sbc_pct[i]
        one_off = s.one_offs[i]
        op_income = adj_ebitda - sbc - d_and_a - one_off

        sbc_by = {k: sbc * v for k, v in s.sbc_split.items()}
        cogs_gaap = rev * s.cash_cogs[i] + sw_amort + sbc_by["cogs"]
        td_gaap = rev * s.td_cash[i] + sbc_by["td"]
        sm_gaap = rev * s.sm_cash[i] + sbc_by["sm"]
        ga_gaap = rev * s.ga_cash[i] + sbc_by["ga"] + one_off + 0.3 - (margin_shock or {}).get(y, 0) * rev
        gm = 1 - cogs_gaap / rev

        ocf_pre = adj_ebitda - one_off - s.wc_pct_of_delta_rev * (rev - prev_rev)
        bb_target = s.buyback_usd[i]
        interest = cash * s.interest_yield[i]
        for _ in range(4):
            pretax = op_income + interest
            cash_tax = max(0.0, pretax) * s.cash_tax_rate[i]
            ocf = ocf_pre + interest - cash_tax
            fcf = ocf - cap_sw
            if no_buyback:
                bb = 0.0
            elif bb_target is None:
                bb = max(0.0, fcf * s.buyback_payout)
            else:
                bb = max(0.0, min(bb_target, cash + fcf - 75.0))  # keep >= $75M (revolver deposit covenant [reported])
            end_cash = cash + fcf - bb
            interest = (cash + end_cash) / 2.0 * s.interest_yield[i]
        pretax = op_income + interest
        book_tax = pretax * s.book_tax_rate
        net_income = pretax - book_tax
        bb_shares = bb / s.buyback_price[i]
        basic_start = basic_end
        basic_end = basic_start + s.gross_issuance_m - bb_shares
        diluted = (basic_start + basic_end) / 2.0 + s.dilution_addon_m[i]
        diluted_end = basic_end + s.dilution_addon_m[i] + EXCLUDED_SHARES
        adj_ni = (pretax + sbc + intang_amort + one_off) * 0.75
        street_ni = (pretax + sbc + intang_amort + sw_amort + one_off) * 0.75
        rows.append(dict(
            year=y, revenue=rev, growth=rev / prev_rev - 1, ptv=ptv,
            small_rev=seg_out["small"]["rev"], mid_rev=seg_out["mid"]["rev"], upper_rev=seg_out["upper"]["rev"],
            small_cust=seg_out["small"]["cust"], mid_cust=seg_out["mid"]["cust"], upper_cust=seg_out["upper"]["cust"],
            small_arpc=seg_out["small"]["arpc"], mid_arpc=seg_out["mid"]["arpc"], upper_arpc=seg_out["upper"]["arpc"],
            customers=cust, rev_per_cust_k=ptv / cust * 1000, creative_other=s.creative_other[i], qf_ai=s.qf_ai[i],
            gross_margin=gm, cash_gross_margin=1 - s.cash_cogs[i], td_pct=td_gaap / rev, sm_pct=sm_gaap / rev,
            ga_pct=ga_gaap / rev, sbc=sbc, sbc_pct=s.sbc_pct[i], d_and_a=d_and_a, sw_amort=sw_amort,
            intang_amort=intang_amort, one_off=one_off, adj_ebitda=adj_ebitda, adj_ebitda_margin=adj_ebitda / rev,
            op_income=op_income, op_margin=op_income / rev, interest=interest, pretax=pretax, book_tax=book_tax,
            cash_tax=cash_tax, net_income=net_income, basic_end=basic_end, diluted=diluted, diluted_end=diluted_end,
            gaap_eps=net_income / diluted, adj_eps=adj_ni / diluted, street_eps=street_ni / diluted,
            ocf=ocf, cap_sw=cap_sw, fcf=fcf, fcf_ps=fcf / diluted, fcf_margin=fcf / rev, fcf_after_sbc=fcf - sbc,
            buyback=bb, buyback_shares=bb_shares, cash_end=end_cash,
        ))
        cash, prev_rev = end_cash, rev
    return dict(scenario=s.name, label=s.label, prob=s.prob, rows=rows, s=s)


# ---------------------------------------------------------------------------------------------
# Scenarios. Probabilities tie to the verdict panel (avg.: Victim ~13%, At Risk ~45%, Neutral ~32%,
# Beneficiary ~9%, Winner ~1%): Bear = Victim + the worse half of At Risk; Base = At Risk/Neutral;
# Bull = Beneficiary/Winner + the best of Neutral.
# ---------------------------------------------------------------------------------------------
BASE = Scenario(
    name="Base", prob=0.55,
    label="At Risk / Neutral: growth fades to ~10% by 2030; modest take-rate give-back; margins short of the 35-40% target",
    cust_g=dict(small=[0.42, 0.24, 0.17, 0.13, 0.10], mid=[0.16, 0.13, 0.105, 0.09, 0.075], upper=[0.25, 0.20, 0.16, 0.13, 0.11]),
    arpc_g=dict(small=[-0.05, -0.035, -0.03, -0.01, 0.00], mid=[0.045, 0.035, 0.02, 0.02, 0.015], upper=[0.04, 0.04, 0.035, 0.03, 0.03]),
    creative_other=[3.3, 1.8, 1.8, 1.8, 1.8], qf_ai=[0.0, 0.5, 1.0, 2.0, 3.0],
    cash_cogs=[0.158, 0.162, 0.166, 0.170, 0.172],
    td_cash=[0.180, 0.180, 0.177, 0.174, 0.171],
    sm_cash=[0.275, 0.270, 0.265, 0.260, 0.255],
    ga_cash=[0.105, 0.098, 0.092, 0.086, 0.087],
    sbc_pct=[0.075, 0.068, 0.065, 0.063, 0.060],
    buyback_usd=[25.0, 75.0, None, None, None], buyback_payout=0.40, buyback_price=[10.5, 12.0, 13.5, 15.0, 16.5],
    ev_ebitda=6.5, ev_sales=1.9, pe=12.0,
)

BULL = Scenario(
    name="Bull", prob=0.15,
    label="AI Winner: AI funnel converts, MNTN becomes the neutral TV layer for SMBs and their agents",
    cust_g=dict(small=[0.45, 0.33, 0.27, 0.22, 0.18], mid=[0.165, 0.16, 0.16, 0.155, 0.14], upper=[0.25, 0.28, 0.26, 0.24, 0.21]),
    arpc_g=dict(small=[-0.05, -0.01, 0.01, 0.02, 0.02], mid=[0.04, 0.045, 0.045, 0.045, 0.04], upper=[0.05, 0.06, 0.06, 0.06, 0.06]),
    creative_other=[3.3, 2.0, 2.0, 2.0, 2.0], qf_ai=[0.0, 2.0, 6.0, 12.0, 18.0],
    cash_cogs=[0.157, 0.159, 0.161, 0.163, 0.165],
    td_cash=[0.178, 0.172, 0.164, 0.156, 0.150],
    sm_cash=[0.273, 0.260, 0.248, 0.236, 0.225],
    ga_cash=[0.103, 0.092, 0.083, 0.076, 0.075],
    sbc_pct=[0.075, 0.066, 0.061, 0.056, 0.052],
    buyback_usd=[25.0, 75.0, None, None, None], buyback_payout=0.50, buyback_price=[11.0, 15.0, 19.0, 23.0, 27.0],
    gross_issuance_m=2.0, dilution_addon_m=[4.8, 6.5, 8.75, 11.0, 13.0],   # perf. options ($3.79, hurdles $25.40+) start vesting
    ev_ebitda=9.5, ev_sales=3.0, pe=18.0,
)

BEAR = Scenario(
    name="Bear", prob=0.30,
    label="AI Victim: platforms/agents capture new SMB TV demand, take rate resets from 2028, mild 2027 SMB slowdown",
    cust_g=dict(small=[0.38, 0.04, -0.04, 0.00, 0.02], mid=[0.15, 0.06, 0.03, 0.04, 0.05], upper=[0.20, 0.05, 0.03, 0.04, 0.05]),
    arpc_g=dict(small=[-0.06, -0.06, -0.05, -0.03, -0.02], mid=[0.05, -0.01, -0.02, -0.01, -0.01], upper=[0.03, -0.01, -0.02, -0.01, -0.01]),
    creative_other=[3.3, 1.5, 1.2, 1.0, 1.0], qf_ai=[0.0, 0.0, 0.0, 0.0, 0.0],
    cash_cogs=[0.159, 0.175, 0.190, 0.198, 0.200],
    td_cash=[0.181, 0.190, 0.190, 0.188, 0.185],
    sm_cash=[0.276, 0.290, 0.290, 0.285, 0.280],
    ga_cash=[0.107, 0.110, 0.115, 0.117, 0.117],
    sbc_pct=[0.076, 0.080, 0.085, 0.085, 0.085],
    buyback_usd=[20.0, 50.0, None, None, None], buyback_payout=0.25, buyback_price=[9.5, 8.5, 7.5, 7.0, 7.0],
    gross_issuance_m=3.5, dilution_addon_m=[4.0, 2.5, 1.5, 1.0, 1.0],
    one_offs=[1.9, 2.0, 3.0, 1.0, 1.0],
    ev_ebitda=4.0, ev_sales=0.8, pe=8.0,
)

SCENARIOS = [BEAR, BASE, BULL]

COE = 0.11            # cost of equity (no debt): small cap, SMB-ad cyclicality, dual class
T_NOW = 2026.79       # Oct 15, 2026
TERMINAL_G = 0.03


def valuation(res):
    """Per share at end-2027 on FY2028 (NTM) metrics with scenario peer multiples; PV to today at COE.
    Uses end-2027 cash and end-2027 diluted shares (incl. excluded shares)."""
    r = {x["year"]: x for x in res["rows"]}
    s = res["s"]
    nc, sh = r[2027]["cash_end"], r[2027]["diluted_end"]
    v_ebitda = (s.ev_ebitda * r[2028]["adj_ebitda"] + nc) / sh
    v_sales = (s.ev_sales * r[2028]["revenue"] + nc) / sh
    v_pe = s.pe * r[2028]["adj_eps"]
    blend = (v_ebitda + v_sales + v_pe) / 3
    t = 2028.0 - T_NOW
    g31 = max(-0.05, r[2030]["growth"] * 0.6)
    v30 = (s.ev_ebitda * r[2030]["adj_ebitda"] * (1 + g31) + r[2030]["cash_end"]) / r[2030]["diluted_end"]
    return dict(ev_ebitda=v_ebitda, ev_sales=v_sales, pe=v_pe, blend=blend, blend_pv=blend / (1 + COE) ** t,
                ev_ebitda_pv=v_ebitda / (1 + COE) ** t, v2030=v30, v2030_pv=v30 / (1 + COE) ** (2031.0 - T_NOW))


def dcf(res, coe=COE):
    """FCF after SBC (SBC treated as a cash cost), unlevered (strip after-tax interest). 2H26 credited as
    FY26 FCF - 1H26 actual - 2H SBC; FY27-30 explicit; growth then fades linearly to 3% by FY35 at the FY30
    margin structure (FCF-after-SBC margin held); Gordon terminal after FY35. Equity = PV + Jun-26 cash."""
    rows = res["rows"]
    r26 = rows[0]
    f_2h26 = (r26["fcf"] - FCF_1H26) - r26["sbc"] * 0.55 - r26["interest"] * 0.5 * 0.75
    pv = f_2h26 / (1 + coe) ** 0.15
    for r in rows[1:]:
        f = r["fcf_after_sbc"] - r["interest"] * 0.75
        pv += f / (1 + coe) ** ((r["year"] + 0.5) - T_NOW)
    last = rows[-1]
    fm = (last["fcf_after_sbc"] - last["interest"] * 0.75) / last["revenue"]
    rev, g30 = last["revenue"], last["growth"]
    f = 0.0
    for j, y in enumerate(range(2031, 2036), start=1):
        g = g30 + (TERMINAL_G - g30) * j / 5.0
        rev *= 1 + g
        f = rev * fm
        pv += f / (1 + coe) ** ((y + 0.5) - T_NOW)
    pv += f * (1 + TERMINAL_G) / (coe - TERMINAL_G) / (1 + coe) ** (2036.0 - T_NOW)
    return (pv + CASH_JUN26) / VALUATION_SHARES


def generic_value(cagr_27_30, margin_2030, rev26=352.0, sbc_pct=0.065, cap_sw_pct=0.043, tax=0.26,
                  wacc=COE, tg=TERMINAL_G, wc=0.22):
    """Generic DCF for the reverse DCF and sensitivity grid: revenue grows at g for FY27-30, then fades
    linearly to 3% by FY35; adj. EBITDA margin moves linearly from 28% (FY26) to M (FY30), then held.
    FCF after SBC = EBITDA - SBC - tax on EBIT - capitalized software - working capital."""
    m0, prev, pv, f = 0.28, rev26, 0.0, 0.0
    for k, y in enumerate(range(2027, 2036)):
        if y <= 2030:
            g, m = cagr_27_30, m0 + (margin_2030 - m0) * (k + 1) / 4.0
        else:
            g, m = cagr_27_30 + (tg - cagr_27_30) * (y - 2030) / 5.0, margin_2030
        rev = prev * (1 + g)
        ebitda = rev * m
        ebit = ebitda - rev * sbc_pct - rev * cap_sw_pct * 0.95 - 0.3
        f = ebitda - rev * sbc_pct - max(0.0, ebit) * tax - rev * cap_sw_pct - wc * (rev - prev)
        pv += f / (1 + wacc) ** ((y + 0.5) - T_NOW)
        prev = rev
    pv += f * (1 + tg) / (wacc - tg) / (1 + wacc) ** (2036.0 - T_NOW)
    pv += 34.0 / (1 + wacc) ** 0.15      # 2H26 FCF after SBC (base case)
    return (pv + CASH_JUN26) / VALUATION_SHARES


def solve_growth(price, margin_2030, **kw):
    lo, hi = -0.30, 0.60
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if generic_value(mid, margin_2030, **kw) > price else (mid, hi)
    return (lo + hi) / 2


def fmt(v, kind):
    if kind == "m":
        return f"{v:,.1f}" if v >= 0 else f"({-v:,.1f})"
    if kind == "pct":
        return f"{v*100:.1f}%"
    if kind == "eps":
        return f"${v:.2f}" if v >= 0 else f"(${-v:.2f})"
    if kind == "int":
        return f"{v:,.0f}"
    return str(v)


TABLE_ROWS = [
    ("Revenue ($M)", "revenue", "m", "290.1"),
    ("  y/y growth", "growth", "pct", "28.6% (36.0% ex-ME)"),
    ("  Small business, incl. Express ($M)", "small_rev", "m", "~39.5"),
    ("  Mid-sized ($M)", "mid_rev", "m", "~219.8"),
    ("  Larger / non-SMB, incl. Premium ($M)", "upper_rev", "m", "~22.6"),
    ("  Creative services + QuickFrame AI ($M)", "_creative", "m", "~2.8 (+5.4 Max. Effort)"),
    ("TTM active PTV customers, year-end", "customers", "int", "3,632"),
    ("  small / mid-sized / larger (count)", "_counts", "str", "~2,600 / ~970 / ~62"),
    ("Net PTV revenue per TTM customer ($K)", "rev_per_cust_k", "m", "77.6"),
    ("Gross margin (GAAP)", "gross_margin", "pct", "77.2%"),
    ("T&D % rev (GAAP, incl. SBC)", "td_pct", "pct", "17.0%"),
    ("S&M % rev (GAAP, incl. SBC)", "sm_pct", "pct", "31.2%"),
    ("G&A % rev (GAAP, incl. SBC)", "ga_pct", "pct", "19.9%"),
    ("SBC ($M)", "sbc", "m", "31.7"),
    ("  SBC % rev", "sbc_pct", "pct", "10.9%"),
    ("Adj. EBITDA ($M)", "adj_ebitda", "m", "68.0"),
    ("  Adj. EBITDA margin", "adj_ebitda_margin", "pct", "23.4%"),
    ("GAAP operating income ($M)", "op_income", "m", "24.0"),
    ("  GAAP operating margin", "op_margin", "pct", "8.3%"),
    ("Interest income ($M)", "interest", "m", "3.5"),
    ("Book tax / cash tax ($M)", "_tax", "str", "(9.6) VA-release benefit / 2.7"),
    ("GAAP net income ($M)", "net_income", "m", "(6.4)"),
    ("Diluted shares, avg. (M)", "diluted", "m", "50.9 (79.7 in Q4)"),
    ("GAAP EPS", "gaap_eps", "eps", "($0.13); ~$0.26 normalized"),
    ("Adjusted EPS (ours)", "adj_eps", "eps", "~$0.60 pro forma"),
    ("  Street-style EPS (also ex cap.-software amort.)", "street_eps", "eps", "-"),
    ("Free cash flow ($M)", "fcf", "m", "44.0"),
    ("FCF per diluted share", "fcf_ps", "eps", "~$0.55 pro forma"),
    ("FCF after SBC ($M)", "fcf_after_sbc", "m", "12.3"),
    ("Buybacks ($M) / shares retired (M)", "_bb", "str", "0"),
    ("Year-end cash, no debt ($M)", "cash_end", "m", "210.2"),
]


def scenario_table(res):
    rows = res["rows"]
    out = ["| | FY2025A | " + " | ".join(f"FY{r['year']}E" for r in rows) + " |", "|---|---|" + "---|" * len(rows)]
    for label, key, kind, a in TABLE_ROWS:
        if key == "_creative":
            vals = [fmt(r["creative_other"] + r["qf_ai"], "m") for r in rows]
        elif key == "_counts":
            vals = [f"{r['small_cust']:,.0f} / {r['mid_cust']:,.0f} / {r['upper_cust']:,.0f}" for r in rows]
        elif key == "_tax":
            vals = [f"{r['book_tax']:.1f} / {r['cash_tax']:.1f}" for r in rows]
        elif key == "_bb":
            vals = [f"{r['buyback']:.0f} / {r['buyback_shares']:.1f}" for r in rows]
        else:
            vals = [fmt(r[key], kind) for r in rows]
        out.append(f"| {label} | {a} | " + " | ".join(vals) + " |")
    return "\n".join(out)


def main():
    os.makedirs(OUT, exist_ok=True)
    results = [run(s) for s in SCENARIOS]
    md = [f"Model v3. Price ${PRICE:.2f} (prior close ${PRICE_PRIOR_CLOSE:.2f}). Cost of equity {COE:.0%}. Terminal growth "
          f"{TERMINAL_G:.0%} after a 5-year fade. Valuation share base {VALUATION_SHARES:.1f}M (basic + dilutive + excluded).\n"
          "FY25 GAAP net loss includes $43.5M of IPO-related fair-value/extinguishment charges and a $9.6M tax benefit "
          "from the valuation-allowance release (Q4'25); normalized FY25 EPS = (24.0 + 3.5) x 0.74 / 79.7M = ~$0.26.\n"]
    summary = {}
    for res in results:
        v = valuation(res)
        d = dcf(res)
        nb = run(res["s"], no_buyback=True)
        summary[res["scenario"]] = dict(prob=res["prob"], label=res["label"], dcf=d, **v,
                                        eps_2030_no_buyback=nb["rows"][-1]["gaap_eps"])
        md.append(f"### {res['scenario']} case ({res['prob']:.0%}): {res['label']}\n")
        md.append(scenario_table(res))
        s = res["s"]
        md.append(
            f"\nValuation at end-2027 on FY28E (PV today at {COE:.0%}): {s.ev_ebitda}x EV/EBITDA ${v['ev_ebitda']:.2f}; "
            f"{s.ev_sales}x EV/Sales ${v['ev_sales']:.2f}; {s.pe:.0f}x adj. P/E ${v['pe']:.2f}; blend ${v['blend']:.2f} "
            f"(PV ${v['blend_pv']:.2f}). 2030 exit at {s.ev_ebitda}x FY31E EBITDA ${v['v2030']:.2f} (PV ${v['v2030_pv']:.2f}). "
            f"DCF ${d:.2f}. 2030 GAAP EPS with no buybacks: {fmt(nb['rows'][-1]['gaap_eps'], 'eps')}.\n")
    keys = ["revenue", "adj_ebitda", "adj_ebitda_margin", "op_income", "gaap_eps", "adj_eps", "street_eps", "fcf", "fcf_ps"]
    pw = {y: {k: sum(res["prob"] * res["rows"][i][k] for res in results) for k in keys} for i, y in enumerate(YEARS)}
    md.append("### Probability-weighted (30% Bear / 55% Base / 15% Bull)\n")
    md.append("| | " + " | ".join(f"FY{y}E" for y in YEARS) + " |")
    md.append("|---|" + "---|" * len(YEARS))
    for k, lab, kind in [("revenue", "Revenue ($M)", "m"), ("adj_ebitda", "Adj. EBITDA ($M)", "m"),
                         ("op_income", "GAAP operating income ($M)", "m"), ("gaap_eps", "GAAP EPS", "eps"),
                         ("adj_eps", "Adjusted EPS", "eps"), ("fcf_ps", "FCF/share", "eps")]:
        md.append(f"| {lab} | " + " | ".join(fmt(pw[y][k], kind) for y in YEARS) + " |")
    pwv = {k: sum(summary[n]["prob"] * summary[n][k] for n in ["Bear", "Base", "Bull"])
           for k in ["blend", "blend_pv", "ev_ebitda_pv", "v2030_pv", "dcf"]}
    md.append(f"\nProbability-weighted value per share: multiples blend at end-2027 ${pwv['blend']:.2f} (PV ${pwv['blend_pv']:.2f}); "
              f"EV/EBITDA-only PV ${pwv['ev_ebitda_pv']:.2f}; 2030-exit PV ${pwv['v2030_pv']:.2f}; DCF ${pwv['dcf']:.2f}.\n")
    # market-implied bear weight
    b, ba = summary["Bear"], summary["Base"]
    w_mult = (ba["blend_pv"] - PRICE) / (ba["blend_pv"] - b["blend_pv"])
    w_dcf = (ba["dcf"] - PRICE) / (ba["dcf"] - b["dcf"])
    md.append(f"Market-implied weight on Bear vs Base at ${PRICE:.2f}: {w_mult:.0%} (multiples PV) / {w_dcf:.0%} (DCF).\n")
    # discount-rate sensitivity
    md.append("DCF by cost of equity: " + "; ".join(
        f"{c:.0%}: Bear ${dcf(results[0], c):.2f} / Base ${dcf(results[1], c):.2f} / Bull ${dcf(results[2], c):.2f}" for c in [0.10, 0.11, 0.12]) + "\n")

    md.append("### Stress tests on the Base case\n")
    stress = {
        "Sharp 2027 SMB ad recession (PTV -18% vs base in FY27, -9% FY28, -4% FY29; margin -5pts FY27, -2pts FY28)":
            dict(rev_shock={2027: -0.18, 2028: -0.09, 2029: -0.04, 2030: -0.02}, margin_shock={2027: -0.05, 2028: -0.02}),
        "Take-rate reset: -5 pts of take rate from FY28 (~-10% revenue; half of the ~7.5pt margin hit flexed out)":
            dict(rev_shock={2028: -0.10, 2029: -0.10, 2030: -0.10}, margin_shock={2028: -0.04, 2029: -0.035, 2030: -0.03}),
        "No buybacks at all": dict(no_buyback=True),
    }
    md.append("| Stress | FY27 revenue | FY30 revenue | FY30 adj. EBITDA | FY30 GAAP EPS | FY30 FCF/share | DCF $/sh |")
    md.append("|---|---|---|---|---|---|---|")
    br = results[1]["rows"]
    md.append(f"| Base (no stress) | {br[1]['revenue']:.0f} | {br[-1]['revenue']:.0f} | {br[-1]['adj_ebitda']:.0f} | "
              f"{fmt(br[-1]['gaap_eps'],'eps')} | {fmt(br[-1]['fcf_ps'],'eps')} | ${summary['Base']['dcf']:.2f} |")
    for name, kw in stress.items():
        rr = run(BASE, **kw)
        r = rr["rows"]
        md.append(f"| {name} | {r[1]['revenue']:.0f} | {r[-1]['revenue']:.0f} | {r[-1]['adj_ebitda']:.0f} | "
                  f"{fmt(r[-1]['gaap_eps'],'eps')} | {fmt(r[-1]['fcf_ps'],'eps')} | ${dcf(rr):.2f} |")
    md.append("")

    md.append("### Reverse DCF (generic path: FY26 revenue $352M; adj. EBITDA margin 28% -> M by FY30)\n")
    md.append("| 2030 adj. EBITDA margin | FY27-30 revenue CAGR implied at $10.25 | at $9.40 | at 10% CoE | at 12% CoE |")
    md.append("|---|---|---|---|---|")
    rdcf = {}
    for m in [0.22, 0.25, 0.28, 0.30, 0.325]:
        vals = (solve_growth(PRICE, m), solve_growth(PRICE_PRIOR_CLOSE, m), solve_growth(PRICE, m, wacc=0.10), solve_growth(PRICE, m, wacc=0.12))
        rdcf[m] = vals
        md.append(f"| {m:.1%} | " + " | ".join(f"{g*100:+.1f}%" for g in vals) + " |")
    md.append("")
    growths = [-0.05, 0.0, 0.05, 0.10, 0.15, 0.20, 0.25]
    margins = [0.20, 0.25, 0.30, 0.35, 0.40]
    md.append("### Sensitivity: DCF value per share by FY27-30 revenue CAGR (rows) x FY30 adj. EBITDA margin (columns)\n")
    md.append("| Revenue CAGR FY27-30 \\ FY30 margin | " + " | ".join(f"{m:.0%}" for m in margins) + " |")
    md.append("|---|" + "---|" * len(margins))
    for g in growths:
        md.append(f"| {g:+.0%} (FY30 rev ${352*(1+g)**4:,.0f}M) | " + " | ".join(f"${generic_value(g, m):.2f}" for m in margins) + " |")
    md.append("")
    md.append("### Sensitivity: value per share at end-2027 by EV/EBITDA multiple (rows) x FY28 adj. EBITDA (columns)\n")
    ebitdas = [70, 90, 110, 140, 170, 200]
    mults = [3, 4, 5, 6.5, 8, 9.5]
    nc, sh = br[1]["cash_end"], br[1]["diluted_end"]
    md.append("| EV/EBITDA \\ FY28 adj. EBITDA ($M) | " + " | ".join(str(e) for e in ebitdas) + " |")
    md.append("|---|" + "---|" * len(ebitdas))
    for m in mults:
        md.append(f"| {m}x | " + " | ".join(f"${(m*e+nc)/sh:.2f}" for e in ebitdas) + " |")
    md.append(f"\n(Base-case end-2027 net cash ${nc:.0f}M and {sh:.1f}M diluted shares held constant; not discounted.)\n")

    text = "\n".join(md)
    with open(os.path.join(OUT, "model_output.md"), "w") as f:
        f.write(text + "\n")
    for res in results:
        with open(os.path.join(OUT, f"scenario_{res['scenario'].lower()}.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(res["rows"][0].keys()))
            w.writeheader()
            for r in res["rows"]:
                w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})
    with open(os.path.join(OUT, "summary.json"), "w") as f:
        json.dump({"scenarios": summary, "prob_weighted_values": pwv, "prob_weighted_rows": pw,
                   "market_implied_bear_weight": {"multiples": w_mult, "dcf": w_dcf},
                   "reverse_dcf": {str(k): v for k, v in rdcf.items()}}, f, indent=1, default=float)
    print(text)
    return results, summary


if __name__ == "__main__":
    main()
