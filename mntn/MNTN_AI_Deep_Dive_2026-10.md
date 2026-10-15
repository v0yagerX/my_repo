# MNTN (NYSE: MNTN): AI victim or AI winner? Deep dive and 2027–2030 outlook

*As of **October 15, 2026**. Share price **~$10.25** (IBKR, Oct 15 intraday; prior close $9.40) (S112). Q3 2026 results have **not** been released. MNTN reports on **Wednesday, Nov 4, 2026, after the close** (S14). All company data below is therefore as of Q2 2026 (reported Aug 4, 2026).*

**Labels used throughout:**
- **[R]**: reported in an SEC filing or company release.
- **[R\*]**: management statement on a call or at a conference. These come from third-party transcripts and were not checked against audio.
- **[G]**: company guidance.
- **[C]**: sell-side consensus.
- **[3P]**: third-party data or press.
- **[E]**: our estimate, with the math shown.

`S#` refers to the numbered source list in §9. Not to be confused with MTN (Vail), MNTS (Momentus) or Schiehallion (LSE: MNTN).

Companion files:
- [`model/mntn_model.py`](model/mntn_model.py): the driver-based model.
- [`model/output/model_output.md`](model/output/model_output.md): full scenario tables, stress tests and sensitivities.
- `model/output/scenario_*.csv`: scenario data.

---

## 1. Bottom line

