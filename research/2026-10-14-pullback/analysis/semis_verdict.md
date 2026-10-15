# Layer 3 verdict: semiconductors (SOXX / SMH / SOX)

*Chief analyst for semis. Written about 04:15–04:45 UTC Oct 15 (12:15–12:45 am ET). Data runs through the Oct 14 close, plus IBKR overnight quotes.*

**Source tags**
- **[DB]**: data/DATA_BRIEF.md and its companion files.
- **[MV] / [TV]**: market_verdict.md (with its audit addendum) and tech_verdict.md.
- **[SL] / [CAT] / [SP] / [MR] / [FX]**: research/semis_leadership.md, catalysts.md, sentiment_positioning.md, macro_rates.md, and analysis/verify/facts.md together with research/zz_verification_corrections.md.
- **[calc]**: my scripts in `scratchpad/sv_scripts/`:
  - `levels_verify.py`: ranges, AVWAPs, Fibonacci levels, 200-day paths, volume profile.
  - `sox_baserates.py`: ^SOX daily 1994–2026 and ^NDX, unbiased swing-pullback signals.
  - `incr_beta.py`: how far SOX fell relative to NDX after past signals.
  - `extra.py`: betas.

**Live checks**
- **IBKR real-time, 04:10 UTC:** SOXX **509.46** (−1.92%), QQQ 720.92 (−1.10%), NVDA 218.25 (−1.38%). SOXX implied vol 35.6%, at the 26th percentile of its 52-week range.
- **Asia overnight** [FX; AP and Reuters]: KOSPI −7.7%, SK Hynix −11.4%, Samsung −9.5%, Kioxia −11.2%, Tokyo Electron −7.3%, Taiex −3%.
- **TSMC Q3:** **not out when I checked at about 04:12 UTC and again at about 04:17 UTC** (WebSearch returned previews and older years only). It is due about 05:30–06:00 UTC and is not used below. §7 gives explicit rules for how to read it.

## Bottom line

| Scenario (lowest SOXX **daily close**, Oct 15 – Fri Dec 4) | Boundary | Prob. | Bottoming zone (SMH / SOX equivalent) | Drawdown: from the 589.51 Oct 5 high / from the 655.01 Jun 22 record | Low most likely forms |
|---|---|---|---|---|---|
| **Shallow pullback** | Low ≥ **497.40** (Sep 14 close) | **26%** | 497.4–515, core 500–512 (SMH 541.5–561; SOX 11,130–11,500) | −12.6% to −15.6% / −21.4% to −24.1% | Oct 15–23 |
| **Deeper correction** | 465.00 ≤ low < 497.40 | **39%** | 465–497, core 474–492 (SMH 504–541, core 515–535; SOX 10,450–11,130) | −15.6% to −21.1% (core −16.5% to −19.6%) / −24.1% to −29.0% | Oct 21 – Nov 10; mode Oct 28 – Nov 4 |
| **Trend break** | Low < **465.00** (Jul 29 close; a new cycle low) | **35%** | 420–460, core 435–455; tail about 400–410 (SMH 452–499; SOX 9,500–10,340) | −22% to −29% (tail −32%) / −30% to −36% (tail −39%) | Nov 3 – Dec 4, and it may come after the window |

**The deeper bucket is the most likely, but the edge is thin. Trend break is a close second, and well ahead of shallow.**
- My median lowest close is about **480–485**.
- **Most likely closing-low zone: SOXX 474–497.** That is −4.3% to −8.7% from the Oct 14 close, −15.7% to −19.6% from the Oct 5 closing high and −24.1% to −27.6% from the June record.
- SMH equivalent: about 515–541. SOX equivalent: about 10,640–11,120.

**This is not a buy-the-dip call.**
- Overnight, SOXX trades at 509.46, already **−13.6%** from the Oct 5 closing high and only 2.4% above the 497.40 hinge.
- None of the semis capitulation markers are present: volume is below 2× its average, breadth is not at 0–5%, VIX/VIX3M is not above 1, and there are no sell-side downgrades.

## 1. Where the early-October move sits: a failed breakout, with the larger base still undecided [calc, DB, SL]

