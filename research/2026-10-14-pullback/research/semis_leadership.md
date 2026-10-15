# Semiconductor leadership, rotation and the cycle narrative (as of the Oct 14, 2026 close, plus the overnight session)

Prepared on the evening of Oct 14, 2026 (ET). All price math comes from the local Yahoo daily CSVs (split-adjusted, through the Oct 14 close) using the scripts in `scratchpad/scripts/semis_lead.py`, `semis_lead2.py`, `semis_range.py`, `semis_breadth.py` and `semis_md*.py`. Raw output is in `scratchpad/analysis/semis_leadership_returns.csv` and `semis_lead2_out.txt`. Overnight quotes are IBKR real-time snapshots taken at 03:27–03:28 UTC Oct 15 (11:27 pm ET Oct 14).

**Source labels:**
- **[P]** primary source or local data
- **[M]** multiple independent reputable outlets
- **[S]** a single source, or a low-quality or aggregator source
- **[C]** commentary or opinion

**Return windows:**
- "1m" runs from the Sep 15 close and "3m" from the Jul 16 close (21 and 63 sessions).
- Both windows start near local lows (Sep 14 and mid-July), so they flatter semis. The "since Jun 22", "since Oct 6" and "since Oct 8" columns are cleaner.

*Disclosure: the model that wrote this report is made by Anthropic. Two Anthropic-related items (the Sep 14 Amodei essay and the reported Anthropic IPO) are reported only as third-party news, without editorializing.*

---

## 1. Key findings (most decision-relevant first)

1. **This is a failed breakout, not a retest.** [P]
   - **The range:** Through Aug 1–Sep 16, SOXX closed between 497.40 (Sep 14) and 559.12 (Aug 17). Intraday the range was 485.71–566.02.
   - **The breakout:** SOXX closed above the range on Sep 21. It stayed above for 15 sessions and peaked at a 589.51 close (Oct 5), 596.44 intraday (Oct 2).
   - **The failure:** It fell back into the range on Oct 12 (544.85). It closed Oct 14 at **519.42**, 36% of the way up the range and **below the range midpoint (528.26)**.
   - **Overnight:** SOXX traded at **509.35 (−1.94%)**. That is through the Sep 17 breakaway gap (510.37–514.80) and below the 61.8% retracement of the Jul 29→Oct 5 rally (512.56).
   - **The SOX index has the same structure.** Its close is 37% of the way up its range, and it re-entered the range after only 10 closes above it.
   - **SMH is somewhat stronger** because NVDA and TSM carry more weight in it. It sits 44% of the way up its range (just below the midpoint), and its overnight 554.50 is inside its own Sep 17 gap (553.17–557.56).
   - **On a weekly basis, the Sep/Oct rally made a lower high:** a best weekly close of 588.9 on Oct 2, versus 639.5 on Jun 19.
   - **Next levels:**
     - The range floor: 497.40 close, 485.71 intraday.
     - The 78.6% retracement: 491.65.
     - The Jul 29 low: 465.00 close, 464.08 intraday.
   - Reclaiming 528 and then 542 would be the first repair signal. A close back above 559 would negate the failed breakout.

2. **NVDA is the relative safe haven inside semis, not the weak link.** [P]
   - **Relative strength:**
     - NVDA/SOXX is up 5.0% since Oct 6 and sits above its 50-day average.
     - NVDA is only 7.5% below its high close, versus a **median of −30.8%** for the 29 semis names tracked here.
     - NVDA has given back 36% of its Jul 29→Oct 6 rally, versus 56% for SOXX.
   - **Its own Aug–Sep range:** NVDA closed between 206.64 and 230.36. It closed Oct 14 at 221.30, 62% of the way up, and traded at 217.75 overnight. That is just above its own tiny Sep 17 gap (216.76–217.15) and below the 38.2% retracement (220.43).
   - **Bullish reading:**
     - NVDA lagged the first-half blow-off: YTD +18.7% versus +72.5% for SOXX. It therefore has less excess to unwind.
     - Morgan Stanley puts it at about 15x FY28 earnings (Oct 2).
     - In the June–July crash, NVDA fell only 8.9% from Jun 22 to the Jul 29 low, while SOXX fell 29.0%.
   - **Bearish reading:**
     - NVDA/SOXX is still below its 200-day average, and the ratio peaked in November 2025.
     - A last leader standing often "catches down" when a sector sell-off ends in capitulation.
     - NVDA volume on Oct 14 was only 1.01x its 50-day average. NVDA holders have not capitulated.

3. **Leadership inside semis has broken and breadth has collapsed.** [P]
   - **Breadth in the 29-name semis basket:**

     | Date | % above 50-day average | Context |
     |---|---|---|
     | Oct 6 | 93% | |
     | Oct 14 | **14%** | |
     | Sep 14 | 17% | Low that preceded the Sep–Oct rally |
     | Jul 29 | 0% | The washout low |

     - **76% of the basket is in a bear market**, meaning more than 20% below its 52-week closing high.
     - Only 66% remain above their 200-day average.
   - **SOXX/SPY fell 10.0% in five sessions.** It is below its 50-day average but still 5.8% above its 200-day.
   - **The momentum leaders of the Sep–Oct rally have fallen hardest since Oct 6.** Median moves by group: optics/networking −19.9%, AI compute −14.5%.
     - Optics: LITE −20.9%, COHR −22.2%.
     - AI compute: ALAB −23.0%, ARM −21.3%.
     - Neoclouds: CRWV −28.3%, NBIS −25.6%.
   - **Analog and legacy names held up best:** median −11.0% since Oct 6 and −5.0% since Oct 8. TXN and ADI remain above their 50-day averages.
   - **Memory and storage is the epicentre of the full cycle:** median −36.5% since Jun 22, and WDC is −51% from its high.

4. **The money is rotating into defensives and energy, not broadening out.** Bearish for "buy the dip." [P]
   - **One-week sector moves:**

     | Gainers | 1-week move | Losers | 1-week move |
     |---|---|---|---|
     | XLE | **+6.7%** | IWM | −2.3% |
     | XLP | **+5.3%** | QQQ | −3.8% |
     | XLV | **+3.1%** | XLK | −5.4% |
     | TLT | +2.3% | SMH | −9.6% |
     | XLRE | +2.3% | SOXX | −10.9% |

   - **Small caps are not catching the flow.** IWM/SPY is at its 1-year low (2nd percentile).
   - **Equal-weight is not a convincing breadth story.** RSP/SPY is up 1.1% since Oct 6 but sits below both its 50-day and 200-day averages.
   - **This is a risk-off rotation into energy (oil/Iran), staples, health care and Treasuries,** not a healthy rotation into cyclicals.
   - Over one month, tech and semis are still positive (XLK +3.6%, SOXX +4.1%). That is only because the window starts at the Sep 15 low.

5. **The June peak was a parabolic blow-off, led by memory.** [M]
   - **The run-up:** SOXX rose **+111%** from its Mar 30 low (309.79) to its Jun 22 peak (655.01), and MU rose +276%.
   - **Valuation:** Chips' forward P/E premium over the Nasdaq-100 peaked above 32x vs 24x in late June. [S, Benzinga]
   - **Three air pockets broke the run:**
     - **Jun 5:** SOX −10.3%, the worst day since March 2020. Cited causes were Broadcom's AI guide, a hot May jobs report with higher yields, and a basket-level unwind of the "Parabolic 7."
     - **Jun 23:** SOX −7.9%. The KOSPI fell 10% and triggered a trading halt. Pre-Micron positioning was also cited.
     - **Good news sold:** Micron posted a blowout FQ3 on Jun 24 and the stock was sold within days.
   - **July's legs down:**
     - Memory supply fears: CXMT filed for an IPO of about $10bn.
     - TSMC raised its capex on Jul 16 and was sold.
     - Alphabet raised capex on Jul 22 alongside its first negative free cash flow (−7.1%).
     - A report on Jul 27 said China had begun producing its own DUV lithography tools (ASML −7%).
     - The Jul 29 FOMC held, with three hawkish dissents, while the 30-year yield neared 5.24%. Meta missed that evening.
   - **The bottom:** SOXX hit its trough on **Jul 29, −29.0%** close to close from the June peak. *The task premise of "~20% into late July/August" understates the decline.*
   - **The turn:** It came the next day, on Microsoft's Azure +43% print. SOXX rose +8.5% on Jul 30.

