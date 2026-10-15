# Layer 4 verdict: NVDA

*Written about 04:30–05:30 UTC on Oct 15 (12:30–1:30 am ET). Data runs through the Oct 14 close of 221.30.*

**Overnight IBKR real-time prints**
- NVDA **218.96** (−1.06%) at 04:24 UTC; earlier prints were 217.94–218.50.
- SOXX 512.27; QQQ 722.57.
- "Overnight" below means the **218.35** midpoint of the 218.2–218.5 band.

**Source tags**
- [DB]: DATA_BRIEF.md and the data files.
- [MV] / [TV] / [SV]: the market, tech and semis verdicts. Market and tech are used as corrected by their audit addenda.
- [CAT] / [SP] / [SL] / [O8] / [MR] / [FX]: catalysts.md, sentiment_positioning.md, semis_leadership.md, oct8_narrative.md / oct8_skeptic.md, macro_rates.md, and zz_verification_corrections.md together with verify/facts.md.
- [calc]: my scripts in `scratchpad/nv_scripts/` (v1–v3.py, mc.py). They run on Yahoo daily data: NVDA from 1999, SOXX from 2001, QQQ from 1999.

**TSMC:** see §10.

## Bottom line

| Scenario (lowest NVDA **daily close**, Oct 15 – Fri Dec 4\*) | Boundary | Prob. | Bottoming zone | Drawdown from 239.24 close / 243.37 intraday | Low most likely forms | Zone vs the ~$171 margin level (reference only) |
|---|---|---|---|---|---|---|
| **Shallow pullback** | Low ≥ **210.00** | **33%** | 211–218.9 (core 214.5–217.2) | −8.5% to −11.8% / −10.1% to −13.3% | Oct 15–23; Oct 29 at the latest | 171 is 19.0–21.9% below |
| **Deeper correction** | 190.01 ≤ low < 210.00 | **47%** | 198–209 (core 201–207) | −12.6% to −17.2% / −14.1% to −18.6% | Oct 26 – Nov 13 (mode Oct 28 – Nov 6). Second window: earnings week | 171 is 13.6–18.2% below |
| **Trend break** | Low < **190.01** (Jul 29 closing low) | **20%** | 175–189 (core 179–188); tail 165–172 | −21.0% to −26.9% (tail about −31%) / −22.3% to −28.1% | Nov 10 – Dec 4, often after the print. The low may fall after the window | 171 is 2.3–9.5% below; **the tail reaches 171** |

\*NVDA's earnings date is **not announced**. The realistic window is Nov 18–25 [FX]. If it reports Nov 25, read the window as running to about Dec 9.

**Most likely closing-low zone: 201–209, centred on 203–207.**
- That is −5.6% to −9.2% from 221.30, or −4.3% to −7.9% from overnight.
- My median lowest close is about **205–207**.
- About 67% of my probability sits below the 210 hinge. **This is not a buy-the-dip call.**

## 1. Where NVDA stands [DB]

**Price and averages**
- 221.30 is −7.50% from the Oct 6 record close of 239.24 and −9.07% from the 243.37 intraday record. Overnight it is about −8.5% to −8.7%.
- Price is under the 50-day (223.21, rising 4.5% per 20 sessions). This is the first close below it since Sep 15 [calc].
- It is above the 100-day (214.45, +3.2%) and the 200-day (202.69, +9.2%). Both are rising.

**Momentum:** RSI 43.9; ATR 5.83 (2.63%).

**The failed breakout:** NVDA closed above the May high of 235.74 for three sessions (Oct 5–7), then fell back below it on Oct 8 (230.48).

**Retracement:** NVDA has given back 36.4% of the Jul 29 → Oct 6 rally (190.01 → 239.24). SOXX has given back 56% [SL].

**Overnight position:** the 218.96 print sits on the 3-month volume POC (218.85), just above the Sep 17 gap (216.76–217.15).

## 2. How the upper layers constrain NVDA (mandatory conditioning)

