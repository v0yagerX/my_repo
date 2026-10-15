# Layer 2, broad tech (QQQ / XLK): the shallow-pullback case

*Advocate brief, written about 03:55 UTC Oct 15 (11:55 pm ET Oct 14). Data runs through the Oct 14 close.*

**Source tags**
- **[DB]**: DATA_BRIEF.md, betas_ratios.txt, analog_forward_returns.txt, base_rates.json.
- **[MV]**: analysis/market_verdict.md.
- **[CAT] / [MR] / [SP] / [SL] / [O8]**: research/catalysts.md, macro_rates.md, sentiment_positioning.md, semis_leadership.md, oct8_narrative.md.
- **[calc]**: my scripts in `scratchpad/tb_scripts/`:
  - `tech_base.py`, `tech_postrec.py`, `tech_timing.py`: base rates from ^NDX daily 1985– (`analysis/sent/long/_NDX.csv`), plus QQQ (1999–) and XLK (1998–) histories I fetched from Yahoo into `dl_techbull/`. Their Oct 14 closes match DB.
  - `tech_more.py`: regressions, mega-caps and S&P IT breadth.

**Live checks**
- **IBKR real-time, about 03:23–03:46 UTC:** QQQ 720.81 (−1.12%), XLK 188.12 (−1.21%), SOXX 510.04 (−1.81%), NVDA 218.36 (−1.33%). These are thin overnight prints.
- **TSMC Q3** was **not out** when I searched at 03:51 UTC (previews only). It is not used here.

**Upper layer:** I argue *consistently with* [MV] (Shallow 40 / Deeper 38 / Trend break 22). My zone is what [MV]'s shallow scenario implies for tech.

## 1. Thesis

1. Tech is pulling back because semis are being de-rated, and the tech uptrend itself is intact. A 126-day regression attributes all of QQQ's Oct 6–14 drop to SMH, while the six non-semis mega-caps are flat. The pullback also began only 10 sessions after QQQ/NDX recovered from an 11.3% correction, and historically pullbacks in that position are usually shallow and rarely exceed −12%.
2. **Projected closing low:**

   | | Zone | Central | From the record close | From the Oct 14 close |
   |---|---|---|---|---|
   | **QQQ** | **700–716** | ~709 | **−5.7% to −7.9%** (759.66) | −1.8% to −4.0% (728.95) |
   | **XLK** | **180.5–187** | ~184 | **−7.4% to −10.6%** (202.00) | −1.8% to −5.2% (190.43) |

3. **Timing and odds:** the low most likely prints **Oct 16–23**, with **Oct 28–29** as the fallback window. I put **about 40%** on QQQ's closing low holding 700, and **about 85%** on it holding 668.5 (−12%).

## 2. Evidence, ranked by weight

**1. The damage is in semis, not tech [calc].**
- **QQQ:** QQQ ≈ 0.39·SMH + 0.32·MEGA6 (R² 0.95), where MEGA6 is an equal-weight AAPL/MSFT/GOOGL/AMZN/META/TSLA basket. Over Oct 7–14, QQQ fell −4.09%. The SMH term accounts for −4.31% and the MEGA6 term for −0.03%.
- **XLK:** XLK ≈ 0.57·SMH + 0.20·MEGA6 (R² 0.90). Actual −5.83%; SMH term −6.41%.
- **The mega-caps since Oct 6:** MEGA6 −0.13%. AAPL is at its 52-week closing high, MSFT is −1.8% from its high and +5.9% above its 50-day, and META is +13.5% above its 50-day.
- **IT breadth outside semis held up.**
  - S&P IT members excluding semis: 52.7% above their 50-day and 69.1% above their 200-day. On Oct 6 the figures were 69.1% and 74.5%.
  - Semis: 20% above their 50-day.
- **Implication:**
  - With MEGA6 flat, even the semis bear advocate's SMH zone of 504–532 maps to QQQ ≈ 698–712 and XLK ≈ 179–184.
  - The tech floor therefore depends on the mega-caps, and they report next.

**2. Pullbacks that start soon after a correction recovers are usually shallow [calc].**

The NDX's last ≥10% episode (Jun 2 – Jul 29, −11.3%) recovered on Sep 22, and the current peak came 10 sessions later. I measured ATH-to-ATH episodes that reached −4% within 10 sessions of a record set ≤60 sessions after a ≥10% correction recovered:

| Index (period) | n | Median final depth | Share shallower than −8% / −10% / −12% |
|---|---|---|---|
| NDX (1985–) | 46 | **−6.1%** | 61 / 70 / **89%** |
| NDX (1999–) | 22 | −10.2% | 41 / 50 / 86% |
| QQQ (1999–) | 21 | −7.5% | 52 / 57 / **95%** |
| QQQ (2003–) | 12 | −5.6% | 67 / 67 / 100% |
| NDX, no recent recovery (1985–) | 28 | −12.45% | 36 / 39 / 46% |

