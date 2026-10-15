# Layer 1 verdict: the broad US market (S&P 500 / SPY, equal-weight RSP)

*Written about 03:45 UTC Oct 15 (11:45 pm ET Oct 14); data through the Oct 14 close.*

**Source tags:** [DB] = data/DATA_BRIEF.md and companion files; [MR] = research/macro_rates.md; [CAT] = research/catalysts.md; [calc] = my own scripts in `scratchpad/mv/verify1–5.py` (Yahoo ^GSPC 1950–, RSP 2003–, ^SOX 1994–, ^NDX 1985–, VIX/VIX3M, FRED DGS10).

**TSMC:** Q3 results were **not out** at about 03:35 UTC (WebSearch). They are due about 05:30–06:00 UTC and are not used here.

## Bottom line

| Scenario (lowest S&P 500 **daily close**, Oct 15 – Fri Dec 4) | Boundary | Prob. | Bottoming zone | Drawdown from the 7,818.93 record close | Low most likely forms |
|---|---|---|---|---|---|
| **Shallow pullback** | Low ≥ **7,505** | **40%** | 7,540–7,650 (core 7,580–7,620) | −2.2% to −3.6% | Oct 15–30, most likely by Oct 23 |
| **Deeper correction** | 7,314 ≤ low < 7,505 | **38%** | 7,370–7,460 | −4.6% to −5.7% | Oct 27 – Nov 10 |
| **Trend break** | Low < **7,314** (Jul 29 low; below the rising 200-day) | **22%** | 6,850–7,250 (tail to about 6,560) | −7.3% to −12.4% (tail −16%) | Nov 10 – Dec 4, with real risk the low comes after the window |

**Shallow is the most likely bucket, but only just.** The median of my distribution of lows is about **7,480**, below the 7,505 hinge. Whether this ends as a shallow pullback or a deeper correction is a coin flip, and the **7,505 close** decides it.

**Most likely closing-low zone: 7,420–7,600.** That is −2.8% to −5.1% from the record close, or −1.5% to −3.9% from the Oct 14 close.

**This is not a call to buy the dip.** Three of the five things a durable low usually shows are missing: a volatility capitulation, credit stabilising, and a breadth thrust. Only two are present: rates have stopped rising and investment-grade credit is calm.

**RSP is on its own clock.** It is −4.8% from its Aug 14 record of 222.77, and its correction low was 208.02 on Sep 30 (−6.6%). Mapped onto the scenarios:
- **Shallow:** RSP holds **207.16** (zone 207.2–211).
- **Deeper:** RSP undercuts 207.16 and its 200-day of 206.51 (zone 201–207).
- **Trend break:** RSP closes below **200.5** (−10%).

## 1. Where the pullback stands [DB]

**S&P 500: 7,718.94.**
- −1.28% from the record close (Oct 6) and −1.6% from the intraday record of 7,844.52. This is session 6 of the pullback.
- Above the 50-day 7,707.02 (+0.15%), 100-day 7,593.85 (+1.65%) and 200-day 7,263.43 (+6.27%). The 50-day and 200-day are both rising.
- Higher lows are intact: 7,313.92 (Jul 29), 7,507.77 (Sep 16), 7,616.78 (Oct 1).

**Overnight (IBKR):** SPY 765.75, −0.50% (real-time, 03:28 UTC), which is about **7,680 on the S&P 500** by my scaling (UNVERIFIED). ES December was 7,732.75, −0.48% (delayed). The first support band is already being tested.

**RSP: 212.09.** It is below its falling 50-day (216.02, slope −0.57%), above its 200-day (206.51), and just under its Oct 13 lower high of 213.30.

The S&P 500 is in week 2 of an AI- and semis-led pullback. The average stock is in month 2 of a broad correction and a bounce.

## 2. Checking the advocates' numbers