**What the "breakout" actually was.** It was a break out of the Aug–Sep range, **not a new high**.
- **The range (Aug 1–Sep 16):** closes 497.40 (Sep 14) to 559.12 (Aug 17); intraday 485.71–566.02; midpoint 528.26.
- **Step 1:** SOXX first closed above 559.12 on **Sep 21 (559.34)**. It closed at 572.78 on Sep 22 and then built a late-September shelf at 551.95–579.98.
- **Step 2, the actual "early-October breakout":** the **Oct 2 gap** above that shelf (open 590.91). The closing high was **589.51 on Oct 5**; the intraday high was 596.44 on Oct 2.
- **Context:** SOXX's June record is 655.01, and its July closing high was 599.70. Measured against June, October was a **lower high**. On a weekly basis it was 588.9 vs 639.5.
- **Definitions note:** DATA_BRIEF's "~573 range top" uses an Aug 1–Sep 24 window that already contains the post-breakout Sep 22 close. The clean range top is **559.12** on closes and **566.02** intraday.

**Evidence that it failed**
- **A retest should hold the breakout level. Both levels gave way:**
  - The 572.78 shelf was lost on the **Oct 8** close (563.28).
  - The 559.12 range top was lost on the **Oct 12** close (544.85).
- SOXX closed Oct 14 below the 528.26 midpoint.
- **It sits below every anchored VWAP that matters** [calc]:

  | Anchor | AVWAP |
  |---|---|
  | Oct 5 high | 555.84 |
  | Sep 14 low | 548.99 |
  | Jun 22 peak | 544.50 |
  | Jul 29 low | 530.19 |
  | Mar 30 low | 525.39 |

- **Volume favoured sellers.** The Oct 2 breakout day traded 6.88M shares, against 10.36M (1.40×) on Oct 8 and 10.67M (1.52×) on Oct 14.
- **Seven straight down closes** retraced 56% of the Jul 29 → Oct 5 rally.
- **Overnight, 509.46 is already below** the Sep 17 breakaway gap (510.37–514.80) and the 61.8% retracement on closes (512.56).
- The two-point line of closing lows from Jul 29 (465.00) to Sep 14 (497.40) projects to about **520 today**. SOXX closed on it at 519.42 and is now below it. This trend line is subjective.

**Evidence that this is still a retest of the larger base**
- SOXX is still **inside** the range and above its floor.
- Intraday lows since July are rising: 464.08 → 485.71 → 489.21 → 495.15.
- Since Jul 29 the structure is a higher high (589.51 vs 559.12) and a higher low (497.40 vs 465.00).
- SOXX is +11.5% above a 200-day that is rising 5.9% per 20 sessions.
- SOXX/SPY is still 5.8% above its own 200-day, with no relative lower low.

**Verdict on the structure**
- **The breakout itself has failed. That is settled.**
- **What is still open:** does the failure resolve into a wider base with a higher low, or into a full traverse of the range and a breakdown?
- **The deciding level is SOXX 497.40 on a closing basis.** It is the Sep 14 low, sitting on the 3-month volume POC of 500.28 [DB], with 495.15 as the intraday line. On the sister measures it is **SMH 541.50** and **SOX 11,131.28**.
- **Below it,** the range measured move points to **435.7** (497.40 − 61.72), with 465 first.

**Larger structure since the Jun 22 peak**
- **The path:** 655.01 → 465.00 on Jul 29 (−29.0%, 26 sessions) → 559.12 → 497.40 → 589.51 → 519.42.
- **Against June** the highs are lower: 655.01, then 599.70, then 589.51.
- **Since July** the highs and lows are both higher.
- This is a contracting triangle. Price is now pressing the rising lower edge.
- **The air pocket:** only about **7.7% of 3-month volume traded at 465–495**, against 12.4% at 495–505 and 19.3% at 505–520 [calc, range-distributed profile]. Once 495 goes, there is little volume support until the 465–486 cluster.

## 2. Key levels (closing basis; % vs the 519.42 close)