- **Timing:** the median trough came **3 sessions** after the first −4% close (IQR 0–14) [calc]. QQQ's first −4% close was Oct 14.

**3. My zone is what [MV]'s shallow case implies.** The bracketed values are QQQ at a beta of 1.43–1.62 and XLK at a beta of 1.75–2.0 [DB].

| S&P 500 low | QQQ | XLK |
|---|---|---|
| 7,620 | 714–716 | 185.5–186.2 |
| 7,540 | 702–705 | 181.6–182.7 |
| 7,505 ([MV] hinge) | 696–700 | 180–181 |

- Using [MV]'s regression (S&P ≈ 0.40·RSP + 0.41·QQQ), QQQ at 700 with RSP at 208.02 implies an S&P of about **7,534**. That is still inside [MV]'s shallow case.

**4. The trend and relative strength are intact [DB].**
- **Moving averages:** QQQ is above its 50-day (726.66), 100-day and 200-day (+8.2%). Its 50-day and 200-day are rising, at +2.36% and +1.86% over 20 days. XLK is +14.0% above its 200-day.
- **Relative ratios:**
  - QQQ/SPY 0.9472, versus a 50-day of 0.9454 and a 200-day of 0.9292. It was 0.9346 on Sep 16.
  - XLK/SPY 0.2474, versus a 50-day of 0.2471 and a 200-day of 0.2298.
- **Sector breadth:** IT has the third-highest share of members above their 200-day of any sector, at 66.7%.

**5. The catalyst reaction function rewards capex that comes with revenue [CAT][calc].**
- **In July:** QQQ's low close of 661.73 came on Jul 29, the FOMC and META night. QQQ then rose +3.3% on Jul 30 as MSFT rose +15.5% (Azure guided to 45%), and it was +9.4% ten sessions later.
- **Mega-cap moves, Jul 28 → Jul 31:** MSFT +18.1%, AMZN +17.6%.
- **This time the mega-caps go in strong:** META reports Oct 21; MSFT and GOOGL Oct 28 (all CONFIRMED); AMZN about Oct 29 (ESTIMATE).

**6. Supporting signals.**
- **Analogs [DB]:** QQQ analogs (n=17) had a 10-day median return of +1.2%, positive 71% of the time.
  - The median worst drawdown along the way was −2.3%, which maps to about 712. The 25th-percentile drawdown, −3.8%, maps to about 701.
  - For XLK, the median 20-day worst drawdown, −4.8%, maps to about 181.3.
- **Rates were not the driver [MR]:** the 10-year fell 12 bp from Oct 5 to Oct 14 while QQQ fell 3.6%.
- **Seasonality [SP]:** in midterm years, NDX from Oct 14 → Oct 31 averaged +5.0%, and Oct 14 → Dec 31 had a median of +5.1%, up 90% of the time (n=10).
- **Positioning [SP]:**
  - US fundamental long/short net leverage is at the 2nd percentile (SINGLE-SOURCE).
  - Money-market funds took in +$166bn in one week (SINGLE-SOURCE).

## 3. Key levels (closing basis)

**QQQ** (% vs the 728.95 close / vs the 759.66 record close) [DB]

| Level | Type | % | Why it matters |
|---|---|---|---|
| 744.2–746.45 | Resistance | +2.2 / +2.4 | Oct 13 gap; VWAP anchored at the Oct 6 high. Reclaiming it ends the pullback |
| 731.23 | Repair | +0.3 / −3.7 | VWAP anchored at the Sep start. The first close above it is the first bottoming signal |
| 726.4–728.7 | Lost overnight | −0.3 / −4.3 | 50-day, 50-day EMA, Oct 14 low |
| 716.6–722 | Support | −1.0 to −1.7 / −5.0 to −5.7 | 6-month volume point of control (POC) 719.62 (11.3% of volume); 3-month POC 718.73 (14.0%); VWAP anchored at the Jul low 721.12; 100-day 720.83; Sep 21 gap fill. Overnight is here |
| **707.5–713.3** | **Core** | −2.1 to −2.9 / −6.1 to −6.9 | Sep 17 gap; 50% Fibonacci 712.0; volume nodes 713.6 / 710.5 / 707.5 |
| **697.1–700.1** | **Floor** | −4.0 to −4.4 / −7.9 to −8.2 | 61.8% Fibonacci 700.0; Sep 16 low 700.0; Aug–Sep closing low 700.07; VWAP anchored at Mar 30 697.13 |
| 683.7 / 673.9 / 661.1 | Deeper | −6.2 / −7.6 / −9.3 | −10% from the record; 200-day; Jul 29 low |

**XLK** (% vs the 190.43 close / vs the 202.00 record close)

