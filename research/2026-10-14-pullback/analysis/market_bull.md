# Broad US market (SPX/SPY, RSP): the shallow-pullback case

*Advocate brief, written ~03:20 UTC Oct 15 (11:20 pm ET Oct 14).*

- **Sources.** Numbers come from DATA_BRIEF.md and the data files unless marked. **[computed]** = my own statistics from `scratchpad/mb/` scripts (`mb_base.py`: ^GSPC 1950–2026, FRED DGS10, VIX/VIX3M; `mb_conc.py`: concentration; `mb_rsp.py`: RSP 2003–2026).
- **TSMC.** Q3 results were not out at ~03:20 UTC (WebSearch found only previews; call at 2:00 am ET).
- **Overnight (IBKR).** SPY 765.93 (−0.48%, real-time, 03:20 UTC; ≈ SPX 7,682); ES Dec 7,732.5 (−0.49%, delayed); QQQ 721.01 (−1.09%).

## 1. Thesis

The S&P 500 is in a rotation-driven pullback inside an intact uptrend. The equal-weight market already took its correction (RSP −6.6% from Aug 14 to Sep 30) and has turned up, so this decline is the AI/semis unwind dragging the cap-weighted index rather than a broad liquidation.

**Projected bottoming zone: SPX 7,505–7,645 on a closing basis, most likely 7,580–7,645.** That is a −2.2% to −4.0% drawdown from the 7,818.93 ATH close, or −1.0% to −2.8% below the Oct 14 close. RSP should hold 207.2–209.2.

**Timeframe: the low prints between Oct 16 (monthly opex) and Oct 30 (after the Oct 28 FOMC and the Oct 29 GDP+PCE release), with an ATH retest by late November.** My honest odds that the closing low holds above 7,428 (−5%) are about 60%.

## 2. Evidence, ranked by weight

**1. Base rates strongly favour a shallow outcome from here [computed].**

Since 1950, 244 S&P episodes running from one ATH to the next reached a −1.28% closing drawdown, which is where we are now.
- **Final depth:** median **−3.3%**. 70% ended shallower than −5%, 84% shallower than −7.5% and 90% shallower than −10%. Only 5% became bear markets.
- **Timing:** median 9 sessions from ATH to trough (that would be Oct 19) and 10 sessions from trough to a new ATH.

Two filters that match today do not hurt the odds:
- **10y yield up ≥40bp in the 3 months before the ATH** (1999–, n=14; today +63bp over 3m per macro_rates.md): median −4.2%, 71% shallower than −5%, none ≥20%.
- **SPX 1–2.5% below its ATH with VIX <20 and VIX/VIX3M <0.95** (2006–, n=119, de-clustered):
  - median 40-session maximum drawdown −1.7%;
  - 74% never closed more than 5% below the ATH within 40 sessions;
  - 94% never closed more than 10% below it.

**2. Index arithmetic caps the AI drag unless the other ~490 break [computed].**

A 126-day regression gives SPX ≈ 0.62×RSP + 0.118×SOXX (R² 0.75). Applied to Oct 6–14 it predicts −1.56% against the actual −1.28%, so it slightly *overstates* the drag.

| Scenario (from Oct 14 closes) | Implied SPX | vs ATH |
|---|---|---|
| SOXX to its Jul 29 low close of 465 (−10.5%), RSP flat | 7,619 | −2.6% |
| Same, but RSP back to its Sep 30 close of 208.02 | 7,528 | −3.7% |
| SOXX −25%, RSP flat | 7,462 | −4.6% |
| QQQ to −10% from its ATH (683.69), RSP flat (QQQ model) | 7,517 | −3.9% |

Getting past −5% requires a semis crash *and* new lows in equal-weight. Caveat: daily betas understate how correlated stocks become in a tail event.

**3. Breadth already corrected and has been rising while SPX fell** (breadth_timeseries.csv, 503 members).
- **A/D line:** it bottomed at 4,960 on Sep 30 and is now 5,686 (+726). It *rose* 238 during the Oct 6–14 SPX decline.
- **Members above their 20-day:** 22.7% on Sep 30, now 57.3%.
- **New 52-week lows:** 45 on Sep 24, 12 on Oct 14. There were 18 new highs on Oct 14.
- **Oct 8:** 339 advancers against 163 decliners, on a day NVDA fell 2.9%.
- **Sectors:** the median one-week return was positive in 9 of 11 sectors. Only IT (−5.52%) and Communication Services (−1.12%) were down.
- **RSP/SPY:** +1.1% since Oct 6 (betas_ratios.txt).

This is a rolling correction: the rest of the index corrected in Aug–Sep, and the leaders are correcting now.