| Upper-layer line | NVDA at the 1-year ratio | NVDA if it "catches down" |
|---|---|---|
| SOXX 497.40 (semis shallow/deeper hinge) | ≈216.0 (ratio 0.57) | ≈211.9 (ratio 1.0) |
| SOXX 465.00 (semis trend line) | ≈208.1 | ≈198.1 |
| SOXX 435–455 (semis trend-break core) | ≈200.8–205.7 | ≈185–194 |
| QQQ 700–716 (tech shallow zone) | ≈208.9–215.7 (down-day ratio 1.41) | — |
| QQQ 697 (tech hinge) | ≈207.6 | ≈203.3 (current-leg ratio 1.86) |
| QQQ 672–692 (tech deeper zone) | ≈196.9–205.5 | — |
| QQQ 661.73 (tech trend line) | ≈192.5 | ≈183.3 |
| QQQ 620–655 (tech trend-break zone) | ≈174.7–189.7 | — |

**Tech is the binding constraint** [TV, audited 37 / 38 / 25].
- NVDA's 1-year beta to QQQ is 1.30 (correlation 0.68). Its down-day beta is 1.41, and the average move ratio on QQQ days below −1% is 1.41 [DB, calc].
- At that ratio, QQQ's 697 hinge maps to about 207.6 and its 661.73 trend line to about 192.5. Tech's buckets therefore line up almost one-for-one with my 210 / 190.01 boundaries.
- NVDA cannot decouple from QQQ. Mapping tech's probabilities through my conditional table gives about **31 / 50 / 20**.

**Semis is a weak constraint, but only under the current regime** [SV, 26 / 39 / 35].
- NVDA's 1-year beta to SOXX is 0.48 (correlation 0.59).
  - On SOXX days below −2%, the average move ratio is 0.57 (n=54). The regression slope through the origin is 0.54, which is the bull's figure; the ordinary least-squares slope is 0.38 [calc].
  - Down-day beta is 0.56 and up-day beta 0.30 [calc].
  - The current leg runs at a ratio of 0.63: −7.50% against −11.88%.
- At these ratios, even a semis trend break (SOXX below 465) maps to only about 200–208. Semis-only mapping gives **42 / 46 / 12**.
- **The caveat matters.** Over 5 years, NVDA's median move ratio on SOXX days below −3% is **1.01** (n=113). Over the last year it is 0.60 (n=34) [calc].
  - The low beta belongs to the post-November-2025 regime. It is not a constant.
  - NVDA/SOXX peaked at 0.6738 on Nov 20, 2025 and bottomed at 0.3185 on Jun 22, 2026. The +33.7% "holdout" rally since then started from a deeply depressed ratio.
  - NVDA lagged the first half of 2026: YTD +18.7% vs SOXX +72.5% [SL].

**The market sets the trend-break tail** [MV, audited 46 / 34 / 20, hinge S&P 500 7,505].
- NVDA's beta to SPY is 1.89 (correlation 0.64).
- A market trend break (S&P 500 below 7,314) implies QQQ at about 660 or lower, which maps to NVDA at about 192 or lower.
- A shallow market does **not** protect NVDA. From May 14 to Jul 29, 2026, NVDA fell −19.4% while the S&P 500's worst close was −4.5% [DB, MV].
- Market mapping gives about **32 / 48 / 20**.

## 3. Checking the advocates' numbers

