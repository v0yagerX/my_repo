"""
MNTN, Inc. (NYSE: MNTN) - driver-based model, 2026E-2030E, three scenarios.

Run:  python3 mntn/model/mntn_model.py      (writes mntn/model/output/*.md, *.csv, mntn_model.xlsx)

Conventions
- $M unless noted. Revenue is NET of media cost (MNTN reports as agent; 10-K FY2025 Note 2).
- Every input below is an [estimate] unless tagged [reported] / [guidance] / [consensus].
- Revenue = sum over customer-size segments of (TTM active customers x net revenue per TTM customer)
  + creative/QuickFrame services + QuickFrame AI monetization.
  MNTN discloses only total TTM active customers (3,632 at FY25 [reported]) and the small-business
  share of revenue (~6% Q4'24, 12% Q1'25, ~15% Q3'25 [reported via 424B4 / Q3'25 call]).
  The FY25 segment split is therefore an [estimate] calibrated to those disclosures and to the CEO's
  "~$15K/yr" small-business and "deep six figures" mid-market spend remarks (Canaccord, Aug 2026).
- Adjusted EBITDA follows the company definition (adds back SBC, D&A, fair-value marks,
  acquisition/legal costs, restructuring).
- Adjusted EPS (ours; MNTN reports none) = (GAAP pre-tax income + SBC + amortization of acquired
  intangibles + one-off items) x (1 - 25% normalized tax) / diluted shares.
- FCF = operating cash flow - capitalized internal-use software (MNTN has ~no other capex).
"""
from __future__ import annotations

import copy
import csv
import json
import math
import os
from dataclasses import dataclass, field

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
YEARS = [2026, 2027, 2028, 2029, 2030]

PRICE = 10.25            # MNTN, 2026-10-15 intraday (IBKR last $10.24-10.34; prior close $9.40) [reported market data]
CASH_JUN26 = 237.3       # [reported] Q2'26, no debt
BASIC_SHARES_YE25 = 74.0  # [estimate] (Q4'25 basic WASO 73.84M; Jun-30-26 74.21M; Jul-31-26 74.80M [reported])

# ---------------------------------------------------------------------------------------------
# FY2025 actuals [reported] and FY2025 segment split [estimate]
# ---------------------------------------------------------------------------------------------
FY25 = dict(
    revenue=290.1, revenue_exME=284.7, ptv=281.9, creative_other=2.8, max_effort=5.4,
    gross_margin=0.772, adj_ebitda=68.0, sbc=31.7, d_and_a=9.9, op_income=24.0,
    interest=3.5, net_income=-6.4, gaap_eps=-0.13, ocf=56.5, cap_sw=12.5, fcf=44.0,
    ttm_customers=3632, cash_ye=210.2,
)
# FY2025 segment split [estimate]: small business ~13% of PTV revenue (6% Q4'24 -> ~15% Q3'25),
# upper mid-market/enterprise ~8% (Q1'25: small 12%, mid 79%, remainder ~9%).
SEG0 = {
    #               TTM customers, net revenue per TTM customer ($K)
    "small":  dict(cust=2450, arpc=15.0),    # ~$36.8M
    "mid":    dict(cust=1112, arpc=200.3),   # ~$222.7M
    "upper":  dict(cust=70,   arpc=323.0),   # ~$22.6M
}


@dataclass
class Scenario:
    name: str
    prob: float
    # customer growth by segment, 2026..2030
    cust_g: dict
    # revenue-per-customer growth by segment, 2026..2030
    arpc_g: dict
    creative_other: list          # $M (QuickFrame human-creator services, breakage)
    qf_ai: list                   # $M QuickFrame AI / creative subscription monetization
    gross_margin: list            # GAAP gross margin
    cash_cogs_addback: list       # (cap-SW amortization + SBC in COGS)/revenue, i.e. cash GM - GAAP GM
    td_cash: list                 # technology & development ex-SBC, % rev
    sm_cash: list                 # sales & marketing ex-SBC, % rev
    ga_cash: list                 # G&A ex-SBC, ex-one-offs, % rev
    sbc_pct: list                 # SBC % revenue
    sbc_split: dict = field(default_factory=lambda: dict(cogs=0.02, td=0.22, sm=0.38, ga=0.38))
    one_offs: list = field(default_factory=lambda: [1.9, 0.5, 0.5, 0.5, 0.5])  # restructuring/acq. legal
    cap_sw_pct: float = 0.043
    wc_pct_of_delta_rev: float = 0.18   # calibrated: OCF/(adj. EBITDA+interest) ran 79-83% in FY25-1H26 [estimate]
    cash_tax_rate: list = field(default_factory=lambda: [0.05, 0.12, 0.20, 0.24, 0.25])
    book_tax_rate: float = 0.26
    interest_yield: list = field(default_factory=lambda: [0.035, 0.032, 0.030, 0.030, 0.030])
    gross_issuance_m: float = 1.6     # new shares/yr from options, RSUs, ESPP, contractor RSUs
    dilution_addon_m: list = field(default_factory=lambda: [4.6, 4.2, 4.0, 4.0, 4.0])
    buyback_usd: list = field(default_factory=lambda: [30.0, 70.0, None, None, None])  # None => payout ratio x FCF
    buyback_payout: float = 0.5
    buyback_price: list = field(default_factory=lambda: [10.5, 12.0, 14.0, 16.0, 18.0])
    ev_ebitda_exit: float = 8.0       # multiple applied for valuation
    pe_exit: float = 15.0