| Claim | Status |
|---|---|
| Bull: since 1950, ATH-to-ATH episodes that reached −1.28% had a median final depth of −3.3%, with 70/84/90% shallower than −5/−7.5/−10% | **Confirmed** [calc]: n=252, median −3.2%, 71/84/90% |
| Bull: S&P 500 ≈ 0.62·RSP + 0.118·SOXX (R² 0.75). Bear: S&P 500 ≈ 0.57·RSP + 0.29·XLK (R² 0.86) | **Confirmed** [calc] |
| Bear, since Aug 14: IWM −11.05%, XLI −10.44%, XLF −6.26%. RSP/SPY at a 1-year low of 0.2710 on Oct 7 | **Confirmed** [calc] |
| Bear: before September 2026, the lowest share above the 200-day when the index was within 1% of a record was 53.4% (May 13) | **Confirmed** (breadth series starts Aug 2025) |
| Bull: of RSP episodes that reached −6.6%, the median final depth was −9.1% (n=15) | **Confirmed**; 60% ended shallower than −10% |
| **Both:** "since Oct 2023, once the index reached −2%, the median final depth was −5.3% (n=8); 6 of 8 went to −4.5% or worse" | **WRONG (selection bias).** base_rates.py counts only episodes that went on to ≥3%. Unbiased recount given −2%: **n=15, median −3.2%, 40% reached −4.5%**. The n=8 / −5.3% figures are really the *given −3%* statistic, so the bear's "≈7,405" target is overstated |
| Bear: "intraday low −1.93%" | Measured against the intraday high. Against the record close it is −1.61% |
| catalysts.md: about 54% odds of an October hike | That was the intraday peak; the late-day figure was about 35% (single source) [MR] |

**The corrected statistic still leaves a real tripwire.** Since Oct 2023, 7 of the 8 episodes that reached **−3% (7,584)** went on to −4% or worse.

## 3. Internals

**Breadth** (503 current members; survivorship bias) [DB]
- **A/D line:** peaked **Aug 14** at 7,174. It is now 5,686, so it has not confirmed the Oct 6 high. It bottomed at 4,960 on Sep 30, and it *rose* 238 while the index fell from Oct 6 to Oct 14.
- **Members above their averages:** 57.3% (20-day), 34.7% (50-day), 40.5% (100-day), 48.1% (200-day).
- **Highs and lows:** 18 new highs, 12 new lows. The median member is −15.2% from its 52-week high, and 70.5% of members are ≥10% off theirs.
- **The rotation cushion is thinning.** Oct 14 had 241 advancers and 261 decliners, the first net-negative day since Oct 7. The prior days ran 339/163, 319/184 and 321/179.
- **The rotation went into defensives.** The share above the 50-day is 66.7% in Energy, 61.7% in Health Care and 52.9% in Staples. It is 19.7% in Financials, 18.1% in Industrials and 13.3% in Real Estate.
- **RSP/SPY:** +1.1% since Oct 6, but still 2.0% below its 50-day.

**Volatility**
- VIX 16.87; VIX/VIX3M **0.898** (contango); VVIX 94.45 [DB].
- In **16 of 19** S&P 500 drawdowns of 5% or more since 2007, VIX/VIX3M reached ≥1.0 within about a week of the trough [calc]. The exceptions were 2020-09 (0.88), 2021-10 (0.97) and 2024-04 (0.98).
- So a deeper low without a VIX-curve inversion is possible but unusual. A shallow low needs no inversion at all.

**Rates and the Fed** [MR]
- **Yields:** 10-year 5.19% (5.31% on Oct 5, the highest since 2002). 10-year real yield 2.88% (2.95% peak, the highest since 2008). Term premium 1.07.
- **Policy:** the Fed hiked to 3.75–4.00% on Sep 16. The September projections put end-2026 at 4.1%.
- **Pricing:** odds of an Oct 28 hike were **about 35% late on Oct 14**, after an intraday 49–54% (single source). At least one hike by year-end is priced above 95%.
- **Overnight:** ZN futures were +0.58 points, about −6 to −8 bp in yield.
- **Stock–yield correlation:** turned to +0.47 in Q4. That is only 9 sessions of data, but it is a growth-scare tell.

