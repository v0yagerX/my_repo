# N. MNTN's own AI capabilities and the AI-upside hypotheses

**As of:** 2026-10-15. **Ticker:** MNTN (NYSE), CIK 0001891027.

**Status of Q3 2026:** not yet reported. MNTN will report Q3 2026 after the close on **Nov 4, 2026** [reported] ([MNTN IR / Business Wire, 2026-10-14](https://s205.q4cdn.com/886349678/files/doc_news/MNTN-To-Announce-Third-Quarter-2026-Financial-Results-on-November-4-2026-2026.pdf)). Everything below uses data through Q2 2026 plus product and partner announcements up to Oct 14, 2026.

**Source caveats**
- Motley Fool and Investing.com call transcripts are partly LLM-generated, and both outlets flag possible errors.
- The Fool Q1'26 page is contaminated: its prepared remarks belong to AtriCure. For Q1'26 I use only the Q&A, cross-checked against the Investing.com transcript.
- Web search was unavailable for this topic (the session's search budget was exhausted). Everything below comes from documents I fetched directly: SEC filings, MNTN IR PDFs, mountain.com, quickframe.com, Adobe Experience League, the HubSpot and Shopify app listings, Google DeepMind, Walmart and Vibe.

---

## 0. Bottom line

1. **The AI product surface is real and shipping fast. Proof of economic impact is thin.**
   - Shipped: QuickFrame AI (beta Oct 30, 2025; v3.0 GA May 5, 2026), MNTN Matched AI targeting (2024), an XGBoost "Intelligent Intent Scoring" bidder, AI media planning (2026), "agentic AI" for mid-market, and a read-write MCP server in beta (Aug 2026).
   - Not disclosed: any audited or third-party KPI linking these products to faster revenue, higher spend per customer or lower CAC. Spend per customer is falling (10-Q), and customer growth has slowed since QuickFrame AI launched.
2. **Margins: AI is a cost today, not a source of savings.**
   - Technology and development (T&D) spend is +52% y/y with T&D headcount only +13%. So the all-in cost per T&D head rose by ~35% [estimate].
   - Gross margin rose from 77% to 80%. The causes were operating leverage on a near-fixed cost base, the hosting switch to GCP and the Maximum Effort divestiture. Management calls QuickFrame AI "essentially gross margin neutral."
3. **Distribution: MNTN builds integrations into other AI and CRM stacks. It is not their default TV channel.**
   - Adobe's own GenStudio documentation shows a native CTV ad builder (Apr 2026) and an activation list that omits MNTN.
   - The HubSpot app shows "100+" installs.
4. **Data flywheel: real, but only a moderate moat.**
   - 81M conversions and 565M verified visits (Feb 2020 to Dec 2024), 4,225 advertisers, and 98% of supply through direct deals.
   - Against that: "minimal patent protection," no MRC accreditation claimed, and partly licensed training data.
5. **Market expansion: top-of-funnel numbers are large, conversion is undisclosed.**
   - 73,000+ QuickFrame AI signups in 1H26, 7,000+ Express signups, and "hundreds" of paying Express customers.
   - Conversion of QuickFrame users to paying PTV customers is **not disclosed**.

**Net:** this topic pushes MNTN slightly toward "AI winner" as a **fast adopter**. The edge is mostly commoditized: the generative models are third-party, and Adobe, Google and Vibe/Walmart offer comparable tools. My score is **+1 on a −5 to +5 scale** [estimate], low confidence until Q3/Q4'26 show Express and QuickFrame conversion.

---

## 1. AI product inventory, with dates

| Capability | What it is | Launch / status | Pricing | Source |
|---|---|---|---|---|
| **Verified Visits** (attribution) | Cross-device "replacement for the missing click." Pixel on advertiser sites. De-duplicates visits when another paid channel had the last touch (~25% of visits in a branded-search scenario). Posts to GA4 as session-start events | In use since at least Feb 2020 (the prospectus counts data from that date) | Included | [424B4, 2025-05-22](https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm); [MNTN tech blog, Mar 2026](https://mountain.com/tech/how-mntn-measures-performance-without-clicks-a-deep-dive-into-the-verified-visits-model/) |
| **MNTN Matched** (AI audience targeting) | "Keyword- and intent-based predictive audience builder for CTV using AI technologies." Scans the advertiser's site and scores households | "In 2024, we introduced MNTN Matched" [reported] | "No fee" [reported] | [10-K FY25, filed 2026-02](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm); [tech blog, Aug 2026](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/) |
| **Intelligent Intent Scoring** (bidder AI) | XGBoost "ensemble of hundreds of models." ~900 behavioral signals per household. >120M households scored. Retrained on "tens of millions of rows" | Live by Aug 2026 | n/a | [tech blog, Aug 2026](https://mountain.com/tech/the-ai-engine-behind-the-bid-inside-mntns-intelligent-intent-scoring/) |
| **Automated optimization** | 10-K: 53 signals and "hundreds of thousands of daily optimizations." Marketing pages say ">1 billion optimizations a day" and "4M bid decisions per second." These units are inconsistent | Ongoing | Included | [10-K FY25](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm); [tech blog](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/); [mountain.com home, accessed 2026-10-15](https://mountain.com/) |
| **QuickFrame** (human creator marketplace) | Acquired Dec 30, 2021 | Legacy. Creative-credit deferred revenue fell from $5.5M (Dec 2025) to $2.7M (Jun 2026) [reported] | Creative credits | [10-Q Q2'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm) |
| **QuickFrame AI** (generative video) | URL to finished ad. Multi-model orchestration. Exports to MNTN, Meta, TikTok, YouTube and Google Ads. "On average… just 12 minutes" from idea to ad [reported] | Beta **Oct 30, 2025**. Characters/products/effects **Jan 28, 2026**. **v3.0 GA May 5, 2026**, adding "new subscription tiers" | Site: Free (50 one-time credits), Starter **$39/mo**, Pro **$99/mo**, Max **$250/mo** [reported, quickframe.com, accessed 2026-10-15]. CEO on Aug 4 and Aug 11, 2026: "it is free right now… we're testing" [reported] | PRs [2025-10-30](https://s205.q4cdn.com/886349678/files/doc_news/MNTN-Unveils-QuickFrame-AI-New-AI-Platform-in-Beta-Allows-Brands-of-Any-Size-to-Create-Studio-Quality-Ads-in-Minutes-2025.pdf), [2026-01-28](https://s205.q4cdn.com/886349678/files/doc_news/MNTNs-Latest-Innovation-QuickFrame-AI-Scales-Rapidly-With-New-AI-Video-Features-Including-Consistent-Characters-Products-and-Location-EXE9B.pdf), [2026-05-05](https://s205.q4cdn.com/886349678/files/doc_news/MNTN-Releases-QuickFrame-AI-3-0-with-a-Major-Feature-Expansion-Delivering-TV-Ready-Commercials-in-Minutes-2026.pdf); [quickframe.com](https://quickframe.com/) |
| QuickFrame AI models (all third-party) | **Oct 2025:** Google Veo/Imagen, ElevenLabs, WellSaid, Stability. **Feb 2026 call:** Gemini, Sora 2, Nano Banana. **May 2026:** Seedance 2.0, fal, Kling, Pixverse, Shutterstock, Brandfetch. **Site, Oct 2026:** Seedance 2.5, Gemini Omni Flash. MNTN says only the **orchestration layer** is proprietary; CEO, Q1'26: "Others can and likely will do this… it is table stakes" | — | — | Same PRs; [Fool Q4'25 transcript, 2026-02-10](https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/); [Fool Q1'26 Q&A, 2026-05-06](https://www.fool.com/earnings/call-transcripts/2026/05/06/mntn-mntn-q1-2026-earnings-transcript/) |
| **AI media planning** | Ranked, budget-allocated network plan. Reallocates after launch. Every automated decision appears in a "live newsfeed" | "Now introducing" Feb 10, 2026. "It's with customers" May 5, 2026. Described as live Aug 2026. **Exact GA date not disclosed** | "No fee" | [Q4'25 release, 2026-02-10](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000004/mntnearningsrelease2025-q4.htm); [Investing.com Q1'26, 2026-05-05](https://www.investing.com/news/transcripts/earnings-call-transcript-mntn-q1-2026-tops-forecasts-stock-rises-93CH-4661246); [tech blog, Aug 2026](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/) |
| **"Agentic AI" for mid-market** | "We've added significant agentic AI technology into the platform… to give our customers control of the daily decision-making." No feature specifics | Mentioned Aug 4, 2026 | n/a | [Fool Q2'26, 2026-08-11](https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/) |
| **MCP server (beta)** | "Read-write Model Context Protocol server, operable from Claude, ChatGPT, and other leading AI assistants." Read: campaigns, audiences, creatives, reporting. Write: budgets, creative weights, targeting, launching campaigns | Described in the Aug 2026 tech blog only. **No press release, launch date, usage or pricing.** Not listed on the integrations page | n/a | [tech blog](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/); [integrations page, accessed 2026-10-15](https://mountain.com/performance-tv/integrations/) |
| **Public API** | Reporting API 3.8.0 and Async Batch Export API 3.8.0 (OpenAPI 3.0.1). **Read-only.** The 10-K says data "can also be pulled… through our API" | Live | n/a | [api3.mountain.com/docs](https://api3.mountain.com/docs) (specification retrieved 2026-10-15); [10-K FY25](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm) |
| **Tiers: Express / Pro / Premium** | Express is the small-business edition, "live in minutes… from any device." Pro is mid-market. Premium covers upper mid-market and "Super Premium" guaranteed inventory | **Express Apr 1, 2026.** Premium inventory push from **Jan 2026** | Not disclosed. mountain.com says "No minimums" and also "as little as $2,000" | [Fool Q2'26](https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/); [Investing.com Canaccord, 2026-08-11](https://www.investing.com/news/transcripts/mntn-at-canaccord-conference-growth-broadens-beyond-early-adopters-93CH-4852453); [mountain.com/go-big](https://mountain.com/go-big/) |
| **Premium inventory** | Q1'26: March Madness, NHL playoffs, MLB, reality TV. Q2'26: **FIFA World Cup on Telemundo**, HBO's House of the Dragon, Love Island, Tour de France. "Soon the NFL." Magnite partnership (Jan 22, 2026) adds live sports and pause ads, plus an "AI-driven contextual taxonomy." **The World Cup is not a separate driver in guidance** | 2026 | n/a | [Q1'26 release](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000038/mntnearningsrelease2026-q1.htm); [Q2'26 release](https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm); [Magnite/MNTN, 2026-01-22](https://mountain.com/news/mntn-and-magnite-turn-live-streamings-biggest-moments-into-performance-tv-for-growth-brands/) |

**Integrations, by date** (32 listed on [mountain.com/performance-tv/integrations](https://mountain.com/performance-tv/integrations/), accessed 2026-10-15)
- Shopify app: listed Mar 29, 2023.
- ZoomInfo: Jul 1, 2025.
- PubMatic: Oct 13, 2025.
- Northbeam: Dec 3, 2025.
- Magnite: Jan 22, 2026.
- HubSpot: Jun 15, 2026.
- Upwave expansion: Jun 18, 2026.
- Klaviyo: Sep 9, 2026.
- AppsFlyer: Sep 28, 2026.
- Tealium (into MNTN Matched): Oct 14, 2026.
- **Not found:** Salesforce. Shopify is listed only as a pixel/web-tracking integration. Adobe and Google appear only as claims in the Q2'26 8-K (section 4).

**What SEC filings do *not* mention:** Express, MCP, "agentic" and AI media planning appear in none of the FY25 10-K, Q1'26 10-Q or Q2'26 10-Q (text search of the filings). The filings name only MNTN Matched and "our video creative platform that leverages generative AI" as AI products [reported] ([10-Q Q2'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm)).

---

## 2. Does MNTN's AI produce better results? (Evidence quality matters.)

| Claim | Value | Who measured | Quality |
|---|---|---|---|
| MNTN Matched vs "traditional audiences" | **6x** site traffic, **2x** revenue, **½** CPA. Footnote: "customer averages" [reported] | MNTN | Self-reported. No sample size, period or method ([Matched page, accessed 2026-10-15](https://mountain.com/performance-tv/matched/)) |
| Same product, other MNTN pages | **6x** visits and **3x** revenue ([Tealium PR, 2026-10-14](https://mountain.com/press/mntn-brings-tealium-first-party-data-into-mntn-matched-to-advance-ai-powered-tv-targeting/)). **5.8x** traffic and **3.2x ROAS** ([tech blog, Aug 2026](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/)). **7x** traffic, **2.4x ROAS**, ½ CPA ([home page](https://mountain.com/)) [reported] | MNTN | The figures disagree across pages, which lowers confidence |
| Intent-scoring rollout | **+44% ROAS**, **+37% visit rate** vs advertisers not yet migrated [reported] | MNTN internal holdout and A/B tests | Self-reported, but the design is reasonable ([blog, Aug 2026](https://mountain.com/tech/the-ai-engine-behind-the-bid-inside-mntns-intelligent-intent-scoring/)) |
| Content targeting plus AI Media Planning | "**129% lower** incremental CPA" than AI Media Planning alone [reported] | MNTN | A cost cannot fall by more than 100%, so the claim as stated is impossible. Quality flag |
| Rockerbox | **70%** of advertisers see MNTN CPAs **18–33% lower** than their top acquisition channels [third-party, relayed by MNTN; undated] | Rockerbox | Third-party, but no date and quoted only through MNTN |
| Northbeam (beta) | 32 advertisers over 30 days: **~1.8x MER** and **~90% net-new** site visits [third-party] | Northbeam | Third-party, but a small sample in a joint PR ([2025-12-03](https://s205.q4cdn.com/886349678/files/doc_news/MNTN-and-Northbeam-Give-Marketers-a-Trusted-Way-to-Verify-CTV-Performance-and-Acquire-New-Consumers-2025.pdf)) |
| Upwave brand lift | ~50 campaigns, >1B impressions. **94%** lifted at least one brand KPI. Average **+1.7%** aided awareness [third-party] | Upwave | Third-party. Measures brand lift, not performance ([2026-06-18](https://mountain.com/press/upwave-and-mntn-expand-partnership-to-scale-brand-outcomes-on-connected-tv/)) |
| Aggregate | MNTN campaigns "generated over **$18 billion** in revenue for our customers in 2025" [reported, CEO] | MNTN (Verified Visits) | Unaudited. Last-touch, de-duplicated, but self-attributed ([Fool Q4'25](https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/)) |
| Head-to-head tests | "Never lost a head-to-head performance test in streaming TV" [reported, CEO, Q1'26] | MNTN | Unverifiable. The Investing.com rendering is garbled ([2026-05-05](https://www.investing.com/news/transcripts/earnings-call-transcript-mntn-q1-2026-tops-forecasts-stock-rises-93CH-4661246)) |
| **QuickFrame AI → ROAS** | **No measured evidence.** CEO: "more creative equals more return on ad spend" (Q3'25). "Go-live rates up," but "not quantifying yet" (Q1'26). None of the 22 case studies on the site credits AI creative; the QuickFrame case studies describe human "Makers" | — | Gap ([case studies, accessed 2026-10-15](https://mountain.com/case-studies/)) |

**Does AI raise spend per customer?** Not visibly.
- The 10-Q says the rise in active customers "was offset by a **decrease in average spend per customer**" as MNTN expands into small businesses [reported] ([10-Q Q2'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm)).
- TTM revenue (ex-Maximum Effort) per TTM active customer fell **~9%**, from **$81.2K to $74.2K** [estimate].
  - Q2'25: (53.4 + 64.2 + 59.1 + 68.5) / 3,020.
  - Q2'26: (70.0 + 87.1 + 73.7 + 82.5) / 4,225.
  - Quarterly revenue is from the [Q3'25](https://www.sec.gov/Archives/edgar/data/1891027/000189102725000019/mntnearningsrelease2025-q3.htm) and [Q2'26](https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm) releases.
- Same-customer "expansion rate" is "well north of 115%" [reported, Q4'25 and Q2'26 calls]. The disclosed SMB net revenue retention (NRR) was **111%** (Q1'25), up from **108%** (FY24) [reported] ([424B4](https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm)). That is healthy, but nothing ties it to AI.

---

## 3. Margins: what T&D buys, headcount, and whether AI drives gross margin

### 3a. Technology and development spend

| Period | T&D ($M) | y/y | % of revenue | Capitalized software ($M) | T&D + capitalized, % of revenue [estimate] | T&D headcount y/y |
|---|---|---|---|---|---|---|
| FY23 | 27.9 | — | 15.8% | n/a | — | — |
| FY24 | 32.7 | +17% | 14.5% | 9.9 | 18.9% | — |
| FY25 | 49.2 | **+50.8%** | 17.0% | 12.5 | 21.3% | **avg +31%** |
| 1H26 | 31.0 | +52.2% | 19.8% | 7.0 (vs 6.2) | 24.3% (vs 19.9%) | +18% |
| Q2'26 | 16.4 | **+52.4%** | 19.8% (vs 15.7%) | — | — | **+13%** |

All values [reported] except where marked. Sources: [424B4](https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm), [10-K FY25](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm), [10-Q Q1'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000040/mntn-20260331.htm), [10-Q Q2'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm).

**What the money is for**
- **Filings:** personnel (+$4.3M in Q2'26) "to maintain and support further development of our platform," plus **$1.0M** of "incremental tools" [reported]. T&D stock-based compensation was only $1.2M vs $0.9M [reported], so SBC does not explain the growth.
- **Management:**
  - QuickFrame AI has a "pretty decent-sized team… releases multiple times a week" (Q2'26 call).
  - The largest share of engineering works on "MNTN Matched and the matching models" (Canaccord, 2026-08-11).
  - Other projects: the Express, Pro and Premium rebuild, agentic AI, AI media planning, and the MCP server.
- **All-in T&D cost per head rose ~35% y/y in Q2'26** (1.524 / 1.13 − 1), versus ~24% in Q1'26 and ~15% in FY25 [estimate]. This fits pricier AI/ML talent, AI tooling and higher compensation. The company does not break this out.
- Internal-use software amortization is up **$1.2M** in Q2'26 "due to disposals of obsolete software" [reported]. That is consistent with platform rewrites [estimate].

### 3b. Headcount and productivity

| Date | Total FTEs | Product development and engineering | Sales, marketing and customer success | Other [estimate] |
|---|---|---|---|---|
| Dec 2022 | 417 | — | — | — |
| Dec 2023 | 478 | — | — | — |
| Mar 2024 | 467 | — | — | — |
| Mar 2025 | 502 | 179 (36%) | 202 | 121 |
| Dec 2025 | 534 | **231 (43%)** | 211 | 92 |

Sources [reported]: [DRS 2024](https://www.sec.gov/Archives/edgar/data/1891027/000110465924060066/filename1.htm), [424B4](https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm), [10-K FY25](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm).

- **Engineering share:** the CEO says "half" (Q2'26) and "over 50%" (Q1'26). The 10-K count is **43%** at YE25. The gap may come from the April 2026 restructuring or from a different definition. No headcount has been disclosed after December 2025.
- **Changes since then** [reported, 10-Q Q2'26]:
  - Cost-of-revenue headcount: **−38%** y/y, "as a result of the strategic restructuring plan."
  - T&D headcount: **+13%**.
  - G&A headcount: +10%.
  - S&M average headcount: −2% in 1H26.
  - S&M added 53 hires in Q4'25 (CFO).
- **Restructuring** (approved Apr 28, 2026; completed by Jun 30, 2026) [reported, 10-Q Q2'26]:
  - $1.49M in charges: S&M $1.14M, cost of revenue $0.26M, T&D $0.06M, G&A $0.03M.
  - The company does not disclose the number of roles cut or attribute any of it to AI.
- **Revenue per FTE** (net revenue / year-end FTEs) [estimate]:
  - FY23: $176.3M / 478 = **$369K**.
  - FY25: $290.1M / 534 = **$543K**, up 47%.
  - Gross profit per FTE: $258K → **$419K**, up 62%.
  - Most of this pre-dates generative AI. It comes from flat S&M headcount from 2024 to 2025 (CFO, Q4'25) and from revenue leverage.
- **Support cost per customer:** not disclosed. S&M per TTM-active customer was ~$24.9K (FY25: 90.4 / 3,632) and ~$22.9K (TTM Q2'26: (44.4 + 52.3) / 4,225) [estimate].
- **Management's AI productivity claims, all unquantified:**
  - "AI-native, using AI to build faster" (Q2'26).
  - AI is used "to become more efficient in our own operations to drive margin expansion" (Q1'26, Investing.com).
  - "Our model scales with efficiency, not headcount" (Q3'25).
  - MNTN runs at least one AI-made video ad a week in its own marketing (Q4'25).
  - Internal monitoring: chart-building that took analysts "hours" now takes seconds ([tech blog, Sep 2026](https://mountain.com/tech/how-an-automotive-plant-inspired-mntns-new-production-operations-system/)).
- The 10-Q also notes that MNTN "may use AI Technologies offered by third parties to develop… our own software code" (IP risk) [reported].

### 3c. Is AI behind the 77% → 80% gross margin?

**Mostly no.**

Gross margin excluding Maximum Effort [reported, Q3'25 and Q2'26 releases]:
- 2024: Q1 70.0%, Q4 78.9%.
- 2025: Q1 72%, Q2 77%, Q3 79%, Q4 82%.
- 2026: Q1 81%, Q2 80%.

Most of the expansion happened **before** QuickFrame AI launched (Oct 30, 2025).

**Q2'26 y/y bridge** [reported drivers; arithmetic is estimate]:
- Revenue +20.6% ($68.46M → $82.54M) against cost of revenue +2.2% ($15.90M → $16.24M). At the old ratio, cost of revenue would have been $19.17M, so ~$2.9M ≈ **3.5pp** was saved.
- Disclosed line items:
  - Amortization: **+$1.2M** (a headwind).
  - Platform fees: −$0.6M.
  - Personnel: **−$0.4M** (headcount −38%).
  - Hosting: 1H26 −$2.7M, of which Q1 was −$2.5M, implying ~−$0.2M in Q2.
- The 1H26 hosting saving came from the switch to **GCP** (cutover Oct 2025) and "changes in data vendors" ([Investing.com Q3'25, 2025-11-04](https://www.investing.com/news/transcripts/earnings-call-transcript-mntn-q3-2025-sees-strong-earnings-beat-stock-dips-93CH-4332329); [10-Q Q1'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000040/mntn-20260331.htm)).
- So the expansion is **leverage on a near-fixed cost of revenue**, plus hosting.

**QuickFrame AI's own cost:** "There are some gross margin costs, but… essentially gross margin neutral," because hosting efficiencies "make room for" the AI models [reported, Q2'26 call]. The hosting savings are a **one-time** step, so a free AI product that scales becomes a margin headwind later [estimate].

**Upper bound on AI's contribution:** if all of the −$0.4M cost-of-revenue personnel saving reflected AI replacing human ad production, that is ~**0.5pp** of the 350bp (0.4 / 82.5) [estimate]. Related signals:
- Creative-credit deferred revenue was run down: $5.5M → $2.7M, including $1.7M recognized in Q1'26 from expired credits "associated with amended contracts" [reported].
- Non-PTV (creative) revenue was only ~$0.7M in Q2'25 (PTV $67.8M of $68.5M) [estimate from the [Q2'25 release](https://www.sec.gov/Archives/edgar/data/1891027/000189102725000009/mntn-20250805xexx991.htm)].
- So AI replacing human creative barely affects revenue.

**Targets:** long-term gross margin **75–80%** and adjusted EBITDA **35–40%** [guidance, CFO, Q4'25 call].

---

## 4. Distribution partnerships: default TV channel, or one of many?

| Partner | What exists | Date | Terms | Traction | Assessment |
|---|---|---|---|---|---|
| **Adobe** | MNTN 8-K: "**Adobe integrating QuickFrame AI into GenStudio for Performance Marketing**" [reported] | 2026-08-04 | Undisclosed | None disclosed | **Not default.** Adobe shipped its own "**GenStudio for CTV**" builder (release notes 2026.04.16): "the workflow… runs entirely in GenStudio… there is no separate CTV app or publisher embed" (doc updated 2026-10-06). Adobe's bulk-activation channels (2026-09-15) are Meta, LinkedIn, CM360, Amazon Ads, Innovid, TikTok, YouTube, ChatGPT and The Trade Desk. **No MNTN or QuickFrame mention** in Adobe documentation [third-party] ([release notes](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/release-notes); [create-CTV doc](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/create/create-ctv)) |
| **Google** | "Google recognizing QuickFrame AI as an early adopter of its latest **Gemini Omni Flash** models" [reported] | 2026-08-04 | None | — | A model-supplier relationship, not distribution. Google's model card (2026-08-27) names no partners ([DeepMind](https://deepmind.google/models/model-cards/gemini-omni-flash/)). QuickFrame exports to Google Ads and YouTube |
| **HubSpot** | Native app. TV exposure is written to contact records; lists sync daily. "First CTV platform" to do so | 2026-06-15 | **Free** app; "Requires MNTN subscription" | **100+ installs, 0 reviews** [third-party, accessed 2026-10-15] | Early, small ([PR](https://s205.q4cdn.com/886349678/files/doc_news/MNTN-Brings-Advanced-Data-Attribution-to-CTV-with-First-of-its-Kind-HubSpot-Integration-2026.pdf); [listing](https://ecosystem.hubspot.com/marketplace/apps/mntn)) |
| **Klaviyo** | Two-way sync. TV exposure triggers email and SMS flows. "One of MNTN's largest technology partners" | 2026-09-09 | Undisclosed | No numbers | One of many CRM channels ([PR](https://s205.q4cdn.com/886349678/files/doc_news/MNTN-and-Klaviyo-Integrate-Performance-TV-with-CRM-2026.pdf)) |
| **Shopify** | Pixel app | Listed 2023-03-29 | Free to install | **9 reviews** (5.0) [third-party] | Small ([listing](https://apps.shopify.com/mntn)) |
| Tealium, AppsFlyer, Northbeam, Upwave, ZoomInfo | Audience and measurement integrations | Jul 2025 – Oct 2026 | Mixed. Some are absorbed by MNTN ("one cost… the cost of media"); with Northbeam the customer contracts directly [reported, Q2'26 call] | — | Plumbing, not distribution |
| **MCP (Claude, ChatGPT)** | Read-write beta | Blog Aug 2026 | — | None disclosed | **Parity, not first.** Vibe's read-write MCP launched 2026-07-16, claiming "the first time any CTV platform has been available inside an AI assistant" ([Vibe](https://www.vibe.co/blog/product-updates/ctv-just-stopped-being-a-separate-tab-introducing-the-vibe-mcp)). Walmart closed its acquisition of Vibe (>10,000 advertisers) on **2026-08-04** ([Walmart](https://corporate.walmart.com/news/2026/08/04/walmart-completes-acquisition-of-vibe-co)) |
| Agencies | Agency-led accounts grew ~4x in 2025; 45 verified agencies | 2025-09-29 | Rewards and credits | ">90% of PTV advertisers do not use an agency" (Q1'26) | Growing channel. Partnership commissions rose **+$1.2M** y/y in Q2'26 S&M [reported, 10-Q] |

**Conclusion:**
- MNTN is a diligent integrator. It plugs TV into the CRMs and attribution tools SMBs already use, and it is early with MCP.
- There is **no evidence that any AI platform routes CTV demand to MNTN by default.**
- Adobe, the most important "AI workflow" claim, has its own native CTV creative and activates through Innovid, The Trade Desk and Amazon.

---

## 5. Data flywheel: scale, credentials, replicability

| Asset | Figure | Label / source |
|---|---|---|
| Verified visits / conversions | **~565M** visits and **81M** conversions, Feb 2020 – Dec 2024 | [reported] [424B4](https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm) |
| Devices | ~**400M** devices analyzed (424B4). "Hundreds of millions" (10-K) | [reported] |
| Households | Reach to "99%" of US TV households (424B4). ">100M unique TV households" segmentable (10-K). ">120M" scored (blog, Aug 2026). "About **142M**" (CEO, Canaccord). The figures differ | [reported] |
| Signals | 53 optimization signals (10-K). ~900 per household (blog). ">1 trillion… signals… every day" (blog) | [reported] |
| Advertisers | **4,225** TTM active (Q2'26). Pixels on "tens of thousands of websites" | [reported] |
| Supply | **98%** via direct relationships with **200+** networks (blog). ">99%" through private-marketplace (PMP) deals (Q2'26 call). The home page says "150+" networks | [reported] |
| Price flywheel | Premium inventory cost down ~**8% per quarter** on average since Q1'22 | [reported] 424B4 |
| Downstream measurement | 30+ integrations. Data sent to ~11 attribution platforms | [reported] Q4'25 call; blog |
| **Patents** | "We have applied for and obtained **minimal patent protection**… our patent strategy is still in its early stages" (10-K). The blog calls Verified Visits "patented," with **no patent number** | [reported] [10-K FY25](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm) |
| **MRC accreditation** | **None claimed** in filings or on MNTN's pages. Validation relies on partners (LiftLab, Haus, Northbeam, Rockerbox, iSpot, DoubleVerify and others) | [reported, absence] |
| Data dependency | "Certain of the data that we use in training our own proprietary AI Technologies is **licensed from third parties**" | [reported] [10-Q Q2'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm) |

**Replicability** [estimate, qualitative]
- **Hard to copy:** a CTV-exposure-to-site-conversion dataset labelled across thousands of SMB pixels, plus packaged direct deals for small budgets.
- **Easy to copy:**
  - The household graph: Amazon, Google/YouTube, Roku and Walmart (Vizio + Vibe) hold larger first-party identity and commerce data.
  - The generative creative layer: all third-party models, and "table stakes" by the CEO's own description.
  - The UI: MCP lets agents drive any platform.
- **Moat rating:** moderate. It sits in attribution and conversion-trained bidding, not in AI creative.

---

## 6. Market expansion: does AI creative bring first-time TV advertisers?

| Metric | Value | Source |
|---|---|---|
| QuickFrame AI signups | 5,000 "within the first month" (Q4'25 call). **~36K in Q1'26** [estimate: 73K − 37K]. **37K+ in Q2'26** and **73K+ in 1H26** [reported] | [Fool Q4'25](https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/); [Fool Q2'26](https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/) |
| Usage inside the customer base | "Nearly all the Express customers, and… like 30%, 40% of our mid-market customers" [reported, CEO] | [Canaccord, 2026-08-11](https://www.investing.com/news/transcripts/mntn-at-canaccord-conference-growth-broadens-beyond-early-adopters-93CH-4852453) |
| QuickFrame → paying PTV | **Not disclosed.** CEO: "a lot of the QuickFrame users are creators. They're not necessarily the marketers" | Q2'26 call |
| Express | >**7,000** signups in 120 days. "**Hundreds**" paying. SMB spend "approximately… **$15,000** a year" (gross vs net not stated). Mid-market spend "deep six figures" | Q2'26 call; Canaccord |
| First-time-TV share | 97% (Q2'25 / Q3'25 releases). ~95% (10-K). ">90%" (HubSpot PR, Jun 2026). The share is not rising | [reported] |
| TTM active-customer net adds | Q1'25 +422, Q2'25 +373, Q3'25 +296. **After the AI launch:** Q4'25 +316, Q1'26 +242, Q2'26 +351 | [reported counts, Q2'26 release; differences are estimate] |
| Active-customer growth | TTM: 67% → 63% → 46% → **40%**. Period-active: 85% (Q2'25) → 26% (Q1'26) → **24%** (Q2'26) | [reported] releases and 10-Qs |

**Funnel arithmetic** [estimate]
- Express: "hundreds" of 7,000 is a **~3–10%** conversion (200–700 payers). At ~$15K a year that is **~$3–10M** of annualized spend, under 3% of FY26 revenue guidance even if all of it were net revenue.
- QuickFrame AI: even if all **593** net TTM adds in 1H26 came from QuickFrame AI, conversion would be **≤0.8%** of 73K signups. Gross adds are unknown because churn is not disclosed.
- Standalone QuickFrame AI subscriptions: 2–5% of ~150K annual signups at ~$60/month gives **~$2–5M ARR**. That is immaterial before 2027.
- **Caveat:** management says customer adds are "largely within our control" through S&M pacing. Customer counts are therefore a noisy test of AI pull.

---

## 7. AI-upside hypothesis scorecard (for the 2026–2030 model)

| # | Hypothesis | Evidence today | My probability it is material by 2028 [estimate] | Model implication [estimate] |
|---|---|---|---|---|
| H1 | AI creative (QuickFrame AI + Express) widens the SMB funnel into TV | Large signups, weak disclosed conversion, no customer re-acceleration yet | ~45% | Base: Express adds 1–3 pts of growth in 2027–28. Bull: TTM customers above 8K by 2028 |
| H2 | AI targeting and bidding raise ROAS, which drives retention and spend | Self-reported +44% ROAS and 2–6x claims; same-customer expansion above 115%; some third-party support (Northbeam, Rockerbox) | ~60% | Supports NRR of 110–120%. Does not offset falling average spend per customer from mix |
| H3 | AI cuts MNTN's own costs | Gross margin gains are non-AI; T&D +52%; restructuring not tied to AI | ~30% for opex savings by 2028 | Model T&D at **19–21% of revenue** in 2026–27, leveraging to ~15–18% by 2030 only with ~20% growth. Hold gross margin at 78–81% |
| H4 | AI ecosystems (Adobe, Google, HubSpot, MCP) become a low-CAC channel | Integrations exist, small traction, Adobe omits MNTN, Vibe/Walmart at parity | ~25% | Do not lower S&M % for this before evidence appears |
| H5 | The data flywheel deepens the moat as AI raises the value of conversion data | Real assets; weak IP and credentials | ~50% (moat holds, not widens) | Supports a stable take rate in the base case |
| H6 | QuickFrame AI becomes a standalone revenue line | Tiers priced at $39–250 a month; CEO says "free right now"; no revenue disclosed | ~20% for more than $15M of revenue by 2030 | Exclude from base. Bull option $5–20M by 2030 |

**Overall for this topic: +1 on a −5 to +5 scale** [estimate].
- MNTN is a credible, fast AI adopter in its niche.
- But its AI advantages are either self-reported (targeting) or commoditizing (creative, UI/agents). Meanwhile AI raises its cost base (T&D) and lowers barriers for well-funded rivals (Adobe's CTV builder, Walmart-Vibe MCP).

**What would move the score:**
- Q3/Q4'26 disclosure of QuickFrame → PTV conversion.
- Express payer counts and revenue.
- Re-acceleration of TTM net adds above ~450 a quarter.
- T&D growth converging toward revenue growth.
- Any Adobe- or Google-side announcement naming MNTN as an activation partner.

---

## 8. Data gaps (explicit)

- QuickFrame AI paying subscribers, revenue, inference cost per video, and conversion to PTV customers: **not disclosed**.
- Express payer count (only "hundreds"), revenue, minimums and pricing: **not disclosed**.
- MCP usage, launch date and agent-sourced spend; AI media-planning GA date and adoption: **not disclosed**.
- Adobe integration terms and status: only in MNTN's 8-K line; **no Adobe-side confirmation found**. The same applies to Google's "early adopter" recognition.
- Headcount after Dec 2025, roles cut in the April 2026 restructuring, and any AI attribution: **not disclosed**.
- Support or customer-success cost per customer, and engineering productivity metrics: **not disclosed**.
- An independent audit of the Matched and Intent-Scoring lifts, and MRC accreditation: **none found**.
- Patent numbers for Verified Visits: **not disclosed**. Patent databases were not searched (search budget exhausted).
- Gross ad spend and take rate: **not disclosed**, which limits any spend-per-customer analysis.

---

## Sources

1. MNTN, "MNTN To Announce Third Quarter 2026 Financial Results on November 4, 2026," Business Wire / IR PDF, 2026-10-14. https://s205.q4cdn.com/886349678/files/doc_news/MNTN-To-Announce-Third-Quarter-2026-Financial-Results-on-November-4-2026-2026.pdf
2. MNTN, Q2 2026 earnings release (8-K ex-99.1), SEC, 2026-08-04. https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm
3. MNTN, Form 10-Q for Q2 2026, SEC, 2026-08. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm
4. MNTN, Form 10-Q for Q1 2026, SEC, 2026-05. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000040/mntn-20260331.htm
5. MNTN, Form 10-K for FY2025, SEC, 2026-02/03. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm
6. MNTN, 424B4 IPO prospectus, SEC, 2025-05-22. https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm
7. MNTN, Draft registration statement (2024), SEC. https://www.sec.gov/Archives/edgar/data/1891027/000110465924060066/filename1.htm
8. MNTN, Q4 2025 earnings release, SEC, 2026-02-10. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000004/mntnearningsrelease2025-q4.htm
9. MNTN, Q1 2026 earnings release, SEC, 2026-05-05. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000038/mntnearningsrelease2026-q1.htm
10. MNTN, Q3 2025 earnings release, SEC, 2025-11-04. https://www.sec.gov/Archives/edgar/data/1891027/000189102725000019/mntnearningsrelease2025-q3.htm
11. MNTN, Q2 2025 earnings release, SEC, 2025-08-05. https://www.sec.gov/Archives/edgar/data/1891027/000189102725000009/mntn-20250805xexx991.htm
12. MNTN, "MNTN Unveils QuickFrame AI…," IR PDF, 2025-10-30. https://s205.q4cdn.com/886349678/files/doc_news/MNTN-Unveils-QuickFrame-AI-New-AI-Platform-in-Beta-Allows-Brands-of-Any-Size-to-Create-Studio-Quality-Ads-in-Minutes-2025.pdf
13. MNTN, "QuickFrame AI Scales Rapidly With New AI Video Features…," IR PDF, 2026-01-28. https://s205.q4cdn.com/886349678/files/doc_news/MNTNs-Latest-Innovation-QuickFrame-AI-Scales-Rapidly-With-New-AI-Video-Features-Including-Consistent-Characters-Products-and-Location-EXE9B.pdf
14. MNTN, "MNTN Releases QuickFrame AI 3.0…," IR PDF, 2026-05-05. https://s205.q4cdn.com/886349678/files/doc_news/MNTN-Releases-QuickFrame-AI-3-0-with-a-Major-Feature-Expansion-Delivering-TV-Ready-Commercials-in-Minutes-2026.pdf
15. MNTN, "…First of its Kind HubSpot Integration," IR PDF, 2026-06-15. https://s205.q4cdn.com/886349678/files/doc_news/MNTN-Brings-Advanced-Data-Attribution-to-CTV-with-First-of-its-Kind-HubSpot-Integration-2026.pdf
16. MNTN, "MNTN and Klaviyo Integrate Performance TV with CRM," IR PDF, 2026-09-09. https://s205.q4cdn.com/886349678/files/doc_news/MNTN-and-Klaviyo-Integrate-Performance-TV-with-CRM-2026.pdf
17. MNTN, "MNTN and Northbeam…," IR PDF, 2025-12-03. https://s205.q4cdn.com/886349678/files/doc_news/MNTN-and-Northbeam-Give-Marketers-a-Trusted-Way-to-Verify-CTV-Performance-and-Acquire-New-Consumers-2025.pdf
18. MNTN, "MNTN and ZoomInfo Announce Partnership…," IR PDF, 2025-07-01. https://s205.q4cdn.com/886349678/files/doc_news/MNTN-and-ZoomInfo-Announce-Partnership-to-Revolutionize-B2B-Advertising-on-Television-2025.pdf
19. PubMatic / MNTN partnership release, IR PDF, 2025-10-13. https://s205.q4cdn.com/886349678/files/doc_news/PubMatic-and-MNTN-Partner-to-Expand-Premium-CTV-Market-Driving-Net-New-Advertiser-Demand-and-Unlocking-a-10-Publisher-Revenue-Lift-20-9ATCJ.pdf
20. MNTN, "Agency-Led Accounts Grow 4x in 2025," IR PDF, 2025-09-29. https://s205.q4cdn.com/886349678/files/doc_news/MNTN-Agency-Led-Accounts-Grow-4x-in-2025-as-Demand-for-Performance-TV-Surges-2025.pdf
21. MNTN, "Expands Executive Team…," IR PDF, 2026-03-10. https://s205.q4cdn.com/886349678/files/doc_news/MNTN-Expands-Executive-Team-to-Support-Growth-of-Performance-TV-2026.pdf
22. MNTN, "Recognized as a 2025 Inc. Power Partner," IR PDF, 2025-11-10. https://s205.q4cdn.com/886349678/files/doc_news/MNTN-Recognized-as-a-2025-Inc--Power-Partner-Award-Winner-2025.pdf
23. MNTN, "Tealium First-Party Data Into MNTN Matched," mountain.com, 2026-10-14. https://mountain.com/press/mntn-brings-tealium-first-party-data-into-mntn-matched-to-advance-ai-powered-tv-targeting/
24. MNTN, "Expands Attribution with AppsFlyer," mountain.com, 2026-09-28. https://mountain.com/press/mntn-expands-attribution-with-appsflyer-to-drive-better-performance-tv-results/
25. MNTN / Upwave, "Expand Partnership…," mountain.com, 2026-06-18. https://mountain.com/press/upwave-and-mntn-expand-partnership-to-scale-brand-outcomes-on-connected-tv/
26. MNTN / Magnite, "Turn Live Streaming's Biggest Moments Into Performance TV," GlobeNewswire via mountain.com, 2026-01-22. https://mountain.com/news/mntn-and-magnite-turn-live-streamings-biggest-moments-into-performance-tv-for-growth-brands/
27. MNTN Tech Blog, "The Technology That Puts Performance in Performance TV," Aug 2026. https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/
28. MNTN Tech Blog, "The AI Engine Behind the Bid: Inside MNTN's Intelligent Intent Scoring," Aug 2026. https://mountain.com/tech/the-ai-engine-behind-the-bid-inside-mntns-intelligent-intent-scoring/
29. MNTN Tech Blog, "How MNTN Measures Performance Without Clicks…," Mar 2026. https://mountain.com/tech/how-mntn-measures-performance-without-clicks-a-deep-dive-into-the-verified-visits-model/
30. MNTN Tech Blog, "How an Automotive Plant Inspired MNTN's New Production Operations System," Sep 2026. https://mountain.com/tech/how-an-automotive-plant-inspired-mntns-new-production-operations-system/
31. MNTN, MNTN Matched product page, accessed 2026-10-15. https://mountain.com/performance-tv/matched/
32. MNTN, Integrations page, accessed 2026-10-15. https://mountain.com/performance-tv/integrations/
33. MNTN, home page, accessed 2026-10-15. https://mountain.com/
34. MNTN, case-study library, accessed 2026-10-15. https://mountain.com/case-studies/
35. MNTN, "To Go Big, Think Small (Business)," undated, accessed 2026-10-15. https://mountain.com/go-big/
36. QuickFrame AI home and pricing, accessed 2026-10-15. https://quickframe.com/
37. MNTN Reporting API 3.8.0 docs, accessed 2026-10-15. https://api3.mountain.com/docs
38. Motley Fool, MNTN Q2 2026 earnings call transcript, 2026-08-11 (call 2026-08-04). https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/
39. Motley Fool, MNTN Q1 2026 transcript (Q&A only; prepared remarks contaminated), 2026-05-06. https://www.fool.com/earnings/call-transcripts/2026/05/06/mntn-mntn-q1-2026-earnings-transcript/
40. Motley Fool, MNTN Q4 2025 earnings call transcript, 2026-02-10. https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/
41. Investing.com, MNTN Q1 2026 call transcript, 2026-05-05. https://www.investing.com/news/transcripts/earnings-call-transcript-mntn-q1-2026-tops-forecasts-stock-rises-93CH-4661246
42. Investing.com, MNTN Q3 2025 call transcript, 2025-11-04. https://www.investing.com/news/transcripts/earnings-call-transcript-mntn-q3-2025-sees-strong-earnings-beat-stock-dips-93CH-4332329
43. Investing.com, "MNTN at Canaccord conference…," 2026-08-11. https://www.investing.com/news/transcripts/mntn-at-canaccord-conference-growth-broadens-beyond-early-adopters-93CH-4852453
44. Adobe, GenStudio for Performance Marketing release notes (updated 2026-09-16). https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/release-notes
45. Adobe, "Create a connected TV experience" (updated 2026-10-06). https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/create/create-ctv
46. Google DeepMind, Gemini Omni Flash model card, 2026-08-27. https://deepmind.google/models/model-cards/gemini-omni-flash/
47. HubSpot App Marketplace, MNTN listing, accessed 2026-10-15. https://ecosystem.hubspot.com/marketplace/apps/mntn
48. Shopify App Store, MNTN listing, accessed 2026-10-15. https://apps.shopify.com/mntn
49. Vibe, "CTV just stopped being a separate tab: Vibe MCP," 2026-07-16. https://www.vibe.co/blog/product-updates/ctv-just-stopped-being-a-separate-tab-introducing-the-vibe-mcp
50. Walmart, "Walmart Completes Acquisition of Vibe.co," 2026-08-04. https://corporate.walmart.com/news/2026/08/04/walmart-completes-acquisition-of-vibe-co

---

## Verification (adversarial check)

*Checked 2026-10-15 by an independent fact-checker against primary sources: the SEC filings themselves (10-Q Q2'26, 10-K FY25, 424B4, and the Q2'25, Q3'25, Q4'25, Q1'26 and Q2'26 earnings releases), MNTN IR PDFs, mountain.com, quickframe.com, Adobe Experience League, Walmart and Vibe. Web search was unavailable (budget exhausted), so the "absence" checks rely only on the pages fetched directly. Two transcript pages (Fool Q2'26, Fool Q4'25) contained embedded instructions addressed to AI tools; these were ignored.*

| # | Finding | Verdict | Correct value / note | Evidence |
|---|---|---|---|---|
| 1 | QuickFrame AI: 37K+ signups in Q2'26, 73K+ in 1H26; free, monetization being tested; PTV conversion not disclosed | **Confirmed** | CEO, Q2'26 call: "over 37,000 QuickFrame AI signups in Q2, bringing us to over 73,000 signups year-to-date"; "we're making it available at no charge"; "In terms of monetization… we're looking at that." Canaccord: "currently free, with monetization tests under way." **Nuance:** quickframe.com (accessed 2026-10-15) sells paid tiers (Starter $39, Pro $99, Max $250 a month; Free = 50 one-time credits), and the 2026-05-05 PR announced "new subscription tiers." "Free" probably refers to PTV advertisers' use; the 2025-10-30 PR offered free ads "for use on MNTN Performance TV." | [Fool Q2'26](https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/); [Canaccord](https://www.investing.com/news/transcripts/mntn-at-canaccord-conference-growth-broadens-beyond-early-adopters-93CH-4852453); [quickframe.com](https://quickframe.com/) |
| 2 | Express: >7,000 signups in 120 days, "hundreds" paying, ~$15K/yr SMB spend; implied 3–10% conversion and $3–10M spend | **Confirmed (reported parts); flag on label** | Fool Q2'26: "over 7,000 signups for Express in the first 120 days," "hundreds… have become paying customers," launched April 1. **Caveats:** (a) the $15K is the CEO's figure for small businesses generally ("small businesses spend about $15,000 annually"), not for Express payers specifically, so Express ARPU may be lower; (b) the Investing.com Canaccord page is an auto-written summary with date errors (it says "first half of 2024"); (c) the 3–10% and $3.0–10.5M figures are **[estimate]** (200–700 payers × $15K), but the finding carries the label "reported." Arithmetic checks: 200/7,000 = 2.9%, 700/7,000 = 10%. | [Fool Q2'26](https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/); [Canaccord](https://www.investing.com/news/transcripts/mntn-at-canaccord-conference-growth-broadens-beyond-early-adopters-93CH-4852453) |
| 3 | TTM net adds: Q4'25 +316, Q1'26 +242, Q2'26 +351 vs +422/+373/+296; TTM growth 67% → 40%; period-active growth 85% → 24% | **Confirmed** | TTM counts from the Q3'25/Q4'25/Q2'26 releases: Q4'24 2,225; Q1'25 2,647; Q2'25 3,020; Q3'25 3,316; Q4'25 3,632; Q1'26 3,874; Q2'26 4,225. All differences match. TTM growth: Q3'25 66.6%, Q4'25 63%, Q1'26 46%, Q2'26 39.9%. Period-active: 85% (Q2'25 release), 24% (Q2'26 10-Q). **Nuance:** Q2'26 (+351) was a sequential re-acceleration from +242 and above Q3'25/Q4'25 levels, coinciding with the Express launch. "No acceleration" holds against 1H25, not against 2H25. | [Q2'26 release](https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm); [Q4'25 release](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000004/mntnearningsrelease2025-q4.htm); [Q2'25 release](https://www.sec.gov/Archives/edgar/data/1891027/000189102725000009/mntn-20250805xexx991.htm) |
| 4 | TTM ex-ME revenue per TTM active customer: $81.2K → $74.2K | **Confirmed (estimate; rounding)** | (53.4+64.2+59.1+68.5)/3,020 = $81.19K; (70.0+87.1+73.7+82.5)/4,225 = $74.15K; change **−8.7%** (not −8.6%). The quarterly ex-ME revenue figures match the Q2'26 release table (Q4'25 revised to $87.1M). The direction matches the 10-Q text: "offset by a decrease in average spend per customer." | [10-Q Q2'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm); [Q2'26 release](https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm) |
| 5 | T&D +52.4% ($16.4M vs $10.7M; 19.8% vs 15.7% of revenue), headcount +13%, cost per head +~35%, T&D plus capitalized software 24.3% vs 19.9% of 1H revenue | **Confirmed** | 10-Q: T&D $16,354K vs $10,732K, +52.4%; 19.8% vs 15.7% of revenue; "headcount increased by 13%." 1H: T&D $30,965K plus capitalized software $6,991K over revenue $156,210K = 24.3%; prior year ($20,340K + $6,185K) / $132,972K = 19.9%. Cost per head: 1.524/1.13 − 1 = +34.9% **[estimate]**. | [10-Q Q2'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm) |
| 6 | GM expansion 77% → 80% driven by leverage, the GCP hosting switch and the Maximum Effort divestiture, not AI; "essentially gross margin neutral"; LT targets 75–80% GM, 35–40% EBITDA | **Corrected (driver attribution)** | Confirmed: GM 76.8% → 80.3%; revenue +20.6% vs cost of revenue +2.2%; 1H26 hosting −$2.7M; the "essentially gross margin neutral" quote (Q2'26 call); LT targets 75–80% / 35–40% (CFO, Q4'25 call). **Wrong:** for the Q2'25 → Q2'26 comparison, the **Maximum Effort divestiture is not a driver**, because it closed Apr 1, 2025, so Q2'25 already had $0 ME revenue (ex-ME GM was 77% in both cases). **Hosting is not cited** in the 10-Q's Q2 cost-of-revenue bridge either; the 1H hosting saving fell mostly in Q1. The Q2 drivers the 10-Q cites are revenue leverage, platform fees −$0.6M and personnel −$0.4M (restructuring, headcount −38%), offset by amortization +$1.2M. ME and hosting explain the 2024 → 1H26 arc, not this y/y. The "not AI" conclusion stands. | [10-Q Q2'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm); [Q2'26 release](https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm); [Fool Q4'25](https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/) |
| 7 | AI results inconsistent across pages: 6x/2x/½ CPA, 6x/3x, 5.8x/3.2x ROAS, 7x/2.4x ROAS; +44% ROAS / +37% visits; "129% lower CPA" | **Confirmed, except "129%": unverifiable** | Matched page: "6x more Site Traffic," "2x more Revenue," "2x lower CPA*" (customer averages). Tealium PR: "6x more site visits and 3x more revenue." Tech blog: "5.8x more site traffic and 3.2x higher ROAS." Home page: "7x more site traffic," "2.4x higher ROAS," "½ the CPA." Intent-scoring blog: "an **estimated** 44% increase in return on ad spend and 37% lift in visit rate" in a "controlled rollout" vs advertisers not yet migrated. The page does not call these figures holdout/A/B results, so §2's "internal holdout and A/B tests" overstates the rigor. The **"129% lower" CPA claim was not found** on the intent-scoring blog, the Matched, home, inventory or optimization pages, or the Tealium PR. Also, the optimization page says "651,000 times per day," a third unit for the ">1 billion optimizations" row in §1. | [Matched](https://mountain.com/performance-tv/matched/); [Tealium PR](https://mountain.com/press/mntn-brings-tealium-first-party-data-into-mntn-matched-to-advance-ai-powered-tv-targeting/); [tech blog](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/); [home](https://mountain.com/); [intent-scoring blog](https://mountain.com/tech/the-ai-engine-behind-the-bid-inside-mntns-intelligent-intent-scoring/); [optimization](https://mountain.com/performance-tv/optimization/) |
| 8 | Expansion rate "well north of 115%"; SMB NRR 111% (Q1'25) from 108% (FY24) | **Confirmed; caveat on comparability** | 424B4: "For the three months ended March 31, 2025, our SMB Net Revenue Retention Rate was 111%, which increased from 108% for the year ended December 31, 2024." CFO, Q4'25 and Q2'26 calls: "well north of 115%." **Caveat:** the "expansion rate" is an undefined management metric (current customers' spend vs the same customers' spend a year earlier). It may exclude churned customers, so it should not be read as an update to the defined NRR. | [424B4](https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm); [Fool Q4'25](https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/) |
| 9 | Adobe: MNTN 8-K says Adobe is integrating QuickFrame AI; Adobe's docs show a native CTV builder and an activation list without MNTN | **Confirmed** | The Q2'26 release (8-K ex-99.1) has the exact line "Adobe integrating QuickFrame AI into GenStudio for Performance Marketing." Adobe release notes (updated 2026-09-16): CTV ads in Create (2026.04.16); bulk activation (2026.09.15) to Meta, LinkedIn, CM360, Amazon Ads, Innovid, TikTok, YouTube, ChatGPT and The Trade Desk; no MNTN, Mountain or QuickFrame. Create-CTV doc (updated 2026-10-06): "runs entirely in GenStudio… there is no separate CTV app or publisher embed." **Caveat:** absence from the docs does not prove there is no integration in progress. | [Adobe release notes](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/release-notes); [Adobe create-CTV](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/create/create-ctv); [Q2'26 release](https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm) |
| 10 | MNTN MCP beta-only; Vibe read-write MCP 2026-07-16; Walmart closed Vibe (>10,000 advertisers) 2026-08-04 | **Confirmed** | Tech blog (Aug 2026) heading: "Agentic Layer: The MNTN MCP (beta)," "read-write… operable from Claude, ChatGPT." Not on the integrations page. Vibe post dated July 16, 2026: create campaigns by conversation, "first time any CTV platform has been available inside an AI assistant." Walmart release, Aug 4, 2026: acquisition completed; Vibe has "more than 10,000 advertisers." The absence of an MNTN MCP PR could not be search-verified. | [tech blog](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/); [Vibe](https://www.vibe.co/blog/product-updates/ctv-just-stopped-being-a-separate-tab-introducing-the-vibe-mcp); [Walmart](https://corporate.walmart.com/news/2026/08/04/walmart-completes-acquisition-of-vibe-co) |
| 11 | 10-K: "minimal patent protection," "patent strategy… early stages"; Verified Visits "patented" with no number; no MRC; licensed training data | **Confirmed** | 10-K FY25: "We have applied for and obtained minimal patent protection…" and "our patent strategy is still in its early stages." No "MRC" or "Media Rating Council" in the 10-K or the Q2'26 10-Q; none on the home page. 10-Q/10-K: "Certain of the data that we use in training our own proprietary AI… is licensed from third parties." Tech blog: "Verified Visits™ is MNTN's patented replacement for the missing click" (no number). | [10-K FY25](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm); [10-Q Q2'26](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm) |
| 12 | Standalone QuickFrame AI ≈ $2–5M ARR, under 2% of FY26 guidance of $347–357M | **Confirmed as estimate (inputs verified)** | FY26 guidance of $347–357M is confirmed (Q2'26 release). Tiers are $39/$99/$250 a month at standard rates, with discounted first months of $32/$65/$125, so a ~$60 blended price is plausible. 150K annual signups ≈ 2 × 73K. 2–5% × 150K × $60 × 12 = $2.2–5.4M, which is 1.5% of guidance at the top end. Conversion and ARPU are assumptions; no paid-subscriber data is disclosed. Correctly labeled estimate. | [quickframe.com](https://quickframe.com/); [Q2'26 release](https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm) |
| 13 | Q3'26 results after the close on Nov 4, 2026 | **Confirmed** | IR PDF / Business Wire, 2026-10-14: results "after the close of the U.S. markets on Wednesday, November 4, 2026," with a webcast at 4:30 p.m. ET. | [IR PDF](https://s205.q4cdn.com/886349678/files/doc_news/MNTN-To-Announce-Third-Quarter-2026-Financial-Results-on-November-4-2026-2026.pdf) |
| 14 | QuickFrame AI beta 2025-10-30; v3.0 GA 2026-05-05 with subscription tiers; third-party models | **Confirmed** | 2025-10-30 PR: "beta launch of QuickFrame AI"; Google (Veo and Imagen), ElevenLabs, WellSaid Labs, Stability AI; "just 12 minutes." 2026-05-05 PR: "Now out of beta… Now widely available," "new subscription tiers," Seedance 2.0, fal, Kling, Pixverse, WellSaid, ElevenLabs, Shutterstock, Brandfetch. Gemini and Sora 2 come from the Q4'25 call and were not re-checked here. | [2025-10-30 PR](https://s205.q4cdn.com/886349678/files/doc_news/MNTN-Unveils-QuickFrame-AI-New-AI-Platform-in-Beta-Allows-Brands-of-Any-Size-to-Create-Studio-Quality-Ads-in-Minutes-2025.pdf); [2026-05-05 PR](https://s205.q4cdn.com/886349678/files/doc_news/MNTN-Releases-QuickFrame-AI-3-0-with-a-Major-Feature-Expansion-Delivering-TV-Ready-Commercials-in-Minutes-2026.pdf) |

**Net:** every load-bearing number checked matches primary sources. There is one material correction: the gross-margin driver attribution in #6, where the Maximum Effort divestiture and hosting do not explain the Q2'25 → Q2'26 change. Label and wording fixes:
- The Express funnel math (#2) is an estimate.
- The $15K is general SMB spend, not Express ARPU.
- The +44% ROAS is described as "estimated," not as a formal A/B result.
- The "129% lower CPA" source could not be found.
- The spend-per-customer decline rounds to −8.7%.
- The >115% "expansion rate" is not the defined NRR metric.
