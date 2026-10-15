# F. AI Threat 2: Agentic Ad Buying and MNTN (as of 2026-10-15)

**Question:** If advertisers' AI agents buy media directly from publishers, exchanges and platforms, does MNTN get bypassed, or does it become the TV layer those agents call?

**Labels:** [reported] = company or filing disclosure; [guidance] = company outlook; [third-party] = trade press, surveys or competitor disclosures; [estimate] = my own derivation, with the math shown; [qualitative] = no number. Q3 2026 results had **not** been released as of 2026-10-15. The latest MNTN 8-K under Item 2.02 is dated 2026-08-04, and the only later filings are an Item 5.02 8-K (director Michael Katz, 2026-09-08) and Forms 3/4 ([EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001891027.json), accessed 2026-10-15).

---

## 1. Bottom line

1. **Agentic ad buying is real infrastructure but not yet real money (Oct 2026).** Every major buy-side and sell-side platform now exposes an agent interface:
   - Amazon Ads MCP Server: open beta Feb 2026, more than 700 external connections.
   - Meta Ads AI Connectors: Apr 2026.
   - Yahoo DSP: MCP plus agents, Jan 2026.
   - The Trade Desk Koa Agents in Kokai Zuma: Aug 27, 2026.
   - PubMatic AgenticOS: Jan 2026.
   - Magnite seller agent in SpringServe: Jan 2026.
   - Netflix: testing agents that "purchase ads".

   Two competing standards stacks exist: AdCP/AgenticAdvertising.org and IAB Tech Lab's ARTF/AAMP. **No platform discloses dollar volume transacted by agents.** The best hard counts are small: PubMatic reported "over 80 agentic campaigns" and about 4,000 "AI-powered deals" in Q2 2026 [third-party, competitor call]. My estimate is that autonomous agent-to-agent buying is **well under 1% of US CTV spend in 2026** [estimate, low confidence; see §4].
