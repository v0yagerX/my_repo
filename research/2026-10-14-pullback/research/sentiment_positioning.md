# Sentiment, positioning, volatility and options structure (as of the Oct 14, 2026 close)

Data pulled Oct 15, 2026, about 03:15–04:00 UTC (11:15 pm–midnight ET Oct 14).

Evidence labels used throughout:
- **[CONFIRMED]**: a primary source, or computed from local data or IBKR.
- **[SINGLE-SOURCE]**: one secondary outlet only.
- **[OPINION]**: a strategist's view or a desk model.
- **[UNVERIFIED]**: I could not confirm it.

Computed files:
- `analysis/sent/vol.py`, `vol_lows.py`, `season.py`, `opt_calc.py`, `cboe_pc.py`
- `analysis/sent/nvda_options_oct14.csv`
- `analysis/sent/dl/cboe_pc_all.csv`
- `analysis/sent/dl/fg_long.json`

All paths are under `/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/`.

---

## 1. Key findings (most decision-relevant first)

1. **The vol market has not capitulated. Index-level fear is ordinary [CONFIRMED, computed].**
   - Oct 14 readings:
     - VIX 16.87, at the 44th percentile of the past year.
     - VIX/VIX3M 0.898. That is contango, not stress.
     - VVIX 94.45, below its 1-year median of 96.2.
   - Every tradable low in the data was set at much higher readings:

     | Low | VIX | VIX/VIX3M | VVIX |
     |---|---|---|---|
     | Semis/NDX low, Jul 29 2026 | 20.66 | 0.961 | 109.5 |
     | Mar 30 2026 | 30.61 | 1.051 | 127.8 |
     | Apr 8 2025 | 52.33 | 1.261 | 170.9 |
     | Aug 5 2024 | 38.57 | 1.144 | 173.3 |

   - Only the shallow Sep 16 2026 low (VIX 17.71, ratio 0.898) looks like today.
   - **Reading:** if this pullback is more than a two-day semis shakeout, vol has room to reprice before a washout-style low.

2. **SPX ≈ 7,700 is a mechanical cliff, and SPX closed 19 points above it.** SPX closed at 7,718.94; the intraday low was 7,693.31.
   - SpotGamma (Oct 12) [OPINION]: "Below 7,700 the gamma profile turns negative." Dealer hedging then amplifies moves instead of damping them, and 7,400 "comes into view."
   - Goldman's CTA model, via a Tickmill recap of Oct 13 [SINGLE-SOURCE]:
     - Short-term pivot 7,704, medium-term 7,493, long-term 7,012.
     - Global CTA equity length is about $43.5B, down from $125B a month ago.
     - A 1-month "down tape" implies about −$65.8B of US equity selling (−$143.8B globally).
   - Overnight ES (~7,744 Dec future) puts cash SPX at roughly the level itself. That conversion is an UNVERIFIED fair-value estimate from `live_snapshots.md`.

3. **Sentiment is fearful underneath but not capitulative.**
   - CNN Fear & Greed [CONFIRMED, CNN data feed]:
     - 32.4 ("Fear") on Oct 14, down from 44.1 on Oct 13.
     - Breadth was 7.8 and strength 10 (both "extreme fear"). Junk-bond demand read 59.2 ("greed").
     - At prior lows it was much lower: 5.8 (Mar 30 2026), 25.6 (Jul 29 2026), 27.3 (Sep 16 2026), 2.9 (Apr 8 2025), 16.6 (Aug 7 2024).
   - AAII [CONFIRMED, aaii.com], last reading the week ending Oct 7, *before* this selloff:
     - Bulls 40.3%, bears 39.0%.
     - Bears have been above average for 35 straight weeks: a persistent wall of worry, not euphoria.
     - The 1-year bearish high was 53.3% on Sep 16, the week of a minor SPX low.
   - **CBOE equity put/call [CONFIRMED, Cboe CDN]:** 0.61 on Oct 14.
     - The 10-day average is 0.589, which is the 1-year median.
     - The 10-day average peaked at 0.65–0.72 around every prior low in the sample.
     - No hedging panic is visible.

4. **Crowding is at the top of the AI/semis complex. Discretionary hedge-fund net exposure is light, while systematic and retail books are full.**
   - BofA October FMS (fieldwork Oct 2–8):
     - Net 37% overweight tech, up from 30%, the highest since Aug 2020 [CONFIRMED across investingLive, TechFlow and TheStreet].
     - "Long global semiconductors" is the most crowded trade [CONFIRMED]. The 45% share is [SINGLE-SOURCE].
   - Deutsche Bank (Oct 12) [SINGLE-SOURCE via Investing.com]:
     - Tech and mega-cap positioning is overweight, "near the top of a long-run trend."
     - Discretionary investors are modestly underweight. Systematic strategies are still overweight.
   - Goldman prime book, via Tickmill (Oct 13) [SINGLE-SOURCE]:
     - US fundamental L/S net leverage 46.9%, the **2nd percentile** of the past year.
     - Long/short ratio 1.565, the 1st percentile over 5 years.
     - Global net 75.9% (10th percentile); global gross 308.7% (60th percentile).
   - Nomura's McElligott (Oct 13 recap) [SINGLE-SOURCE / OPINION]:
     - US systematic positioning at the **86th percentile**.
     - SPX 25-delta put skew at the 0.4th percentile, call skew at the 99.6th: "fear of benchmark underperformance."
     - Downside hedges are cheap and upside is being chased.