def _seg_rev(seg):
    return seg["cust"] * seg["arpc"] / 1000.0


def run(s: Scenario) -> dict:
    segs = copy.deepcopy(SEG0)
    rows = []
    prev_rev = FY25["revenue"]
    basic_end = BASIC_SHARES_YE25
    cash = FY25["cash_ye"]
    cap_sw_hist = [9.9, 12.5]  # FY24, FY25 [reported]
    intang_left = 11.4 + 0.66 * 2  # acquired intangibles at Jun-26 [reported] + 1H26 amortization ~=> YE25 balance
    for i, y in enumerate(YEARS):
        seg_out = {}
        for k in segs:
            segs[k]["cust"] *= 1 + s.cust_g[k][i]
            segs[k]["arpc"] *= 1 + s.arpc_g[k][i]
            seg_out[k] = dict(cust=segs[k]["cust"], arpc=segs[k]["arpc"], rev=_seg_rev(segs[k]))
        ptv = sum(v["rev"] for v in seg_out.values())
        rev = ptv + s.creative_other[i] + s.qf_ai[i]
        cust = sum(v["cust"] for v in seg_out.values())

        gp = rev * s.gross_margin[i]
        cash_gm = s.gross_margin[i] + s.cash_cogs_addback[i]
        adj_ebitda = rev * (cash_gm - s.td_cash[i] - s.sm_cash[i] - s.ga_cash[i])
        sbc = rev * s.sbc_pct[i]

        # D&A: capitalized software amortized over 3 years + acquired intangibles ($2.63M/yr)
        cap_sw = rev * s.cap_sw_pct
        cap_sw_hist.append(cap_sw)
        cap_sw_amort = sum(cap_sw_hist[-3:]) / 3.0 * 0.95
        intang_amort = min(2.63, intang_left)
        intang_left -= intang_amort
        d_and_a = cap_sw_amort + intang_amort + 0.3
        one_off = s.one_offs[i]
        op_income = adj_ebitda - sbc - d_and_a - one_off

        # GAAP opex lines (incl. SBC; COGS includes cap-SW amortization)
        sbc_by = {k: sbc * v for k, v in s.sbc_split.items()}
        td_gaap = rev * s.td_cash[i] + sbc_by["td"]
        sm_gaap = rev * s.sm_cash[i] + sbc_by["sm"]
        ga_gaap = rev * s.ga_cash[i] + sbc_by["ga"] + one_off + 0.3

        # Share count & buybacks (FCF computed first using beginning cash for interest)
        ocf_pre_int = adj_ebitda - one_off - s.wc_pct_of_delta_rev * (rev - prev_rev)
        interest = None
        # iterate once for interest on average cash
        bb_usd = s.buyback_usd[i]
        for _ in range(3):
            pretax = op_income + (interest or cash * s.interest_yield[i])
            cash_tax = max(0.0, pretax) * s.cash_tax_rate[i]
            ocf = ocf_pre_int + (interest or cash * s.interest_yield[i]) - cash_tax
            fcf = ocf - cap_sw
            bb = bb_usd if bb_usd is not None else max(0.0, fcf * s.buyback_payout)
            end_cash = cash + fcf - bb
            interest = (cash + end_cash) / 2.0 * s.interest_yield[i]
        pretax = op_income + interest
        book_tax = pretax * s.book_tax_rate
        net_income = pretax - book_tax
        bb_shares = bb / s.buyback_price[i]
        basic_start = basic_end
        basic_end = basic_start + s.gross_issuance_m - bb_shares
        basic_avg = (basic_start + basic_end) / 2.0
        diluted = basic_avg + s.dilution_addon_m[i]
        eps = net_income / diluted
        adj_pretax = pretax + sbc + intang_amort + one_off
        adj_ni = adj_pretax * 0.75
        adj_eps = adj_ni / diluted
        rows.append(dict(
            year=y, revenue=rev, growth=rev / prev_rev - 1, ptv=ptv,
            small_rev=seg_out["small"]["rev"], mid_rev=seg_out["mid"]["rev"], upper_rev=seg_out["upper"]["rev"],
            small_cust=seg_out["small"]["cust"], mid_cust=seg_out["mid"]["cust"], upper_cust=seg_out["upper"]["cust"],
            small_arpc=seg_out["small"]["arpc"], mid_arpc=seg_out["mid"]["arpc"], upper_arpc=seg_out["upper"]["arpc"],
            customers=cust, rev_per_cust_k=ptv / cust * 1000,
            creative_other=s.creative_other[i], qf_ai=s.qf_ai[i],
            gross_margin=s.gross_margin[i], gross_profit=gp,
            td_pct=td_gaap / rev, sm_pct=sm_gaap / rev, ga_pct=ga_gaap / rev,
            td_cash_pct=s.td_cash[i], sm_cash_pct=s.sm_cash[i], ga_cash_pct=s.ga_cash[i],
            sbc=sbc, sbc_pct=s.sbc_pct[i], d_and_a=d_and_a, one_off=one_off,
            adj_ebitda=adj_ebitda, adj_ebitda_margin=adj_ebitda / rev,
            op_income=op_income, op_margin=op_income / rev, interest=interest,
            pretax=pretax, book_tax=book_tax, cash_tax=cash_tax, net_income=net_income,
            basic_end=basic_end, diluted=diluted, gaap_eps=eps, adj_eps=adj_eps,
            ocf=ocf, cap_sw=cap_sw, fcf=fcf, fcf_ps=fcf / diluted, fcf_margin=fcf / rev,
            fcf_after_sbc=fcf - sbc, buyback=bb, buyback_shares=bb_shares, cash_end=end_cash,
        ))
        cash = end_cash
        prev_rev = rev
    return dict(scenario=s.name, prob=s.prob, rows=rows, s=s)