2. **The near-term disruption is to the interface, not the pipes.** What is scaling in 2026 is agents *operating* existing platforms through MCP/APIs: reporting, building campaigns, shifting budgets. Agents are not yet replacing DSPs or SSPs in the auction. That hits MNTN's core differentiation, "TV as easy as search/social" through a self-serve UI ([10-K FY2025](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm)). Once any agent can drive Amazon DSP, Yahoo DSP, Vibe or Meta in plain language, ease of use stops being a moat.
3. **MNTN has responded faster than its filings suggest.** It has:
   - a **read-write MCP server (beta)** "operable from Claude, ChatGPT, and other leading AI assistants";
   - an AI Media Plan;
   - a public Reporting API (v3.8.0);
   - native HubSpot (Jun 2026) and Klaviyo (Sep 2026) integrations;
   - "significant agentic AI technology" for mid-market customers (CEO, Q2 call).

   It does not disclose any usage metric for these. The words "agentic" and "AI agents" appear in **zero** MNTN SEC filings ([EDGAR full-text search](https://efts.sec.gov/LATEST/search-index?q=%22agentic%22&ciks=0001891027), accessed 2026-10-15).
4. **What an agent cannot replicate** is MNTN's closed loop:
   - Verified Visits pixel attribution with last-touch de-duplication;
   - a household identity graph covering more than 99% of US CTV households;
   - optimization models trained on conversions;
   - 98% direct supply from 200+ networks, packaged into small-budget access;
   - gross billing with credit risk on net-30 terms.

   These are *tools agents call*, not things agents replace. They are also what Amazon, Walmart (with Vibe and VIZIO), Google/YouTube and Roku can match or exceed on data scale.
5. **Verdict for this topic: modestly negative, about −1 on a −5 to +5 scale.** Agentic buying is more likely to compress MNTN's **take rate and pricing power** (2028-2030) than to eliminate it. My probability-weighted 2030 revenue impact versus a no-agent counterfactual is **about −5% to −12%** [estimate, §8]. Because revenue is recognized net, the effect on EBITDA is magnified roughly 3.5x. Upside comes if MCP and agents cut MNTN's customer-acquisition cost: sales & marketing was ~35% of revenue in Q2 2026 [reported, derived].

---

## 2. State of the standards (Oct 2026)

| Initiative | Backers | Status | Key facts |
|---|---|---|---|
| **Ad Context Protocol (AdCP)** / AgenticAdvertising.org (AAO) | Founding members Triton Digital, Yahoo, PubMatic, Scope3, Optable, Swivel. Each committed a **$10,000** annual budget [third-party] ([AdExchanger, 2025-10-15](https://www.adexchanger.com/publishers/the-ad-context-protocol-aims-to-make-sense-of-agentic-ad-demand/)) | "AdCP 3.2 is now generally available"; **154+ members** listed, including Yahoo, PubMatic, Scope3, Samba TV, LG Ads, Kargo [reported by AAO] ([adcontextprotocol.org](https://adcontextprotocol.org/), accessed 2026-10-15) | First agent-to-agent media buy on **2025-10-16**, with LG Ads inventory [reported by AAO]. AAO board has **22 of 40** seats filled. No major DSP sits on it; DSPs are only "dabbling," per board president Ben Masse [third-party] ([Marketing Brew, 2026-09-28](https://www.marketingbrew.com/stories/agentic-advertising-trade-group-adcp)). MNTN is not named on the AAO homepage (membership not verifiable). |
| **IAB Tech Lab ARTF** (Agentic RTB Framework) | Built with Index Exchange, OpenX, The Trade Desk, Chalice. Participants include Amazon Ads, Netflix, Yahoo, Paramount, Magnite, PubMatic, WPP Media [third-party] ([PPC Land, 2025-11-15](https://ppc.land/iab-tech-lab-opens-agentic-rtb-framework-for-container-based-advertising/)) | v1.0 public comment Nov 13, 2025 to Jan 15, 2026 | Containerized agents inside RTB infrastructure, communicating over gRPC/MCP. Stated goal of **80%** latency reduction [third-party] ([The Current, 2025-11-13](https://www.thecurrent.com/marketing/marketing-strategy-iab-tech-lab-adcp-agentic-advertising-framework-ai)). IAB Tech Lab CEO Katsur said the industry did not need "another industry trade group" (a dig at AdCP). |
| **IAB Tech Lab Agentic Roadmap / AAMP** | IAB Tech Lab | Roadmap announced 2026-01-06 ([PR Newswire](https://www.prnewswire.com/news-releases/iab-tech-lab-unveils-agentic-roadmap-for-digital-advertising-302654047.html)). AAMP page lists **AAMP 3.0** (adds OpenProposal for RFPs), 2.3 and 2.0 releases; page updated 2026-09-22 ([IAB Tech Lab](https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/)) | Open-source buyer- and seller-agent SDKs, an Agent Registry, and a built-on-OpenDirect/AdCOM approach. AAMP 2.3 is described as moving agentic buying "beyond demos" into production stacks. **No volume metrics.** |

**Read-across for MNTN:** the standards are converging on **seller agents at the SSP/publisher layer** (SpringServe, PubMatic, LG, WBD) and **buyer agents at the agency/holding-company layer** (MiQ, Dentsu, Butler/Till, RPA/Newton). Neither stack has a natural role for a vertically integrated SMB platform unless that platform exposes itself as a buyer agent or tool, which is what MNTN's MCP does.

---

## 3. Platform moves (who is building agent access)

| Company | What is live / announced | Agentic status | Source |
|---|---|---|---|
| **The Trade Desk** | **Kokai Zuma** (2026-08-27) adds Koa Assistant plus specialist **Koa Agents** for audience building and frequency optimization. Claims "average **32%** improvement in CPA" [third-party, company claim]. Koa analyzes more than **20M** impressions per second. | Some features GA, others in open or closed beta. In May 2026 the agents "don't buy ads yet" and need marketer sign-off. Claude can create a campaign for closed-beta participants through the "Open Agentic Kit" interoperability layer. | [TTD PR, 2026-08-27](https://investors.thetradedesk.com/news-and-events/news/news-details/2026/The-Trade-Desk-Introduces-Kokai-Zuma-the-Latest-Release-of-Kokai/default.aspx); [Digiday, 2026-05-18](https://digiday.com/media-buying/inside-the-trade-desks-claude-powered-campaign-agent/) |
| **Amazon Ads** | **Ads MCP Server** in open beta from Feb 2026. Agents (Claude, ChatGPT, Gemini) can create campaigns, pull reports and manage billing. **700+ external connections** since launch. New "expert tools" tier (AMC SQL Generator, closed beta, broader availability early 2027). | Beta. Amazon's Paula Despins: "connectivity alone doesn't guarantee reliable outcomes." | [Digiday, 2026-02-03](https://digiday.com/media-buying/ad-tech-briefing-amazon-launches-mcp-server-for-agent-driven-advertising/); [MediaPost, 2026-09-29](https://www.mediapost.com/publications/article/418355/amazon-ads-unveils-new-ai-tools.html) |
| **Google** | **Ads Advisor** (Nov 2025) applies changes "with your review and approval." Ask Advisor consolidation was announced at Google Marketing Live (May 2026; secondary coverage only). Official **googleads/google-ads-mcp** server exposes only retrieval tools (`search`, `get_resource_metadata`, `list_accessible_customers`), with no mutate operations in its README. | In-product agent; external MCP is read-only. | [Google blog, 2025-11-12](https://blog.google/products/ads-commerce/ads-advisor-and-analytics-advisor/); [GitHub](https://github.com/googleads/google-ads-mcp) (accessed 2026-10-15) |
| **Meta** | **Ads AI Connectors** open beta announced 2026-04-29. Hosted MCP server; Claude and GPT can create and edit campaigns, ad sets, ads and catalogs (write access from day one). | Open beta, all business sizes. | [PPC Land](https://ppc.land/meta-opens-its-ad-system-to-claude-and-chatgpt-with-new-ai-connectors/) |
| **Yahoo DSP** | CES 2026: "Yours, Mine, Ours" framework. External agents connect via **MCP**. A Newton/RPA trafficking agent "has already executed programmatic guaranteed buys." Troubleshooting agent is live. Agent Network followed in June 2026. | Live (activation via MCP, troubleshooting, audience exploration); more through 2026. | [Yahoo, 2026-01-06](https://www.yahooinc.com/press/yahoo-dsp-advances-its-buying-platform-with-new-agentic-ai-capabilities) |
| **PubMatic** | **AgenticOS** launched Jan 2026. Q2 2026: "over **80** agentic campaigns" (up from **30** the prior quarter), about **4,000** AI-powered deals, used with "all **5** global agency holding companies." "Emerging" revenue is about **15%** of revenue, driven partly by AgenticOS (no separate figure). CFO: agentic buying through Activate generates "a buying fee." | Live, early scale. | [PubMatic Q2 2026 call, Motley Fool, 2026-08-13](https://www.fool.com/earnings/call-transcripts/2026/08/13/pubmatic-pubm-q2-2026-earnings-call-transcript/) |
| PubMatic + Butler/Till (CTV case) | Geloso Beverage, Dec 2025: agents planned and executed end to end on AgenticOS via Butler/Till's enterprise **Claude** interface. **5.5x** lower buy-side supply-chain cost, impressions **40%** above plan, **98%** video completion rate [third-party, press-material claims]. | Single campaign, vendor claims. | [Marketing Dive, 2026-03-17](https://www.marketingdive.com/news/beverage-marketer-sees-cost-savings-with-agentic-media-buying-test/814905/) |
| **Magnite** | Seller agent built into **SpringServe** (CTV ad server; per Jounce, 99% of US streaming supply). Supports AdCP. First test Dec 2025 with Scope3 as buyer agent; MiQ ran "one of the first AdCP buys." LG Ad Solutions and WBD are testing. A buyer agent and "Magnite Orchestration" followed (Apr and Jun 2026, per trade coverage). | Testing/pilots. | [PPC Land, 2026-01-06](https://ppc.land/magnite-builds-seller-agent-into-springserve-for-ai-driven-ad-buying/) |
| **Netflix** | 2026 Upfront: "testing AI agents to manage, optimize, and purchase ads on Netflix"; Audience Insights and Reach Curve APIs. | Testing. | [Netflix, 2026-05-13](http://about.netflix.com/en/news/netflix-upfront-2026-get-closer) |
| Fox / other TV sellers | Fox AdStudio to roll out agentic planning and buying "in the coming months." | Announced. | [Adweek, May 2026](https://www.adweek.com/convergent-tv/what-agentic-tv-buying-really-means-according-to-disney-youtube-netflix-and-more/) |
| **Vibe.co (now Walmart)**, the closest SMB-CTV competitor | **Vibe MCP** launched 2026-07-16: read and write, launches campaigns from Claude, ChatGPT or Gemini Enterprise; "first time any CTV platform has been available inside an AI assistant" (vendor claim). CEO: "**more than 1,000 brands** have adopted Vibe's MCP integration," and MCP-enabled buying "accounts for a large portion of ad spend" on Vibe [third-party, CEO claim]. Walmart completed the Vibe acquisition 2026-08-04; Vibe has **10,000+** advertisers [reported by Walmart]. Price not disclosed by Walmart; ~$1.4B per trade reports (unverified). | Live. | [Vibe, 2026-07-16](https://www.vibe.co/blog/product-updates/ctv-just-stopped-being-a-separate-tab-introducing-the-vibe-mcp); [AdExchanger, 2026-10-08](https://www.adexchanger.com/ctv-roundup/how-does-agentic-buying-work-in-ctv/); [Walmart, 2026-08-04](https://corporate.walmart.com/news/2026/08/04/walmart-completes-acquisition-of-vibe-co) |
| OpenAI | ChatGPT Ads self-serve Ads Manager (US 2026, expanded to 31 European markets Aug 2026, per OpenAI post seen in search snippets; page returned 403). This competes for SMB budgets more than it acts as an agentic buyer of CTV. | Live (ads). No evidence of OpenAI buying CTV for advertisers. | [OpenAI](https://openai.com/index/chatgpt-ads-expands-across-europe/) (not directly readable; flagged) |

**Market signal:** New Street Research cut its TTD target from $17 to $10 (Aug 2026), citing rising **disintermediation risk** from AWS and Google "Buyer Direct" [third-party] ([MediaPost, 2026-08-27](https://www.mediapost.com/publications/article/417511/trade-desk-goes-agentic-simplifies-programmatic-b.html)). Investors are already pricing agentic and AI disintermediation into independent buy-side intermediaries. MNTN's de-rating (peak ~$32 in Aug 2025 to ~$10.24 now, per baseline facts) sits inside the same narrative.

---

## 4. Is real spend flowing through agentic buying in 2026?

| Evidence | Metric | Label |
|---|---|---|
| PubMatic agentic campaigns (cumulative since Jan 2026) | 80+ campaigns; ~4,000 AI-powered deals (Q2 2026) | [third-party, competitor call] |
| Amazon Ads MCP Server | 700+ external connections (Feb to Sep 2026); no spend disclosed | [third-party] |
| Vibe MCP | 1,000+ brands adopted; a "large portion" of Vibe spend is MCP-enabled; no dollar figure | [third-party, CEO claim] |
| AdCP | First live agent-to-agent buy 2025-10-16; no aggregate volume published | [reported by AAO] |
| IAB 2026 Outlook (200+ buyers) | "Two-thirds now focused on agentic AI for ad buying and campaign execution"; US ad spend +9.5%, **CTV +13.8%** in 2026 | [third-party] ([IAB/PR Newswire, 2026-01-28](https://www.prnewswire.com/news-releases/iab-2026-outlook-study-forecasts-9-5-growth-in-us-ad-spend-fueled-by-digital-growth-major-cyclical-events-and-accelerating-adoption-of-agentic-ai-302671862.html)) |
| IAB 2026 Digital Video report (fielded Feb 20 to Mar 13, 2026) | ~67% of buyers have live tests or plan to use agentic AI for video; 28% investigating. Smaller and mid-sized budgets use it to automate execution-heavy tasks. | [third-party] ([MediaPost, 2026-05-05](https://www.mediapost.com/publications/article/414834/iab-highlights-agentic-adoption-in-video-ad-spend.html)) |
| IAB Europe (n=50) | 58% expect agentic buying to reach operational use or scale within a year; 36 of 47 have no day-to-day agentic system or one still directed by people | [third-party] ([Digiday, 2026-09-24](https://digiday.com/media-buying/58-of-ad-execs-expect-agentic-buying-to-hit-scale-within-a-year-according-to-iab-europe-research/)) |

**Estimate of autonomous agent-executed share of US CTV spend in 2026: <1%** [estimate, low confidence].
- Reasoning: the only platform giving counts (PubMatic) reports tens of campaigns per quarter, against hundreds of thousands of programmatic campaigns.
- TTD's agents did not autonomously buy as of May 2026.
- Every surveyed source describes tests and intent.
- No company has disclosed agentic dollars, which suggests the numbers are not yet flattering.

**By contrast, "agent-assisted" management of existing self-serve platforms through MCP is already material at the SMB end.** Vibe claims 1,000+ of its 10,000+ advertisers (roughly 10%) use its MCP [estimate from third-party figures: 1,000 / 10,000]. That segment is exactly MNTN's.

---

## 5. MNTN's own agentic moves

| Item | Detail | Label / source |
|---|---|---|
| **MNTN MCP (beta)** | "read-write Model Context Protocol server, operable from Claude, ChatGPT, and other leading AI assistants." **Read:** advertisers, campaigns, flights, audiences, creatives, geography, full reporting. **Write:** adjust budgets, pause or reweight creatives, change audience and geo targeting, launch campaigns. MNTN claims "Read-write agentic control of this depth is unique in Performance TV" (contestable: Vibe shipped read-write MCP on 2026-07-16). No press release, launch date, usage or pricing found. | [reported, marketing] ([MNTN tech blog, Aug 2026](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/)) |
| AI Media Plan | Ranked, budget-allocated network plan, live newsfeed of automated decisions, reallocates post-launch; no fee | [reported, marketing] (same) |
| Agentic AI for mid-market | CEO Mark Douglas: "we've added significant agentic AI technology into the platform … We surround them with AI tech to give our customers control of the daily decision-making." Tiering: Express (SMB, launched Apr 1, 2026; 7,000+ signups, "hundreds" paying), Pro, Premium. | [reported, call] ([Motley Fool transcript, Q2 2026](https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/)) |
| Public APIs | **MNTN Reporting API 3.8.0** (OpenAPI 3.0.1; `/apilist`, `/apidata`) and **Async Batch Export API 3.8.0**, documented at api3.mountain.com/docs. The 10-K says reporting can be "pulled directly from the platform through our API." A third-party catalog also lists a campaign-management PTV API at api.mountain.com (not verified). | [reported] ([api3.mountain.com/docs](https://api3.mountain.com/docs), spec at [/api-docs/API](https://api3.mountain.com/api-docs/API), accessed 2026-10-15); [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm) |
| HubSpot | TV exposure written into HubSpot contact records; CRM lists synced into MNTN daily ("first CTV platform" to do so). No agent/Breeze mention. | [reported] ([MNTN press, ~2026-06-15](https://mountain.com/press/mntn-brings-advanced-data-attribution-to-ctv-with-first-of-its-kind-hubspot-integration/)) |
| Klaviyo | Two-way: Klaviyo audiences on MNTN; TV exposure triggers Klaviyo email and SMS flows. No AI/agent mention. | [reported] ([MNTN press, ~2026-09-09](https://mountain.com/press/mntn-and-klaviyo-integrate-performance-tv-with-crm/)) |
| Adobe / Google | Adobe integrating QuickFrame AI into GenStudio for Performance Marketing; Google named QuickFrame an early adopter of Gemini Omni Flash models | [reported] ([Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm)) |
| Measurement integrations | 30+ partners (LiftLab, Haus, Northbeam, Rockerbox, iSpot, Klaviyo, HubSpot) | [reported, marketing] ([MNTN tech blog](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/)) |
| **What's absent** | No "agentic", "AI agents", MCP or LLM-disintermediation risk factor in the FY2025 10-K or Q2 2026 10-Q (EDGAR FTS: 0 hits for "agentic" and "AI agents"). No MCP usage, agent-sourced revenue or AdCP membership disclosed. No ChatGPT app or Claude directory listing found. | [reported, absence] ([EDGAR FTS](https://efts.sec.gov/LATEST/search-index?q=%22agentic%22&ciks=0001891027)) |

**Existing generic risk language already covers the bypass case.** Customers "may bypass us and transact directly with sellers of advertising inventory or through other intermediaries." Separately: "many sellers are investing in capabilities that enable them to connect more effectively directly with customers" ([10-K FY2025](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm); repeated in the [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm)).

**A dependency worth noting:** MNTN "relies on multiple vendors to serve as its demand-side platform from which customers can purchase advertising inventory, which account for a significant portion of costs" (10-K concentration note). The vendors are not named. MNTN does not own every layer of its pipe; its tech blog also describes a homegrown bidder handling up to **4M** bid requests per second [reported, marketing]. If agent-native DSPs (TTD, Amazon, Yahoo) turn into competing front ends, the vendor relationship becomes a two-sided risk.

---

## 6. What an agent can and cannot replicate (MNTN value stack)

| MNTN layer | What it is (facts) | Can a buyer agent replicate or bypass it? | Defensibility (1-5) |
|---|---|---|---|
| Self-serve UI / workflow simplicity | Core pitch: "launch TV campaigns directly without the help of traditional media agencies" (10-K) | **Yes.** MCP on Amazon, Meta, Yahoo, Vibe and TTD lets any agent run any platform in natural language; the UI premium erodes. | **1** |
| Media planning | AI Media Plan; content-level targeting (no fee) | Largely yes. LLMs plus publisher APIs (Netflix Reach Curve/Audience Insights) and AdCP `get_products`-style discovery can plan. | 2 |
| Creative | QuickFrame AI (from $39/month); ~95% of customers never advertised on TV ([10-K](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm)) | Yes. Gen-video is commoditizing (Veo/Sora-class models; Meta and Amazon creative tools). | 2 |
| **Attribution: Verified Visits** | Patented; pixel on tens of thousands of sites; VAST event TTL matched to window; cross-device via graph; withholds credit when another paid channel had the last touch (~25% branded-search case); posts to GA4; Rockerbox receives it directly ([tech blog](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/)) | **No** for the data. Agents can *substitute* platform-neutral measurement (GA4, Northbeam, Haus incrementality) and compare across vendors, which commoditizes MNTN's self-reported ROAS. | **4** |
| **Household identity graph** | Covers >99% of US CTV households; hundreds of millions of devices; real-time updates | No (proprietary data). But Amazon, Walmart+VIZIO, Roku, Google/YouTube have equal or bigger first-party graphs. | 3-4 |
| **Optimization models trained on conversions** | Optimizer trained on de-duplicated last-touch set; Matched audiences; "more than a billion" optimizations per day | No. This is what an agent would *call* as a tool (set goal = CPA X, let MNTN bid). | **4** |
| Supply aggregation for small budgets | **98%** direct relationships, **200+** networks; non-preemptible, non-skippable; >99% via PMP deals ([Q2 call](https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/)) | Partially. Agent-to-agent buying (AdCP seller agents at LG, WBD, SpringServe) lowers the cost of direct deals, but publishers still impose minimums. A typical MNTN customer's annual net revenue is **~$78k** [estimate: Q2'26 revenue $82.5M × 4 / 4,225 TTM-active customers; overstates spend per active customer because TTM count includes churned accounts], below most direct-deal thresholds. | 3 |
| Billing / credit / fraud & brand safety | Bills gross, recognizes revenue net; "net 30" terms for credit customers; carries collection risk ([10-K](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm)) | Agents don't extend credit, so an aggregator is needed. But Amazon, Walmart and Google can do this at lower cost of capital. | 3 |

**Net:** MNTN's defensible core (attribution, graph, conversion-trained bidding, small-budget supply packaging) works best when it is **called by** agents through MCP. Its least defensible layer, ease of use, was the original wedge.

---

## 7. Who holds the advertiser relationship in an agentic world?

- **Today:** MNTN holds it directly. It is brand-direct and self-serve; ~95% of customers are new to TV; net expansion is "still well north of 115%" (CFO, Q2 2026) [reported] ([Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/)). Active Performance TV customers: **4,225** TTM, **+40%** y/y [reported] ([Q2 release](https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm)).
- **Agentic world: the relationship migrates to whoever owns the agent surface.**
  - (a) General assistants (Claude, ChatGPT, Gemini): neutral routers that need MCP connectors. MNTN is present in beta.
  - (b) Walled-garden in-product agents (Google Ask Advisor, Amazon Ads Agent, Meta Advantage+, TTD Koa). These will route SMB TV budgets to YouTube CTV, Prime Video/Amazon DSP or TTD, **not** to MNTN.
  - (c) Systems-of-record agents (HubSpot "agentic customer platform," Klaviyo, which is opening its own platform to Claude/ChatGPT via MCP per [MediaPost Email Insider, Sep 2026](https://www.mediapost.com/publications/article/417762/tv-email-buddy-up-the-two-channels-can-now-be-in.html) (seen via search summary only), Shopify, Adobe). MNTN has native integrations with HubSpot, Klaviyo and Adobe.
  - (d) Agency buyer agents (MiQ, Dentsu, Butler/Till on Claude, InterMedia on Claude with Vibe/Olyzon). AdExchanger notes "agent ownership is unclear when access runs through Claude rather than [the vendor's] platform" ([AdExchanger, 2026-10-08](https://www.adexchanger.com/ctv-roundup/how-does-agentic-buying-work-in-ctv/)).
- **Implication:** MNTN moves from *destination* to *supplier of a TV outcome* inside someone else's agent. Distribution then depends on being selected by an agent comparing CPA/ROAS across options, which pressures pricing. The quality of the outcomes data matters more than the brand or UI.
- **The strongest competitive fact here:** Walmart now owns Vibe, the SMB-CTV platform with the most-advanced MCP adoption claim (1,000+ brands). Walmart can pair it with commerce audiences and closed-loop measurement ([Walmart, 2026-08-04](https://corporate.walmart.com/news/2026/08/04/walmart-completes-acquisition-of-vibe-co)). An agentic SMB ecosystem anchored by Walmart Connect, Amazon Ads and Google is the bear case for MNTN's relationship ownership.

---

## 8. Economics: why agentic buying matters through the take rate

- MNTN recognizes revenue **net**: gross billings minus inventory cost and certain agency consideration ([Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm)). Gross billings and take rate are **not disclosed** (data gap).
- Cost of revenue (~20% of revenue) scales with impressions served, not fees. So any compression in MNTN's fee on media flows almost 1:1 to gross profit.
- Agentic buying's explicit pitch is fee compression: Butler/Till/PubMatic claimed **5.5x** lower buy-side supply-chain cost [third-party, vendor claim] ([Marketing Dive, 2026-03-17](https://www.marketingdive.com/news/beverage-marketer-sees-cost-savings-with-agentic-media-buying-test/814905/)). A PubMatic March 2026 agency-partnership release reportedly cited 40-50% supply-chain cost reductions (seen only in search snippets; the page returned 403, so treat as unverified).

**Static sensitivity on FY26 guidance midpoints, before any cost response** [estimate]:
- Revenue $352M = ($347M + $357M) / 2 [guidance]. Adj. EBITDA $98.5M = ($96M + $101M) / 2 [guidance]. Margin ≈ 28.0%.
- **5%** take-rate compression → revenue −$17.6M → EBITDA $80.9M (−18%), margin 24.2%.
- **10%** → revenue $316.8M, EBITDA $63.3M (−36%), margin 20.0%.
- **20%** → revenue $281.6M, EBITDA $28.1M (−71%).
- Rule of thumb: each 1% of take-rate compression costs about 3.6% of EBITDA unless offset.

**Offsets (bull mechanics)** [estimate]:
- Q2'26 sales & marketing $28.6M = **34.7%** of revenue ($28.6M / $82.537M); T&D 19.9%; G&A 16.5% [reported inputs, derived ratios].
- If agents and MCP become a lower-cost acquisition channel (an agent recommends MNTN, an SMB onboards via Claude/ChatGPT/HubSpot), S&M could fall 5-10 points of revenue by 2030. That roughly offsets a 5-10% take-rate cut.

**Scenarios: agentic-specific revenue effect in 2030 vs. a no-agent counterfactual** [all estimates]

| Scenario | Probability | Mechanism | Math | 2030 revenue effect |
|---|---|---|---|---|
| **Winner: MNTN becomes the TV tool agents call** | 25% | MCP/agent distribution lowers CAC; agents expand the SMB long tail into TV; outcomes data wins agent comparisons; take rate holds | +10-20% volume, −3-5% take | **+5% to +15%** |
| **Base: agent-mediated but not disintermediated** | 55% | 25-35% of MNTN spend agent-routed by 2030; agent-routed spend earns 15-25% lower take; small share loss to walled-garden agents | 0.25-0.35 × 15-25% = −4% to −9% take effect, plus −1% to −3% volume | **−5% to −12%** |
| **Victim: commoditized** | 20% | ~50% of spend agent-routed at 30-50% lower take; Walmart/Vibe, Amazon, Google, Roku agents capture SMB TV; customer growth stalls | 0.5 × 30-50% = −15% to −25% take, plus −10% to −15% volume | **−25% to −40%** |
| **Probability-weighted** | | | 0.25 × (+10%) + 0.55 × (−8.5%) + 0.20 × (−32.5%) = **−8.7%** | **≈ −5% to −12%** |

**For the model:** apply the agentic effect mainly to the **take rate / revenue per customer** from **2028** onward, not to customer counts in 2026-27. Through 2027 the evidence supports only pilots and agent-assisted management. Keep a separate S&M-efficiency offset in the bull case.

---

## 9. Timing and likelihood

| Period | What I expect | Confidence |
|---|---|---|
| 2026 (now) | Agent *interfaces* everywhere (MCP betas); autonomous buys in the tens to hundreds of campaigns; human sign-off standard ("I still want a pilot in the cockpit" — InterMedia, [AdExchanger](https://www.adexchanger.com/ctv-roundup/how-does-agentic-buying-work-in-ctv/)). No measurable MNTN revenue impact; FY26 guidance reiterated Aug 4, 2026 [guidance]. | High |
| 2027 | Standards mature (AdCP 3.x, AAMP 3.x, IAB agent registry). SMB self-serve platforms without solid MCP lose share. Agents start comparing CTV vendors on CPA. First pricing pressure on SMB-CTV fees; Walmart-Vibe bundles likely. | Medium |
| 2028-2030 | Agent-to-agent PMP/direct deals in premium CTV become a meaningful channel (my range: **10-30%** of programmatic CTV by 2030 [estimate, low confidence]). Intermediary take rates compress industry-wide. MNTN's outcome is decided by whether its attribution and bidding are what agents select. | Low-medium |

**Likelihood that MNTN is materially bypassed (>25% revenue impact) by 2030:** ~20% [estimate]. **Likelihood of some take-rate pressure attributable to agents:** ~65-75% [estimate].

---

## 10. Signposts (what would change the view)

- **Positive (toward winner):**
  - MNTN discloses MCP/API-sourced customers or spend.
  - MNTN joins AdCP/AAO or IAB agent registry as a buyer agent.
  - An official Claude/ChatGPT directory listing.
  - S&M as a percentage of revenue falls while customer growth stays above 25%.
  - Expansion rate stays >115% after agent adoption.
  - Agent-integrated partners (HubSpot, Klaviyo, Shopify) show up in customer-acquisition commentary.
- **Negative (toward victim):**
  - Walmart-Vibe price cuts or agent-only bundles.
  - Amazon or Google in-product agents offering CTV to SMBs at lower fees.
  - Q3/Q4 2026 revenue per customer declines faster than mix explains.
  - Gross margin falls below ~78% without a mix explanation.
  - An agentic/AI-disintermediation risk factor appears in the FY2026 10-K.
  - Netflix/Disney/WBD open low-minimum agent-to-agent direct buying.

---

## 11. Verdict for this topic

**Score: −1 (slightly toward AI victim) on a −5 to +5 scale.**

- **Why negative:** agentic buying attacks the *interface* moat that made MNTN unique to SMBs, shifts relationship ownership to agent owners (Google, Amazon, Meta, Walmart-Vibe, OpenAI/Anthropic), and its explicit value proposition is fee compression. MNTN's revenue is a net fee on media with ~3.6x EBITDA leverage to take rate.
- **Why only −1:** MNTN's hard-to-replicate assets are the ones agents need as tools: Verified Visits attribution, the household graph, conversion-trained bidding, and small-budget packaging of 200+ direct network relationships. MNTN was early with a read-write MCP and CRM integrations, and real autonomous spend in 2026 is negligible.
- **Swing factor:** whether MNTN can show by 2027-28 that agents choose it on outcomes. That would turn the score positive by lowering CAC.

---

## Sources

1. MNTN, "The Technology That Puts Performance in Performance TV" (tech blog), Aug 2026. https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/
2. MNTN, Q2 2026 earnings release (8-K Ex-99.1), 2026-08-04. https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm
3. MNTN, Form 10-Q for quarter ended 2026-06-30, filed 2026-08-10. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm
4. MNTN, Form 10-K FY2025, filed 2026-02-19. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm
5. MNTN, 424B4 IPO prospectus, 2025-05-22. https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm
6. SEC EDGAR full-text search ("agentic", CIK 0001891027), accessed 2026-10-15. https://efts.sec.gov/LATEST/search-index?q=%22agentic%22&ciks=0001891027
7. SEC EDGAR submissions feed for MNTN, accessed 2026-10-15. https://data.sec.gov/submissions/CIK0001891027.json
8. MNTN, 8-K Item 5.02 (director Michael J. Katz), filed 2026-09-08. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000089/mntn-20260903.htm
9. The Motley Fool, "MNTN (MNTN) Q2 2026 Earnings Call Transcript," 2026-08-11. https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/
10. Investing.com, "Earnings call transcript: MNTN Q2 2026…," Aug 2026. https://www.investing.com/news/transcripts/earnings-call-transcript-mntn-q2-2026-profit-miss-sparks-afterhours-drop-93CH-4835959
11. MNTN Reporting API 3.8.0 / Async Batch Export API docs, accessed 2026-10-15. https://api3.mountain.com/docs ; https://api3.mountain.com/api-docs/API
12. MNTN press, "MNTN Brings Advanced Data Attribution to CTV with First of its Kind HubSpot Integration," ~2026-06-15. https://mountain.com/press/mntn-brings-advanced-data-attribution-to-ctv-with-first-of-its-kind-hubspot-integration/
13. MNTN press, "MNTN and Klaviyo Integrate Performance TV with CRM," ~2026-09-09. https://mountain.com/press/mntn-and-klaviyo-integrate-performance-tv-with-crm/
14. AdExchanger, "MNTN Wants Its AI Video Ad Generator To Stand Apart From Its CTV Platform," 2026-05-07. https://www.adexchanger.com/tv/mntn-wants-its-ai-video-ad-generator-to-stand-apart-from-its-ctv-platform/
15. MNTN Research, "The Proof Is in the Performance: Why 2026 Upfronts Coverage Signaled a TV Sea Change," May 2026. https://research.mountain.com/trends/the-proof-is-in-the-performance-why-2026-upfronts-coverage-signaled-a-tv-sea-change/
16. AdExchanger, "The Ad Context Protocol Aims To Make Sense Of Agentic Ad Demand," 2025-10-15. https://www.adexchanger.com/publishers/the-ad-context-protocol-aims-to-make-sense-of-agentic-ad-demand/
17. AgenticAdvertising.org / AdCP homepage, accessed 2026-10-15. https://adcontextprotocol.org/
18. Marketing Brew, "Agentic advertising trade group debuts board amid broader industry adoption," 2026-09-28. https://www.marketingbrew.com/stories/agentic-advertising-trade-group-adcp
19. IAB Tech Lab (PR Newswire), "IAB Tech Lab Unveils Agentic Roadmap for Digital Advertising," 2026-01-06. https://www.prnewswire.com/news-releases/iab-tech-lab-unveils-agentic-roadmap-for-digital-advertising-302654047.html
20. PPC Land, "IAB Tech Lab opens agentic RTB framework for container-based advertising," 2025-11-15. https://ppc.land/iab-tech-lab-opens-agentic-rtb-framework-for-container-based-advertising/
21. The Current, "IAB Tech Lab, not a fan of AdCP, releases an agentic advertising framework," 2025-11-13. https://www.thecurrent.com/marketing/marketing-strategy-iab-tech-lab-adcp-agentic-advertising-framework-ai
22. IAB Tech Lab, "AAMP: Agentic Advertising Management Protocols," page updated 2026-09-22. https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/
23. The Trade Desk, "The Trade Desk Introduces Kokai Zuma, the Latest Release of Kokai," 2026-08-27. https://investors.thetradedesk.com/news-and-events/news/news-details/2026/The-Trade-Desk-Introduces-Kokai-Zuma-the-Latest-Release-of-Kokai/default.aspx
24. Digiday, "Inside The Trade Desk's Claude-powered campaign agent," 2026-05-18. https://digiday.com/media-buying/inside-the-trade-desks-claude-powered-campaign-agent/
25. MediaPost, "Trade Desk Goes Agentic, Simplifies Programmatic Buying," 2026-08-27. https://www.mediapost.com/publications/article/417511/trade-desk-goes-agentic-simplifies-programmatic-b.html
26. Digiday, "Ad Tech Briefing: Amazon launches MCP server for agent-driven advertising," 2026-02-03. https://digiday.com/media-buying/ad-tech-briefing-amazon-launches-mcp-server-for-agent-driven-advertising/
27. MediaPost, "Amazon Ads Unveils New AI Tools," 2026-09-29. https://www.mediapost.com/publications/article/418355/amazon-ads-unveils-new-ai-tools.html
28. Adweek, "Amazon Opens Its Ad Stack to AI Agents With MCP Rollout," ~Feb 2026. https://www.adweek.com/media/amazon-agentic-ads-model-context-protocol/
29. Google, "Google's AI advisors: agentic tools to drive impact and insights," 2025-11-12. https://blog.google/products/ads-commerce/ads-advisor-and-analytics-advisor/
30. GitHub, googleads/google-ads-mcp README, accessed 2026-10-15. https://github.com/googleads/google-ads-mcp
31. PPC Land, "Meta opens its ad system to Claude and ChatGPT with new AI connectors," Apr/May 2026. https://ppc.land/meta-opens-its-ad-system-to-claude-and-chatgpt-with-new-ai-connectors/
32. Yahoo, "Yahoo DSP Advances its Buying Platform with New Agentic AI Capabilities," 2026-01-06. https://www.yahooinc.com/press/yahoo-dsp-advances-its-buying-platform-with-new-agentic-ai-capabilities
33. PPC Land, "Magnite builds seller agent into SpringServe for AI-driven ad buying," 2026-01-06. https://ppc.land/magnite-builds-seller-agent-into-springserve-for-ai-driven-ad-buying/
34. The Motley Fool, "PubMatic (PUBM) Q2 2026 Earnings Call Transcript," 2026-08-13. https://www.fool.com/earnings/call-transcripts/2026/08/13/pubmatic-pubm-q2-2026-earnings-call-transcript/
35. Marketing Dive, "Beverage marketer sees cost savings with agentic media-buying test," 2026-03-17. https://www.marketingdive.com/news/beverage-marketer-sees-cost-savings-with-agentic-media-buying-test/814905/
36. Netflix, "Netflix Upfront 2026: Get Closer," 2026-05-13. http://about.netflix.com/en/news/netflix-upfront-2026-get-closer
37. Adweek, "What Agentic TV Buying Really Means, According to Disney, YouTube, Netflix, and More," May 2026. https://www.adweek.com/convergent-tv/what-agentic-tv-buying-really-means-according-to-disney-youtube-netflix-and-more/
38. Vibe, "CTV just stopped being a separate tab: Vibe MCP is live," 2026-07-16. https://www.vibe.co/blog/product-updates/ctv-just-stopped-being-a-separate-tab-introducing-the-vibe-mcp
39. AdExchanger, "How Does Agentic Buying Work In CTV?," 2026-10-08. https://www.adexchanger.com/ctv-roundup/how-does-agentic-buying-work-in-ctv/
40. Walmart, "Walmart Completes Acquisition of Vibe.co," 2026-08-04. https://corporate.walmart.com/news/2026/08/04/walmart-completes-acquisition-of-vibe-co
41. IAB (PR Newswire), "IAB 2026 Outlook Study Forecasts 9.5% Growth in U.S. Ad Spend…," 2026-01-28. https://www.prnewswire.com/news-releases/iab-2026-outlook-study-forecasts-9-5-growth-in-us-ad-spend-fueled-by-digital-growth-major-cyclical-events-and-accelerating-adoption-of-agentic-ai-302671862.html
42. MediaPost, "IAB Highlights Agentic Adoption In Video Ad-Spend Report," 2026-05-05. https://www.mediapost.com/publications/article/414834/iab-highlights-agentic-adoption-in-video-ad-spend.html
43. Digiday, "58% of ad execs expect agentic buying to hit scale within a year, according to IAB Europe research," 2026-09-24. https://digiday.com/media-buying/58-of-ad-execs-expect-agentic-buying-to-hit-scale-within-a-year-according-to-iab-europe-research/
44. MediaPost Email Insider, "TV, Email Buddy Up: The Two Channels Can Now Be Integrated," Sep 2026 (not opened directly). https://www.mediapost.com/publications/article/417762/tv-email-buddy-up-the-two-channels-can-now-be-in.html
45. OpenAI, "ChatGPT Ads expands across Europe," Aug 2026 (page returned 403; seen only via search snippet; flagged). https://openai.com/index/chatgpt-ads-expands-across-europe/
46. apis.io, MNTN provider profile (third-party crawler, used only to locate API docs), accessed 2026-10-15. https://apis.io/providers/mntn/

---

## Verification (adversarial check)

Checked 2026-10-15 against primary sources: the SEC 10-Q, 10-K and 8-K, the EDGAR full-text search API, and the MNTN, Vibe, Walmart and TTD pages. Trade press was used where no primary source exists. The web-search budget ran out partway through, so the sub-claims marked unverifiable below could not be searched further.

| # | Finding | Verdict | Correct value / note | Evidence |
|---|---|---|---|---|
| 1 | MNTN read-write MCP (beta), usable from Claude/ChatGPT; no launch date, usage or pricing | **Confirmed** | The page says "Agentic Layer: The MNTN MCP (beta)" and "operable from Claude, ChatGPT, and other leading AI assistants". The read side also covers advertisers, flights and geography. No launch date, usage or pricing on the page. MNTN's press page has no MCP release, and the Q2'26 call never says "MCP", "Claude", "ChatGPT" or "agent". This is a website claim only. | [mountain.com/tech](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/) |
| 2 | Revenue is net of inventory cost; gross billings and take rate not disclosed; ~3.6% EBITDA per 1% take-rate cut; 10% cut → ~$63M (−36%) | **Confirmed** (arithmetic and facts) | 10-Q: "reports revenue from the sale of advertising inventory on its platform on a net basis… gross billings net of amounts it pays suppliers". No billings or take-rate figure is given. Guidance midpoints of $352M and $98.5M are correct (8-K: $347-357M and $96-101M). The math is right: 1/0.28 = 3.57x. A 10% cut gives $63.3M (−35.7%). Caveat: some revenue (ad production, QuickFrame) is not a media take rate, so 3.6x slightly overstates the leverage. Keep the **estimate** label. | [10-Q Q2'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm); [8-K Ex.99.1](https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm) |
| 3 | Probability-weighted 2030 agentic revenue effect ≈ −9% (range −5% to −12%) | **Corrected** (range mislabeled; source misattributed) | Point estimate checks out: 0.25×10 + 0.55×(−8.5) + 0.20×(−32.5) = **−8.7%**. But "−5% to −12%" is the **base-case** range, not the weighted range. Weighting the scenarios' low ends together gives **−6.5%**, and the high ends **−10.9%**. The extreme combinations give **−4% to −13%**. The cited source_url (MNTN tech page) does not support any scenario numbers. This is a pure analyst estimate with no source. | Internal arithmetic (§8 table) |
| 4 | Autonomous agent-executed buying <1% of US CTV spend in 2026 | **Unverifiable** (estimate) | The supporting facts check out. No platform discloses agentic dollar volume. PubMatic reported 80+ campaigns cumulative, up from 30 a quarter earlier, so ~50 in Q2. Digiday (2026-05-18) says TTD's agent "is not buying ads — at least not yet" and works within a "human-approved workflow". Counter-evidence to address: Vibe's CEO says MCP-enabled buying is a "large portion" of Vibe spend (AdExchanger, 2026-10-08), and Amazon reports 700+ MCP connections. Both are agent-mediated buying, although each is small relative to US CTV. The "<1%" is unsourced, so keep it labeled estimate/low confidence. | [PubMatic Q2'26 call](https://www.fool.com/earnings/call-transcripts/2026/08/13/pubmatic-pubm-q2-2026-earnings-call-transcript/); [Digiday](https://digiday.com/media-buying/inside-the-trade-desks-claude-powered-campaign-agent/) |
| 5 | Vibe read-write MCP launched 2026-07-16 for Claude/ChatGPT/Gemini; CEO: 1,000+ brands; "large portion" of spend | **Confirmed** (with nuance) | The Vibe blog is dated July 16, 2026 and says "Launch and manage campaigns through conversation". Gemini works **only via Gemini Enterprise**, not the consumer app. AdExchanger (Oct 8, 2026) quotes CEO Arthur Querou: "more than 1,000 brands have adopted Vibe's MCP integration". It also says MCP-enabled buying "accounts for a large portion of ad spend", with no percentage given. Both are CEO claims (third-party label is correct). "Closest SMB-CTV competitor" is analyst opinion. | [Vibe blog](https://www.vibe.co/blog/product-updates/ctv-just-stopped-being-a-separate-tab-introducing-the-vibe-mcp); [AdExchanger](https://www.adexchanger.com/ctv-roundup/how-does-agentic-buying-work-in-ctv/) |
| 6 | Walmart completed Vibe.co acquisition 2026-08-04; to combine with Walmart Connect; 10,000+ advertisers; ~$1.4B unverified | **Confirmed**, except price **unverifiable** | Walmart release (Bentonville, Aug 4, 2026): "With more than 10,000 advertisers…" and "combining Vibe.co's… self-service platform with Walmart Connect's commerce media capabilities". The release gives no price. The ~$1.4B trade-report figure could not be checked (search budget exhausted), so keep it flagged as unverified. | [Walmart](https://corporate.walmart.com/news/2026/08/04/walmart-completes-acquisition-of-vibe-co) |
| 7 | Hard-to-replicate assets: patented Verified Visits withholding last-touch credit; 99%+ HH graph; 98% direct supply; 200+ networks | **Confirmed as company website claims; label corrected** | The MNTN page says: "patented replacement for the missing click"; "withholds credit where another paid channel delivered the final touch"; "more than 99% of CTV households in the United States"; "98% of its ad inventory through direct relationships"; "200+ networks". **None of 99%, 98% or 200+ appears in the FY25 10-K or Q2'26 10-Q.** These are marketing claims, so the label should be "company claim", not "reported". Moat counterpoint: the 10-K says "We have applied for and obtained **minimal patent protection** for our proprietary technology." "Hard to replicate" is analyst judgment. | [mountain.com/tech](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/); [10-K FY25](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm) |
| 8 | Q2'26 S&M ~34.7% of revenue ($28.6M / $82.537M) | **Corrected** (minor) | From the 10-Q in thousands, $28,567 / $82,537 = **34.6%**. The 34.7% came from rounding S&M to $28.6M before dividing. In §8, T&D is **19.8%** ($16,354K), not 19.9%; G&A of 16.5% is correct. S&M includes **$4.1M SBC** in Q2'26, up from $0.7M in Q2'25, so S&M excluding SBC is **~29.6%** of revenue. FY25 S&M was 31.2%. The 5-10 point CAC offset should be sized against the ~30% non-SBC base. | [10-Q Q2'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm) |
| 9 | CEO on Q2'26 call: "significant agentic AI technology" for mid-market; Express launched Apr 1, 7,000+ signups, "hundreds" paying | **Confirmed** (minor wording) | Mark Douglas: "For mid-sized customers, we've added significant agentic AI technology into the platform…" The transcript says "mid-sized", not "mid-market". Express launched April 1 with 7,000+ signups "in its first 120 days". Douglas: "hundreds of those signups have become paying customers". The call was held **2026-08-04**; 2026-08-11 is the Fool transcript's publication date. | [MNTN Q2'26 call](https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/) |
| 10 | "agentic" / "AI agents" in zero MNTN SEC filings; 10-K/10-Q risk factor "may bypass us and transact directly with sellers of advertising inventory" | **Confirmed** | EDGAR full-text search (CIK 0001891027) returned 0 hits for "agentic" and for "AI agents". As a control, "Performance TV" returned 26 hits. "bypass us" returned 21 hits, including the 10-K filed 2026-02-19 and the 10-Qs filed 2026-05-11 and 2026-08-10. Exact 10-Q text: "may bypass us and transact directly with sellers of advertising inventory or through other intermediaries that compete with us." | [EFTS query](https://efts.sec.gov/LATEST/search-index?q=%22agentic%22&ciks=0001891027); [10-Q](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm) |
| 11 | PubMatic AgenticOS 80+ campaigns (30 prior qtr), ~4,000 AI-powered deals, all 5 holdcos; emerging ~15% of revenue; no agentic figure | **Confirmed** | CEO Rajeev Goel: "over 80 agentic campaigns, including with all 5 global agency holding companies… up from 30 campaigns just a quarter ago". He also cited "4,000 AI-powered deals". CFO Steven Pantelick: emerging revenues were "approximately 15% of total revenue". AgenticOS earns a buying fee via Activate, but no dollar figure is given. Note that 80 is cumulative. | [PubMatic Q2'26 call](https://www.fool.com/earnings/call-transcripts/2026/08/13/pubmatic-pubm-q2-2026-earnings-call-transcript/) |
| 12 | Butler/Till–Geloso on PubMatic AgenticOS via enterprise Claude; 5.5x lower supply-chain cost; impressions +40% vs plan | **Confirmed** (vendor claim) | Marketing Dive (2026-03-17): "reduced buy-side supply chain costs by 5.5x". The figure comes from press materials, not independent verification. Also: "40% more impressions than planned for"; "Butler/Till's enterprise Claude interface". The campaign ran in Dec 2025 across CTV, online and mobile, so it was **not CTV-only**. | [Marketing Dive](https://www.marketingdive.com/news/beverage-marketer-sees-cost-savings-with-agentic-media-buying-test/814905/) |
| 13 | Amazon Ads MCP Server open beta since Feb 2026 (Claude/ChatGPT/Gemini; campaigns, reports, billing); 700+ external connections; "expert tools" tier Sep 2026 | **Confirmed** (source split) | Digiday (2026-02-03): open beta, "AI platforms such as Claude, ChatGPT, or Gemini", agents can "create campaigns, pull reports, and manage billing". MediaPost (2026-09-29): "more than 700 external connections have been established" plus the new "expert tools" tier. Its first tool is the AMC SQL Generator, in **closed beta** in the US. The cited MediaPost piece does not name the assistants or billing; those come from Digiday. | [MediaPost](https://www.mediapost.com/publications/article/418355/amazon-ads-unveils-new-ai-tools.html); [Digiday](https://digiday.com/media-buying/ad-tech-briefing-amazon-launches-mcp-server-for-agent-driven-advertising/) |
| 14 | TTD Kokai Zuma with Koa Assistant/Agents; 32% avg CPA improvement; May 2026 agents not autonomous; Claude builds campaigns for closed beta | **Confirmed** (attribution nuance) | TTD release (2026-08-27): "an average 32% improvement in CPA performance". TTD attributes this to Zuma's modeling and forecasting, not to the Koa agents. It is a company claim. The release does not mention Claude or approval requirements. Digiday (2026-05-18): "The agent is not buying ads — at least not yet", it runs in a "human-approved workflow", and Jeff Green: "If you're a part of our closed beta, yes." The no-autonomy point is as of May 2026; post-Zuma status was not re-verified. | [TTD IR](https://investors.thetradedesk.com/news-and-events/news/news-details/2026/The-Trade-Desk-Introduces-Kokai-Zuma-the-Latest-Release-of-Kokai/default.aspx); [Digiday](https://digiday.com/media-buying/inside-the-trade-desks-claude-powered-campaign-agent/) |

**Fixes to apply downstream:**
- (a) Restate the weighted agentic effect as **≈ −9% point estimate (consistent-scenario range ≈ −6.5% to −11%)**. The table's "−5% to −12%" is the base-case range.
- (b) Q2'26 S&M is **34.6%** of revenue, or **~29.6%** excluding SBC. T&D is **19.8%**.
- (c) Relabel the 99% household, 98% direct and 200+ network figures as **company website claims**, not SEC-reported.
- (d) Add the 10-K line "minimal patent protection" as a counterpoint to the patented Verified Visits moat.
- (e) The MNTN Q2 call date is **2026-08-04**.
- (f) The Walmart-Vibe ~$1.4B price is still unverified.
