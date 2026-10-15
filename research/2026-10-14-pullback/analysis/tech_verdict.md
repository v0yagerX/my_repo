# Layer 2 verdict: broad tech (QQQ / XLK)

*Chief analyst, written about 04:05 UTC Oct 15 (12:05 am ET). Data runs through the Oct 14 close, plus IBKR overnight quotes.*

**Source tags**
- **[DB]**: data/DATA_BRIEF.md and its companion files (betas_ratios.txt, analog_forward_returns.txt, base_rates.json, levels.json).
- **[MV]**: analysis/market_verdict.md.
- **[CAT] / [MR] / [SP] / [SL] / [O8] / [SK]**: research/catalysts.md, macro_rates.md, sentiment_positioning.md, semis_leadership.md, oct8_narrative.md, oct8_skeptic.md.
- **[calc]**: my scripts in `scratchpad/tv_scripts/`:
  - `verify_claims.py`: mega-caps, regressions, ratios, sector ETFs, July reactions, volume, 200-day projections.
  - `it_breadth.py`: the 75 S&P IT members.
  - `base_rates_tech.py` and `base_rates_tech2.py`: NDX daily from 1985, SOX from 1994, QQQ from 1999, XLK from 1998, DGS10, VIX.

**Live checks**
- **IBKR real-time:** QQQ **721.00** (−1.09%) at about 03:59 UTC; XLK **188.12** (−1.21%) at about 03:23 UTC. These are thin overnight prints, not closes.
- **QQQ implied vol:** 17.0%, at the 8th percentile of its 52-week range.
- **TSMC Q3:** **not out** at about 04:00 UTC (WebSearch returned previews only). It is not used here.

## Bottom line

| Scenario (lowest QQQ **daily close**, Oct 15 – Fri Dec 4) | Boundary | Prob. | Bottoming zone (XLK equivalent) | Drawdown from the 759.66 record close | Low most likely forms |
|---|---|---|---|---|---|
| **Shallow pullback** | Low ≥ **697.0** | **35%** | 700–716, core 705–713 (XLK 180.5–186) | −5.7% to −7.9% | Oct 15–23; Oct 29 at the latest |
| **Deeper correction** | 661.73 ≤ low < 697.0 | **40%** | 672–692, core 680–690 (XLK 171–178) | −8.9% to −11.5% | Oct 27 – Nov 13 |
| **Trend break** | Low < **661.73** (the Jul 29 closing low) | **25%** | 620–655, core 635–650; tail about 608 (XLK 153–165) | −13.8% to −18.4%; tail −20% | Nov 10 – Dec 4, and it may come later |

**Most likely closing-low zone: QQQ 680–700.** That is −7.9% to −10.5% from the record close, or −4.0% to −6.7% from the Oct 14 close of 728.95. For XLK the zone is **174–181**: −10.4% to −13.9% from its 202.00 record, or −5.0% to −8.6% from its 190.43 close.

**The deeper bucket leads, but only narrowly.** My median low is about 688–690. Whether this ends as a shallow pullback or a deeper correction depends on the **697–700 close**.

**This is not a buy-the-dip call.**
- Overnight, QQQ is already −5.1% from its record.
- None of the tech-specific bottoming signals are present: no volatility capitulation, no mega-cap washout, no breadth thrust.
- The mega-caps that cushioned the index have not been tested yet. They report from near their highs.

**Scenario boundaries in XLK.** XLK is more semis-heavy: its 6-month beta to QQQ is 1.31 (correlation 0.96) [calc].
- Shallow: XLK holds about **180** (61.8% Fibonacci level 180.51).
- Trend break: XLK closes below **166.57** (Jul 29 close; the 200-day is 167.1).

## 1. Where the pullback stands [DB]

**QQQ 728.95**
- −4.04% from the 759.66 record close (Oct 6) and −4.45% from the 762.86 intraday record. This is session 6 of the pullback.
- It sits on its 50-day (726.66, +0.3%) and 50-day EMA (728.71). It is above its 100-day (720.83) and 200-day (673.92, +8.2%). The 50-day and 200-day slopes are +2.36% and +1.86% over 20 days.
- RSI 44.7.
- **Overnight 721.00 (IBKR):** below the 50-day and the 721.12 VWAP anchored at the Jul low. It has filled the Sep 21 gap (721.73–727.81) and is sitting in the 716.6–722 volume-node band.