**Verdict: At Risk, bordering Neutral (~45–55% confidence).**
- No reported metric yet shows AI damage (Q2'26 revenue +21%, gross margin 80%, positive FCF [R]). The sharp slowdown in new-customer wins is unexplained.
- AI and the platforms are eroding what made MNTN special for small businesses: self-serve simplicity, cheap TV creative and its own measurement.
- What remains (premium private-marketplace supply packaged for small budgets, conversion-trained bidding) holds against startups but only partly against Amazon, Walmart or Google.

**Base case (55%), 2030** [E]: revenue **~$580M** (growth slowing to ~10%); adjusted EBITDA **~$182M** (31.5%); GAAP EPS **~$1.36** (adjusted ~$1.76).

**What the price implies.** ~$10.25 prices **FY27–30 revenue growth of ~1–3.5% a year at ~28–30% margins**. That sits between our bear (~$6) and base (~$14–15) values: an implied bear-vs-base weight of ~45–55%, against our 35%. Probability-weighted value: **~$13–14.5** [E].

---

## 2. How MNTN makes money (Part 1)

### 2.1 What it charges for, and how revenue is booked
- **Pricing: one bundled price on a dynamic CPM.** MNTN charges no separate tech or data fees and "keeps a share of your media spend". In its own words: "we don't disclose our margin" [R, help center, Feb 9, 2026] (S26). The CEO describes it as "one cost to using MNTN, which is the cost of media" [R\*] (S20).
- **Revenue is booked net; MNTN acts as an agent.** The 10-K: the company "does not act as the principal… reports revenue… on a net basis which represents gross billings net of amounts it pays suppliers for the cost of advertising inventory" [R] (S1). Two consequences:
  - Media cost appears in neither revenue nor cost of revenue.
  - The **~80% gross margin is a margin on MNTN's fee**. It is not comparable with companies that book revenue gross.
- **Cost of revenue** [R] (S1):
  - hosting and data;
  - third-party platform fees (MNTN "relies on multiple vendors to serve as its demand-side platform");
  - platform-support and video-production staff;
  - amortization of capitalized software ($7.1M in FY25).
  
  Card-processing fees sit in G&A.
- **Take rate (net revenue as a share of gross media billings)** is **not disclosed**:
  - Our estimates from receivables and payables run **~35–60%, central ~45%** [E].
  - Quo Vadis estimated ~40% for FY24 [3P] (S42).
  - The Trade Desk's take rate was 21.6% in FY25 [E from R] (S71).
  - Sensitivity: each point of take rate is worth **~2.0–2.5% of revenue** and **~1.5–1.8 points of adjusted EBITDA margin** (at 50% / 40% take rates) before any cost response [E].
- **Creative revenue is ~1% of revenue.** That includes the QuickFrame human-creator marketplace and creative credits (FY25 ≈ $2.8M) [E].
  - QuickFrame AI is "free right now" per the CEO [R\*] (S20). quickframe.com, however, lists $39/$99/$250 monthly tiers after a free first video [R, company website] (S32).
  - Q1'26 included **$1.7M of breakage** from expired creative credits on amended contracts [R] (S4). We treat it as one-off [E].
- **Product tiers:** Express for small businesses (launched Apr 1, 2026), Pro for mid-sized businesses (with "agentic AI"), and Premium for upper mid-market, including live sports [R\*] (S20).
- **Contracts:** "almost all of our customers are not subject to committed contracts" [R] (S1).
- **Segment:** one segment, US only [R].

### 2.2 Customers: mix, retention, cohorts, concentration
| Item | What is disclosed |
|---|---|
| First-time TV advertisers | ~95% had never advertised on CTV [R, 10-K]; 97% of brands launched in 2025 had never advertised on TV [R, Q2'25 release] (S11). This pre-dates QuickFrame AI. |
| Size mix | SMBs were ~92% of FY24 Performance TV (PTV) revenue [R] (S2). Small businesses were ~6% of revenue (FY24) → 12% (Q1'25) [R] → **~15% (Q3'25)** [3P, CEO via AdExchanger] (S40). The 424B4 wording is ambiguous: mid-sized was either 79% or 86% of PTV. |
| Spend levels | Small businesses spend "~$15K a year"; the top of mid-market spends "deep six figures" [R\*, Canaccord, Aug 11, 2026] (S24). It is not stated whether these are gross or net figures. Customers with >$100K of net revenue: 297 (FY23) and 421 (FY24); not updated since [R] (S2). |
| Retention | Last true net revenue retention: **SMB NRR 108% (FY24) and 111% (Q1'25)** [R] (S2). Since the IPO the company gives only an undefined, survivor-only "expansion rate **well north of 115%**" [R\*] (S20, S22). **No gross churn, logo retention, cohort charts or trial-conversion data have ever been disclosed** [R, by absence]. |
| Concentration | Top-10 customers: ~17% of FY25 revenue and ~20% of 1H26. No customer above 10% [R] (S1, S3). |
| Agencies | ">90%" of advertisers use no agency [R\*]. Agency-led accounts grew ~4x in 2025 [R] (S37). |

### 2.3 Revenue per customer: why customers grow about twice as fast as revenue

| Quarter | TTM active PTV customers [R] | TTM y/y [E] | Customers active **in the quarter**, y/y [R; quarterly window inferred: the 10-Qs say "between the periods in comparison"] | Revenue ex-ME y/y [R] | TTM revenue ex-ME / TTM customer [E] | y/y [E] | Spend per in-quarter active customer, y/y [E] |
|---|---|---|---|---|---|---|---|
| Q4'24 | 2,225 | +56% | n/d | n/d (GAAP ≈+34% [E]) | $94.1K | — | — |
| Q1'25 | 2,647 | +68% | +88.6% | +46% | $86.1K | — | ≈ −22% |
| Q2'25 | 3,020 | +73% | +85% | +34% | $81.2K | — | ≈ −27% |
| Q3'25 | 3,316 | +67% | +67% | +31% | $79.0K | — | ≈ −22% |
| Q4'25 | 3,632 | +63% | n/d | +36% | $78.4K | −16.7% | — |
| Q1'26 | 3,874 | +46% | +26% | +25% (≈+22% excluding $1.7M breakage) | $77.3K | −10.3% | ≈ −1% (≈ −3% excluding breakage) |
| Q2'26 | 4,225 | +40% | **+24%** | **+21%** | **$74.2K** | **−8.7%** | **≈ −2.5% to −3%** |

*Math:*
- TTM revenue excluding Maximum Effort (ex-ME) rolls forward quarterly. For example, Q2'26 = $299.3M − $68.5M + $82.5M = $313.3M, and $313.3M ÷ 4,225 = $74.2K.
- Spend per in-quarter active customer ≈ (1 + revenue growth) ÷ (1 + in-quarter active growth) − 1.
- Sources: S3–S11 and S2.

**Diagnosis:**
- **2025: a deliberate move to smaller customers.** Spend per active customer fell 21–27% while customers active in the quarter grew 67–89%. Every 10-Q gives the same cause: "a decrease in average spend per customer as we continued to expand our overall SMB footprint, including small businesses" [R] (S3).
- **2026: the gap mostly reflects the lagging TTM count, behind which customer wins have slowed sharply.**
  - The headline count is trailing-twelve-month (TTM). It includes paid-trial customers (trials of ≤3 months) and anyone active at any point in the past year [R] (S3), so it lags.
  - Customers active in the quarter grew only +24%, and spend per active customer fell only ~3%.
  - About 16 of the 19-point gap between customer growth (+40%) and revenue growth (+21%) is the lag between the TTM count and in-quarter customers [E]. That is arithmetic, not proof of cause, and it largely reflects the real slowdown below.
  - **The real story is customer acquisition slowing: from +85% to +24% in-quarter growth.**
- **Pricing pressure is not proven, but cannot be ruled out without a take-rate disclosure.** Every proxy is flat or better:
  - Gross margin 80% [R].
  - The allowance for concessions was flat: $2.50M (2024) and $2.65M (2025) [R].
  - Receivables per dollar of quarterly revenue fell from 0.90 (Q2'25, like-for-like) to 0.73 (Q2'26) [E] (S1, S3). Receivables are booked at gross billings, so a rising ratio would mean a lower take rate. A shift to card-paying SMBs could also explain the decline.

### 2.4 Supply: where the TV inventory comes from, and who controls access
- **How it buys.** CEO: "over 99% private marketplace deals" [R\*] (S20), with no open-market buying (S41). The 10-K describes "negotiated arrangements directly with premium TV networks and SSPs" [R] (S1).
  - Named supply-side platforms (SSPs): **PubMatic** (Paramount, NBCU, Sling, Philo, LG Channels) and **Magnite** (Disney live inventory, pause ads, home-screen units) [R] (S38, S39).
  - Premium content: NBCU/Peacock/Telemundo (World Cup), WBD/HBO Max, Paramount, Fox, Disney/ESPN, and sports packages [R\*].
  - MNTN **rents its DSP layer from "multiple vendors"** [R] (S1).
- **What it cannot show access to:**
  - **No evidence of access to YouTube (14.2% of US TV time) or Prime Video (4.3%)**. Together that is ~18.5% of TV time and ~38% of streaming [3P/E] (S95).
  - **Netflix is contested.** The CEO says buys "go across" Netflix [3P] (S41). Netflix's listed programmatic partners (Amazon DSP, TTD, DV360, Yahoo, Microsoft) do not include MNTN [R/3P] (S61). MNTN may still reach it through rented DSPs.
- **Who controls access.** The owners of streaming content and TV operating systems are consolidating and building their own front doors for small advertisers:
  - Paramount Skydance closed its acquisition of WBD on Oct 6, 2026 [R] (S68).
  - Fox is acquiring Roku (~$22B EV, closing 1H27) [R] (S60).
  - Amazon's DSP has privileged pipes into Roku (Amazon + Roku together reach ~80M US CTV households), Netflix and Disney [3P] (S121).
  - Paramount Ads Manager advertises CTV from a $7 CPM [3P, vendor claim] (S120).
- **Cost of inventory is falling:**
  - Average streaming upfront CPM: $25.90 vs $27.75 [3P] (S97).
  - Roku's price per impression fell 12% (affected by mix) [R] (S59).
  - Because revenue is net, CPM deflation does not hit MNTN's gross margin. Under dynamic CPM, MNTN can keep part of the decline as spread or pass it on as better returns for the advertiser.

### 2.5 Moat test: which candidate moats actually hold
| Candidate moat | Holds vs AI-native startups? | Holds vs walled gardens and AI agents? | Evidence |
|---|---|---|---|
| **Proprietary conversion data** | Partly | Partly / no | 81M conversions and ~565M verified visits, 2020–24 [R] (S2). Bidding trained on conversions ("intent scoring", ~120M households). Walmart and Amazon have larger, closed-loop *purchase* data. |
| **Attribution (Verified Visits)** | Weak | **No** | Household-level view-through credit within 7-day (retargeting) or 14-day (prospecting) windows, with modeled outcomes blended in [R] (S27). 10-K: "minimal patent protection"; no MRC accreditation [R] (S1). MNTN added 10% holdout incrementality tests and **8 third-party measurement integrations** (Haus, Northbeam, HubSpot, AppsFlyer, Upwave, etc.) [R] (S28). That makes measurement a level playing field rather than a moat. |
| **Integrations / partners** | No | **No** | HubSpot app: "100+ installs", 0 reviews [3P] (S33). Adobe's GenStudio documentation does not list MNTN as an activation channel [3P] (S92). The 8-K claims a QuickFrame *creative* integration, which is a different thing. The MCP server (lets AI agents operate the platform) is in beta [R] (S29). |
| **Ease of use (self-serve)** | Eroded | **No** | AI agents can now operate Amazon (Ads MCP, 700+ connections), Meta (read/write connectors), Universal Ads and Vibe (1,000+ brands via MCP) [3P] (S80, S81, S83). Ease of use is becoming an API call. |
| **Creative tools (QuickFrame AI)** | No: a funnel | **No** | Built entirely on third-party models. OpenAI removed the Sora API on 2026-09-24 (S91). The CEO calls the orchestration "table stakes" [R\*]. Google, Meta and Amazon give video generation away (S55). |
| **Brand** | Moderate | Weak | Inbound leads ~75% of pipeline [R\*]. But S&M is still ~35% of revenue [R], so the brand has not cut acquisition cost. |
| **Supply packaged for small budgets** | **Yes (strongest)** | Partly | >99% private-marketplace deals and live sports at budgets far below direct-deal minimums [R\*]. Not exclusive (runs through SSPs). Suppliers are consolidating and selling direct. |

**Net:** only (1) premium supply aggregated for small budgets and (2) conversion-trained bidding still hold. Both hold against startups; against the walled gardens they hold only partly. Attribution, ease of use and creative have become table stakes.

### 2.6 Growth: what is driving the slowdown, and how reliable is guidance
- **The numbers:**
  - FY25 revenue: $290.1M GAAP (+28.6%), or **$284.7M ex-ME (+36.0%)** [R] (S9).
  - FY26 guidance: **$347–357M** (~+24% ex-ME / ~+21% GAAP) and adj. EBITDA $96–101M [G] (S7).
  - Quarterly ex-ME growth: 46%, 34%, 31%, 36%, 25% (≈22% excluding the breakage), then **21% (Q2'26)** [R].
- **Drivers of the slowdown**, in order of evidence:
  1. **Customer acquisition slowed** (in-quarter active customers +85% → +24%). Management's explanation [R\*] (S20, S21):
     - The category is moving from "early adopter" to "mainstream", which needs a sales and marketing rebuild that started in Q4'25.
     - "We constantly adjust how much small business we drive… we also control product minimums."
  2. **Go-to-market churn** [R] (S3, S4):
     - 53 S&M hires in Q4'25, then an **Apr 28, 2026 restructuring of ~76 people**. Headcount went from 542 to 451, so about 15 more departures beyond the cuts.
     - **Marketing spend down $1.3M y/y in Q2'26**.
     - A **$10M/yr marketing contract paid in stock** to an unnamed contractor.
  3. **Tough comps**: Q1'25 grew +46%.
  4. **One-offs**: $1.7M of breakage flattered Q1'26.
  
  Management rules out macro ("nearly zero impact"), political ads and the World Cup [R\*]. **No disclosure attributes the slowdown to AI or walled gardens. None can rule that out either:** there are no win/loss, churn or take-rate disclosures.
- **Guidance track record** [R/G, E] (S7–S11):

| Quarter | Revenue guide ($M) | Actual ($M) | vs midpoint | vs high end | Adj. EBITDA vs midpoint |
|---|---|---|---|---|---|
| Q3'25 | 69.5–70.5 | 70.0 | 0.0% | −0.7% | +14% |
| Q4'25 | 85.5–86.5 | 87.1 | +1.3% | +0.7% | +10% |
| Q1'26 | 71.3–73.3 | 73.7 (≈72.0 excluding breakage) | +1.9% (−0.4% excluding breakage) | +0.5% | +21% |
| Q2'26 | 81.0–83.0 | 82.5 | +0.7% | −0.6% | +4.9% (below the high end) |
| Q3'26 | **86.0–89.0** (+23% to +27%) | due Nov 4 | | | |

- **Read: the guidance is accurate, not conservative.**
  - The average revenue beat vs midpoint is **+0.4%** excluding the breakage.
  - FY26 revenue guidance was raised only $2M (May 5) and then reiterated.
  - The midpoint needs **2H26 growth of ~24.6%**, against **~21% underlying in 1H26** [E]. Implied Q4'26 is ~$108M (+24%), with ~34% adj. EBITDA margin [E].

---

## 3. AI threats (Part 2)

**Likelihood scale:** probability the threat materially affects MNTN by 2030. "Impact" is versus a no-threat path. Threat impacts overlap, so they are **not additive**; the model stacks them through scenario probabilities (§6).

| # | Threat | Mechanism | Evidence **for** | Evidence **against** | Likelihood | Timing | Impact (revenue / margin) [E] |
|---|---|---|---|---|---|---|---|
| 1 | **Walled gardens automate SMB ads, including TV** | Amazon, Google/YouTube, Meta, Roku, Walmart, Comcast and Disney let an SMB plan, generate creative, buy and measure TV inside tools it already uses, using their own first-party data. New first-time TV advertisers default there. | **Amazon:** DSP "now part of Amazon Ads Agent"; "DVA+ brings… programmatic to all advertisers" (S51); free Creative Agent makes streaming-TV ads (Nov 2025) (S52); ads +26% y/y to $19.8B (S50); cross-publisher reach (Prime Video, Netflix, Disney, Roku). **YouTube:** 14.2% of TV time (S95); Demand Gen on TV screens, "SMBs continue to fuel our direct response growth" (S53, S54). **Others:** Roku Ads Manager advertisers >2x y/y (S58); Universal Ads has no minimum, an AI video tool and an MCP connector (S66, S67); Walmart bought Vibe (10,000+ advertisers) (S62). | Meta's Q2'26 call had **zero** TV mentions; CTV is only "exploratory" (S56, S57). Each garden mostly sells its *own* inventory. MNTN offers neutral cross-publisher premium supply (>99% PMP) plus attribution to the advertiser's own site and CRM. No reported metric yet shows damage (gross margin 80%, flat concessions, Q3 guided +23–27%), though the new-customer slowdown is unexplained. | **High (~80%)** that gardens capture most *new* SMB TV adopters by 2030. **~60%** that it materially damages MNTN by 2028–30 (share-shift 45% + severe 15%, dossier E). | Amazon and YouTube: now. Fox-Roku and Walmart-Vibe: 2027. Meta: tail risk, 2027+. | Revenue: probability-weighted ~**−15% to −16%** on 2030 revenue. Dossier E scenarios: $705M contained (40%), $553M share-shift (45%), $410M severe (15%). Margin: adj. EBITDA plateaus at ~28–32% in share-shift and falls to the low 20s if severe, vs the 35–40% target. |
| 2 | **Agentic buying** | Advertisers' AI agents (Claude, ChatGPT, Gemini, or CRM agents in HubSpot or Klaviyo) buy directly from publishers, SSPs and platforms through MCP/AdCP. MNTN's self-serve interface stops mattering; agents compare cost per acquisition across channels and push on price. | Amazon Ads MCP has 700+ connections (S81). Meta has read/write AI connectors (S83). TTD launched Koa agents (S82). Netflix is "testing AI agents to… purchase ads" (S122). Vibe says 1,000+ brands buy through its MCP, a "large portion" of spend (S80). MNTN's own MCP is beta-only, and "agentic" appears in none of its filings. | Autonomous agent-executed buying is **<1% of US CTV spend in 2026** [E]; TTD's agents did not buy autonomously as of May 2026 (S123). Agents need *tools* to call: supply packaged for small budgets, conversion-trained bidding, attribution, billing and credit. MNTN has a read/write MCP beta, a reporting API, and HubSpot and Klaviyo integrations (S29). It could become the "TV tool" agents call. | **Low (<10%)** before 2027. By 2028–30: **~55%** moderate pricing/relationship pressure, **~20%** severe (dossier F). | Pilots in 2026; pricing pressure 2027–28; material 2028–30. | Revenue: probability-weighted ~**−9%** on 2030 revenue (range −6.5% to −11%; scenarios +5–15% / −5–12% / −25–40%). Margin: each 1% of revenue lost to take-rate compression ≈ −3.6% of EBITDA; a 5% compression takes adj. EBITDA margin from ~28% to ~24% before cost flex. Upside if agents lower acquisition cost (S&M ~30% of revenue ex-SBC). |
| 3 | **Cheaper competition** (AI-native startups and established rivals) | AI coding and AI creative collapse the cost of a self-serve TV ad tool. Rivals undercut on minimums and price. | **Rivals and their entry points:** Vibe (now Walmart) at **$50/day**, no commitment, $15–35 simulator CPM (S65); Universal Ads with **no minimum** (S66); Adwave at $30/day (pre-seed AI-native startup); Paramount from a "$7 CPM"; Roku with a ~$500 start. Pinterest bought tvScientific for **$465.1M** (S64). **Share signals:** Northbeam tracked spend H1'26: **Vibe +1,900% vs MNTN +29%** [3P, chart published by Vibe] (S117); Tranco rank for mountain.com fell, for vibe.co it rose [3P] (S114). | What AI coding does **not** lower: premium private-marketplace supply, conversion data and credible measurement, customer acquisition (S&M ~35% of revenue), and fraud and brand-safety controls. AI-native startups (Adwave, Olyzon, etc.) have trivial traction. The serious rivals (Vibe, tvScientific) were **bought by platforms**, leaving MNTN as the last scaled independent. AppLovin calls CTV "step three" (S72). | **Low (~10%)** from AI-native startups. **Medium-High (~50–60%)** from platform-owned rivals (Walmart-Vibe, Pinterest-tvScientific, Universal Ads, Roku/Fox); overlaps threat 1. | Now–2028. | Revenue: inside threat 1's −15–16%, not additive. Base growth fades to mid-teens by 2028; bear high-single-digit (dossier G). Margin: 0–3 take-rate points ≈ 0 to −4.5 pts of adj. EBITDA margin; S&M stays ~30–35% of revenue. |
| 4 | **Fee / take-rate pressure** | MNTN's undisclosed spread (~35–60% [E]) is roughly twice TTD's ~21.6%. Agents and fee-transparent platforms expose it. MNTN's agency push brings buyers who expect transparency. | Amazon DSP reportedly charges **0% on its own programmatic-guaranteed inventory and ~1% on open web** [3P] (S87). Google Buyer Direct caps fees at ~10% [3P] (S88). A PubMatic agentic CTV campaign ran **18% below target CPM** [R, PubMatic, 2026-08-06] (S74). TTD Q2'26 +3% and Q3 guide ≥ −12% (S69). FTC sued Amazon (Aug 2026) over opaque SMB auction pricing [3P] (S89). | **Not visible at MNTN:** gross margin 72% → 80% [R]; concessions flat <1% of revenue [R]; receivables per $ of revenue 0.90 → 0.73 like-for-like (consistent with no compression; confounded by payment mix) [E]. SMB buyers judge on ROAS, not fee %. Top-10 customers are only ~20% of revenue, so there is no holding-company leverage. TTD's slowdown is mainly lower spend from existing clients, not a disclosed take-rate cut (S70). CPM deflation gives MNTN room to keep its spread. | ≥2 points of compression: **15–25% by end-2027, 45–55% by 2030**. Severe (5–10 points): 20–25%. | Mostly 2027–30. | Revenue: probability-weighted ~**−5.5%** of 2030 revenue (range ~−3% to −8%). Margin: **−2 to −5 points** of adj. EBITDA after partial cost flex. A 5-point cut ≈ −10% revenue and ≈ −$2.7 a share (stress test, §6.10). |
| 5 | **Creative commoditization** | Free or near-free generative video (Veo, Sora, Runway, Firefly, Kling, Seedance) lets anyone make a TV-grade spot. QuickFrame AI stops differentiating MNTN. | Google lists Veo 3.1 at **$0.08–0.40 per second** with audio, so a 30-second take costs **$2.40–12** and a finished spot ~$24–600 [3P/E] (S90). Runway: $15/$35/$95 a month; Adobe Firefly: $9.99–199.99 a month, ~$0.10/s [3P] (S93). Google, Meta (9M+ SMBs using its AI creative tools) (S56) and Amazon bundle generation **free**. QuickFrame AI runs only on third-party models (OpenAI removed the Sora API, S91; Seedance faces Disney/MPA demands, S94). | MNTN's human creative revenue is **~1% of revenue**, so direct revenue exposure is tiny. QuickFrame AI is a full workflow: 15/30-second TV spots, spec and quality checks, one-click publishing to Performance TV. **73K+ signups in 1H26** [R\*]; used by "nearly all" Express customers and 30–40% of mid-market [R\*] (S24). | **High (~80%)** that creative is commoditized. | 2026–28. | Revenue: direct exposure negligible (human creative ~1% of revenue). Indirect exposure **moderate**: lower switching costs to Amazon, Roku and YouTube, worth −1 to −3 pts of growth a year from 2027 in the bear (dossier I). Margin: ~0 now ("essentially gross margin neutral"); turns negative if free QuickFrame AI usage scales, and where inference cost is booked is undisclosed. QuickFrame AI is a **funnel, not a moat**: a 12–24-month integration edge. |
| 6 | **Budget migration to AI assistants and AI search ads** | SMB test budgets go to ChatGPT, Google AI Mode, Copilot and Rufus ads instead of trying TV. Agentic checkout could also claim the conversion credit that CTV's measured ROAS depends on. | ChatGPT ads hit a **$1B annualized run-rate in <200 days**, with "tens of thousands of advertisers" and a self-serve Ads Manager with CPC bidding [R/3P] (S101, S102). eMarketer: US AI-search ads ~$1B (2025) → ~$26B (2029) [3P] (S103). MNTN's 10-K says it targets "marketers currently using paid search and social" (S1), the same wallet. | Forecasters expect the money to come mainly from search and e-commerce budgets (WPP) [3P] (S104). Incumbent pools are still growing: Google Search +17%, Meta ads +27%, US streaming TV +21.5% (2026) (S53, S100). Perplexity has exited ads [3P] (S124). | **Medium (~40–50%)** for some reallocation of SMB test budgets by 2030; **low** near term. | 2027–30. | Revenue: growth drag **0 to −1 point a year** (base), **−2 to −3 points** (bear). It could be larger, because MNTN's budgets come from search and social. Margin: not quantified (data gap); would show as higher acquisition cost (lower incremental revenue per S&M dollar). |

**Why would an SMB still use MNTN rather than let Amazon, Google or Meta allocate its budget?** (Part 2, threat 1)
1. **One buy across most named premium US networks and live sports** (Disney, NBCU, Paramount/WBD, Fox and others), which no single garden other than Amazon can match. YouTube and Prime Video are gaps in MNTN's own reach, and Netflix access is contested.
2. **Attribution to the advertiser's own website and CRM**: exportable to ~11 third-party attribution tools, with 8 measurement integrations added since Oct 2025. It is also a referee independent of the platform already running the SMB's search and social.
3. **Packaging for SMBs**: low (undisclosed) minimums, creative included, set-up in minutes.

These advantages are **strongest for mid-market DTC brands that don't sell on Amazon** (mid-sized customers are ~78–86% of PTV revenue; the non-Amazon DTC share is undisclosed). They are **weakest for micro-SMBs and Amazon or Walmart sellers**, which is exactly where MNTN is now pushing growth (Express).

---

## 4. AI upside (Part 3)

| # | Upside | Mechanism | Evidence **for** | Evidence **against** | Likelihood | Timing | Impact (revenue / margin) [E] |
|---|---|---|---|---|---|---|---|
| 1 | **Market expansion** (AI collapses TV production cost) | A TV spot used to cost $10K–$500K and take weeks [3P, low confidence]; now it costs ~$24–600 and takes minutes. The SMBs that never ran TV, ~95% of MNTN's customers, become addressable. | QuickFrame AI: **37K signups in Q2'26; >73K in 1H26** [R\*] (S20). Express: **>7,000 signups in 120 days; "hundreds" paying** [R\*]. Share of smaller advertisers investing in CTV rose from 60% (2024) to 85% (2026) [3P, IAB via The Current] (S125). | **QuickFrame AI signup-to-paying conversion is not disclosed.** Net TTM adds of +593 in 1H26 are ~0.8% of 73K signups. Allowing for churned trials (~1,000–2,000 gross adds), conversion is ≤~1.4–2.7% [E] (I). Many users are "creators… not necessarily the marketers" [R\*]. Express converts ~3–10% [E]. The 95% first-time-TV statistic pre-dates the AI launch. TTM net adds did **not** accelerate after it: 316 / 242 / 351 vs 422 / 373 / 296 before [E from R]. +351 in Q2'26 was a sequential pickup from +242. | **Medium-High (~65%)** for more advertisers. **~45%** that revenue growth re-accelerates above 25%. | 2026–28. | Revenue: base +1–3 pts of growth in 2027–28 from Express (in the base); bull +2–5 pts from 2027. Margin: ~neutral now; negative if free AI usage scales without converting. |
| 2 | **Better results → higher spend per customer** | AI targeting (MNTN Matched, intent scoring), AI media planning and "agentic" optimization raise ROAS, so advertisers scale budgets. | Intent-scoring rollout: **+44% ROAS** (company estimate from a "controlled rollout") (S30). Northbeam beta (n=32): ~1.8x marketing efficiency ratio [R, company press release] (S36). Survivor "expansion rate" >115% [R\*]. Spend per in-quarter active customer has stabilized at ≈ −3% y/y (from −22% to −27% in 2025) [E]. | All lift claims are **self-reported and inconsistent** across MNTN's own pages (Matched: "2–7x traffic", "2–3x ROAS"). No independent lift study. No NRR since Q1'25. Top-10 share is rising (17% → 20%), so the long tail is not scaling faster. | **Medium (~50–60%)** that results improve; **low-medium** that it shows in revenue per customer. | 2026–28. | Revenue: each +1 pt of spend per active customer ≈ +1% revenue. Bull assumes mid-market revenue per customer +4–4.5% a year vs base +1.5–3.5%. Margin: positive (no added cost of revenue). Would show as spend per active customer ≥0% and NRR ≥110%. |
| 3 | **Margins** (AI lowers MNTN's own costs) | AI-native engineering, AI support deflection, automated creative operations and ad ops. | Headcount **472 → 451** y/y while revenue +21% and TTM customers +40% [R]. Cost-of-revenue headcount **−38%** [R] (S3). Revenue per FTE ~$627–695K, up from $519K [E]. Job postings target "AI deflection" and "agentic workflows" (S35). | AI is currently a **net cost**: **T&D +52% y/y** (19.8% of revenue vs 15.7%) on +13% T&D headcount [R]. The gross-margin gain (77% → 80%) came from revenue leverage, platform fees and the restructuring, **not AI** [R, 10-Q bridge]. QuickFrame AI is "essentially gross margin neutral" [R\*]. No engineering, productivity or support-cost metrics are disclosed. | **Medium (~30–50%)** that AI drives structural operating leverage beyond normal scale. | 2027–30. | Revenue: none. Margin: base T&D cash 18% → 17% of revenue by 2030; bull → 15%, adding ~2–4 points to the 2030 margin. |
| 4 | **Distribution** (Adobe, Google, HubSpot make MNTN the default TV channel in AI workflows) | MNTN becomes the TV "activation" inside creative suites, CRMs and agent ecosystems, lowering CAC. | 8-K: "Adobe integrating QuickFrame AI into GenStudio"; Google named QuickFrame AI an "early adopter" of Gemini Omni Flash [R] (S7). HubSpot (Jun 2026), Klaviyo (Sep 2026) and AppsFlyer integrations; MCP beta usable from Claude and ChatGPT (S29). | Adobe's own documentation shows a **native "GenStudio for CTV"** builder and an activation list with **no MNTN** (S92). HubSpot app: 100+ installs, 0 reviews (S33). Google recognition is a model-supplier relationship, not distribution. **Vibe launched a read/write MCP first.** No usage disclosed. | **Low (~25%)**. | 2027–29. | Revenue: faster customer adds (bull only). Margin: if real, S&M down 3–5 points by 2030 (bull case only). |
| 5 | **Data flywheel** | More advertisers produce more conversion data, which improves bidding, results and spend, which brings more advertisers. New entrants can't copy this. | 81M conversions and ~565M verified visits (2020–24); household graph covering ~99% of US CTV households [R/claim] (S2). Bidding trained on conversions. 4,225 active advertisers. | "Minimal patent protection"; no MRC accreditation (S1). Some training data is licensed. **No evidence that performance improves as data grows.** Walmart, Amazon and Pinterest have far larger closed-loop data. | **Medium (~50%)** against startups; **Low** against walled gardens. | Ongoing. | Revenue: supports a stable take rate and revenue per customer (each take-rate point ≈ 2–2.5% of revenue); no stand-alone bull case. Margin: protects ~1.5–1.8 pts per take-rate point. |

**Net of Parts 2–3:**
- **MNTN's recent cost gains came from operating leverage and the restructuring, not demonstrably from AI.** These are revenue per employee and gross margin at the top of its 75–80% target range. AI is so far a net cost (T&D +52%).
- **AI's revenue-side benefits are unproven**: QuickFrame AI earns ~$0, and Express is <3% of revenue (~$3–10M annualized [E]).
- **The threats are mostly 2027–30 and aimed at pricing and at who owns the customer relationship.** They are not visible in reported numbers yet, and they are not existential.

---

## 5. Verdict and analog comparison (Part 4)

### 5.1 Placement

| AI Victim | **At Risk** | Neutral | Beneficiary | AI Winner |
|---|---|---|---|---|
| 13% | **45%** ◀ | 32% | 9% | 1% |

**Verdict: At Risk, bordering Neutral. Confidence ~45–55%.** Across the panel, 45% is on At Risk, 58% on At Risk or worse, and 77% on At Risk or Neutral.

The distribution averages three independent judge agents, each given the same verified evidence pack but a different lens:
- **Competitive strategy (7 Powers):** At Risk, −1.
- **Unit economics:** Neutral, −0.2.
- **Ad-tech practitioner:** At Risk, −1.

Each judge put ~55% on its own modal bucket; averaged, At Risk gets 45% vs Neutral 32%. The financial lens is less negative because **no reported metric yet shows AI or walled-garden damage**.

- **Why not Neutral:**
  - MNTN's original edge was counter-positioning: serving SMBs that agencies and enterprise DSPs couldn't profitably reach.
  - AI removed that constraint for the platforms. Creative, campaign setup and measurement now come free inside Amazon, Google, Walmart-Vibe, Universal Ads and Roku.
  - The slowdown is in **winning new customers** (in-quarter active +85% → +24%), exactly where platform defaults bite.
  - The opaque ~35–60% spread is the obvious target for fee-transparent rivals and agents.
- **Why not AI Victim:**
  - Gross margin, concessions and receivables are flat or better, and spend per active customer is down only ~3%.
  - Q3 is guided to re-accelerate.
  - Customers are fragmented SMBs, not holding companies.
  - Premium private-marketplace supply packaged for small budgets cannot be created by AI.
  - FCF is ~$60M TTM and net cash $237M.

### 5.2 Analogs

| Analog | 2026 YTD / multiple [3P/E] | What MNTN shares | Where MNTN differs |
|---|---|---|---|
| **AppLovin** (the AI winner) | −59% YTD; Q2'26 revenue +53%, 84% adj. EBITDA margin; ~11.5x NTM EBITDA (S72) | Outcome-based ML bidder; self-serve Ads Manager aimed at mid-market performance advertisers | AppLovin **owns its supply** (MAX mediation) and signal. MNTN rents its DSP layer and every generative model. AppLovin calls CTV "step three… not at the point yet where we can go execute on it" (S72), so it is a future entrant, not a 2027 one. MNTN is not on AppLovin's path: its AI gains are on cost, not on a proprietary model compounding revenue. |
| **The Trade Desk** (squeezed by bigger platforms) | −65% YTD; Q2'26 +3%, Q3 guide ≥ −12%; ~6x NTM EBITDA; ~15% staff cut (S69, S70) | Independent buyer with no owned inventory, paid by take rate; exposed to Amazon's reported 0–1% DSP fees and to agents | MNTN's customers are SMBs, not holding companies, so no agency joint-business-plan discounts. MNTN still grows ~21%. But its spread is **~2x TTD's**, so the same squeeze would hurt more. **This is the closest template, running perhaps 2–3 years behind.** |
| **Roku** | +43% YTD (Fox bid $160); platform +25%; Ads Manager advertisers >2x (S58, S60) | SMB self-serve TV advertising | Roku **owns the home screen and OS data**. After Fox closes it is both a supplier and a competitor. MNTN owns no supply. |
| **Magnite / PubMatic** | +48% / +100% YTD; Magnite CTV ex-TAC +36%; PubMatic mid-market DSP spend +25% (S73, S74) | The same premium CTV supply; MNTN brings them *new* demand (PubMatic: +14% unique advertisers) | They are paid whichever buyer wins and are building seller-side agents. In 2026 the market **rewarded the sell side and punished the buy side**, and MNTN sits on the buy side. |
| **Criteo** (the AI-victim floor) | −24% YTD; ex-TAC −13%; ~1.5x NTM EBITDA (S75) | Performance intermediary on rented inventory | Criteo is shrinking; MNTN is not. It shows where the multiple goes if growth turns negative. |
| **Pinterest–tvScientific / Walmart–Vibe** (closest product analogs) | $465.1M (~8–9x estimated net revenue) / ~$1.2B + ~$180M retention (~12x a stale, undefined, likely gross-spend "$100M ARR" claim, so not comparable to net-revenue multiples) (S63, S64) | Self-serve performance CTV for SMBs | Both were **absorbed by owners of first-party data**. Strategic buyers paid ~2.3–2.6x MNTN's whole EV for Vibe. That supports a valuation floor and takeout optionality; Class B holds ~66% of votes, so any deal must be friendly. |

### 5.3 What would move the verdict over the next 4–8 quarters
**Up one notch, to Neutral** (needs ≥3 of these):
- In-quarter active customers ≥ +30% y/y with spend per active customer ≥ −3%, and TTM net adds ≥450 a quarter.
- An FY27 guide midpoint ≥ $425M (consensus $417.3M) (S109).
- A disclosed take rate or gross billings that hold flat; gross margin ≥78%; concessions <1% of revenue.
- Disclosed agent/MCP-sourced spend, or QuickFrame-to-paid conversion ≥3%, or Adobe or Google naming MNTN an activation partner.
- Confirmed Netflix or Prime Video access, or NFL guaranteed access live. Fox-Roku and Paramount-WBD keep MNTN's private-marketplace terms after closing.

**Down one notch, to AI Victim** (needs ≥2 of these):
- Revenue growth <15% for two quarters, or in-quarter active customer growth <15%.
- Gross margin <76% for two quarters, disclosed rebates or volume discounts, or a switch to transparent fee pricing.
- A major supplier (Fox-Roku or Paramount-WBD) routing SMB demand to its own self-serve tool, or MNTN losing an SSP or network.
- Meta launching CTV audience extension (via Magnite or FreeWheel), Amazon disclosing SMB streaming-TV adoption at scale, or Walmart-Vibe keeping $50/day pricing as its MCP scales.
- S&M >35% of revenue while incremental revenue per S&M dollar falls below 0.6x (now 0.72x [E]).

---

## 6. Financial model, 2025A–2030E (Part 5)

### 6.1 Structure and key assumptions
The model lives in [`model/mntn_model.py`](model/mntn_model.py); all figures are [E] unless tagged. It was red-teamed by an independent agent, and the corrections (milder bear, lower base margins, higher cash taxes, more bull dilution, consistent DCF) are incorporated.

- **Revenue = Σ over customer-size segments of (TTM active customers × net revenue per TTM customer) + creative services + QuickFrame AI monetization.**
  - The segments follow MNTN's own size definitions: small business (including Express); mid-sized; and larger / upper mid-market (≈ the Premium tier).
  - MNTN discloses only the *total* customer count and the small-business revenue share, so the FY25 split is calibrated [E]:
    - small ~2,600 customers × ~$15.2K;
    - mid-sized ~970 × ~$227K;
    - larger / upper mid-market (≈ the Premium tier) ~62 × ~$365K.
  - That reproduces $281.9M of PTV revenue with ~14% from small business.
  - Segment averages are means over a highly skewed distribution: the top-10 customers are ~17% of revenue.
- **Costs are modeled on a cash basis** (excluding SBC and D&A). GAAP lines are rebuilt by adding SBC by function and amortization (capitalized software in cost of revenue, per the 10-K schedule $7.5M / $6.2M / $3.6M / $0.5M for 2026–29, plus new vintages; acquired intangibles $2.6M a year).
- **Taxes** (§6.4): book rate 26%; cash tax 7% / 22% / 25% / 26% / 26%.
- **Share count** (§6.5): 74.8M basic plus dilution; buybacks as authorized.
- **FCF** = operating cash flow − capitalized software. Working capital drains 22% of each incremental revenue dollar, calibrated to FY25–1H26 operating-cash-flow conversion of 79–81%.
- **Other assumptions:**
  - Interest yield on cash: 3.5% (2026), falling to 3.0%.
  - Capitalized software: 4.3% of revenue, 3-year life.
  - At least $75M of cash is kept (revolver deposit covenant).
  - One-off add-backs: $1.9M in 2026, ~$0.5M a year after.
- **New products are modeled implicitly; MNTN discloses no economics for them.**
  - Express sits in the small-business segment, which grows from ~$40M (FY25) to $89M (FY30) in the base. Most of the increment is Express-type customers at ~$12–15K of net revenue each.
  - Premium sits in the larger / upper mid-market segment: ~$23M → $59M.
  - QuickFrame AI subscriptions are a separate line: $0 bear / $3M base / $18M bull by FY30.

| Driver | Bear (30%): "AI Victim" | Base (55%): "At Risk / Neutral" | Bull (15%): "AI Winner" |
|---|---|---|---|
| Narrative | Platforms and agents take the *new* SMB TV demand; Express stalls; take rate resets from 2028; mild 2027 SMB slowdown | In-quarter customer growth decays from 24% toward ~10%; spend per customer roughly flat. Cash cost of revenue rises ~1.4 pts as a proxy for a ~1-pt take-rate give-back, with no revenue haircut | QuickFrame and Express funnel converts; MNTN is the neutral TV layer after rivals are absorbed; agents become a cheap acquisition channel |
| FY26 revenue / adj. EBITDA | $347.9M / $96.4M (guide low end) | $352.4M / $99.4M (≈ guide midpoint; consensus $352.3M) | $353.7M / $102.2M |
| Customer growth FY27→FY30 (small / mid / larger) | +4%→+2% / +6%→+5% / +5%→+5% (dips in FY28) | +24%→+10% / +13%→+7.5% / +20%→+11% | +33%→+18% / +16%→+14% / +28%→+21% |
| Revenue per customer FY27→FY30 | −6%→−2% / −1%→−1% / −1%→−1% | −3.5%→0% / +3.5%→+1.5% / +4%→+3% | −1%→+2% / +4.5%→+4% / +6% |
| QuickFrame AI revenue by FY30 | $0 | $3M | $18M |
| Revenue CAGR FY26–30 | +2.1% | +13.2% | +23.0% |
| Gross margin (GAAP) FY30 | 75.8% | 79.0% | 80.2% |
| S&M / T&D cash, % of revenue, FY30 | 28.0% / 18.5% | 25.5% / 17.1% | 22.5% / 15.0% |
| SBC, % of revenue | 7.6% → 8.5% | 7.5% → 6.0% | 7.5% → 5.2% |
| Adj. EBITDA margin FY30 | 21.8% | 31.5% | 38.5% |
| Buybacks | $20M (2026) + $50M (2027), then 25% of FCF | $25M + $75M (completes the $100M), then 40% of FCF | $25M + $75M, then 50% of FCF |
| Gross new shares a year / treasury add-on | 3.5M / 1–4M | 2.1M / 4.7–6.0M | 2.0M / 4.8–13M (performance options vest above $25.40) |
| Valuation multiples (NTM at end-2027) | 4.0x EBITDA / 0.8x sales / 8x P/E | 6.5x / 1.9x / 12x | 9.5x / 3.0x / 18x |

**How the probabilities tie to the verdict.** The judge panel averages Victim 13%, At Risk 45%, Neutral 32%, Beneficiary/Winner 10%. Mapping:
- **Bear (30%)** = Victim plus the worse third of At Risk.
- **Base (55%)** = the rest of At Risk plus most of Neutral.
- **Bull (15%)** = Beneficiary/Winner plus the best of Neutral.

Per the brief, the bear is labeled "AI Victim", but our panel puts only ~13% on an outright Victim outcome, so the bear also includes the worse part of At Risk. The bull likewise blends Beneficiary with a little AI Winner. The bear is deliberately *not* the −70% tail; that is pre-mortem #1 (§7.3), at ~10% probability. Probability-weighted 2030 revenue ($553M) sits inside the research's stacked threat range (~$530–570M): walled gardens −16%, plus the non-overlapping parts of agentic −9% and fees −5.5%.

### 6.2 Scenario outputs, FY2025A–FY2030E
FY2025A column notes:
- FY25 GAAP figures include IPO-related charges and the Q4'25 valuation-allowance release (§6.4).
- "Pro forma" per-share figures use ~79.7M shares.
- The FY25 segment split and FY25 adjusted EPS are [E].

**Bear (30%): AI Victim: platforms/agents capture new SMB TV demand, take rate resets from 2028, mild 2027 SMB slowdown**

| | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---|---|---|---|---|---|
| Revenue ($M) | 290.1 | 347.9 | 359.2 | 357.4 | 365.0 | 377.6 |
|   y/y growth | +28.6% (+36.0% ex-ME) | 19.9% | 3.2% | -0.5% | 2.1% | 3.5% |
|   small business / mid-sized / larger ($M) | ~39.5 / ~219.8 / ~22.6 | 51 / 265 / 28 | 50 / 279 / 29 | 46 / 281 / 29 | 44 / 289 / 30 | 44 / 301 / 31 |
| TTM active customers (year-end) | 3,632 | 4,778 | 4,992 | 4,881 | 4,933 | 5,072 |
| Net PTV revenue per TTM customer ($K) | 77.6 | 72.1 | 71.6 | 73.0 | 73.8 | 74.3 |
| Gross margin (GAAP) | 77.2% | 81.2% | 78.6% | 76.4% | 75.8% | 75.8% |
| T&D / S&M / G&A, % of revenue (GAAP incl. SBC) | 17.0% / 31.2% / 19.9% | 19.5% / 30.6% / 14.4% | 20.4% / 32.2% / 14.9% | 20.5% / 32.4% / 15.9% | 20.3% / 31.9% / 15.5% | 20.0% / 31.4% / 15.5% |
| SBC ($M) and % of revenue | 31.7 (10.9%) | 26.4 (7.6%) | 28.7 (8.0%) | 30.4 (8.5%) | 31.0 (8.5%) | 32.1 (8.5%) |
| Adj. EBITDA ($M) | 68.0 | 96.4 | 84.4 | 76.8 | 77.4 | 82.3 |
|   Adj. EBITDA margin | 23.4% | 27.7% | 23.5% | 21.5% | 21.2% | 21.8% |
| GAAP operating income ($M) | 24.0 | 55.1 | 37.0 | 24.2 | 26.5 | 31.1 |
| Interest income ($M) | 3.5 | 8.2 | 8.6 | 8.9 | 10.2 | 11.6 |
| Book tax / cash tax ($M) | (9.6) benefit / 2.7 | 16.5 / 4.4 | 11.8 / 10.0 | 8.6 / 8.3 | 9.6 / 9.6 | 11.1 / 11.1 |
| GAAP net income ($M) | (6.4) | 46.9 | 33.7 | 24.5 | 27.2 | 31.6 |
| Diluted shares, avg. (M) | 50.9 (79.7 in Q4) | 78.7 | 76.7 | 75.3 | 76.2 | 77.5 |
| **GAAP EPS** | ($0.13) [~$0.26 normalized] | $0.60 | $0.44 | $0.33 | $0.36 | $0.41 |
| **Adjusted EPS** (ours) | ~$0.60 pro forma | $0.90 | $0.77 | $0.69 | $0.70 | $0.75 |
| Free cash flow ($M) | 44.0 | 70.6 | 63.0 | 59.5 | 59.7 | 62.8 |
| **FCF per diluted share** | ~$0.55 pro forma | $0.90 | $0.82 | $0.79 | $0.78 | $0.81 |
| Buybacks ($M) / year-end cash ($M) | 0 / 210.2 | 20 / 261 | 50 / 274 | 15 / 318 | 15 / 363 | 16 / 410 |

**Base (55%): At Risk / Neutral: growth fades to ~10% by 2030; cost-side proxy for a modest take-rate give-back; margins short of the 35-40% target**

| | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---|---|---|---|---|---|
| Revenue ($M) | 290.1 | 352.4 | 414.4 | 470.4 | 526.5 | 578.5 |
|   y/y growth | +28.6% (+36.0% ex-ME) | 21.5% | 17.6% | 13.5% | 11.9% | 9.9% |
|   small business / mid-sized / larger ($M) | ~39.5 / ~219.8 / ~22.6 | 53 / 266 / 29 | 64 / 312 / 37 | 72 / 351 / 44 | 81 / 390 / 51 | 89 / 426 / 59 |
| TTM active customers (year-end) | 3,632 | 4,895 | 5,943 | 6,869 | 7,706 | 8,440 |
| Net PTV revenue per TTM customer ($K) | 77.6 | 71.3 | 69.3 | 68.1 | 67.8 | 68.0 |
| Gross margin (GAAP) | 77.2% | 81.3% | 80.3% | 79.5% | 79.2% | 79.0% |
| T&D / S&M / G&A, % of revenue (GAAP incl. SBC) | 17.0% / 31.2% / 19.9% | 19.4% / 30.5% / 14.2% | 19.2% / 29.7% / 12.8% | 18.9% / 29.1% / 12.0% | 18.5% / 28.5% / 11.3% | 18.2% / 27.9% / 11.3% |
| SBC ($M) and % of revenue | 31.7 (10.9%) | 26.4 (7.5%) | 28.2 (6.8%) | 30.6 (6.5%) | 33.2 (6.3%) | 34.7 (6.0%) |
| Adj. EBITDA ($M) | 68.0 | 99.4 | 120.2 | 141.1 | 163.2 | 182.2 |
|   Adj. EBITDA margin | 23.4% | 28.2% | 29.0% | 30.0% | 31.0% | 31.5% |
| GAAP operating income ($M) | 24.0 | 58.1 | 74.3 | 89.2 | 107.1 | 123.1 |
| Interest income ($M) | 3.5 | 8.2 | 8.3 | 8.7 | 10.5 | 12.5 |
| Book tax / cash tax ($M) | (9.6) benefit / 2.7 | 17.2 / 4.6 | 21.5 / 18.2 | 25.4 / 24.5 | 30.6 / 30.6 | 35.3 / 35.3 |
| GAAP net income ($M) | (6.4) | 49.0 | 61.1 | 72.4 | 87.0 | 100.4 |
| Diluted shares, avg. (M) | 50.9 (79.7 in Q4) | 78.6 | 76.4 | 74.5 | 74.2 | 73.7 |
| **GAAP EPS** | ($0.13) [~$0.26 normalized] | $0.62 | $0.80 | $0.97 | $1.17 | $1.36 |
| **Adjusted EPS** (ours) | ~$0.60 pro forma | $0.93 | $1.12 | $1.32 | $1.56 | $1.76 |
| Free cash flow ($M) | 44.0 | 72.2 | 78.3 | 92.3 | 107.6 | 122.7 |
| **FCF per diluted share** | ~$0.55 pro forma | $0.92 | $1.02 | $1.24 | $1.45 | $1.66 |
| Buybacks ($M) / year-end cash ($M) | 0 / 210.2 | 25 / 257 | 75 / 261 | 37 / 316 | 43 / 381 | 49 / 454 |

**Bull (15%): AI Winner: AI funnel converts, MNTN becomes the neutral TV layer for SMBs and their agents**

| | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---|---|---|---|---|---|
| Revenue ($M) | 290.1 | 353.7 | 438.7 | 545.0 | 671.4 | 808.3 |
|   y/y growth | +28.6% (+36.0% ex-ME) | 21.9% | 24.0% | 24.2% | 23.2% | 20.4% |
|   small business / mid-sized / larger ($M) | ~39.5 / ~219.8 / ~22.6 | 54 / 266 / 30 | 72 / 323 / 40 | 92 / 391 / 54 | 114 / 472 / 71 | 138 / 560 / 91 |
| TTM active customers (year-end) | 3,632 | 4,978 | 6,424 | 8,013 | 9,680 | 11,357 |
| Net PTV revenue per TTM customer ($K) | 77.6 | 70.4 | 67.7 | 67.0 | 67.9 | 69.4 |
| Gross margin (GAAP) | 77.2% | 81.4% | 80.7% | 80.4% | 80.4% | 80.2% |
| T&D / S&M / G&A, % of revenue (GAAP incl. SBC) | 17.0% / 31.2% / 19.9% | 19.1% / 30.3% / 14.0% | 18.4% / 28.6% / 12.1% | 17.5% / 27.2% / 10.9% | 16.6% / 25.8% / 10.0% | 15.9% / 24.6% / 9.7% |
| SBC ($M) and % of revenue | 31.7 (10.9%) | 26.5 (7.5%) | 29.0 (6.6%) | 33.2 (6.1%) | 37.6 (5.6%) | 42.0 (5.2%) |
| Adj. EBITDA ($M) | 68.0 | 102.2 | 139.1 | 187.5 | 247.7 | 311.2 |
|   Adj. EBITDA margin | 23.4% | 28.9% | 31.7% | 34.4% | 36.9% | 38.5% |
| GAAP operating income ($M) | 24.0 | 60.8 | 92.3 | 131.9 | 184.8 | 239.8 |
| Interest income ($M) | 3.5 | 8.2 | 8.5 | 9.0 | 11.0 | 13.6 |
| Book tax / cash tax ($M) | (9.6) benefit / 2.7 | 18.0 / 4.8 | 26.2 / 22.2 | 36.7 / 35.2 | 50.9 / 50.9 | 65.9 / 65.9 |
| GAAP net income ($M) | (6.4) | 51.1 | 74.6 | 104.3 | 144.9 | 187.5 |
| Diluted shares, avg. (M) | 50.9 (79.7 in Q4) | 78.7 | 78.7 | 79.0 | 80.1 | 80.7 |
| **GAAP EPS** | ($0.13) [~$0.26 normalized] | $0.65 | $0.95 | $1.32 | $1.81 | $2.32 |
| **Adjusted EPS** (ours) | ~$0.60 pro forma | $0.95 | $1.27 | $1.68 | $2.21 | $2.77 |
| Free cash flow ($M) | 44.0 | 74.5 | 87.3 | 113.9 | 150.7 | 193.5 |
| **FCF per diluted share** | ~$0.55 pro forma | $0.95 | $1.11 | $1.44 | $1.88 | $2.40 |
| Buybacks ($M) / year-end cash ($M) | 0 / 210.2 | 25 / 260 | 75 / 272 | 57 / 329 | 75 / 404 | 97 / 501 |



### 6.3 Requested deliverables and the probability-weighted result

| Metric | Scenario | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---|---|---|---|---|---|
| Revenue ($M) | Bear | 347.9 | 359.2 | 357.4 | 365.0 | 377.6 |
| Revenue ($M) | Base | 352.4 | 414.4 | 470.4 | 526.5 | 578.5 |
| Revenue ($M) | Bull | 353.7 | 438.7 | 545.0 | 671.4 | 808.3 |
| Revenue ($M) | **Prob.-weighted** | **351.3** | **401.5** | **447.7** | **499.8** | **552.7** |
| Adj. EBITDA ($M) | Bear | 96.4 | 84.4 | 76.8 | 77.4 | 82.3 |
| Adj. EBITDA ($M) | Base | 99.4 | 120.2 | 141.1 | 163.2 | 182.2 |
| Adj. EBITDA ($M) | Bull | 102.2 | 139.1 | 187.5 | 247.7 | 311.2 |
| Adj. EBITDA ($M) | **Prob.-weighted** | **98.9** | **112.3** | **128.8** | **150.1** | **171.6** |
| GAAP EPS | Bear | $0.60 | $0.44 | $0.33 | $0.36 | $0.41 |
| GAAP EPS | Base | $0.62 | $0.80 | $0.97 | $1.17 | $1.36 |
| GAAP EPS | Bull | $0.65 | $0.95 | $1.32 | $1.81 | $2.32 |
| GAAP EPS | **Prob.-weighted** | **$0.62** | **$0.71** | **$0.83** | **$1.02** | **$1.22** |
| Adjusted EPS | Bear | $0.90 | $0.77 | $0.69 | $0.70 | $0.75 |
| Adjusted EPS | Base | $0.93 | $1.12 | $1.32 | $1.56 | $1.76 |
| Adjusted EPS | Bull | $0.95 | $1.27 | $1.68 | $2.21 | $2.77 |
| Adjusted EPS | **Prob.-weighted** | **$0.92** | **$1.04** | **$1.19** | **$1.40** | **$1.61** |
| FCF / share | Bear | $0.90 | $0.82 | $0.79 | $0.78 | $0.81 |
| FCF / share | Base | $0.92 | $1.02 | $1.24 | $1.45 | $1.66 |
| FCF / share | Bull | $0.95 | $1.11 | $1.44 | $1.88 | $2.40 |
| FCF / share | **Prob.-weighted** | **$0.92** | **$0.98** | **$1.14** | **$1.32** | **$1.52** |

FY2026E–FY2030E revenue CAGR: Bear +2.1%, Base +13.2%, Bull +23.0%. FY2025–30 CAGR: +5.4% / +14.8% / +22.7%.

### 6.4 Taxes, NOLs and the valuation allowance: normalizing GAAP EPS
- **The valuation-allowance release has already happened, so do not model another one-off jump.**
  - The P&L release came **entirely in Q4'25**: a $9.2M Q4 tax benefit ($9.6M for FY25) [R] (S1, S5, S9). The allowance fell from $49.0M (YE24) to $0.7M partly because gross deferred tax assets also fell, from $52.8M to $21.0M [R].
  - Only $0.7M of allowance remains [R].
  - The 10-K: "it is more likely than not that it will realize the benefit of its deferred tax assets."
- **Normalizing the reported EPS:**
  - **Q4'25 diluted GAAP EPS of $0.43 falls to ~$0.23–0.24 at a normal tax rate** [E]: (25.3 × 0.74) ÷ 79.7M.
  - **FY25 GAAP EPS of −$0.13** is distorted three ways:
    - $43.5M of IPO-related non-operating charges: a $26.4M loss on debt extinguishment plus fair-value marks; the company calls $23.0M of it a "one-time charge… related to the IPO".
    - The tax benefit above.
    - A 50.9M-share average that is mostly pre-IPO.
    
    **Normalized FY25 GAAP EPS is ~$0.26** [E]: (operating income $24.0M + interest $3.5M) × 0.74 ÷ 79.7M.
  - **TTM GAAP EPS of $0.71** [R sum] **falls to ~$0.52 normalized** [E] (S110).
- **Tax attributes at YE25** [R] (S1):
  - Federal NOLs: $33.9M, of which $31.8M is indefinite-lived.
  - State NOLs: $49.8M.
  - R&D credit deferred tax asset: $3.7M.
  - All are already net of Section 382 limits.
  - OBBBA's restoration of R&E expensing turned 2025 into a *taxable loss*.
- **Book vs cash tax:**
  - Book tax rate is ~25.5–26.6% in 2026 [R] (S3).
  - Cash paid in 1H26 was only $0.7M, but the *current* provision was ~18% of pre-tax income; the payment lagged (taxes payable rose to $2.8M) [E from R].
  - Federal NOLs (~$7M of tax value) are largely consumed in 2026–27. We model cash tax at 7% (2026), 22% (2027) and 25–26% thereafter.
  - Any future one-offs would come from state-law conformity to OBBBA or uncertain-tax-position reversals ($2.0M expected within 12 months) [R], which are immaterial.

### 6.5 Share count: buybacks vs dilution
- **Starting point** [R] (S3, S12, S16):
  - 74.80M basic shares (61.89M Class A + 12.91M Class B, Jul 31, 2026); 78.64M Q2 diluted average.
  - Legally issued but excluded from the count: ~1.8–2.0M note-restricted shares, plus 1.57M Maximum Effort earnout shares contingent to Mar 2027.
  - ~14.6M time-based options at ~$9.0 weighted strike.
  - 7.27M CEO/COO performance options at $3.79, vesting only at price hurdles of **$25.40–$508**.
  - Plan reserve 11.7M plus 1.85M ESPP, with a **5% + 1% annual evergreen**; the board took the full amount for 2026.
- **Buyback:** $100M authorized Aug 3, 2026 through Aug 5, 2027. That is ~13% of shares at $10.25 and ~14% at $9.40.
  - **No execution disclosed yet.** The Q3 10-Q (~Nov 9–10) will show it.
  - The CEO's claim of "$100M of free cash flow" does not reconcile with reported 1H26 FCF of $27.0M [R] (S24).
- **Modeled diluted shares** (average, FY26 → FY30): Bear 78.7M → 77.5M; Base 78.6M → 73.7M; Bull 78.7M → 80.7M. In the bull case, the performance options and in-the-money options outweigh buybacks.
- **Without any buyback**, base FY30 GAAP EPS is **$1.18 instead of $1.36**. Gross dilution of ~2–3% a year (SBC at $10–16 a share) is otherwise unchecked.

### 6.6 Versus Wall Street consensus and management's long-term targets
| Metric | Our Base | Prob.-weighted | Consensus [C] (S109, S110) | Management [G/R\*] | Gap explained |
|---|---|---|---|---|---|
| FY26 revenue | $352.4M | $351.3M | **$352.3M** (10 analysts; $350.4–354.4M) | $347–357M | In line. History lands within ~0–2% of the guidance midpoint; 2H must accelerate to ~24.6%. |
| FY26 adj. EBITDA | $99.4M | $98.9M | No free consensus | $96–101M | In line. Q4 implied at ~34% margin. |
| FY27 revenue | $414.4M (+17.6%) | $401.5M | **$417.3M** (+18.5%; $401.5–427.0M) | Benefits to "contribute to stronger growth in the second half of the year and meaningfully in 2027 as the core business accelerates, complemented by new revenue streams from Express and Premium" [R\*] (S20) | Base ~1% below the Street: in-quarter active customers +24% and slowing, spend per active customer −3%, and Express is low revenue per customer. The probability-weighted figure is ~4% below because the Street carries no bear weight. We do not adopt management's implied acceleration above 2H26's ~24.6%: in-quarter active customers have slowed to +24%, S&M efficiency fell to 0.72x, and Express/Premium are <3% of revenue. |
| FY27 adj. EBITDA | $120.2M (29.0%) | $112.3M | ~$115–130M [E, backed out of Citizens' and Evercore's price targets] (S113) | — | Inside the range. |
| FY26 / FY27 EPS | GAAP $0.62 / $0.80; adjusted $0.93 / $1.12; **"Street-style" $1.02 / $1.26** | GAAP $0.62 / $0.71 | "Normalized" **$1.05 / $1.31** (2 analysts); MarketBeat $0.87 / $1.19 | MNTN reports **no** non-GAAP EPS | **Definitional, not a real gap.** The 2-analyst "normalized" series appears to add back all amortization; on that basis our base is $1.02 / $1.26. On GAAP, our FY26E $0.62 compares with TTM reported $0.71 (inflated by the tax benefit) and normalized ~$0.52. |
| FY28–30 | See §6.3 | | **No public consensus** (paywalled or none) | No multi-year revenue target; no investor day | — |
| Long-term gross margin | 79–81% | | — | **75–80%** [R\*] (S22) | Consistent; MNTN is already at the top. |
| Long-term adj. EBITDA margin | **31.5% (FY30)** | ~31% | — | **35–40%** [R\*] (S22) | **We are below management.** Base assumes (a) S&M stays ≥25% of revenue as platforms raise acquisition costs; (b) T&D stays ~17–18% to keep up in AI ("table stakes"); (c) cash cost of revenue drifting up ~1.4 pts (15.8% → 17.2%) as a proxy for a ~1-point take-rate give-back with partial cost flex. There is no revenue haircut; a full 1–3-point give-back would cut revenue 2–7.5% (see the §6.10 stress test). Only the bull case reaches the target (38.5%). |
| Long-term S&M | 27.9% GAAP (FY30) | | — | 25–30% of revenue [R\*; sources conflict] | Inside the range. |
| Price target | Prob.-weighted ~$13–14.5 today; ~$14.6–15.7 on a 12-month-forward basis | | Mean **$18.10** (median $18; $13–22; 9 Buy / 1 Hold) [C] (S110) | — | With zero bear weight (base and bull reweighted 79/21), our value would be ~$18–19, so our 30% bear weight explains essentially all of the gap to the Street. Street target multiples have already fallen from 23–25x to 10–15x EBITDA (S113). |

### 6.7 Reverse-engineering the current price
We use the same DCF engine as the scenarios:
- FCF after SBC (treating stock pay as a cash cost);
- 11% cost of equity;
- revenue growth fading to 3% by FY35;
- 81.0M shares (74.80M basic + 4.72M dilutive + ~1.5M probability-weighted of ~3.5M excluded shares);
- $237.3M cash.

| FY30 adj. EBITDA margin | FY27–30 revenue CAGR implied at **$10.25** | at $9.40 (prior close) | at 10% cost of equity | at 12% cost of equity |
|---|---|---|---|---|
| 22.0% | +14.1% | +10.7% | +10.5% | +17.6% |
| 25.0% | +8.0% | +4.7% | +4.7% | +11.1% |
| **28.0% (≈ FY26 guide; TTM 26%)** | **+3.5%** | +0.3% | +0.4% | +6.4% |
| **30.0%** | **+1.0%** | −2.1% | −1.9% | +3.8% |
| 32.5% | −1.6% | −4.7% | −4.4% | +1.0% |

**Read:**
- **The market is pricing ≈1–3.5% revenue growth a year at ~28–30% margins**, or low-teens growth only if margins fall to the low 20s. Compare:
  - consensus FY27 growth of +18.5%;
  - our base of +13% CAGR at a 31.5% margin;
  - our bear of +2% CAGR at a ~22% margin.
- Equivalently, **$10.25 implies a 45% (multiples) to 55% (DCF) bear-vs-base weight**, against our 35% (30 ÷ (30 + 55)). **The price sits between our bear (~$6) and base (~$14–15) values, closer to the bear than our weights imply.**
- Cross-checks:
  - EV ≈ $529M on basic shares (≈$593M on the 81.0M valuation count; ≈$466M at the $9.40 close) is **~5.4x (6.0x) FY26 adj. EBITDA guidance**, ~4.4x (4.9x) our FY27 base and ~1.3x NTM revenue [E].
  - TTM FCF is $59.6M (a 7.8% equity yield; 4.8% after SBC) [E].
  - A simpler Gordon-growth check on unlevered FCF implies perpetual FCF growth of **−0.4% to −2.2% before SBC**, or **+2.8% to +4.7% after SBC** [E, dossier K corrected].

### 6.8 Valuing each scenario with peer multiples
Method:
- Value at end-2027 on FY2028 (next-twelve-month) metrics, using end-2027 net cash and diluted shares.
- Discount to today at 11%.
- Cross-checks: a 2030 exit and a DCF.

| | Multiples applied, and the peer anchor | EV/EBITDA | EV/Sales | P/E (adj.) | Blend at end-2027 | **PV today** | 2030 exit PV | DCF |
|---|---|---|---|---|---|---|---|---|
| **Bear** | 4.0x / 0.8x / 8x: between Criteo (~1.5x) and TTD (~6x) | $7.55 | $7.27 | $5.51 | $6.77 | **$5.97** | $6.04 | **$6.49** |
| **Base** | 6.5x / 1.9x / 12x: below the peer median (~7.75x NTM EBITDA, ~2.15x NTM revenue) and the DV/IAS take-privates (8.1x / ~9x) | $15.53 | $15.22 | $15.90 | $15.55 | **$13.70** | $14.73 | **$14.85** |
| **Bull** | 9.5x / 3.0x / 18x: below AppLovin (~11.5x), near IAS (~9x) | $26.08 | $24.22 | $30.31 | $26.87 | **$23.68** | $30.25 | **$26.66** |
| **Prob.-weighted** (30/55/15) | | | | | $14.61 | **$12.88** | $14.45 | **$14.12** |

- **Peer and deal reference set** [3P/E] (S69–S79):
  - Peer median NTM EV/EBITDA ~7.75x: ZETA ~17x, APP ~11.5x, MGNI ~11x, PUBM ~8x, PINS ~7.6x, DSP (Viant) ~7.5x, TTD ~6x, CRTO ~1.5x.
  - Deals: Nielsen–DV ~8.1x TTM EBITDA; Novacap–IAS ~9x; Mediaocean–Innovid ~3.3x revenue; Pinterest–tvScientific ~8–9x net revenue; AppLovin–Wurl ~8x revenue; Walmart–Vibe ~12x a stale, likely gross-spend "ARR" claim (not comparable).
  - MNTN at ~4.4–5.4x (basic EV) sits **~30–43% below the peer median**.
- **Dispersion:** bear ~$6 vs bull ~$24–27. Probability-weighted ~**$13–14.5**, which is **+25% to +40%** versus $10.25 (+37% to +54% versus the $9.40 prior close).
- **Discount-rate sensitivity** (DCF):
  - 10%: Bear $6.93 / Base $16.61 / Bull $30.45.
  - 12%: Bear $6.14 / Base $13.49 / Bull $23.74.

### 6.9 Sensitivity: revenue growth vs EBITDA margin
**DCF value per share** by FY27–30 revenue CAGR (rows) and FY30 adj. EBITDA margin (columns). FY26 revenue is $352M; the margin moves from 28% to the column value by FY30. Today's price (~$10.25) sits around the **+0–5% growth / 28–30% margin** cells.

| Revenue CAGR FY27-30 \ FY30 margin | 20% | 25% | 30% | 35% | 40% |
|---|---|---|---|---|---|
| -5% (FY30 rev $287M) | $6.28 | $7.49 | $8.71 | $9.92 | $11.14 |
| +0% (FY30 rev $352M) | $6.78 | $8.37 | $9.96 | $11.54 | $13.13 |
| +5% (FY30 rev $428M) | $7.40 | $9.46 | $11.52 | $13.58 | $15.64 |
| +10% (FY30 rev $515M) | $8.17 | $10.83 | $13.48 | $16.13 | $18.78 |
| +15% (FY30 rev $616M) | $9.13 | $12.51 | $15.90 | $19.28 | $22.67 |
| +20% (FY30 rev $730M) | $10.29 | $14.59 | $18.88 | $23.18 | $27.47 |
| +25% (FY30 rev $859M) | $11.72 | $17.13 | $22.54 | $27.95 | $33.36 |

**Value per share at end-2027** (undiscounted) by EV/EBITDA multiple (rows) and FY28 adj. EBITDA (columns). Base-case end-2027 net cash is $261M; shares 75.9M. Our FY28 adj. EBITDA: Bear $77M, Base $141M, Bull $188M.

| EV/EBITDA \ FY28 adj. EBITDA ($M) | 70 | 90 | 110 | 140 | 170 | 200 |
|---|---|---|---|---|---|---|
| 3x | $6.20 | $6.99 | $7.79 | $8.97 | $10.16 | $11.34 |
| 4x | $7.13 | $8.18 | $9.24 | $10.82 | $12.40 | $13.98 |
| 5x | $8.05 | $9.37 | $10.69 | $12.66 | $14.64 | $16.62 |
| 6.5x | $9.43 | $11.15 | $12.86 | $15.43 | $18.00 | $20.57 |
| 8x | $10.82 | $12.93 | $15.04 | $18.20 | $21.36 | $24.53 |
| 9.5x | $12.20 | $14.71 | $17.21 | $20.97 | $24.72 | $28.48 |


### 6.10 Stress tests on the base case
| Stress | FY27 revenue | FY30 revenue | FY30 adj. EBITDA | FY30 GAAP EPS | FY30 FCF/share | DCF $/share |
|---|---|---|---|---|---|---|
| Base (no stress) | 414 | 579 | 182 | $1.36 | $1.66 | $14.85 |
| Sharp 2027 SMB ad recession (PTV -18% vs base in FY27, -9% FY28, -4% FY29; margin -5pts FY27, -2pts FY28) | 340 | 567 | 179 | $1.32 | $1.57 | $14.33 |
| Take-rate reset: -5 pts of take rate from FY28 (~-10% revenue; half of the ~7.5pt margin hit flexed out) | 414 | 521 | 149 | $1.05 | $1.33 | $12.16 |
| No buybacks at all (value-neutral in the DCF, which charges SBC as cash; dilutes per-share EPS) | 414 | 579 | 182 | $1.18 | $1.42 | $14.85 |

- **A sharp but temporary SMB ad recession costs ~$0.5 a share of value.** In a 2020-style shock, SMB/performance platforms troughed at −10% to −32% (Yelp −32%, TTD −13%, Google Search −10% in Q2'20 [R]) (S108). MNTN's ~91–92% SMB exposure and lack of contracts would hit FY27 hard, but net cash cushions the value.
- **A 5-point take-rate reset costs ~$2.7 a share.** A durable fee reset matters far more than a cyclical shock. **The take rate is the single most important undisclosed variable.**

---

## 7. Bull case vs bear case, two pre-mortems, and non-AI risks

### 7.1 The strongest bull case (as a committed long would pitch it)
> **"Priced as an AI casualty, operating like an AI beneficiary."** At ~5.4x FY26 adjusted EBITDA guidance, with 31% of the market cap in net cash and a ~9–10% forward FCF yield, the market is pricing *no growth*. The reverse DCF implies ~0–3.5% revenue CAGR at today's margins. Yet nothing in the numbers shows the damage the market fears:
> - Revenue has beaten or matched consensus in 5 of 5 quarters [C].
> - Gross margin is 80% [R].
> - Concessions are flat and receivables per revenue dollar have fallen [R/E], so there is no sign the take rate is being squeezed.
> - Q3 is guided to re-accelerate to +23–27% [G].
>
> The growth slowdown was self-inflicted mix: a deliberate 2025 push into small businesses, now in the base. Spend per in-quarter active customer has stabilized (−3% vs −25%).
>
> **AI widens MNTN's market more than it threatens it.** 95% of customers have never run a TV ad, and the binding constraint was *having a commercial*. A finished spot now costs ~$24–600. MNTN is the only scaled *independent* platform taking an SMB from AI-generated creative (73K signups in 1H26) to an aired, measured TV campaign on premium inventory. AppLovin, the strongest AI ad engine, says CTV is "step three" and SMBs lack TV-grade creative. On costs, AI is already working: headcount −4% while revenue +21%.
>
> **Scarcity and ownership.**
> - The two look-alikes were bought for **~$1.2B (Vibe) and $465M (tvScientific)**. Walmart paid ~2x MNTN's entire EV. MNTN is the last scaled *neutral* SMB TV platform, and networks consolidating against Amazon and Google want a non-retailer demand partner.
> - No executive has sold a share since the IPO, and the CEO's 10b5-1 plan is unexecuted.
> - Qualcomm's 5.1M-share overhang is gone.
> - A $100M buyback can retire ~13% of shares outstanding (~22–24% of the free float).
>
> **Valuation.** Base value is ~$14–15 (DCF and multiples), the bull ~$24–27, and the Street mean target $18. Downside to the bear (~$6) needs revenue to stall for four years *and* the multiple to stay at 4x.
>
> **Catalysts:**
> - Nov 4: Q3 against $87.7M, plus the buyback in the 10-Q.
> - Dec 15: the CEO's 10b5-1 plan expires.
> - Feb 2027: FY27 guide vs $417M. The stock rose +37% the last time guidance beat.
> - 2027: Express and QuickFrame monetize.
> - Margin heads toward the 35–40% target.
>
> **I'd sell if:** Q3 misses the midpoint; spend per active customer drops >5% again while in-quarter customer growth falls below 20%; gross margin falls below 78%; or Meta launches self-serve CTV for SMBs.

### 7.2 The strongest bear case (as a committed short would pitch it)
> **"The last independent in a category the platforms are absorbing."** MNTN sold first-time TV advertisers three things: a TV-quality ad, an easy self-serve buy, and a performance number. For that it keeps an **undisclosed ~35–60% of media spend**, ~1.6–2.8x The Trade Desk's take rate. AI made the first two free. The platforms now give away the third, bundled with their own purchase data:
> - Amazon's Ads Agent and DVA+;
> - Walmart-Vibe at $50/day with MCP;
> - Universal Ads with no minimum;
> - Roku Ads Manager, doubling advertisers.
>
> What's left is a reseller of other people's inventory, running on rented DSPs.
>
> **Growth is decaying faster than the headline:**
> - The +40% customer metric counts trials and churners. Customers active in the quarter grew **+24%, down from +85%**.
> - Revenue per TTM customer is down 8.7%.
> - **QuickFrame AI's 73K signups produced at most ~600 net new customers.**
> - Incremental revenue per S&M dollar fell from 0.85x to 0.72x.
> - Alternative data points the same way: Northbeam-tracked spend **Vibe +1,900% vs MNTN +29%**; mountain.com's web rank is falling while vibe.co's rises. *(Editor's caveat: Vibe published the Northbeam chart, and small-base and integration-timing effects apply.)*
>
> **Moats are now table stakes:**
> - Attribution is household view-through with 7–14-day windows, "minimal patent protection" and no MRC accreditation. MNTN's own holdout tests and 8 third-party integrations put it on a level playing field.
> - The MCP is a beta; Vibe got there first.
> - YouTube and Prime Video (~38% of streaming) are out of reach.
> - Suppliers are merging (Paramount-WBD; Fox-Roku) and building their own SMB front doors.
>
> **Disclosure is weak:**
> - NRR was replaced by a survivor-only "expansion rate".
> - A $10M stock-paid marketing deal moves marketing cost into SBC, which adjusted EBITDA adds back.
> - A 14% layoff went unmentioned on the calls we could review.
> - The CEO claims "$100M of FCF" against $27M in 1H26.
>
> **Why cheap is a trap.** Count SBC as a cost and EV/EBITDA is ~7.6x, not 5.4x. Buy-side intermediaries that get disintermediated follow TTD (−65% YTD, ~6x) toward Criteo (~1.5x). Our bear case is worth ~$6 (DCF $6.49).
>
> **Catalysts:** the Nov 4 Q4 guide (consensus ~$108M), TTM customer growth converging to the mid-20s, a Feb 2027 FY27 guide that laps a 2026 inflated by one-off events, Fox-Roku closing in 1H27, and agentic price pressure in 2027–28.
>
> **I'd cover on:** a disclosed take rate plus cohort/NRR data that hold up; in-quarter customer growth ≥30% with flat spend per customer; net adds >450 a quarter; or a strategic bid (the biggest risk to the short).

**Our adjudication.**
- The **bear is right about structure.** The moat has narrowed to supply aggregation and bidding, the slowdown is in customer acquisition, and the take rate is the target. That is why the verdict is At Risk.
- The **bull is right about price and timing.** No damage is visible yet, net cash plus FCF give a floor, and the price already embeds a ~45–55% bear-vs-base weight (ours is 35%).
- The debate will be settled by data MNTN does not yet disclose (take rate, NRR, conversion), plus the in-quarter customer line in each 10-Q.

### 7.3 Pre-mortem #1: it's 2030 and the stock is down ~70% (~$3). Why?
**Probability ~10% (7–13%)** [E]. A $3 stock needs *both* a shrinking business *and* most of today's ~$3.17 a share of net cash spent or diluted away.

**The story:**
1. **Q4'26/FY27 guides miss (Nov 2026, Feb 2027).** FY27 guidance is ~+12% against $417M consensus. In-quarter customer growth slides to ~16%. Management blames the go-to-market rebuild again. The real cause is the one its 10-K names: customers transacting "directly… or through intermediaries other than us". Amazon DVA+, Walmart-Vibe, Roku/Fox and Pinterest-tvScientific catch the new-to-TV SMBs, and QuickFrame AI converts at ~1–2%.
2. **A 2027–28 SMB ad recession hits a no-contract, Q4-heavy, ~92%-SMB base.** Returning advertisers come back through Amazon and Walmart, not MNTN.
3. **2028: the take rate breaks.** Agents compare cost per acquisition against 0–1% Amazon fees and ~10% Google caps. MNTN's agency push brings fee-transparent buyers, and regulatory scrutiny of opaque SMB ad pricing rises (FTC v. Amazon). MNTN cuts ~7 points of take rate, about −14% to −17% of revenue with flat gross spend. Meta launches TV inside Advantage+.
4. **Attribution loses authority.** Clean third-party incrementality reads come in well below the self-reported "2–7x" lifts.
5. **Capital allocation fails:**
   - The $100M buyback is spent at $8–9.
   - A ~$120M acquisition (agentic/measurement) is written off with the ~$52M goodwill.
   - SBC is issued at $3–5 a share, and an option repricing follows.
   - The dual-class vote blocks an activist, and the takeout window closes unused.

**Illustrative P&L:** revenue $344M → $245M (FY30); adj. EBITDA margin 27% → 6–9%; FCF negative in 2029–30; diluted shares ~84M.

**Early-warning signs (2026–28):**
1. In-quarter active customer growth **<15% for 2 quarters** (<10% means the thesis is broken).
2. Q4'26 implied guide **< $104M**, or FY27 guide **< $400M**, or any quarter below its guidance midpoint.
3. Spend per active customer **≤ −8% y/y** for 2 quarters; TTM revenue per customer **< $62K** (below every scenario path).
4. Receivables ÷ quarterly revenue **≥ 0.90**, gross margin **< 76%** for 2 quarters, concessions **> 1.5%** of revenue, or any "transparent pricing" tier.
5. Incremental revenue per S&M dollar **≤ 0.60x** with S&M ex-SBC ≥30% of revenue.
6. The "expansion rate >115%" phrase is dropped, or top-10 customers rise above **25%** of revenue.
7. Net cash **< $2.25 a share**, any cash acquisition **> $75M**, SBC **> 9%** of revenue, or an option repricing.
8. Meta TV inside Advantage+; Northbeam showing MNTN **< +10%** for a half-year; a regulatory inquiry or class action on MNTN's pixel or pricing.

### 7.4 Pre-mortem #2: it's 2030 and the stock has tripled (~$31). Why?
**Probability ~20% (15–25%), of which ~5 points come via a takeover** [E]. In our model, tripling needs roughly the **bull path**: FY30 revenue ≳ $700M at ≳35% margin, worth ~$27–47 at 9.5x depending on the year. Alternatively, the base path plus a re-rating to ≥9–10x or a takeout.

**The story:**
1. **Delivery, not hype (Nov 2026–2027).**
   - Q3 lands at the top of guidance and Q4 passes $108M.
   - The FY27 guide beats $417M.
   - In-quarter customer growth re-accelerates as the rebuilt sales team, agency channel and Express mature.
   - The full $100M buyback is done at $10.5–13, retiring ~8M shares before the story is believed.
2. **The AI funnel converts.**
   - Paying Express customers reach thousands.
   - Small businesses that grow move up to Pro, and revenue per customer stops falling at ~$66–67K.
   - QuickFrame AI subscriptions become a ~$10–20M line.
3. **MNTN becomes the neutral SMB TV channel.**
   - Walmart points Vibe at its own sellers.
   - Merged networks prefer a non-retailer demand partner to Amazon or Google.
   - Guaranteed live-sports access builds the Premium tier.
   - Falling CPMs are passed through as better ROAS, so the take rate gives back only 1–2 points.
4. **Agents become a sales channel.** The MCP exits beta. Agents pick MNTN on Verified Visits outcomes for non-Amazon DTC brands. S&M ex-SBC falls from ~30% to ~22–23% of revenue, and the adjusted EBITDA margin reaches the 35–40% target.
5. **What didn't happen:**
   - Meta never scaled TV.
   - Amazon's tools stayed mostly useful to Amazon sellers.
   - ChatGPT ads took from search.
   - The 2027 recession was shallow or absent.

**Takeover branch.** MNTN is the last scaled independent with a ~$0.5B EV, and Walmart paid ~2x that for Vibe. The CEO has said he'd hear a legitimate approach.
- **Constraints:** the Class B block (Greycroft, Douglas and MGD hold ~68% of the vote) and the CEO's $25.40+ performance-option hurdles make a bid below ~$25 hard.
- **Likely bidders:** AppLovin (CTV "step three"), a merged network group, Adobe, or private equity at DV/IAS-like 8–9x EBITDA.
- **Probability of any takeover announced before 2030: ~25%** (15–35%). The most likely bid range is $15–25 [E], below the CEO's $25.40 hurdle and so harder to agree. A takeover at ≥$31 is only ~5%.

**Early confirming signs:**
1. Q3'26 ≥ $88.5M; FY26 ≥ $353M; FY27 guide midpoint ≥ $425M.
2. In-quarter customer growth ≥ +30% in some 2027 quarter with spend per customer ≥ −3%; TTM net adds ≥450 a quarter.
3. ≥1,000 paying Express customers by Q4'27 (≥2,500 by Q4'28), or disclosed QuickFrame-to-paid conversion ≥3%.
4. Gross margin ≥78% every quarter; receivables ÷ revenue ≤0.80; concessions <1%; a disclosed NRR ≥110%.
5. S&M ex-SBC ≤27% of revenue in FY27 and ≤25% in FY28 with growth ≥20%; incremental revenue per S&M dollar ≥0.85x.
6. Adj. EBITDA margin ≥30% (FY27) and ≥33% (FY28); headcount ≤~520 at end-2027.
7. ≥$20M repurchased in the Q3'26 10-Q, ≥$90M by Aug 2027 and the program renewed; net share count growth ≤1% a year.
8. Walmart narrows Vibe to its own ecosystem; MNTN confirms NFL, Netflix or Prime Video access; Adobe or Google names MNTN a launch partner; Northbeam shows MNTN ≥ +40% y/y.

### 7.5 Non-AI risks (Part 6)
- **SMB ad spending in a downturn.**
  - **Exposure:** ~91–92% of PTV revenue is from SMBs [R] (S2); almost no committed contracts [R]; Q4 is ~30% of revenue [R].
  - **Macro now:** NFIB small-business optimism was **97.9** in Sep 2026, roughly at its 52-year average (98.0), but the uncertainty index was elevated at 90 (average 68) [R] (S105). University of Michigan sentiment hit a **record-low 44.8** in May 2026 (51.7 in Aug) [R] (S106). CPI is ~+3.7% y/y [E]. But unemployment is 4.2% [R] (S106), and 2026 ad forecasts were *raised* (IAB +12.3%) [3P] (S96).
  - **History:** SMB/performance platforms fell 10–32% at the 2020 trough (Yelp −32%, TTD −13%, Google Search −10%) [R] (S108). MNTN's own downturn sensitivity is unobserved: 2022 quarterly data is not public.
  - **Our estimate:** a ~20–30% probability of a 2027 ad recession [E], with trough-year growth of −20% to +8% vs the ~+15–18% base [E]. The stress test (§6.10) costs ~$0.5 a share; a deeper multi-year version is part of the bear case.
- **One-offs that distort year-over-year comparisons:**
  - **2026 midterm political spend:**
    - AdImpact projects a record $11.6B for the 2025–26 cycle, $2.7B of it on CTV [3P] (S107).
    - MNTN *does* accept political ads; a help article dated Sep 30, 2026 covers running them (S34).
    - Management says it "traditionally ha[s] not participated in any significant way" and that >99% private-marketplace pricing mutes CPM spikes [R\*]. Q4'24 grew ~34% through a presidential cycle [E].
    - **Read:** a small tailwind to Q3–Q4'26 is possible but undisclosed. The 2027 comparison is neutral to slightly tougher.
  - **2026 World Cup (Jun 11–Jul 19):** MNTN sold World Cup inventory on Telemundo, but discloses no related revenue. It spanned Q2 and Q3'26. There was no visible Q2 boost (+21% was the slowest quarter), but it overlaps Q3's guided re-acceleration. We estimate ≤1–2% of Q2–Q3'26 revenue [E], so up to a 1–2 point headwind to Q2–Q3'27 comparisons.
  - **Maximum Effort divestiture (Apr 1, 2025)** [R] (S1, S9):
    - Q1'25 included $5.4M of Maximum Effort revenue, and FY24 had $16.3M.
    - FY26 GAAP growth is understated by ~2.3 points (~21% GAAP vs ~24% ex-ME); there is no effect from Q2'26 onward.
    - Note that MNTN acquired Maximum Effort in Aug 2021, not 2023. $13.5M of goodwill is still attributed to it inside a single reporting unit.
  - **Q1'26 one-off:** $1.7M of creative-credit breakage makes the Q1'27 comparison ~2 points tougher.
- **TV inventory costs.** CPMs are deflating (upfront streaming −5–7%; Prime Video and Netflix CPMs fell sharply in 2024–25 [3P] (S97, S98)). That helps SMB returns and, because revenue is net, does not hit gross margin directly. The real supply risk is **access, not cost**:
  - supplier consolidation (Paramount-WBD; Fox-Roku);
  - publishers selling direct to SMBs;
  - reliance on rented DSP vendors and two named SSPs [R] (S1).
- **Insider selling and share structure** [R] (S12, S17, S111):
  - **Executives:** no executive officer has sold since the IPO. The CEO's 1M-share 10b5-1 plan (expires Dec 15, 2026) has not been used.
  - **Post-IPO Form 4 selling (~$10.3M):**
    - director Partovi: 447,520 shares, ~$6.0M, Dec 2025, outside a plan;
    - Baroda Ventures: 335,555 shares, ~$4.3M, Aug 2026.
  - **Qualcomm** sold ~4.98M shares in 1H26 (stake now 147K).
  - **Overhang:** the lock-up expired Nov 6, 2025. Pre-IPO holders still own ~44% of shares, against ~0.7–1.0M shares of daily volume [E].
  - **Control:** Class B shares carry 10 votes each and hold ≈66% of the vote [E: 129.1M ÷ ~194M]. Its three holders control ~68% of the combined vote including their Class A (Greycroft 27.7%, Douglas 25.0%, MGD 15.5%) [R, proxy]. Class B sunsets around May 2032.
  - **Short interest:** 3.97M shares (~9–10% of float; 3.98 days to cover) at Sep 30, 2026.
- **SBC** [R] (S1, S3):
  - FY25 was $31.7M (10.9% of revenue), dominated by 2021 G&A awards that have now vested. TTM is ~7.2%.
  - Q2'26 jumped to $8.8M, including a **$10M/yr stock-paid marketing contract** with an unnamed contractor. This is a quality-of-earnings flag: marketing cost moves into SBC, which adjusted EBITDA adds back.
  - TTM FCF after SBC is only ~$37M [E].
  - The full 5% + 1% evergreen was taken for 2026 [R] (S16).
- **Recent quarters where EPS missed consensus** [R/C] (S110):
  - **Q2'25:** GAAP EPS −$0.65 (IPO-related charges); vendor-adjusted −$0.08 vs −$0.06 (MarketBeat): **a miss**.
  - **Q3'25:** $0.08 vs $0.03–0.04: **beat**.
  - **Q2'26:** $0.09 vs $0.15–0.22 across data vendors. SBC rose $4.9M q/q and there was $1.5M of restructuring, ≈$0.06 [E].
  - **Q4'25:** $0.43 vs $0.24–0.26, a reported beat flattered by the $9.2M tax benefit. At a normal tax rate it was ~$0.24, i.e. in line.
  - **Q1'26:** $0.11 vs $0.04 (Investing.com, beat), $0.12 (MarketBeat, miss), $0.12 (Zacks, −8.3%, miss).
  - **Revenue** was in line or a beat in 5 of 5 quarters.
  - **The stock trades on the revenue guide, not EPS:** −8.1% (Nov 5, 2025), **+37.1% (Feb 11, 2026)**, **−22.8% (May 6, 2026)**, +3.8% (Aug 5, 2026) [3P market data] (S112). Counterexample: Aug 6, 2025 fell 17.9% after an above-Street guide.
- **Other:**
  - Legal fees rose $2.1M in 1H26 on "ongoing litigation", though MNTN says it is not party to any material proceedings [R].
  - Unaccrued state sales-tax exposure [R].
  - Pixel/privacy litigation risk (VPPA/CIPA) [R, risk factor].
  - Dependence on third-party AI models: OpenAI removed the Sora API, and Seedance faces IP claims [3P] (S91, S94).
  - Key-person risk (CEO) and brand risk (Ryan Reynolds).

---

## 8. Scorecard: what to check every quarter

The first read is **Nov 4, 2026** (Q3 release and Q4 guide), followed by the Q3 10-Q around Nov 9–10. The second is the **FY27 guide in ~Feb 2027**.

| # | Metric (where to find it) | Latest | **Confirms** (verdict moves up toward Neutral/Beneficiary) | **Breaks** (verdict moves down toward Victim) |
|---|---|---|---|---|
| 1 | **Customers active in the quarter, y/y** (10-Q MD&A; *not* the TTM headline) | +24% (Q2'26) [R] | ≥ +30% for 2 quarters | ≤ +15% for 2 quarters |
| 2 | **Spend per in-quarter active customer, y/y** = (1 + revenue growth) ÷ (1 + active-customer growth) − 1 | ≈ −3% [E] | ≥ −3% while Express scales | ≤ −8% for 2 quarters |
| 3 | **Revenue vs guidance; FY27 guide vs consensus** (release) | Q3 guide $86–89M; FY27 consensus $417.3M | Q3 ≥ $88.5M; FY27 guide midpoint ≥ $425M | Q3 < $87.5M; FY27 guide midpoint < $400M; any quarter below its guidance midpoint |
| 4 | **Gross margin and concessions** (release; 10-K allowance roll-forward) | 80.3%; concessions ≈ $2.65M/yr (<1% of revenue) [R] | ≥ 78% and concessions < 1% of revenue | < 76% for 2 quarters, or disclosed rebates, volume discounts or "transparent pricing" |
| 5 | **Receivables ÷ quarterly revenue** (proxy for take rate; receivables are booked at gross billings) | 0.73 [E] | ≤ 0.80 | ≥ 0.90 with unchanged billing terms |
| 6 | **Sales-and-marketing efficiency**: TTM incremental revenue ÷ TTM S&M | 0.72x; S&M 34.6% of revenue (GAAP) [E/R] | ≥ 0.85x | ≤ 0.60x, or S&M > 35% of revenue with flat net adds |
| 7 | **AI monetization and disclosure** (call, 10-Q) | QuickFrame AI ~$0; Express "hundreds" paying (<3% of revenue, ~$3–10M [E]); MCP in beta | Express + QuickFrame AI ≥ 5% of revenue, **or** disclosed QuickFrame-to-paid conversion ≥ 3%, **or** disclosed spend sourced through agents/MCP | Still undisclosed, or < 3% of revenue at Q4'27 |
| 8 | **Capital allocation and dilution** (10-Q equity note) | $100M authorized, $0 disclosed; 78.6M diluted shares; SBC 7.2% of revenue (TTM) | ≥ $20M repurchased in the Q3 10-Q; ≥ $90M by Aug 2027; net share count growth ≤ 1% a year; SBC ≤ 7% | Buyback unused; SBC > 9%; any cash acquisition > $75M; option repricing |

Watch two other signals alongside the scorecard:
- **Retention disclosure:** a real net revenue retention figure (≥110% confirms). Dropping the "well north of 115%" phrase would be a break signal.
- **External moves:** Meta launching CTV ads for SMBs; Amazon disclosing SMB streaming-TV adoption; Walmart-Vibe pricing and openness after integration; whether Fox-Roku and Paramount-WBD keep MNTN's private-marketplace terms.

---

## 9. Sources

All accessed between Oct 14 and Oct 15, 2026 unless noted. Call transcripts are third-party (Motley Fool, Investing.com, Equibles) and **not checked against the audio**. The Q1'26 Motley Fool page mixes in text from another company, so only its Q&A was used.

**MNTN primary filings and releases**
- S1. MNTN Form 10-K FY2025, SEC, filed 2026-02-19. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm
- S2. MNTN IPO prospectus (424B4), SEC, 2025-05-22. https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm
- S3. MNTN Form 10-Q Q2 2026, SEC, 2026-08-10. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm
- S4. MNTN Form 10-Q Q1 2026, SEC, 2026-05-11. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000040/mntn-20260331.htm
- S5. MNTN Form 10-Q Q3 2025, SEC, 2025-11-10. https://www.sec.gov/Archives/edgar/data/1891027/000189102725000022/mntn-20250930.htm
- S6. MNTN Form 10-Q Q2 2025, SEC, 2025-08-11. https://www.sec.gov/Archives/edgar/data/1891027/000189102725000012/mntn-20250630.htm
- S7. Q2 2026 earnings release (8-K Ex. 99.1), 2026-08-04. https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm
- S8. Q1 2026 earnings release, 2026-05-05. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000038/mntnearningsrelease2026-q1.htm
- S9. Q4/FY2025 earnings release, 2026-02-10. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000004/mntnearningsrelease2025-q4.htm
- S10. Q3 2025 earnings release, 2025-11-04. https://www.sec.gov/Archives/edgar/data/1891027/000189102725000019/mntnearningsrelease2025-q3.htm
- S11. Q2 2025 earnings release, 2025-08-05. https://www.sec.gov/Archives/edgar/data/1891027/000189102725000009/mntn-20250805xexx991.htm
- S12. DEF 14A proxy, 2026-04-30. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000033/mntn-20260430.htm
- S13. DRS/A (FY2022–23 financials), 2024-05-13. https://www.sec.gov/Archives/edgar/data/1891027/000110465924060066/filename1.htm
- S14. "MNTN To Announce Third Quarter 2026 Financial Results on November 4, 2026", MNTN IR, 2026-10-14. https://s205.q4cdn.com/886349678/files/doc_news/MNTN-To-Announce-Third-Quarter-2026-Financial-Results-on-November-4-2026-2026.pdf
- S15. Q2 2026 investor deck, 2026-08-04. https://s205.q4cdn.com/886349678/files/doc_financials/2026/q2/MNTN-2Q26-Investor-Deck.pdf
- S16. Form S-8 (2026 evergreen shares), 2026-02-19. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000021/forms-8evergreenshares2026.htm
- S17. Qualcomm Schedule 13G/A, 2026-07-16. https://www.sec.gov/Archives/edgar/data/1891027/000110465926084288/0001104659-26-084288-index.htm
- S18. Qualcomm Form 144, 2026-02-19. https://www.sec.gov/Archives/edgar/data/1891027/000110465926017446/primary_doc.xml
- S19. MNTN EDGAR filing index (incl. Form 4s). https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001891027&type=&dateb=&owner=include&count=100

**MNTN calls, conferences, company pages**
- S20. Q2 2026 earnings call transcript (call 2026-08-04), The Motley Fool. https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/
- S21. Q1 2026 earnings call (2026-05-05): Investing.com https://www.investing.com/news/transcripts/earnings-call-transcript-mntn-q1-2026-tops-forecasts-stock-rises-93CH-4661246 ; Motley Fool Q&A https://www.fool.com/earnings/call-transcripts/2026/05/06/mntn-mntn-q1-2026-earnings-transcript/
- S22. Q4 2025 earnings call (2026-02-10), The Motley Fool. https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/
- S23. Q3 2025 earnings call (2025-11-04), Investing.com. https://www.investing.com/news/transcripts/earnings-call-transcript-mntn-q3-2025-sees-strong-earnings-beat-stock-dips-93CH-4332329
- S24. MNTN at the Canaccord conference, Investing.com, 2026-08-11. https://www.investing.com/news/transcripts/mntn-at-canaccord-conference-growth-broadens-beyond-early-adopters-93CH-4852453
- S25. Q2 2025 call (auto-transcript; low reliability), Equibles. https://equibles.com/stocks/mntn/calls/2025-q2
- S26. "Understand MNTN's pricing model", MNTN Help Center, 2026-02-09. https://help.mountain.com/en/articles/8054978-understand-mntn-s-pricing-model
- S27. "Understand MNTN attribution", MNTN Help Center, 2026-04-03. https://help.mountain.com/en/articles/12608309-understand-mntn-attribution
- S28. "Understand MNTN incrementality", MNTN Help Center, 2026-03-25. https://help.mountain.com/en/articles/11096577-understand-mntn-incrementality
- S29. "The technology that puts performance in Performance TV" (MCP server, API), MNTN tech blog, 2026-08. https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/
- S30. "The AI engine behind the bid: intelligent intent scoring", MNTN tech blog, 2026-08. https://mountain.com/tech/the-ai-engine-behind-the-bid-inside-mntns-intelligent-intent-scoring/
- S31. "MNTN releases QuickFrame AI 3.0", 2026-05-05. https://mountain.com/press/mntn-releases-quickframe-ai-3-0-with-a-major-feature-expansion-delivering-tv-ready-commercials-in-minutes/
- S32. QuickFrame pricing page (accessed 2026-10-15). https://quickframe.com/
- S33. MNTN app, HubSpot Marketplace (accessed 2026-10-15). https://ecosystem.hubspot.com/marketplace/apps/mntn
- S34. "Run political advertising on MNTN", MNTN Help Center, 2026-09-30. https://help.mountain.com/en/articles/17177735-run-political-advertising-on-mntn
- S35. MNTN Greenhouse job board (2026-10-15). https://boards-api.greenhouse.io/v1/boards/mntn/jobs
- S36. "MNTN and Northbeam…" press release, 2025-12-03. https://s205.q4cdn.com/886349678/files/doc_news/MNTN-and-Northbeam-Give-Marketers-a-Trusted-Way-to-Verify-CTV-Performance-and-Acquire-New-Consumers-2025.pdf
- S37. "MNTN agency-led accounts grow 4x in 2025", 2025-09-29. https://ir.mountain.com/news/news-details/2025/MNTN-Agency-Led-Accounts-Grow-4x-in-2025-as-Demand-for-Performance-TV-Surges/default.aspx
- S38. "MNTN and Magnite turn live streaming's biggest moments into Performance TV", Magnite, 2026-01-22. https://www.magnite.com/press/mntn-and-magnite-turn-live-streamings-biggest-moments-into-performance-tv-for-growth-brands/
- S39. "PubMatic and MNTN partner to expand premium CTV…", MNTN IR, 2025-10. https://s205.q4cdn.com/886349678/files/doc_news/PubMatic-and-MNTN-Partner-to-Expand-Premium-CTV-Market-Driving-Net-New-Advertiser-Demand-and-Unlocking-a-10-Publisher-Revenue-Lift-20-9ATCJ.pdf

**Trade press and third-party analysis on MNTN**
- S40. "MNTN's SMB CTV ad business is growing like gangbusters", AdExchanger, 2025-11-05. https://www.adexchanger.com/tv/mntns-smb-ctv-ad-business-is-growing-like-gangbusters/
- S41. "Why MNTN's CEO isn't sweating media consolidation", AdExchanger, 2026-08-07. https://www.adexchanger.com/ctv-roundup/why-mntns-ceo-isnt-sweating-media-consolidation/
- S42. T. Triscari, "#119: MNTN IPO + valuation update" (take-rate estimate), Quo Vadis, 2025-05-27. https://www.quovadisnews.com/p/119-mntn-ipo-valuation-update
- S43. Marketecture (A. Paparo, a Vibe board member): "Moving MNTNs", 2025-03-03, https://news.marketecture.tv/p/moving-mntns ; "Takeaways from Walmart's Vibe deal", 2026-06-29, https://news.marketecture.tv/p/takeaways-from-walmart-s-vibe-co-deal

**Platforms, competitors and peers**
- S50. Amazon Q2 2026 earnings release, 2026-07-30. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm
- S51. Amazon DSP product page (accessed 2026-10-15). https://advertising.amazon.com/solutions/products/amazon-dsp
- S52. "unBoxed 2025: simplifying advertising with AI", Amazon Ads, 2025-11-11. https://advertising.amazon.com/library/news/unboxed-2025-simplifying-advertising-ai
- S53. Alphabet Q2 2026 earnings release, 2026-07-22. https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm
- S54. "Demand Gen drop", Google, 2026-01-22. https://blog.google/products/ads-commerce/demand-gen-drop-january-2026/
- S55. "Veo in Google Ads", Google, 2026-03-24. https://business.google.com/en-all/accelerate/announcements/veo-google-ads/
- S56. Meta Q2 2026 earnings call transcript, 2026-07-29. https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf
- S57. "Meta eyes CTV expansion…", Digiday, 2026-04-27. https://digiday.com/future-of-tv/meta-eyes-ctv-expansion-to-fuel-its-next-wave-of-ad-growth/
- S58. Roku Q1 2026 shareholder letter, 2026-04-30. https://www.sec.gov/Archives/edgar/data/0001428439/000162828026028851/a04fy2026q1exhibit991.htm
- S59. Roku Form 10-Q Q2 2026, 2026-08-06. https://www.sec.gov/Archives/edgar/data/1428439/000162828026054335/roku-20260630.htm
- S60. Fox to acquire Roku (Ex. 99.1), 2026-06-15. https://www.sec.gov/Archives/edgar/data/1428439/000114036126025115/ef20076172_ex99-1.htm
- S61. Netflix Q2 2026 shareholder letter, 2026-07-16. https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000211/ex991_q226.htm
- S62. "Walmart completes acquisition of Vibe.co", Walmart, 2026-08-04. https://corporate.walmart.com/news/2026/08/04/walmart-completes-acquisition-of-vibe-co
- S63. "Time to wake up: Walmart's quest to own TV advertising" (WSJ-reported price), The Current, 2026-07-08. https://www.thecurrent.com/opinion/time-wake-up-walmart-quest-own-tv-advertising
- S64. Pinterest Form 10-Q Q1 2026 (tvScientific purchase price), 2026-05. https://www.sec.gov/Archives/edgar/data/0001506293/000150629326000068/pins-20260331.htm
- S65. Vibe pricing page (accessed 2026-10-15). https://www.vibe.co/pricing
- S66. "Self-service linear TV", Universal Ads, 2026-04-27. https://www.universalads.com/newsroom/self-service-linear-tv
- S67. "Universal Ads must pass the pizza test…", Digiday, 2026-05-28. https://digiday.com/media-buying/universal-ads-must-pass-the-pizza-test-if-its-to-steal-ad-dollars-from-social/
- S68. Warner Bros. Discovery 8-K (Paramount Skydance merger completed), 2026-10-06. https://www.sec.gov/Archives/edgar/data/1437107/000119312526415055/d200872d8k.htm
- S69. The Trade Desk Q2 2026 earnings release, 2026-08-06. https://www.sec.gov/Archives/edgar/data/1671933/000167193326000085/ttd-20260806x8kexx991.htm
- S70. The Trade Desk Form 10-Q Q2 2026, 2026-08-06. https://www.sec.gov/Archives/edgar/data/1671933/000167193326000086/ttd-20260630.htm
- S71. The Trade Desk Form 10-K FY2025, 2026-02-27. https://www.sec.gov/Archives/edgar/data/1671933/000167193326000014/ttd-20251231.htm
- S72. AppLovin Q2 2026 earnings presentation, 2026-08. https://s21.q4cdn.com/165405286/files/doc_financials/2026/q2/Q2-2026-AppLovin-Earnings-Presentation.pdf
- S73. Magnite 10-K FY2025 (2026-02-25), https://www.sec.gov/Archives/edgar/data/1595974/000159597426000007/mgni-20251231.htm ; Q2 2026 release, https://www.sec.gov/Archives/edgar/data/1595974/000162828026053334/a991-earningsq22026.htm
- S74. PubMatic Q2 2026 earnings call, The Motley Fool, 2026-08-13. https://www.fool.com/earnings/call-transcripts/2026/08/13/pubmatic-pubm-q2-2026-earnings-call-transcript/
- S75. Criteo Q2 2026 release, 2026-08-05. https://www.sec.gov/Archives/edgar/data/1576427/000162828026052913/exhibit991-8xkq22026.htm
- S76. Nielsen–DoubleVerify merger release, 2026-08-06. https://www.sec.gov/Archives/edgar/data/1819928/000110465926092121/tm2621904d1_ex99-1.htm
- S77. Novacap–Integral Ad Science release, 2025-09-24. https://www.sec.gov/Archives/edgar/data/1842718/000119312525214050/d938971dex991.htm
- S78. Teads Q2 2026 release, 2026-08-06. https://www.sec.gov/Archives/edgar/data/1454938/000145493826000051/q22026er-exhibit991.htm
- S79. Viant Q2 2026 release, 2026-08-06. https://www.sec.gov/Archives/edgar/data/1422930/000142293026000029/q226pressrelease.htm

**Agentic buying and fees**
- S80. "How does agentic buying work in CTV?", AdExchanger, 2026-10-08. https://www.adexchanger.com/ctv-roundup/how-does-agentic-buying-work-in-ctv/
- S81. "Amazon Ads unveils new AI tools" (Ads MCP server), MediaPost, 2026-09-29. https://www.mediapost.com/publications/article/418355/amazon-ads-unveils-new-ai-tools.html
- S82. "The Trade Desk introduces Kokai Zuma", 2026-08-27. https://investors.thetradedesk.com/news-and-events/news/news-details/2026/The-Trade-Desk-Introduces-Kokai-Zuma-the-Latest-Release-of-Kokai/default.aspx
- S83. "Meta opens its ad system to Claude and ChatGPT…", PPC Land, 2026-04-29. https://ppc.land/meta-opens-its-ad-system-to-claude-and-chatgpt-with-new-ai-connectors/
- S84. AdCP / AgenticAdvertising.org, Marketing Brew, 2026-09-28. https://www.marketingbrew.com/stories/agentic-advertising-trade-group-adcp
- S85. IAB Tech Lab, Agentic Advertising Management Protocols (AAMP), 2026-09-22. https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/
- S86. IAB 2026 Outlook study, 2026-01-28. https://www.prnewswire.com/news-releases/iab-2026-outlook-study-forecasts-9-5-growth-in-us-ad-spend-fueled-by-digital-growth-major-cyclical-events-and-accelerating-adoption-of-agentic-ai-302671862.html
- S87. "Omnicom allegedly pivoted a chunk of its Q3 spend from The Trade Desk to Amazon", AdExchanger, 2025-11-18. https://www.adexchanger.com/platforms/omnicom-allegedly-pivoted-a-chunk-of-its-q3-spend-from-the-trade-desk-to-amazon/
- S88. "The Trade Desk's revenue growth stalls…", AdExchanger, 2026-08-07. https://www.adexchanger.com/programmatic/the-trade-desks-revenue-growth-stalls-as-big-brands-tighten-their-belts/
- S89. "The Amazon Ads lawsuit raises questions about auction disclosure…", AdExchanger, 2026-09-09. https://www.adexchanger.com/data-driven-thinking/the-amazon-ads-lawsuit-raises-questions-about-auction-disclosure-dsp-buyers-need-to-ask/

**Generative video and creative**
- S90. Gemini API pricing (Veo 3.1 per-second prices), Google (accessed 2026-10-15). https://ai.google.dev/gemini-api/docs/pricing
- S91. OpenAI API deprecations (Sora 2 API removed 2026-09-24). https://developers.openai.com/api/docs/deprecations
- S92. Adobe GenStudio for Performance Marketing release notes, 2026-09-16. https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/release-notes
- S93. Runway pricing, https://runway.com/pricing ; Adobe Firefly plans, https://www.adobe.com/products/firefly/plans.html (accessed 2026-10-15)
- S94. "ByteDance safeguards Seedance after Disney legal threat", Variety, 2026-02-16. https://au.variety.com/2026/film/global/bytedance-safeguards-seedance-disney-legal-threat-ip-violations-33139/

**Industry data, macro and AI ads**
- S95. Nielsen, The Gauge, July 2026 (published 2026-09-10). https://www.nielsen.com/news-center/2026/tv-usage-kicks-usual-summer-slowdown-fueled-by-world-cup-and-streaming-in-nielsens-july-gauge-reports/
- S96. "IAB raises 2026 U.S. ad spend forecast", IAB, 2026-09-10. https://www.iab.com/news/iab-raises-2026-u-s-ad-spend-forecast/
- S97. "Prime-time upfront ad sales rise 9% to $33.7B; CPM…", MediaPost, 2026-08-11. https://www.mediapost.com/publications/article/417166/prime-time-upfront-ad-sales-rise-9-to-337b-cpm.html
- S98. "Streaming TV ad rates are falling, and Amazon's the anchor", Digiday, 2025-02-24. https://digiday.com/marketing/streaming-tv-ad-rates-are-falling-and-amazons-the-anchor/
- S99. "CTV becomes TV's growth engine as linear collapses", eMarketer, 2025-12. Page blocked (403); figures are snippet-level and unverified. https://www.emarketer.com/content/ctv-becomes-tv-s-growth-engine-linear-collapses
- S100. WPP Media mid-year forecast, The Measure, 2026-06-15. https://www.themeasure.net/wpp-media-boosts-ad-revenue-forecast-sees-8-9-growth/
- S101. "ChatGPT ads reach $1B annualized in 200 days", MediaPost, 2026-08-31. https://www.mediapost.com/publications/article/417561/chatgpt-ads-reaches-1b-annualized-in-200-days.html
- S102. "OpenAI launches self-serve Ads Manager for ChatGPT", Search Engine Journal, 2026-05-05. https://www.searchenginejournal.com/openai-launches-self-serve-ads-manager-for-chatgpt/573971/
- S103. "AI search ad spend to reach $26B by 2029" (eMarketer), MediaPost, 2025-06-04. https://www.mediapost.com/publications/article/406378/ai-search-ad-spend-to-reach-26b-by-2029.html
- S104. "WPP forecasts AI search ads to become fastest-growing channel", Digiday, 2026-06-16. https://digiday.com/media-buying/wpp-forecasts-ai-search-ads-to-become-fastest-growing-channel-in-advertising/
- S105. NFIB Small Business Economic Trends, September 2026 (2026-10-13). https://www.nfib.com/wp-content/uploads/2026/10/NFIB-SBET-Report-September-2026.pdf
- S106. FRED series (accessed 2026-10-15): University of Michigan consumer sentiment (UMCSENT), https://fred.stlouisfed.org/series/UMCSENT ; unemployment rate (UNRATE), https://fred.stlouisfed.org/series/UNRATE ; CPI (CPIAUCSL), https://fred.stlouisfed.org/series/CPIAUCSL
- S107. "2026 election cycle to reach record $11.6B in ad spending", AdImpact, 2026-06-11. https://adimpact.com/blogs/adimpact-reveals-2026-election-cycle-to-reach-record-11.6-billion-in-ad-spending
- S108. Yelp Q2 2020 shareholder letter (downturn benchmark), 2020-08-06. https://www.sec.gov/Archives/edgar/data/1345016/000134501620000045/yelpq220exhibit992shareh.htm

**Consensus, market and alternative data**
- S109. Yahoo Finance, MNTN analysis page (consensus; 2026-10-15). https://finance.yahoo.com/quote/MNTN/analysis/
- S110. StockAnalysis.com, MNTN forecast and ratings (S&P Global data; updated 2026-08-13). https://stockanalysis.com/stocks/mntn/forecast/ ; https://stockanalysis.com/stocks/mntn/ratings/
- S111. FINRA consolidated short interest, settlement 2026-09-30. https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest
- S112. Interactive Brokers market data (MNTN and peer prices, daily history), 2026-10-15. Accessed via API; no public URL.
- S113. Broker target changes: Evercore (2026-02-11), https://www.investing.com/news/analyst-ratings/evercore-isi-lowers-mntn-stock-price-target-to-27-on-peer-multiple-compression-93CH-4500455 ; Citizens (2026-05-06), https://www.investing.com/news/analyst-ratings/citizens-cuts-mntn-stock-price-target-to-19-on-lower-valuation-93CH-4662073
- S114. Tranco list rank, mountain.com (2026-10-14). https://tranco-list.eu/api/ranks/domain/mountain.com
- S115. Similarweb, mountain.com (Sep 2026 snapshot). https://www.similarweb.com/website/mountain.com/
- S116. BuiltWith, MNTN pixel usage (accessed 2026-10-15). https://trends.builtwith.com/analytics/MNTN
- S117. "Fastest-growing ad channel" (Northbeam-tracked spend chart), Vibe blog, 2026-07-14. A competitor publication. https://www.vibe.co/blog/whats-new/fastest-growing-ad-channel-northbeam
- S118. Blind, MNTN employee reviews (accessed 2026-10-15). https://www.teamblind.com/company/MNTN/reviews
- S119. Shopify App Store, MNTN reviews (accessed 2026-10-15). https://apps.shopify.com/mntn/reviews
- S120. Paramount Ads Manager, "CTV advertising cost" page (vendor claim; accessed 2026-10-15). https://adsmanager.paramount.com/insights/ctv-advertising-cost
- S121. "Amazon, Roku partner to meet advertisers' demands for CTV scale", Marketing Dive, 2025-06-18. https://www.marketingdive.com/news/amazon-roku-partner-to-meet-advertisers-demands-for-ctv-scale/751027/
- S122. "Netflix Upfront 2026", Netflix, 2026-05-13. http://about.netflix.com/en/news/netflix-upfront-2026-get-closer
- S123. "Inside The Trade Desk's Claude-powered campaign agent", Digiday, 2026-05-18. https://digiday.com/media-buying/inside-the-trade-desks-claude-powered-campaign-agent/
- S124. "Perplexity stops testing advertising", Search Engine Land, 2026-02. https://searchengineland.com/perplexity-stops-testing-advertising-469452
- S125. "Biggest screen, smallest budgets…" (IAB SMB CTV adoption data), The Current, 2026-07-23. https://www.thecurrent.com/media/biggest-screen-smallest-budgets-retail-broadcast-tech-tv-advertising-walmart-comcast

---

## Appendix A: Method, data gaps and caveats

**Method.** The work ran in four steps:
1. **Research:** 15 parallel research dossiers, each built primary-source first with every number labeled. They covered filings; calls and guidance; customers; MNTN's AI; walled gardens; agentic buying; fees; competitors; creative AI; alternative data; supply and the CTV market; budget migration and macro; consensus and valuation; insiders; and peers.
2. **Fact-checking:** an independent adversarial agent fact-checked each dossier. No load-bearing reported number was refuted; corrections are applied throughout.
3. **Independent perspectives:** a completeness critic, three verdict judges, committed bull and bear advocates, two pre-mortems, and a model red-team whose fixes are in the final model.
4. **Model:** written in Python so every assumption is visible and re-runnable.

The dossiers are in [`research/`](research/).

**Data that does not exist publicly.** These are stated as gaps, not estimated around:
- Take rate and gross billings.
- Net revenue retention since Q1'25, churn and cohorts.
- QuickFrame AI signup-to-paying conversion and revenue.
- Express pricing and paying-customer count.
- Usage of MNTN's MCP agent interface, and spend sourced through agents.
- Customer counts by size.
- Political and World Cup revenue.
- Customers above $100K after FY24.
- Free FY26–27 adjusted EBITDA consensus, and any FY28–30 consensus.
- MNTN's results in a recession (2022 quarterly data is not public).

**Weaker evidence to read with care:**
- All management quotes come from third-party transcripts.
- Product-performance claims are company marketing.
- Walmart-Vibe terms come from WSJ via The Current.
- eMarketer CTV forecasts are snippet-level and mix vintages.
- Northbeam's "MNTN +29%" was published by a competitor.
- Alternative-data sources (Tranco, Similarweb, BuiltWith) are noisy.
- The 2-analyst "normalized" EPS consensus has an unknown definition.

**Price basis.** $10.25 is an Oct 15, 2026 intraday price on a +9% day with no identified catalyst. At the $9.40 prior close, upside to the probability-weighted value is +37% to +54% instead of +25% to +40%, and the implied growth is ~3 points lower (§6.7).