| Level | Type | % | Why it matters |
|---|---|---|---|
| 192.4 / 197.08 | Repair | +1.0 / +3.5 | Sep-start VWAP; Oct 6 high VWAP |
| 187.1–188.0 | Support | −1.3 to −1.7 / −6.9 to −7.4 | VWAP anchored at the Jul low; volume node (8.6%). Overnight is here |
| **183.75–186.7** | **Core** | −1.9 to −3.5 / −7.6 to −9.0 | Sep 17 gap; 100-day 186.53; 50% Fibonacci 184.86; volume POC 183.75 |
| **180.5–182.1** | **Floor** | −4.4 to −5.2 / −9.9 to −10.6 | Sep 14 low; 61.8% Fibonacci 180.51 |
| 178.04 | Invalidation | −6.5 / −11.9 | Aug–Sep closing low |

## 4. Base rates and analogs: for and against

**For**
- **Post-recovery set:** the table in §2.2.
- **All NDX records that reached −4% within 10 sessions (n=74):** median −7.7%; 51% ended shallower than −8% and 73% shallower than −12% [calc].
- **The QQQ 10-day analog** and **NDX midterm seasonality** above.

**Against** (honestly, these are heavy)
- **The overnight print is already −5.1%.** If QQQ closes ≤721.7 (−5%), the relevant base rates get much worse:
  - post-recovery QQQ (n=13): median −10.7%; only 23% ended shallower than −8%, though 92% were shallower than −12%;
  - all NDX (n=47): median −10.9% [calc].
- **[DB], 3-year history:**
  - QQQ given −5%: n=6, median −11.75%.
  - XLK given −5%: n=7, median −16%.
- **XLK post-recovery (n=13):** median −11.7%; 38% ended shallower than −10% [calc].
- **QQQ 40-day analog:** median −0.6%, positive only 40% of the time. The XLK 10-day analog is positive only 43% of the time [DB].
- **2018, a tightening midterm year:** NDX fell −23% into Dec 24 [SP].
- **Samples are small,** and the post-recovery sets lean on the 1990s and include 2000 (−83%).

## 5. The strongest counter-evidence

1. **The mega-cap leg is two-sided.**
   - In July, GOOGL fell −7.1% and META −8.0% on capex [CAT].
   - Oct 28 stacks the FOMC (about 35% hike odds, SINGLE-SOURCE) on the same night as MSFT and GOOGL.
   - A linear regression understates how closely stocks move together in a tail.
2. **There is no capitulation.**
   - VIX 16.87; VIX/VIX3M 0.898 [DB].
   - QQQ implied vol is at the 8th percentile, and QQQ option put/call is 0.84 against a 1.10 average [SP].
   - BofA FMS: a net 37% overweight in tech, the highest since Aug 2020 [SP].
3. **The relative highs are in June.**
   - QQQ/SPY and XLK/SPY peaked Jun 18 and Jun 2, and each sits only 0.2% / 0.1% above its 50-day [DB].
   - The rotation is defensive: XLE +6.7%, XLP +5.3%, XLV +3.1% over one week [SL].
4. **The financing narrative can reach the spenders.**
   - CoreWeave bonds yield about 15%; ORCL fell −8.8% [O8].
   - HY OAS is at the 91st percentile of its 1-year range and CCC spreads are at a 3-year high [MR].
   - The 10-year real yield is 2.88% [MR].

## 6. What would prove me wrong (closing basis)

- **QQQ below 697.1** on any close kills the shallow case. **Below 683.7** (−10%) confirms the deeper case.
- **XLK below 178.04.**
- **Timing failure:** QQQ sets a new closing low after **Oct 29**. That falsifies "soon" even if 697 holds.
- **The mega-cap test fails:** two of META (Oct 22 session), MSFT and GOOGL (Oct 29) and AMZN (about Oct 30) close ≥5% lower the day after reporting. Alternatively, MEGA6 closes more than 5% below its Oct 14 level.
- **Semis:** SMH closes below **503.6** (Jul 29 low). With MEGA6 flat, that alone maps QQQ to about 698.
- **Relative trend:** QQQ/SPY closes below **0.9454** and XLK/SPY below **0.2471** for 3 or more sessions.
- **Market and macro:**
  - S&P 500 below 7,505 with RSP below 207.16 [MV];
  - an Oct 28 hike with a signalled follow-up;
  - the 10-year above 5.31%;
  - HY OAS above 3.46%;
  - VIX/VIX3M above 1.0 for 2 sessions.
- **Confirmation for me:** QQQ closes above 731.23 by Oct 23, then above 746.45 by mid-November.

**UNVERIFIED or caveated**
- **Single-source figures:** the hike odds, hedge-fund leverage, and money-market flows.
- **AMZN date:** an estimate.
- **Overnight quotes:** indicative only.
- **Regressions:** linear and estimated over 126 days.
- **TSMC:** results were pending when this was written.