**XLK 190.43**
- −5.73% from its 202.00 record. RSI 43.1.
- 0.3% above its 50-day (189.9); 14.0% above its 200-day.
- Overnight 188.12.

**Momentum trend.** Both the 10-day and 20-day averages have rolled over. QQQ's 10-day is 748.26 and its 20-day 742.55.

**Volume**
- QQQ had 7 distribution days in 25 sessions, 4 of them in the last 5 [calc].
- Down-day volume on Oct 8 and Oct 14 was 1.46x and 1.58x the 50-day average. XLK on Oct 14 was 1.75x.
- Oct 12 and Oct 13 counted as distribution only because volume rose from the prior day; both were below average (0.77x and 0.89x).

## 2. How the market layer constrains tech

**The market verdict [MV]:** S&P 500 shallow 40% (low ≥ 7,505), deeper 38%, trend break 22%. Its median low is about 7,480.

**Betas [DB]**
- QQQ to SPY: 1.43 (1 year), 1.62 (6 months), 1.50 (3 months). Correlation about 0.91.
- XLK to SPY: 1.75–2.00.

**Mapping [MV]'s zones onto QQQ by beta, from the Oct 14 closes**

| [MV] scenario | S&P 500 zone | Implied QQQ |
|---|---|---|
| Shallow (core) | 7,580–7,620 | ≈ 708–716 |
| Hinge | 7,505 | ≈ 696–700 |
| Deeper | 7,370–7,460 | ≈ 676–694 |
| Trend break | 6,850–7,250 | ≈ 605–662 |

**The layers line up almost exactly:** my 697 tech hinge *is* [MV]'s 7,505 hinge at beta.

**Where tech can decouple from the index**
1. **Downside via rotation.** From Jun 2 to Jul 29, 2026, QQQ fell −11.3% and XLK −16.0%, while RSP rose +2.7% and the S&P 500's worst close was only −4.5% [calc]. Tech can reach my deeper bucket while the index stays shallow.
2. **Upside, holding up in a broad selloff.** In Dec 2024 the S&P 500 fell −4.3% and QQQ only −6.1%. In a selloff driven by rates or equal weight, tech can stay shallow while the index goes deeper.
3. **How the conditional odds combine with [MV]'s weights**

   | | P(tech shallow) | P(tech deeper) | P(tech trend break) |
   |---|---|---|---|
   | Given [MV] shallow (40%) | ≈ 0.72 | ≈ 0.25 | ≈ 0.03 |
   | Given [MV] deeper (38%) | ≈ 0.13 | ≈ 0.64 | ≈ 0.23 |
   | Given [MV] trend break (22%) | ≈ 0.03 | ≈ 0.17 | ≈ 0.80 |
   | **Combined** | **34%** | **38%** | **28%** |

   - The [MV] trend-break row is not 1.0 for tech: from Oct 2025 to Mar 2026 the S&P 500 fell −9.1% while QQQ fell only −12.2%.

**For the layers below**
- SOXX's beta to QQQ is 2.04–2.26 [DB]. Semis amplify whatever tech does.
- NVDA's beta to QQQ is only 1.16–1.30 and to SOXX 0.39–0.52. NVDA can decouple from semis, but not from QQQ.

## 3. Checking the advocates' numbers [calc unless noted]

