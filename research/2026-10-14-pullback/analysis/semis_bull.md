# Semiconductors (SOXX / SMH / SOX): the shallow-pullback case

*Advocate brief, written ~03:50 UTC Oct 15 (11:50 pm ET Oct 14). Data through the Oct 14 close.*

**Source tags**
- **[DB]** DATA_BRIEF.md, levels.json, base_rates.json, analog_forward_returns.txt
- **[SL]** semis_leadership.md
- **[CAT]** catalysts.md
- **[SP]** sentiment_positioning.md
- **[MR]** macro_rates.md
- **[O8]** oct8_narrative.md
- **[MV]** market_verdict.md
- **[calc]** my own scripts in `scratchpad/scripts/`: `semis_bull_stats.py`, `semis_bull_long.py` (^SOX daily 1994–2026, matching data/_SOX.csv exactly where they overlap) and `semis_bull_breadth.py`

**Live checks**
- **Overnight (IBKR real-time, 03:35 UTC):** SOXX 510.64 (−1.69%), QQQ 721.42 (−1.03%).
- **TSMC Q3 was not out** when I searched at about 03:37 UTC. I found previews only: [Kaohoon](https://www.kaohooninternational.com/?p=592325), [Crypto Briefing](https://cryptobriefing.com/tsmc-record-profit-sixth-quarter-ai/), [Hudson Labs](https://www.hudson-labs.com/research/tsmc-q3-2026-earnings-preview-tsm-revenue-and-margins).
- **Upper layers:** no tech_verdict.md existed when I wrote this. I argue alongside MV (Shallow 40 / Deeper 38 / Trend break 22).

## 1. Thesis

1. SOXX's early-October move **failed as a breakout** above the Aug–Sep range top (559–573), but the **post-July uptrend has not failed**. Since the Jul 29 low (465.00) SOXX has made a higher high (589.51 vs 559.12) and a higher low (497.40), and the current leg is a retracement of that up-leg into a dense support shelf.
2. **Projected closing low: SOXX 490–512, core 495–505** (SMH ≈ 532–556; SOX ≈ 11,040–11,530).
   - −1.4% to −5.7% from the 519.42 close.
   - −13.1% to −16.9% from the Oct 5 closing high of 589.51.
   - −21.8% to −25.2% from the Jun 22 record.
3. **Timing: the closing low prints between Oct 15 and Oct 26,** before the Oct 28 FOMC / MSFT / GOOGL / KLAC night. I put **about 50–55%** on the 490 close holding: the edge over a coin flip is modest, not a lock.

## 2. Evidence, ranked by weight

### 2.1 Structure: failed breakout, intact post-July trend

**What the breakout was** [DB, SL, calc]
- SOXX closed above the Aug 17 high (559.12) on Sep 21 at 559.34, and at 572.78 on Sep 22.
- It cleared the late-September shelf on Oct 1 (576.33) and made its closing high on Oct 5 (589.51; intraday 596.44 on Oct 2).
- It fell back inside the range on Oct 12 (544.85) and below the range midpoint (528.26) on Oct 14.

**Retest or failed breakout?**
- **On textbook terms it is a failed breakout,** and I concede that. A retest holds 559–573, and price lost both that zone and the midpoint within six sessions.
- **What keeps it a retest of the launch point** rather than a breakdown:
  - Overnight trade (510.64) sits in the **unfilled Sep 17 breakaway gap (510.37–514.80)**, at the **61.8% retracement** (512.56 on closes, 514.64 on intraday prices).
  - The intraday lows since July are still rising: 464.08 (Jul 29), 485.71 (Aug 3), 489.21 (Sep 3), 495.15 (Sep 14).
- **The deciding level is 497.40 on a closing basis** (the Sep 14 low and the range floor).
  - Above it, the failed breakout resolves into a wider base with a higher low.
  - Below it, the range height projects to about 436, with 465 first.

**Trend context**
- SOXX is 11.5% above a 200-day average that is rising 5.9% per 20 sessions [DB].
- The SOXX/SPY ratio is 5.8% above its 200-day and above its Jul 29 and Sep 14 levels, so there is no relative lower low [SL].

### 2.2 Swing-leg base rates put the median low inside the zone [calc]

**Long history.** ^SOX, 1995–2026: 57 swing legs (8% zigzag) that fell at least 11.9% from a peak set above a rising 200-day.
- Median final depth **−16.6%**, which is **491.6** in SOXX terms.
- 56% ended shallower than −17%, 68% shallower than −20% and 79% shallower than −25%.
- Median 18 sessions from peak to trough.

**Since 2009** (n=30): median −16.0% (495.2), and 63% ended shallower than −17%.

**Fast legs only.** Of the 16 legs that reached −11.9% within 7 sessions, as this one did, 75% troughed within 14.5 sessions of the peak. That points to **Oct 23–26**.

**SOXX-only legs since 2021** (n=10): median −16.2% (494).

**DATA_BRIEF analogs** [DB]
- SOXX once 10% below its record (n=5): a median further −4.2% after first hitting −10% (≈497.6 from here).
- Setup analog (SOXX 15–25% below its record, below the 50-day, above a rising 200-day; n=17 signals including today): median 20-day maximum adverse move −6.2% (≈487); median 40-day return +10.4%, positive 86% of the time.

### 2.3 Breadth is as washed out as at the last two lows

**Semis breadth** (29-name semis basket)
- 14% of the basket is above its 50-day. It was 17% at the Sep 14 low, which preceded an **+18.5%** SOXX rally, and 0% on Jul 29 [SL].

**History of this signal** [calc]
- Signal: basket at or below 17% above its 50-day while SOXX is above a rising 200-day. There were 10 completed signals since 2023.
  - Median 20-day maximum adverse move −2.5%.
  - 9 of 10 were higher 20 sessions later.
  - Worst adverse move −10.9%, in July 2026.
- Caveat: the basket is today's names, so the history carries survivorship bias.

**Volatility at the Sep 16 low** looked exactly like today: VIX 17.71 and VIX/VIX3M 0.898 [SP]. Semis lows have not required index-level panic.

### 2.4 The selling is concentrated in crowded, financing-sensitive pockets

**Group damage** [SL]

| Group or name | Move | Window |
|---|---|---|
| Optics/networking (median) | −19.9% | since Oct 6 |
| CRWV | −28.3% | since Oct 6 |
| NBIS | −25.6% | since Oct 6 |
| Memory (median) | −36.5% | since Jun 22 |
| NVDA | −7.5% | since Oct 6 |
| AVGO | −7.9% | since Oct 6 |
| Analog (median) | −11.0% (−5.0% since Oct 8) | since Oct 6 |

- TXN and ADI remain above their 50-day averages.
- NVDA/SOXX is up 5.0% since Oct 6.
- **Reading:** if end-demand were breaking, the largest AI-compute names would lead the decline. Instead NVDA (−7.5%) and AVGO (−7.9%) are falling less than SOXX (−11.9%), while the momentum and credit-exposed tail (optics, neoclouds, memory) is being de-grossed. TSM (−10.8%) is falling in line with the group, so this argument rests mainly on NVDA and AVGO.

**Positioning is not uniformly long** [SP]
- Discretionary long/short net leverage is at the 2nd percentile (Goldman via Tickmill, SINGLE-SOURCE).
- The SOXX option put/call ratio is 2.59, against a 1.87 average.

### 2.5 Fundamentals keep rising: the July pattern

**Hard data** [CAT, SL]
- **TSMC:** Q3 revenue NT$1,494.2bn, +50.9% y/y and about 2% above the top of its guide (6-Ks).
- **ASML:** Q4 guide of €14.2–15.2bn, above the ~€13.97bn consensus. It says 2027–28 supply will not meet demand (6-K).
- **Micron:** FQ1 guide of $61.5bn.
- **Deutsche Bank:** wafer-fab equipment forecast raised to $154bn / $217bn / $270bn for 2026–28.

**The July precedent** [SL]
- SOXX fell −29% while fundamentals improved.
- The low came on Jul 29 and was followed by +8.5% on Microsoft's Azure print.
- The same kind of catalyst window lands Oct 21 (META, LRCX, TXN) and Oct 28 (MSFT, GOOGL, KLAC).

### 2.6 Cross-layer consistency

**Beta mapping**
- SOXX's beta to QQQ is 2.04 over 1 year and 2.26 over 6 months [DB].
- QQQ's support band at 712–722 maps to **SOXX ≈ 492–509**. That band holds:
  - the Sep 17 gap at 711.88–713.32;
  - the 50% retracement at 712.0;
  - the 3-month volume POC at 718.73;
  - the VWAP anchored at the July low, 721.12.

**Fit with MV**
- MV's shallow scenario has the S&P 500 low "most likely by Oct 23" and "SOXX and NVDA make their lows by late October." My timing matches it.
- **Tension, stated openly:** MV's shallow path takes QQQ to 695–710. At a 2.04 beta that is SOXX ≈ 470–492, at or below the bottom of my zone. My case needs the semis-specific excess to stop. Since Oct 6 SOXX has fallen 2.9x as much as QQQ (−11.9% vs −4.0%), well above its beta.

### 2.7 Seasonality (low weight) [SP]

- In midterm years, SOX's Oct 14 → Oct 31 return averaged +9.0% (up 71% of the time), and November was up in 7 of 7 years.

## 3. Key levels (closing basis unless noted; % vs 519.42)

| Level | % | Why it matters |
|---|---|---|
| 559.12–572.78 | +7.6 to +10.3 | Range top (Aug 17 / Sep 22 closes). A close above negates the failed breakout |
| 538.4–545.9 | +3.7 to +5.1 | 50-day 538.43; VWAP anchored at Sep start 539.98; 38.2% retracement 541.95 / 545.88 |
| **525.4–531.3** | +1.1 to +2.3 | VWAP anchored at Mar 30 525.39; midpoint 528.26; VWAP anchored at the Jul low 530.19; 50% retracement 530.26; volume node 531.33. **The first repair signal** |
| 510.4–515.8 | −0.7 to −1.7 | Sep 17 gap; 61.8% retracement; 3-month volume nodes 511.92 / 515.8. Overnight trade is here |
| **495.2–500.3** | −3.7 to −4.7 | Sep 14 low (497.40 close, 495.15 intraday); 3-month volume POC **500.28 (11.7% of volume, the largest node)**; 6-month node 499.84. **The decision zone and the core of my target** |
| 485.7–492.4 | −5.2 to −6.5 | Aug 3 low 485.71 (intraday); 78.6% retracement 491.65 / 492.41; Sep 3 low 489.21. Intraday undercuts are tolerable; closes below are not |
| 464–476.5 | −8.3 to −10.7 | Jul 29 low 465.00; 200-day ≈ 470.5 on Oct 21 and ≈ 475 on Oct 28 if price stays flat near 500–510 [calc]; VWAP anchored at the start of 2026, 476.52. The bear target |

## 4. Base rates and analogs

**Supporting:** sections 2.2–2.3.

**Not supporting:**
- **Fast legs are deeper, not shallower.** The 16 SOX legs that reached −11.9% within 7 sessions had a median depth of −17.5% (≈486), and only 50% ended shallower than −17%. 12 of the 16 date from 1997–2000.
- **Conditioning on the overnight depth** (−13.4% from the swing high; SOX, n=44) shifts the median to **−18.3% (≈481.6)**, and only 43% ended shallower than −17%.
- **Fast-crash analog** (SOX 7-session return of −10% or worse while above a rising 200-day; 1995–2026, n=24):
  - median further 40-day adverse move −9.25% (≈471);
  - only 21% marked the low on the signal day;
  - median 15 sessions to the low.
  - Since 2009 (n=9) the median is −5.0%, but 4 of 9 fell another 11% or more: 2020, 2022, Jul 2024 and Jul 2026.
- **The distribution is bimodal.** Of the 10 SOXX legs, 7 ended at depths that map to 482–519 from 589.51, and 3 at depths that map to 395–443: Jul 2024, Feb–Apr 2025 and Jun–Jul 2026.
- **The record-high framing is hostile.** SOXX is −20.7% from its record. Given −20%, the only prior case went to −41.7%; given −15% over 5 years, the median was −29.2% (n=4) [DB].
- **The 2018 midterm analog:** SOX was −13.3% by Oct 14, then −26% at the Dec 24 low [SP].

## 5. Strongest counter-evidence

1. **The breakout failed outright.**
   - SOXX had seven straight down closes.
   - It sits below the VWAPs anchored at the July low and at Mar 30, so the average buyer since July is underwater.
   - The weekly close made a lower high: 588.9 vs 639.5 [SL].
2. **Good news is being sold.**
   - ASML fell −3.9% on a beat-and-raise, and MU is −16.7% since its record guide [CAT].
   - The Oct 9 clarification bounce faded [O8].
   - The question is financing (CoreWeave at about 15% yield to maturity, the IMF GFSR, Hock Tan's "capital" remark), and an earnings beat does not answer it.
3. **There is no capitulation.**
   - SOXX volume was 1.52x its 50-day average, against 2.88x on Jun 5 and 1.79x on Jul 29 [SL]. VIX/VIX3M is 0.898.
   - Retail added +$711.9M to SOXL on Oct 13 (one vendor), and BofA's survey names long semis the most crowded trade [SP].
4. **Memory's rate of change is turning.** TrendForce says "price increases are slowing," and CXMT is coming. Memory led the June–July crash [SL].
5. **For most semis this is already a bear market.** 76% of the basket is more than 20% off its highs, and the median name is −30.8% [SL].
6. **Macro offers no cushion.**
   - The Fed is hiking. The 10-year is at 5.19% and the real yield at 2.88% [MR].
   - Oct 28 hike odds are about 35% (single source).
   - MV's median S&P 500 low (≈7,480) falls in its deeper bucket, which implies QQQ −10% to −13%, or roughly **SOXX 420–455** at a 2.04 beta.
7. **Rotation is defensive.** Over one week XLE rose +6.7%, XLP +5.3% and XLV +3.1% [SL].

## 6. What would prove me wrong (closing basis)

**Price**
- **SOXX below 497.40:** the shape is wrong, because the post-July higher low breaks.
- **Two closes below 491.65, or any close below 485.71:** the depth is wrong.
- **SMH below 531.97, or SOX below 11,040:** the same breaks on the sister measures.
- **Cross-layer:** QQQ below 711.88, or the S&P 500 below 7,505 (MV's hinge).

**Time**
- A new SOXX closing low after **Oct 30**, or no close above **528.26 by Nov 4**.

**Events**
- **Oct 15, TSMC:** a Q4 guide flat or down quarter on quarter, a gross-margin guide below ~63–64%, a capex cut, or "digestion" language [CAT]. A beat that still closes SOXX red on Oct 15–16 below 510 would be a third good-news sale and would badly weaken the case.
- **Oct 21:** LRCX guides the December quarter below the $8.10bn September-quarter midpoint; TXN guides Q4 weak; META cuts capex, or raises it and is sold hard.
- **Oct 28:** the Fed hikes and signals a follow-up; MSFT or GOOGL talk of moderating 2027 capex; KLAC gives a second cautious guide.
- **Nov 3 and Nov 4:** AMD cuts its data-center GPU guide; ARM disappoints.
- **About Nov 10:** CoreWeave signals funding stress, or its 2032 bonds fall below ~75c [O8].

**Stress gauges**
- The 10-year closes above 5.31%.
- HY OAS goes above 3.46%.
- VIX/VIX3M stays above 1.0 for two or more sessions.
- The semis basket falls to 5% or less above its 50-day *with* SOXX below 497: a July-style washout, which means deeper.

**What would confirm the case**
- A close above 528–530 by Oct 23, then above 545.9.
- Semis-basket breadth back above 50%.
- SOXX/SPY back above its 50-day.
- A close above 559.12 would void the failed breakout.
