"""
MNTN, Inc. (NYSE: MNTN) - driver-based model, FY2026E-FY2030E, three scenarios + stress tests.

Run:  python3 mntn/model/mntn_model.py
      -> writes mntn/model/output/model_output.md, scenario_*.csv, summary.json

Conventions
- $M unless noted. Revenue is NET of media cost (MNTN reports as an agent; 10-K FY2025 Note 2).
- Every assumption below is an [estimate] unless tagged [reported]/[guidance]/[consensus].
- Revenue build = sum over customer-size segments of
      (TTM active Performance TV customers) x (net revenue per TTM customer)
  + creative/QuickFrame services + QuickFrame AI subscription monetization.
  MNTN discloses only TOTAL TTM active customers (3,632 at FY25 [reported]) and the small-business share of
  PTV revenue (~6% FY24 -> 12% Q1'25 [reported, 424B4] -> ~15% Q3'25 [CEO via AdExchanger]); SMBs were ~92% of
  FY24 PTV revenue [reported]. The FY25 count split below is therefore an [estimate]; segment averages are
  means over a highly skewed distribution (top-10 customers = ~17% of FY25 revenue [reported]).
- Adjusted EBITDA follows the company definition (adds back SBC, D&A, fair-value marks, acquisition-related
  legal, restructuring).
- Adjusted EPS (ours; MNTN reports no non-GAAP EPS) = (GAAP pre-tax income + SBC + amortization of acquired
  intangibles + one-off items) x (1 - 25% normalized tax) / diluted shares.
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

PRICE = 10.25            # 2026-10-15 intraday (IBKR last $10.24-10.34) [market data]
PRICE_PRIOR_CLOSE = 9.40  # 2026-10-14 close [market data]
CASH_JUN26 = 237.3       # [reported] Q2'26 10-Q; no debt
BASIC_JUL26 = 74.80      # [reported] 61,892,533 Class A + 12,910,630 Class B (10-Q cover, Jul 31 2026)
DILUTED_Q2 = 78.64       # [reported] Q2'26 diluted weighted average
BASIC_YE25 = 74.0        # [estimate] (Q4'25 basic WASO 73.84M; Jun-30-26 balance sheet 74.21M [reported])

FY25 = dict(  # [reported] FY2025 (10-K / Q4'25 8-K)
    revenue=290.1, revenue_exME=284.7, ptv=281.9, gross_margin=0.772, adj_ebitda=68.0, sbc=31.7,
    d_and_a=9.9, op_income=24.0, interest=3.5, net_income=-6.4, gaap_eps=-0.13, ocf=56.5, cap_sw=12.5,
    fcf=44.0, ttm_customers=3632, cash_ye=210.2,
)

# FY2025 segment split [estimate] -- calibrated to: PTV $281.9M; small ~13% of PTV, mid-sized ~79%, larger ~8%
SEG0 = {
    "small": dict(cust=2550, arpc=14.35),   # ~$36.6M  (CEO: small businesses spend "~$15K a year")
    "mid":   dict(cust=1020, arpc=218.3),   # ~$222.7M ("deep six figures" at the top; skewed)
    "upper": dict(cust=62,   arpc=364.5),   # ~$22.6M  (upper mid-market / Premium)
}


@dataclass
class Scenario:
    name: str
    label: str
    prob: float
    cust_g: dict                  # TTM customer growth by segment, 2026..2030
    arpc_g: dict                  # net revenue per TTM customer growth by segment
    creative_other: list          # QuickFrame human-creator services, breakage ($M)
    qf_ai: list                   # QuickFrame AI subscription monetization ($M)
    gross_margin: list            # GAAP gross margin
    td_cash: list                 # T&D ex-SBC, % revenue
    sm_cash: list                 # S&M ex-SBC, % revenue
    ga_cash: list                 # G&A ex-SBC/one-offs, % revenue (net of other adj.-EBITDA add-backs)
    sbc_pct: list
    buyback_usd: list             # $M per year; None => payout x FCF
    buyback_payout: float
    buyback_price: list
    ev_ebitda: float              # valuation multiples applied to NTM (FY2028) at end-2027
    ev_sales: float
    pe: float
    gross_issuance_m: float = 1.6
    dilution_addon_m: list = field(default_factory=lambda: [4.5, 4.2, 4.0, 4.0, 4.0])
    cash_cogs_addback: float = 0.025  # (cap-SW amortization + COGS SBC)/rev: cash GM = GAAP GM + this
    sbc_split: dict = field(default_factory=lambda: dict(cogs=0.01, td=0.18, sm=0.40, ga=0.41))
    one_offs: list = field(default_factory=lambda: [1.9, 0.5, 0.5, 0.5, 0.5])
    cap_sw_pct: float = 0.043
    wc_pct_of_delta_rev: float = 0.18   # calibrated: OCF/(adj. EBITDA + interest) ran ~79-83% FY25-1H26
    cash_tax_rate: list = field(default_factory=lambda: [0.05, 0.12, 0.20, 0.24, 0.25])
    book_tax_rate: float = 0.26
    interest_yield: list = field(default_factory=lambda: [0.035, 0.032, 0.030, 0.030, 0.030])


def run(s: Scenario, no_buyback: bool = False, rev_shock: dict | None = None, margin_shock: dict | None = None) -> dict:
    segs = copy.deepcopy(SEG0)
    rows = []
    prev_rev = FY25["revenue"]
    basic_end = BASIC_YE25
    cash = FY25["cash_ye"]
    cap_sw_hist = [9.9, 12.5]          # FY24, FY25 [reported]
    intang_left = 12.7                 # acquired intangibles at YE25 [estimate from $11.4M at Jun-26 + 1H amort.]
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

        gm = s.gross_margin[i]
        cash_gm = gm + s.cash_cogs_addback
        margin = cash_gm - s.td_cash[i] - s.sm_cash[i] - s.ga_cash[i]
        if margin_shock and y in margin_shock:
            margin += margin_shock[y]
        adj_ebitda = rev * margin
        sbc = rev * s.sbc_pct[i]
        cap_sw = rev * s.cap_sw_pct
        cap_sw_hist.append(cap_sw)
        cap_sw_amort = sum(cap_sw_hist[-4:-1]) / 3.0          # 3-yr straight line on prior-year vintages
        intang_amort = min(2.63, intang_left)
        intang_left -= intang_amort
        d_and_a = cap_sw_amort + intang_amort + 0.3
        one_off = s.one_offs[i]
        op_income = adj_ebitda - sbc - d_and_a - one_off

        sbc_by = {k: sbc * v for k, v in s.sbc_split.items()}
        td_gaap = rev * s.td_cash[i] + sbc_by["td"]
        sm_gaap = rev * s.sm_cash[i] + sbc_by["sm"]
        ga_gaap = rev * s.ga_cash[i] + sbc_by["ga"] + one_off + 0.3 + (margin_shock or {}).get(y, 0) * 0  # shocks hit EBITDA
        cogs_gaap = rev * (1 - gm)

        ocf_pre = adj_ebitda - one_off - s.wc_pct_of_delta_rev * (rev - prev_rev)
        bb_target = 0.0 if no_buyback else s.buyback_usd[i]
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
                bb = min(bb_target, cash + fcf - 75.0)   # keep >= $75M (revolver deposit covenant [reported])
            end_cash = cash + fcf - bb
            interest = (cash + end_cash) / 2.0 * s.interest_yield[i]
        pretax = op_income + interest
        book_tax = pretax * s.book_tax_rate
        net_income = pretax - book_tax
        bb_shares = bb / s.buyback_price[i]
        basic_start = basic_end
        basic_end = basic_start + s.gross_issuance_m - bb_shares
        diluted = (basic_start + basic_end) / 2.0 + s.dilution_addon_m[i]
        eps = net_income / diluted
        adj_ni = (pretax + sbc + intang_amort + one_off) * 0.75
        rows.append(dict(
            year=y, revenue=rev, growth=rev / prev_rev - 1, ptv=ptv,
            small_rev=seg_out["small"]["rev"], mid_rev=seg_out["mid"]["rev"], upper_rev=seg_out["upper"]["rev"],
            small_cust=seg_out["small"]["cust"], mid_cust=seg_out["mid"]["cust"], upper_cust=seg_out["upper"]["cust"],
            small_arpc=seg_out["small"]["arpc"], mid_arpc=seg_out["mid"]["arpc"], upper_arpc=seg_out["upper"]["arpc"],
            customers=cust, rev_per_cust_k=ptv / cust * 1000, creative_other=s.creative_other[i], qf_ai=s.qf_ai[i],
            gross_margin=gm, cogs_pct=cogs_gaap / rev, td_pct=td_gaap / rev, sm_pct=sm_gaap / rev, ga_pct=ga_gaap / rev,
            sbc=sbc, sbc_pct=s.sbc_pct[i], d_and_a=d_and_a, one_off=one_off,
            adj_ebitda=adj_ebitda, adj_ebitda_margin=adj_ebitda / rev, op_income=op_income, op_margin=op_income / rev,
            interest=interest, pretax=pretax, book_tax=book_tax, cash_tax=cash_tax, net_income=net_income,
            basic_end=basic_end, diluted=diluted, gaap_eps=eps, adj_eps=adj_ni / diluted,
            ocf=ocf, cap_sw=cap_sw, fcf=fcf, fcf_ps=fcf / diluted, fcf_margin=fcf / rev, fcf_after_sbc=fcf - sbc,
            buyback=bb, buyback_shares=bb_shares, cash_end=end_cash,
        ))
        cash = end_cash
        prev_rev = rev
    return dict(scenario=s.name, label=s.label, prob=s.prob, rows=rows, s=s)


# ---------------------------------------------------------------------------------------------
# Scenarios (probabilities tie to the verdict: At Risk ~45%, Neutral ~32%, Victim ~13%, Beneficiary/Winner ~10%)
# ---------------------------------------------------------------------------------------------
BASE = Scenario(
    name="Base", label="At Risk / Neutral: growth fades to low-teens, modest take-rate give-back from 2028", prob=0.60,
    cust_g=dict(small=[0.40, 0.28, 0.20, 0.15, 0.12], mid=[0.19, 0.125, 0.11, 0.095, 0.08], upper=[0.25, 0.20, 0.17, 0.14, 0.12]),
    arpc_g=dict(small=[-0.07, -0.02, 0.00, 0.01, 0.01], mid=[0.018, 0.03, 0.025, 0.025, 0.025], upper=[0.03, 0.04, 0.04, 0.04, 0.04]),
    creative_other=[3.3, 1.8, 1.8, 1.8, 1.8], qf_ai=[0.0, 0.0, 0.0, 0.0, 0.0],
    gross_margin=[0.805, 0.800, 0.795, 0.790, 0.790],
    td_cash=[0.175, 0.175, 0.170, 0.165, 0.160],
    sm_cash=[0.280, 0.270, 0.260, 0.252, 0.245],
    ga_cash=[0.0950, 0.0900, 0.0850, 0.0830, 0.0820],
    sbc_pct=[0.076, 0.068, 0.065, 0.063, 0.060],
    buyback_usd=[25.0, 75.0, None, None, None], buyback_payout=0.40,
    buyback_price=[10.5, 12.0, 14.0, 16.0, 18.0],
    ev_ebitda=7.0, ev_sales=2.0, pe=13.0,
)

BULL = Scenario(
    name="Bull", label="AI Winner: AI funnel converts, MNTN becomes the neutral TV layer for SMBs and their agents", prob=0.15,
    cust_g=dict(small=[0.45, 0.38, 0.30, 0.24, 0.20], mid=[0.20, 0.16, 0.16, 0.15, 0.14], upper=[0.25, 0.32, 0.28, 0.25, 0.22]),
    arpc_g=dict(small=[-0.06, 0.01, 0.03, 0.03, 0.03], mid=[0.019, 0.045, 0.05, 0.05, 0.045], upper=[0.04, 0.06, 0.06, 0.06, 0.06]),
    creative_other=[3.3, 2.0, 2.0, 2.0, 2.0], qf_ai=[0.0, 2.0, 6.0, 12.0, 18.0],
    gross_margin=[0.807, 0.805, 0.805, 0.800, 0.800],
    td_cash=[0.174, 0.168, 0.160, 0.152, 0.145],
    sm_cash=[0.277, 0.258, 0.242, 0.228, 0.218],
    ga_cash=[0.0935, 0.0840, 0.0760, 0.0700, 0.0640],
    sbc_pct=[0.075, 0.065, 0.060, 0.055, 0.050],
    buyback_usd=[25.0, 75.0, None, None, None], buyback_payout=0.50,
    buyback_price=[11.0, 15.0, 20.0, 25.0, 30.0],
    gross_issuance_m=1.4, dilution_addon_m=[4.8, 5.5, 6.0, 7.0, 8.0],
    ev_ebitda=11.0, ev_sales=3.5, pe=20.0,
)

BEAR = Scenario(
    name="Bear", label="AI Victim: walled gardens/agents take the SMB funnel, take rate resets from 2028", prob=0.25,
    cust_g=dict(small=[0.38, 0.12, 0.00, -0.06, -0.06], mid=[0.18, 0.09, 0.06, 0.01, -0.01], upper=[0.20, 0.06, 0.02, -0.02, -0.03]),
    arpc_g=dict(small=[-0.075, -0.05, -0.04, -0.04, -0.03], mid=[0.025, 0.00, -0.02, -0.03, -0.03], upper=[0.02, -0.01, -0.03, -0.03, -0.03]),
    creative_other=[3.3, 1.5, 1.2, 1.0, 1.0], qf_ai=[0.0, 0.0, 0.0, 0.0, 0.0],
    gross_margin=[0.803, 0.790, 0.775, 0.765, 0.760],
    td_cash=[0.176, 0.185, 0.190, 0.190, 0.190],
    sm_cash=[0.281, 0.290, 0.295, 0.295, 0.290],
    ga_cash=[0.0970, 0.1000, 0.1050, 0.1080, 0.1100],
    sbc_pct=[0.077, 0.080, 0.085, 0.088, 0.090],
    buyback_usd=[20.0, 50.0, None, None, None], buyback_payout=0.25,
    buyback_price=[9.5, 8.5, 7.5, 6.5, 6.0],
    gross_issuance_m=2.0, dilution_addon_m=[4.0, 2.5, 1.5, 1.0, 1.0],
    one_offs=[1.9, 2.0, 3.0, 1.0, 1.0],
    ev_ebitda=4.0, ev_sales=0.8, pe=8.0,
)

SCENARIOS = [BEAR, BASE, BULL]

COE = 0.11            # cost of equity (no debt): small cap, SMB-ad cyclicality, dual class
T_NOW = 2026.79       # Oct 15, 2026
TERMINAL_G = 0.03


def valuation(res):
    """Value per share at end-2027 on FY2028 (NTM) metrics with scenario peer multiples, PV'd to today at COE."""
    r = {x["year"]: x for x in res["rows"]}
    s = res["s"]
    t = 2028.0 - T_NOW
    net_cash = r[2027]["cash_end"]
    sh = r[2028]["diluted"]
    v_ebitda = (s.ev_ebitda * r[2028]["adj_ebitda"] + net_cash) / sh
    v_sales = (s.ev_sales * r[2028]["revenue"] + net_cash) / sh
    v_pe = s.pe * r[2028]["adj_eps"] + net_cash / sh * 0.0  # P/E already embeds interest on cash
    blend = (v_ebitda + v_sales + v_pe) / 3
    pv = lambda v: v / (1 + COE) ** t
    # 2030 exit: same EV/EBITDA on FY2031E (= FY2030 x (1 + half of 2030 growth, floored -5%))
    g31 = max(-0.05, r[2030]["growth"] * 0.5)
    v30 = (s.ev_ebitda * r[2030]["adj_ebitda"] * (1 + g31) + r[2030]["cash_end"]) / r[2030]["diluted"]
    return dict(ev_ebitda=v_ebitda, ev_sales=v_sales, pe=v_pe, blend=blend, blend_pv=pv(blend),
                ev_ebitda_pv=pv(v_ebitda), v2030=v30, v2030_pv=v30 / (1 + COE) ** (2031.0 - T_NOW))