| Claim | Status |
|---|---|
| Bull: QQQ ≈ 0.39·SMH + 0.32·MEGA6 (R² 0.95); all of the drop came from SMH | **Confirmed**: same coefficients and R². Small slips: QQQ's Oct 6–14 move was −4.04%, not −4.09%; the SMH term is −4.14%, not −4.31%; XLK's move was −5.73%, not −5.83%. MEGA6 −0.13% is correct |
| Bull: AAPL at its 52-week closing high; MSFT −1.8% from high and +5.9% above its 50-day; META +13.5% above its 50-day | **Confirmed**. GOOGL is −13.7% from its May high and AMZN −10.5% from its Aug high |
| Bull: IT members excluding semis are 52.7% above their 50-day and 69.1% above their 200-day | **Confirmed, but incomplete.** The bull omits three things about IT outside semis: the median member is **−20.9%** from its 1-year high, 50.9% are 20% or more below theirs, and **only 21.8% rose on Oct 14**. The weakness spread beyond semis on Oct 14 |
| Bull: the post-recovery set (n=46, median −6.1%) | **Directionally confirmed** with my 36-session version (n=55: 67% shallow / 27% deeper / 5% trend break). But 41 of the 55 signals predate 2001. Adding a broken-semis filter leaves n=10: 60/40/0 |
| Bull: July QQQ 661.73 low, +3.3% the next day, +9.4% after 10 sessions; MSFT +18.1% and AMZN +17.6% (Jul 28→31) | **Confirmed** |
| Bear: NDX given −4.04%, n=80, median −7.7%; given −5%, n=60, median −10.7% | **Confirmed** |
| Bear: NDX −4% with SOX ≥10% below its 20-day high, n=8, median −11.2% | **Confirmed**. The set includes 2000 (−83%) and 2018 (−23%). My 36-session version gives n=14, median −11.2%, 43/29/29 |
| Bear: XLK given −5.73%, n=25, median −11.7% | **Confirmed** |
| Bear: rotation table (QQQ and RSP at session 6) | **Confirmed**: Jul 2024 −4.7% / +2.7%; Jun 2026 −7.0% / −1.7%; Oct 2025 −3.8% / −1.2%; now −4.0% / −0.1% |
| Bear: at the record, QQQ/SPY was 1.7% and XLK/SPY 0.6% below their June relative highs; QQQE/QQQ was 7.3% below its Jul 29 high | **Confirmed** |
| Bear: median IT member −23.8% from its 1-year high; IT share above the 50-day fell from 76.0% to 44.0%; 29% of IT members rose Oct 8 and 17% Oct 14 | **Confirmed** (17.3%) |
| Bear: MSFT +18.3% and META +36.8% above their post-July closes | **Confirmed** against the Jul 30 closes (+14.8% and +32.5% against Jul 31) |
| Bear: QQQ 200-day reaches 683–689 by Nov 6–20; XLK's 171–173 | **Confirmed** on a flat price path: QQQ 683.2 / 688.6, and 694.7 by Dec 4 |

## 4. Internals

**Relative strength [DB, calc]**
- **QQQ/SPY:** 0.9472, just 0.2% above its 50-day (0.9454) and 1.9% above its 200-day. It is −4.5% from its Jun 18 high.
- **XLK/SPY:** 0.2474, 0.1% above its 50-day and 7.7% above its 200-day. It is −5.2% from its Jun 2 high.
- **The Oct 6 records did not come with relative-strength highs.**
- **QQQE/QQQ:** 0.1626, below its 50-day (−2.4%) and 200-day, and −6.9% from its Jul 29 high. Only a few names carried the Aug–Oct rally. Since Oct 6, equal weight (−3.63%) has done slightly better than cap weight (−4.04%).

**Rotation (sector ETFs since the Oct 6 close) [calc]**
- **Gainers:** XLE +6.1%, XLP +5.2%, XLV +4.1%, TLT +2.1%, XLU +1.4%, XLF +0.9%.
- **Losers:** XLK −5.7%, IWM −3.5%, XLI −2.6%, XLC −0.7%.

**The two key sessions**

| | Oct 8 | Oct 14 |
|---|---|---|
| XLK | −1.79% | −2.98% |
| QQQ | −1.34% | −1.97% |
| RSP | +0.60% | −0.57% |
| Defensive leaders | XLE +2.97%, XLP +2.11% | XLV +2.53%, XLP +2.22% |
| S&P 500 members | 67% rose [O8] | 241 advancers / 261 decliners [DB] |
| IT members that rose | 29% | 17% |
| Semis that rose | 0% | 5% |

- Oct 8 was a rotation *within* the market.
- Oct 14 was the first broad down day, and it reached into software and hardware.