6. **The late-Sep/early-Oct rally was a stack of good news, and it failed on financing and return-on-capital doubts.** [M]
   - **The run:** From the Sep 14 low, SOXX rose +18.5% to Oct 5.
   - **The Sep 14 low itself:** Anthropic CEO Amodei published an essay urging a slowdown in AI development. Musk and Altman agreed, and Altman said there would be no OpenAI IPO this year. SOX fell −5.1%.
   - **The good news that drove the rally:**
     - Dip-buying after the Fed's Sep 16 hike.
     - AMD briefly topped $1T on Sep 21 (+10%), with ARM and INTC up 11–12% as oil fell.
     - NVDA announced a $150bn buyback (Sep 28).
     - Axios reported OpenAI's run-rate near $70bn (Sep 29).
     - Micron beat and guided FQ1 to $61.5bn (Sep 30).
     - TrendForce forecast Q4 DRAM contract prices up 10–15% (Sep 30).
     - TSMC's September revenue rose +54.6% y/y.
     - Marvell raised its targets at its investor day (Oct 6).
   - **What killed it:**
     - 10-year yield peaked at 5.31% (Oct 5) and the 30-year at 5.67% (Oct 7).
     - The FT reported OpenAI's run-rate at about $50bn (Oct 8), and the clarification bounce was sold (Oct 9).
     - Broadcom CEO Hock Tan said AI investing is "almost like they are in a casino" and that capital is the biggest constraint (Oct 12).
     - CXMT made server-DRAM claims, and Korean memory crashed: SK Hynix −10%, Samsung −7.4% (Oct 13).
     - The IMF's GFSR flagged circular AI financing (Oct 13).
     - CoreWeave bonds fell to about a 15% yield-to-maturity (Oct 13–14).
     - Barclays downgraded Dell over enterprise AI and normalizing memory prices (Oct 14).
     - ASML was sold on a beat (Oct 14).
   - **The result:** SOXX closed lower seven sessions in a row (Oct 6's −0.01% included).

7. **The AI-capex debate has moved from "is demand there?" to "who pays, and what is the return?"**
   - **Spending forecasts are still rising.** [M]
     - Goldman (Sep 25): hyperscaler capex of about $800bn in 2026 and **$1.2T in 2027**, versus a $1.1T consensus.
     - NVDA CFO Kress: $1.3T in 2027.
     - Deutsche Bank raised its wafer-fab-equipment (WFE) forecast to **$154bn / $217bn / $270bn** for 2026–28 (Oct 13).
   - **The financing side is where the stress is:**
     - Goldman estimates about **$300bn of annual AI revenue is needed to break even**, against about $70bn of incremental AI cloud revenue today. Roughly a third of 2026 capex is bond-funded. [S, via TechTimes]
     - The IMF's October 2026 GFSR counts **14 circular deals, with about $300bn of equity plus about $650bn of debt against $1.4T of revenue commitments**. It lists an AI correction among its three salient near-term risks. [M secondary; the IMF primary document was not fetched]
     - S&P cut Oracle to BBB− on Jul 9. [M]
     - CoreWeave's 2031s and 2032s yield about 15%. [M]
     - OpenAI's own-basis revenue is about $50bn. [M]
   - **Power:** Citi (Oct 8) sees a timing and location constraint, not an absolute shortage. Hock Tan says capital, not power, is the binding constraint.
   - **Equity supply is a looming overhang** for the AI complex. [S]
     - The reported Anthropic IPO: up to $100bn raised. Its S-1 was not public as of Oct 11.
     - Kioxia is considering a US ADR listing of $10bn or more.
     - CXMT's IPO.

8. **The memory cycle: prices are still rising, but the rate of increase is decelerating, and the stocks have already discounted the peak.** [P]/[M]
   - **TrendForce (Sep 30):** Q4 conventional DRAM contract prices +10–15% q/q and NAND +15–20%, but "price increases are slowing."
   - **Spot DRAM:** flat (TrendForce, Oct 7).
   - **Samsung's Q3 preliminary (Oct 8):** a record operating profit of ₩107.4tn, and the stocks fell anyway.
   - **Micron:** −16.7% since Oct 1, despite guiding FQ1 to $61.5bn.
   - **This is the classic late-cycle sequence.** Memory equities peak when the *rate of change* of pricing peaks, before prices themselves turn.
   - **For NVDA the effect is mixed:**
     - A memory cost peak helps margins. Kress has guided to a gross-margin trough of 71–72% in Q4 on memory costs.
     - But memory-*demand* doubts are a read on AI-capex fatigue.

9. **The sell-side is still constructive. That is supportive fundamentally, but it means sentiment is not washed out.**
   - **Bullish calls:**
     - Morgan Stanley: NVDA is its top pick, with a $300 target (Oct 2). [M]
     - Citi (Sep 15): the pullback is a "buying opportunity." [M]
     - Citi (Oct 8): top picks are AMD, TXN, LRCX, TER and SNPS. It says the sector is in "Phase 2" of its playbook, but **estimate-revision momentum slowed in Q2 and is expected to moderate further in Q3**. It downgraded NXPI and Nova. [P-ish, via Investing.com/Yahoo]
     - Deutsche Bank raised its WFE forecasts (Oct 13).
     - Rosenblatt raised its MU target to $1,900 (Oct 6).
   - **Bearish calls:**
     - Barclays downgraded Dell, HPE and NetApp (Oct 14).
     - D.A. Davidson's Luria has said CRWV equity could be worth zero if AI spending turns.
   - **No semis downgrades were found for Oct 8–14.** The search was limited.

10. **There is no capitulation signature yet.** [P]
    - **Volume vs the 50-day average on Oct 14:**

      | Instrument | Oct 14 | Earlier comparisons |
      |---|---|---|
      | SOXX | 1.52x | 2.88x on Jun 5; 1.79x on Jul 29 |
      | SMH | 1.77x | |
      | NVDA | 1.01x | |

    - **SOXX RSI(14) is 37.3,** versus 33.1 at the Jul 29 low.
    - **VIX 16.9 sits below VIX3M 18.8** (contango).
    - **Breadth at 14% is near a washout but not at the Jul 29 zero.**

---

## 2. Detailed evidence

### 2.1 Price structure: retest or failed breakout? [P, local CSVs + IBKR]

**Aug 1–Sep 16 range and where price sits** (computed by `semis_range.py`)

| | SOXX | SMH | ^SOX | NVDA (for reference) |
|---|---|---|---|---|
| Range closes (low / high) | 497.40 (Sep 14) / 559.12 (Aug 17) | 541.50 (Sep 14) / 594.07 (Aug 17) | 11,131.28 / 12,621.00 | 206.64 (Aug 3) / 230.36 (Sep 4) |
| Range intraday (low / high) | 485.71 (Aug 3) / 566.02 (Aug 17) | 524.77 / 600.37 | 10,922.31 / 12,770.71 | 196.85 / 234.76 |
| Range midpoint (closes) | 528.26 | 567.79 | 11,876.14 | 218.50 |
| First close above range | Sep 21 | Sep 21 | Sep 22 | Oct 1 |
| Closes above range / last one | 15 / Oct 9 | 15 / Oct 9 | 10 / Oct 8 | 6 / Oct 8 |
| Breakout peak (close; intraday) | 589.51 Oct 5; 596.44 Oct 2 | 633.90 Oct 5; 639.47 Oct 6 | 13,217.82 Oct 6; 13,349.96 Oct 6 | 239.24 Oct 6; 243.37 Oct 6 |
| Oct 14 close; position in range | 519.42; **36%** | 564.74; **44%** | 11,684.38; **37%** | 221.30; 62% |
| Oct 14 intraday low | 517.47 | 563.12 | 11,638.92 | 219.64 |
| Overnight (IBKR, 11:27 pm ET) | **509.35 (−1.94%)** | **554.50 (−1.81%)** | n/a | **217.75 (−1.60%)** |
| Sep 17 breakaway gap (prior high → gap-day low) | 510.37–514.80 (overnight trade is inside or below it) | 553.17–557.56 (overnight trade is inside it) | n/a | 216.76–217.15 |
| Fib retracement of Jul 29 → peak (closes): 38.2 / 50 / 61.8 / 78.6% | 541.95 / 527.26 / 512.56 / 491.65 | 584.36 / 569.06 / 553.76 / 531.97 | 12,159.55 / 11,832.66 / 11,505.76 / 11,040.34 | 220.43 / 214.63 / 208.82 / 200.55 |
| SMA 50 / 100 / 200 | 538.43 / 553.10 / 465.65 | 579.88 / — / 509.49 | 12,090.35 / 12,411.75 / 10,555.78 | 223.21 / 214.45 / 202.69 |
| Jul 29 low (close) | 465.00 | 504.22 | 10,447.49 | 190.01 |

**Weekly closes (SOXX).** Lower highs since June:
- Jun 19: 639.5. Jun 26: 589.9. Jul 31: 504.9 (the Jul 29 low falls in this week).
- Aug 14: 550.4. Sep 4: 519.9. Sep 25: 572.7. Oct 2: **588.9** (the rally high).
- Oct 9: 559.4. Oct 16, week to date: 519.4.

**Reading.**
- A retest holds at or above the old range top (about 559–566 for SOXX). Price fell back through it and through the midpoint within six sessions, so that test failed.
- The "from failed moves come fast moves" setup points to the bottom of the range (497 close, 486 intraday) as the next test.
- SOXX's 200-day average (465.65, rising at +5.9% per 20 days) sits almost exactly at the Jul 29 low (465). That is a confluence level if the range breaks.
- SMH and NVDA are still above their range midpoints and act as the relatively firm part of the complex.

### 2.2 Returns tables [P]

**Per-name returns (%)**, close to close, through the Oct 14 close:

| Group | Sym | Last | Since Jun 22 | Since Oct 6 | Since Oct 8 | 1w | 1m | 3m | YTD | From 52w high (close) | 52w high date | vs 50d | vs 200d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ETFs/Index | SOXX | 519.42 | -20.7 | -11.9 | -7.8 | -10.9 | +4.1 | -2.1 | +72.5 | -20.7 | 2026-06-22 | -3.5 | +11.5 |
| ETFs/Index | SMH | 564.74 | -15.6 | -10.7 | -7.0 | -9.6 | +4.2 | -0.7 | +56.8 | -15.6 | 2026-06-22 | -2.6 | +10.8 |
| ETFs/Index | ^SOX | 11684.38 | -20.2 | -11.6 | -7.4 | -10.6 | +4.6 | -1.5 | +65.0 | -20.2 | 2026-06-22 | -3.4 | +10.7 |
| ETFs/Index | QQQ | 728.95 | -1.2 | -4.0 | -2.5 | -3.8 | +3.5 | +3.3 | +18.7 | -4.0 | 2026-10-06 | +0.3 | +8.2 |
| ETFs/Index | XLK | 190.43 | -0.9 | -5.7 | -3.7 | -5.4 | +3.6 | +7.3 | +32.3 | -5.7 | 2026-10-06 | +0.3 | +14.0 |
| ETFs/Index | SPY | 769.60 | +3.4 | -1.2 | -0.6 | -1.0 | +1.6 | +2.5 | +12.9 | -1.2 | 2026-10-06 | +0.1 | +6.3 |
| ETFs/Index | RSP | 212.09 | +1.2 | -0.1 | +0.1 | +0.7 | -0.9 | -1.4 | +10.7 | -4.8 | 2026-08-14 | -1.8 | +2.7 |
| AI compute | NVDA | 221.30 | +6.1 | -7.5 | -4.0 | -6.8 | +4.3 | +6.7 | +18.7 | -7.5 | 2026-10-06 | -0.9 | +9.2 |
| AI compute | AMD | 570.82 | +3.5 | -12.1 | -8.0 | -11.6 | +13.2 | +13.9 | +166.5 | -12.1 | 2026-10-06 | +6.7 | +46.0 |
| AI compute | AVGO | 346.25 | -11.7 | -7.9 | -3.9 | -8.0 | +2.1 | -7.5 | +0.0 | -28.1 | 2026-06-02 | -6.2 | -6.0 |
| AI compute | MRVL | 245.28 | -20.3 | -14.5 | -10.7 | -13.8 | +10.6 | +30.3 | +188.6 | -22.5 | 2026-06-04 | +2.2 | +40.7 |
| AI compute | ARM | 238.01 | -41.6 | -21.3 | -13.5 | -19.1 | -1.6 | -9.2 | +117.7 | -45.8 | 2026-06-18 | -11.7 | +7.1 |
| AI compute | ALAB | 300.28 | -31.7 | -23.0 | -13.5 | -21.4 | +18.9 | -6.1 | +80.5 | -37.8 | 2026-06-30 | -5.1 | +20.8 |
| AI compute | CRDO | 179.23 | -40.8 | -18.8 | -15.4 | -18.5 | +19.2 | -13.8 | +24.6 | -40.8 | 2026-06-22 | -13.9 | -0.4 |
| Foundry/equipment | TSM | 430.00 | -8.1 | -10.8 | -6.1 | -8.9 | +3.9 | +4.9 | +41.5 | -11.5 | 2026-10-05 | -1.0 | +9.2 |
| Foundry/equipment | ASML | 1650.00 | -14.5 | -10.0 | -6.8 | -8.6 | +3.7 | -7.6 | +54.2 | -17.1 | 2026-06-30 | -5.2 | +5.0 |
| Foundry/equipment | AMAT | 446.63 | -30.2 | -15.8 | -12.4 | -14.2 | +6.0 | -20.4 | +73.8 | -38.2 | 2026-06-30 | -8.2 | +2.1 |
| Foundry/equipment | LRCX | 286.92 | -29.9 | -14.1 | -10.5 | -12.9 | +5.9 | -10.6 | +67.6 | -33.8 | 2026-06-30 | -7.6 | +2.1 |
| Foundry/equipment | KLAC | 178.81 | -33.6 | -9.4 | -9.1 | -9.2 | +6.4 | -18.5 | +47.2 | -40.7 | 2026-06-30 | -4.8 | -1.0 |
| Foundry/equipment | TER | 359.44 | -21.3 | -16.5 | -9.9 | -12.7 | +8.0 | +11.5 | +85.7 | -25.7 | 2026-06-30 | -6.1 | +4.7 |
| Memory/storage | MU | 914.13 | -24.5 | -12.6 | -11.7 | -16.0 | -1.5 | +7.1 | +220.3 | -24.7 | 2026-06-25 | -7.0 | +28.4 |
| Memory/storage | SNDK | 1403.34 | -38.3 | -15.5 | -12.8 | -17.1 | -8.3 | -0.5 | +491.2 | -39.9 | 2026-06-25 | -11.8 | +17.0 |
| Memory/storage | WDC | 364.10 | -50.3 | -11.4 | -7.4 | -10.2 | -11.6 | -22.0 | +111.4 | -51.2 | 2026-06-18 | -18.7 | -10.9 |
| Memory/storage | STX | 713.54 | -34.8 | -11.4 | -7.9 | -11.6 | -7.5 | -4.3 | +159.1 | -34.8 | 2026-06-22 | -15.9 | +6.4 |
| Optics/networking | LITE | 896.33 | +0.3 | -20.9 | -14.5 | -19.3 | +6.8 | +26.9 | +143.2 | -20.9 | 2026-10-06 | -3.7 | +16.0 |
| Optics/networking | COHR | 263.32 | -38.1 | -22.2 | -12.9 | -21.3 | -2.9 | -4.9 | +42.7 | -38.3 | 2026-06-02 | -13.2 | -10.4 |
| Optics/networking | CIEN | 359.60 | -21.9 | -18.9 | -15.6 | -19.5 | +7.6 | -7.5 | +53.8 | -42.6 | 2026-06-02 | -5.5 | -9.8 |
| Optics/networking | ANET | 195.42 | +12.0 | -9.3 | -7.4 | -9.5 | +1.3 | +15.9 | +49.1 | -9.8 | 2026-10-09 | -1.8 | +20.5 |
| Analog/legacy | TXN | 280.65 | -15.5 | -5.6 | -2.6 | -2.9 | +6.5 | -3.6 | +61.8 | -15.5 | 2026-06-22 | +3.1 | +10.8 |
| Analog/legacy | ADI | 403.57 | -9.4 | -4.0 | -0.6 | -1.6 | +11.7 | +6.1 | +48.8 | -9.4 | 2026-06-22 | +5.5 | +10.6 |
| Analog/legacy | NXPI | 220.83 | -31.7 | -9.6 | -4.4 | -6.1 | -2.4 | -18.4 | +1.7 | -33.6 | 2026-05-26 | -4.1 | -10.2 |
| Analog/legacy | ON | 73.36 | -44.2 | -15.0 | -7.6 | -11.1 | +0.2 | -16.7 | +35.5 | -45.2 | 2026-06-03 | -3.6 | -9.9 |
| Analog/legacy | MCHP | 71.25 | -30.6 | -12.3 | -5.7 | -8.7 | -0.3 | -12.8 | +11.8 | -30.8 | 2026-05-06 | -6.0 | -10.2 |
| Analog/legacy | INTC | 98.12 | -30.4 | -12.8 | -8.4 | -13.3 | +1.0 | +1.2 | +165.9 | -30.4 | 2026-06-22 | -5.2 | +16.8 |
| Analog/legacy | QCOM | 172.62 | -22.2 | -4.6 | -1.9 | -2.5 | -8.1 | +1.2 | +0.9 | -31.2 | 2026-05-29 | -1.0 | +1.9 |
| Analog/legacy | MPWR | 1243.11 | -19.2 | -15.6 | -9.2 | -12.8 | +8.8 | -4.8 | +37.2 | -26.4 | 2026-06-03 | -5.3 | -4.4 |
| AI infra/neoclouds | ORCL | 130.55 | -25.4 | -9.8 | -3.8 | -9.1 | -7.0 | +5.1 | -33.0 | -58.3 | 2025-10-16 | -10.3 | -18.8 |
| AI infra/neoclouds | CRWV | 65.78 | -40.9 | -28.3 | -19.4 | -25.6 | -18.7 | -9.8 | -8.1 | -53.6 | 2025-10-16 | -25.2 | -28.9 |
| AI infra/neoclouds | NBIS | 186.01 | -34.4 | -25.6 | -15.3 | -21.6 | -10.3 | +8.3 | +122.2 | -35.1 | 2026-06-18 | -16.9 | +7.4 |
| AI infra/neoclouds | DELL | 507.93 | +21.3 | -11.5 | -11.6 | -12.3 | -6.5 | +29.8 | +303.5 | -13.7 | 2026-09-17 | -0.9 | +63.5 |
| AI infra/neoclouds | SMCI | 35.78 | +0.9 | -17.7 | -16.3 | -20.4 | +0.4 | +45.0 | +22.2 | -35.0 | 2025-10-20 | -7.1 | +10.3 |
| AI infra/neoclouds | VRT | 222.83 | -37.8 | -12.0 | -8.6 | -9.6 | -5.0 | -24.2 | +37.5 | -40.8 | 2026-05-14 | -13.7 | -16.8 |
| AI infra/neoclouds | CEG | 279.54 | +1.5 | -6.9 | -1.9 | -6.7 | +7.6 | +11.0 | -20.9 | -30.8 | 2025-10-15 | +1.5 | -1.9 |
| AI infra/neoclouds | VST | 151.79 | -9.2 | -5.4 | -2.8 | -9.0 | +7.2 | -0.5 | -5.9 | -28.0 | 2025-10-15 | +5.1 | -1.9 |

Notes on the table:
- AVGO YTD is +0.04%: Dec 31, 2025 close 346.10 vs 346.25 now.
- "52w high" for ORCL, CRWV, SMCI, CEG and VST falls in Oct 2025, at the edge of the 1-year window.

**Group medians (%)**

| Group (median) | Since Jun 22 | Since Oct 6 | Since Oct 8 | 1w | 1m | 3m | YTD | From 52w high | vs 50d | vs 200d |
|---|---|---|---|---|---|---|---|---|---|---|
| AI compute | -20.3 | -14.5 | -10.7 | -13.8 | +10.6 | -6.1 | +80.5 | -28.1 | -5.1 | +9.2 |
| Foundry/equipment | -25.6 | -12.5 | -9.5 | -10.9 | +6.0 | -9.1 | +60.9 | -29.7 | -5.7 | +3.4 |
| Memory/storage | -36.5 | -12.0 | -9.8 | -13.8 | -7.9 | -2.4 | +189.7 | -37.3 | -13.9 | +11.7 |
| Optics/networking | -10.8 | -19.9 | -13.7 | -19.4 | +4.1 | +5.5 | +51.5 | -29.6 | -4.6 | +3.1 |
| Analog/legacy | -26.3 | -11.0 | -5.0 | -7.4 | +0.6 | -4.2 | +36.3 | -30.6 | -3.8 | -1.3 |
| AI infra/neoclouds | -17.3 | -11.7 | -10.1 | -10.9 | -5.8 | +6.7 | +8.2 | -35.1 | -8.7 | -1.9 |

**Breadth in the 29-name semis basket** (the AI compute, foundry/equipment, memory, optics and analog groups above):

| Date | % above 50d | % above 200d | % >20% below 52w closing high |
|---|---|---|---|
| Jun 22 (SOXX peak) | 83 | 100 | 3 |
| Jul 29 (low) | 0 | 79 | 90 |
| Aug 17 (range high) | 52 | 93 | 48 |
| Sep 14 (range low) | 17 | 69 | 83 |
| Sep 25 | 76 | 86 | 48 |
| Oct 6 (NVDA/SOX high) | 93 | 97 | 55 |
| Oct 8 | 83 | 83 | 59 |
| Oct 13 | 45 | 79 | 69 |
| **Oct 14** | **14** | **66** | **76** |

- The AI-infra basket of 8 names is worse: 25% above their 50-day average, 38% above their 200-day, and 88% are more than 20% off their highs.
- The semis basket's median drawdown is −30.8%, and its mean −29.2%.

### 2.3 Ratio trends [P]

| Ratio | vs 50d MA | vs 200d MA | Above 50d? | Above 200d? | 20d change | 20d-MA slope (20d) | 50d-MA slope (20d) | 5d change | Since Oct 6 | Since Jun 22 | 1y pct-rank | 1y high date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SOXX/SPY | -3.6% | +5.8% | NO | yes | +1.4% | +8.6% | +0.8% | -10.0% | -10.8% | -23.3% | 62 | 2026-06-22 |
| SMH/QQQ | -2.9% | +3.3% | NO | yes | +0.1% | +3.8% | +0.0% | -6.1% | -7.0% | -14.5% | 59 | 2026-06-22 |
| NVDA/SOXX | +2.6% | -5.5% | yes | NO | +0.0% | -4.4% | +2.3% | +4.6% | +5.0% | +33.7% | 38 | 2025-11-20 |
| RSP/SPY | -2.0% | -3.4% | NO | NO | -2.1% | -3.9% | -1.8% | +1.7% | +1.1% | -2.1% | 10 | 2026-02-27 |
| QQQ/SPY | +0.2% | +1.9% | yes | yes | +1.3% | +3.4% | +1.1% | -2.8% | -2.9% | -4.5% | 73 | 2026-06-18 |
| XLK/SPY | +0.1% | +7.7% | yes | yes | +1.4% | +5.3% | +2.6% | -4.5% | -4.6% | -4.1% | 84 | 2026-06-02 |
| NVDA/QQQ | -1.2% | +0.9% | NO | yes | +0.0% | +0.4% | +2.1% | -3.1% | -3.6% | +7.4% | 58 | 2026-05-14 |
| QQQE/QQQ | -2.4% | -2.5% | NO | NO | -1.7% | -3.9% | -1.4% | +1.1% | +0.4% | -1.3% | 11 | 2026-07-29 |
| IWM/SPY | -6.6% | -7.9% | NO | NO | -6.4% | -5.3% | -3.0% | -1.3% | -2.4% | -12.0% | 2 | 2026-06-26 |

**Reading:**
- **SOXX/SPY and SMH/QQQ** have broken below their 50-day averages but stay above their 200-day.
  - Their 20-day slopes still look positive only because they are measured from the Sep 15 trough. The 5-day change (−10% and −6%) is the real signal.
  - SOXX/SPY is still 5.9% above its Jul 29 level and 3.2% above its Sep 14 level. The relative trend has not yet made a lower low.
- **QQQ/SPY and XLK/SPY** sit right on their 50-day averages, at +0.2% and +0.1%. One more bad day breaks them.
- **RSP/SPY and QQQE/QQQ** are below both averages. The equal-weight "broadening" is weak and only tactical (+1.1% since Oct 6).
- **IWM/SPY** is at a 1-year low, which reads as rate-sensitive and risk-off.
- **NVDA/SOXX** is the one ratio improving in the short term (+4.6% in 5 days), but it remains below its 200-day average.

### 2.4 Is money rotating out of tech and semis, and into what? [P]

| ETF | 1d (Oct 14) | 1w | 1m | Since Oct 6 | 3m | 1w vs SPY | 1m vs SPY | vs 50d |
|---|---|---|---|---|---|---|---|---|
| XLE | +0.6 | +6.7 | +2.6 | +6.1 | +18.6 | +7.8 | +1.0 | +7.1 |
| XLP | +2.2 | +5.3 | +2.8 | +5.2 | +0.3 | +6.4 | +1.2 | +2.4 |
| XLV | +2.5 | +3.1 | +3.8 | +4.1 | +7.5 | +4.1 | +2.1 | +2.6 |
| XLRE | -0.8 | +2.3 | -3.7 | +0.9 | -8.7 | +3.3 | -5.2 | -4.0 |
| TLT | +0.7 | +2.3 | -2.3 | +2.1 | -6.3 | +3.3 | -3.8 | -2.4 |
| XLF | -0.5 | +1.4 | -4.1 | +0.9 | -3.9 | +2.4 | -5.6 | -3.3 |
| XLB | -0.1 | +1.4 | -2.1 | -0.1 | -2.4 | +2.4 | -3.6 | -3.1 |
| XLU | -0.4 | +1.4 | +1.0 | +1.4 | -8.2 | +2.4 | -0.6 | -0.9 |
| RSP | -0.6 | +0.7 | -0.9 | -0.1 | -1.4 | +1.7 | -2.4 | -1.8 |
| XLY | -0.8 | +0.1 | +0.6 | -0.2 | -5.0 | +1.1 | -1.0 | -2.3 |
| GLD | -1.5 | +0.0 | -4.6 | -1.6 | +3.0 | +1.0 | -6.1 | -5.4 |
| XLC | -1.3 | -0.4 | -2.8 | -0.7 | -1.6 | +0.6 | -4.4 | -1.0 |
| XLI | -1.0 | -0.5 | -1.1 | -2.6 | -7.3 | +0.5 | -2.6 | -4.5 |
| HYG | -0.4 | -0.5 | -2.0 | -0.6 | -3.7 | +0.5 | -3.6 | -2.3 |
| MDY | -1.3 | -0.7 | -1.5 | -2.3 | -4.8 | +0.3 | -3.1 | -3.4 |
| SPY | -1.1 | -1.0 | +1.6 | -1.2 | +2.5 | +0.0 | +0.0 | +0.1 |
| IWM | -1.9 | -2.3 | -4.8 | -3.5 | -8.2 | -1.3 | -6.3 | -6.5 |
| QQQ | -2.0 | -3.8 | +3.5 | -4.0 | +3.3 | -2.8 | +1.8 | +0.3 |
| XLK | -3.0 | -5.4 | +3.6 | -5.7 | +7.3 | -4.5 | +2.0 | +0.3 |
| SMH | -4.0 | -9.6 | +4.2 | -10.7 | -0.7 | -8.8 | +2.5 | -2.6 |
| SOXX | -4.5 | -10.9 | +4.1 | -11.9 | -2.1 | -10.0 | +2.5 | -3.5 |

**Verdict: yes, money is rotating out of tech and semis in the 1-week window.**
- **Where it is going:**
  - **Energy** (XLE +6.7%). Oil is high on Iran (Brent was above $104 on Oct 8; see oct8_narrative.md).
  - **Defensives:** staples +5.3% and health care +3.1%.
  - **Long Treasuries** (TLT +2.3%).
- **Where it is not going:** small or mid caps (IWM −2.3%, MDY −0.7%), cyclicals (XLI −0.5%), credit (HYG −0.5%) or gold (flat).
- This is the signature of de-risking, not of a "broadening bull" rotation.
- **Third-party summaries agree** [S/C]:
  - A sector review for Oct 7–14 ranked Energy (+6.7%), Staples (+5.3%) and Health Care (+3.1%) top three (Jesse Franklin Substack): https://jessefranklin1.substack.com/p/sector-rotation-this-week-energy
  - A daily note for Oct 12 reported AI-linked names sold and flows went to tankers, refiners and pharma (PC Thematic, Oct 12, 2026): https://pcthematic.substack.com/p/daily-market-report-october-12-2026
- **Context:** On Oct 14 S&P breadth was 47.9% of members up, and on Oct 8 it was 67.4% (oct8_narrative.md). The S&P 500 is only −1.3% from its high, because the money stays inside equities, in defensives.

### 2.5 Narrative: why semis peaked in late June 2026 and fell into late July

**Setup (blow-off).** [P] for prices, [S] for valuation
- From the Mar 30 low to Jun 22, SOXX rose 309.79 → 655.01 (+111%). Over the same span MU rose 321.80 → 1,211.38 (+276%) and AMD 196.04 → 551.63.
- Semis' forward P/E premium over the Nasdaq-100 peaked above 32x vs 24x in late June. By mid-July, SOXX's forward P/E had fallen to 24.7x, in line with the NDX. [S] Benzinga via Webull, Jul 16, 2026: https://www.webull.com/news/15237342889927680
- "Parabolic 7" (Ben Emons, Highline AM) was the label for a basket of SNDK, MRVL, MU, INTC, DELL, AMD and AVGO. By Jun 2, SNDK was up 623% YTD, MU +273% and MRVL +243%. [S/C] Yahoo Finance (David Moadel), Jun 5, 2026: https://finance.yahoo.com/markets/stocks/articles/micron-sandisk-marvell-plummet-parabolic-145117645.html

**Jun 5: the first crack.** SOXX −10.44% on local data; SOX about −10.3%, the worst day since March 2020; QQQ −4.80%; VIX +39.7%. [P] for prices; [M] for causes, which are not settled.
- Cited causes: Broadcom's AI guidance (AVGO fell almost 20% over two sessions), a hot May payrolls report that lifted yields, profit-taking at the basket level, and an unconfirmed rumor that Nvidia's Rubin would cut memory allocations.
- Sources: Tech Insider, https://tech-insider.org/chip-stocks-crash-2026/ ; Gotrade, https://www.heygotrade.com/en/blog/semiconductor-stocks-selloff-2026/ (search summaries; secondary).

**Jun 23: the second crack, on the day after the peak.** SOXX −7.88%, MU −13.18%, NVDA −4.13% on local data. [P] for prices; [M] for facts; causes speculative.
- GIGAZINE (Jun 24, 2026, citing CNBC, Reuters and NBC): https://www.gigazine.net/gsc_news/en/20260624-ai-tech-stock-sell-off
  - SOX −7.9%. The KOSPI fell −9.99% with a 20-minute market-wide halt, and SK Hynix and Samsung each fell −12%.
  - Reuters linked the KOSPI drop to regulators signalling semiconductor overheating and warning about leveraged ETFs.
  - A JPMorgan analyst said it "may reflect anxiety ahead of Micron's upcoming earnings."
  - MU was up more than 260% YTD at the time.

**Jun 24–26: good news sold.** [M]
- Micron's FQ3: revenue $41.46bn vs about $35.5bn consensus, EPS $25.11, and FQ4 guided to $49–51bn. MU rose +15.7% on Jun 25 (local), then SOXX fell −5.64% on Jun 26.
- Investing.com, Jun 2026: https://www.investing.com/news/stock-market-news/chip-stocks-surge-afterhours-on-microns-record-quarter-4759184

**July legs down.** Mixed sourcing.
- **Jul 1–2:** SOXX −6.41% and −5.57% (local).
  - A search summary attributes this to a report that SK Hynix was slowing AI memory expansion, a Citi warning on hyperscaler spending justification, and rising odds of a second Fed hike under new Chair Warsh.
  - Source: Babypips, Jul 2026, https://www.babypips.com/news/headline-ai-chip-stocks-selloff-july-2026-china-lithography-fed (403 on fetch).
  - **The SK Hynix and Citi items are UNVERIFIED.** A targeted search found no Citi note.
- **Mid-July:** CXMT filed for a Shanghai IPO raising close to $10bn, which raised memory-supply concerns, and memory led the decline. SOXX was −13.2% over four weeks to Jul 14, its sharpest since April 2025. [S] Benzinga via Webull, Jul 16 (above).
- **Jul 16: TSMC.** It reported a record Q2 and raised 2026 capex to US$60–64bn from $52–56bn. The stock fell on capex and margin-dilution worries, and SOXX fell −4.46% (local). [M] Focus Taiwan, Jul 16, 2026: https://focustaiwan.tw/business/202607160020 ; Invezz, Jul 16: https://invezz.com/news/2026/07/16/why-is-tsmc-stock-falling-despite-record-q2-earnings/
- **Jul 22: Alphabet.** Capex was raised to $195–205bn alongside the first negative free cash flow since its IPO, and GOOGL fell −7.1% (catalysts.md). Hyperscaler capex without revenue acceleration was punished.
- **Jul 27: China DUV.** The Information reported that a state-backed effort had begun producing immersion DUV tools (about 5 units in 2026, about 20 in 2027). ASML fell more than 7%, and BESI fell −8.5%.
  - JPMorgan said "producing a limited number of DUV lithography machines does not equate to supplying machines capable of mass production." [M]
  - GIGAZINE, Jul 28, 2026: https://gigazine.net/gsc_news/en/20260728-china-making-duv/ ; AI Weekly: https://aiweekly.co/alerts/asml-sinks-7-as-china-begins-homegrown-duv-machine-output
- **Jul 29: the capitulation day.** SOXX −5.38% (local) to the cycle low of 465.00. [M]
  - The FOMC held at 3.50–3.75% with three hawkish dissents ([P], Fed statement; see macro_rates.md).
  - The 30-year yield neared 5.24%. The Dow fell more than 1,100 points, and the Nasdaq-100 fell more than 10% from its peak.
  - Meta reported after the close: an EPS miss and free cash flow down 91%. It fell −9.5% the next day.
  - Source: HDFC Sky, Jul 30, 2026: https://hdfcsky.com/news/nasdaq-soars-2-54percent-as-microsoft-jumps-15percent-sp-500-dow-rebound-after-fed-led-selloff-july-30-2026
- **Jul 30: the turn.** [M]
  - Microsoft reported revenue of $90.0bn and Azure growth of +43%, and kept its CY26 capex plan. MSFT rose +15%.
  - SOXX rose +8.50% (local). LRCX rose +20.2%, its best day since 1999, and SNDK +21%.
  - Sources: HDFC Sky (above); Digital Today: https://www.digitaltoday.co.kr/en/view/87619/semiconductor-stocks-surge-again-two-days-after-1-trillion-market-cap-wipeout-lam-research-up-20-percent ; Invezz, Jul 30: https://invezz.com/news/2026/07/30/dow-jumps-640-points-as-microsoft-chip-stocks-power-wall-street-rebound/
- **Magnitude check.** [P]
  - SOXX fell **−29.0%** close to close from Jun 22 to Jul 29 (intraday 655.95 → 464.08, −29.3%).
  - Press figures of "nearly 18%" for July and "~21% intraday by Jul 17" are partial windows.

**Synthesis:**
- The June–July top was a positioning and valuation blow-off. Memory and the "Parabolic 7" were at the centre, and Korea's leveraged retail flows amplified the move.
- The fundamentals kept improving throughout: Micron, TSMC and hyperscaler capex all beat or rose.
- That is the pattern now repeating: good news is being sold.
- The low came on a macro capitulation day (Fed plus long yields) followed by a hyperscaler "capex with revenue" print (MSFT).

### 2.6 The late-Sep/early-Oct rally and why it failed

**Sep 14: the low before the rally.** [M]
- Moves: SOX −5.1%, NVDA −3.6%, AMD −5.6%, MU −6%, and LRCX and AMAT −6% each. SoftBank fell as much as −13.2%.
- The trigger:
  - Anthropic CEO Dario Amodei published an essay urging AI companies to slow capability advances. In it he wrote that within 6–12 months AI agents "could be capable of taking over the entire internet."
  - Musk and Altman agreed. Altman said OpenAI would not pursue an IPO this year.
  - Michael Burry called the warnings "hype and puffery" covering slowing growth. [C]
  - Deutsche Bank said a slowdown seemed unlikely.
- Sources: Reuters via Korea Times, Sep 15, 2026: https://www.koreatimes.co.kr/world/20260915/global-ai-stocks-fall-as-industry-chiefs-call-for-slowing-development ; Motley Fool, Sep 14, 2026: https://fool.com/investing/2026/09/14/why-micron-intel-amd-chip-stocks-fell-today ; Finviz, Sep 14, 2026: https://finviz.com/news/391528/amd-shares-fall-56-as-ai-development-debate-weighs-on-semiconductor-stocks
- Citi (Sep 15) called the pullback a buying opportunity and said AI-spending fears were overdone. [M] Investing.com: https://www.investing.com/news/stock-market-news/pullback-in-chip-stocks-is-a-buying-opportunity-citi-says-4811639

**Sep 16–17.**
- The FOMC hiked 25 bp to 3.75–4.00% ([P]; see macro_rates.md).
- SOXX rose +3.39% on Sep 17 (local). Dip-buying "led by semis" is described only in a low-quality blog [S]: https://tradingstrategyguides.com/chip-stocks-rally-stock-market-recap-september-17-2026/
- The causal link between the hike and the rebound is UNVERIFIED.

**Sep 21: breakout day.** SOXX +4.93% (local) closed above the August high.
- AMD hit a record above $613 and briefly topped a $1T market cap. ARM rose more than 12% and INTC more than 11%, while US crude fell about 3% to just above $96. [S/M]
- Stocktwits, Sep 21, 2026: https://stocktwits.com/news-articles/markets/equity/amd-stock-hits-record-high-briefly-joins-1-trillion-club-amid-chip-sector-rally/cZMRlieRBI3
- The local CSV shows AMD +9.95%.

**Sep 25.** Goldman, in a note titled "More AI capex, more volatility," lifted its 2027 hyperscaler capex estimate to $1.2T. [S] TechTimes, Sep 28: https://www.techtimes.com/articles/328112/20260928/goldman-sachs-quantifies-ais-230b-annual-gap-800b-spent-300b-needed-break-even.htm

**Sep 28.** NVDA added a record $150bn to its buyback, for $235bn in total through FY2028. Reuters noted the stock was near its lowest earnings multiple in more than a decade. [M] Business Today (Malaysia), Sep 28: https://www.businesstoday.com.my/2026/09/28/nvidia-announces-largest-stock-buyback-plan-of-us150-billion/ ; The Daily Record (AP), Sep 29: https://thedailyrecord.com/2026/09/29/nvidia-boosts-record-buyback-ai-chip-competition/

**Sep 29.** Axios reported OpenAI's ARR near $70bn (see oct8_narrative.md).

**Sep 30.**
- Micron's FQ4: revenue $54.23bn and FQ1 guided to $61.5bn ([P], 8-K; see catalysts.md).
- TrendForce forecast Q4 conventional DRAM contract prices +10–15% and NAND +15–20% ([P], see 2.8).

**Oct 2–6.**
- NVDA reached a record (Oct 2). Morgan Stanley re-named it a top pick with a $300 target (Oct 2) ([M], see 2.9).
- TSMC hit a record on Oct 5. Musk mentioned a possible TSMC role in the "Terafab" project; that claim comes from a promotional press release [S]. TSMC's September revenue was NT$511.86bn (+54.6% y/y).
- Marvell's investor day (Oct 6) raised its FY28 target to about $20bn (catalysts.md).
- Source: Stock Preachers/PR Newswire via Placera, Oct 10, 2026: https://www.placera.se/pressmeddelanden/taiwan-semiconductor-manufacturing-ai-revenue-questions-pull-semiconductor-stocks-off-october-highs-20261010-1

**Oct 8: Citi's read.** [M] Yahoo/Investing.com, Oct 8, 2026: https://finance.yahoo.com/markets/stocks/articles/citi-names-5-top-chip-104534003.html
- SOX was up about 24% from its summer correction.
- The industry remains in Citi's "Phase 2," with data center about 40% of the semis market and auto and industrial recovering.
- "Estimate revision momentum slowed in Q2 … expects further moderation in Q3."

**Failure sequence, Oct 6–14** (details and sources in oct8_narrative.md and macro_rates.md; new items cited here):
- **Rates.** The 10-year peaked at 5.31% on Oct 5 and the 30-year at 5.67% on Oct 7 ([P] FRED; macro_rates.md). Yields then *fell* into Oct 14, while semis kept falling. The selling is AI-specific, not driven by rates.
- **Oct 8:** The FT reported OpenAI's run-rate at about $50bn. SOXX −3.35%.
- **Oct 9:** The "≥$70bn by year-end" clarification bounce was sold. SOXX −0.69%, while the S&P rose +0.59%.
- **Oct 12:** SOXX −2.60%.
  - Broadcom's Hock Tan spoke at DBS's Asia Future Forward conference in Singapore. [M] Bloomberg via Yahoo, Oct 12, 2026: https://finance.yahoo.com/technology/ai/articles/broadcom-ceo-says-many-ai-193518585.html ; Tradingpedia, Oct 12: https://www.tradingpedia.com/2026/10/12/broadcom-chief-flags-casino-like-speculation-in-ai-stocks/
    - "A lot of investors have no clue what they are investing in." AI investing is "almost like they are in a casino."
    - "[What] I think might be the biggest constraint is capital."
  - Microsoft unveiled its Maia 300 chip.
  - CXMT made claims about denser DRAM.
  - Optics fell −8% to −10%.
- **Oct 13:** SOXX −0.17%, while NVDA rose +0.97%.
  - Memory crashed in Seoul: SK Hynix −10.09%, Samsung −7.39%, KOSPI −5.5%. CXMT said it is pursuing server-grade DRAM. [M] Quartz: https://qz.com/global-chip-stocks-fall-cxmt-memory-chip-101326 ; Yahoo: https://finance.yahoo.com/markets/stocks/articles/sk-hynix-sinks-5-china-180104796.html ; TechTimes, Oct 14: https://techtimes.com/articles/328974/20261014/chinas-cxmt-claims-next-gen-dram-lead-seoul-plunges-korea-keeps-hbm-moat.htm
  - AMAT fell −6.7% after giving no industry spending forecast at its investor day. Investing.com: https://investing.com/news/stock-market-news/applied-materials-shares-slide-as-chip-equipment-outlook-remains-uncertain-4947269 ; 24/7 Wall St., Oct 13: https://247wallst.com/investing/2026/10/13/semiconductor-equipment-stocks-slide-as-investors-take-profits-on-a-huge-year-applied-materials-sinks-7-lam-research-and-kla-drop-4/
  - The IMF GFSR was published (see 2.7).
- **Oct 14:** SOXX −4.50%, NVDA −3.16%.
  - CPI came in hot.
  - Barclays downgraded Dell, citing enterprise AI spending that may not sustain servers and normalizing memory prices. It also downgraded HPE and NetApp.
  - CRWV fell −15.5%, and its 2032 bonds yield about 15%.
  - ORCL fell −8.8%.
  - ASML fell on a beat-and-raise.
  - That made **seven straight down closes** for SOXX.

**Why it failed (synthesis):**
- The rally was built on (a) the OpenAI growth narrative ($70bn), (b) memory-price momentum and (c) "capex goes up forever" sell-side estimates.
- Within two weeks:
  - (a) was cut to a ~$50bn base.
  - (b) showed deceleration, CXMT supply risk and normalization talk from Barclays.
  - (c) was reframed from "how much capex" to "who finances it" (Hock Tan, the IMF, CoreWeave credit, Oracle at BBB−).
- Meanwhile record 10- and 30-year yields raised the hurdle rate for long-duration, debt-funded AI capex.

### 2.7 The AI-capex debate: sustainability, financing, circularity, power

**Spending (still rising)**
- **Goldman** (Ryan Hammond, Sep 25 note) [S]:
  - Top-5 hyperscaler capex about $800bn in 2026, **$1.2T in 2027** (consensus $1.1T) and about $1.4T in 2028.
  - About **$300bn of annual AI revenue needed to break even**, versus about $70bn of AI cloud revenue above the pre-AI trend, a gap of about $230bn a year.
  - Bonds are expected to fund about a third of 2026 capex, with issuance near $250bn.
  - AI capex is "a larger share of GDP than any technological investment cycle since the railroad build-out."
  - Source: TechTimes, Sep 28, 2026 (link above).
  - A secondary figure of "$1.4T by 2027" conflicts with this on base vs bull case. Seeking Alpha: https://seekingalpha.com/news/4644612-goldman-sachs-expects-us-hyperscaler-capex-to-reach-14t-by-2027
- **NVDA CFO** (Aug 26 transcript): "nearly $800bn in 2026 and $1.3tn in 2027" ([P]; catalysts.md).
- **Deutsche Bank** (Melissa Weathers, Oct 13, 2026) [M]: https://in.investing.com/news/stock-market-news/deutsche-bank-raises-outlook-on-semiconductor-equipment-stocks-93CH-5630384
  - WFE of $154bn in 2026 (+40%), $217bn in 2027 (+41%) and $270bn in 2028 (+24%).
  - "Buy-side expectations for 2028 WFE are approaching $300 billion."
  - Semicap stocks are down 29% on average from their July highs, versus a 16% drop for the SOX.
  - Future debate shifts to "sustainability of spending levels beyond 2028."

**Financing and circularity**
- **IMF October 2026 GFSR**, released at the Bangkok meetings around Oct 13.
  - Asia Times, Oct 14, 2026: https://asiatimes.com/2026/10/imf-warns-of-debt-fueled-ai-spending-as-bubble-fears-grow/
    - "free cash flows are rapidly declining as hyperscalers try to sustain large AI investment needs."
    - "distress at key investee firms could present significant 'wrong-way risk' to the AI ecosystem."
  - TechTimes, Oct 14, 2026: https://www.techtimes.com/articles/328970/20261014/imf-names-14t-ai-financing-loop-top-trigger-global-market-shock.htm
    - 14 deals: about $300bn of equity plus about $650bn of debt, against $1.4T of revenue commitments.
    - The IMF's Jason Wu described a "triple whammy" if monetization disappoints: equity falls, debt service suffers and revenue commitments fail.
    - Deputy Director Vamvakidis: "Market discipline is back." He also noted that P/E ratios have *fallen* because AI earnings beat forecasts, unlike the dot-com era.
  - Startup Fortune: https://startupfortune.com/imf-warns-an-ai-stock-correction-could-threaten-global-financial-stability/
  - Hyperscalers are about 10% of global IG issuance, versus about 0.5–1% in 2024 (the baseline conflicts across sources).
  - **Labeling:** [M]-secondary. The IMF's own GFSR page still listed the April 2026 edition when fetched, so the primary document is UNVERIFIED.
- **Oracle:** S&P cut it to BBB− on Jul 9, 2026, citing debt and negative free cash flow. S&P's Andrew Chang said a further cut is possible if leverage stays above 4.5x. [M] Computing, 2026: https://www.computing.co.uk/news/2026/ai/oracle-under-pressure-after-ratings-downgrade-over-ai-expansion
- **CoreWeave:** Its 2031 and 2032 bonds yield about 15%, and the 2032s trade below 80c ([M]; oct8_narrative.md, citing CNBC and SiliconANGLE, Oct 14).
- **Debt volumes:** Fortune (Jul 31, 2026) cited about $1.65T of off-balance-sheet obligations (Nikkei) and S&P Global's $225bn of hyperscaler-related bonds in 1H26. [C/S] https://fortune.com/2026/07/31/ai-debt-hypescalers-capex-capital-spending-hidden-borrowing-bond-issuance/
- **NVDA's own circular exposure:** residual-value guaranties capped at $105bn for OpenAI's Ohio capacity (8-K, Aug 17), and supply commitments of $279bn ([P]; catalysts.md).
- **Equity supply** [S]:
  - Anthropic IPO: reportedly up to $100bn at about $2T, with Nvidia in talks for an anchor stake of up to $10bn (Reuters, mid-September, via PYMNTS: https://www.pymnts.com/news/artificial-intelligence/2026/anthropic-could-land-nvidia-as-10-billion-ipo-investor/).
  - Its public S-1 was still not on EDGAR as of Oct 11. An investor day was reported for Oct 14 (Yahoo: https://finance.yahoo.com/markets/stocks/articles/anthropic-public-1-still-missing-210349323.html ; FinanceFeeds: https://financefeeds.com/anthropics-14-october-investor-day-nears-but-its-s-1-still-isnt-public-the-ipo-timeline-explained/).
  - Kioxia is considering a US ADR raise of $10bn or more (Reuters via Korea Times, Sep 15).

**Power constraints**
- **Citi** (Oct 8): disputes the "power wall" thesis. It expects global data-center supply to grow from 140 GW (2026) to 395 GW (2031), versus 370 GW of demand. The constraints are "timing, location and deliverability," not an absolute shortage. TrendForce sees interconnection bottlenecks from 2028. [M] (Yahoo link above)
- **Morgan Stanley's Moore** (Oct 2): "if the biggest constraint becomes land/power/shell, the highest tokens per Gigawatt win." That is a pro-NVDA framing. [M] TheStreet: https://www.thestreet.com/technology/nvidia-300-stock-price-target-morgan-stanley ; Investing.com: https://www.investing.com/news/stock-market-news/morgan-stanley-reinstates-this-ai-chipmaker-as-its-top-pick-in-semiconductors-4935139
- **Hock Tan** (Oct 12): capital, not power or chip supply, may be the biggest constraint. Supply-chain issues are easing.
- **Exelon** cut its high-probability data-center load from about 18 GW to about 11 GW in July. Turbine lead times are reported to run to 2030–31. [S] Oilprice.com: https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.html

### 2.8 Memory pricing cycle

- **TrendForce, Sep 30, 2026** [P]: https://www.trendforce.com/presscenter/news/20260930-13258.html
  - 4Q26 conventional DRAM contract prices +10–15% q/q. NAND overall +15–20%.
  - On conventional DRAM, the market stays undersupplied but **"price increases are slowing."**
  - Server RDIMM stays undersupplied on agentic-AI demand. Enterprise SSD bit demand is up more than 80% y/y.
  - Consumer weakness: notebook sales are pressured, smartphone production is cut, and client SSD price rises are restrained.
  - PC DRAM supply may fall in 2027.
- **Earlier path** [S]: TrendForce raised its Q3 2026 PC DRAM forecast from 8–13% to 15–20%, and Q4 from 0–5% to 3–8% (June update). Gate: https://www.gate.com/news/detail/trendforce-raises-q3-q4-2026-dram-contract-price-forecasts-to-15-20-and-3-8-22224554
  - So Q4 expectations rose through the summer, which supported the Sep–Oct rally.
- **Spot** [P]: DRAM spot was "largely sideways." Mainstream DDR4 1Gx8 3200 sat at $46.32, unchanged w/w as of Oct 6. NAND 512Gb TLC wafer spot fell −2.90% w/w. https://www.trendforce.com/news/2026/10/07/insights-memory-spot-price-update-dram-spot-largely-sideways-as-holidays-month-end-effects-weigh
- **Samsung Q3 preliminary (Oct 8)** [M]:
  - Operating profit ₩107.4tn (+782.5% y/y), slightly above the ₩106.6tn consensus. Sales of ₩195tn missed ₩200.6tn.
  - Memory operating profit is estimated at about ₩110tn. Full results come Oct 29.
  - Korea Times, Oct 8, 2026: https://www.koreatimes.co.kr/business/companies/20261008/samsung-electronics-estimates-803-bil-in-q3-operating-profit
- **SK Hynix Q2 (late July):** a record, but it missed lofty expectations on slower shipment growth and less aggressive pricing. [S] FXLeaders, Jul 29, 2026: https://www.fxleaders.com/news/2026/07/29/skhy-stock-falls-below-130-as-sk-hynixs-record-ai-memory-profit-misses-lofty-expectations/
- **China supply:** the CXMT IPO filing (about $10bn, July) and its server-DRAM claims on Oct 12–13. One strategist called the sell-off disproportionate, because CXMT has not proven volume production (search summary of Quartz and Yahoo coverage). [M]
- **Sell-side on memory pricing:**
  - Barclays' Dell downgrade (Oct 14) cites *normalizing* memory prices ([M]; oct8_narrative.md).
  - Rosenblatt raised its MU target to $1,900 (Oct 6) [S].
  - NVDA's Kress (Aug 26) said memory prices "exceeded our prior expectations and are headed even higher" ([P]; catalysts.md).
- **Price action** [P]:
  - MU is −24.7% from its 52-week closing high and −16.7% since Oct 1, despite the best guide in its history.
  - Memory/storage median: −36.5% since Jun 22. WDC is −51%, SNDK −40% and STX −35%.
- **Reading:** Contract prices are still rising but decelerating, and the equities have been falling since late June. That is consistent with the market discounting a *rate-of-change* peak in memory pricing, which typically leads the price peak by one to three quarters. This is analyst judgment, not sourced.

### 2.9 Sell-side views (dated)

| Date | Firm / analyst | View | Label |
|---|---|---|---|
| Oct 2 | Morgan Stanley / Joseph Moore | NVDA back to top pick, OW, $300 PT (about 15x FY28 EPS); half the business is a broad non-hyperscaler customer base | [M] |
| Oct 1 | Cantor | NVDA OW, $350 (catalysts.md / oct8_narrative.md) | [S] |
| Sep 15 | Citi | Semis pullback is a "buying opportunity"; AI-spend slowdown fears overdone; NVDA and AVGO Buy | [M] |
| Oct 8 | Citi / Atif Malik | Top picks AMD, TXN, LRCX, TER, SNPS. "Phase 2." Revision momentum slowing (Q2), expected to moderate further in Q3. Downgraded NXPI to Neutral ($260 from $370), Nova to Neutral, OLED to Sell | [M] |
| Oct 13 | Deutsche Bank / Melissa Weathers | WFE raised to $154bn / $217bn / $270bn (2026–28); buy-side 2028 expectations near $300bn | [M] |
| Oct 6 | Rosenblatt | MU PT $1,900 from $1,500 | [S] |
| Sep 25 | Goldman / Ryan Hammond | 2027 hyperscaler capex $1.2T (> $1.1T consensus); "more AI capex, more volatility"; $300bn revenue needed to break even | [S] |
| Oct 14 | Barclays | Downgraded DELL (OW→EW, PT $603→$574), HPE and NTAP: enterprise AI may not sustain servers; normalizing memory prices | [M] |
| Oct 14 | D.A. Davidson / Gil Luria | CRWV equity could be worth zero if AI spending turns (oct8_narrative.md) | [M] |
| Jul (date inconsistent) | BofA | "Healthy reset"; low-beta leadership (NVDA, TXN, ADI); $1.5T cloud capex by 2027. **The article has internal inconsistencies (an MU PT of $155), so it is not relied upon** | [S, unreliable] |

**Net:**
- The Street remains constructive on AI semis and is raising capex and WFE forecasts.
- Citi's revision-momentum comment and Barclays' memory-normalization comment are the first sell-side cracks in the "second derivative."
- No broad semis downgrade cycle has started. That means sentiment has not capitulated: it supports fundamentals, but it is not a contrarian buy signal.

---

## 3. Numbers table (key levels and stats)

| Item | Value |
|---|---|
| SOXX: Jun 22 peak → Jul 29 low (close) | 655.01 → 465.00 (**−29.0%**) |
| SOXX: Jul 29 → Oct 5 rally | +26.8%. Sep 14 → Oct 5: +18.5% |
| SOXX: Oct 5 → Oct 14 | −11.9%; retraced **56%** of the Jul 29 → Oct 5 rally |
| NVDA: retracement of Jul 29 → Oct 6 rally | **36%** |
| SOXX: consecutive down closes | 7 (Oct 6 −0.01% through Oct 14) |
| SOXX RSI(14) | 37.3 now; 33.1 at Jul 29; 41.8 at Sep 14 |
| Volume / 50d average on Oct 14 | SOXX 1.52x, SMH 1.77x, QQQ 1.58x, NVDA 1.01x. For comparison, SOXX was 2.88x on Jun 5, 1.43x on Jun 23 and 1.79x on Jul 29 |
| 1y beta NVDA vs SOXX | 0.48 (correlation 0.59). 3m: 0.52 (betas_ratios.txt) |
| SOXX range Aug 1–Sep 16 (closes) | 497.40–559.12; midpoint 528.26 |
| SOXX overnight (IBKR, 11:27 pm ET) | 509.35 (−1.94%): inside or below the Sep 17 gap at 510.37–514.80; below the 61.8% retracement at 512.56 |
| SMH overnight | 554.50 (−1.81%): inside its gap at 553.17–557.56 |
| NVDA overnight | 217.75 (−1.60%): just above its gap at 216.76–217.15. 50% retracement 214.63; 61.8% 208.82; 200d 202.69; Jul 29 low 190.01 |
| SOXX 200d SMA | 465.65 (≈ the Jul 29 low of 465.00); rising +5.9% per 20 days |
| Semis basket % above 50d | 14% (93% on Oct 6; 0% on Jul 29) |
| Semis median drawdown from 52w closing high | −30.8% (NVDA −7.5%) |
| TrendForce 4Q26 contract | Conventional DRAM +10–15%; NAND +15–20% ("slowing") |
| Goldman 2026 / 2027 / 2028 hyperscaler capex | ~$800bn / $1.2T / ~$1.4T |
| DB WFE 2026 / 2027 / 2028 | $154bn / $217bn / $270bn |
| IMF circular deals | 14 deals; ~$300bn equity + ~$650bn debt against $1.4T commitments (secondary) |

---

## 4. UNVERIFIED or conflicting

- **Jun 23 cause.** There is no definitive cause. Reuters speculated that Korean regulators had signalled overheating and warned on leveraged ETFs; JPMorgan pointed to pre-Micron anxiety. Speculative.
- **Jun 5 cause.** Sources mix Broadcom's guide, payrolls and yields, a basket unwind, and a *rumor* about Rubin memory allocation. The weighting is unsettled, and the Rubin rumor is unconfirmed.
- **Early-July drivers.** The items about SK Hynix slowing AI-memory expansion and a Citi warning on hyperscaler justification come from a search summary of a page that returned 403. A targeted search found **no such Citi note**. UNVERIFIED.
- **July decline magnitude.** Press figures range from "nearly 18%" to about 21% intraday by Jul 17. Local data shows −29.0% close to close, Jun 22 → Jul 29. Use the local figure.
- **Sep 17 rebound cause.** The only source is a low-quality blog, which attributes the prior day's selling to the Fed hike. The hike itself is confirmed (Fed statement); the causal story is UNVERIFIED.
- **Sep 28 "AI safety concerns" sell-off.** This appears only in a promotional press release. Local data shows SOXX −2.08% that day while NVDA rose +1.68%, on its buyback. The cause is UNVERIFIED.
- **Musk/Terafab/TSMC (Oct 5).** Single promotional source. TSMC's September revenue figure should be checked against TSMC's monthly report; catalysts.md computed Q3 revenue from 6-Ks.
- **IMF GFSR figures** (14 deals, $300bn / $650bn / $1.4T). These are consistent across at least four secondary outlets, but the IMF primary document was not retrieved: imf.org still showed the April 2026 GFSR when fetched. The IG-issuance baseline conflicts (0.5% vs "<1%" in 2024).
- **TechTimes claim that the KOSPI fell "about 44% from its July 2026 peak, erasing $2.18T in two days."** This looks implausible and inconsistent with other reporting. UNVERIFIED; do not use.
- **Goldman's 2027 capex:** $1.2T base (Sep 25 note) vs "$1.4T by 2027" headlines (bull case or a different peer set).
- **BofA "healthy reset" article** (Investing.com, dated Jul 6, 2026): the dates and the MU price target ($155) are internally inconsistent. Not relied upon.
- **"JPMorgan sees a buying opportunity / Morgan Stanley more cautious on semis in 2H26":** one commentary source. UNVERIFIED.
- **Anthropic IPO size, valuation and timing:** secondary sources, and the details conflict (October vs November; $2T vs $2.3T). The S-1 was not public as of Oct 11.
- **Oracle debt totals:** sources give about $130bn and about $167bn.
- **SK Hynix Q2 "miss" magnitude** (−9.6% to −18% post-report): single, low-quality source.
- **Exelon data-center load cut (18 → 11 GW):** single source.
- **No semis analyst downgrades were found for Oct 8–14,** other than Citi's Oct 8 NXPI and Nova cuts and Barclays on Dell, HPE and NTAP. The search was not exhaustive.
- **Overnight quotes** are IBKR real-time prints in thin overnight trading (03:27 UTC). They are indicative, not settlement levels.

---

## 5. Implications for the pullback-bottom question

### Bearish readings (the semis bottom is probably not in yet)
1. **Structure.** The breakout failed and price is back through the midpoint. Overnight, SOXX trades below the Sep 17 gap and the 61.8% retracement. The weekly lower high (588.9 vs 639.5) is in place.
   - The textbook next test is the bottom of the range: **497 (close) / 486–492 (intraday and the 78.6% retracement)**. That is about −4.2% to −6.5% from the Oct 14 close and −2.3% to −4.6% from the overnight print.
   - If 486 fails, the **465 area** comes next: the Jul 29 low, which coincides with the rising 200-day average. That is about −10.5% from the close.
2. **Good news is being sold:** Micron in June and on Oct 1, TSMC in July, ASML on Oct 14, Samsung's record on Oct 8, and the OpenAI clarification on Oct 9. That is the hallmark of a market repricing the *durability* of the cycle, not the current quarter.
3. **The narrative has moved to financing.** Hock Tan, the IMF, CoreWeave at about 15%, Oracle at BBB−, Goldman's $230bn revenue gap, and roughly a third of capex bond-funded at multi-decade-high long yields. Positive capex revisions do not answer this. It needs either revenue proof or cheaper capital.
4. **Memory's second derivative is turning:** "price increases are slowing," spot is flat, Barclays talks of normalization, and CXMT supply is coming. Memory led the June–July crash and is leading again.
5. **The rotation is defensive** (energy, staples, health care, Treasuries), with small caps at relative lows. Money is leaving risk, not just tech.
6. **No capitulation yet.** SOXX volume is 1.5x (vs 2.9x on Jun 5), NVDA volume 1.0x, VIX is in contango, and breadth is 14%, not 0%. The sell-side is still bullish. The Jun–Jul decline ran −29% and seven weeks. This one is −11.9% and seven sessions from the Oct 5 high.
7. **For NVDA specifically, its relative strength is a double-edged sword.**
   - If semis capitulate, the "last leader standing" often catches down.
   - NVDA's beta to SOXX is about 0.5 in normal tape, but correlations rise in flushes.
   - Its overnight 217.75 is already below the 38.2% retracement. The 50% retracement (214.63), the 61.8% (208.82) and the 200-day average (202.69) are the next references.

### Bullish readings (a buyable low could form soon)
1. **SOXX is at the 50–61.8% retracement zone** of a +26.8% rally. RSI is 37 (the Jul 29 low printed 33), and the 29-name basket's breadth is 14% above the 50-day, close to the 17% that preceded the Sep 14 → Oct 5 rally. SOXX is still +11.5% above a rising 200-day average.
2. **Fundamentals are still accelerating:**
   - TSMC Q3 revenue +50.9% y/y.
   - ASML raised guidance and says 2027–28 supply will not meet demand.
   - Micron guided FQ1 to $61.5bn, and Samsung posted record operating profit.
   - DB raised WFE; Goldman and Kress put 2027 capex at $1.2–1.3T.
   - The June–July −29% drawdown also happened while fundamentals improved, and it ended on a hyperscaler earnings catalyst (MSFT, Jul 30).
   - **The same catalyst window is coming:** META Oct 21, MSFT and GOOGL Oct 28, AMZN about Oct 29. "Capex up and the spender's stock up" is the setup that would mark a low (catalysts.md).
3. **NVDA is the strongest large-cap semi.** It is cheap on Street numbers (about 15x FY28 per MS), backed by a $235bn buyback authorization, and holding above its Aug–Sep range midpoint. Its June–July drawdown was only −8.9% versus −29% for SOXX.
4. **The October selling is AI-specific, not macro-systemic:** S&P −1.3% from its high, HY OAS 3.16%, IG calm. Pullbacks confined to one sector usually resolve faster than broad bear markets.

### Signals that would separate the two
- **Repair:** SOXX daily closes back above **528 (range midpoint)**, then **542 (38.2%)**. A close above **559** would negate the failed breakout. SOXX/SPY reclaiming its 50-day average. Semis breadth back above 50% of names over the 50-day.
- **Range breakdown:** a SOXX close below **497**, especially on 2x or more volume, opens 465–486. An NVDA close below 214.6 (50% retracement), then 208.8, would mean the leader is catching down.
- **Capitulation signature** (often marks the real low): breadth near 0–5% above the 50-day, SOXX volume above 2x its 50-day average, VIX above VIX3M, and the first sell-side semis downgrades. These would point to a better-quality low than one formed without them.
- **Rotation reversal:** XLP and XLV underperforming SPY again, IWM/SPY turning up, and SMH/QQQ rising. That would mean risk appetite is returning rather than merely shifting into defensives.
- **Memory and credit tells:** MU holding its Oct 14 area while SK Hynix and Samsung stabilize; CoreWeave 2032s recovering above 80c; no further Oracle rating action.
- **Catalysts to watch:** TSMC Q3 (Oct 15, Taiwan time), META (Oct 21), MSFT/GOOGL (Oct 28), Samsung full Q3 (Oct 29), plus the Anthropic S-1 timing as an equity-supply event.