# ---------------------------------------------------------------------------------------------
# Scenarios
# ---------------------------------------------------------------------------------------------
BASE = Scenario(
    name="Base", prob=0.50,
    cust_g=dict(small=[0.43, 0.30, 0.22, 0.16, 0.12], mid=[0.19, 0.13, 0.11, 0.09, 0.08], upper=[0.21, 0.22, 0.18, 0.15, 0.12]),
    arpc_g=dict(small=[-0.07, -0.03, 0.00, 0.02, 0.02], mid=[0.018, 0.03, 0.03, 0.03, 0.03], upper=[0.03, 0.04, 0.04, 0.04, 0.04]),
    creative_other=[3.3, 1.8, 1.8, 1.8, 1.8],
    qf_ai=[0.0, 1.0, 3.0, 5.0, 7.0],
    gross_margin=[0.805, 0.800, 0.795, 0.790, 0.790],
    cash_cogs_addback=[0.025, 0.025, 0.025, 0.025, 0.025],
    td_cash=[0.180, 0.180, 0.175, 0.170, 0.165],
    sm_cash=[0.275, 0.265, 0.255, 0.245, 0.235],
    ga_cash=[0.095, 0.090, 0.085, 0.080, 0.080],
    sbc_pct=[0.076, 0.068, 0.065, 0.063, 0.060],
    buyback_price=[10.5, 12.0, 14.0, 16.0, 18.0],
    ev_ebitda_exit=7.0, pe_exit=13.0,
)

