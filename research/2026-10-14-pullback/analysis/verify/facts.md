# Facts re-verification: decision-critical external claims

*Verifier: facts. Started 03:48 UTC Oct 15, 2026 (11:48 pm ET Oct 14); final check 06:35 UTC (2:35 am ET). I used fresh WebSearch and WebFetch, primary sources where I could reach them, live prediction-market APIs (Polymarket gamma API, Kalshi public API) and IBKR quotes (read-only). I did not reuse the research files' sources except to locate the claims under test.*

*Files present at audit time: analysis/market_{bull,bear,verdict}.md and .json; semis_{bull,bear}.md; tech_{bull,bear}.md; nvda_{bull,bear}.md. **Not present:** semis_verdict, tech_verdict and nvda_verdict (.md/.json). This report checks facts; where a finding contradicts text in an existing file, I name the file.*

## 11. TSMC Q3 2026: RELEASED (Q3 results out; Q4 guide comes on the 06:00 UTC call)
- **Status by check time:**
  - **Not out** at 03:48, 04:05 and 05:33 UTC (WebSearch returned previews only).
  - At **~05:35 UTC**, pr.tsmc.com listed "**TSMC Reports Third Quarter EPS of NT$29.43**" (dated 2026/10/15) ([TSMC PR](https://pr.tsmc.com/english/news/3346)), with the management report posted ([IR Q3 page](https://investor.tsmc.com/english/quarterly-results/2026/q3)).
  - The posted earnings release and presentation are the "**WoG**" (without guidance) versions. **Q4 guidance is given on the call** at 14:00 Taiwan time (06:00 UTC, 2:00 am ET).
- **Q3 actuals vs guide / consensus:**

  | Item | Actual | Guide / consensus |
  |---|---|---|
  | Revenue | NT$1,494.24bn (+17.6% q/q, +50.9% y/y); **US$46.72bn** | July guide was US$44.6–45.8bn, so a **beat** (already known from monthly sales) |
  | **Gross margin** | **66.4%** (2Q 67.7%; 3Q25 59.5%) | Guide 65–67%, so **mid-range**; consensus ~66.5% |
  | **Operating margin** | **58.7%** (2Q 60.3%) | Guide 56–58%, so **above the top** |
  | **Net income** | **NT$763.06bn** (+8.0% q/q, +68.7% y/y); net margin 51.1% | LSEG SmartEstimate NT$746.3bn, so a **beat by ~2.2%**, a sixth straight record |
  | EPS | NT$29.43 (US$4.60/ADR) | |

  - **Node mix:** 2nm 8% of wafer revenue (from 3% in 2Q), 3nm 33%, 5nm 28%, 7nm 10%; advanced (≤7nm) 79%.
  - **Platform:** **HPC 68%** (2Q 66%; 3Q25 57%). HPC grew +22% q/q; Smartphone 21% (+10% q/q).
  - **Geography:** North America 79%, China 5%.
  - **Capex:** **US$13.84bn in Q3**, US$40.64bn YTD. That leaves ~US$19–23bn for Q4 if the US$60–64bn 2026 range holds; any change will come on the call.
  - **Free cash flow:** NT$476.6bn.
  - Source: [3Q26 Management Report, Oct 15, 2026](https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-10/f53a64fd40fc0b453f94e077e5aba8cad506f27b/3Q26%20ManagementReport.pdf) (pdftotext extraction).
- **Reaction so far (IBKR, read-only):**
  - TSM ADR overnight **417.80, −2.84%** at 05:33 UTC. That is weaker than −1.64% at 03:57 UTC, pre-release.
  - NVDA 218.60 (−1.22%), SOXX 509.34 (−1.94%), ES Dec 7,743 (−0.35%, delayed, 05:23 UTC).
  - **Taiwan's cash session closed (13:30 local = 05:30 UTC) before the release.** TSMC (2330) traded ~−2% intraday (IBKR NT$2,440 at 03:38 UTC; AP −2.2%), so the Taiwan share reaction comes Friday.
- **Read:**
  - A clean beat on profit and operating margin.
  - The gross margin fell 1.3 pp q/q, as guided (2nm ramp, overseas fab dilution).
  - **The tradeable items are not yet known:** the Q4 revenue/GM guide, the 2026 capex range, 2027 commentary, CoWoS/AI remarks. The early overnight ADR tape is soft.

- **Final check, 06:35 UTC (2:35 am ET):**
  - **Q4 2026 guidance, 2026 capex update, 2027 / CoWoS / AI remarks: still UNVERIFIABLE.**
    - The call began at 06:00 UTC, but no outlet had published the guide yet: Google News TSMC feed, Reuters/CNBC/Bloomberg/Nikkei headlines, and WebSearch all checked.
    - The IR page still showed only the "_WoG" release and presentation.
    - The Reuters brief (updated 01:42 am ET) has no guidance.
    - **The next agent must pull the guide before using TSMC as a catalyst.**
  - **Benchmark for the guide:** a Morgan Stanley preview had Q4 at +10–15% q/q, about US$51.4–53.7bn. A guide at or below ~US$51bn, or a GM guide below ~65%, would disappoint.
  - **ADR reaction so far (IBKR overnight, real-time):**
    - TSM **423.11 (−1.60%)** at 06:34 UTC. That is a recovery from the post-release low of **417.80 (−2.84%)** at 05:33 UTC, and roughly back to the pre-release −1.6%.
    - An Investing.com ticker widget showed TSM −3.40%, untimed.
    - NVDA 218.52 (−1.26%), SOXX 511.70 (−1.49%) at 06:33–06:34 UTC.
    - **The beat has not reversed the overnight semis tape.**
  - **Sources:** [Reuters via Investing.com, 01:35/01:42 am ET](https://www.investing.com/news/stock-market-news/tsmc-q3-profit-jumps-69-to-record-beating-expectations-4950551); [CNBC](https://www.cnbc.com/2026/10/15/tsmc-third-quarter-profit-global-ai-.html) (403); Bloomberg headline "TSMC's Profit Surpasses Expectations After AI Orders Rush In" (05:36 UTC).

---

## Scorecard

| # | Claim | Verdict | Correction / note |
|---|---|---|---|
| 1 | FOMC hiked Sep 16 to 3.75–4.00%; Warsh is Chair; next FOMC Oct 27–28 | **CONFIRMED** | Vote 12–0 |
| 2 | Oct 28 hike odds ~35% late Oct 14; >95% odds of a hike by year-end | **PARTLY CONFIRMED, now STALE** | By 11 pm–midnight ET, market pricing for Oct 28 was **~24–32%**, not 35%: prediction markets ~24% and fed-funds futures 28–32%. Pricing for at least one more hike by Dec 9 was **~82–91%**, not >95%. The "54%" figure in catalysts.md is a peak or stale reading, not a current one |
| 3 | Sep CPI: +0.6% m/m, 3.7% y/y; core +0.3%, 2.6% | **CONFIRMED** (BLS) | Consensus (LSEG): headline 0.6% / 3.6%, core 0.2% / 2.5%. **The headline m/m was in line**; the beats were y/y headline and both core prints |
| 4 | FT Oct 8: OpenAI ~$50bn run rate vs ~$70bn reported; Anthropic-comparison / gross-vs-net explanation; Bloomberg ≥$70bn by year-end | **CONFIRMED**, with two nuances | Prior figure was **$68bn** (CNBC). Outlets give two different stories for the gap (see below) |
| 5 | NVDA 8-K Aug 17: guarantees capped at $105bn, ~4.25 GW; supply commitments $279bn | **CONFIRMED** | Combined guarantee exposure is **$108.5bn**. Total of all commitment categories is **$366bn**, plus $56bn of AI-cloud and third-party lease commitments. The $279bn sits in the CFO commentary (8-K exhibit); I did not open the 10-Q itself |
| 6 | Q2 FY27 revenue $96.2bn; Q3 guide $108bn ±2%; Q4 GM trough 71–72%; FY28 ~+70% | **CONFIRMED** (CFO commentary + call transcript) | Also: Q3 GM guide **74.0% ±50 bp**; FY28 GM **72–73%**; "supply-constrained outlook" |
| 7 | NVDA Q3 FY27 earnings date Nov 17 vs Nov 18 | **UNVERIFIABLE: no official announcement yet** | Third-party calendars say Nov 17, 18 or 25. Last year's notice came Oct 29 |
| 8 | META Oct 21; MSFT Oct 28; GOOGL Oct 28; LRCX Oct 21; KLAC Oct 28; AMD Nov 3; AMZN | **CONFIRMED** for META, MSFT, GOOGL, LRCX, KLAC, AMD. **AMZN UNVERIFIABLE** | AMZN's date is not announced. It is estimated at about Oct 29 (last year's notice came Oct 16) |
| 9 | CRWV −15.5% Oct 14; bonds ~15% yield; 2032s below 80c | **CONFIRMED** | Price data: −15.46%. CNBC (intraday): 2032 notes at 14.8% YTM. Overnight, Reuters says the 2032s are **below 78c** |
| 10 | Brent ~$103–107 Oct 8–14; Hormuz disruption; Trump "no Iran strike before midterms" | **CONFIRMED** (minor range nit) | Closes **$104.28–106.65**; settle **$106.06** Oct 14. Brent fell to ~$104.3–104.7 overnight on reports the US may ease sanctions |
| 11 | TSMC Q3 2026 results | **RELEASED ~05:30 UTC.** Q3 CONFIRMED; **Q4 guide UNVERIFIABLE as of 06:35 UTC** | Net income NT$763.06bn beat NT$746.3bn; GM 66.4% (mid-guide); OM 58.7% (above guide); HPC 68%; Q3 capex US$13.84bn. TSM ADR −1.6% at 06:34 UTC (low −2.84%). The Q4 guide, capex and 2027 remarks come on the 06:00 UTC call and had not been published when I last checked |
| 12 | ASML Q3: record ~€11.7bn; Q4 guide €14.2–15.2bn; shares −3.9% | **CONFIRMED** (6-K) | **The −3.9% is the NASDAQ ADR** (1,717.76 → 1,650.00). The Amsterdam close is unverified |
| 13 | Microsoft Maia 300 | **CONFIRMED** (Oct 12) | "Multi-gigawatt deployments beginning in 2027" is in Microsoft's release. "**Potentially** more than 1M chips next year" is Reuters, not Microsoft. The 40% tokens/MW vs "leading GPU-based systems" is Guthrie's own projection |
| 14 | Oracle cut to BBB− | **CONFIRMED, but misdated by implication** | **S&P**, **Jul 9, 2026** (BBB → BBB−; A-2 → A-3; stable). This is **not new news on Oct 14**. Moody's has a negative outlook; I found no Oct downgrade |
| 15 | SpotGamma "below 7,700 gamma turns negative"; Goldman CTA pivots 7,704 / 7,493 / 7,012 | **PARTLY CONFIRMED** | SpotGamma calls 7,700 the "risk pivot" (Oct 12 and Oct 14 notes). Its Oct 14 TRACE map puts negative gamma **below ~7,600**, and I could not find the "7,400 comes into view" wording. The CTA levels appear only in a Tickmill post (Oct 13) whose **body never names Goldman** |
| 16 | SPX closes Oct 8 = 7,765.36; Oct 14 = 7,718.94 | **CONFIRMED** (AP/Yahoo/WTOP) | Oct 8: −36.41 (−0.47%). Oct 14: −86.51 (−1.11%) |

---

## Detail and sources

### 1. FOMC Sep 16 hike, Chair, next meeting: CONFIRMED
- **Hike:** the Fed statement says the Committee "decided to raise the target range for the federal funds rate by 1/4 percentage point to 3-3/4 to 4 percent." The vote was 12–0. [federalreserve.gov press release, Sep 16, 2026](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm); [statement PDF](https://www.federalreserve.gov/monetarypolicy/files/monetary20260916a1.pdf).
- **Chair:** the Board page lists "Kevin Warsh, Chairman" ([federalreserve.gov, accessed Oct 15](https://www.federalreserve.gov/aboutthefed/bios/board/default.htm)). The press-conference PDF is titled "Chairman Warsh's Press Conference" ([Sep 16, 2026](https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20260916.pdf)). Jerome Powell is still listed on the Board, with no title.
- **Next meeting:** the Fed calendar shows Oct 27–28 (no SEP), then Dec 8–9 (with SEP). There is no November meeting. [FOMC calendar, accessed Oct 15](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm). The Sep minutes came out Oct 7.

### 2. Market-implied Oct 28 and December odds: PARTLY CONFIRMED; the team's numbers are stale
**Oct 28 hike (25 bp), latest readings I could get:**

| Source | Reading | Timestamp |
|---|---|---|
| **Polymarket**, "Fed Decision in October?" (live API) | **23.5%** hike 25 bp; 76.5% no change; ~$12m volume on the no-change leg | **03:45 UTC Oct 15** (11:45 pm ET Oct 14) |
| **Kalshi** KXFED-26OCT, "above 4.00%" (live API) | **bid 23 / ask 24** | ~03:55 UTC Oct 15 |
| **Investing.com Fed Rate Monitor** (fed funds futures) | **27.6%** hike (4.00–4.25%); 72.4% hold | **11:25 pm EDT Oct 14** |
| Reuters via Investing.com (LSEG rate futures) | **31.6%**, up from 22.1%; ~40 bp of hikes priced by end-January | article 10:53 pm Oct 14 |
| Yahoo Finance (CME FedWatch) | 35%, up from 22% | 2:50 pm CDT = **3:50 pm ET Oct 14** |
| CNN, morning (CME FedWatch) | 49% | morning Oct 14 |
| CME Group's X account | "jumped to 50% post-CPI, from 22% a day ago" | Oct 14 (post seen only via search snippet) |

- **The "54.2%" reading is stale.** One "54.2%" FedWatch article is dated **Sep 23, 2026** ([Phemex](https://phemex.com/news/article/cme-fedwatch-542-probability-of-rate-hike-at-october-meeting-97512)). Other outlets do describe Oct 14 intraday readings "up to ~54%". catalysts.md lines 41, 105, 451 and 504 state "~54% after CPI" as the current level. **That is wrong as a current level.** It was a peak at best, and possibly contaminated by the Sep 23 figure.
- **The "~35% late on Oct 14" figure is a 3:50 pm ET snapshot.** By 11:25 pm–midnight ET, futures-based and prediction-market pricing were **24–28%**, and LSEG had 31.6%. This affects market_verdict.md lines 74, 144, 256, 303 and 324, market_bull.md:61 and tech_bear.md:76. Direction is unchanged (a hold is the base case), but the hike risk is overstated by roughly 7–11 points.

**December / year-end:**
- **Polymarket**, "Fed Decision in December?" (03:45 UTC): 25 bp hike at the Dec meeting **78.5%**, no change 19.5%. Separately, "Another Fed rate hike in 2026?" is at **81.5%**.
- **Kalshi** KXFED-26DEC: "above 4.00%" (at least one more hike by Dec 9) bid 88 / ask 91; "above 4.25%" (two more hikes) bid 26 / ask 28.
- **Investing.com** (11:25 pm EDT): Dec 9 at 3.75–4.00% **14.3%**, 4.00–4.25% **63.6%**, 4.25–4.50% **22.1%**. That implies about **86%** for at least one more hike.
- CNBC (Oct 14) said ">90% likelihood of at least one more rate hike before the year is out" ([CNBC, Oct 14](https://www.cnbc.com/2026/10/14/us-treasury-yields-cpi-inflation-report.html), via search snippet; the page returns 403).
- **Verdict:** the ">95% at least one hike by year-end" figure (market_verdict.md:74 and :324; market_bear.md:93; market_bull.md:61) is **overstated**. Current pricing is **~82–91%**.

### 3. September CPI: CONFIRMED
- **BLS (released 8:30 am ET Wed Oct 14):** CPI-U +0.6% SA m/m (Aug +0.4%), 3.7% y/y (Aug 3.4%). Core +0.3% m/m, 2.6% y/y. Energy +5.2%, gasoline +9.1%, shelter +0.4% m/m (3.2% y/y). [BLS CPI release, Oct 14, 2026](https://www.bls.gov/news.release/cpi.nr0.htm).
- **Consensus (LSEG):** headline **0.6% m/m (in line)**, 3.6% y/y; core 0.2% m/m, 2.5% y/y ([Fox Business, Oct 14, 8:33 am EDT](https://www.foxbusiness.com/economy/cpi-inflation-september-2026)). Dow Jones/WSJ also had core at 0.2%.
- **Nuance:** any text calling the headline m/m a "beat" is wrong. Headline m/m was in line. Headline y/y and both core figures beat.

### 4. OpenAI revenue (FT, Oct 8): CONFIRMED, with nuances
- **Reuters (Oct 8, 5:12 pm; Singh/Hu):** a person familiar said September annualized revenue was "almost $50 billion, a drop from what it signaled earlier." OpenAI had earlier indicated a run rate "approaching $70 billion" at a separate investor event. The discrepancy "mainly arose from an attempt to produce a direct comparison with figures from rival Anthropic." OpenAI did not comment. [Reuters via Investing.com](https://www.investing.com/news/stock-market-news/openais-annualized-revenue-20-billion-less-than-previously-signaled-ft-reports-4939854).
- **CNBC:** OpenAI told investors ~$50bn at end-September, below the widely reported **$68bn**. A person familiar said "the $68 billion figure included gross revenue from OpenAI's partners." The run rate grew 77% in Q3, and enterprise grew 107%. [CNBC, Oct 8](https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html) (403 on fetch; quoted from search extracts).
- **A second, different explanation:** Yahoo (Howley, Oct 8, 12:40 pm CDT), citing the FT, says investors took an estimated ~$40bn August figure and added OpenAI's stated 70% growth to reach $70bn ([Yahoo Finance](https://finance.yahoo.com/technology/article/openais-annualized-revenue-20-billion-lower-than-prior-investor-estimates-174058048.html)). **So the "gross-vs-net / Anthropic comparison" story is one of two published explanations, not settled fact.**
- **Bloomberg (Oct 9):** "OpenAI Expects $70 Billion in Annualized Revenue by End of 2026" ([Bloomberg](https://www.bloomberg.com/news/articles/2026-10-09/openai-expects-70-billion-in-annualized-revenue-by-end-of-2026); [Investing.com relay](https://ng.investing.com/news/stock-market-news/openai-expects-to-reach-70-bln-revenue-by-end2026-bloomberg-reports-2728445)). The relays say "$70bn or more", on OpenAI's own (net) accounting. Bloomberg's companion piece covers the different accounting methods ([Oct 9](https://www.bloomberg.com/news/articles/2026-10-09/anthropic-and-openai-s-revenue-calculations-confuse-investors)).
- **Context:** Anthropic's annualized revenue was $65bn in July (Bloomberg/Yahoo), and Reuters sources said it was "set to reach $100bn by year-end". On those figures, OpenAI is now below Anthropic on comparable gross-up assumptions.

### 5. NVIDIA guarantee and commitments: CONFIRMED
- **8-K (filed Aug 17, 2026):** residual-value guaranties to SB Energy (lessor) covering ~4.25 GW of IT load at the Portsmouth/PORTS-Pike site, Pike County, Ohio. The tenant is "an affiliate of OpenAI Group PBC". NVIDIA's aggregate obligation is "cumulatively capped at $105 billion for its initial commitment." NVIDIA may also, at its sole discretion, provide credit support for **~3.8 GW more**. OpenAI reimburses NVIDIA for any amounts paid. Ready-for-service is expected to begin in 2028. [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000069/nvda-20260817.htm).
- **CFO commentary for Q2 FY27 (8-K exhibit, Aug 26):**
  - Supply and capacity commitments are **$279bn** (up from $119bn), "primarily related to the procurement of memory." By year: remainder of FY27 $92bn, FY28 $87bn, FY29 $88bn.
  - Other commitments: cloud service agreements $29bn, leases not yet commenced $25bn, equity investments $25bn, capex $8bn. **The total across all categories is $366bn.** There are another $36bn of AI-cloud agreements and $20bn of third-party leases not yet commenced.
  - Guarantees: **$3.5bn existing plus $105bn = $108.5bn** maximum gross exposure. The first phase is expected in FY29.
  - Inventory: **$31.6bn**.
  - [SEC](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27cfocommentary.htm).
- **Caveats:**
  - I verified the $279bn in the CFO commentary, not in the 10-Q itself.
  - The "3.8 GW optional" extension is a tail risk the team should mention.
  - Press reports say the cap is less than half the ~$250bn discussed in July. That is secondary-source only.

### 6. NVIDIA Q2 FY27 and guidance: CONFIRMED
- **Results:** revenue **$96,221m**; Data Center $89,023m (+18% q/q, +117% y/y); GAAP and non-GAAP GM 75.0% ([CFO commentary](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27cfocommentary.htm)).
- **Q3 guide:** "$108.0 billion, plus or minus 2%", with no China data-center compute assumed. **GM 74.0% ±50 bp.**
- **Call transcript (Aug 26, 5 pm ET; NVIDIA IR PDF, my pdftotext extraction):** Kress said "We expect margins to bottom in Q4 in the 71% to 72% range before settling at 72% to 73% in fiscal year 2028 as executed price increases take effect in Q1." She also said "our preliminary expectation is for fiscal year 2028 revenue to grow approximately 70% year-over-year," calling it "a supply-constrained outlook," with supply a bottleneck "at least through the end of fiscal year 2028." [Transcript PDF](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf).
- **Additional fact the team may want:** Kress said the memory price increase "exceeded our prior expectations and are headed even higher into next year."

### 7. NVIDIA Q3 FY27 earnings date: UNVERIFIABLE (not announced)
- NVIDIA's IR events page lists no upcoming event (accessed Oct 15). No "Sets Conference Call for Third-Quarter" release for FY27 exists yet.
- Last year's notice came **Oct 29, 2025**, for a **Nov 19, 2025** call ([NVIDIA newsroom](https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6914442)).
- Third-party calendars conflict: Wall Street Horizon says Nov 17 "confirmed" (not company-sourced), Public.com says Nov 18, Investing.com says Nov 25.
- The analysis files correctly flag this as UNVERIFIED. **Do not anchor scenario timing on Nov 17 vs 18.** Nov 18–25 is the realistic window, and the notice should come around late October.

### 8. Earnings dates
| Company | Date | Status | Source |
|---|---|---|---|
| META | Wed **Oct 21**, after close; call 4:30 pm ET | CONFIRMED | [Meta IR release, Oct 12](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-to-Announce-Third-Quarter-2026-Results/default.aspx) |
| MSFT | **Oct 28** (time not posted) | CONFIRMED | [Microsoft IR](https://www.microsoft.com/en-us/investor/default): "The next earnings release will be on October 28, 2026" |
| GOOGL | Wed **Oct 28**, call 1:30 pm PT / 4:30 pm ET | CONFIRMED | [Alphabet IR, announced Oct 6](https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Date-of-Third-Quarter-2026-Financial-Results-Conference-Call-2026-8tpGZsLS6v/default.aspx) |
| AMZN | not announced | UNVERIFIABLE | MarketBeat estimates Thu Oct 29. Last year's notice was issued Oct 16 for an Oct 30 call |
| LRCX | Wed **Oct 21**, 2 pm PT | CONFIRMED | [Lam newsroom, Sep 30](https://newsroom.lamresearch.com/2026-09-30-Lam-Research-Corporation-Announces-September-Quarter-Financial-Conference-Call). Guide was $8.1bn ±$0.4bn |
| KLAC | Wed **Oct 28**, 2 pm PT | CONFIRMED | [KLA IR event page](https://ir.kla.com/news-events/ir-calendar/event/first-quarter-fiscal-year-2027-earnings-call). One KLA news page reportedly shows Nov 4, which looks like an error |
| AMD | Tue **Nov 3**, 5 pm ET | CONFIRMED | [AMD newsroom, Oct 6](https://newsroom.amd.com/news/earnings-date-3q-2026/). Guide ~$13.0bn ±$0.3bn, GM ~56% |

Nov 3 is also US Election Day. AMD reports that evening.

### 9. CoreWeave: CONFIRMED
- **Stock:** close 65.78 vs 77.81 = **−15.46%** on 108m shares (local CSV, matches Reuters' −15.46%). The intraday low was 64.41, about −17%.
- **Bonds:** CNBC reported the 9.625% 2032 notes at **14.8% YTM** and the 9.75% 2031s at ~14.9% (intraday, 12:24 pm ET Oct 14). Barron's reportedly had the 2032s at ~79.5c. LSEG data had the 2032s below 80c by Oct 14 ([aggregated in FourWeekMBA](https://fourweekmba.com/ai-coreweave-falls-16-as-yield-on-its-2032-bonds-nears-15/); [Forbes, Oct 14](https://www.forbes.com/sites/jimosman/2026/10/14/coreweave-bonds-are-warning-of-a-bigger-problem-for-ai-stocks/), 403).
- **Overnight:** Reuters (via Investing.com, 10:53 pm Oct 14) has the 2032 bonds "**below 78 cents**".
- **Single-source:** 5-year CDS went from 368 to 643 bp in a week. Treat as unverified.

### 10. Oil / Hormuz / Trump: CONFIRMED
- **Brent front-month closes** ([Investing.com historical](https://www.investing.com/commodities/brent-oil-historical-data)):

  | Date | Close |
  |---|---|
  | Oct 7 | 100.20 |
  | Oct 8 | **104.28** (+4.07%) |
  | Oct 9 | 104.72 |
  | Oct 12 | **106.65** |
  | Oct 13 | 105.69 |
  | Oct 14 | **106.06** (settle +$0.37, matching CNBC and [The Nation, Oct 15](https://www.nationthailand.com/news/world/40072291)) |
  | Oct 15 (early) | ~104.3 |

  The intraday range for Oct 8–14 was 100.76–107.33. **"$103–107" is fine for closes, and slightly too high at the bottom for intraday.** WTI settled at $95.09 on Oct 14.
- **Hormuz:**
  - UKMTO: a container ship and a tanker were hit by projectiles in the strait on Oct 13. The IRGC Navy says a container ship sank after hitting a mine.
  - The IEA says Gulf crude exports are at ~75% of pre-war levels.
  - The US says it facilitated the shipment of >19m barrels through Hormuz.
  - [The Nation/Reuters, Oct 15](https://www.nationthailand.com/news/world/40072291); [CNBC, Oct 14](https://www.cnbc.com/2026/10/14/oil-rises-amid-growing-tensions-between-saudis-and-iran-backed-houthis.html).
  - There was also a Houthi attack on an Aramco building in Dhahran.
- **Trump, on Truth Social late Oct 8:** "We will not be attacking Iran at any time prior to the midterm elections to be held in the United States on November 3rd." [Al Jazeera, Oct 9](https://www.aljazeera.com/news/2026/10/9/trump-says-us-will-not-strike-iran-before-midterm-elections); [CNN, Oct 8](https://www.cnn.com/2026/10/08/politics/trump-iran-attack-election); [Axios, Oct 8](https://www.axios.com/2026/10/08/trump-iran-strikes-midterm-elections). Per search extracts, the US blockade of Iranian ports "will remain in full force and effect."

### 12. ASML Q3: CONFIRMED (one attribution fix)
- **Q3:** net sales **€11,662m**. The CEO calls them "record total net sales of €11.7 billion." GM 57.5%, net income €5.0bn (including a ~€0.5bn Mistral revaluation gain, per the call summary).
- **Guidance:** Q4 **€14.2–15.2bn**, GM ~57%. FY26 €44–45bn, GM ~56%.
- **2027–28 supply** "will not fully meet" customer demand. ASML is studying 2028 capacity beyond the +30% already announced.
- **No bookings figure is disclosed.**
- [ASML 6-K, Oct 14, 2026](https://www.sec.gov/Archives/edgar/data/0000937966/000162828026065813/pressreleasefinancialresul.htm).
- **The −3.9% is the US ADR:** local CSV 1,717.76 → 1,650.00 = −3.94%. I could not verify the Euronext Amsterdam close. Label it "ADR −3.9%".

### 13. Microsoft Maia 300: CONFIRMED (Oct 12, 2026)
- **Microsoft's release:** "multi-gigawatt deployments beginning in 2027." Maia 300 will become "the primary AI inference system for Microsoft products and services," with up to 7× the rack-scale throughput of Maia 200. [Microsoft Source EMEA, Oct 12](https://news.microsoft.com/source/emea/2026/10/microsoft-announces-maia-300-its-next-generation-custom-ai-chip/).
- **The 40% claim:** Guthrie said "We expect Maia 300 to deliver 40% more tokens per megawatt compared to leading GPU-based systems" ([Computerworld, Oct 13](https://www.computerworld.com/article/4234722/microsoft-unveils-new-maia-300-ai-chip.html)). This is a company projection; no GPU or workload is specified.
- **The unit count is from Reuters, not Microsoft:** Microsoft "plans to deploy **potentially** more than one million of the chips next year" ([Yahoo Finance, Oct 12, 11:56 am CDT](https://finance.yahoo.com/technology/ai/articles/microsoft-unveils-maia-300-ai-165614749.html)).

### 14. Oracle BBB−: CONFIRMED, but it is old news
- **Action:** S&P Global Ratings cut Oracle's long-term issuer rating to **BBB− from BBB on Jul 9, 2026**, and its short-term rating to A-3 from A-2, with a stable outlook ([The Next Web](https://thenextweb.com/news/oracle-sp-downgrade-ai-spending-junk-risk); [Computing.co.uk](https://www.computing.co.uk/news/2026/ai/oracle-under-pressure-after-ratings-downgrade-over-ai-expansion), 403; multiple relays agree on the date).
- **Other agencies:** Moody's has a negative outlook. **I found no Oct 2026 downgrade by any agency.**
- **Why ORCL fell on Oct 14:** the Motley Fool piece (Oct 14) that macro_rates.md relies on says Oracle "recently suffered" the downgrade, without naming the agency or date. It attributes the −8.8% move to Project Jupiter spending and financing worries, and to CPI/yields ([Fool, Oct 14](https://www.fool.com/investing/2026/10/14/why-did-oracle-stock-drop-today/)).
- **Correction:** macro_rates.md:251 and :388, and market_bear.md:132, imply the downgrade was a catalyst for the Oct 14 move. **It was not.** It is three months old. semis_leadership.md:511 has it right ("S&P cut it to BBB− on Jul 9").

### 15. SpotGamma / CTA levels: PARTLY CONFIRMED
- **SpotGamma, Oct 12** ([CPI note](https://spotgamma.com/cpi-options-positioning-spx-gamma/)): "7,700 as the key downside risk level", resistance at 7,825, Low Volatility Point at ~7,765, and "A sustained break below that level could shift dealer positioning into negative gamma." **7,400 is not mentioned.**
- **SpotGamma, Oct 14** ([note](https://spotgamma.com/selling-options-premium-low-volatility/)): 7,700 is "the risk pivot, SpotGamma's lens on a gamma flip". But the forward TRACE map shows "negative gamma above roughly 7,900 and below roughly 7,600." **So the strict claim "below 7,700 gamma turns negative" is softer than stated.** The negative-gamma pocket on the latest map starts nearer 7,600.
- **SPX on Oct 14:** low 7,693.31, close 7,718.94. It traded briefly below 7,700 and closed above it.
- **CTA pivots (Tickmill, Patrick Munnelly, "Update 13/10/26")** ([Tickmill](https://www.tickmill.com/blog/institutional-insights-goldman-sachs-sp500-flows-positioning-update-131026)):
  - Short-term **7,704**, medium **7,493**, long **7,012**.
  - Global CTA length ~$43.5bn (vs $67bn a week earlier and $125bn a month earlier).
  - 1-month down-tape scenario: −$143.8bn global, −$65.8bn US.
  - **The page body never names Goldman Sachs; only the title does.** Treat it as a single-source relay of what is presumably Goldman's CTA model.
- **Same-day check:** SPX closed **above** 7,704 on Oct 14 (7,718.94), so the short-term pivot has **not** been broken on a closing basis.

### 16. SPX closes: CONFIRMED
- **Oct 8:** 7,765.36, −36.41 (−0.47%). Nasdaq 27,193.34 (−1.3%), Dow 51,231.64. [AP via WTOP/Yahoo, "How major US stock indexes fared Thursday 10/8/2026"](https://wtop.com/national/2026/10/how-major-us-stock-indexes-fared-thursday-10-8-2026).
- **Oct 14:** 7,718.94, −86.51 (−1.1%). Dow 51,621.48, Nasdaq 26,692.87 (−1.9%), Russell 2000 2,729.53 (−1.9%). [AP via Yahoo, Oct 14](https://finance.yahoo.com/markets/stocks/articles/major-us-stock-indexes-fared-201908701.html).
- The AP Oct 8 piece says it was the S&P's "second straight loss after setting an all-time high". That is consistent with the local CSV ATH close of 7,818.93 on Oct 6, which makes Oct 14 just **−1.28% from the record close**.

---

## New material news after the Oct 14 close (overnight Oct 14–15)

1. **Asia chip rout, Thu Oct 15 session** ([AP via Yahoo, 8:50 pm CDT Oct 14](https://finance.yahoo.com/markets/world-indices/articles/south-korea-benchmark-kospi-index-015023409.html); [Reuters via Investing.com](https://www.investing.com/news/stock-market-news/asia-stocks-slump-as-chip-rout-deepens-after-hotter-us-inflation-4950421)):
   - **Indexes:** KOSPI **−7.7%** to 5,548.78 (Reuters −7.2%; it was above 9,000 in June). Nikkei **−4.8%** to 64,489. Taiex −3%. MSCI Asia-Pacific nearly −3%.
   - **Memory and equipment:** **SK Hynix −11.4%**, **Samsung −9.5%**, Kioxia −11.2%, **Tokyo Electron −7.3%**.
   - **Others:** **SoftBank −9.4%** (a direct OpenAI-exposure read), TSMC −2.2% ahead of results.
   - **Causes cited:** CXMT 4F² DRAM progress (Oct 10 conference), hot US CPI, Hock Tan's "casino" remarks, and AI-financing worries.
   - **Why it matters:** the team's layers may not reflect it. The memory-led de-grossing is **accelerating**, not exhausting, going into the US Thursday session.
2. **US overnight futures and ADRs (IBKR, read-only):**

   | Instrument | Last | Move | Time (UTC) | Feed |
   |---|---|---|---|---|
   | ES Dec | 7,730.5 | −0.51% vs 7,770.25 settle | 03:48 | delayed |
   | NVDA | **217.94** | −1.52% | 03:57 | real-time overnight |
   | SOXX | 509.71 | −1.87% | 03:55 | real-time overnight |
   | TSM ADR | 422.95 | −1.64% | 03:57 | real-time overnight |
   | TSMC (2330.TW) | NT$2,440 | −2.0% | 03:38 | delayed |

   The AP page ticker showed NQ about −1.1%.
   - **The ES settle sits 51 points above the SPX cash close.** So ES at 7,730 implies SPX cash of about **7,680**, below SpotGamma's 7,700 pivot and the 7,704 CTA pivot. This uses my rough fair-value assumption and is UNVERIFIED.
   - This is the real "bottom" test: the US open is set up to test 7,700 / 7,704 decisively.
3. **Rates and oil:**
   - Reuters/LSEG Oct hike odds are 31.6%, with ~40 bp priced by end-January. Prediction markets are lower (~24%).
   - Brent eased to **~$104.3–104.7**, on reports Washington is weighing easing sanctions on vessels carrying petroleum ([Business Standard, Oct 15](https://www.business-standard.com/amp/markets/commodities/oil-prices-fall-as-us-weighs-easing-sanctions-on-west-asian-crude-supply-126101500082_1.html)). That is a modest disinflation offset.
4. **Credit:** CoreWeave's 2032s are now quoted **below 78c** (Reuters), worse than the "below 80c" in the files.
5. **Scheduled today (Thu Oct 15):**
   - **TSMC Q3** results and call (see the top section).
   - **Sep PPI at 8:30 am ET.** Consensus is not settled:
     - Dow Jones/CNBC: +0.6% m/m, 5.5% y/y.
     - Schwab and Chaincatcher: +0.5% headline, +0.3% core.
     - RBC: +0.9% / core +0.4%.
     - macro_rates.md's +0.5% / +0.3% sits at the soft end, **so the hot-surprise bar is lower than the files imply.**
   - Jobless claims.
   - **Warsh fireside chat in Bangkok at 11:30 pm ET** (Fri local time), his last remarks before the blackout.
6. **Anthropic Q3 numbers (Reuters, shared with prospective investors Wed Oct 14; reported overnight)** ([Tribune/ANI citing Reuters, Oct 15](https://www.tribuneindia.com/news/business/anthropics-q3-revenue-jumps-45-to-usd-16-8-billion-ahead-of-anticipated-ipo)):
   - Q3 revenue **$16.8bn, +45% q/q** (Q2 $11.6bn). It reported an **adjusted profit**.
   - Analysts see a ~$110bn run rate by year-end. The IPO target valuation is reportedly >$2T, possibly after the midterms.
   - This is a demand-side positive for the AI-compute narrative and partly offsets the OpenAI $50bn story. IBD's 03:10 UTC headline framed it as "Anthropic Revenue Jumps, But Not Enough?"
7. **Bloomberg (03:41 UTC Oct 15):** "SK Hynix Down 57% From Peak as Chip Stocks Rout Intensifies". The Kospi fell as much as 7.9% intraday ([Bloomberg](https://www.bloomberg.com/news/articles/2026-10-15/chip-stocks-deepen-losses-as-concerns-mount-over-rates-ai-debt); [CNBC, Oct 15](https://www.cnbc.com/2026/10/15/sk-hynix-samsung-softbank-stocks-asia-tech-rout-ai-funding-worries.html)).
8. **Not new, so do not treat as overnight news:**
   - A Google News item dated Oct 14 ("Nvidia says roadmap intact after Kyber rack delay report") is a **Jul 6, 2026** Stocktwits story about SemiAnalysis's Kyber-to-2028 report.
   - The IDC "NVDA China share 34% in 1H26" is real: Reuters, IDC report dated Oct 13. Shipments were 678k, −44% y/y; Huawei 28% ([TechNode, Oct 14](https://technode.com/2026/10/14/nvidias-china-ai-chip-share-falls-to-34-as-huawei-reaches-28/)).
9. **Other confirmations made while checking:**
   - Micron's FQ1 FY27 guide is $61.5bn ±$1.5bn (Sep 30 8-K relays).
   - Treasury 10y par yield was 5.31% on Oct 5 and 5.19% on Oct 14 (2y 4.82%, 30y 5.52%) ([Treasury](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610)).
   - Hock Tan's "no clue" / "casino" remarks were made at the DBS forum in Singapore on Oct 12, as relayed from Bloomberg.
   - Kress's "$1.3 trillion in 2027" top-5 hyperscaler capex and "roughly a quarter of our business next year" from balance-sheet-backed AI labs are both in the Aug 26 transcript.
10. **Minor NVDA items (Oct 14):**
   - Huang said NVIDIA could cut off buyers developing unsafe AI ("hypothetical").
   - NVIDIA pledged a $250m five-year UK compute donation and launched the cuPotential CUDA-X library.
   - None of these is material.

## Errors and weak spots found in the team's files (fact level)
1. **Hike odds are stale and overstated.**
   - catalysts.md: "~54% after CPI". market_verdict.md / market_bull.md / market_bear.md / tech_bear.md: "~35% late Oct 14". Late-night pricing is **~24–32%** depending on venue.
   - ">95% at least one hike by year-end" should be **~82–91%**.
2. **The Oracle BBB− downgrade is treated as Oct 14 news** (macro_rates.md, market_bear.md). It is S&P, **Jul 9**.
3. **The SpotGamma framing is too strong.**
   - The latest map's negative-gamma zone starts below ~7,600, not 7,700.
   - "7,400 comes into view" was not found in SpotGamma's Oct 12 or Oct 14 notes.
   - The CTA pivots are from Tickmill, whose body does not name Goldman.
4. **ASML −3.9%** is the ADR move. Label it.
5. **CPI "beat" wording:** headline m/m was in line (0.6% vs 0.6%).
6. **OpenAI explanation:** two competing published accounts exist (cloud gross-up vs 40bn×1.7 extrapolation). Do not present gross-vs-net as settled.
7. **NVDA tail risk:** the 8-K lets NVIDIA, at its discretion, extend credit support to another ~3.8 GW. Combined guarantee exposure is $108.5bn, and total disclosed commitments are $366bn plus $56bn. Bear cases citing "$105bn" understate the exposure slightly; bull cases should note OpenAI's reimbursement obligation.
8. **Calendar:**
   - The NVDA date is unannounced, with a realistic window of Nov 18–25. The files' "Nov 17/18" is too narrow and should stay UNVERIFIED.
   - The AMZN date is unannounced.
   - AMD reports on Election Day (Nov 3).