5. **Retail leverage is still buying dips, with no retail capitulation.**
   - Oct 13 ETF flows (ETF Action) [CONFIRMED-ish, one flow vendor]:
     - **SOXL +$711.9M** inflow.
     - NVDL −$491.4M, after **+$526.7M** in the prior report (Yahoo/ETF.com data as of Oct 13, 6 am). That is roughly flat net, consistent with churn.
     - SMH +$324.8M; SOXX −$140M (Yahoo).
   - NVDL total net assets are about $3.76B (IBKR) to $4.05B (flow vendors).
   - FINRA margin debt was $1.45T in August, +37.2% YoY [SINGLE-SOURCE: Advisor Perspectives/TradingTools]. June set the record at $1.502T, then July fell $84.8B, the largest monthly drop in the series.
   - Precedent: in July 2026 SOXL took a record $6.9B inflow while SOX fell 28.6% peak-to-trough [SINGLE-SOURCE: Memeburn citing Bloomberg/Balchunas]. SOX has still not reclaimed its June high.

6. **NVDA options price a normal, not stressed, regime.** All figures computed from IBKR frozen Oct 14 close quotes, S = 221.30.
   - ATM IV term structure:
     - Oct 16: 47.6%. This is a 2-day window that includes TSMC results (~2 am ET Oct 15) and opex. On a trading-day basis it is about 40%.
     - Oct 23: 36.4%; Oct 30: 35.5%; Nov 13: 33.9%.
     - **Nov 20: 38.5%.** This expiry spans earnings, expected Nov 17 or 18.
     - Dec 18: 36.6%; Jan 15: 36.2%.
   - Earnings-event 1 sd ≈ **±5.8%** (expected absolute move ≈ 4.6%).
   - Nov 20 straddle ≈ ±$21.60 (±9.8%), a 199.7–242.9 range. The 1-sd range is 195.8–250.2.
   - IBKR IV percentile: 15% (52-week), 24% (26-week).
   - Skew is mild. The 25-delta risk reversal is −3.8 vols on Nov 20 and −4.0 on Dec 18.
   - NVDA option volume put/call on Oct 14: 0.79, against a 90-day average of 0.69. That is only modestly elevated.

7. **Open-interest map for NVDA [CONFIRMED, IBKR OI; partial chains].**
   - **Oct 16:** the 220 strike dominates both sides (99.2k calls, 64.6k puts). Max pain ≈ 220.
     - Put OI shelves: 200 (37.5k), 180 (35.8k), 195 (33.6k), 210 (28.4k).
     - Call OI at 230–250 (60–80k per strike) is now far out of the money and decays to zero.
   - **Nov 20:** the largest strike is the **245 call (104.0k)**, then the 210 call (77.6k) and 230 call (61.9k).
     - Puts: 200 (53.2k), 180 (33.5k), 215 (29.6k), 210 (29.4k).
     - Max pain ≈ 210 (partial chain).
   - **Dec 18:** the 200 put holds 64.5k; the 220 strike holds 59.2k calls and 44.4k puts.
   - **The 200 strike is the visible put-OI shelf across Nov and Dec.**
   - OI does not reveal who is long or short. Dealer direction is an inference.

8. **Midterm-year Q4 seasonality is supportive on average but conditional [CONFIRMED, computed from Yahoo index history].**
   - SPX, midterm years 1954–2022 (n=18): Oct 14 → Dec 31 mean +5.1%, median +6.0%, 78% positive. Q4 mean +6.7%. The post-Oct-14 Q4 low fell in October in 12 of 18 years.
   - NDX (n=10): Oct 14 → Dec 31 median +5.1%, 90% positive.
   - SOX (n=7): median +17.1%, 71% positive.
   - The big midterm October lows mostly came after deep year-to-date drawdowns: 1962, 1966, 1974, 1990, 2002, 2022. SPX is only −1.3% from its high today.
   - **2018 is the cautionary analog.** Semis peaked first (SOX was already −13% by Oct 14, 2018). SPX made its high on Sep 20 while yields rose. Then SPX fell −19.8% and SOX −26% into Dec 24.
   - In midterm years December is weak for NDX (mean −1.2%, 30% positive) and SOX (mean −3.2%).

9. **Buyback support is near its seasonal low and returns over late October and November.**
   - Goldman, via Tickmill [SINGLE-SOURCE]:
     - About 10% of S&P market cap enters its open window by Fri Oct 16.
     - The buyback desk is running at 0.8x its average.
     - 86% of desk volume runs through 10b5-1 plans, which continue during blackouts.
   - Citadel's Rubner [SINGLE-SOURCE via AdvisorAnalyst and search snippets]: a "reload" from about Oct 15 against record $1.3T of authorizations.
   - About 44% of S&P weight reports in the last week of October [SINGLE-SOURCE].
   - NVDA's own discretionary buyback window is very likely closed until after its ~Nov 18 report. This is an inference [UNVERIFIED]; 10b5-1 purchases may continue.

---

## 2. Detailed evidence

### 2.1 Volatility, computed from local Yahoo files (`data/_VIX.csv`, `_VIX3M.csv`, `_VVIX.csv`)

**Latest (Oct 14, 2026)**
- VIX 16.87 (intraday high 17.45). It rose +1.60 points (+10.5%) from 15.27.
- VIX3M 18.79.
- VIX/VIX3M 0.898, up from 0.850 the day before.
- VVIX 94.45, up from 85.38.
- Percentile ranks of today's readings:

  | Window | VIX percentile | VIX/VIX3M percentile | VVIX percentile |
  |---|---|---|---|
  | 1 year | 43.7 | 69.8 | 42.5 |
  | 2 years | 46.0 | — | — |
  | ~5 years | 41.9 | — | — |

- 1-year VIX range: 13.47–31.05 (median 17.16). 1-year VVIX median is 96.2.

**2026 context**
- VIX max 31.05 (Mar 27), min 14.21 (Sep 22).
- VIX/VIX3M was ≥1 on only 11 days in 2026, all between Feb 6 and Apr 7.
- The ratio has not reached 0.95 since Jul 29.