BULL = Scenario(
    name="Bull", prob=0.20,
    cust_g=dict(small=[0.45, 0.36, 0.30, 0.24, 0.20], mid=[0.20, 0.17, 0.16, 0.15, 0.14], upper=[0.22, 0.28, 0.28, 0.25, 0.22]),
    arpc_g=dict(small=[-0.06, 0.00, 0.03, 0.03, 0.03], mid=[0.025, 0.045, 0.05, 0.05, 0.05], upper=[0.03, 0.06, 0.06, 0.06, 0.06]),
    creative_other=[3.3, 2.0, 2.0, 2.0, 2.0],
    qf_ai=[0.0, 2.0, 6.0, 12.0, 20.0],
    gross_margin=[0.807, 0.807, 0.805, 0.805, 0.805],
    cash_cogs_addback=[0.025, 0.024, 0.023, 0.022, 0.022],
    td_cash=[0.178, 0.175, 0.165, 0.155, 0.150],
    sm_cash=[0.272, 0.255, 0.240, 0.225, 0.215],
    ga_cash=[0.094, 0.085, 0.075, 0.068, 0.062],
    sbc_pct=[0.075, 0.065, 0.060, 0.055, 0.050],
    gross_issuance_m=1.4, dilution_addon_m=[4.8, 5.5, 6.0, 7.0, 8.0],
    buyback_price=[11.0, 15.0, 20.0, 25.0, 30.0],
    ev_ebitda_exit=11.0, pe_exit=20.0,
)

BEAR = Scenario(
    name="Bear", prob=0.30,
    cust_g=dict(small=[0.42, 0.15, -0.03, -0.06, -0.05], mid=[0.18, 0.06, -0.02, -0.04, -0.03], upper=[0.18, 0.06, -0.02, -0.03, -0.03]),
    arpc_g=dict(small=[-0.075, -0.05, -0.04, -0.04, -0.03], mid=[0.01, -0.02, -0.04, -0.04, -0.03], upper=[0.02, -0.02, -0.04, -0.04, -0.03]),
    creative_other=[3.3, 1.5, 1.2, 1.0, 1.0],
    qf_ai=[0.0, 0.0, 0.0, 0.0, 0.0],
    gross_margin=[0.802, 0.785, 0.770, 0.760, 0.750],
    cash_cogs_addback=[0.025, 0.026, 0.027, 0.028, 0.028],
    td_cash=[0.182, 0.195, 0.205, 0.205, 0.200],
    sm_cash=[0.278, 0.290, 0.290, 0.285, 0.280],
    ga_cash=[0.097, 0.100, 0.105, 0.110, 0.110],
    sbc_pct=[0.077, 0.080, 0.085, 0.090, 0.090],
    gross_issuance_m=2.0, dilution_addon_m=[4.0, 2.5, 1.5, 1.0, 1.0],
    one_offs=[1.9, 2.0, 3.0, 1.0, 1.0],
    buyback_price=[9.5, 8.0, 6.5, 5.5, 5.0],
    ev_ebitda_exit=4.0, pe_exit=8.0,
)

SCENARIOS = [BEAR, BASE, BULL]


# ---------------------------------------------------------------------------------------------
# Valuation helpers
# ---------------------------------------------------------------------------------------------
COE = 0.11            # cost of equity / WACC (no debt): small-cap, SMB ad cyclicality, dual class
T_NOW = 2026.79       # Oct 15, 2026
TERMINAL_G = 0.03


def value_on_multiple(res, year_metric=2028, at_year_end=2027, multiple=None):
    """EV/EBITDA on the following year's EBITDA at year-end `at_year_end`, plus net cash, per diluted share,
    discounted back to today at COE."""
    rows = {r["year"]: r for r in res["rows"]}
    m = multiple if multiple is not None else res["s"].ev_ebitda_exit
    ev = m * rows[year_metric]["adj_ebitda"]
    eq = ev + rows[at_year_end]["cash_end"]
    ps = eq / rows[year_metric]["diluted"]
    t = (at_year_end + 1.0) - T_NOW
    return ps, ps / (1 + COE) ** t


def value_2030(res, multiple=None):
    rows = {r["year"]: r for r in res["rows"]}
    m = multiple if multiple is not None else res["s"].ev_ebitda_exit
    # value at end-2030 on 2030 EBITDA x (1+g_2031) where g_2031 = half of 2030 growth (floored at -5%)
    g31 = max(-0.05, rows[2030]["growth"] * 0.5)
    ev = m * rows[2030]["adj_ebitda"] * (1 + g31)
    eq = ev + rows[2030]["cash_end"]
    ps = eq / rows[2030]["diluted"]
    t = 2031.0 - T_NOW
    return ps, ps / (1 + COE) ** t