**Sector breadth [DB]:** IT has 44.0% of members above their 50-day and 66.7% above their 200-day. That is still the third-highest 200-day reading of any sector. Its median weekly return was −5.5%.

**The mega-caps are the swing factor [calc]**

| QQQ correction | QQQ | SMH | MEGA6 |
|---|---|---|---|
| Jul–Aug 2024 | −13.6% | −24.8% | −15.9% |
| Oct 2025 – Mar 2026 | −12.2% | — | −17.6% |
| Jun–Jul 2026 | −11.3% | −20.2% | −9.1% |
| **Now** | | −10.9% | **flat** |

- Every QQQ drop of 11% or more since 2024 needed MEGA6 to fall at least 9%.
- Using the regression, a deeper outcome needs roughly another −8% in SMH **plus** −5% to −7% in MEGA6.

**Volatility and positioning**
- **Volatility [DB, SP]:** VIX 16.87, VIX/VIX3M 0.898, QQQ implied vol at the 8th percentile, QQQ option put/call 0.84 against a 1.10 average. At the Jul 29 NDX low, VIX was 20.66 and VIX/VIX3M 0.961.
- **Positioning:**
  - BofA FMS: net 37% overweight tech, the highest since Aug 2020 (CONFIRMED).
  - Discretionary US long/short net leverage at the 2nd percentile (SINGLE-SOURCE).
  - Systematic positioning at the 86th percentile (SINGLE-SOURCE).
  - QQQ ETF flows for Oct 13 conflict between vendors (+$6.38bn vs −$1.16bn) and are UNVERIFIED.

**Rates and credit [MR]**
- The Fed hiked on Sep 16. Oct 28 hike odds were about 35% (single source).
- 10-year 5.19%; real yield 2.88%, the highest since 2008.
- HY OAS 3.16% (91st percentile); CCC spreads at a 3-year high.
- Yields *fell* 12 bp while QQQ fell 3.6%. This was not a rates selloff, but nothing in rates offers a safety net either.

## 5. Calibration: base rate first, then regime

**Reference sets** for the lowest close over the 36 sessions to Dec 4, bucketed at −8.2% and −12.9% from the record [calc unless noted]

