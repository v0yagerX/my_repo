# audit_market: numbers audit of market_verdict.md / market_verdict.json

Audited files: `analysis/market_verdict.md` and `analysis/market_verdict.json`. Both exist.

Method: I wrote my own code in `scratchpad/audit_mkt_code/a1.py`–`a7.py`. None of it imports the team's scripts. Inputs were:
- `dl_spxlong/gspc.json` (^GSPC 1950–). On the 14,318 overlapping days it matches `analysis/sent/long/_GSPC.csv` with a maximum relative difference of 2e-16.
- `dl_bull_long` (RSP 2003–, VIX, VIX3M), `analysis/sent/long` (^NDX, ^SOX), `dl_fred` (DGS10, DFII10, ACM, ICE OAS) and `data/*.csv`.

IBKR, read-only: SPY 765.86, −3.74 (−0.49%) vs a 769.60 prior close (real-time, about 03:57 UTC Oct 15). This is consistent with the verdict's SPY 765.75 / −0.50% and its ≈7,680 S&P 500 scaling.

## ERRORS

| # | Sev | Claim (where) | Correct value | Evidence |
|---|---|---|---|---|
| 1 | **HIGH** | §4 row "+ NDX ≥4% below its 20-day high (today's state), n=35, **40/40/20**". It is presented as a filter added to row 1 (0.8–2.0% below a record ≤10 sessions old, above a rising 200-day). §4 calls it "the best-matched set" and uses it as the anchor for the net 40/38/22 and for the "median ≈7,480 below the hinge" claim. | **Applied to the stated base: n=26, 58/19/23** at the verdict's own hinges (7,505 = −4.015%, 7,314 = −6.458%), or 50/27/23 with 4.0/6.5 cut-offs. The 40/40/20 figure only reproduces on a different, looser base (SPX 0.5–2.5% below the record, no 200-day filter; `mv/verify5.py`) **and** with 4.0% instead of 4.015% as the cut-off. Correctly bucketed, the loose base gives **n=35, 46/34/20**. | a1.py/a2.py. Two of the 35 signals (1992-01-21 and 2021-05-10) had 36-session lows of −4.01%. That maps to about 7,506, which is inside the shallow bucket, but 40/40/20 counts them as deeper. |
| 2 | MED | §4 row "+ SOX ≥10% below its 20-day high, n=12, 50/25/25". Same mislabel. | Stated base: **n=11, 55/18/27**. 50/25/25 only reproduces on the loose verify5 base. | a1.py/a2.py |
| 3 | MED | All the 36-session calibration rows are bucketed at 4.0% / 6.5%, but the scenario hinges are 7,505 (−4.015%) and 7,314 (−6.458%). This moves outcomes between −4.000% and −4.015% from shallow into deeper. | 1950–: **58/24/18** (stated 57/25/18). 2004–: **62/21/18** (stated 59/24/18). NDX: see #1. The bias always points toward "deeper". | a1.py vs a2.py; 4 of the 68 signals since 2004 sit at −3.95% to −4.06% |
| 4 | MED | §9: "A close below 7,505 with RSP below 207.16 → deeper becomes the base case at about 55%, with a trend break at about 30%." | These sum to 85%. Shallow is defined as "lowest close ≥7,505", so once any close prints below 7,505 its probability is **0**. Deeper plus trend break must equal 100 (for example about 65/35). | Scenario definitions, MD table and JSON |
| 5 | MED | "Most likely closing-low zone 7,420–7,600" and "median of my distribution about 7,480" | Much of that zone, and the median itself, sits in the **7,460–7,540 gap**, which is in neither the shallow zone (7,540–7,650) nor the deeper zone (7,370–7,460). With P(≥7,505)=40% and a median of 7,480, at least 10 percentage points must lie in 7,480–7,505. So 10 of the deeper bucket's 38 points (26%) sit **above** its stated zone. Zones, median and most-likely band are not mutually consistent. | Arithmetic on the verdict's own numbers |
| 6 | MED | "To get below 7,505, both legs must fall: tech and equal weight" (MD §3, JSON internals, bull point 2) | Using the verdict's own 126-day model (0.397·RSP + 0.414·QQQ, R² 0.911, which I reproduced), **QQQ ≤680.2 (−10.5% from its record) breaks 7,505 on its own with RSP flat.** At QQQ's cited recent-regime median of −11.75% (670.4) with RSP flat, the model gives **≈7,462 (deeper)**. The claim contradicts §5.1. | a4.py |
| 7 | MED | JSON `upper_layer_conditioning` is `""` | MD §10 has the content (QQQ thresholds, timing for the higher-beta lows). Downstream layers reading the JSON get nothing. | market_verdict.json |
| 8 | LOW | §5: "cut shallow from about 50% (the average of the tech-state sets) to 40%" | The average of the two tech-state rows as reported is (40+50)/2 = **45%**. With the corrected rows (#1–#2) it is 48–56%. | Arithmetic |
| 9 | LOW | §4 row "Fed-tightening midterms (1994/1978/2018), n=3, 0/1/2" | macro_rates.md lists **four** tightening midterm years, and the verdict itself counts four in "3 of 4". 2022's worst close from Oct 15 to Dec 31 was **+2.3%** vs Oct 14 (shallow). With n=4 the split is **1/1/2**. | a5.py. 1978 −11.63% (Nov 14), 1994 −5.04%, 2018 −15.03% (Dec 24) and 2022 +2.31% all match MR otherwise. |
| 10 | LOW | "Rising 200-day, projected at about 7,340–7,410 for late Nov to early Dec [flat price path]", used in the deeper zone and the key-level table | 7,410 needs price held flat at **7,719** until Dec 4. On deeper-scenario paths the 200-day is lower: flat at 7,450–7,505 gives **7,332–7,370** (Nov 19 to Dec 4). The range mixes paths, and the top end is about 40 points high for the scenario it supports. | a4.py: flat 7,719 → 7,367/7,387/7,409 (Nov 19/27, Dec 4); flat 7,505 → 7,339/7,354/7,370 |
| 11 | LOW | §5.3: RSP median −9.1% "about 202.7" | 222.77 × (1 − 0.0913) = **202.44** | a3.py (n=15, median −9.13%) |
| 12 | LOW | "SOXX fell 29%, XLK 16% and QQQ 11.3% (Jun 2 – Jul 29)" | SOXX's −29.0% runs **Jun 22**–Jul 29. From Jun 2 to Jul 29 SOXX fell **−23.1%**. The QQQ (−11.3%) and XLK (−16.0%) figures are right. | a4.py |
| 13 | LOW | §10: QQQ "at or above about 695 (−8.5%) if RSP slips to 210" | The model breakeven for 7,505 with RSP at 210 is **QQQ 687.1 (−9.55%)**. With RSP flat it is **680.2 (−10.5%)**, against "about 684". | a4.py |
| 14 | LOW | JSON `verdict_confidence`: "real yields at a 24-year high" | The 10-year real yield of 2.95% is the highest since **Nov 2008** (an 18-year high). The 24-year high is the *nominal* 10-year at 5.31%. | DFII10 / DGS10 files; MR |
| 15 | LOW | Breadth: "The prior days ran 339/163, 319/184 and 321/179" | These are Oct 8, 9 and 12. The verdict skips the immediately prior day, **Oct 13 at 265/237**, which already showed the thinning. | breadth_timeseries.csv |
| 16 | LOW | Close-based scenario hinges use intraday levels | 7,314 is the Jul 29 **intraday** low (the close was **7,316.15**). 7,505 is the intraday range floor 7,504.78 (the Aug–Sep closing low was 7,551.81). The effect is trivial (about 0.03%) but the definitions are mixed. | data/_GSPC.csv |
| 17 | LOW | Credit framing: "IG OAS 0.83%, 43rd percentile of 3 years … calm" | The level is right. On a 1-year basis IG is at the **80th–84th percentile** (MR table: 80th), which the verdict omits while citing HY on a 1-year basis (91st). The selective window flatters the "calm IG" pillar. | a7.py; MR §E |
| 18 | LOW | §4 row "Episodes since Oct 2023 that reached −1.78%, n=16, 56/25/19" | Reproduces exactly (9/4/3), but it measures ATH-to-ATH final depth with no time limit. Every other row measures the 36-session window, so the row is not comparable to the others. | a1.py |
| 19 | LOW | Calendar: "Fri Oct 30 … BoJ" | MR puts the BoJ decision at about 11 pm ET **Thu Oct 29**. MR tags the ECB and BoJ dates [S], but the verdict's calendar drops that tag. | macro_rates.md §4 |
| 20 | LOW | JSON trend-break tail "6,560–6,820 (−12.7% to −16.1%)" | 6,820 is **−12.8%** from 7,818.93 | Arithmetic |

**Methodological caveat (not counted as an error).** The 36-session forward windows are de-clustered only 20 sessions apart. In the 1950– base set, 109 of 207 consecutive signals have overlapping windows, so the effective sample sizes are roughly half the stated n. The "16 of 19 VIX/VIX3M ≥1.0" result reproduces, but 4 of the 16 hits are marginal (1.00–1.02: 2013, 2015–16, 2019-06 and 2022).

## Load-bearing computations re-run independently

| Computation | Verdict | My result | Reproduces? |
|---|---|---|---|
| A. ATH-to-ATH episodes since 1950 reaching −1.28% | n=252, median −3.2%, 71/84/90% shallower than 5/7.5/10% | n=252, −3.19%, 70.6/83.7/89.7 | **Yes** |
| B. Recent regime (since Oct 2023), unbiased: given −2% / −3% / −1.78%; and the biased n=8 | −2%: n=15, −3.2%, 40% ≥4.5%. −3%: 7 of 8 reach ≥4%. −1.78%: n=16, 56/25/19. Biased: n=8, −5.3% | −2%: 15, −3.17%, 40.0%. −3%: 8, 7 of 8. −1.78%: 16, 56/25/19. Biased: 8, −5.29%, 6 of 8 | **Yes**. The verdict's selection-bias finding against base_rates.py (`episodes(df, 0.03, …)`) is **correct**. |
| C. 36-session calibration sets | 57/25/18 (n=208); 59/24/18 (n=68); NDX 40/40/20 (n=35); SOX 50/25/25 (n=12); RSP 29/14/57 (n=7); 10-year 53/47/0 (n=15) | 58/24/18; 62/21/18; **NDX on the stated base 58/19/23 (n=26)**; SOX 55/18/27 (n=11); RSP 29/14/57; 10-year 53/47/0 | **Partly.** RSP and 10-year: yes. Base rows: yes only with the wrong 4.0% cut-off. **NDX and SOX: no**, because they are computed on a different base. |
| D. VIX/VIX3M ≥1.0 within about a week of the trough, ≥5% drawdowns since 2007 | 16 of 19; exceptions 2020-09 (0.88), 2021-10 (0.97), 2024-04 (0.98) | 16 of 19, the same three exceptions (±5 sessions or ±8 calendar days; all hits also occur before the trough) | **Yes** |
| E. RSP episodes reaching −6.6% since 2003 | n=15, median −9.1%, 60% shallower than −10% | n=15, −9.13%, 60% | **Yes** (price 202.44, not 202.7) |
| F. Concentration regressions and the implied-S&P table | 0.40·RSP + 0.41·QQQ (R² 0.91); 0.62/0.118 (R² 0.75); 0.57/0.29 (R² 0.86); 7,571 / 7,520 / 7,461 / 7,273 / 7,019 | 0.397/0.414 (0.911); 0.620/0.118 (0.747); 0.572/0.286 (0.860); 7,571 / 7,520 / 7,461 / 7,273 / 7,019 | **Yes** |
| G. Narrow-leadership analog (JSON): n=16, 56% vs 33% | — | n=16, 56% vs 33% (n=73 base) | **Yes** |
| H. Midterms | median +6.0%, 78% up, median worst −0.75% | +6.01%, 78%, −0.74% | **Yes** |

## Could not be verified

- **IBKR pulls I could not repeat:** ES Dec 7,732.75 (−0.48%, 03:19 UTC) and RSP 211.73 (00:28 UTC). The prior-settle arithmetic is consistent with live_snapshots.md (7,770.25).
- **FedWatch figures:** 35% late Oct 14, 49–54% intraday, and >95% for a hike by year-end. Single-source tags are preserved as MR gives them; MR tags the intraday range [M], not [S].
- **Credit anecdotes:** CoreWeave at about 15% YTM (it matches oct8_narrative.md's 14.8–14.9%, "briefly >15%", LSEG via coverage), Oracle at BBB−, hyperscaler CDS records. The secondary/[S] tags are preserved.
- **TSMC timing:** "not out at 03:35 UTC" and "due 05:30–06:00 UTC".
- **Earnings dates:** NVDA Nov 17/18 and AMZN Oct 29 are flagged UNVERIFIED. META Oct 21, MSFT/GOOGL Oct 28, INTC Oct 29 and AMD Nov 3 are CONFIRMED in catalysts.md.
- **Judgment numbers:** the net 40/38/22, the median of about 7,480, the 75–80% band for 7,250–7,650, and the 55%/30% conditional update (which is incoherent anyway; see #4).
- **Percentile conventions:** HY at the 91st percentile (1y), IG at the 43rd (3y), BBB 1.03, DFII10 2.88/2.95, ACM 1.07, CCC 12.67 (+1.91 in a month) and HY +51 bp in a month. Levels and changes match FRED exactly. My percentiles (≤ convention) are HY 92 and IG 47, so the differences come from the convention, not the data.

## Claims verified OK

About **250** discrete numeric claims matched. Duplicates between the MD and JSON are counted once. They include:
- **Index state:** all S&P 500, SPY, RSP, QQQ, XLK and SOXX levels, MAs, slopes, drawdowns and session counts.
- **Scenario arithmetic:** every scenario boundary and bottom-zone drawdown (from the record close and from the Oct 14 close). Each zone lies inside its own boundary, and 40+38+22 = 100.
- **Key levels:** every key-level price and % distance (12 S&P 500 rows and 7 RSP levels, all on the correct Oct 14 base). The JSON `distance_pct` values are the midpoints of each range.
- **Technical levels:** Fibonacci levels (7,641.83 / 7,579.22 / 7,516.61 / 7,427.47), anchored VWAPs, volume POC/nodes and gaps.
- **Breadth:** A/D 7,174 (Aug 14) / 4,960 (Sep 30) / 5,448 / 5,706 / 5,686, the +238 and +726 moves, all breadth percentages, and the sector shares.
- **Relative performance and volatility:** RSP/SPY 0.2710 (Oct 7), +1.1% and −2.0%; IWM −11.05%, XLI −10.44%, XLF −6.26% since Aug 14 (IWM's 52-week high was also Aug 14); VIX, VIX3M, VVIX and the 0.898 ratio.
- **Rates and credit:** the levels in MR.
- **Seasonality:** the midterm statistics.
- **Calendar:** every weekday and every expiration rule (Oct 16 and Nov 20 option expirations; VIX expirations Oct 21 and Nov 18). There are 36 sessions from Oct 15 to Dec 4.
- **Other:** S&P 500 YTD +12.76%; −1.93% intraday vs −1.61% close basis; the 7,584 and 7,428 lines; the 6,824/6,561 tails; the QQQ −11.75% and XLK −16.0% base rates.

## Does any error change the verdict's scenario probabilities, zones or key level?

**Yes for the probabilities. No for the key level, and only at the edges for the zones.**
- **Probabilities.** The verdict says its net 40/38/22 sits on the "best-matched set" of 40/40/20, and its median of lows "below 7,505" depends on that anchor. That set is mislabelled and bucketed at the wrong cut-off (#1, #3). Correctly computed, the tech-state sets give shallow at **46–58%**, not 40%. The base rates give 58–62% (#3), and the tightening-midterm set gives 1/1/2 rather than 0/1/2 (#9). Following the verdict's own method (anchor on the matched set, then make a net-bearish adjustment of a few points) gives roughly **45–48 / 33–35 / 19–20**. That makes shallow clearly the modal bucket and puts the median low at or just above 7,505. The "coin flip, median below the hinge" framing does not survive. A 40% shallow figure can only stand as an explicit judgment overlay of about 6–18 points below the data, and the verdict would have to say so.
- **Conditional update.** The §9 update must be restated so it sums to 100 (#4).
- **Zones.** The scenario zones need no change. However, the 7,420–7,600 "most likely" band and the 7,480 median are inconsistent with them (#5), and the top of the deeper zone's 200-day support should be about 7,370, not 7,410 (#10).
- **Key level.** 7,505 on a closing basis, paired with RSP 207.16, is unaffected. #6 also means a tech-only break of 7,505 is plausible at QQQ's base-rate median, so 7,505 matters even more as a tripwire.