def dcf(res):
    """FCF after SBC (SBC treated as a cash cost), unlevered (strip after-tax interest), Q4'26-2030 explicit
    + Gordon terminal at min(3%, half of 2030 growth). Equity = PV + Jun-26 cash."""
    rows = res["rows"]
    pv = 0.0
    for r in rows:
        f = r["fcf_after_sbc"] - r["interest"] * 0.75
        frac = 0.21 if r["year"] == 2026 else 1.0
        t = (r["year"] + 0.5) - T_NOW if r["year"] > 2026 else 0.1
        pv += frac * f / (1 + COE) ** t
    last = rows[-1]
    f_last = last["fcf_after_sbc"] - last["interest"] * 0.75
    g = min(TERMINAL_G, max(-0.03, last["growth"] * 0.5))
    pv += f_last * (1 + g) / (COE - g) / (1 + COE) ** (2031.0 - T_NOW)
    return (pv + CASH_JUN26 + 8.0) / DILUTED_Q2   # + ~Q3'26 FCF retained (approx.)


def generic_value(cagr_27_30, margin_2030, rev26=350.0, sbc_pct=0.065, cap_sw_pct=0.043, tax=0.25,
                  wacc=COE, tg=TERMINAL_G, shares=DILUTED_Q2, net_cash=CASH_JUN26 + 8.0, wc=0.18):
    """Generic DCF used for the reverse DCF and the sensitivity grid: revenue grows at g for FY27-30, then fades
    linearly to 3% by FY35; adj. EBITDA margin moves linearly from 28% (FY26) to M (FY30) and is then held.
    FCF after SBC = EBITDA - SBC - cash tax on EBIT - capitalized software - working capital."""
    m0, prev, pv, f = 0.28, rev26, 0.0, 0.0
    for k, y in enumerate(range(2027, 2036)):
        if y <= 2030:
            g = cagr_27_30
            m = m0 + (margin_2030 - m0) * (k + 1) / 4.0
        else:
            g = cagr_27_30 + (tg - cagr_27_30) * (y - 2030) / 5.0
            m = margin_2030
        rev = prev * (1 + g)
        ebitda = rev * m
        da = rev * cap_sw_pct * 0.95 + 0.3
        ebit = ebitda - rev * sbc_pct - da
        f = ebitda - rev * sbc_pct - max(0.0, ebit) * tax - rev * cap_sw_pct - wc * (rev - prev)
        pv += f / (1 + wacc) ** ((y + 0.5) - T_NOW)
        prev = rev
    pv += f * (1 + tg) / (wacc - tg) / (1 + wacc) ** (2036.0 - T_NOW)
    pv += 12.0 / (1 + wacc) ** 0.1     # ~Q4'26 FCF after SBC
    return (pv + net_cash) / shares