| Level | Type | % | Why |
|---|---|---|---|
| 583.89–589.51 | Resistance | +12.4 to +13.5 | Unfilled Oct 7 gap; Oct 5 closing high |
| 552.87–566.02 | Resistance | +6.4 to +9.0 | Oct 12 gap (552.87–557.26); Oct 5 AVWAP 555.84; Oct 2 AVWAP 559.71; old range top 559.12 / 566.02. **A close above 559 voids the failed breakout** |
| 538.43–545.88 | Resistance | +3.7 to +5.1 | 50-day 538.43; Sep-start AVWAP 539.98; 38.2% Fibonacci 541.95 / 545.88; Jun 22 AVWAP 544.50 |
| 525.39–531.33 | Resistance | +1.2 to +2.3 | Mar 30 AVWAP; midpoint 528.26; 50% Fibonacci 527.26 / 530.26; Jul 29 AVWAP 530.19. **The first repair** |
| 517.5–520.7 | Pivot (lost overnight) | −0.4 to +0.3 | Oct 14 low 517.47; rising lows line about 520 |
| 510.37–514.80 | Support | −1.7 to −0.9 | Unfilled Sep 17 gap; 61.8% Fibonacci 512.56 (closes) / 514.64 (intraday). Overnight trade is below it |
| **495.15–500.28** | **Support (hinge)** | **−4.7 to −3.7** | **Sep 14 low 497.40 close / 495.15 intraday; 3-month POC 500.28 (11.7% of volume). Shallow vs deeper** |
| 485.71–492.41 | Support | −6.5 to −5.2 | 78.6% Fibonacci 491.65 / 492.41; Sep 3 low 489.21; Aug 3 low 485.71 |
| 474.5–486 | Support (cluster) | −8.7 to −6.4 | Rising 200-day: 474.5 by Oct 28, 478.5 by Nov 4, 485.7 by Nov 18, 493.7 by Dec 4 (flat path at 495) [calc]. YTD AVWAP 476.52; 50% of the Mar 30 → Jun 22 run 482.40 |
| **464.08–465.65** | **Trend line** | **−10.7 to −10.4** | **Jul 29 low 465.00 close / 464.08 intraday; 200-day today 465.65. Deeper vs trend break** |
| 435.7–441.7 | Support | −16.1 to −15.0 | Range measured move; 61.8% of the Mar–Jun run 441.66 |
| 407.5–409.6 | Support | −21.6 to −21.2 | Unfilled Apr 17 gap |

**Timing caveat:** a late low in the deeper bucket would sit *below* the 200-day. The 200-day climbs to about 486 by Nov 18 and about 494 by Dec 4.

## 3. Internals

**Breadth (29-name basket) [SL]**
- **14%** are above their 50-day, down from 93% on Oct 6. The reading was 17% at the Sep 14 low and 0% at the Jul 29 low.
- **76%** are more than 20% below their highs; the median name is −30.8%.
- 66% remain above their 200-day.
- The basket uses today's names, so it carries survivorship bias.

**Leadership and rotation inside semis (median moves since Oct 6) [SL]**

| Group | Move | Notes |
|---|---|---|
| Optics / networking | −19.9% | COHR −22.2%, LITE −20.9% |
| AI compute, excluding the mega-caps | −14.5% | ALAB −23.0%, ARM −21.3%, CRDO −18.8% |
| Foundry / equipment | −12.5% | AMAT −15.8%, LRCX −14.1%, KLAC −9.4%; ASML ADR −3.9% on a beat-and-raise |
| Memory / storage | −12.0% | **−36.5% since Jun 22** |
| Analog | −11.0% | Only −5.0% since Oct 8; TXN and ADI still above their 50-day |
| NVDA / AVGO / TSM | −7.5% / −7.9% / −10.8% | |

- Overnight, Asian memory and equipment fell another 7–11% [FX].
- **What the rotation says:** money is not exiting on an AI-demand collapse. If it were, NVDA would lead the decline; instead NVDA/SOXX is +5.0% since Oct 6.
- Three things are being de-grossed:
  - the crowded momentum and financing-sensitive tail;
  - memory, where the rate of price increase is turning (TrendForce: "price increases are slowing"; CXMT);
  - semi-cap, where good news is being sold.