| Claim | Status |
|---|---|
| Bull: down-day beta 0.54 to SOXX (n=54); ratio 0.57; current leg 0.63 | **Confirmed.** The 0.54 is a through-origin slope. Over 5 years the big-down-day ratio is 1.01, which the bull omits |
| Bull: 5 of 11 three-year episodes ended at −7.6% to −9.7%, each bottoming 0–3 sessions after the first −7.5% close | **Confirmed** (2, 0, 0, 0 and 3 sessions). But conditioned on the overnight −8.7%, only 3 of 9 three-year episodes ended shallower than −12.2% |
| Bull: retraced 36%; Oct 16 OI at 220; Oct 23 straddle 211.2–231.4; IV 15th percentile | **Confirmed** [SP, calc] |
| Bull: "[MV] median 7,480 → QQQ 660–685 → NVDA 192–203" | **Overstated.** The audited [MV] median is about 7,505, which is QQQ about 696–700 [TV], which maps to NVDA about 207–208 |
| Bull: holdout set (n=15), median 60-day max drawdown −17.6%; swing-leg set (n=21) | Not re-run as specified. My closest holdout version (n=12, 36 sessions) has a median low of −13.9% versus the record, split 42 / 33 / 25 |
| Bear: 5-year episodes from −7.5%, n=14, median −16.15%, 36% shallower than −10%; excluding 2022, n=13, median −14.0%, 8 of 13 at −13.4% or worse; median 13.5 extra sessions; from −8.7%, 25% shallower than −10% (n=12) | **All confirmed** [calc, DB] |
| Bear: beta 0.56 down vs 0.30 up | **Confirmed.** "Ratio 0.63 on SOXX days below −3% (n=40)": I get 0.60 (n=34) over 1 year |
| Bear: "no capitulation, volume 1.01×" | **True, but it is not a valid signal for NVDA.** NVDA's last three lows printed on 1.01× (Mar 30), 0.96× (Jul 29) and 1.05× (Sep 14) volume [calc] |
| Bear: 200-day at about 204.4 by Oct 28 and 205.3 by Nov 4 | **Approximately confirmed:** 204.2 / 205.1 on a flat path at 218; 203.3 / 203.7 on a flat path at 200 [calc] |
| Both: 7 of the last 9 prints were lower five sessions later | **Confirmed** [CAT, local CSV] |
| Both: Oct 28 hike odds about 35%; earnings Nov 17/18 | **Stale / unverified.** Late Oct 14 odds were 24–32%. The earnings date is unannounced (Nov 18–25) [FX] |
| Bear: $235bn buyback authorization | **Confirmed** [SL, M]. $150bn was added Sep 28. catalysts.md's "$99bn left" predates that addition |

## 4. NVDA internals

**Relative strength [DB]**
- NVDA/SOXX: 0.4261. +5.0% since Oct 6; +2.6% above its 50-day; −5.5% below its 200-day.
- NVDA/QQQ: −3.6% since Oct 6, and below its 50-day.
- NVDA is still the refuge inside semis. The median semi is −30.8% from its high, and 76% of the 29-name basket is in a bear market [SL].

**The credit channel runs through NVDA's own balance sheet [CAT, FX; 8-K and transcript]**
- Guarantees capped at **$105bn** (**$108.5bn** gross including existing ones) for about 4.25 GW of OpenAI-affiliate capacity, starting 2028. OpenAI reimburses NVDA for any amounts paid.
- **$279bn** of supply commitments; $366bn of total commitments.
- AI labs that NVDA backs with its balance sheet will be "roughly a quarter" of next year's business.
- **Overnight:** CoreWeave's 2032 bonds below 78c (Reuters) and SoftBank −9.4% [FX].
- OpenAI's run-rate is about $50bn against $68–70bn. Outlets give two competing explanations, so the gross-vs-net account is **not settled** [FX].

**Options [SP]**
- **Oct 16 expiry:** 220 dominates (99.2k calls / 64.6k puts).
- **Nov 20 expiry:** max pain about 210 (partial chain); a 200-strike put shelf (53.2k, and 64.5k in December).
- **Implied moves:** the earnings event is about ±5.8–5.9% one standard deviation; the Nov 20 straddle is ±9.8% (199.7–242.9).
- **Risk-neutral odds of a Nov 20 close:** below 210, 35%; below 200, 23%; below 190, 15%.

**Positioning and fundamentals**
- **Positioning:**
  - NVDL flows are churning rather than liquidating.
  - Discretionary hedge-fund net exposure is at the 2nd percentile (SINGLE-SOURCE).
  - Long semis is the most crowded trade (CONFIRMED).
  - NVDA's discretionary buyback window is likely closed until the print (UNVERIFIED inference).
- **Fundamentals** [CAT, primary]:
  - Q3 guide $108bn ±2%; Q4 gross-margin trough 71–72%; FY28 about +70%, "supply-constrained".
  - About 15x FY28 earnings (Morgan Stanley, [M]).
  - No NVDA-specific downgrades, and no insider selling [O8].

## 5. Calibration: base rate first, then regime

Buckets: low ≥ −12.2% (210) / −12.2% to −20.6% / below −20.6% (190.01), measured from the record [calc].