**Credit** [MR, FRED]
- **HY OAS 3.16%:** 91st percentile of 1 year, +51 bp in a month. Still below the Mar 30 high of 3.46%.
- **CCC OAS 12.67%:** a 3-year high, +191 bp in a month.
- **IG OAS 0.83%:** 43rd percentile of 3 years. BBB is 1.03%.
- **HYG** is at a 1-year low.
- **AI-linked credit:** CoreWeave bonds at about 15% yield to maturity. Oracle's downgrade to BBB− is single-source.

**Concentration** [calc]

A 126-day regression gives **S&P 500 ≈ 0.40·RSP + 0.41·QQQ** (R² 0.91). These are linear betas, which understate how closely stocks move together in a tail.

| QQQ low | RSP low | Implied S&P 500 | Scenario |
|---|---|---|---|
| ≈699 (−8% from record) | 211 | ≈7,571 | Shallow |
| 683.7 (−10%) | 212.09 | ≈7,520 | Shallow, barely |
| 683.7 (−10%) | 208.02 | ≈7,461 | Deeper |
| 645.7 (−15%) | 206.51 | ≈7,273 | Trend break |
| 607.7 (−20%) | 200.49 | ≈7,019 | Trend break |

- **To get below 7,505, both legs must fall:** tech and equal weight.
- **The June–July 2026 precedent.** SOXX fell 29%, XLK 16% and QQQ 11.3% (Jun 2 – Jul 29), yet the index's worst close was only −4.5% (Jun 10), because RSP rallied to new highs [calc].

**Seasonality** [MR]
- **All midterm years** (n=18): Oct 14 → Dec 31 has a median of +6.0% and is up 78% of the time. The median worst close is −0.75%. Returns 6 and 12 months after the election were positive 18 of 18 times.
- **Fed-tightening midterms — 1978, 1994 and 2018 are the most relevant:**
  - 1978: −11.6% from the Oct 14 level, low on Nov 14.
  - 2018: −15.0%, low on Dec 24.
  - 1994: −5.0%.
  - Oct 14 → Dec 31 was negative in 3 of 4 tightening years. **2026 is one of them.**

## 4. Calibration: base rate, then regime