**Realized vs implied**
- SPX 20-day realized vol 10.3%, so VIX−RV = +6.6 points. Hedging demand jumped on Oct 14 more than realized movement did.
- 20-day realized vol: NVDA 25.5% (10-day 28.5%, 60-day 36.9%); SOX 35.4%.

**Vol at prior drawdown lows** (`vol_lows.py`)

| Episode (peak → low) | Depth | VIX at low | VIX/VIX3M | VVIX | Max VIX in episode |
|---|---|---|---|---|---|
| SPX Jul 16 → Aug 5 2024 | −8.5% | 38.57 (intraday 65.73) | 1.144 | 173.3 | 38.57 |
| NDX/NVDA low Aug 7 2024 | NDX −13.6%, NVDA −27% | 27.85 | 1.031 | 151.2 | 38.57 |
| SPX Feb 19 → Apr 8 2025 | −18.9% | 52.33 | 1.261 | 170.9 | 52.33 |
| SPX Oct 28 → Nov 20 2025 | −5.1% | 26.42 | 1.026 | 128.6 | 26.42 |
| SPX/SOX/NVDA low Mar 30 2026 | SPX −9.1%, SOX −15.6%, NVDA −20.2% | 30.61 | 1.051 | 127.8 | 31.05 |
| SOX Jun 22 → Jul 29 2026 | SOX −28.6%, NDX −11.3%, NVDA −19.4% | 20.66 | 0.961 | 109.5 | 22.22 |
| Minor SPX low Sep 16 2026 | SPX −3.7% | 17.71 | 0.898 | 95.4 | — |
| **Now (Oct 14 2026)** | SPX −1.3%, SOX −20.2%, NVDA −7.5% (close basis) | **16.87** | **0.898** | **94.45** | — |

The July 2026 thresholds sit at the 84th (VIX 20.66), 88th (ratio 0.96) and 83rd (VVIX 109.5) percentiles of the past year.