def dcf(res):
    """Equity value per share today from explicit FCF-after-SBC (SBC treated as a cash cost, i.e.
    buyback-neutralized) 2026Q4-2030 + Gordon terminal value. Uses net cash at Jun-26."""
    rows = res["rows"]
    pv = 0.0
    for r in rows:
        f = r["fcf_after_sbc"] - r["interest"] * (1 - 0.25)  # unlevered: strip after-tax interest income
        frac = 0.21 if r["year"] == 2026 else 1.0           # only ~Q4'26 remains in 2026
        t = (r["year"] + 0.5 if r["year"] > 2026 else 2026.9) - T_NOW
        pv += frac * f / (1 + COE) ** max(t, 0.05)
    last = rows[-1]
    f_last = last["fcf_after_sbc"] - last["interest"] * 0.75
    g = min(TERMINAL_G, max(-0.03, last["growth"] * 0.5))
    tv = f_last * (1 + g) / (COE - g)
    pv += tv / (1 + COE) ** (2031.0 - T_NOW)
    shares = rows[0]["diluted"]
    return (pv + CASH_JUN26 + 1.0) / shares  # + ~Q3 FCF retained (approx.)


# ---------------------------------------------------------------------------------------------
# Reverse-DCF / sensitivity engine (generic path: growth g for 2027-2030 fading to 3% by 2035,
# adj. EBITDA margin moving linearly from 28% (FY26) to M by 2030 then held)
# ---------------------------------------------------------------------------------------------
def generic_value(cagr_27_30, margin_2030, rev26=350.0, sbc_pct=0.065, cap_sw_pct=0.043, tax=0.25,
                  wacc=COE, tg=TERMINAL_G, shares=79.5, net_cash=CASH_JUN26 + 1.0, wc=0.10):
    rev = rev26
    m0 = 0.28
    pv = 0.0
    prev = rev
    for k, y in enumerate(range(2027, 2036)):
        if y <= 2030:
            g = cagr_27_30
            m = m0 + (margin_2030 - m0) * (k + 1) / 4.0
        else:
            j = y - 2030
            g = cagr_27_30 + (tg - cagr_27_30) * j / 5.0
            m = margin_2030
        rev = prev * (1 + g)
        ebitda = rev * m
        da = rev * cap_sw_pct * 0.95 + 0.3
        ebit = ebitda - rev * sbc_pct - da
        f = ebitda - rev * sbc_pct - max(0.0, ebit) * tax - rev * cap_sw_pct - wc * (rev - prev)
        t = (y + 0.5) - T_NOW
        pv += f / (1 + wacc) ** t
        prev = rev
    tv = f * (1 + tg) / (wacc - tg)
    pv += tv / (1 + wacc) ** (2036.0 - T_NOW)
    # add Q4'26 FCF after SBC (~$12M)
    pv += 12.0 / (1 + wacc) ** 0.1
    return (pv + net_cash) / shares


def solve_growth_for_price(price, margin_2030, **kw):
    lo, hi = -0.30, 0.60
    for _ in range(100):
        mid = (lo + hi) / 2
        if generic_value(mid, margin_2030, **kw) > price:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


# ---------------------------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------------------------
def fmt(v, kind):
    if v is None:
        return "-"
    if kind == "m":
        return f"{v:,.1f}"
    if kind == "m0":
        return f"{v:,.0f}"
    if kind == "pct":
        return f"{v*100:.1f}%"
    if kind == "eps":
        return f"${v:.2f}"
    if kind == "int":
        return f"{v:,.0f}"
    if kind == "x":
        return f"{v:.1f}x"
    return str(v)