| Reference set [calc unless noted] | n | Shallow / Deeper / Trend break |
|---|---|---|
| Index 0.8–2.0% below a record set ≤10 sessions earlier, above a rising 200-day; 36-session window, 1950– | 208 | 57 / 25 / 18 |
| Same, 2004– | 68 | 59 / 24 / 18 |
| Episodes since Oct 2023 that reached −1.78% (the overnight level) | 16 | 56 / 25 / 19 |
| + NDX ≥4% below its 20-day high (today's state) | 35 | **40 / 40 / 20** |
| + SOX ≥10% below its 20-day high | 12 | 50 / 25 / 25 |
| + RSP ≥3% below its 52-week high (narrow breadth) | 7 | 29 / 14 / **57** |
| + 10-year up ≥40 bp in 3 months | 15 | 53 / **47** / 0 |
| Fed-tightening midterms (1994 / 1978 / 2018), from the Oct 14 level [MR] | 3 | 0 / 1 / 2 |

**The base rate is about 57/25/18.** Conditioning on the tech damage already done, which is today's actual state, gives **about 40/40/20** on the best-matched set (n=35).

**Bearish adjustments:**
- Narrow breadth and an A/D line that did not confirm the high. The samples are small but point toward a trend break.
- A hiking Fed with real yields at 2008 highs. In the rate analogs this pushes outcomes into the *deeper* bucket rather than a break.
- Junk and AI credit are widening.
- The rotation is going into defensives, and small caps are 11% off their highs.

**Bullish adjustments:**
- Breadth has improved since Sep 30, which is unlike a classic top.
- Investment-grade spreads are calm, and VIX is in contango.
- Bonds absorbed a hot CPI.
- The June–July rotation cushion held the index to −4.5%.

**Net: 40 / 38 / 22.** I took weight off a trend break relative to the narrow-breadth set, because the rate analogs and calm IG credit argue against a crash-type move. Most of the extra bear weight went into the deeper bucket, where the concentration arithmetic puts the central bear path.

## 5. The strongest case that "shallow" is wrong (and what I changed)

1. **The tech leg is only halfway through its base rate.** Since Oct 2023, once QQQ was down 5%, its median final drawdown was −11.75%. For XLK it was −16% [DB]. QQQ is about −5% overnight.
2. **At QQQ −12% (about 668), the index needs equal weight to rally.** RSP would have to gain about 1.7%, to about 215.5 near its falling 50-day, just to hold 7,505.
3. **The rotation is fading, and RSP's own history points lower.**
   - Oct 14 was net negative, and the money went into defensives.
   - RSP episodes that reached −6.6% had a median final depth of −9.1%, about 202.7.
4. **The calendar is dense.** Oct 27 – Nov 6 brings about a 35% hike risk, MSFT and GOOGL on FOMC night, PCE, the midterms, the refunding and payrolls. A shallow outcome needs nearly all of them to pass benignly.
5. **The −3% line (7,584) is only 1.7% away.** Once it was hit, 7 of 8 recent episodes went to −4% or worse.

**This is persuasive.** It is why I cut shallow from about 50% (the average of the tech-state sets) to 40%, which puts my median below 7,505.

**Why I did not cut further:**
- The most recent identical setup (June–July 2026) ended at −4.5%, right on the hinge rather than in a breakdown.
- IG credit, the VIX curve and the bond market do not confirm a broad de-risking.

## 6. Scenarios

**Shallow (40%): lowest close ≥ 7,505**
- **Zone:** 7,540–7,650. The core is 7,580–7,620: the 100-day 7,594, the 50% Fibonacci level 7,579 and the Oct 1 low 7,617.
- **Timing:** the low forms Oct 15–30, most likely by Oct 23 (Oct 16 options expiration; Oct 21 META and VIX expiration).
- **Path:**
  1. QQQ falls to about 695–710 while RSP holds 210–212.
  2. The index tests 7,580–7,640.
  3. The Fed holds on Oct 28 without escalating, and investors accept hyperscaler capex.
  4. The index reclaims 7,790.83 (the Oct 6 anchored VWAP) in November and retests its record around NVDA's results.
- **Confirming signals:**
  - RSP closes above 210.96 and never below 207.16.
  - The A/D line rises on down days for the index.
  - VIX peaks below about 22, with VIX/VIX3M below 0.95.
  - HY OAS stays at or below 3.25%, and the 10-year below 5.31%.
  - Semis close green and hold after TSMC and hyperscaler results.
  - The index closes back above 7,707, then 7,790.83.
- **Invalidation:**
  - A close below 7,505.
  - Two closes below 7,584 while RSP is below 208.02.
  - RSP closes below 207.16.
  - VIX/VIX3M above 1 for two sessions.
  - HY OAS above 3.46%.

**Deeper correction (38%): 7,314 ≤ lowest close < 7,505**
- **Zone:** 7,370–7,460. Supports cluster here:
  - the VWAP anchored at Mar 30, 7,450;
  - the −5% line, 7,428;
  - the 78.6% Fibonacci level, 7,427;
  - the 6-month volume point of control, 7,418.5;
  - the rising 200-day, projected at about 7,340–7,410 for late Nov to early Dec [calc, flat price path].
- **Timing:** the low forms Oct 27 – Nov 10 (FOMC, MSFT/GOOGL and PCE, then midterms, refunding, payrolls and CPI).
- **Path:**
  1. QQQ falls 10–13%, to about 660–685.
  2. The rotation fails and RSP drops to 205–208.
  3. The 7,505 range floor breaks around Oct 28–29.
  4. A VIX spike into the low to mid 20s, with a brief curve inversion, marks the low.
  5. The index recovers into NVDA's results.
- **Confirming signals:**
  - A close below 7,505 with RSP below 207.16.
  - VIX/VIX3M above 1 on the flush.
  - HY OAS at 3.3–3.46% but not above, and IG below 1.0%.
  - The A/D line holds above 4,960.
- **Invalidation:**
  - Upside: the index holds 7,505 through Nov 6 and reclaims 7,790.83.
  - Downside: a close below 7,314, HY OAS above 3.46%, the A/D line below 4,960, or VIX/VIX3M above 1 for three or more sessions.

**Trend break (22%): lowest close < 7,314**
- **Zone:** 6,850–7,250. Stepping stones on the way:
  - 7,252–7,263: today's 200-day and the YTD anchored VWAP;
  - 7,037: −10% from the record;
  - 6,887–6,905: the unfilled Apr 14 gap.
- **Tail:** the tightening-midterm analogs reach about 6,824 (1978) and about 6,561 (2018).
- **Timing:** the low forms Nov 10 – Dec 4. The low could come after Dec 4: the Dec 9 FOMC and Dec 11 continuing-resolution deadline follow, and in 2018 the low came on Dec 24.
- **Path:**
  1. The Fed hikes on Oct 28 or escalates, and the 10-year breaks 5.31%. Alternatively, a stagflation scare: negative payrolls on Nov 6 alongside a hot Nov 10 CPI.
  2. AI-credit stress spreads and HY OAS rises above 3.46%.
  3. RSP falls below 200.5.
  4. NVDA's results fail to stop it.
- **Confirming signals:**
  - The A/D line below 4,960, and fewer than 40% of members above their 200-day.
  - IG above 1.0%, CCC above 13–14%.
  - VIX/VIX3M above 1 for three or more sessions.
  - The 10-year above 5.31%, or the real yield above 3.0%.
  - Escalation with Iran after the election.
- **Invalidation:**
  - Every close through Dec 4 holds 7,314.
  - A quick reversal after a flush, with HY OAS back below 3.0% and the VIX curve back in contango. A 2024-style V-shaped flush still counts as a trend break on price.

## 7. Key levels (S&P 500 closes; % vs the 7,718.94 close)

| Level | Type | % | Why |
|---|---|---|---|
| 7,818.93 / 7,844.52 | Resistance | +1.30 / +1.63 | Record close and intraday record. A close above, with RSP above 216, confirms the high |
| 7,790.83 | Resistance | +0.93 | VWAP anchored at the Oct 6 high. Reclaiming it ends the pullback |
| 7,733–7,769 | Resistance | +0.19 to +0.65 | 20-day, 21-day EMA and 10-day |
| 7,675–7,707 | Support | −0.15 to −0.57 | 50-day 7,707.02; anchored VWAPs from the Sep start (7,699.4) and Jul low (7,686.6); unfilled Oct 2 gap (7,684.75–7,693.31); 50-day EMA 7,678.7. Being tested overnight |
| 7,611–7,642 | Support | −1.00 to −1.40 | 38.2% Fibonacci 7,641.83; Oct 1 low 7,616.78; Sep 1 low 7,611.2. A close below makes a lower low |
| 7,579–7,594 (7,584 = −3%) | Support | −1.62 to −1.81 | 100-day 7,593.85; 50% Fibonacci 7,579.22. The −3% tripwire (7 of 8 recent episodes then went to −4% or worse) |
| **7,505–7,552** | **Support (hinge)** | −2.17 to −2.77 | Aug–Sep closing low 7,551.81; 61.8% Fibonacci 7,516.61; Sep 16 low 7,507.77; range floor 7,504.78 |
| 7,418–7,450 | Support | −3.48 to −3.89 | Mar 30 anchored VWAP 7,450.03; −5% = 7,428; 78.6% Fibonacci 7,427.47; 6-month volume point of control 7,418.54 |
| 7,314–7,410 | Support (trend line) | −4.0 to −5.25 | Jul 29 low 7,313.92; 200-day projected at 7,340–7,410 for late Nov / early Dec |
| 7,252–7,263 | Support | −5.90 to −6.04 | 200-day today 7,263.43; YTD anchored VWAP 7,252.46 |
| 7,037 | Support | −8.83 | −10% from the record |
| 6,887–6,905 | Support | −10.5 to −10.8 | Unfilled Apr 14 gap |

**RSP (% vs its 212.09 close)**
- **Resistance:** 213.30–213.99 (+0.6% to +0.9%) and the falling 50-day at 216.02 (+1.85%).
- **Support:**
  - 210.96, the Sep 16 and Oct 14 lows (−0.53%);
  - 207.16–208.02, the Oct 1 low and Sep 30 close (−1.9% to −2.3%);
  - 206.51, the 200-day (−2.63%);
  - 204.05–205.52, the YTD anchored VWAP and May 22 gap (−3.1% to −3.8%);
  - 200.49, −10% from the record (−5.47%).

## 8. Calendar (ET) [MR, CAT]

| Date | Events |
|---|---|
| Thu Oct 15 | PPI and retail sales (8:30 am); TSMC results; Warsh speaks in Bangkok (11:30 pm) |
| Fri Oct 16 | Monthly options expiration |
| Oct 17–29 | Fed blackout (dates inferred) |
| Wed Oct 21 | META, LRCX, TXN results; VIX expiration |
| Tue–Wed Oct 27–28 | **FOMC** (decision 2:00 pm, hike odds about 35%); **MSFT and GOOGL** report after the close |
| Thu Oct 29 | Q3 GDP and September PCE; ECB; INTC; AMZN (date estimated) |
| Fri Oct 30 | ECI; BoJ |
| Tue Nov 3 | Midterms; Iran no-strike pledge lapses; AMD results |
| Wed Nov 4 | Treasury refunding announcement |
| Fri Nov 6 | Payrolls |
| Tue Nov 10 | CPI; CoreWeave results (estimated) |
| Nov 17 or 18 | NVDA results (UNVERIFIED) |
| Nov 18 / Nov 20 | VIX expiration / monthly options expiration |
| Dec 8–9 | FOMC, with projections |
| Dec 11 | Continuing resolution expires |

## 9. What tells the scenarios apart, and what would change the verdict

**Oct 15–16**
- Does 7,675–7,707 hold after PPI, retail sales and TSMC?
- Do semis close green on good news and stay there?
- Does RSP hold 210.96?
- Does the A/D line rise while the index dips (rotation), or fall with it (liquidation)?

**To Oct 23**
- Does 7,580–7,600 hold through META and VIX expiration?
- If it breaks, a VIX spike with VIX/VIX3M above 1 would point to a *deeper* correction, not a trend break.

**Oct 27 – Nov 6**
- The FOMC outcome.
- How MSFT and GOOGL stocks react to their capex: a rising stock means the market accepts it.
- PCE, payrolls and the refunding.
- Whether HY OAS breaks 3.46% and the 10-year breaks 5.31%.

**What would move me toward shallow (above 55%):**
- Closes hold 7,584 through Oct 30, RSP stays above 210.96, and the index reclaims 7,790.83.
- More than 50% of members above their 50-day (34.7% now).
- HY OAS back below 3.0%.
- The Fed holds on Oct 28 without escalating.

**What would move me toward deeper or a trend break:**
- **A close below 7,505 with RSP below 207.16.** Deeper then becomes the base case at about 55%, with a trend break at about 30%.
- Any of these push further toward a trend break:
  - HY OAS above 3.46% or IG above 1.0%;
  - VIX/VIX3M above 1 for three or more sessions;
  - the 10-year above 5.31%;
  - an Oct 28 hike with a signalled follow-up;
  - the A/D line below 4,960.

**Single most important level:** S&P 500 **7,505 on a closing basis**, the Aug–Sep range floor, Sep 16 higher low and 61.8% Fibonacci level, which both advocates name. Pair it with RSP 207.16.

**Single most important event:** **Wed Oct 28**, when the FOMC decides (2:00 pm, about 35% hike odds), MSFT and GOOGL report capex that evening, and GDP and PCE follow the next morning.

## 10. Conditioning for the tech, semis and NVDA layers

- **Shallow.** This needs QQQ at or above about 684 (−10% from its record) with RSP flat near 212, or at or above about 695 (−8.5%) if RSP slips to 210. In this case SOXX and NVDA make their lows by late October.
- **Deeper.** A close below 7,505 most likely means QQQ is already down 10–13%. The higher-beta lows then cluster around **Oct 28 – Nov 10**.
- **Trend break.** In a market trend break, the semis and NVDA low most likely comes **after** NVDA's results (late Nov or Dec), so the results do not mark the low.

---

**Sources**
- **Data files:** DATA_BRIEF.md, technicals.json, levels.json, breadth.json, breadth_timeseries.csv, base_rates.json (and scripts/base_rates.py for the episode definition), betas_ratios.txt, analog_forward_returns.txt and live_snapshots.md.
- **Research and advocate briefs:** macro_rates.md (FRED, BLS, the Fed, and FedWatch via Yahoo [S]), catalysts.md, oct8_narrative.md, oct8_skeptic.md, market_bull.md and market_bear.md.
- **My scripts:** scratchpad/mv/verify1–5.py.
- **IBKR, Oct 15:** SPY 765.75 (03:28 UTC, real-time); ES December 7,732.75 (03:19 UTC, delayed); RSP 211.73 (00:28 UTC, thin).
- **WebSearch at about 03:35 UTC Oct 15:** TSMC Q3 results not yet out ([Crypto Briefing](https://cryptobriefing.com/tsmc-record-profit-sixth-quarter-ai/), [Kaohoon](https://www.kaohooninternational.com/?p=592325)).
- **Fed calendar:** https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- **Hike odds of 35%:** Yahoo Finance, Oct 14, https://finance.yahoo.com/economy/policy/articles/fed-interest-rate-hike-seems-195052044.html

**UNVERIFIED or caveated**
- **Single-source figures:**
  - Oct 28 hike odds of 35% (intraday readings 49–54%), and >95% odds of at least one hike by year-end.
  - Oracle's downgrade to BBB−.
  - The CoreWeave yield of about 15%.
  - Hyperscaler CDS "records" (social media).
- **My own estimates:** the S&P 500 equivalent of the overnight SPY price, and the ES fair value.
- **Unconfirmed dates:** NVDA results (Nov 17 or 18) and AMZN results.
- **Unverified sentiment and odds:** the CNN Fear & Greed feed, and the midterm prediction-market odds.
- **Data limits:**
  - Breadth uses current S&P 500 members only (survivorship bias), and the 200-day breadth series starts in Aug 2025.
  - Every analog sample is small (n=3–35).
  - Classifying a year as "Fed-tightening" is my judgment.
  - The 200-day projections assume a flat price path.
- **Pending:** TSMC Q3 results were not out when this was written.

---

## AUDIT ADDENDUM (independent numbers audit, analysis/verify/audit_market.md) — lower layers must use these corrections

1. **Calibration anchor was mislabelled.** The "+NDX ≥4% below 20-day high, n=35, 40/40/20" set was computed on a looser base; on the stated base it is n=26, **58/19/23**; on the loose base correctly bucketed **46/34/20**. SOX-conditioned set: n=11, 55/18/27. Base rows correctly bucketed: 58/24/18 (1950–), 62/21/18 (2004–). Tightening-midterm set is n=4, 1/1/2 (2022 counted).
2. **Corrected market probabilities (auditor's re-derivation using the verdict's own method): ≈ 45–48% shallow / 33–35% deeper / 19–20% trend break.** Shallow is the modal bucket; the median of lows sits at or just above 7,505 (not "below the hinge"). Working figures for downstream use: **46 / 34 / 20**.
3. **A tech-only break of 7,505 is possible:** using the verdict's own regression (S&P ≈ 0.397·RSP + 0.414·QQQ), QQQ ≤ ~680 (−10.5% from its record) breaks 7,505 with RSP flat; QQQ at its recent-regime median drawdown (−11.75%, ~670) implies S&P ≈ 7,462 (deeper). The "both legs must fall" claim is withdrawn.
4. Conditional update must sum to 100: after a close below 7,505, roughly 65% deeper / 35% trend break.
5. Deeper-zone 200-day support on deeper-scenario paths ≈ 7,330–7,370 by late Nov/early Dec (not 7,410). RSP −9.1% median = 202.4. 10y *real* yield is an 18-year high (since Nov 2008); the 24-year high is the nominal 10y.
6. Unchanged: scenario zones (7,540–7,650 / 7,370–7,460 / 6,850–7,250), key level **7,505 close (paired with RSP 207.16)**, key event **Oct 28**.
