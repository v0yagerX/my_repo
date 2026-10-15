# NVDA: the shallow-pullback case (advocate brief)

*Written ~03:55 UTC Oct 15 (11:55 pm ET Oct 14). Data through the Oct 14 close (221.30). **TSMC Q3 was NOT out** when I searched at ~03:49 UTC (previews only: [Kaohoon](https://www.kaohooninternational.com/?p=592325), [Crypto Briefing](https://cryptobriefing.com/tsmc-record-profit-sixth-quarter-ai/), [TrendForce](https://www.trendforce.com/news/?p=65041)). My IBKR snapshot calls at ~03:50 UTC returned errors, so for the overnight price I use **218.20** (IBKR, 03:39 UTC, recorded in semis_bear.md). nvda_bear.md recorded 218.36 at 03:45 UTC.*

**Source tags**
- [DB] DATA_BRIEF.md, plus levels.json, technicals.json, base_rates.json, analog_forward_returns.txt and betas_ratios.txt
- [SL] semis_leadership.md · [CAT] catalysts.md · [SP] sentiment_positioning.md · [O8] oct8_narrative.md / oct8_skeptic.md · [MR] macro_rates.md
- [MV] market_verdict.md · [SBu] / [SBe] semis_bull.md / semis_bear.md
- [calc] my scripts `scratchpad/nb_scripts/nvda_bull_stats.py` and `nvda_bull_stats2.py`. They run on Yahoo daily data (NVDA from 1999, SOXX from 2001, QQQ from 1999), fetched 03:45 UTC Oct 15 into `scratchpad/dl_nvdabull/`.

**Upper layers:** [MV] puts the market at Shallow 40% / Deeper 38% / Trend break 22%. No tech or semis verdict existed when I wrote this. My case is effectively [MV]'s shallow bucket.

## 1. Thesis

1. NVDA is pulling back inside an intact uptrend.
   - The lows since July are rising: 190.01, then 207.25, then 208.93.
   - It set a record on Oct 6.
   - Both the 50-day and 200-day averages are rising, and price is 9.2% above the 200-day [DB].
   - It is the low-beta leader of a semis complex that has already done most of the damage.
2. **Projected closing low: 210.4–218.9, core 214.5–217.2.**
   - From the 221.30 close: −1.1% to −4.9%.
   - From the 218.20 overnight print: +0.3% to −3.6%.
   - Total drawdown: −8.5% to −12.1% from the 239.24 record close, or −10.1% to −13.6% from the 243.37 intraday record.
   - Intraday undercuts to about 208.9 are tolerable.
3. **Timing: the closing low prints Oct 15–23,** before the Oct 28 FOMC and MSFT/GOOGL night.
   - **Probability:** about 40% that closes hold 210.4 through NVDA's November print, and about 50% that they hold the 206.64 range floor.
   - That makes this the single most likely zone, but **not** a better-than-even call.

## 2. Evidence, ranked by weight

**(1) The cross-layer arithmetic lands in this zone [calc, DB, SBu, SBe].**
- **NVDA's beta to SOXX does not jump in flushes.**
  - On the 54 days in the past year when SOXX fell more than 2%, NVDA's down-day beta was **0.54** (average-move ratio 0.57) [calc].
  - The current leg has run at 0.63: NVDA −7.5% vs SOXX −11.9% since Oct 6 [DB].
- **Both semis advocates' zones map into mine** at a beta of 0.54:
  - Bull zone, SOXX 490–512 → **NVDA 214.5–219.6**.
  - Bear zone, SOXX 465–490 → **208.8–214.5**.
  - Only a semis trend break, a SOXX close below 465, puts NVDA clearly below 208.
- **QQQ mapping.** At NVDA's 1.41 down-day ratio to QQQ [calc], QQQ at 705–722 maps to **211.0–218.3**. That QQQ band holds:
  - the Sep 17 gap at 711.88–713.32;
  - the 50% retracement at 712.0;
  - the 3-month volume POC at 718.73;
  - the anchored VWAP from the July low at 721.12 [DB].
- **Track record as the holdout:**
  - From Jun 22 to Jul 29, NVDA fell 8.9% while SOXX fell 29.0% [calc].
  - NVDA/SOXX is up 33.7% since Jun 22 [DB].

**(2) The trend structure is intact and price is at a dense support shelf [DB].**
- **Trend:** 50-day slope +4.51% over 20 sessions, 200-day +2.39%; price above the 100-day (+3.19%) and 200-day (+9.18%); RSI 43.9.
- **Shallow retracement:** NVDA has given back only **36%** of the Jul 29 → Oct 6 rally, versus 56% for SOXX [SL].
- **The shelf at 214.5–219 holds five supports:**
  - the 3-month volume POC at 218.85, the largest node with 11.8% of volume;
  - the 50% retracement at 216.69 (214.63 on closes);
  - the unfilled Sep 17 gap at 216.76–217.15;
  - the 100-day at 214.45;
  - a 6-month volume node at 219.45.
- **A second shelf at 210.2–211.0** holds:
  - the anchored VWAP from Mar 30, 210.21;
  - the 61.8% retracement, 210.39;
  - the 6-month volume POC, 211.02;
  - a 3-month node at 210.82 with 9.6% of volume.

**(3) In the AI era, NVDA's pullbacks either stop above about 210 or go much deeper; few end in between [calc, DB].**
- **NVDA swing legs since Oct 2023** that reached −7.5% (n=21; 7.5% zigzag, peak above a rising 200-day):

  | Final depth | Share of legs | Price equivalent |
  |---|---|---|
  | Shallower than −12.1% | **48% (10 of 21)** | ≥210.4 |
  | Between −12.1% and −15.3% | 10% | 202.6–210.4 |
  | Deeper than −15.3% | 43% | <202.6 |

- **Record-close episodes (3 years) that reached −7.5%** (n=11) [DB]:
  - 5 of 11 ended between −7.6% and −9.7%. In price terms, that is 216.0–221.1.
  - Each of those five bottomed within 0–3 sessions of first touching −7.5%. Oct 14 was the first close at −7.5%.
- **The analog setup** (n=23 signals) [DB]: NVDA 6–12% below its record, below the 50-day, above a rising 200-day. The median 40-day return was **+6.5%**, and 76% of signals were positive.

**(4) The damage is in the financing-exposed tail, not in NVDA's own fundamentals [SL, O8, CAT].**
- **Moves since Oct 6:**

  | | Move since Oct 6 |
  |---|---|
  | CRWV | −28.3% |
  | Optics (median) | −19.9% |
  | NVDA | −7.5% |

- **No NVDA-specific negatives** [O8]: no downgrades or insider sales; consensus target about $320–329 (secondary); Morgan Stanley's top pick at $300, about 15x FY28 earnings.
- **The OpenAI damage has already round-tripped.** From the Sep 28 close to the Oct 8 close NVDA was +0.71%, so the Oct 8 drop erased the gain that followed the $70bn headline [O8].
- **Hard data still rising** [CAT]: TSMC Q3 revenue +50.9% y/y (6-Ks); ASML says 2027–28 supply will not meet demand; NVDA guides Q3 to $108bn ±2% and FY28 to about +70%.

**(5) Options and seasonality support an October low (lower weight) [SP, CAT].**
- IV is 33.2% (15th percentile, 1-year) with a 25-delta risk reversal of only −3.8 vols.
- Oct 16 open interest clusters at the **220** strike (99.2k calls, 64.6k puts), and the Oct 23 straddle range (211.2–231.4) brackets my zone.
- Midterm-year S&P 500 Q4 lows came in October in 12 of 18 years, often Oct 15–23.

## 3. Key levels (closing basis; % vs 221.30 / vs 218.20)

| Level | % | Why it matters |
|---|---|---|
| 239.24 / 243.37 | +8.1 / +10.0 | Record close / intraday record |
| 235.74 | +6.5 / +8.0 | May high; the failed breakout. A close above revives it |
| 229.85–230.48 | +3.9 to +4.1 / +5.3 to +5.6 | Oct 8 pivot where the narrative broke; anchored VWAP from the Oct 6 high 230.98. Reclaiming it confirms the low |
| 222.99–223.21 | +0.8 / +2.3 | 38.2% retracement; 50-day. The first repair close |
| 221.0 | −0.1 / +1.3 | Anchored VWAP from the July low. Oct 16 pin at 220 |
| **214.45–218.85** | −1.1 to −3.1 / +0.3 to −1.7 | **Core shelf** (section 2, item 2) |
| **210.2–211.0** | −4.6 to −5.0 / −3.3 to −3.7 | **Floor of my zone**; Sep 14 close 210.96 |
| 206.64 / 208.93 | −6.6 / −5.6 (vs close) | Aug–Sep closing range low; Sep 14 intraday higher low. **The structural hinge** |
| 202.69 / 200.85 | −8.4 / −9.2 | 200-day; YTD anchored VWAP. The bear's zone |
| 190.01 | −14.1 / −12.9 | Jul 29 low; trend-change line |

**Liquidation reference (~$171):**
- 18.7% below the 210.4 floor of my zone, and 20.3–21.3% below the 214.5–217.2 core.
- 22.7% below the 221.30 close, and 21.6% below the 218.20 overnight print.

## 4. Base rates: for and against

**Supporting:** items 1 and 3 above, plus the SOXX analog (n=17): 40-day median +10.4%, positive 86% of the time [DB].

**Against (stated plainly):**
- **Longer samples are deeper.**
  - Record-close episodes since 2016 that reached −7.5% (n=31): median **−14.0%** (≈205.7). Only 23% ended shallower than −11.4%, and 29% shallower than −12.5% [calc].
  - The 5-year set that includes 2022 (n=14): median −16.15% [DB].
- **The overnight depth makes it worse.** Swing legs since 2015 that reached −8.7% (n=58) had a median of −13.75%. Only 29% ended shallower than −12% [calc].
- **The analog's path is deep even when it ends well.** Its median 10-day maximum adverse excursion is −5.8% (≈208.5) and its 20-day figure −8.1% (≈203.4) [DB].
- **Holdouts partly catch down.**
  - Signal: SOXX 15% or more off its 1-year high while NVDA is 5–10% off its own and above a rising 200-day. n=15 since 2003 (de-clustered).
  - NVDA's median 40-day return was +3.2%, positive 67% of the time.
  - But its median 60-day maximum drawdown from its high was **−17.6%**, and 53% went past −15% [calc].
  - Positive NVDA/SOXX 20-day relative strength at the −7.5% hit came with *deeper* outcomes (n=18, median −16.15%). That ratio is flat today [calc, DB].
- **Earnings history:** 7 of NVDA's last 9 prints were lower five sessions later [CAT].
- **Options:** the risk-neutral chance of a Nov 20 close below 210 is about 35% [SP]. A reflection-principle approximation (mine, UNVERIFIED) implies roughly a 60–70% chance of at least *trading* below 210 by then. That is consistent with my ~40% for closes holding 210.4.

**Net:** a ~40% probability is honest. This is a plurality case, not a majority case.

## 5. Strongest counter-evidence

1. **This is a failed breakout in a broken group.**
   - The move above 235.74 reversed within three sessions.
   - SOXX made a lower high and is −20.7% from its June high. 76% of the 29-name semis basket is more than 20% off its highs [SL].
2. **Good news is being sold.** ASML fell 3.9% on a beat-and-raise, MU is −16.7% after a record guide, and the Oct 9 clarification bounce failed [CAT, O8].
3. **The credit mechanism is NVDA's own.**
   - NVDA has guaranteed up to **$105bn** of leases for an OpenAI affiliate, from 2028.
   - Its supply commitments are **$279bn**.
   - AI labs it backs with its balance sheet will be "roughly a quarter" of next year's business.
   - One customer was 16% of Q2 revenue.
   - CoreWeave bonds yield about 15% [CAT, O8].
4. **There has been no capitulation.** NVDA volume was 1.01x its 50-day average [SL], VIX/VIX3M is 0.898 [DB], retail is still adding leveraged semis exposure, and long semis is the most crowded trade [SP].
5. **Macro offers no cushion.** The Fed is hiking, with odds of an Oct 28 hike near 35% (single source). The 10-year real yield is about 2.9% [MR]. [MV]'s median S&P 500 low (≈7,480) implies QQQ at about 660–685, which maps to **NVDA about 192–203**.

## 6. What would prove me wrong (closing basis)

**Price**
- **A close below 210.4** means the zone is wrong.
- **Any close below 206.64** means the thesis is wrong: the higher-low structure breaks, and the bear's 200–203 becomes the base case.
- **A new closing low after Oct 23** means the timing is wrong.
- **No close above 223.21 by Oct 30**, or none above 230.48 by Nov 13, means there is no recovery.
- **Catch-down underway:** NVDA's daily move ratio to SOXX above 0.8 for three or more sessions, or NVDA/SOXX falling more than 5% in a week from 0.4261.

**Cross-layer**
- A SOXX close below 465.
- A QQQ close below 705.
- An S&P 500 close below 7,505 ([MV]'s hinge).

**Events**
- **Oct 15, TSMC:** a flat or down Q4 guide, or "digestion" language. Or a beat with NVDA still closing below 216.69 on Oct 15–16.
- **Oct 21, META:** a capex cut.
- **Oct 28:** a Fed hike with a signalled follow-up, plus MSFT or GOOGL moderating 2027 capex.
- **About Nov 10 (estimated date), CoreWeave:** funding stress, or its 2032 bonds below 75c.
- **Any time:** a new NVDA credit-support commitment, or a delayed or down-round OpenAI raise.
- **Nov 17 or 18 (date UNVERIFIED), NVDA results:** a Q4 guide at or below $115bn, a gross-margin trough below 71%, or a hedged FY28 outlook.

**Stress gauges**
- VIX/VIX3M above 1 for two or more sessions.
- HY OAS above 3.46%.
- The 10-year above 5.31%.

**What would confirm the case**
- Closes hold 214.45 through Oct 16 expiration.
- A close above 223.21 by Oct 23.
- MSFT or GOOGL raise capex *and* their stocks rise.
- A close above 230.48 before the print.