- This pattern of defensive analog stocks plus mega-cap quality holding up is what a correction looks like. In a final flush, the last leaders usually catch down.

**Volume, volatility and positioning**
- **Volume and momentum:** SOXX volume is 1.52× its 50-day average (2.88× on Jun 5; 1.79× on Jul 29). RSI is 37.3 (33.1 at Jul 29).
- **Volatility:** VIX 16.87, VIX/VIX3M 0.898 [DB].
- **Hedging:** the SOXX option put/call ratio is 2.59 against a 1.87 average, so puts are bid [SP].
- **Crowding:**
  - BofA FMS names long semis the most crowded trade (CONFIRMED). The 45% share figure is SINGLE-SOURCE.
  - SOXL took +$711.9M on Oct 13 (one vendor).

**Relative strength**
- SOXX/SPY fell 10.0% in five sessions. It is below its 50-day and +5.8% above its 200-day.
- SMH/QQQ is below its 50-day.

**Macro and credit [MR, FX]**
- **Rates:** 10-year 5.19–5.21%; real yield about 2.9% (the highest since 2008).
- **Spreads:** HY OAS 3.16% (91st percentile); CCC at a 3-year high.
- **AI credit:** CoreWeave 2032s **below 78c** overnight (Reuters).
- **Fed:** Oct 28 hike odds were **24–32% late Oct 14** (corrected from the stale 35% and 54%).
- **No cushion from yields:** yields fell 12 bp from their peak while SOXX fell 11.9%.

## 4. How the market and tech verdicts constrain semis (mandatory conditioning)

**Market [MV, audited 46 / 34 / 20; hinge S&P 500 7,505]**
- **The market layer barely constrains semis on the downside.**
- **June–July 2026 precedent:** SOXX −29% while the S&P 500's worst close was only −4.5%, because RSP rallied.
- **So a market shallow outcome is compatible with any semis bucket.** The semis 497 / 465 tests are decided by tech and by semis-specific flows.
- **It does constrain the trend-break timing.** MV says that in a market trend break, the high-beta low comes after NVDA's results.

**Tech [TV, 35 / 40 / 25; hinge QQQ 697–700, trend line 661.73]**
- **Betas** [DB, calc]:
  - SOXX to QQQ: **2.04** over 1 year, 2.26 over 6 months.
  - Down-day beta: **2.25 / 2.46**.
  - Correlation: 0.85–0.89.
- **Residual vol** is about 22–24% a year, roughly ±6% over 20 sessions, so decoupling is common.
- **Semis have already overshot their beta:** since Oct 6, SOXX is −11.9% against QQQ −4.0% (2.9×).
- **In past SOX signals** (the first close ≥11.6% below the 60-day high, n=54), SOX's further fall ran only about **1.1–1.2×** NDX's further fall, in points of each index's high (correlation 0.84–0.91) [calc]. That is about 1.5× in today's price terms.
- **Mapping each tech scenario onto SOXX** (effective beta 1.5–2.0):

  | Tech scenario | QQQ low | SOXX range by beta | Conditional SOXX odds (judgment) |
  |---|---|---|---|
  | Shallow | 700–716 | about 478–505 | **straddles 497.40**: S 0.60 / D 0.36 / T 0.04 |
  | Deeper | 672–692 | about 440–480 (core 450–478) | **straddles 465**: S 0.07 / D 0.50 / T 0.43 |
  | Trend break | below 661.73 | ≤ about 440 | S 0.01 / D 0.06 / T 0.93 |

  - The analog bins agree. With NDX's further fall ≤4.5 points, 68–81% of SOX lows held −15.6%. With 4.5–9 points, the outcome was 0–8% shallow, 54–56% deeper and 38–44% trend break (n=9–13).
- **Top-down result:**
  - With TV's 35/40/25: **24 / 34 / 42**.
  - With TV re-weighted for MV's audit (about 38/37/25): **26 / 34 / 41**.