**IBKR live implied vol** (overnight Oct 14, REALTIME; IBKR's "IV percentile" methodology is undocumented):

| Underlying | IV | 30-day HV | IV percentile 52w / 26w / 13w | Option P/C volume today vs average |
|---|---|---|---|---|
| NVDA | 33.2% | 29.6% | 15% / 24% / 48% | 0.79 vs 0.69 |
| SOXX | 35.6% | 37.2% | 26% / 6% / 12% | 2.59 vs 1.87 |
| QQQ | 17.0% | 15.5% | 8% / 8% / 15% | 0.84 vs 1.10 |
| SPY | 13.3% | 10.2% | 37% / 46% / 74% | 1.13 vs 1.07 |

Option P/C volumes are computed from IBKR fields: today's put volume over call volume, and the same for the average. SOXX put demand is elevated; NVDA and QQQ put demand is not.

**Nomura (via Tickmill, Oct 13; note probably written before the Oct 14 drop)** [SINGLE-SOURCE]
- SPX 3-month ATM IV at the 2nd percentile (1-year).
- 25-delta put skew at the 0.4th percentile; call skew at the 99.6th.
- 1DTE straddle at the 9th percentile (2-year).
- SPX realized vol: 10-day 7.0, 1-month 10.0.
- Source: https://www.tickmill.com/blog/institutional-insights-nomura-mcelligott-binaries (Oct 13, 2026).

### 2.2 Sentiment surveys and gauges

**AAII Sentiment Survey** [CONFIRMED]
- Sources: https://www.aaii.com/sentimentsurvey/sent_results (accessed Oct 15); https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-plummets (Oct 10, 2026).
- Week ending Oct 7: bullish 40.3% (+5.6), neutral 20.8%, bearish 39.0% (−7.5). Spread +1.3, below its 6.5 average for the 12th week.
- Bears have been above their 31.5% average for 35 straight weeks.
- Recent history (bull/bear):

  | Week ending | Bullish | Bearish | Note |
  |---|---|---|---|
  | Sep 30 | 34.6% | 46.5% | |
  | Sep 23 | 32.7% | 48.1% | |
  | Sep 16 | 28.8% | 53.3% | 1-year bearish high; SPX swing low 7,507.77 that day |
  | Jul 29 | 31.0% | 42.1% | Week of the semis low |

- The Oct 14 week's survey is released Thu Oct 15 and is **not yet available**.
- Cash-allocation special question: 24.3% of members are putting new cash into cash equivalents.

**CNN Fear & Greed** [CONFIRMED, CNN data feed]
- Source: https://production.dataviz.cnn.io/index/fearandgreed/graphdata (timestamp 2026-10-14T23:59 UTC).
- Score 32.4 ("Fear"). Previous close 44.7, 1 week ago 42.1, 1 month ago 31.0, 1 year ago 28.3.
- Components (score, raw value):

  | Component | Score | Raw value |
  |---|---|---|
  | Momentum | 35.6 | SPX 7,718.94 vs 125-day MA 7,530.8 |
  | Strength | 10 (extreme fear) | Net new highs/lows −8.3 |
  | Breadth | 7.8 (extreme fear) | McClellan volume summation 250.7 |
  | Put/call | 25.6 | 5-day average 0.770 |
  | VIX | 42.7 | 16.87 vs 50-day MA 15.48 |
  | Junk bonds | 59.2 (greed) | Spread 1.199 |
  | Safe haven | 46 | — |

- Over the past year the score ranged 5.2 (Nov 20 2025) to 71.2 (May 1 2026). Today ranks at the 28th percentile.
- In 2026 the score was below 25 only during Mar 9–Apr 7 and on Jun 26.

**NAAIM Exposure Index** [UNVERIFIED]
- Paywalled since Aug 1, 2026 ("transitioned to a subscription-based access model"): https://naaim.org/programs/naaim-exposure-index/
- One third-party site shows 77 on Oct 2, 2026; I could not open it. YCharts' last public value is 79.70 (Jul 29, 2026).
- An unverified claim puts the late-August reading at 102.66.

**Investors Intelligence** [UNVERIFIED]: no current reading found. II publishes behind a paywall.

**BofA Global FMS, October** (fieldwork Oct 2–8; 161 participants, $453bn AUM)
- Sources: investingLive https://investinglive.com/news/long-global-semiconductors-remains-the-most-crowded-trade-followed-by-short-us-treasuries-according-to-bank-of-america/ (Oct 13, 2026); TechFlow https://www.techflowpost.com/en-US/article/34548 (Oct 14, 2026).
- Confirmed findings:
  - Net 37% overweight tech, up from 30%, the highest since Aug 2020.
  - Most crowded trade: long global semiconductors; short US Treasuries second.
  - Biggest tail risk: a disorderly rise in bond yields; second: an AI bubble.
  - A net 4% expect a weaker global economy, the first negative reading in several months.
  - Largest cut to bank exposure since Mar 2023.
- Bond-yield question: 37% would switch from equities to bonds if the 10-year reaches 6%, and 19% are already doing so (TechFlow).
- Semis crowding was "45%, down from 82% in July" [SINGLE-SOURCE].
- The October cash level is UNVERIFIED. The 3.9% figure is September's.

### 2.3 CBOE put/call ratios (Cboe daily market statistics)

[CONFIRMED] Endpoint pattern: https://cdn.cboe.com/data/us/options/market_statistics/daily/YYYY-MM-DD_daily_options. Data cover 576 sessions, Jul 2024–Oct 14 2026.

**Oct 14, 2026**
- Equity 0.61; total 0.88; index 1.01; SPX+SPXW 1.24; VIX 0.29.

**Equity put/call averages**
- 5-day 0.590; 10-day 0.589; 20-day 0.550 (25th percentile of the past year).
- The 10-day average rose from 0.512 on Sep 30 to 0.589: hedging is rising, but from a complacent base.
- Past year: median 0.58 (single day) and 0.586 (10-day). Single-day maximum 0.92 (Dec 31 2025); 10-day maximum 0.718 (Mar 20 2026).

**Readings at or near prior lows**

| Episode | Peak single day | 10-day average | Total P/C |
|---|---|---|---|
| Aug 2024 | 0.97 (Aug 8) | 0.725 | 1.28 on Aug 5 |
| Apr 2025 | 1.02 (Apr 3) | 0.687 (Apr 8), max 0.695 | 1.23 on Apr 8 |
| Mar 2026 | 0.90 (Mar 18) | 0.718 | — |
| Jul 2026 | 0.86 (Jul 8) | 0.684 (Jul 28) | — |
| Sep 2026 | 0.69 (Sep 16) | 0.598 | — |
| **Now** | 0.61 | 0.589 | 0.88 |

Today's readings look like the minor September low, not the July or March lows.

### 2.4 Positioning: systematic, hedge funds, institutions, flows

**Goldman Sachs flows and positioning, via Tickmill "Institutional Insights: Goldman Sachs SP500 Flows & Positioning Update 13/10/26"**
- Source: https://www.tickmill.com/blog/institutional-insights-goldman-sachs-sp500-flows-positioning-update-131026 (Oct 13, 2026) [SINGLE-SOURCE; the page body does not explicitly attribute every number to Goldman].
- CTA positioning:
  - Global CTA equity length about $43.5B, down from $67B a week earlier and $125B a month earlier.
  - Pivots: 7,704 short-term, 7,493 medium-term, 7,012 long-term.
- CTA flow scenarios:

  | Scenario | 1-week global | 1-week US | 1-month global | 1-month US |
  |---|---|---|---|---|
  | Flat tape | −$3.64B | +$5.27B | +$5.97B | +$8.39B |
  | Up tape | +$23.24B | +$6.39B | +$136.81B | +$24.53B |
  | Down tape | −$26.07B | −$0.94B | −$143.84B | −$65.79B |

- Hedge fund leverage:

  | Book | Gross | Net |
  |---|---|---|
  | Global | 308.7% (60th percentile, 1-year) | 75.9% (10th percentile) |
  | US fundamental L/S | 213.0% (53rd percentile) | 46.9% (2nd percentile) |

  - US long/short ratio 1.565, the 1st percentile over 5 years.
- Buybacks: desk at 0.8x the 2024/25 average daily volume; 86% via 10b5-1; ~10% of S&P cap opens its window by Friday.
- Breadth: the median S&P 500 stock is 16% below its 52-week high, described as "the lowest breadth since the 2000 Dot-Com Bubble."

**Deutsche Bank weekly positioning (Oct 12)** [SINGLE-SOURCE]
- Source: Investing.com https://www.investing.com/news/stock-market-news/tech-positioning-nears-longrun-trend-top-deutsche-bank-says-93CH-4943505 (Oct 12, 2026).
- Overall positioning declined slightly but stays modestly overweight. Tech and mega-cap growth fell but stay overweight, "near the top of a long-run trend."
- Discretionary investors are modestly underweight.
- Systematic strategies are "dropped from elevated levels but remain overweight." Vol-control funds *increased* equity allocation; CTA positioning "fell materially but remains elevated."
- Weekly fund flows (EPFR via DB):
  - Equity funds +$12.4B.
  - Bond funds +$33.8B, a 4-month high.
  - **Money-market funds +$166.4B, the largest in more than 6.5 years.**
- The Oct 5 note had discretionary positioning below neutral and systematic positioning in the top 10% of history.

**Citadel Securities, Scott Rubner** ("The Market You Think You Own Is Not the Market You Own," Oct 2, 2026), via AdvisorAnalyst https://advisoranalyst.com/2026/10/06/four-stocks-one-yield-and-the-october-15-reload.html/ (Oct 6, 2026) [SINGLE-SOURCE / OPINION]
- CTA equity positioning fell from +2.35 sd (end of August) to −0.80 sd.
- Buyback windows reopen around Oct 15 against record $1.3T of authorizations.
- Seasonality: in midterm years since 1930, the Q4 low came in October 14 of 24 times. The median rally from that low into year-end is 10%, and midterm Q4s average +5.6%.
- His framing: early-quarter weakness is "an opportunity."
- Citadel's own pages returned HTTP 403.

**Nomura / McElligott (via Tickmill, Oct 13)** [SINGLE-SOURCE]
- Collective US systematic positioning at the 86th percentile, near year-to-date highs.
- Collapsing realized vol forced vol-scaling funds to buy back equity exposure.
- Breadth: 85% of SPX constituents are more than 10% below their all-time highs and 59% are more than 20% below.

**Goldman prime-book hedge fund flows**
- May 22, 2026 (Yahoo UK, citing Bloomberg/Goldman) [CONFIRMED-ish]: semis were the "most heavily net-sold U.S. subsector over the past month."
  - Source: https://uk.finance.yahoo.com/news/hedge-funds-lock-gains-following-115500316.html
- July 20, 2026 (Bloomberg, Goldman Prime): hedge funds sold US tech at a record pace over two months, about 10% cumulative.
  - Source: https://www.bloomberg.com/news/articles/2026-07-20/goldman-says-hedge-funds-sell-us-tech-stocks-at-record-pace
- A search snippet claims a newer (~Oct 13) Goldman report: semis and hardware were the most net-sold, IT is 32% of North American HF net exposure (98th percentile since 2010), and Thursday (Oct 8) was the heaviest tech selling day after an OpenAI revenue disappointment. **[UNVERIFIED]**: I could not locate the article.

### 2.5 Retail and leverage

**ETF Action, data for Oct 13 (published Oct 14)** [CONFIRMED, one vendor]
- Source: https://www.etfaction.com/growth-and-blend-equity-lead-17b-inflow-day/
- SOXL +$711.9M; NVDL −$491.4M; SMH +$324.8M; QQQ +$6.38B.
- Leveraged/inverse equity category +$864.2M; single-stock leveraged −$470.7M.
- Equity ETFs +$15.69B on the day, +$38.70B over the week.

**Yahoo / ETF.com "Daily ETF Flows: RSP Gathers $565M" (Oct 13, data as of 6 am ET)**
- Source: https://finance.yahoo.com/markets/options/articles/daily-etf-flows-rsp-gathers-210004324.html
- NVDL +$526.67M, AUM $4.05B (+12.99%).
- QQQ −$1.16B; SOXX −$139.96M.
- The two NVDL figures probably cover consecutive sessions, implying churn. Possible custom-basket noise.

**IBKR snapshot of NVDL** (overnight Oct 14) [CONFIRMED]
- Total net assets $3.756B; 90-day average dollar volume $413M a day; YTD +25.2%; 1-month +5.6%.

**July 2026 precedent** [SINGLE-SOURCE]
- Memeburn (Aug 6, 2026, citing Bloomberg Intelligence and Balchunas): https://memeburn.com/leveraged-etfs-in-chip-stocks-hit-21-billion/
  - SOXL took a record $6.9B inflow in July.
  - About $21B sits in chip leveraged/inverse ETFs.
  - Global single-stock leveraged exposure to Nvidia is about $4.8B.
- ETF Action (Aug 3, 2026): SOXL +$2.50B in a week when it fell −16.15%.
  - Source: https://www.etfaction.com/traders-pour-nearly-2-5-billion-into-leveraged-semiconductor-etf-soxl-despite-weekly-drop/

**FINRA margin debt** [SINGLE-SOURCE; FINRA's site returned 403]
- August 2026: $1.45T, +2.6% m/m, +37.2% YoY (+33.1% real), and 3.2% below the June record of $1.502T.
  - Sources: Advisor Perspectives, Sep 17, 2026 (https://www.advisorperspectives.com/dshort/updates/2026/09/17/margin-debt-finra-august-2026; snippet only, page 403); TradingTools (https://www.thetrading.tools/margin-debt).
- July: $1.417T, a record monthly drop of $84.8B (TradingTools, Sep 10, 2026: https://www.thetrading.tools/chart-of-the-day/2026-09-10-margin-debt-record-drop).
- Free credit balances about $0.43T, so net free credit ≈ −$1.03T.
- September data is not yet published (due around the third week of October).

### 2.6 Corporate buyback blackout timing
- Goldman, via Tickmill (Oct 13) [SINGLE-SOURCE]: about 10% of S&P cap enters its open window by Oct 16; desk at 0.8x average; 86% via 10b5-1.
- Citadel (Rubner, Oct 2, via AdvisorAnalyst; search snippet of Citadel's October piece) [SINGLE-SOURCE]: a broad reopening "beginning" around Oct 15, building through earnings and accelerating into November. Record $1.3T authorized through Sep 29.
- An earlier Citadel note (late September; search snippet, page 403) said 61% of companies would be in blackout by Sep 30 and that "the window does not reopen for the majority of the index until November 1" [UNVERIFIED and conflicting with the Oct 15 framing; both can hold, since windows reopen gradually].
- About 44% of S&P weight reports in the final week of October [SINGLE-SOURCE, search snippet].
- **NVDA specifically:**
  - Its fiscal Q3 ends in late October and it reports around Nov 17–18 (`research/catalysts.md`).
  - Its open-market window is therefore likely closed now, which is inferred and UNVERIFIED.
  - $99bn remains on its authorization (catalysts.md, from the NVDA Q2 release).

### 2.7 NVDA options (IBKR, read-only)

**Method**
- IBKR returned FROZEN_DELAYED quotes stamped 16:00 ET Oct 14, plus open interest.
- IBKR's own IV and greeks fields were invalid, so I backed IVs out of bid/ask mids with Black-Scholes: S = 221.30, r = 4.08% (13-week bill), no dividend, calendar-day time.
- I re-pulled six contracts to spot-check an earlier agent's transcription in `scripts/opt_raw.py`. All six matched: Oct 16 220C/220P/200P, Nov 20 200P/210C, and Dec 18 220P.
- 46 contracts are new pulls (`analysis/sent/opt_new.py`). Full table: `analysis/sent/nvda_options_oct14.csv`.

**ATM (220 strike) term structure**

| Expiry | Days | Call IV | Put IV | ATM IV | Straddle | Straddle move | Straddle range | 1-sd range |
|---|---|---|---|---|---|---|---|---|
| Oct 16 (opex; TSMC Oct 15) | 2 | 49.6 | 45.7 | 47.6* | $6.30 | ±2.85% | 215.0–227.6 | 213.6–229.2 |
| Oct 23 | 9 | 37.1 | 35.6 | 36.4 | $10.12 | ±4.58% | 211.2–231.4 | 209.0–234.3 |
| Oct 30 | 16 | 36.1 | 34.8 | 35.5 | $13.12 | ±5.93% | 208.2–234.4 | 205.4–238.4 |
| Nov 13 (pre-earnings) | 30 | 34.3 | 33.5 | 33.9 | $17.15 | ±7.75% | 204.2–238.5 | 200.8–243.9 |
| **Nov 20 (spans earnings)** | 37 | 38.9 | 38.1 | **38.5** | $21.60 | **±9.76%** | **199.7–242.9** | 195.8–250.2 |
| Dec 18 | 65 | 36.7 | 36.6 | 36.6 | $27.20 | ±12.29% | 194.1–248.5 | 189.6–258.3 |
| Jan 15 2027 | 93 | 36.4 | 35.9 | 36.2 | $32.05 | ±14.48% | 189.3–253.4 | 184.3–265.7 |

\*Calendar-day basis. It is about 40% on a 252-trading-day basis.

- **Earnings event:** total variance from Nov 13 to Nov 20 implies a 1-sd move of 7.5% including normal days. Removing 7 calendar days at Nov 13 IV leaves an **event-only 1 sd of about ±5.8%** (expected absolute move about 4.6%). This matches catalysts.md (±5.9%).
- Forward vols: Oct 16 → Oct 23 32.5%; Nov 20 → Dec 18 33.9%.

**Skew**, interpolated in delta:

| Expiry | 25d put IV | ATM IV | 25d call IV | 25d RR (call − put) | Other |
|---|---|---|---|---|---|
| Nov 20 | 40.3 | 38.5 | 36.5 | −3.8 vols | 10d put 45.0, 10d call 35.9 |
| Dec 18 | 38.6 | 36.6 | 34.6 | −4.0 vols | — |
| Oct 16 | — | — | — | −2.6 vols | — |

I found no historical NVDA skew series, so I cannot rank this. SpotGamma (Oct 12) says NVDA Nov and Dec upside calls are "priced cheaper than the equivalent moves in the S&P 500" [OPINION].

**Risk-neutral probabilities**
- Approximation: N(d2) at each strike's own IV, ignoring the skew-slope term, so put-side probabilities are slightly understated.
- Nov 20: P(below 210) 35%; below 200 23%; below 190 15%; below 180 9%. P(above 245) 18%; above 260 8%.
- Dec 18: P(below 200) 28%; below 180 14%.

**Open interest**, 16:00 Oct 14, contracts:

Oct 16 expiry:

| Strike | 180 | 185 | 190 | 195 | 200 | 205 | 210 | 212.5 | 215 | 217.5 | 220 | 222.5 | 225 | 230 | 235 | 240 | 245 | 250 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calls | — | — | 3.2k | 6.7k | 8.0k | 8.2k | 15.8k | — | 22.7k | 1.2k | **99.2k** | 2.6k | 24.6k | 59.6k | 76.5k | 70.2k | 42.8k | 80.4k |
| Puts | 35.8k | 25.1k | 26.1k | 33.6k | **37.5k** | 25.6k | 28.4k | 11.7k | 18.6k | 8.4k | **64.6k** | 12.9k | 24.0k | 20.6k | 10.9k | 6.6k | — | — |

- Max pain ≈ **220** (partial chain).
- Sampled-strike put/call OI 0.75.

Nov 20 expiry:

| Strike | 160 | 165 | 170 | 175 | 180 | 185 | 190 | 195 | 200 | 205 | 210 | 215 | 220 | 225 | 230 | 235 | 240 | 245 | 250 | 255 | 260 | 270 | 280 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calls | — | — | — | — | — | — | — | — | 25.4k | — | **77.6k** | — | 18.0k | 15.7k | 61.9k | 19.4k | 40.1k | **104.0k** | 42.0k | 21.2k | 28.7k | 26.1k | 15.3k |
| Puts | 21.8k | 11.7k | 24.3k | 18.9k | 33.5k | 12.9k | 28.1k | 21.3k | **53.2k** | 22.7k | 29.4k | 29.6k | 23.6k | 17.7k | 13.8k | — | — | — | — | — | — | — | — |

- Max pain ≈ **210** (partial chain; in-the-money puts above 230 and in-the-money calls below 200 not sampled).

Dec 18 expiry:
- Puts: 180 26.8k; 190 35.5k; **200 64.5k**; 210 29.3k; 220 44.4k.
- Calls: 220 59.2k; 230 25.6k; 240 29.5k; **250 51.7k**; 260 27.0k.

**What IBKR could not provide**
- Valid IV and greeks: the fields were invalid on frozen data, so I computed them myself.
- Full-chain OI in one call; I sampled about 90 contracts.
- Any customer-versus-dealer direction.

### 2.8 Seasonality (computed: `analysis/sent/season.py`; SPX daily from 1950, NDX from 1985, SOX from 1994, Yahoo)

| Midterm-year stat | SPX (1954–2022, n=18) | NDX (1986–2022, n=10) | SOX (1998–2022, n=7) |
|---|---|---|---|
| October return, mean / median / % up | +3.1% / +2.8% / 72% | +3.9% / +4.4% / 80% | +6.6% / +3.4% / 86% |
| Oct 14 → Oct 31, mean / % up | +1.5% / 67% | +5.0% / 90% | +9.0% / 71% |
| November, mean / % up | +2.9% / 83% | +4.9% / 70% | +11.6% / 100% |
| December, mean / % up | +0.6% / 61% | **−1.2% / 30%** | **−3.2% / 43%** |
| Q4, mean / median / % up | +6.7% / +7.9% / 83% | +7.8% / +5.4% / 80% | +15.5% / +9.8% / 86% |
| Oct 14 → Dec 31, mean / median / % up | +5.1% / +6.0% / 78% | +9.1% / +5.1% / 90% | +17.9% / +17.1% / 71% |
| Oct 14 → Dec 31, all years (comparison) | +3.5% / +4.5% / 79% | +5.2% / +4.2% / 78% | +7.1% / +7.8% / 71% |
| Worst Oct 14 → Dec 31 (midterm) | 2018 −9.4%; 1978 −8.2%; 1974 −5.7% | 2018 −11.6% | 2018 −7.9% |
| Mean / median max drawdown, Oct 14 close → year-end low | −2.5% / −0.7% | −2.0% / −0.9% | −2.2% / −0.2% |

- **Timing of the SPX Q4 low after Oct 14 in midterm years:** October in 12 of 18 years (often Oct 15–23), November in 3 (1970, 1978, 1982), December in 3 (1974, 1994, 2018).
- **SPX midterm-year annual lows came in October** in 1966, 1974, 1990, 2002 and 2022. Each followed a 16–36% decline from the prior year-end. 2026 is the opposite case: SPX is near its high, and the stress is concentrated in semis.
- **SOX conditional:** in years where SOX fell more than 4% from Sep 30 to Oct 14 (n=8: 1995, 2000, 2005, 2008, 2012, 2014, 2018, 2022), the Oct 14 → Dec 31 return averaged −1.8%. The range ran from −24.0% (2000) to +22.7% (2014). SOX is −7.5% over that window in 2026.
- **2018 analog (computed):**
  - SOX peaked Mar 12, 2018 and was −13.3% by Oct 14.
  - SPX peaked Sep 20, 2018 and was −5.6% by Oct 14; NDX was −6.6%.
  - The Q4 low came Dec 24: SPX −19.8%, NDX −23.0%, SOX −26.0% from their 2018 peaks.
- **2014 analog:** a sharp V-low on Oct 15 led to SPX +9.7% and SOX +22.7% by year-end.
- **2026 so far:** SPX +0.9% from Sep 30 to Oct 14, NDX −1.5%, SOX −7.5%. SOX is −20.2% from its Jun 22 peak of 14,634.7.

---

## 3. Numbers table: current readings vs prior lows

| Gauge | Now (Oct 14) | Sep 16 2026 minor low | Jul 29 2026 semis low | Mar 30 2026 low | Apr 8 2025 | Aug 5–7 2024 |
|---|---|---|---|---|---|---|
| VIX | 16.87 | 17.71 | 20.66 | 30.61 | 52.33 | 38.57 / 27.85 |
| VIX/VIX3M | 0.898 | 0.898 | 0.961 | 1.051 | 1.261 | 1.144 / 1.031 |
| VVIX | 94.45 | 95.4 | 109.5 | 127.8 | 170.9 | 173.3 / 151.2 |
| CNN F&G | 32.4 | 27.3 | 25.6 | 5.8 | 2.9 | 33.1 / 16.6 |
| CNN P/C 5-day | 0.770 | 0.799 | 0.837 | 0.903 | 0.993 | 0.857 / 0.923 |
| CBOE equity P/C, 10-day average | 0.589 | 0.586 | 0.676 | 0.671 | 0.687 | 0.700 / 0.708 |
| AAII bears | 39.0% (Oct 7, pre-drop) | 53.3% | 42.1% | n/a | n/a | n/a |
| SPX drawdown from high | −1.3% | −3.7% | −6.5% (Jul 29) | −9.1% | −18.9% | −8.5% |
| SOX drawdown from high | −20.2% | −23.2%* | −28.6% | −15.6% | −39.7% | — |
| NVDA close | 221.30 | 213.90 | 190.01 | 165.17 | 96.30 | 100.45 / 98.91 |

\*Sep 16 SOX drawdown from the Jun 22 peak: 11,246 / 14,635 − 1. The Jul 29 SPX drawdown is from the Jun high, per the base-rate files; the other cells come from `vol_lows.py`.

---

## 4. Unverified or conflicting

1. **CTA positioning: the three models disagree.**
   - Goldman, via Tickmill (Oct 13): still long, at $43.5B, down from $125B.
   - Citadel (Oct 2): −0.80 sd, i.e. already short or underweight.
   - Deutsche Bank (Oct 12): CTA positioning "fell materially but remains elevated."
   - Nomura (Oct 13): systematic composite at the 86th percentile.
   - Different models and dates. Goldman and Deutsche Bank imply more selling capacity in a down tape; Citadel implies less.
2. **NVDL flows:** +$526.7M in Yahoo/ETF.com's Oct 13 report and −$491.4M in ETF Action's Oct 13 data. Possibly consecutive days or a custom basket; the net is near zero.
3. **NAAIM:** paywalled; 77 (Oct 2) is unverified.
4. **Investors Intelligence:** not found.
5. **BofA FMS October:** cash level not found (3.9% was September's). The 45% semis-crowding share is single-source.
6. **The "newer" Goldman prime-book note** (IT 32% of NA net, 98th percentile; OpenAI-revenue selling day): UNVERIFIED.
7. **Margin debt:** the August $1.45T figure comes from secondary sources; FINRA's page returned 403. September data is not out.
8. **Buyback window:** "Oct 15 reopening" (Citadel, Oct) and "majority not until Nov 1" (Citadel, late September snippet) conflict in emphasis. NVDA's own blackout status is inferred.
9. **SpotGamma's 7,700 gamma flip and Goldman's 7,704 CTA pivot are modeled levels,** not observable facts. Dealer positioning is estimated.
10. **NVDA options math:**
    - Oct 16 IV is distorted by the 2-day window and the TSMC event.
    - Max pain uses partial chains.
    - IBKR's IV-percentile methodology is not documented.
    - Risk-neutral probabilities are approximations that ignore the skew slope.
11. **Overnight moves:** the IBKR overnight prints were NVDA 218.07, QQQ 720.54, SOXX 509.00 and SPY 765.71. The options snapshot reflects the 4 pm close only. TSMC results (~2 am ET Oct 15) were not yet out at pull time.
12. **The AAII reading predates the Oct 13–14 selloff.** The next release (Thu Oct 15) could show a bearish jump.

---

## 5. Implications for the pullback-bottom question (bullish and bearish readings)

**Bearish or "not yet" readings**
- **No capitulation signature at the index level.**
  - VIX, VVIX, VIX/VIX3M and the CBOE equity put/call 10-day average all sit at or below their 1-year medians.
  - Every prior low in the sample, including the semis-only July 2026 low, came with VIX above 20, ratio above 0.95, VVIX above 109 and the put/call 10-day average above 0.67.
  - If this becomes an index-level correction, those thresholds imply more downside or time.
  - On the SPX side, CTA (down-tape −$65.8B US over a month) and gamma (below 7,700) mechanics are positioned to *accelerate* rather than absorb a break.
- **Crowding without forced liquidation yet.**
  - Tech is the most overweight sector since Aug 2020 (BofA), with long semis the most crowded trade.
  - Systematic books sit at the 86th percentile (Nomura), and SPX put skew is extremely cheap while call skew is rich (complacency).
  - Retail is still adding 3x semis leverage (SOXL +$712M on Oct 13), and margin debt is near record ($1.45T).
  - Washouts usually show leveraged-ETF outflows and margin contraction (cf. July's −$84.8B). That has not happened this time.
- **Breadth is already poor.** CNN breadth and strength are in "extreme fear." A Goldman recap says the median stock is 16% off its 52-week high; Nomura says 59% of SPX constituents are more than 20% below their all-time highs. This is narrow, top-heavy leadership whose last pillar (AI/semis) is cracking: a 2018-style setup (semis lead down, SPX tops last, yields rising) rather than a 2014-style one.
- **For NVDA specifically:**
  - Options imply about a 23% risk-neutral chance of a close below 200 by Nov 20 and about 15% below 190.
  - The 200 strike is the largest put-OI shelf (Nov 53k, Dec 64.5k). If that level is approached, put sellers' hedging could pull price toward it rather than support it.
  - NVDA's own buyback window is likely shut until after earnings.
- **Seasonal caveat:** midterm December is the weakest month for NDX and SOX (mean −1.2% and −3.2%).

**Bullish or "dip is closer to done" readings**
- **The semis complex has already corrected a lot.** SOX is −20.2% from its June high and SOXX puts are bid (option P/C 2.59 vs 1.87 average). In July 2026 semis bottomed with VIX only at 20.7, so a semis-led low does not need index-level panic.
- **Discretionary hedge funds are already light.**
  - US fundamental L/S net leverage is at the 2nd percentile (1-year) and the long/short ratio at the 1st percentile (5-year), via a Tickmill/Goldman recap.
  - AAII bears have been above average for 35 straight weeks.
  - Money-market funds just took their largest weekly inflow in 6.5 years (+$166bn).
  - Plenty of sidelined cash and low hedge-fund net exposure limits the forced-selling pool and fuels squeezes.
- **Mechanical tailwinds arrive soon.**
  - Buyback windows reopen from about Oct 15 into November against record $1.3T authorizations.
  - Oct 16 opex clears a large 220-strike pin and stale out-of-the-money call OI.
  - Midterm-year seasonality is strong from mid-October: SPX median +6.0% to year-end and 78% up; Q4 lows cluster Oct 15–23; SOX median +17%.
- **NVDA options are not stressed.** IV is at the 15th percentile (52-week), skew is mild (25-delta RR about −4 vols), and option put/call is only 0.79. There is no panic premium, but also no hedging overhang to unwind. The earnings event prices only about ±5.8%.

**Net read** (an analytical judgment, not a forecast)

Today's evidence is most consistent with an **unfinished** pullback:
- Sentiment has shifted from greed to moderate fear (F&G 32, rising hedging).
- None of the capitulation markers that accompanied 2024–2026 lows are present.
- Systematic, retail and sector-level positioning in AI/semis remains crowded.

Signposts that would mark a durable low (watch-list):
- VIX/VIX3M ≥ 0.95–1.0.
- VVIX > 110.
- CBOE equity put/call 10-day average ≥ 0.65.
- CNN F&G ≤ 25.
- AAII bears ≥ 45–50%.
- Leveraged semis ETF *outflows*.
- SPX holding or reclaiming 7,700, or flushing to the 7,400–7,500 CTA/gamma zone with a vol spike.

For NVDA these line up with the 210 strike (Nov max pain, 77.6k calls, 29.4k puts) and the 200 strike (largest put OI in Nov and Dec, about the Nov 20 straddle low of 199.7).

The bullish counter-case rests on hedge funds already being under-exposed, the buyback reload, and mid-October midterm seasonality. It is a reason not to assume a crash, but it is not evidence that the low is in.