| Reference set | n | Shallow / Deeper / Trend break |
|---|---|---|
| NDX first close −3.5% to −6% below a record set ≤10 sessions earlier, above a rising 200-day, 1985– | 83 | 59 / 28 / 13 |
| Same, 2003– | 43 | 63 / 30 / 7 |
| QQQ itself, 1999– | 25 | 52 / 32 / 16 |
| NDX starting from a −5% state (today's overnight level) | 45 | 47 / 31 / 22 |
| **+ SOX ≥10% below its 20-day high (today's state)** | 14 | **43 / 29 / 29** |
| + SOX filter + VIX < 20 | 10 | 40 / 20 / **40** |
| + SOX filter, 2003– only (2019 ×2, 2024, 2025, 2026) | 5 | 20 / 40 / 40 |
| + 10-year up ≥40 bp in 3 months (today: +63 bp) | 13 | 23 / **77** / 0 |
| Bull's post-recovery set | 55 | 67 / 27 / 5 |
| Post-recovery + SOX filter | 10 | 60 / 40 / 0 |
| XLK, first −5% to −8%, above a rising 200-day (XLK buckets −10.6% / −17.5%) | 19 | 37 / 47 / 16 |
| [MV]-conditioned mapping (§2) | — | 34 / 38 / 28 |

**Reading the table**
- The unconditional base rate is about **58 / 29 / 13**.
- Conditioning on today's state (SOX broken, a −5% overnight print, the rate shock) moves it to roughly **42 / 39 / 19**.
- The top-down mapping requires about **28%** in trend break.

**Regime adjustments, bearish**
- The Fed is hiking, with real yields at 2008 highs. The rate analogs push outcomes into the deeper bucket.
- AI-credit stress points at the hyperscalers, the biggest QQQ weights:
  - CoreWeave bonds at about 15% (single source);
  - Oracle −58% from its high;
  - CCC spreads at a 3-year high.
- Breadth is narrow: QQQE/QQQ is near its low, and the median IT stock is −23.8% from its high.
- Low VIX means no capitulation yet.
- Tech overweight is at its highest since 2020.

**Regime adjustments, bullish**
- The mega-caps are untouched, and AAPL is at a record.
- Discretionary hedge funds are lightly positioned and buyback windows are reopening (single source).
- Midterm-year NDX seasonality: from Oct 14 to Dec 31 the median is +5.1%, up 90% of the time (n=10) [SP].
- The hard data are strong [CAT]: TSMC Q3 revenue +50.9% y/y; ASML sold out for 2027–28.

**Net: 35 / 40 / 25.**
- Shallow is below the state-conditioned base rates, because of the top-down mapping and the missing capitulation.
- Trend break is below [MV]'s implied 28%, because the rate analogs (77% deeper, 0% trend break) argue for a grind rather than a collapse.

## 6. The strongest case that "deeper" is wrong

**Toward shallow**
1. All of the damage so far is in semis. MEGA6 is flat, and every larger QQQ correction needed mega-caps to fall 9% or more.
2. In July, the mega-caps marked the low: QQQ +3.3% the day MSFT rose +15.5%.
3. The broad NDX base rate is 59% shallow. The post-recovery base rate is 60–67% shallow.
4. The overnight 721 is already inside the 716–722 cluster: the 6-month volume point of control, the Jul-low anchored VWAP and the 100-day.
5. QQQ's 10-day analog has a median of +1.2% and was positive 71% of the time [DB].

**This is persuasive.** It is why shallow is 35% and not 25%.

**Why I did not go further toward shallow**
- From the overnight print, the 697 hinge is only −3.3% away.
- About eight more points of SMH downside alone gets QQQ most of the way there.
- The mega-caps report Oct 21–29, from far higher bars than in July (MSFT +18%, META +37% above their Jul 30 closes). In July, capex without revenue cost GOOGL −7.1% and META −8.0%.
- The 40-day QQQ analog has a median of −0.6% and was positive only 40% of the time [DB].

**Toward a trend break**
1. Since 2003, two of the five broken-semis setups went below −12.9%: Jul 2024 (−13.6%) and Feb 2025 (−22.9%).
2. In the low-VIX set, 4 of 10 broke.
3. The 2018 tightening midterm: NDX fell −23% into Dec 24 [SP].

**I keep trend break at 25%, not higher.** No credit or vol confirmation is in place yet (HY OAS is below 3.46%, IG is calm, VIX/VIX3M is below 1). And the regime-matched rate analog gives 0% trend break.

## 7. Scenarios

**Shallow (35%): lowest close ≥ 697**
- **Zone:** 700–716. The core is 705–713: the Sep 17 gap (711.88–713.32), the 50% Fibonacci level 712.0, the 23.6% Fibonacci of Mar–Oct 713.95, and volume nodes at 713.6, 710.5 and 707.5.
- **Path:**
  1. Opex (Oct 16) and TSMC wash out at 705–716.
  2. META (Oct 21) is received well.
  3. QQQ closes above 731.23 (the Sep-start anchored VWAP) by Oct 23.
  4. The Oct 28 FOMC holds, and MSFT/GOOGL show capex with revenue (the July reaction function).
  5. QQQ reclaims 746.45 in November.
- **Confirming signals:**
  - MEGA6 holds within −3% of its Oct 14 level.
  - QQQ/SPY stays at or above 0.9454.
  - More than 60% of IT members get back above their 50-day.
  - SMH holds 540 or better.
  - The S&P 500 holds 7,505 [MV].
- **Invalidation:** any close below 697, or XLK below 180.

**Deeper correction (40%): 661.73 ≤ lowest close < 697**
- **Zone:** 672–692. The core is 680–690:
  - −10% from the record, 683.7;
  - the 78.6% Fibonacci level, 682.91;
  - the 38.2% Fibonacci of Mar–Oct, 683.69;
  - the Aug–Sep intraday low, 685.82;
  - the 200-day, projected at 680–695 for Oct 30 – Dec 4.
- **Path:**
  1. 716–722 fails, then 697–705 breaks around Oct 21–29.
  2. The mega-caps join semis, through capex punishment and/or an Oct 28 hike.
  3. A volatility flush (VIX/VIX3M above 1 briefly) marks the low, Oct 28 – Nov 10.
  4. QQQ recovers toward 720–730 into NVDA's results.
- **Confirming signals:**
  - MEGA6 falls 5–9%.
  - QQQ/SPY closes below 0.9454 for 3 or more sessions.
  - The S&P 500 closes below 7,505 while RSP holds 207 or better.
  - HY OAS rises to 3.3–3.46% but no higher.
- **Invalidation:**
  - **Upside:** QQQ holds 697 through Oct 29 and reclaims 746.45.
  - **Downside:** a close below 661.73, HY OAS above 3.46%, or the 10-year above 5.31%.

**Trend break (25%): lowest close < 661.73**
- **Zone:** 620–655. Stepping stones:
  - the YTD anchored VWAP, 660.34;
  - −15%, 645.7;
  - the Apr 17 gap, 642.18–644.07;
  - the 61.8% Fibonacci of Mar–Oct, 634.77.
- **Tail:** about 608 (−20%).
- **Path:**
  1. A hike on Oct 28 with a signalled follow-up, or the 10-year breaks 5.31%, or AI credit spreads to the hyperscalers.
  2. MEGA6 falls 10% or more and XLK loses 166.57.
  3. NVDA's results fail to stop the decline; 7 of NVDA's last 9 prints were lower five sessions later [CAT].
- **Confirming signals:**
  - The S&P 500 below 7,314 and RSP below 200.5 [MV].
  - VIX/VIX3M above 1 for 3 or more sessions.
  - SMH below 503.6.
  - QQQ/SPY below its 200-day (about 0.929).
- **Invalidation:** every close through Dec 4 holds 661.73. A V-shaped flush below that line still counts as a trend break on price.

## 8. Key levels (closing basis; % vs the Oct 14 close)

**QQQ (728.95)**

| Level | Type | % | Why |
|---|---|---|---|
| 759.66 / 762.86 | Resistance | +4.2 / +4.7 | Record close and intraday record |
| 744.2–746.45 | Resistance | +2.1 to +2.4 | Oct 13 gap; VWAP anchored at the Oct 6 high. Reclaiming it ends the pullback |
| 737.3–742.6 | Resistance | +1.2 to +1.9 | 20-day; 21-day EMA 739.6; 3-month volume node |
| 726.7–731.2 | Pivot (lost overnight) | −0.3 to +0.3 | 50-day; 50-day EMA; Sep-start anchored VWAP |
| 716.6–722 | Support | −1.0 to −1.7 | 6-month volume POC 719.62 (11.3% of volume); 3-month POC 718.73; Jul-low anchored VWAP 721.12; 100-day 720.83 |
| 707.5–714 | Support | −2.1 to −2.9 | Sep 17 gap; 50% Fibonacci 712.0; volume nodes |
| **697.1–704.7** | **Hinge** | −3.3 to −4.4 | Sep 16 close 704.72; Sep 16 low and 61.8% Fibonacci 700.0; Aug–Sep closing low 700.07; Mar 30 anchored VWAP 697.13 |
| 680–694 | Support | −4.8 to −6.7 | −10%; 78.6% Fibonacci; 38.2% Fibonacci of Mar–Oct; the 200-day path |
| 673.9 | Support | −7.6 | 200-day today |
| **659.2–661.7** | **Trend line** | −9.2 to −9.6 | Jul 29 close and low; YTD anchored VWAP; 50% Fibonacci of Mar–Oct |
| 634.8–645.7 | Support | −11.4 to −12.9 | −15%; Apr 17 gap; 61.8% Fibonacci of Mar–Oct |

**XLK (190.43)**

| Level | Type | % | Why |
|---|---|---|---|
| 202.0 / 197.1 / 192.4 | Resistance | +6.1 / +3.5 / +1.0 | Record; Oct 6 anchored VWAP; Sep-start anchored VWAP |
| 188.0–189.9 | Support | −0.3 to −1.3 | 50-day; 38.2% Fibonacci; Jul-low anchored VWAP |
| 183.75–186.7 | Support | −1.9 to −3.5 | Sep 17 gap; 100-day; 50% Fibonacci; volume POC |
| **180.5–182.1** | **Hinge** | −4.4 to −5.2 | 61.8% Fibonacci; Sep 14 low |
| 173–178.8 | Support | −6.1 to −9.1 | Aug–Sep closing low 178.04; Mar 30 anchored VWAP 176.54; 78.6% Fibonacci 174.33; 38.2% Fibonacci of Mar–Oct 174.0 |
| **166.5–167.1** | **Trend line** | −12.3 to −12.6 | Jul 29 close; 200-day |

## 9. What tells the scenarios apart, and what would change the verdict

**Next 2 sessions**
- Does QQQ close back above 716–722 after TSMC and opex, and above 731.23 by Oct 23?
- Do semis close green and hold?

**Oct 21 – Oct 29**
- The mega-cap reaction function: capex up with the spender's stock up, or capex up with it down.
- MEGA6 against its Oct 14 level.
- The FOMC.
- QQQ/SPY against 0.9454.

**Late Oct – November**
- Is a break of 697 met by a volatility flush (deeper) or by a credit break with HY OAS above 3.46% (trend break)?

**What would move me toward shallow (above 50%)**
- QQQ closes above 731.23 and then 746.45 before Oct 28.
- Or it holds 697 through Oct 29 with at least two of META, MSFT, GOOGL and AMZN up after reporting.
- More than 60% of IT members back above their 50-day.

**What would move me toward a trend break (above 40%)**
- A QQQ close below 683.7 **before** Oct 28; an early break means acceleration.
- MEGA6 −8% from its Oct 14 level.
- An Oct 28 hike with hawkish guidance.
- The 10-year above 5.31%, or HY OAS above 3.46%.
- SMH below 503.6.

**Single most important level:** QQQ **697–700 on a closing basis** (XLK 180.5).

**Single most important event:** **Wed Oct 28**: the FOMC at 2:00 pm, then MSFT and GOOGL after the close. AMZN (estimated) and GDP/PCE follow on Oct 29.

---

**Sources**
- **Data files:** DATA_BRIEF.md, betas_ratios.txt, analog_forward_returns.txt, base_rates.json, levels.json, breadth.json, live_snapshots.md. Raw Yahoo CSVs in data/ and data/spx/; long histories in analysis/sent/long/ and dl_techbull/; FRED DGS10 in dl_fred/.
- **Research and briefs:** market_verdict.md, tech_bull.md, tech_bear.md, and research/*.md (catalysts, macro_rates, sentiment_positioning, semis_leadership, oct8_narrative, oct8_skeptic).
- **My scripts:** `scratchpad/tv_scripts/*.py`.
- **IBKR real-time snapshots, Oct 15:** QQQ (320227571) at about 03:59 UTC; XLK (4215230) at about 03:23 UTC.
- **TSMC:** results not yet out at about 04:00 UTC per WebSearch. Previews: [investingLive](https://investinglive.com/stocks/tsmc-set-for-sixth-straight-record-profit-as-ai-demand-lifts-q3-earnings/), [Yahoo](https://finance.yahoo.com/markets/stocks/articles/tsmc-q3-revenue-tops-own-113733291.html).

**UNVERIFIED or caveated**
- **Single-source figures:**
  - Oct 28 hike odds of about 35%.
  - Hedge-fund leverage and systematic-positioning percentiles.
  - The CoreWeave yield of about 15%.
  - Oracle's downgrade to BBB−.
- **Dates:** AMZN's report date (about Oct 29) is an estimate. NVDA's (Nov 17 or 18) is unconfirmed. **AAPL's report date was not checked.**
- **QQQ ETF flows:** the two vendors conflict.
- **Breadth:** uses current members only (survivorship bias).
- **Base-rate samples:** the conditioned sets are small (n=5–14) and weighted to the 1990s.
- **The joint conditional table in §2 is my judgment.**
- **200-day projections:** assume a flat price path.
- **Overnight prints:** thin, and not closes.
- **TSMC:** results were pending when this was written.
