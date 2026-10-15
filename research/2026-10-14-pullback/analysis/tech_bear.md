# Broader tech (QQQ / XLK): the deeper-correction / trend-change case

*Bear advocate, written ~04:00 UTC Oct 15 (midnight ET). Data through the Oct 14 close.*
- **TSMC Q3:** **not out** when I checked at 03:46 and 03:55 UTC. WebSearch returned previews only ([Tikr](https://www.tikr.com/blog/tsmcs-q3-earnings-preview-65-profit-growth-but-net-margin-seen-slipping-to-50), [investingLive](https://investinglive.com/stocks/preview-tsmc-tipped-for-sixth-straight-record-quarter-with-profit-seen-up-65-on-ai-demand/)). Nothing below uses it.
- **IBKR real-time, 03:46 UTC:** QQQ 720.81 (−1.12%). QQQ implied vol 17.0% (8th percentile of 52 weeks). Option-volume put/call 0.84 vs a 1.10 average.

**Source tags**
- **[DB]** DATA_BRIEF.md and the data files.
- **[MV]** market_verdict.md · **[MR]** macro_rates.md · **[CAT]** catalysts.md · **[SL]** semis_leadership.md · **[SP]** sentiment_positioning.md.
- **[calc]** my scripts `scratchpad/scripts/tech_bear1–4.py`. Inputs: ^NDX 1985–2026 (`analysis/sent/long`), XLK 1998–2026 (Yahoo chart API, fetched Oct 15 to `dl_techbear/`), and the 75 S&P 500 IT members in `data/spx`.
- **Episodes:** record close to recovery, close basis, current one excluded; this avoids the base_rates.py selection bias [MV] found.

---

## 1. Thesis

1. **The Oct 6 tech record was a narrow, unconfirmed high, and this decline looks like July 2024 (−13.6%) and June–July 2026 (−11.3%), not the −6% to −7% dips.** The signature: semis already broken, rotation into defensives, cheap hedges, no volatility capitulation.
2. **Bottoming zone (closing basis).**
   - **QQQ 662–690, core 675–688.** That is −5.3% to −9.2% from the 728.95 close, and −9.2% to −12.9% from the 759.66 record close.
   - **XLK 170–178, core 173–177.** That is −6.5% to −10.7% from 190.43, and −11.9% to −15.8% from the 202.00 record.
3. **Timing and odds.**
   - **The low most likely forms Oct 28 – Nov 13** (FOMC plus MSFT/GOOGL on Oct 28, through CPI on Nov 10). It can slip to the Nov 20 options expiration.
   - **My odds:**
     - QQQ closes below 700 before it makes a new record close: about 60%.
     - It reaches 690: about 50%.
     - It closes below the Jul 29 close of 661.73 (trend change): about 25%. That path leads to QQQ 635–646 and XLK 160–166, with the low in December.

## 2. Evidence, ranked by weight

**(1) Base rates conditioned on today's state point to about −11% for QQQ and about −16% for XLK** [calc, DB]

| Reference set | n | Median final drawdown | Share reaching −10% |
|---|---|---|---|
| NDX, given −4.04% (today's close), 1985– | 80 | −7.7% | 44% |
| NDX, given −5% (QQQ is −5.1% overnight; not a close) | 60 | −10.7% | 58% |
| **NDX −4% with SOX ≥10% below its 20-day high** (today −11.6%) | 8 | **−11.2%** | **75%** (88% reach −8%) |
| XLK, given −5.73%, 1998– | 25 | −11.7% | 64% |
| **XLK −5.73% with the same SOX filter** | 9 | **−16.0%** | **78%** (56% reach −15%) |
| QQQ / XLK, given −5%, since Oct 2023 [DB] | 6 / 7 | −11.75% / −16.0% | 67% / 57% |

- **Timing:** in the SOX-filtered NDX set, the median trough came 19 sessions after the threshold was hit. From Oct 14 that lands on **Nov 10**.
- **Outliers:** dropping 2000 from that set leaves a median of −11.1%.

**(2) The recent "rotation" episodes still took tech down 11–14%** [calc]

| Episode | QQQ at session 6 | RSP at session 6 | Final low |
|---|---|---|---|
| Jul 2024 | −4.7% | **+2.7%** | **−13.6%** (session 20) |
| Jun–Jul 2026 | −7.0% | −1.7% | **−11.3%** (session 39), while the S&P 500 held −4.5% [MV] |
| Oct 2025 | −3.8% | −1.2% | −12.2% |
| **Now** | **−4.0%** | **−0.1%** | — |

- Money moving into equal weight cushions the S&P 500. It has not cushioned tech.

**(3) The record was unconfirmed and the leadership is narrow** [calc, DB]
- **Relative strength did not confirm the high:**
  - At the Oct 6 record, QQQ/SPY was 1.7% *below* its Jun 18 relative high. It is now 4.5% below.
  - XLK/SPY was 0.6% below its Jun 2 relative high, and is now 5.2% below.
- **A few mega-caps carried the Aug–Oct rally:**
  - QQQE/QQQ (equal weight vs cap weight) was 7.3% below its Jul 29 high on Oct 6, and it is below its 50-day and 200-day averages.
  - Since Jul 29: MSFT +36.7%, META +25.9%, AMD +32.9%.
- **XLK's −5.7% hides the typical tech stock:**
  - The median S&P 500 IT member is **23.8% below its 1-year closing high**, and 57% of members are 20% or more below theirs.
  - The share of IT members above their 50-day average fell from 76.0% (Oct 6) to **44.0%** (Oct 14).
  - Only 29% of IT members rose on Oct 8, and 17% on Oct 14.
- **Distribution days** (down ≥0.2% on higher volume): QQQ had 7 in 25 sessions, four in the last five (Oct 8, 12, 13, 14). Volume on Oct 8 and 14 was 1.45x and 1.58x the 50-day average.

**(4) The mega-cap platforms have not been tested yet, and they report from their highs** [calc, CAT]
- **Where they stand:** AAPL is at a record. MSFT is −1.8% from its high and META −5.2%.
- **Where QQQ's −4% came from:** semis and AI infrastructure. Since Oct 6: AMD −12.1%, MU −12.6%, AVGO −7.9%, NVDA −7.5%.
- **July ended from a washed-out tape** (QQQ −11.3%): MSFT and AMZN rose about 15% on revenue acceleration, while GOOGL (−7.1%) and META (−8.0%) were punished for capex without revenue.
- **This time they start high:** MSFT is 18.3% and META 36.8% above their post-July closes. My judgment: the bar is higher, and META (Oct 21), MSFT/GOOGL (Oct 28) and AMZN (~Oct 29, ESTIMATED) put the untested second leg inside my window.
- **The debate has moved to financing and returns, and the hyperscalers are the borrowers:** CoreWeave bonds at about 15% yield, Oracle −58% from its high and cut to BBB− (single-source in MR), the IMF on circular deals (secondary). Maia 300 moves value away from the semis weight in QQQ/XLK [O8].

**(5) Macro removes the safety net, and the market verdict's own mapping lands in my zone** [MR, MV]
- **Rates:** the Fed hiked Sep 16; Oct 28 hike odds about 35% (single source); 10-year 5.19%, real 2.88% (2.95% peak, highest since 2008). The stock–yield correlation turned +0.47 in Q4 (9 sessions), a growth-scare tell: falling yields have not helped tech.
- **The market verdict** puts 60% on an S&P 500 close below 7,505 and says that "most likely means QQQ is already down 10–13%" (660–684). Its median S&P low of about 7,480, at the 1.43–1.62 beta [DB], implies QQQ about 695 before any fresh tech-specific damage.

**(6) No capitulation, cheap hedges, crowded positioning** [SP, IBKR, DB]
- **Volatility:** VIX 16.87, VIX/VIX3M 0.898, against 20.66 and 0.961 at the Jul 29 NDX low. QQQ implied vol is at the 8th percentile and its put/call is below average.
- **Positioning:** BofA October survey net 37% overweight tech, highest since Aug 2020 (CONFIRMED); SOXL +$712M on Oct 13 (one vendor).
- **Analog forward returns [DB]:** QQQ 40-day median −0.6% (40% positive); XLK 10-day median −0.4% (43% positive).

## 3. Key levels on my path (closing basis; % vs the Oct 14 close)

**QQQ** [DB, calc]

| Level | % | Why it matters |
|---|---|---|
| 744.2–746.45 | +2.1 / +2.4 | Oct 13 gap; VWAP anchored at the Oct 6 high. Reclaiming it kills this case |
| 719.6–727.8 | −0.2 to −1.3 | 50-day 726.66; Sep 21 gap 721.73–727.81; 38.2% Fib 724.0; Jul-low anchored VWAP 721.12; 100-day 720.83; 6-month volume point of control 719.62. **The 720.81 overnight print is already below the gap** |
| 711.9–713.3 | −2.3 | Sep 17 gap; 50% Fib 712.0 |
| **697–705** | −3.3 to −4.4 | **The hinge.** Sep 16 low 700.0 (close 704.72), Jul 8 low 700.91, Aug 24 low 702.7, 61.8% Fib 700.0, Mar-30 anchored VWAP 697.13. A close below breaks the 3-month range |
| **680–690** | −5.3 to −6.7 | **Top of my core zone.** Aug–Sep intraday low 685.82; −10% = 683.7; 78.6% Fib 682.91; 38.2% Fib of Mar–Oct 683.69; the 200-day reaches 683–689 by Nov 6–20 on a flat path [calc] |
| **660–662** | −9.2 to −9.4 | **Trend-change line.** Jul 29 close 661.73 (low 661.14); YTD anchored VWAP 660.34; 50% Fib of Mar–Oct 659.23 |
| 635–646 | −11.4 to −12.9 | −15% = 645.7; Apr 17 gap 642.18–644.07; 61.8% Fib of Mar–Oct 634.77 |

**XLK** [DB, calc]

| Level | % | Why it matters |
|---|---|---|
| 197.1–198.2 | +3.5 / +4.1 | Oct 6 anchored VWAP 197.08; 10-day 198.16 |
| 188.0–189.9 | −0.3 to −1.3 | 50-day 189.9; 38.2% Fib 189.2; Jul-low anchored VWAP 188.04 |
| 182–186.7 | −2.0 to −4.4 | Sep 17 gap 186.13–186.73; 50% Fib 184.86; volume point of control 183.87; Sep 14 low 182.08 |
| **178.8–180.5** | −5.2 to −6.1 | **The hinge.** 61.8% Fib 180.51; Aug 24 low 178.82 |
| **173–177** | −7.0 to −9.1 | **My core zone.** Mar-30 anchored VWAP 176.54; 78.6% Fib 174.33; 38.2% Fib of Mar–Oct 174.0; Aug–Sep intraday low 173.04; 200-day reaches 171–173 by November |
| 166.5–167.1 | −12.3 / −12.6 | **Trend-change line.** Jul 29 close 166.57; 200-day today 167.1 |
| 160–165 | −13.4 to −16.0 | 50% Fib of Mar–Oct 164.97; May gaps 163.2–166.8; YTD anchored VWAP 160.26 |

## 4. Base rates and analogs that cut against me

- **Unconditionally it is a coin flip:** given −4.04%, 51% of NDX episodes ended shallower than −8% (about 699), with the median trough only 4.5 sessions later.
- **The "narrow tech dip" set is less bearish:** NDX at −4% with the S&P 500 within 2% of its record (n=21) had a median of −7.4%; 57% ended shallower than −8%.
- **Short horizons favour a bounce:** QQQ analogs' 10-day and 20-day medians are +1.2% (71% / 65% positive) [DB].
- **Seasonality:** midterm-year NDX, Oct 14 → Dec 31, median +5.1%, up 90% of years (n=10); S&P 500 Q4 lows cluster Oct 15–23 [SP].
- **Two recent dips stayed shallow** (Mar 2024 −7.1%, Dec 2024 −6.1%). They started slower, but over the long history a fast early drop does not predict depth (n=72, median −7.7%).
- **Small samples:** the SOX-filtered sets are n=8–9 and include 2000 and 2018.

## 5. The strongest counter-evidence

1. **The primary uptrend is intact.** The 697–705 shelf has held four times; QQQ is 8.2% above a rising 200-day; QQQ/SPY and XLK/SPY are still above their 200-day averages (+1.9%, +7.7%) [DB].
2. **Money is rotating *within* tech.** AAPL is at a record and MSFT near one. Fundamentals keep improving: TSMC Q3 revenue +50.9% y/y, ASML short of 2027–28 supply, NVDA's CFO at $1.3T of 2027 hyperscaler capex [CAT].
3. **Few forced sellers may be left:** US fundamental long/short net leverage at the 2nd percentile, $166bn into money-market funds, buyback windows reopening (all single-source).
4. **Bonds absorbed the hot CPI.** The 10-year is off its 5.31% peak, and ZN futures were +0.58 overnight [MR].
5. **TSMC tonight is a catalyst.** A beat-and-raise that closes green and holds could end the semis selling. Semis drove most of QQQ's decline.

## 6. What would prove me wrong (closing basis)

- **Price:**
  - Two QQQ closes above **746.45**, or XLK above **197.08**, before Oct 28: the low is in above my zone.
  - QQQ holds every close at or above **697** through **Fri Nov 6**, after the FOMC, mega-cap results and payrolls: the shallow case wins.
  - A new record close by **Nov 20** (QQQ above **759.66**, XLK above **202.00**): the trend is intact.
- **Events:**
  - On **Oct 21, 28 or 29**, capex is raised *and* the spenders' stocks rise 5% or more the next day, with QQQ back above its 50-day (**726.66**) by Oct 30. That would be the July reaction function, and it breaks the bear path.
  - The **Oct 28** FOMC holds without escalating, and the 10-year closes below 5.0%.
- **Internals:** more than 60% of IT members back above their 50-day; QQQE/QQQ back above its 50-day; SOXX closes above 559 [SL].
- **What escalates to a trend change:** QQQ closes below **661.73** and XLK below **166.57**; HY OAS above 3.46%; 10-year above 5.31%; an Oct 28 hike with a signalled follow-up.

**UNVERIFIED or single-source:** Oct 28 hike odds; Oracle's BBB− and CoreWeave's ~15% yield; IMF figures (secondary); the AMZN date; the Goldman/Nomura/Citadel positioning and money-market figures; the "higher bar" argument (my judgment); 200-day projections (assumed price paths); IBKR overnight prints (thin, not closes).