def solve_growth(price, margin_2030, **kw):
    lo, hi = -0.30, 0.60
    for _ in range(100):
        mid = (lo + hi) / 2
        if generic_value(mid, margin_2030, **kw) > price:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def fmt(v, kind):
    if kind == "m":
        return f"{v:,.1f}"
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
    ("  Small business incl. Express ($M)", "small_rev", "m", "~36.6"),
    ("  Mid-sized (Pro) ($M)", "mid_rev", "m", "~222.7"),
    ("  Upper mid-market (Premium) ($M)", "upper_rev", "m", "~22.6"),
    ("  Creative services + QuickFrame AI ($M)", "_creative", "m", "~2.8 (+5.4 Max. Effort)"),
    ("TTM active PTV customers, year-end", "customers", "int", "3,632"),
    ("  small / mid / upper (count)", "_counts", "str", "~2,550 / ~1,020 / ~62"),
    ("Net PTV revenue per TTM customer ($K)", "rev_per_cust_k", "m", "77.6"),
    ("Gross margin", "gross_margin", "pct", "77.2%"),
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
    ("Book tax / cash tax ($M)", "_tax", "str", "(9.6) benefit* / 2.7"),
    ("GAAP net income ($M)", "net_income", "m", "(6.4)*"),
    ("Diluted shares (M)", "diluted", "m", "50.9 (79.7 Q4)"),
    ("GAAP EPS", "gaap_eps", "eps", "($0.13); ~$0.26 normalized*"),
    ("Adjusted EPS (ours)", "adj_eps", "eps", "~$0.60 (pro forma)"),
    ("Free cash flow ($M)", "fcf", "m", "44.0"),
    ("FCF per diluted share", "fcf_ps", "eps", "~$0.55 (pro forma)"),
    ("FCF after SBC ($M)", "fcf_after_sbc", "m", "12.3"),
    ("Buybacks ($M) / shares retired (M)", "_bb", "str", "0"),
    ("Year-end cash, no debt ($M)", "cash_end", "m", "210.2"),
]


