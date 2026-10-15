# NVDA layer: the deeper-correction / trend-change case (bear advocate)

*Written ~03:55 UTC Oct 15 (11:55 pm ET Oct 14). Data through the Oct 14 close. **TSMC Q3 was NOT out** at ~03:50 UTC: WebSearch returned only previews ([Tikr](https://www.tikr.com/blog/tsmcs-q3-earnings-preview-65-profit-growth-but-net-margin-seen-slipping-to-50), [Crypto Briefing](https://cryptobriefing.com/tsmc-record-profit-sixth-quarter-ai/), [Kaohoon](https://www.kaohooninternational.com/?p=592325)). IBKR real-time quotes at 03:45 UTC: NVDA 218.36 (−1.33%), SOXX 510.04 (−1.81%), QQQ 720.80 (−1.12%).*

**Source tags:** [DB] DATA_BRIEF.md and the data files · [CAT] catalysts.md · [O8] oct8_narrative.md / oct8_skeptic.md · [MR] macro_rates.md · [SL] semis_leadership.md · [SP] sentiment_positioning.md · [MV] market_verdict.md · [SB] semis_bear.md · [calc] `scratchpad/scripts/nvda_bear_stats.py` (local Yahoo CSVs, Oct 2021–Oct 2026).

## 1. Thesis

1. **The Oct 6 record was a failed breakout.** NVDA's record (239.24 close, 243.37 intraday) was a three-session break above the May high of 235.74, inside a semis complex that has been making lower highs since June. As the last large holdout, NVDA is more likely to catch down to the sector than to lead it back up.
2. **Projected bottoming zone: 200–209 on a closing basis, centre about 205.** That is −5.6% to −9.6% from the 221.30 close, or −4.3% to −8.4% from the 218.36 overnight print. It implies a total drawdown of **−12.6% to −16.4%** from the record close (−14.1% to −17.8% from the intraday record).
3. **Timing: the low most likely forms Oct 28 – Nov 20, not this week.** That window runs from the FOMC/MSFT/GOOGL/AMZN cluster through earnings week. A trend-change branch (about 30%), triggered by a close below about 200, targets **186–192** (−20% to −22% from the record close), with the low coming *after* the NVDA report (late Nov – Dec).

## 2. Evidence, ranked by weight

**(1) The unbiased base rate already points to the zone [calc; matches DB's 5-year conditional].**
- **The sample:** all NVDA closing drawdowns from a record close that reached −7.5% (Oct 14 is exactly −7.50%), n=14 since 2021.
  - Median final depth **−16.15%** (≈200.6).
  - Only **36%** ended shallower than −10%.
  - 29% closed below the 200-day.
- **Without the 2022 bear market** (n=13): median −14.0% (≈205.7). 8 of 13 went to −13.4% or worse.
- **The 3-year set is milder** (n=11): median −13.4% (≈207.2) [DB].
- **Timing:** the median extra time from first hitting −7.5% to the trough was 13.5 sessions (≈Nov 2–3). In the eight non-bear episodes that went deeper than −10%, it was about **32 sessions (≈Nov 30)**.
- **The overnight print matters, though it is not a close.** Conditioning on −8.7% instead leaves only 25% shallower than −10% (n=12).

**(2) Holdout mechanics favour catching down [DB, SL, calc].**
- **Relative strength has been extreme.** NVDA/SOXX is up 33.7% since Jun 22. NVDA is −7.5% from its high while the median semi is −30.8%.
- **NVDA's beta is asymmetric.**
  - Over 1 year it is 0.56 on SOXX down days and 0.30 on up days.
  - On SOXX days worse than −3%, NVDA's median move ratio is 0.63 (n=40). The current leg runs at exactly that ratio (−7.5% vs −11.9%).
- **The signal history:** days when SOXX was ≥10% off its 60-day high while NVDA was only 4–9% off its own.
  - n=10. NVDA's median 20-day maximum adverse excursion was **−6.2%** (≈207.6), and 6 of 10 saw a further drop of 5% or more.
  - The worst cases: −30.7% (Mar 2022), −17.5% (Aug 2024) and −11.9% (Oct 2023).

**(3) The semis structure is broken, not retesting [SL, SB, DB].**
- **A failed breakout:** SOXX is back inside its Aug–Sep range and below its 528.26 midpoint. Overnight it trades below the Sep 17 gap.
- **A lower high:** the weekly close of 588.9 compares with 639.5 in June.
- **Breadth has collapsed:** 14% of the 29-name basket is above its 50-day, down from 93% on Oct 6. 76% of the names are in bear markets.
- **Good news is being sold:** ASML fell 3.9% on a beat-and-raise, MU is −16.7% after the best guide in its history, and NVDA's own Oct 9 clarification bounce faded.
- **The upper layers already imply NVDA's zone:**
  - [SB]'s SOXX zone of 465–490 maps to NVDA ≈207–213 at the 0.63 ratio, or ≈198–209 if NVDA catches down at beta 1.
  - [MV]'s deeper-path QQQ of 660–685 maps to ≈192–203 at NVDA's 1-year down-day beta to QQQ of 1.41 (DB's full 1-year beta, 1.30, gives ≈194–204).

**(4) NVDA's own balance sheet is the transmission channel [CAT, O8; primary SEC filings].**
- **The debate has shifted from demand to financing.** The questions now are "who pays" and "what is the return":
  - OpenAI's own-basis revenue is about $50bn, not $70bn. The gross-vs-net explanation was in the first reports, and the stock was sold anyway.
  - CoreWeave's bonds yield about 15% (multi-source).
  - Hock Tan called capital the constraint.
- **NVDA carries that risk directly:**
  - Guarantees capped at **$105bn** for capacity tenanted by an OpenAI affiliate (8-K, Aug 17).
  - **$279bn** of supply commitments, up from $119bn (10-Q).
  - AI labs that NVDA backs with its balance sheet will be "roughly a quarter of our business next year" (transcript).
  - One customer was 16% of Q2 revenue.
- An earnings beat does not answer these questions.

**(5) Nothing has capitulated [SP, SL, DB].**
- **NVDA:** Oct 14 volume 1.01× its 50-day average; implied volatility at the 15th percentile (52 weeks); option put/call 0.79 vs a 0.69 average.
- **The index:** VIX/VIX3M is 0.898. Every 2024–26 low printed at 0.96 or above, except the shallow Sep 16 low.
- **Retail and buybacks:** SOXL took in $712M on Oct 13 (one vendor). NVDA's discretionary buyback window is likely closed until after its report (inferred, UNVERIFIED).

**(6) Macro and the calendar offer no put [MR, CAT].**
- The Fed hiked on Sep 16. Oct 28 hike odds were about 35% late on Oct 14 (single source; intraday peak 49–54%). The 10-year real yield is 2.88%, and CCC OAS (12.67%) is at a 3-year high.
- Oct 28 stacks the FOMC decision with MSFT and GOOGL capex. NVDA was lower five sessions after 7 of its last 9 reports.

**(7) NVDA's own chart is damaged [DB, calc].**
- The break above 235.74 reversed within three sessions, and Oct 14 was the first close below the 50-day (223.21) since Sep 15.
- **Volume thins below the POC.** The 3-month profile is thin at 212–218 (2.6–2.8% per $2 bin) under the 218.85 POC, while the 6-month heavy shelf sits at **198–214** (4.4–8.4% per bin; POC 211.02). The air pocket points straight into the shelf.

## 3. Key levels (closes; % vs 221.30 / vs the 218.36 overnight print)

| Level | What sits there | % | Why it matters |
|---|---|---|---|
| 235.74 / 239.24 / 243.37 | May high; record close; intraday record | +6.5 / +8.1 / +10.0 | A close above 235.74 voids this case |
| 229.85–230.48 | Oct 8 FT-reaction pivot; Oct 8 close | +3.9 / +4.1 | Where the narrative broke. Reclaiming it negates the timing |
| 222.99–223.21 | 38.2% Fib; 50-day | +0.8 / +0.9 (+2.1 / +2.2) | Lost on Oct 14 |
| 221.01 / 220 | Jul-low AVWAP; Oct 16 open-interest pin | −0.1 / −0.6 | Expiration gravity until Fri, then released |
| 216.69–218.85 | 50% Fib; Sep 17 gap 216.76–217.15; 3-month POC | −2.1 to −1.1 (−0.8 to +0.2) | The bull's line. The overnight print is already testing it |
| 214.45 | 100-day | −3.1 (−1.8) | A close below confirms this case |
| 210.21–211.02 | 61.8% Fib 210.39; Mar-30 AVWAP; 6-month POC; Nov max pain ≈210 (partial chain) | −5.0 to −4.6 | Top of my zone; heavy volume shelf |
| **206.6–208.9** | Aug–Sep closing low 206.64; Aug 24 swing low 207.25; Sep 14 low 208.93 | −6.6 to −5.6 | **Core of the zone** |
| **200.9–205.3** | YTD AVWAP 200.85; 78.6% Fib 201.43; 200-day 202.69, about 204.4 by Oct 28 and 205.3 by Nov 4 on a flat path [calc]; 200-strike put shelf (Nov 53.2k, Dec 64.5k open interest) | −9.2 to −7.2 | **Bottom of the zone.** A close below for two sessions means a trend change |
| 189.66–192 | Jul 29 low 190.01; Apr 14 gap 189.66–190.77; Jun 29 low 189.80 | −14.1 | Trend-change target |

## 4. Base rates and analogs

**Supporting**
- **Conditional drawdowns and holdout signals** (see (1) and (2)) put the low at 200.6–207.6.
- **Even DB's *bullish* analog passes through my zone.**
  - The analog: drawdown of 6–12%, close below the 50-day, close above a rising 200-day (n=23).
  - Its median 20-day maximum adverse excursion is **−8.1% (≈203.4)** and its 40-day is **−9.8% (≈199.6)**. The 25th percentile at 40 days is −13.2% (≈192.1).
  - So a low near 205 is consistent with a positive 40-day return.
- **Options agree** (my approximation: zero drift, continuous monitoring, Nov 13 implied volatility of 33.9%). The chance of *trading* below 205 before Nov 13 is about 43%, and below 200 about 30%. My zone sits inside the market's own 1-sd range for Nov 20 (195.8–250.2) [SP]. **This is not a tail call.**

**Against (honest)**
- **The failed-breakout history is bullish.** There were 5 completed cases where NVDA broke above an old high (≥40 sessions old) and fell back within 5 sessions. 4 of 5 were higher 20 sessions later, and only Nov 2023 saw a maximum adverse excursion beyond −5% (−6.9%) [calc]. The current case is already −4.0% from its Oct 8 failure close.
- **The 2026 holdout signals were mild.** The Aug 5, Aug 21 and Sep 10 signals produced only −2.9% to −4.9% 20-day maximum adverse excursions.
- **The 3-year conditional splits evenly.** 45% of episodes ended shallower than −10%, and the outcomes are bimodal. The shallow bucket, a low at or above 215.3, is a real 35–45% outcome.
- **DB's analog ends higher.** Its 40-day median return is +6.5%, positive 76% of the time.

## 5. The strongest counter-evidence to my case

1. **NVDA is the quality refuge, not the epicentre.** In the June–July semis crash it fell only 8.9% (Jun 22 → Jul 29) while SOXX fell 29% [SL]. Its 3-month down-day beta is just 0.48 to SOXX and 0.93 to QQQ [calc], so a semis-only flush maps to ≈207–213, the top of my zone at best.
2. **The fundamentals are accelerating** (primary sources [CAT]): TSMC Q3 revenue +50.9% y/y; ASML sold out for 2027–28; NVDA's Q3 guide $108bn ±2% and FY28 about +70%, supply-constrained. Morgan Stanley puts it at about 15x FY28 earnings, and the buyback authorization is $235bn.
3. **Positioning is light where it matters** [SP; single source]. US fundamental long/short net exposure is at the 2nd percentile, and money-market funds just took their largest weekly inflow in 6.5 years.
4. **The calendar can also mark a low.** The Jul 29 low formed on the eve of the MSFT print. The same hyperscaler cluster arrives Oct 21–29, and midterm-year seasonality from mid-October is strong (SPX median +6.0% to year-end) [MR].
5. **The last close below the 50-day (Sep 14–15) marked a low** (208.93 intraday, 210.96 close) [calc]. A repeat would still land in my zone, but earlier than my timing.

## 6. What would prove me wrong (closing basis)

**Prices**
- **A close above 230.48 before Oct 28:** the low is likely in at 216–220. My depth and timing are wrong.
- **A close above 235.74:** the case is void.
- **Every close at or above 214.45 (the 100-day) through Oct 30,** after the FOMC/MSFT/GOOGL/AMZN cluster: the shallow case wins.
- **A capitulation reversal above 214:** volume above 1.5–2× the 50-day average and a close in the upper half of the day's range. That would mean an earlier and higher low.
- **SOXX** closes above 530.19 by Oct 21, or above 559.12 at any point [SB].

**Events**

| Date | Event | What would refute me |
|---|---|---|
| Oct 15–16 | TSMC Q3 | Q4 guided up q/q and gross margin at or above ~65%, with TSM, SOXX and NVDA closing green and holding through Friday's expiration |
| Oct 21 / Oct 28 / ~Oct 29 | META / MSFT and GOOGL / AMZN (date estimated) | 2027 capex raised **and** the spender's stock rises, with NVDA closing green |
| Oct 28 | FOMC | A hold without escalation, and the 10-year back below 5.0% |
| ~Nov 10 (estimated) | CoreWeave | Funding secured and its bond yields back toward 12% or below |
| Ongoing | OpenAI round (~$1.4T, single source) | Closes on time, at size |
| Nov 17/18 (UNVERIFIED) | NVDA Q3 | Q4 guided to ≈$120bn or more, gross-margin trough at or above 71%, FY28 ~70% reaffirmed, no new guarantees |

**What confirms the case:** a close below 214.45, then below 210.39; SOXX below 497.40; VIX/VIX3M above 1. Two closes below about 200 (the YTD AVWAP and the 200-day) open the trend-change path to 186–192, and under [MV]'s trend-break conditioning the low would then come *after* the print.

**My odds:** about 55% that NVDA closes at or below 209 before it closes at or above 235.74; about 30% that it closes below 200; about 15% below 190.

## Liquidation reference (reference figure only; not advice)

| Scenario low | Distance to ~$171 (the IBKR level in the user's journal) |
|---|---|
| Zone top 209 / centre 205 / bottom 200 | −18.2% / −16.6% / −14.5% |
| Trend change 192 / 186 | −10.9% / −8.1% |
| Tail: the 2024-style −27% (≈174.6) | −2.1% |

## UNVERIFIED or caveated

- **Single-source:** the 35% Oct 28 hike odds, hedge-fund positioning, SOXL flows and the OpenAI round terms.
- **Not confirmed:** the NVDA earnings date (Nov 17 vs 18), the AMZN and CoreWeave dates, and whether NVDA's buyback window is closed.
- **Data limits:** max pain and open interest come from partial chains; every analog sample is small (n=5–23) and spans only five years; the touch probabilities are my approximations; the 200-day projections assume the stated price paths.