TABLE_ROWS = [
    ("Revenue ($M)", "revenue", "m"),
    ("  y/y growth", "growth", "pct"),
    ("  Small business (incl. Express) ($M)", "small_rev", "m"),
    ("  Mid-market (Pro) ($M)", "mid_rev", "m"),
    ("  Upper mid-market (Premium) ($M)", "upper_rev", "m"),
    ("  Creative services + QuickFrame AI ($M)", None, "m"),
    ("TTM active customers (year-end)", "customers", "int"),
    ("  small / mid / upper", None, "str"),
    ("Net revenue per TTM customer ($K)", "rev_per_cust_k", "m"),
    ("Gross margin", "gross_margin", "pct"),
    ("T&D % rev (GAAP incl. SBC)", "td_pct", "pct"),
    ("S&M % rev (GAAP incl. SBC)", "sm_pct", "pct"),
    ("G&A % rev (GAAP incl. SBC)", "ga_pct", "pct"),
    ("SBC ($M)", "sbc", "m"),
    ("  SBC % rev", "sbc_pct", "pct"),
    ("Adj. EBITDA ($M)", "adj_ebitda", "m"),
    ("  Adj. EBITDA margin", "adj_ebitda_margin", "pct"),
    ("GAAP operating income ($M)", "op_income", "m"),
    ("  GAAP operating margin", "op_margin", "pct"),
    ("Interest income ($M)", "interest", "m"),
    ("Book tax ($M) / cash tax ($M)", None, "str"),
    ("GAAP net income ($M)", "net_income", "m"),
    ("Diluted shares (M)", "diluted", "m"),
    ("GAAP EPS", "gaap_eps", "eps"),
    ("Adjusted EPS (ours)", "adj_eps", "eps"),
    ("Free cash flow ($M)", "fcf", "m"),
    ("FCF per share", "fcf_ps", "eps"),
    ("FCF after SBC ($M)", "fcf_after_sbc", "m"),
    ("Buyback ($M) / shares retired (M)", None, "str"),
    ("Year-end cash ($M)", "cash_end", "m"),
]


def scenario_table(res):
    rows = res["rows"]
    hdr = "| | FY2025A | " + " | ".join(f"FY{r['year']}E" for r in rows) + " |"
    sep = "|---|---|" + "---|" * len(rows)
    a = {
        "revenue": "290.1", "growth": "28.6% (36.0% ex-ME)", "small_rev": "~36.8", "mid_rev": "~222.7",
        "upper_rev": "~22.6", "customers": "3,632", "rev_per_cust_k": "77.6 (PTV)", "gross_margin": "77.2%",
        "td_pct": "17.0%", "sm_pct": "31.2%", "ga_pct": "19.9%", "sbc": "31.7", "sbc_pct": "10.9%",
        "adj_ebitda": "68.0", "adj_ebitda_margin": "23.4%", "op_income": "24.0", "op_margin": "8.3%",
        "interest": "3.5", "net_income": "(6.4)", "diluted": "50.9", "gaap_eps": "($0.13)", "adj_eps": "~$0.60*",
        "fcf": "44.0", "fcf_ps": "~$0.56*", "fcf_after_sbc": "12.3", "cash_end": "210.2",
    }
    lines = [hdr, sep]
    for label, key, kind in TABLE_ROWS:
        if label.startswith("  Creative"):
            vals = [fmt(r["creative_other"] + r["qf_ai"], "m") for r in rows]
            av = "~2.8 (+5.4 ME)"
        elif label.startswith("  small / mid"):
            vals = [f"{r['small_cust']:,.0f} / {r['mid_cust']:,.0f} / {r['upper_cust']:,.0f}" for r in rows]
            av = "~2,450 / ~1,112 / ~70"
        elif label.startswith("Book tax"):
            vals = [f"{r['book_tax']:.1f} / {r['cash_tax']:.1f}" for r in rows]
            av = "(9.6) benefit / 2.7"
        elif label.startswith("Buyback"):
            vals = [f"{r['buyback']:.0f} / {r['buyback_shares']:.1f}" for r in rows]
            av = "0"
        else:
            vals = [fmt(r[key], kind) for r in rows]
            av = a.get(key, "")
        lines.append(f"| {label} | {av} | " + " | ".join(vals) + " |")
    return "\n".join(lines)