def scenario_table(res):
    rows = res["rows"]
    out = ["| | FY2025A | " + " | ".join(f"FY{r['year']}E" for r in rows) + " |",
           "|---|---|" + "---|" * len(rows)]
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
    md = [f"Model v2. Price ${PRICE:.2f} (prior close ${PRICE_PRIOR_CLOSE:.2f}). Cost of equity {COE:.0%}. "
          f"Terminal growth <= {TERMINAL_G:.0%}. *FY25 GAAP includes $43.5M of IPO-related fair-value/extinguishment "
          f"charges and a $9.6M tax benefit from the valuation-allowance release; normalized FY25 EPS = "
          f"(op. income 24.0 + interest 3.5) x 0.74 / 79.7M = ~$0.26.\n"]
    summary = {}
    for res in results:
        v = valuation(res)
        d = dcf(res)
        nb = run(res["s"], no_buyback=True)
        summary[res["scenario"]] = dict(prob=res["prob"], label=res["label"], dcf=d, **v,
                                        eps_2030_no_buyback=nb["rows"][-1]["gaap_eps"],
                                        diluted_2030_no_buyback=nb["rows"][-1]["diluted"])
        md.append(f"### {res['scenario']} case — {res['label']} (probability {res['prob']:.0%})\n")
        md.append(scenario_table(res))
        md.append(
            f"\nValuation (end-2027, on FY28E, PV at {COE:.0%}): {res['s'].ev_ebitda:.0f}x EV/EBITDA ${v['ev_ebitda']:.2f}; "
            f"{res['s'].ev_sales:.1f}x EV/Sales ${v['ev_sales']:.2f}; {res['s'].pe:.0f}x adj. P/E ${v['pe']:.2f}; "
            f"blend ${v['blend']:.2f} (PV ${v['blend_pv']:.2f}). 2030 exit at {res['s'].ev_ebitda:.0f}x FY31E EBITDA "
            f"${v['v2030']:.2f} (PV ${v['v2030_pv']:.2f}). DCF ${d:.2f}. "
            f"No-buyback 2030 GAAP EPS {fmt(nb['rows'][-1]['gaap_eps'], 'eps')} on {nb['rows'][-1]['diluted']:.1f}M shares.\n")
    keys = ["revenue", "adj_ebitda", "adj_ebitda_margin", "gaap_eps", "adj_eps", "fcf_ps"]
    pw = {y: {k: 0.0 for k in keys} for y in YEARS}
    for res in results:
        for r in res["rows"]:
            for k in keys:
                pw[r["year"]][k] += res["prob"] * r[k]
    md.append("### Probability-weighted (25% Bear / 60% Base / 15% Bull)\n")
    md.append("| | " + " | ".join(f"FY{y}E" for y in YEARS) + " |")
    md.append("|---|" + "---|" * len(YEARS))
    for k, lab, kind in [("revenue", "Revenue ($M)", "m"), ("adj_ebitda", "Adj. EBITDA ($M)", "m"),
                         ("gaap_eps", "GAAP EPS", "eps"), ("adj_eps", "Adjusted EPS", "eps"), ("fcf_ps", "FCF/share", "eps")]:
        md.append(f"| {lab} | " + " | ".join(fmt(pw[y][k], kind) for y in YEARS) + " |")
    pwv = {k: sum(summary[n]["prob"] * summary[n][k] for n in summary) for k in ["blend", "blend_pv", "v2030_pv", "dcf", "ev_ebitda_pv"]}
    md.append(f"\nProbability-weighted value per share: multiples blend end-2027 ${pwv['blend']:.2f} (PV ${pwv['blend_pv']:.2f}); "
              f"EV/EBITDA only PV ${pwv['ev_ebitda_pv']:.2f}; 2030-exit PV ${pwv['v2030_pv']:.2f}; DCF ${pwv['dcf']:.2f}.\n")
    summary["prob_weighted"] = pwv
    summary["pw_rows"] = pw

    # Stress tests on the base case
    md.append("### Stress tests on the Base case\n")
    stress = {
        "2027 SMB ad recession (PTV -15% vs base in 2027, -8% 2028; margin -4pts 2027, -2pts 2028)":
            dict(rev_shock={2027: -0.15, 2028: -0.08, 2029: -0.04, 2030: -0.02}, margin_shock={2027: -0.04, 2028: -0.02}),
        "Take-rate reset: -5 points of take rate from 2028 (~-10% revenue, ~-7.5pts margin before cost flex; half flexed)":
            dict(rev_shock={2028: -0.10, 2029: -0.10, 2030: -0.10}, margin_shock={2028: -0.04, 2029: -0.035, 2030: -0.03}),
        "No buyback at all": dict(no_buyback=True),
    }
    md.append("| Stress | FY27 revenue | FY30 revenue | FY30 adj. EBITDA | FY30 GAAP EPS | FY30 FCF/share | DCF $/sh |")
    md.append("|---|---|---|---|---|---|---|")
    base_r = results[1]["rows"]
    md.append(f"| Base (no stress) | {base_r[1]['revenue']:.0f} | {base_r[-1]['revenue']:.0f} | {base_r[-1]['adj_ebitda']:.0f} | "
              f"{fmt(base_r[-1]['gaap_eps'],'eps')} | {fmt(base_r[-1]['fcf_ps'],'eps')} | ${summary['Base']['dcf']:.2f} |")
    for name, kw in stress.items():
        rr = run(BASE, **kw)
        r = rr["rows"]
        md.append(f"| {name} | {r[1]['revenue']:.0f} | {r[-1]['revenue']:.0f} | {r[-1]['adj_ebitda']:.0f} | "
                  f"{fmt(r[-1]['gaap_eps'],'eps')} | {fmt(r[-1]['fcf_ps'],'eps')} | ${dcf(rr):.2f} |")
    md.append("")

    # Reverse DCF & sensitivity
    md.append("### Reverse DCF (generic path; FY26 revenue $350M, adj. EBITDA margin 28% -> M in 2030)\n")
    md.append("| 2030 adj. EBITDA margin | Implied FY27-30 revenue CAGR at $10.25 | at $9.40 |")
    md.append("|---|---|---|")
    rdcf = {}
    for m in [0.25, 0.28, 0.30, 0.325, 0.35, 0.40]:
        g1, g2 = solve_growth(PRICE, m), solve_growth(PRICE_PRIOR_CLOSE, m)
        rdcf[m] = (g1, g2)
        md.append(f"| {m:.1%} | {g1*100:+.1f}% | {g2*100:+.1f}% |")
    md.append("")
    growths = [-0.05, 0.0, 0.05, 0.10, 0.15, 0.20, 0.25]
    margins = [0.20, 0.25, 0.30, 0.35, 0.40]
    md.append("### Sensitivity: DCF value per share, FY27-30 revenue CAGR (rows) x 2030 adj. EBITDA margin (columns)\n")
    md.append("| Revenue CAGR \\ 2030 margin | " + " | ".join(f"{m:.0%}" for m in margins) + " |")
    md.append("|---|" + "---|" * len(margins))
    for g in growths:
        md.append(f"| {g:+.0%} (FY30 rev ${350*(1+g)**4:,.0f}M) | " + " | ".join(f"${generic_value(g, m):.2f}" for m in margins) + " |")
    md.append("")
    md.append("### Sensitivity: value per share at end-2027 from EV/EBITDA multiple (rows) x FY28 adj. EBITDA (columns)\n")
    ebitdas = [70, 100, 130, 145, 160, 190]
    mults = [4, 6, 8, 10, 12]
    md.append("| EV/EBITDA \\ FY28 EBITDA ($M) | " + " | ".join(str(e) for e in ebitdas) + " |")
    md.append("|---|" + "---|" * len(ebitdas))
    nc, sh = base_r[1]["cash_end"], base_r[2]["diluted"]
    for m in mults:
        md.append(f"| {m}x | " + " | ".join(f"${(m*e+nc)/sh:.2f}" for e in ebitdas) + " |")
    md.append(f"\n(Base-case net cash at end-2027 ${nc:.0f}M and {sh:.1f}M diluted shares held constant.)\n")

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
        json.dump({"summary": {k: v for k, v in summary.items() if k != "pw_rows"},
                   "reverse_dcf": {str(k): v for k, v in rdcf.items()}}, f, indent=1, default=float)
    print(text)
    return results, summary


if __name__ == "__main__":
    main()