**4. Volatility and investment-grade credit show no systemic stress** (DATA_BRIEF; macro_rates.md §E).
- **Volatility:** VIX 16.87 / VIX3M 18.79 = 0.90 (contango); VVIX 94.45 (42nd percentile); SPX 20-day realized volatility 10.3%.
- **Credit:** IG OAS 0.83% (43rd percentile of 3 years); BBB 1.03% (41st); HY OAS 3.16%, still below its Mar 30 high of 3.46%.

**5. The bond market absorbed the hot CPI** (macro_rates.md).
- The 10y closed at 5.19% on CPI day (−3bp; −12bp from the Oct 5 peak of 5.31%). ZN futures were +0.58 points overnight (≈ −6 to −8bp). The breakeven is flat at 2.35%.
- A year-end hike is priced above 95% [S], and Oct 28 hike odds faded to ~35% by 3:50 pm ET [S], so a hold on Oct 28 is a relief path.

**6. Trend structure is intact** (technicals.json).
- **Higher lows:** 7,313.92 (Jul 29), then 7,507.77 (Sep 16), then 7,616.78 (Oct 1).
- **Moving averages:** the 50-day and 200-day are rising 1.25% and 1.23% per 20 sessions. SPX is 6.27% above its 200-day and still 0.15% above its 50-day.
- **Momentum:** RSI is 49.5, and October set a monthly closing high.

**7. Seasonality** (macro_rates.md §D, 18 midterm years since 1954).
- **Oct 14 to Dec 31:** median +6.0%, up in 78% of years.
- **Worst close before Dec 31:** a median of only −0.75% versus Oct 14, though 22% of years saw worse than −5%.
- **After the election:** returns 6 and 12 months later were positive in 18 of 18 years.
- See the Fed-tightening caveat in §4.