**Where semis can decouple**
- **Upward:** a semis-specific washout can mark the low *before* QQQ does, as in July, when the semis low came on the MSFT print.
- **Downward:** memory and semi-cap can keep falling while mega-caps cushion QQQ.
- **NVDA for the layer below:**
  - Beta to SOXX is **0.39–0.52** (correlation 0.54–0.62), so NVDA can decouple from semis. In June–July, NVDA fell −8.9% while SOXX fell −29%.
  - Beta to QQQ is **1.16–1.30**, so it cannot decouple from tech.
  - In a semis capitulation, the "last leader" usually catches down.

## 5. Checking the advocates' numbers

| Claim | Status |
|---|---|
| Breakout and range data (559.34 on Sep 21; 15 closes above; back inside on Oct 12; midpoint 528.26; gap 510.37–514.80; Fibonacci 512.56 / 491.65) | **Confirmed** [calc] |
| Bear's AVWAPs (Oct 5 555.84, Jun 22 544.50); 200-day about 474 / 478 / 483–486 for Oct 28 / Nov 4 / Nov 18. Bull's 470.5 (Oct 21) / 475 (Oct 28) | **Confirmed** [calc] |
| Bear: volume 6.88M vs 10.36M (1.40×) and 10.67M (1.52×); measured move 435.7; down-day beta 2.25 | **Confirmed** |
| Bull: swing-leg median −16.6% (≈491.6) | **Consistent.** My unbiased set above a rising 200-day: median 36-session low −16.6% (n=31) |
| Bull: "SOXX once 10% below its record, median further −4.2% (≈497.6)" | **Misapplied.** That figure is measured from the record. On that basis SOXX is −20.7%, where the DB conditional is n=1 at −41.7%, and over 5 years from −15% it is n=4 at a median −29.2% (≈464) |
| Bear: "QQQ at 700 → SOXX 468–478" | Arithmetic **confirmed** at beta 2.0–2.5. But the full daily beta overstates the remaining move after a 2.9× overshoot; the analog-incremental beta gives about 488 |
| Bear: 496–504 holds 14.6% of 3-month volume | **Method-dependent.** I get 12.4% for 495–505 (range-distributed). The air pocket below is confirmed |
| Both: Oct 28 hike odds of about 35% | **Stale.** Late Oct 14 pricing was 24–32% [FX] |
| Both: ASML −3.9% | This is the **ADR** move [FX] |
| Bull: fast-leg set (16 legs, 75% troughed within 14.5 sessions). Bear: lower-high subset (n=14, 5 undercut) and 57-signal table | **Not re-run (advocate-computed).** My closest version gives n=54 and a median 36-session low of −16.1% |

## 6. Calibration: base rate first, then regime

**Reference sets.** Lowest close within 36 sessions, bucketed at −15.6% and −21.1% from the swing high (= 497.40 / 465.00) [calc].