def main():
    os.makedirs(OUT, exist_ok=True)
    results = [run(s) for s in SCENARIOS]
    md = []
    md.append(f"Model run. Price ${PRICE:.2f}. Cost of equity {COE:.0%}. Terminal growth {TERMINAL_G:.0%}.\n")
    summary = {}
    for res in results:
        md.append(f"### {res['scenario']} case (probability {res['prob']:.0%})\n")
        md.append(scenario_table(res))
        v27, v27pv = value_on_multiple(res)
        v30, v30pv = value_2030(res)
        d = dcf(res)
        summary[res["scenario"]] = dict(
            prob=res["prob"], mult_value_end27=v27, mult_value_pv=v27pv, value_2030=v30, value_2030_pv=v30pv,
            dcf=d, rows=res["rows"])
        md.append(
            f"\nValuation: {res['s'].ev_ebitda_exit:.0f}x FY28 adj. EBITDA at end-2027 = ${v27:.2f}/sh "
            f"(PV today ${v27pv:.2f}); {res['s'].ev_ebitda_exit:.0f}x FY31E EBITDA at end-2030 = ${v30:.2f} "
            f"(PV ${v30pv:.2f}); DCF (FCF after SBC, {COE:.0%}, g<= {TERMINAL_G:.0%}) = ${d:.2f}.\n")
    # probability-weighted
    keys = ["revenue", "adj_ebitda", "gaap_eps", "adj_eps", "fcf_ps"]
    pw = {y: {k: 0.0 for k in keys} for y in YEARS}
    for res in results:
        for r in res["rows"]:
            for k in keys:
                pw[r["year"]][k] += res["prob"] * r[k]
    md.append("### Probability-weighted\n")
    md.append("| | " + " | ".join(f"FY{y}E" for y in YEARS) + " |")
    md.append("|---|" + "---|" * len(YEARS))
    for k, lab, kind in [("revenue", "Revenue ($M)", "m"), ("adj_ebitda", "Adj. EBITDA ($M)", "m"),
                         ("gaap_eps", "GAAP EPS", "eps"), ("adj_eps", "Adjusted EPS", "eps"),
                         ("fcf_ps", "FCF/share", "eps")]:
        md.append(f"| {lab} | " + " | ".join(fmt(pw[y][k], kind) for y in YEARS) + " |")
    pv_mult = sum(summary[n]["prob"] * summary[n]["mult_value_pv"] for n in summary)
    pv_2030 = sum(summary[n]["prob"] * summary[n]["value_2030_pv"] for n in summary)
    pv_dcf = sum(summary[n]["prob"] * summary[n]["dcf"] for n in summary)
    e27 = sum(summary[n]["prob"] * summary[n]["mult_value_end27"] for n in summary)
    md.append(f"\nProbability-weighted value: end-2027 multiple method ${e27:.2f} (PV ${pv_mult:.2f}); "
              f"2030 exit PV ${pv_2030:.2f}; DCF ${pv_dcf:.2f}.\n")

    # Reverse DCF & sensitivity
    md.append("### Reverse DCF\n")
    for m in [0.25, 0.30, 0.335, 0.35, 0.40]:
        g = solve_growth_for_price(PRICE, m)
        md.append(f"- 2030 adj. EBITDA margin {m:.1%}: price ${PRICE:.2f} implies FY27-30 revenue CAGR of {g*100:.1f}%")
    md.append("")
    growths = [-0.05, 0.0, 0.05, 0.10, 0.15, 0.20, 0.25]
    margins = [0.20, 0.25, 0.30, 0.35, 0.40]
    md.append("### Sensitivity: DCF value per share by FY27-30 revenue CAGR (rows) and 2030 adj. EBITDA margin (columns)\n")
    md.append("| Revenue CAGR \\ 2030 margin | " + " | ".join(f"{m:.0%}" for m in margins) + " |")
    md.append("|---|" + "---|" * len(margins))
    sens = []
    for g in growths:
        vals = [generic_value(g, m) for m in margins]
        sens.append(vals)
        md.append(f"| {g:+.0%} | " + " | ".join(f"${v:.2f}" for v in vals) + " |")
    md.append("")
    # Sensitivity 2: 2030 EV/EBITDA multiple-based value vs growth & margin
    md.append("### Sensitivity: 2030 adj. EBITDA ($M) by FY27-30 revenue CAGR and 2030 margin (FY26 revenue $350M)\n")
    md.append("| Revenue CAGR \\ 2030 margin | " + " | ".join(f"{m:.0%}" for m in margins) + " |")
    md.append("|---|" + "---|" * len(margins))
    for g in growths:
        rev30 = 350 * (1 + g) ** 4
        md.append(f"| {g:+.0%} (rev ${rev30:,.0f}M) | " + " | ".join(f"{rev30*m:,.0f}" for m in margins) + " |")

    text = "\n".join(md)
    with open(os.path.join(OUT, "model_output.md"), "w") as f:
        f.write(text)
    # CSV per scenario
    for res in results:
        with open(os.path.join(OUT, f"scenario_{res['scenario'].lower()}.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(res["rows"][0].keys()))
            w.writeheader()
            for r in res["rows"]:
                w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})
    with open(os.path.join(OUT, "summary.json"), "w") as f:
        json.dump({k: {kk: vv for kk, vv in v.items() if kk != "rows"} for k, v in summary.items()}, f, indent=1)
    print(text)
    return results, summary


if __name__ == "__main__":
    main()