**8. Lower-weight supporting evidence.**
- **AI fundamentals:** TSMC Q3 revenue +50.9% y/y (6-Ks, catalysts.md); ASML says 2027–28 demand exceeds its supply.
- **Sentiment:** CNN Fear & Greed 32.4 on Oct 14 (46.8 on Oct 6): fear with SPX only −1.3% off its high. UNVERIFIED (another agent's unpublished pull, `dl_sent/cnn_fg.csv`).

## 3. Key levels (closing basis; % vs the Oct 14 close)

| SPX level | % | Why it matters |
|---|---|---|
| 7,790.83 | +0.9% | AVWAP from the Oct 6 high. Reclaiming it means the pullback is over |
| 7,675–7,707 | −0.2 to −0.6% | SMA50 7,707.02; AVWAP from Sep start 7,699.44 and from the Jul low 7,686.6; unfilled part of the Oct 2 gap (7,684.75–7,693.31); EMA50 7,678.7; 3-month volume nodes 7,692 and 7,676.57. The overnight SPY quote (~7,682) is already testing this |
| 7,617–7,642 | −1.0 to −1.3% | 38.2% Fib of the Jul 29–Oct 6 swing (7,641.83); Oct 1 higher low (7,616.78) |
| **7,579–7,594** | −1.6 to −1.8% | SMA100 7,593.85 and 50% Fib 7,579.22. The core of my zone |
| 7,505–7,552 | −2.2 to −2.7% | Aug–Sep range floor (7,551.81 close, 7,504.78 intraday); 61.8% Fib 7,516.61; Sep 16 low 7,507.77. The last higher low in the uptrend |
| 7,418–7,450 | −3.5 to −3.9% | 6-month volume POC 7,418.54; AVWAP from Mar 30 7,450.03. The −5% line is 7,428. A break here means the pullback is not shallow |

**RSP support:**
- 210.96, where the Oct 14 low exactly matched the Sep 16 low;
- 209.15, the AVWAP from Mar 30;
- 208.02 / 207.16, the Sep 30 close and Oct 1 low (−1.9% to −2.3%);
- 206.51, the SMA200 (−2.6%);
- 204.90–205.52, the May 22 gap.

**RSP overhead:** SMA100 213.99 and SMA50 216.02.

## 4. Base rates and analogs: for and against

**Supporting:**
- The numbers in §2.1.
- **DATA_BRIEF analog** (SPX 0.5–3% below ATH, below its 50-day, above a rising 200-day; n=12): positive after 10 days 75% of the time; median 20-day maximum adverse move −1.8%, 25th percentile −3.4%.
- **RSP 3-year base rate:** once down 5%, the median final depth was −6.0% (n=5). RSP's −6.6% already matches that.

**Against (stated honestly):**
- **Narrow-leadership analog [computed]: the best bear analog.** Signals where SPX was 1–2% below its ATH while RSP was ≥4% below its own (2003–, n=15 signals, about 8 episodes):
  - median 40-session maximum drawdown versus the ATH was −5.9%;
  - only 47% stayed shallower than −5%, and 73% shallower than −10%;
  - the bad cases were 2007, 2015 and Feb 2025 (−18.6%).
  This roughly halves my base-rate edge.
- **Long-history RSP [computed]:** across 15 episodes that reached −6.6% (2003–), the median final depth was −9.1% (about 202.7). 53% undercut their low even after a 2% bounce, which is the situation now.
- **The recent SPX regime** (DATA_BRIEF, since Oct 2023): once −2% was reached, the median final depth was −5.3% (n=8), deeper than the long-run −4.4% [computed].
- **Fed-tightening midterm years** (macro_rates.md):
  - 1978: −11.6%, low on Nov 14;
  - 2018: −15.0%, low on Dec 24;
  - 1994: −5.0%;
  - 3 of 4 tightening midterm years fell from Oct 14 to Dec 31. 2026 is one.

## 5. Strongest counter-evidence to my own case

1. **Breadth never confirmed the ATH.**
   - The A/D line peaked on Aug 14 and is still 1,488 below that peak.
   - Only 34.7% of members are above their 50-day and 48.1% above their 200-day.
   - The median member is −15.2% from its 52-week high, and 70.5% of members are ≥10% off theirs.
   - RSP is below a *falling* 50-day (216.02; slope −0.57%).
   - "The 490 already corrected" can also be read as "the 490 are in a downtrend and the leaders are now joining them."
2. **AI credit is cracking.**
   - CCC OAS is 12.67%, a 3-year high, up 191bp in a month. HYG is at its 2026 low.
   - CoreWeave bonds yield about 15% [S], and Oracle was cut to BBB− [S].
   - If AI-capex funding breaks, the "RSP flat" assumption in my scenarios fails. QQQ at −10% with RSP back at 208 already gives about 7,459 (−4.6%) [computed].
3. **Macro offers no put.**
   - The Fed is hiking into 3.7% CPI.
   - The 10y is 5.19–5.21%, near a 24-year high. The real 10y is 2.88%, after a 2.95% peak that was the highest since 2008.
   - The stock/yield correlation is +0.47 so far in Q4 (about 9 sessions).
4. **There has been no capitulation.** If the low turns out deeper, VIX contango means the flush has not happened yet.
5. **The event calendar is dense:** FOMC plus MSFT/GOOGL earnings (Oct 28), GDP+PCE (Oct 29), midterms (Nov 3), refunding (Nov 4), payrolls (Nov 6), CPI (Nov 10). My "low by Oct 30" needs Oct 28 to pass without a hike *plus* escalation.
6. **The overnight tape is already testing the first support band** (SPY at about 7,682 equivalent), before PPI and retail sales (8:30 am Oct 15) and TSMC.

## 6. What would prove me wrong

**Price (closing basis):**
- **SPX below 7,507.77** (Sep 16 low, −4.0% from the ATH): the higher-low structure is broken, so the thesis is wrong in shape.
- **SPX below 7,428** (−5%): the thesis is wrong in depth.
- **Early warning:** two closes below the SMA100 (7,594) while RSP is below 207.16.
- **RSP below 207.16** (Oct 1 low), and especially below 206.51 (SMA200): the equal-weight rebound has failed, and the rolling-correction premise is wrong.
- **S&P A/D line below its Sep 30 low of 4,960** (breadth_timeseries.csv).

**Stress gauges:** VIX/VIX3M above 1.0 for two or more sessions; HY OAS above 3.46%; IG OAS above 1.0%; 10y close above 5.31% or real 10y above 3.0%.

**Events:**
- **Oct 21 (META) and Oct 28–29 (MSFT, GOOGL; AMZN date estimated):** 2027 capex "digestion" or cuts, or the spenders' own stocks falling hard on higher capex.
- **Oct 28 FOMC:** a hike *plus* a signalled follow-up or talk of 50bp.
- **Data:** Oct 29 core PCE ≥0.3% m/m; Nov 6 negative payrolls with unemployment ≥4.4%; Nov 10 core CPI ≥0.3% m/m.

**Time:** if SPX is still making lower closing lows after Nov 6, the "soon" half of the thesis fails even if the depth stays shallow.

**Confirmation:** a close above 7,790.83 (the Oct 6 AVWAP), then above 7,818.93.

---

*Sources:*
- DATA_BRIEF.md, technicals.json, levels.json, breadth_timeseries.csv, betas_ratios.txt;
- macro_rates.md (FRED, BLS, Fed; FedWatch snapshots are [S]);
- catalysts.md (TSMC 6-Ks);
- oct8_narrative.md and oct8_skeptic.md (credit items [S]);
- IBKR MCP snapshots (03:10–03:20 UTC Oct 15);
- WebSearch, ~03:20 UTC: TSMC results not yet published, e.g. [Crypto Briefing preview](https://cryptobriefing.com/tsmc-record-profit-sixth-quarter-ai/).