| Reference set (^SOX) | n | Shallow / Deeper / Trend break | Median low |
|---|---|---|---|
| First close ≤ −11.6% vs 60-day high, above a rising 200-day, 1995– | 31 | 42 / 29 / 29 | −16.6% (≈492) |
| Same, 2003– | 21 | 43 / 33 / 24 | −16.6% |
| Same, 2009– | 20 | 45 / 30 / 25 | −16.1% |
| + NDX within 6% of its 1-year high (semis-led, today's state) | 10 | 30 / 50 / 20 | −17.1% |
| From the overnight state (≤ −13.5%), above a rising 200-day | 20 | **20 / 40 / 40** | −18.0% (≈483) |
| Overnight state, 2003– | 13 | 23 / 46 / 31 | −17.5% |
| Top-down (§4) | — | 24–26 / 34 / 41–42 | — |

**Notes on the reference sets**
- The median time to the low was 6–10 sessions, and 24–30% of signals marked the low on the signal day itself.
- **DB episode stats (measured from the record):** SOXX drops of 8% or more since Oct 2023 had a median depth of −13.4% and took a median 16 sessions to trough. On the record basis the frame is hostile, at −20.7% now.
- The **2018 tightening-midterm analog** puts SOX −14.6% further from Oct 14, which is about 443 [SP].

**Blend**
- The semis-only rates, weighted 60/40 toward the overnight state, give about 31 / 38 / 31.
- Averaging that with the top-down mapping gives **about 28 / 36 / 36**.

**Regime adjustments**
- **Bearish:**
  - The Asian memory and semi-cap rout overnight.
  - The third good-news sale (ASML).
  - AI credit: CoreWeave 2032s below 78c.
  - Crowding, and no capitulation yet.
  - The 465–495 air pocket.
  - A hiking Fed with real yields at 2008 highs.
- **Bullish:**
  - Breadth at a near-washout 14%.
  - Puts are bid.
  - The dense 465–486 demand cluster: the rising 200-day, YTD AVWAP, the 50% retracement of the Mar–Jun run, and the Jul 29 low.
  - Hard fundamentals, plus the July pattern of a low on a hyperscaler print.
  - NVDA and AVGO are holding.
- **Net:** three points from shallow to deeper (overnight state and Asia), and one point from trend break to deeper (the support cluster). **Final: 26 / 39 / 35.**

**Strongest case that "deeper" is wrong**
1. **Trend break could be the true mode.**
   - The mandatory top-down mapping gives 41–42%.
   - The overnight-state base rate gives 31–40%.
   - Memory de-grossing is accelerating, not exhausting.
   - The failed breakout plus a lower high is the 2018 template.
   - Below 495 there is little volume.
   - *Partly persuasive:* it is why trend break is 35% rather than 29%.
   - *Why it is not the mode:* on the analog-incremental slope, the tech-deeper core (QQQ 680–690) maps to about 467–478, so the central path holds 465. And none of the trend-break preconditions has triggered: HY OAS is not above 3.46%, VIX/VIX3M is not above 1, and QQQ is not below 683.7.
2. **Shallow could happen.** The close-state base rates are 42–45% shallow, and TSMC could be the first good news the market buys. I discount this because the overnight print already uses half the cushion (509.46 vs 497.40) and the top-down mapping gives only 24–26%.

## 7. Scenarios

**Shallow (26%): lowest close ≥ 497.40**
- **Zone:** 497.4–515, core 500–512. Built from the Sep 17 gap, the 61.8% Fibonacci level, the 3-month POC and the Sep 14 low. Intraday undercuts to about 490 are tolerable.
- **Path:**
  1. TSMC beats and raises, and SOXX closes green on Oct 15–16 and holds through options expiration.
  2. LRCX and TXN guide up on Oct 21.
  3. SOXX closes above 530.19 by Oct 23.
  4. The Oct 28 FOMC holds, and MSFT/GOOGL show capex with revenue.
  5. SOXX retests 545–559 in November.
- **Confirming signals:**
  - QQQ holds 697 [TV].
  - SMH holds 541.50.
  - Basket breadth gets back above 50%.
  - SOXX/SPY reclaims its 50-day.
  - Memory stabilises: MU, SK Hynix.
- **Invalidation:** any close below 497.40, or SMH below 541.50, or a TSMC beat that closes SOXX red below 510.

**Deeper correction (39%): 465.00 ≤ lowest close < 497.40**
- **Zone:** 465–497, core 474–492. Built from the 78.6% Fibonacci level, the Aug and Sep lows, the 50% retracement of the Mar–Jun run at 482.40, the YTD AVWAP at 476.52 and the rising 200-day at 474–486.
- **Path:**
  1. 497.40 breaks around Oct 16–22.
  2. Memory and semi-cap keep de-grossing, and QQQ tests 680–700.
  3. A flush into the Oct 28 – Nov 4 cluster (FOMC, MSFT/GOOGL/KLAC, INTC, AMD, ARM) marks the low with a capitulation signature.
  4. SOXX recovers to about 510–530 into NVDA's results.
- **Confirming signals:**
  - Volume above 2× its average on the low day, closing in the upper half of the range.
  - Basket breadth at 5% or less, then a reversal.
  - VIX/VIX3M above 1, briefly.
  - HY OAS at 3.3–3.46% but no higher.
  - SMH holds 504.22.
- **Invalidation:**
  - **Upside:** every close at or above 497.40 through Oct 30, plus a close above 530.19.
  - **Downside:** a close below 465.00, especially *before* Oct 28.

**Trend break (35%): lowest close < 465.00**
- **Zone:** 420–460, core 435–455, from the measured move 435.7 and the 61.8% retracement of the Mar–Jun run at 441.66. Tail: the Apr 17 gap at about 408.
- **Path:**
  1. Either an Oct 28 hike with hawkish guidance, or mega-cap capex is punished (the July GOOGL/META pattern) while memory rolls over.
  2. QQQ falls below 683.7, then 661.73.
  3. AI credit spreads: CoreWeave about Nov 10, HY OAS above 3.46%.
  4. NVDA's results (Nov 18–25, unconfirmed) fail to stop it, as 7 of NVDA's last 9 prints were lower five sessions later.
- **Confirming signals:**
  - A SOXX close below 497.40 on more than 2× volume before Oct 21.
  - SMH below 504.22.
  - NVDA below 208.8.
  - SOXX/SPY makes a lower low under its Sep 14 level.
  - The 10-year above 5.31%.
- **Invalidation:**
  - Every close through Dec 4 holds 465.
  - A capitulation reversal above 465 shifts the call to deeper.
  - A V-shaped flush below 465 still counts as a trend break.

**Rules for reading TSMC (results pending)**
- **Shift toward shallow (to about 35%):** a Q4 guide up quarter on quarter, gross margin of about 65% or better, capex at or above $60–64bn, *and* a green SOXX close above 512.6 that holds through Oct 16.
- **Shift toward trend break (to about 42%):** a flat or down guide, "digestion" language, or a beat that fades to a SOXX close below 497.40.

## 8. Catalysts in the window [CAT, FX]

| Date | Event | What it would signal |
|---|---|---|
| Oct 14 (done) | ASML: beat-and-raise; ADR −3.9%; LRCX −4.7% | Good news sold: distribution and semi-cap de-rating, even though 2027–28 WFE is intact |
| **Oct 15** | **TSMC Q3 and guide**; PPI | The tape test (see the rules above) |
| Oct 16 | Options expiration | |
| Oct 21 | LRCX (vs $8.10bn guide midpoint), TXN, META; VIX expiration | LRCX shows whether memory WFE survives the Korea rout. TXN is the last strong subgroup |
| Oct 22 / Oct 27 | WDC / NXPI, STX | |
| **Oct 28** | **FOMC (2 pm), MSFT, GOOGL, KLAC** | Capex up with the spender's stock up is the July-low pattern. A second cautious guide from KLAC means the semi-cap de-rating continues |
| Oct 29 | INTC; Samsung full Q3 (single-source); AMZN (estimated); PCE | |
| Nov 3 / Nov 4 | AMD (Election Day) / ARM | The data-center GPU guide. ARM, at −45.8% from its high, is the gauge for momentum names |
| about Nov 10 | CoreWeave (estimated), TSMC October sales; CPI | The financing test |
| Nov 18–25 | NVDA (unannounced) | A weak base rate as a bottoming event |

## 9. What tells the scenarios apart, and what would change the verdict

**Oct 15–16**
- TSMC's reaction.
- Does SOXX close at or above 497.40, with SMH at or above 541.50?

**To Oct 23**
- A close above 530.19 favours shallow.
- A break of 497.40 on more than 2× volume before Oct 21 favours trend break over deeper, because an early break means acceleration.

**Oct 28 – Nov 4**
- Does the break below 497 meet a capitulation signature above 465 (deeper), or a credit and QQQ break (trend break)?

**What would move me toward shallow (above 40%)**
- A TSMC green close that holds.
- A close above 530.19 by Oct 21.
- Basket breadth above 50%.
- QQQ closes above 731.

**What would move me toward trend break (above 50%)**
- An early SOXX close below 497.40 together with QQQ below 697.
- HY OAS above 3.46%.
- CoreWeave 2032s below 75c.
- An Oct 28 hike with hawkish guidance.
- Weak LRCX/KLAC guides.

**Single most important level:** **SOXX 497.40 on a closing basis** (SMH 541.50; SOX 11,131). **465.00** is the secondary line.

**Single most important event:** **Wed Oct 28.** The FOMC decides at 2:00 pm, then MSFT, GOOGL and KLAC report after the close: the hyperscaler capex reaction function plus the semi-cap guide. **TSMC on Oct 15** is the first test.

---

**Sources**
- **Data:** DATA_BRIEF.md, levels.json, base_rates.json, betas_ratios.txt, analog_forward_returns.txt; local Yahoo CSVs (data/SOXX, SMH, _SOX, QQQ, NVDA); long ^SOX/^NDX histories in analysis/sent/long/.
- **Research and verdicts:** research/semis_leadership.md, catalysts.md, sentiment_positioning.md, macro_rates.md, zz_verification_corrections.md; analysis/verify/facts.md; market_verdict.md (with its audit addendum); tech_verdict.md; semis_bull.md; semis_bear.md.
- **IBKR real-time snapshots, about 04:10 UTC Oct 15:** SOXX (12658194), QQQ (320227571), NVDA (4815747).
- **TSMC (WebSearch, about 04:12 UTC Oct 15; results not out):** [Kaohoon](https://www.kaohooninternational.com/?p=592325), [Crypto Briefing](https://cryptobriefing.com/tsmc-record-profit-sixth-quarter-ai/), [TIKR](https://www.tikr.com/blog/tsmcs-q3-earnings-preview-65-profit-growth-but-net-margin-seen-slipping-to-50), [TSMC IR](https://investor.tsmc.com/quarterly-results).
- **Asia rout and CoreWeave below 78c (via facts.md):** [AP via Yahoo](https://finance.yahoo.com/markets/world-indices/articles/south-korea-benchmark-kospi-index-015023409.html); [Reuters via Investing.com](https://www.investing.com/news/stock-market-news/asia-stocks-slump-as-chip-rout-deepens-after-hotter-us-inflation-4950421).

**UNVERIFIED or caveated**
- **Results and quotes:**
  - TSMC Q3 results were pending.
  - Overnight prints are thin and are not closes.
  - The Asian index levels are intraday.
- **Single-source or stale figures:**
  - Hike odds (24–32%, varies by venue).
  - BofA's 45% crowding share; the SOXL flow figure.
  - The IMF GFSR figures (secondary).
- **Unannounced or estimated dates:** NVDA (Nov 18–25); AMZN, CoreWeave, Samsung, SK Hynix and AMAT.
- **Advocate statistics I did not re-run:** the bull's fast-leg set, and the bear's lower-high subset and 57-signal set.
- **My own judgment and data limits:**
  - The conditional table in §4 is my judgment, informed by small analog bins (n=3–19).
  - The rising lows line is subjective.
  - Basket breadth carries survivorship bias.
  - The 200-day paths assume flat prices.
  - Analogs are weighted toward the 1990s.

---

## AUDIT ADDENDUM (analysis/verify/audit_semis.md)
- "The analog bins agree" with the judgment matrix is withdrawn: the omitted all-signals bin (n=18: 17/39/44) and the overnight-state bins put trend break above deeper; mechanically applied bins give a top-down of 24–32 / 22–30 / 42–46 (close state).
- Window is 35 sessions (Thanksgiving), not 36 — this pulls close-state trend-break rates down a few points.
- Stated arithmetic gives 25/40/35, not 26/39/35.
- **Corrected SOXX probabilities ≈ 26 shallow / 37 deeper / 37 trend break** — deeper and trend break are co-modal (statistically indistinguishable); shallow ~25–27% is robust.
- Median lowest close ≈ 477–480 (not 480–485). "No sell-side downgrades" is wrong as worded (Citi cut NXPI/Nova Oct 8; Barclays cut Dell/HPE/NetApp Oct 14); no leader/sector-level downgrade found.
- Unchanged: all levels/zones, hinges 497.40 / 465.00, key level SOXX 497.40 close, key events TSMC Oct 15 → Oct 28.