| Reference set | n | Shallow / Deeper / Trend break |
|---|---|---|
| Record-close episodes reaching −7.5%, 3 years (final depth) | 11 | 45 / 36 / 18 |
| Same, given −8.7% (overnight state) | 9 | 33 / 44 / 22 |
| 5 years including 2022, given −7.5% | 14 | 36 / 43 / 21 |
| Since 2016, given −7.5% | 31 | 26 / 55 / 19 |
| 36-session window: first close −7.5% to −10% from the record, above a rising 200-day (2016–) | 75 (overlapping) | 33 / 49 / 17 |
| Same, 2021– | 44 | 30 / 48 / 23 |
| Same + below the 50-day (today's state) | 27 | 37 / 48 / 15 |
| Holdout: SOXX ≥15% off its 1-year high, NVDA 5–10% off its record | 12 | 42 / 33 / 25 |
| Holdout, NVDA measured from its 1-year high (2010–) | 17 | 47 / 29 / 24 |
| SOXX ≥10% off its 60-day high, NVDA 6–10% off its record | 14 | 36 / 50 / 14 |
| Driftless fat-tailed simulation at 33% IV with a ±5.8% earnings jump, from 221.30 / from 218.25 | — | 37 / 41 / 22 ; 30 / 44 / 26 |
| Top-down: via semis / tech / market (§2) | — | 42/46/12 ; 31/50/20 ; 32/48/20 |

**The base rates and mappings average about 35 / 46 / 19.** Every independent lens puts the mode in the deeper bucket. Holdout sets are *bimodal*: they show more shallow outcomes **and** more trend breaks than the general set, so the holdout status widens both tails rather than pointing one way. The samples are small and overlapping (effective n is about 6–10 episodes).

**Regime adjustments**
- **Bearish:**
  - The Fed is hiking, with 10-year real yields at their highest since 2008.
  - AI-credit stress hits NVDA's own guarantees.
  - The Asian memory rout overnight.
  - The index shows no volatility capitulation (VIX/VIX3M 0.898).
  - The earnings print falls inside the window, and the post-print record is poor.
  - The low-beta regime could end.
  - The buyback window is probably shut.
- **Bullish:**
  - Hike odds have fallen to 24–32%.
  - Fundamentals are accelerating, and the valuation is about 15x FY28.
  - NVDA's lows do not need volume capitulation.
  - The market is modally shallow.
  - Midterm seasonality.
  - Discretionary positioning is light.
- **Net:** −2 / +1 / +1. **Final: 33 / 47 / 20.**

## 6. The strongest case that "deeper" is wrong

**Toward shallow**
1. **At the 1-year beta, SOXX must break 465 before NVDA reaches 208.** The semis deeper core (474–492) maps to NVDA at about 209–214, right at the hinge.
2. **The quick-shallow template is NVDA's own.** In 5 of 11 recent episodes, NVDA bottomed within 3 sessions at 216–221 equivalents.
3. **The 220 options pin unwinds after Oct 16.** TSMC could be the first good news that holds.
4. **The Jul 29 precedent.** The low formed on the eve of MSFT's results.

*Partly persuasive.* It is why shallow is 33% rather than the 25–30% that the overnight-conditioned sets imply. It does not take the mode, for three reasons:
- The 210 hinge is only 3.8–4.1% below the overnight prints.
- Tech alone puts 63% on QQQ below 697, which maps to NVDA below about 208.
- Every base rate and the implied-volatility walk put at least 55% below 210.

**Toward trend break**
1. The 5-year beta to SOXX is 1.0. If it returns, the semis trend break (35%) maps to 185–194.
2. 24–25% of holdout signals broke.
3. NVDA guarantees part of the financing chain that is under stress.
4. The print falls inside the window.

*Partly persuasive.* It is why trend break is 20% rather than the 12% from the semis-only mapping. I go no higher because none of the trend-break confirmations is in place: HY OAS is 3.16% (not above 3.46%), VIX/VIX3M is 0.898, and QQQ is above 683.7.

## 7. Scenarios

### Shallow pullback (33%): lowest close ≥ 210.00

**Zone:** 211–218.9, core 214.5–217.2.
- 100-day 214.45; 50% Fibonacci level on closes 214.63.
- 50% Fibonacci 216.69; Sep 17 gap 216.76–217.15.
- 3-month volume POC 218.85.
- Intraday undercuts to about 208.9 are tolerable.

**Timing:** Oct 15–23; Oct 29 at the latest.

**Path**
1. TSMC beats and the green close holds through Oct 16 expiration.
2. NVDA holds 214.45, and META's capex is accepted on Oct 21.
3. NVDA closes above 223.21 by Oct 23.
4. On Oct 28 the Fed holds, and MSFT and GOOGL raise capex *and* their stocks rise.
5. NVDA closes above 230.48 before the print, then retests 235.74–239.24.

**Confirming signals**
- Closes at or above 214.45 through Oct 21.
- A close above 223.21 by Oct 23.
- NVDA/SOXX does not fall more than 5% in a week.
- SOXX holds 497.40 and QQQ holds 697.
- VIX/VIX3M stays below 0.95.
- HY OAS stays at or below 3.25%.

**Invalidation**
- Any close below 210.00.
- A TSMC beat with NVDA still closing below 214.45 on Oct 15–16.
- SOXX closes below 497.40 *and* QQQ below 697 before Oct 23.

### Deeper correction (47%): 190.01 ≤ lowest close < 210.00

**Zone:** 198–209, core 201–207.
- Sep 14 low 208.93; Aug 24 low 207.25; Aug–Sep closing low 206.64.
- Rising 200-day: about 203.3–204.2 by Oct 28, about 204.4–205.6 by Nov 18 [calc].
- 78.6% Fibonacci levels 201.43 / 200.55; YTD anchored VWAP 200.85; the 200-strike put shelf.
- DB analog median maximum adverse excursions: about 203.4 at 20 days and 199.6 at 40 days.

**Timing:** Oct 26 – Nov 13, with the mode Oct 28 – Nov 6. Second window: earnings week (Nov 18–27).

**Path**
1. 214.45 and then 210 break between Oct 16 and Oct 28, as SOXX loses 497.40 and QQQ tests 680–700.
2. The Oct 28 cluster punishes capex and/or the Fed stays hawkish.
3. NVDA tags 201–207 on a volatility spike (VIX/VIX3M at or above 0.95).
4. NVDA recovers to 215–225 into the print.

**Confirming signals**
- A close below 210 with SOXX below 497.40.
- NVDA's down-day ratio to SOXX above 0.8 for 3 or more sessions.
- HY OAS at 3.3–3.46%, but no higher.
- SOXX holds 465, or reverses above it on capitulation.
- A reversal day near the 200-day that closes in the upper half of its range.

**Invalidation**
- **Upside:** every close at or above 210 through Oct 30, plus a close above 230.48.
- **Downside:** a close below 190.01. Two closes below 200.85 *before* Oct 28 would mean the decline is accelerating, and would shift odds toward a trend break.

### Trend break (20%): lowest close < 190.01

**Zone:** 175–189, core 179–188.
- Jun 29 low 189.80; Apr 14 gap 189.66–190.77.
- Apr 10 gap 184.08–184.30.
- −25% from the record: 179.4.
- Apr 8 gap 178.23–180.30 and the anchored VWAP from Apr 2025, 178.37.
- The 2024 analog (−27%): about 174.6.
- **Tail:** 165–172. The 52-week low is 164.08.

**Timing:** Nov 10 – Dec 4. The low may fall after the window: the Dec 9 FOMC follows, and in 2018 the low came on Dec 24.

**Path**
1. An Oct 28 hike with a signalled follow-up, a 10-year yield above 5.31%, or capex punished.
2. QQQ falls below 661.73 and SOXX below 465, with NVDA catching down at a ratio of about 1.
3. A credit event:
   - CoreWeave (about Nov 10, date estimated) shows funding stress;
   - OpenAI financing is delayed;
   - or NVDA takes on a new credit-support commitment.
4. The print fails to stop the decline.

**Confirming signals**
- Two closes below 200.85, then a close below 195.
- SOXX below 465 on more than 2× volume.
- QQQ below 683.7 before Oct 28.
- The S&P 500 below 7,505 with RSP below 207.16.
- HY OAS above 3.46%.
- CoreWeave 2032s below 75c.

**Invalidation:** every close through Dec 4 holds 190.01. A V-shaped flush below that line still counts as a trend break on price.

## 8. Key levels (closing basis; % vs 221.30 / vs 218.35)

| Level | Type | % | Why |
|---|---|---|---|
| 243.37 / 239.24 | Resistance | +10.0 / +8.1; +11.5 / +9.6 | Intraday record / record close |
| 235.74 | Resistance | +6.5 / +8.0 | May high and the failed-breakout level. A close above voids the bear case |
| 229.85–230.98 | Resistance | +3.9 to +4.4 / +5.3 to +5.8 | Oct 8 pivot (low 229.85, close 230.48); Oct 6 anchored VWAP 230.98. Reclaiming it means the low is in |
| 228.86–229.11 | Resistance | +3.4 to +3.5 / +4.8 to +4.9 | Unfilled Oct 12 gap |
| 222.60–223.21 | Resistance | +0.6 to +0.9 / +2.0 to +2.2 | 50-day; 38.2% Fibonacci 222.99; 50-day EMA. The first repair close |
| 220.0–221.01 | Pivot | −0.6 to −0.1 / +0.8 to +1.2 | Jul-low anchored VWAP; the Oct 16 pin |
| 216.69–218.85 | Support | −2.1 to −1.1 / −0.8 to +0.2 | 3-month POC; Sep 17 gap; 50% Fibonacci. Overnight trade sits on it |
| 214.45–214.63 | Support | −3.1 / −1.8 | 100-day; 50% Fibonacci on closes. The shallow core floor |
| **210.21–211.02** | **Hinge** | **−5.0 to −4.7 / −3.7 to −3.4** | Mar 30 anchored VWAP; 61.8% Fibonacci 210.39; Sep 14 close 210.96; 6-month POC 211.02; Nov max pain about 210 |
| 206.64–208.93 | Support | −6.6 to −5.6 / −5.4 to −4.3 | Aug–Sep closing low; Aug 24 and Sep 14 lows. The higher-low structure |
| 200.55–202.69 (rising to about 204–205) | Support | −9.4 to −8.4 / −8.2 to −7.2 | 200-day; YTD anchored VWAP 200.85; 78.6% Fibonacci; 200-strike put shelf. Two closes below it are a trend-break warning |
| 195.04 | Support | −11.9 / −10.7 | Jul 30 close |
| **190.01** | **Trend line** | **−14.1 / −13.0** | Jul 29 closing low; Jun 29 low 189.80; Apr 14 gap |
| 178.2–184.3 | Support | −19.4 to −16.7 / −18.3 to −15.6 | Apr 10 and Apr 8 gaps; anchored VWAP from Apr 2025 |
| 171 | Reference | −22.7 / −21.7 | The user's IBKR liquidation level (reference only) |

## 9. Catalysts, what tells the scenarios apart, and what would change the verdict

**Timeline** [CAT, FX]
- **Oct 15:** TSMC results; PPI.
- **Oct 16:** options expiration (the 220 pin).
- **Oct 21:** META, LRCX, TXN; VIX expiration.
- **Oct 28: FOMC (2 pm; 24–32% hike odds); MSFT, GOOGL, KLAC after the close.**
- **Oct 29:** INTC, AMZN (estimated), GDP/PCE.
- **Nov 3–4:** AMD, ARM; midterms.
- **Nov 6:** payrolls.
- **About Nov 10:** CPI; CoreWeave (estimated).
- **Ongoing:** the OpenAI financing round (about $1.4T, single-source).
- **NVDA results, Nov 18–25 (unannounced):** the test is a Q4 guide of about $120bn or more, the 71–72% gross-margin trough holding, FY28 about +70% reaffirmed, and no new guarantees.
- **Nov 20:** options expiration.

**What tells the scenarios apart**

| Window | Question |
|---|---|
| Oct 15–16 | Does a TSMC beat close green and hold? Does NVDA hold 214.45 into and after expiration? |
| Oct 21–23 | A close above 223.21 favours shallow. A close below 210 before Oct 23 makes deeper the base case. A close below 200.85 before Oct 28 points to acceleration |
| Oct 28–29 | Does capex rise with the spender's stock up (the July MSFT/AMZN pattern) or down (GOOGL/META)? Is there a hike? |
| Nov | Credit (CoreWeave, guarantees) and the print. A print is a poor base-rate bottoming event (7 of 9 lower five sessions later) |

**What would move me to shallow above 45%**
- A TSMC green close that holds, plus a close above 223.21 by Oct 23 without losing 214.45.
- Or a close above 230.48 before Oct 28.

**What would move me to trend break above 30%**
- A close below 200.85 before Oct 28.
- NVDA/SOXX down more than 5% in a week while SOXX is below 497.40, which would mean catch-down.
- HY OAS above 3.46%, or CoreWeave 2032s below 75c.
- An Oct 28 hike with hawkish guidance.
- A new NVDA credit-support commitment.
- QQQ below 683.7 before Oct 28.

**Single most important level:** **210 on a closing basis** (the 210.2–211.0 cluster). It separates shallow from deeper and is the bull's own invalidation. **190.01** is the trend line; **230.48** confirms on the upside.

**Single most important event:** **Wed Oct 28**: the FOMC, then MSFT and GOOGL capex after the close. Hyperscalers were 55% of NVDA's Q2 Data Center revenue. NVDA's own print (Nov 18–25) comes second, and TSMC on Oct 15 is the first test.

## 10. TSMC

TSMC Q3 results were **not out** at about 04:25 UTC Oct 15. WebSearch found only previews and the [TSMC IR page](https://investor.tsmc.com/schinese/quarterly-results).

**How to read it**
- **Toward shallow:** a Q4 guide up quarter on quarter, gross margin at or above about 65%, capex at or above $60–64bn, *and* an NVDA close at or above 216.7 that holds through Oct 16.
- **Toward deeper or trend break:** a flat or down guide, "digestion" language, or a beat that fades to an NVDA close below 214.45.

## Sources

**Data and research**
- DATA_BRIEF.md, base_rates.json, technicals.json, levels.json, betas_ratios.txt, analog_forward_returns.txt, live_snapshots.md.
- Long Yahoo files in dl_nvdabull/.
- research/*.md (catalysts, sentiment_positioning, semis_leadership, oct8_narrative, oct8_skeptic, macro_rates, zz_verification_corrections) and analysis/verify/facts.md.
- market, tech and semis verdicts; nvda_bull.md and nvda_bear.md.

**Primary filings (via [CAT] / [FX])**
- NVDA 8-K, Aug 17 (guarantees): https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm
- NVDA 10-Q, Aug 26: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- NVDA Q2 FY27 transcript: https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf

**News**
- Hike odds: Reuters via Investing.com, Oct 14: https://www.investing.com/news/stock-market-news/
- CoreWeave and Asia: Reuters via Investing.com: https://www.investing.com/news/stock-market-news/asia-stocks-slump-as-chip-rout-deepens-after-hotter-us-inflation-4950421

**My scripts and live data**
- `scratchpad/nv_scripts/v1.py`, `v2.py`, `v3.py`, `mc.py`.
- IBKR real-time, 04:24 UTC Oct 15: NVDA (4815747), SOXX (12658194), QQQ (320227571).

## UNVERIFIED or caveated

- **Dates:**
  - NVDA's earnings date is unannounced (Nov 18–25).
  - AMZN's and CoreWeave's dates are estimates.
- **Single-source figures:**
  - Hike odds (24–32%, varies by venue).
  - Hedge-fund positioning percentiles.
  - The OpenAI round terms.
- **Inferences and unsettled facts:**
  - NVDA's buyback blackout is inferred.
  - The OpenAI "gross vs net" explanation is not settled.
- **Base rates:** samples are small and overlapping (effective n ≈ 6–10 episodes). Pre-2016 NVDA is excluded from the record-based sets because NVDA made no records between 2007 and 2016.
- **My own judgment and models:**
  - The conditional mapping tables are judgment.
  - The simulation is a no-drift, no-information benchmark, not a forecast.
  - Options data comes from partial chains, and the risk-neutral odds are approximations.
- **Prices and projections:**
  - Overnight prints are thin, not closes.
  - The 200-day projections assume flat prices.
- **TSMC:** results were pending when this was written.
