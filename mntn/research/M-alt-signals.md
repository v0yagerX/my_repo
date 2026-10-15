# M. Alternative data and ground-level signals: MNTN, Inc. (NYSE: MNTN)

*As of 2026-10-15. Analyst dossier, topic M of the MNTN deep-dive.*

**Labels used throughout**

| Label | Meaning |
|---|---|
| [reported] | Company filing, company website or company help center |
| [guidance] | Company guidance |
| [third-party] | Outside data or commentary |
| [estimate] | My own derivation; the math is shown |

**Q3 2026 status.** Q3 2026 results have **not** been released.

- EDGAR's submissions feed (pulled 2026-10-15) shows no filing after a Form 4 on 2026-10-07.
- The last 8-K was filed 2026-09-08 and covers Item 5.02 only: the election of director Michael Katz ([EDGAR filing index](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001891027&type=&dateb=&owner=include&count=100); [8-K, 2026-09-08](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000089/mntn-20260903.htm)).
- Q3'25 was reported on 2025-11-04, so Q3'26 is likely due in early November 2026 [estimate].

**How the research was done.** The shared web-search budget was exhausted before this topic started, so no search-engine queries were run. Everything below came from three kinds of source:

- **Pages fetched directly:** SEC EDGAR, MNTN's Greenhouse job-board API, MNTN's help center, Similarweb, Tranco, BuiltWith, Wappalyzer, the Shopify App Store, the HubSpot Marketplace, Trustpilot, Blind, LinkedIn, Built In, the Google Trends API, Marketecture, AdExchanger and Digiday.
- **SEC filings already downloaded** by earlier workstreams.
- **Pages that blocked automated access:** G2, Capterra, TrustRadius, Glassdoor, Indeed, Comparably, RepVue, Reddit and the Wayback Machine. Each is flagged as a gap where it matters.

---

## 0. Bottom line

1. **Headcount is falling while revenue grows, which is the clearest internal "AI and automation leverage" signal.**
   - Full-time headcount was **451** at 2026-06-30, against **472** a year earlier (−4.4%) and **542** at 2026-03-31 [reported, 10-Qs].
   - Over the same year, revenue grew +21% and TTM active customers grew +40% [reported].
   - TTM revenue per FTE rose from **~$369K (FY23)** to **~$543K (FY25)** to **~$695K (TTM Q2'26)** [estimate].
   - Cost-of-revenue headcount fell **38% y/y** after an April 2026 cut of about 76 people [reported].
   - Job postings explicitly target "AI deflection" in support and "agentic workflows" in go-to-market (GTM) operations [reported].
2. **Hiring is restarting, but only on the GTM side and with a different model.**
   - 21 roles are open (≈4.7% of headcount) [estimate].
   - **13 of 21 sit in "Revenue"**: five agency-channel roles, five "emerging vertical" hunters (four Sales Executives plus a Head of Industry), and an **on-site Austin inside-sales team**. That team breaks from the "100% remote" model [reported, Greenhouse].
   - **No core software, ML or data-science engineering roles are open**, even though the CEO says "half of the company's headcount is in engineering" [third-party transcript].
3. **External footprint signals are flat to down for MNTN and sharply up for Vibe.co, now owned by Walmart.**
   - *Tranco rank.* mountain.com averaged **3,169** in Q3'26 against **2,740** in Q3'25 (a worse rank). Vibe.co improved from **20,433** to **12,194** over the same period [third-party; averages are my estimate].
   - *Similarweb, September 2026.* mountain.com fell **−12.8% m/m** and vibe.co rose **+16.1%** [third-party].
   - *BuiltWith.* Vibe has **9,790** live pixel sites against MNTN's **5,804**. MNTN also has **7,513 "expired"** sites, against Vibe's 898 [third-party].
   - *Northbeam.* Tracked spend growth in H1'26 was reportedly **Vibe +1,900% vs MNTN +29%** [third-party, low-to-medium confidence].
   - These are noisy proxies, but they all point the same way.
4. **Attribution skepticism is real and long-standing.**
   - Verified Visits is household-level, view-through attribution (full TV view, then a site visit from any device in the household within a **7-day retargeting / 14-day prospecting** default window) [reported, help center].
   - Ari Paparo, who discloses that he sits on Vibe's board, called the weakness "correlation ≠ causation" [third-party].
   - MNTN has responded by adding **10% holdout incrementality** reporting and **8 third-party measurement integrations in about 9 months** (Haus, Northbeam, Freshpaint, HubSpot, AppsFlyer, Upwave, WorkMagic, Prescient AI) [reported].
5. **Customer-review data is thin and mostly inaccessible.**
   - Shopify App Store: **5.0 from 9 reviews**, all dated 2023–Nov 2024, with none since [third-party].
   - HubSpot Marketplace: **"100+ installs", 0 reviews** [third-party].
   - Trustpilot: **2 reviews, both 1-star**; one alleges a media-cost markup [third-party].
   - G2, Capterra, TrustRadius and Reddit could not be read (HTTP 403).
6. **Employee sentiment is stable and decent, with recurring cons.**
   - Blind rates MNTN **4.2/5 on 13 reviews** (Jan 2024–Apr 2026) [third-party].
   - Recurring cons: CEO-driven priority churn and limited career growth. One June 2025 reviewer wrote that the company "Jumped on the 'mention Ai for investor bait' bandwagon."
   - MNTN cites **Ad Age Best Places to Work** in 2024, 2025 and 2026 [reported].

**Net read for "AI victim vs AI winner":** about neutral to slightly negative (≈ −0.5 on a −3 to +3 scale, low confidence).

- *Internal signals* (cost to serve, headcount, product velocity) fit an "AI winner on costs."
- *External demand signals* (web, pixel and spend footprint) show an AI-native, retail-media-backed rival taking share at the margin.
- *Attribution* remains the main point of skepticism among practitioners.

---

## 1. Signal scorecard

| # | Signal | Latest reading | Direction for MNTN | Reliability |
|---|---|---|---|---|
| 1 | Reported FT headcount (SEC) | 451 at 2026-06-30; −4.4% y/y, −16.8% q/q [reported] | Efficiency + (also a GTM reset) | **High** (audited-adjacent disclosure) |
| 2 | Open roles (Greenhouse API, 2026-10-15) | 21 open; 13 Revenue, 6 Engineering, 1 Technology, 1 Marketing; 0 ML/core software engineering [reported] | Mixed: GTM rebuild, engineering frozen | Medium (point-in-time; no history) |
| 3 | Layoffs | ~76-person RIF approved 2026-04-28; $1.49M charge, 77% in S&M [reported] | GTM restructuring | **High** |
| 4 | Similarweb visits | mountain.com: 109.2K over the last 3 months; −12.8% m/m in Sep-26 [third-party] | Negative vs Vibe (+16.1%) | **Low** (panel estimate for a small B2B site) |
| 5 | Tranco rank (DNS + CrUX blend) | 3,115 on 2026-10-14; best was 2,414 in Aug-25 [third-party] | Flat/negative; Vibe rising sharply | Low-Medium (proxy for pixel footprint, not revenue) |
| 6 | BuiltWith pixel install base | 5,804 live, 7,513 expired [third-party] | Large historical churn; smaller than Vibe | Low-Medium (crawler coverage) |
| 7 | Google Trends ("MNTN", US) | Q3'26 average 14.8 vs IPO-week peak of 100 [third-party] | Fading to near pre-IPO level | **Low** (ticker and name ambiguity) |
| 8 | Reviews (Shopify, HubSpot, Trustpilot) | 5.0/9 (stale); 100+ installs/0 reviews; 1-star ×2 [third-party] | Neutral; too small to judge | **Very low** |
| 9 | Employee reviews (Blind) | 4.2/5, 13 reviews [third-party] | Neutral | Low (tiny sample) |
| 10 | Product release log | 15 releases in H2'25, 17 in H1'26, 7 in Jul-26, 0 logged Aug–mid-Oct-26 [reported] | Strong cadence, skewed to measurement; recent logging gap | Medium |
| 11 | Practitioner commentary | Attribution skepticism (view-through/household); doubt about the take rate [third-party] | Negative tail risk | Medium (few sources; conflicts disclosed) |

---

## 2. Hiring, headcount and layoffs

### 2.1 Reported headcount (SEC filings)

| Date | FT team members | Of which S&M + customer success | Of which product + engineering | Source |
|---|---|---|---|---|
| 2022-12-31 | 417 | n/d | n/d | DRS/A 2024 [reported] |
| 2023-12-31 | 478 | 190 | 153 ("engineers") | DRS/A 2024 [reported] |
| 2024-03-31 | 467 | n/d | n/d | 424B4 [reported] |
| 2025-03-31 | 502 | 202 | 179 | 424B4 [reported] |
| 2025-06-30 | 472 (after the Maximum Effort divestiture on 2025-04-01) | n/d | n/d | Q2'25 10-Q [reported] |
| 2025-09-30 | 498 | n/d | n/d | Q3'25 10-Q [reported] |
| 2025-12-31 | 534 | 211 | 231 | FY25 10-K [reported] |
| 2026-03-31 | 542 | n/d | n/d | Q1'26 10-Q [reported] |
| **2026-06-30** | **451** | n/d (≈150–170 [estimate]) | ≈ half of total, per CEO [third-party transcript] | Q2'26 10-Q [reported] |

Sources:
- DRS/A, accession 0001104659-24-060066: https://www.sec.gov/Archives/edgar/data/1891027/000110465924060066/filename1.htm
- 424B4, 2025-05-22: https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm
- 10-Q Q2'25: https://www.sec.gov/Archives/edgar/data/1891027/000189102725000012/mntn-20250630.htm
- 10-Q Q3'25: https://www.sec.gov/Archives/edgar/data/1891027/000189102725000022/mntn-20250930.htm
- 10-K FY25, 2026-02-19: https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm
- 10-Q Q1'26, 2026-05-11: https://www.sec.gov/Archives/edgar/data/1891027/000189102726000040/mntn-20260331.htm
- 10-Q Q2'26, 2026-08-10: https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm

**Mix shift.** Product and engineering rose from **32%** of headcount (153/478, Dec-23) to **36%** (179/502, Mar-25) to **43%** (231/534, Dec-25) [estimate from reported counts].

The CEO said on the Q2'26 call: "half of the company's headcount is in engineering … We're leveraging AI across the organization, especially within engineering, where we're AI-native, using AI to build faster" [third-party transcript, [Motley Fool, 2026-08-11](https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/)].

Engineering growth is slowing. Technology and development (T&D) headcount grew **+23% y/y in Q1'26** and **+13% y/y in Q2'26** [reported, 10-Qs].

**Departmental moves disclosed in the 10-Qs** [reported]:
- Cost-of-revenue headcount was **−38% y/y** in Q2'26, attributed to the restructuring.
- S&M average headcount was **−7% y/y** in Q1'26.
- G&A headcount was **+10% y/y** in Q2'26.

### 2.2 The April 2026 restructuring

- **Approval and scope.** Approved 2026-04-28. The plan "includes a reduction of the Company's workforce by approximately 76 employees." The estimated charge was ~$1.7M [reported, Q1'26 10-Q, Note 13].
- **Final cost.** $1.491M, completed by 2026-06-30 [reported, Q2'26 10-Q, Note 14]. By line:

  | Expense line | Charge | Share |
  |---|---|---|
  | S&M | $1.141M | 76.5% |
  | Cost of revenue | $0.261M | 17.5% |
  | T&D | $0.064M | 4.3% |
  | G&A | $0.025M | 1.7% |

- **Size.** 76/542 ≈ **14%** of the March-31 workforce [estimate].
- **Implied heads by function** [estimate]: about 58 in S&M, 13 in COR, 3 in T&D and 1–2 in G&A. This assumes equal severance per head, which is crude because seniority varies.
- **Headcount bridge.** 542 − 76 = 466, but reported headcount was 451. That leaves about **15 further net departures or unfilled backfills** in Q2 [estimate].
- **Context.**
  - On the Q4'25 call, management cited **53 new S&M hires** in that quarter, yet said "with the 53 hires, we are flat in headcount in sales and marketing from the '24 to the '25" [third-party transcript, [Fool, 2026-02-10](https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/)]. That implies high S&M turnover.
  - The cut followed within one quarter of those hires, and most of it fell on S&M.
  - Management did not explain the RIF on the calls I could read (see dossier B).
- **New language in the filings.**
  - Q2'26 10-Q, first appearance: "Efficiency initiatives, workforce reductions and **changes to our workplace model** may affect our ability to attract and retain qualified personnel" [reported]. The 10-K and Q1'26 10-Q have no such wording.
  - Q2'26 10-Q: "we expect to **strategically** grow headcount." Earlier filings said "continue to grow headcount" [reported].
- **WARN and layoff trackers.**
  - MNTN does not appear in California's WARN report for 2026-07-01 to 2026-10-14 ([EDD WARN report](https://edd.ca.gov/siteassets/files/jobs_and_training/warn/warn_report1.xlsx), accessed 2026-10-15) [third-party]. The prior-period file covering April–June 2026 was not checked.
  - The Texas WARN page returned no data. layoffs.fyi could not be parsed (embedded Airtable).
  - MNTN has an "entirely remote workforce" [reported, 10-K], so a WARN filing may not have been triggered.
  - No press release on the RIF appears on MNTN's press page ([mountain.com/press](https://mountain.com/press/), accessed 2026-10-15).

### 2.3 Open roles snapshot (Greenhouse API, 2026-10-15)

Source: `boards-api.greenhouse.io/v1/boards/mntn/jobs` (MNTN's careers page links to job-boards.greenhouse.io/mntn). **21 postings** [reported]. Greenhouse departments: Revenue 13, Engineering 6, Technology 1, Marketing 1. Product, QuickFrame and "MNTN Select" have **0** [reported].

My functional regrouping [estimate]:

| Function | # | Roles | Notes |
|---|---|---|---|
| Direct new-business sales | 8 | Associate AE; Director, Inside Sales; Manager, Inside Sales; Head of Industry (Restaurant, Automotive & Travel); Sales Executive ×4 (Enterprise Tech; Media & Entertainment; Restaurants & Dining; Travel & Hospitality) | The 3 inside-sales roles are **on-site in Austin** ("This role works onsite from our Austin office"). The vertical roles are "hunter" roles with no "established pipeline or fully developed playbook" in MNTN's "Emerging Verticals business" |
| Agency channel | 5 | Agency Lead; Agency Partner; Agency Partner Specialist; Sr. Manager, Agency Partner Management; Strategic Program Manager, Agency | Agencies are called "one of MNTN's fastest-growing partner segments." The Specialist supports "a large portfolio of agencies … through Intercom" |
| GTM systems / RevOps / finance analytics | 4 | GTM Engineer; Sr. Manager, GTM Systems Delivery; Manager, Revenue Forecasting & Analytics; Sr. Data Analyst, Finance | GTM Engineer: "building agentic workflows and AI-assisted tooling that reduce manual handoffs across lead qualification, enrichment, and routing." Postings reference an internal "AI Engineering" team |
| Product / technical | 3 | Solutions Architect (pre-sales); Technical Program Manager (internal forecasting and lead-enrichment products); Content Designer | Content Designer: "Content is the source our AI draws from"; success measured by "self-service resolution, AI deflection" |
| Marketing (contract) | 1 | Contractor, Email Designer | 3-month contract |
| **Core software / ML / data-science engineering** | **0** | — | — |
| **Direct-customer support / account management** | **0** | — | — |

- **Recency.** 17 of 21 were first published between 2026-09-01 and 2026-10-13. The oldest is from 2026-07-10 [reported].
- **Openings as % of headcount:** 21/451 ≈ **4.7%** [estimate].
- **Boilerplate in every posting:** "We're committed to innovation that empowers, not replaces. At MNTN, AI is a tool for growth, enhancing efficiency while keeping a people-first approach." Each posting also claims Ad Age Best Places to Work 2026 [reported].
- **Compensation:** no pay ranges are posted.

**Interpretation** [estimate]:

1. Post-RIF hiring is a **GTM redesign**, not a pullback:
   - an agency channel (management: >90% of PTV advertisers use no agency, but agencies are "an important and growing channel" [third-party transcript, [Fool Q1'26, 2026-05-06](https://www.fool.com/earnings/call-transcripts/2026/05/06/mntn-mntn-q1-2026-earnings-transcript/)]);
   - vertical teams ("We built vertical teams…" [Q2'26 call]); and
   - a co-located inside-sales hub.
2. The filings show partnership commissions up **$1.2M y/y in Q2'26** [reported]. That fits the agency push.
3. The move into "emerging verticals" (enterprise tech, M&E, restaurants, travel) suggests management sees a need for new demand pools beyond the core DTC/e-commerce SMB base.
4. Zero open engineering roles supports the claim that AI is substituting for engineering headcount growth. It could equally reflect a budget freeze.

**Change versus earlier snapshots.** This could not be measured:
- The Wayback Machine was unreachable (connection reset; WebFetch refused the domain).
- LinkedIn job counts require a login.
- The only historical anchors are the SEC headcount series and management's statements:
  - "we haven't added headcount in sales in over three years" (Q2'25 call, per dossier C);
  - 53 S&M hires in Q4'25;
  - the April 2026 RIF; and
  - the October 2026 rebuild.

**Offshore.** No offshore locations appear in the postings, which are US/Remote plus Austin. The 10-K mentions no offshore centers [reported]. *Not measurable:* contractor or outsourcing use beyond the disclosed marketing-services contractor (dossiers A and L).

### 2.4 Productivity math [estimate]

| Metric | FY23 | FY25 | TTM Q2'25 | TTM Q2'26 |
|---|---|---|---|---|
| Revenue ($M) [reported] | 176.3 | 290.1 | 245.2 (ex-ME, sum of 4 quarters; dossier A) | 313.3 (sum of 4 quarters; dossier A) |
| Period-end FT headcount [reported] | 478 | 534 | 472 | 451 |
| **Revenue per FTE** | **$369K** | **$543K** | **$519K** | **$695K (+34% y/y)** |
| TTM active PTV customers [reported] | 1,426 | 3,632 | 3,020 | 4,225 |
| **Customers per FTE** | 3.0 | 6.8 | 6.4 | **9.4 (+46% y/y)** |
| Customers per S&M/CS FTE | 7.5 (1,426/190) | 17.2 (3,632/211) | n/d | ~25–28 (assumes 150–170 S&M/CS) |

Caveats:
- FY23 and FY25 include Maximum Effort revenue and staff until 2025-04-01.
- The customer count includes paid trial customers ("three months or fewer") [reported, 10-K].
- Smaller SMB customers need less service, so part of the gain is mix rather than AI.

---

## 3. Web traffic and digital footprint

### 3.1 Similarweb (free tier, "September 2026" snapshot, accessed 2026-10-15) [third-party]

| Domain | Total visits, last 3 months | m/m change | Global rank | US rank | Top source (desktop) |
|---|---|---|---|---|---|
| mountain.com | 109.2K (≈36K/month [estimate]) | **−12.77%** | #319,221 | #85,619 | Direct 44.99% |
| vibe.co | 179.5K (≈60K/month [estimate]) | **+16.07%** | #226,881 | #70,274 | Direct 46.96% |
| quickframe.com | 59.1K (≈20K/month [estimate]) | **−32.91%** | #452,340 | #166,634 | Direct 30.72% |
| tatari.tv | 20.6K | −1.95% | #1,354,954 | #685,623 | Organic 44.11% |

Sources: https://www.similarweb.com/website/mountain.com/ ; https://www.similarweb.com/website/vibe.co/ ; https://www.similarweb.com/website/quickframe.com/ ; https://www.similarweb.com/website/tatari.tv/

- **Other mountain.com metrics:** US 78.7% of traffic, bounce rate 40.4%, 3.08 pages per visit, average visit 1:27 [third-party].
- **Reliability: low.**
  - Similarweb panel estimates for sites with under ~100K visits a month are imprecise.
  - The free tier gives no monthly history, so no 2025–2026 trend could be built.
  - Logged-in platform use may be undercounted.
- **QuickFrame cross-check.** MNTN reported **~37,000 QuickFrame AI sign-ups in Q2'26** [reported, Q2'26 call per dossiers B and I]. If Similarweb's ~59K Q3 visits were accurate, Q3 sign-ups would likely be well below Q2's. But Similarweb conflicts with Tranco, where quickframe.com's September-2026 rank of 281,981 was its best on record (§3.2). **Treat as unresolved and ask about it on the Q3 call** [estimate].

### 3.2 Tranco research ranking (lower is better) [third-party]

Tranco lists combine CrUX, Farsight, Majestic, Cloudflare Radar and Umbrella over 30 days, using a Dowdall rule. The list configuration was confirmed via the [Tranco API](https://tranco-list.eu/api/lists/date/2025-10-15). Daily list files were downloaded from tranco-list.eu.

| List date | mountain.com | vibe.co | quickframe.com | universalads.com | steelhouse.com (legacy) | tatari.tv |
|---|---|---|---|---|---|---|
| 2024-07-15 | 3,099 | 59,988 | >1M | — | 57,305 | 735,658 |
| 2024-10-15 | 3,044 | 35,529 | 972,284 | — | 56,578 | >1M |
| 2025-01-15 | 3,217 | 33,886 | >1M | — | 67,833 | 562,041 |
| 2025-04-15 | 2,986 | 29,010 | 724,823 | — | 73,687 | 599,599 |
| 2025-07-15 | 2,865 | 21,245 | 593,826 | — | 80,541 | 638,043 |
| 2025-08-15 | **2,414** (best) | 19,414 | 429,892 | — | — | — |
| 2025-10-15 | 2,706 | 20,467 | 292,330 | — | 80,604 | 525,168 |
| 2026-01-15 | 2,569 | 19,945 | 560,905 | — | 125,829 | >1M |
| 2026-04-15 | 3,030 | 19,066 | 425,631 | 147,891 | 127,932 | 856,991 |
| 2026-07-15 | 3,161 | 12,949 | 552,315 | 115,795 | 148,334 | 925,770 |
| 2026-10-14 | 3,115 | **11,545** | 483,164 | 114,940 | 154,483 | 968,517 |

Additional monthly mountain.com ranks [third-party]:

| Month | Rank |
|---|---|
| Feb-25 | 3,168 |
| Mar-25 | 3,089 |
| May-25 | 2,877 |
| Jun-25 | 2,868 |
| Sep-25 | 2,940 |
| Nov-25 | 2,669 |
| Dec-25 | 2,641 |
| Feb-26 | 2,609 |
| Mar-26 | 2,899 |
| May-26 | 3,010 |
| Jun-26 | 3,146 |
| Aug-26 | 3,217 |
| Sep-26 | 3,128 |

**Period averages** [estimate]:

| Period | Months averaged | mountain.com | vibe.co |
|---|---|---|---|
| 1H25 | Jan–Jun | 3,034 | — |
| 2H25 | Jul–Dec | 2,706 | — |
| 1H26 | Jan–Jun | 2,877 | — |
| Q3'25 | Jul–Sep | 2,740 | 20,433 |
| Q3'26 | Jul–Sep | 3,169 | 12,194 |

Implied relative "popularity," assuming score ∝ 1/rank (Zipf) [estimate]:
- **mountain.com ≈ −13.5% y/y** (2,740/3,169 = 0.865).
- **vibe.co ≈ +68% y/y** (20,433/12,194 = 1.68).
- The rank gap between mountain.com and vibe.co narrowed from about **11.7x** (Oct-24) to **3.7x** (Oct-26).

**What this measures.** Similarweb ranks mountain.com about #319K globally by human visits, while Tranco ranks it about #3,100. Tranco's position therefore comes mainly from **DNS lookups of MNTN's tags and ad-serving endpoints** (for example, MNTN's image pixel is served from px.mountain.com [reported, [help center](https://help.mountain.com/en/articles/7251381-install-image-pixels)]). In effect, it proxies **MNTN's pixel and ad-delivery footprint**: the number of advertiser sites carrying the tag times their traffic.

The mountain.com footprint improved through Aug-25 to Feb-26 and then returned to its 2024 level. Over the same period Vibe's footprint grew about 5x since mid-2024. Reported revenue still grew 21%, so this series is not a revenue tracker. Possible reasons it diverges:
- server-side or GA4-based event flows replacing browser pixels;
- a mix shift toward advertisers with smaller websites;
- Tranco methodology noise.

Reliability: **low-medium**. It is useful as a relative competitive-footprint indicator against Vibe.

### 3.3 Pixel install base (BuiltWith "Usage Statistics" pages, accessed 2026-10-15) [third-party]

| Technology | Live sites | US live | Expired (used historically) | Expired / ever-detected | Live sites outside top-1M |
|---|---|---|---|---|---|
| **MNTN** | **5,804** | 5,018 | **7,513** | **56%** | 3,680 (63%) |
| Vibe | 9,790 | 8,726 | 898 | 8% | 8,097 (83%) |
| tvScientific (Pinterest) | 1,806 | 1,490 | 178 | 9% | n/a |
| Tatari | 507 | 401 | 3,766 | 88% | n/a |
| SteelHouse (legacy MNTN tag) | 276 | 206 | 24,848 | 99% | 179 |

Sources: https://trends.builtwith.com/analytics/MNTN ; https://trends.builtwith.com/analytics/Vibe ; https://trends.builtwith.com/analytics/tvScientific ; https://trends.builtwith.com/analytics/Tatari ; https://trends.builtwith.com/analytics/SteelHouse

Wappalyzer, using a different and smaller crawl, sees **300** live MNTN sites ([Wappalyzer](https://www.wappalyzer.com/technologies/advertising/mntn/)) [third-party].

**Reading** [estimate]:
- *Sites per customer.* 5,804 live MNTN sites against 4,225 TTM customers is about **1.4 sites per customer**. That is plausible: brands run several domains, and churned advertisers often leave tags in place.
- *Churn.* The 56% expired share is consistent with **substantial cumulative SMB churn**, including paid-trial churn the 10-K acknowledges ("Churn during paid trial periods is primarily due to limited experience using performance marketing platforms" [reported, 10-K]).
- *Age bias.* The expired share is biased by platform age: Vibe and tvScientific are younger.
- *Vibe's lead.* Vibe has **1.7x** MNTN's live tags, skewed to smaller sites. That fits Vibe's $50/day self-serve model (dossier G).
- *Gaps.* BuiltWith's time series is paywalled, so there is **no trend data**. Detection gaps (tag managers, server-side events) make absolute counts unreliable.

### 3.4 Google Trends (US, weekly, 2024-01-01 to 2026-10-14; pulled via the Trends API) [third-party]

| Quarter (average index) | "MNTN" | "QuickFrame" | "Tatari" | "tvScientific" |
|---|---|---|---|---|
| 2024 Q1–Q4 | 7.0 / 8.9 / 7.8 / 7.5 | 0–0.2 | 3.5–4.2 | 0–0.2 |
| 2025 Q1 | 11.4 | 0 | 4.2 | 0.2 |
| 2025 Q2 (IPO 2025-05-22) | 24.7 (peak week of May 18–24 = **100**) | 0.4 | 4.5 | 0.8 |
| 2025 Q3 | 21.5 | 0 | 6.8 | 8.0 |
| 2025 Q4 | 14.6 | 0 | 5.2 | 7.5 |
| 2026 Q1 | 16.7 | 0.2 | 6.8 | 4.6 |
| 2026 Q2 | 18.2 | 0.8 | 20.1 | 2.0 |
| 2026 Q3 | 14.8 | 0.6 | 20.9 | 0.2 |
| 2026 Q4 to date (2 weeks) | 8.5 | 0.5 | 16.0 | 1.0 |

Quarterly averages of the weekly index are my estimate.

- Branded search interest in "MNTN" peaked in IPO week. It has faded to **about 1–2x the 2024 baseline**, and the latest weeks read 8–9.
- **"QuickFrame" has essentially no search demand** despite 73K+ sign-ups in 1H26. That implies sign-ups come through in-platform, partner (Adobe, Google) or paid channels rather than organic brand demand [estimate].
- "MNTN ads" and "MNTN stock" read near zero (separate pull).
- Reliability: **low**.
  - "MNTN" is contaminated by ticker interest and unrelated "MNTN" brands.
  - "Tatari" is a common Japanese word.
  - "Performance TV" showed an unexplained 2025–26 spike and collapse with no related-query data, so I excluded it.

---

## 4. Customer reviews and marketplace listings

### 4.1 Shopify App Store, "MNTN" app ([listing](https://apps.shopify.com/mntn); [reviews](https://apps.shopify.com/mntn/reviews), accessed 2026-10-15) [third-party]

- **Rating:** 5.0 from **9 reviews**, all 5-star. Shopify does not publish install counts.
- **Dates:** 2023-07-25 (Rumpl), then eight between **2024-09-09 and 2024-11-26**. That cluster suggests a solicited review drive.
  - Reviewers: Nex Playground, The Honey Pot, Blueshift Nutrition, KICKS CREW, Primo Golf Apparel, Sachin & Babi, Audien Hearing, Global Healing.
  - **No reviews have been posted since Nov 2024.**
- **Themes:** easy integration ("It literally takes minutes!", KICKS CREW, 2024-09-10); responsive team; conversion-tracking clarity ("the best thing is how they track conversions," Primo Golf, 2024-09-10); attribution model appreciated (Global Healing, 2024-10-02).
- **Listing copy:** "Free to install. Additional charges may apply." "No contracts, commitments, or agencies required." Measures results "through Google Analytics."

### 4.2 HubSpot App Marketplace ([listing](https://ecosystem.hubspot.com/marketplace/listing/mntn), accessed 2026-10-15) [third-party]

- "MNTN - Advertising and Marketing Analytics App for HubSpot": **"100+ installs"** and **0 reviews**.
- Timeline: the integration went GA on 2026-02-13 and added attribution (v2) on 2026-06-15 [reported, [release notes Jan–Jun 2026](https://help.mountain.com/en/articles/13728265-mntn-updates-january-june-2026)].
- **Reading** [estimate]: 100+ installs against 4,225 customers is ≤~2–5% adoption after 8 months. That is early. Note too that B2B is not MNTN's core base.

### 4.3 Trustpilot, mountain.com ([page](https://www.trustpilot.com/review/mountain.com), accessed 2026-10-15) [third-party]

- **2 reviews, both 1-star.** TrustScore is 2.9; the profile is unclaimed with no invitations.
  - **2022-11-20, "Finicky":** "Uploading display ad creative is the most frustrating process."
  - **Posted 2025-03-10 (experience dated 2024-12-05), "Not great ethics":** the company "mark[s] up the media cost"; "Pretty trash company all around."
- quickframe.com has no Trustpilot page (404).

### 4.4 Sites I could not read

G2 (403), Capterra (product ID unknown; search page renders client-side), TrustRadius (403), Glassdoor (403), Indeed (401/403), Comparably (403), RepVue (429) and Reddit (403 on JSON/search) could not be read.

- Vibe's site claims "**Rated 4.8/5 on G2**" [company claim, [vibe.co blog](https://www.vibe.co/blog/whats-new/fastest-growing-ad-channel-northbeam)].
- MNTN's homepage shows **no** G2 or Capterra badge [reported, [mountain.com](https://mountain.com/), accessed 2026-10-15]. That absence is a weak signal at most.
- **I cannot report review themes, sentiment shifts or head-to-head comparisons against Tatari, Vibe, Roku, Amazon or YouTube from G2 or Reddit.**

### 4.5 Ground-level commercial terms (company pages) [reported]

- **Homepage** (accessed 2026-10-15):
  - "No upfront commitments. No minimums." / "Cancel Anytime."
  - "AI creates an on-brand TV ad from your website at no additional cost."
  - Lead-qualification prompt: "Is your team managing $100,000+ in annual marketing spend?"
  - Calculator: **$5K/month → "893K" impressions, "580K" households**.
- **Implied CPM** ≈ $5,000 / 893K × 1,000 = **$5.60** [estimate].
  - Premium CTV usually prices well above that; Vibe's simulator shows $15–35 CPMs (dossier G).
  - The calculator likely blends in cheaper "Multi-Touch" (non-TV) impressions, or it is promotional.
  - This echoes Paparo's 2025 suspicion that the bidding algorithm "probably heavily weights to remnant and less desirable inventory" (§5.2). **Unverified; flagged, not load-bearing.**
- **Pricing transparency:** "we retain a portion of your overall media spend as a margin … As a performance platform, we don't disclose our margin" [reported, [help center, updated 2026-02-09](https://help.mountain.com/en/articles/8054978-understand-mntn-s-pricing-model)]. Opaque take rates are the root of the Trustpilot "markup" complaint and of Paparo's take-rate skepticism.

---

## 5. Practitioner commentary on attribution and performance claims

### 5.1 What "Verified Visits" is (primary source) [reported]

Source: [help center, "Understand MNTN Attribution," updated 2026-04-03](https://help.mountain.com/en/articles/12608309-understand-mntn-attribution).

- A Verified Visit is a site visit after a **full-completion TV ad view**, within a **default window of 7 days for retargeting and 14 days for prospecting**. The window is customizable.
- Visits are matched at the **household** level, from any device, through MNTN's identity graph covering "132 million households."
- Clicks on MNTN "Multi-Touch" (non-TV) ads also count.
- Optional "Last Touch Verified Visits" metrics de-duplicate against other channels using UTMs.
- MNTN's tech page (Aug 2026) adds two points ([mountain.com/tech](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/)):
  - credit is withheld when another paid channel had the last touch (an example "about 25%" branded-search case);
  - "Deduplication governs what the optimizer learns from, not what the advertiser gets to see."
- **"Comprehensive Reporting"** (released 2025-11-19) now "combin[es] verified results with **modeled outcomes** for impressions, visits, conversions, and order value" [reported, [release notes H2'25](https://help.mountain.com/en/articles/12590590-mntn-updates-july-december-2025)]. This helps comparability with Meta and Google, but it raises the share of modeled, not observed, conversions in in-platform reports [estimate].

### 5.2 Skeptics [third-party]

- **Ari Paparo, Marketecture, "Moving MNTNs," 2025-03-03** ([link](https://news.marketecture.tv/p/moving-mntns)). He discloses: "I am on the board of directors of Vibe.co, a competitor to MNTN."
  - He describes Verified Visits as IP-based, view-through attribution with cross-device matching: "The obvious weakness of this approach … correlation ≠ causation."
  - On supply cost declines: "What is left unsaid here, is that the algo probably heavily weights to remnant and less desirable inventory."
  - He estimated the take rate at "maybe 50% or more," implying ~$400–450M of gross spend at the time.
  - He noted the S-1 gave no sense of the political-ad boost in 2024: "my guess is a LOT."
- **Paparo, Marketecture, 2026-06-29** ([link](https://news.marketecture.tv/p/takeaways-from-walmart-s-vibe-co-deal)).
  - On MNTN's reported "81% take rate (!!)": "I read this three times, and I'm still not convinced this is correct."
  - Yet he listed MNTN as a Walmart–Vibe "winner": "Direct comp for Vibe with half the market cap."
- **Trade press (AdExchanger, Victoria McNally).** Coverage on [2025-11-05](https://www.adexchanger.com/tv/mntns-smb-ctv-ad-business-is-growing-like-gangbusters/), [2026-05-07](https://www.adexchanger.com/tv/mntn-wants-its-ai-video-ad-generator-to-stand-apart-from-its-ctv-platform/) and [2026-08-07](https://www.adexchanger.com/ctv-roundup/why-mntns-ceo-isnt-sweating-media-consolidation/) contains **no practitioner criticism of Verified Visits**. The tone is mildly skeptical only on growth sustainability ("Debates about the feasibility of infinite growth aside…").
  - The CEO himself invokes an "unquantified halo effect from television" (2026-08-07).
- **Digiday (2026-05-28)** covers SMB CTV economics: Universal Ads' pizzeria test showed +3.2% average incremental sales lift, measured by the vendors themselves; agencies point SMBs to cheaper FAST channels. **MNTN is not mentioned** ([link](https://digiday.com/media-buying/universal-ads-must-pass-the-pizza-test-if-its-to-steal-ad-dollars-from-social/)).
- **Attribution-window sensitivity** (vendor evidence, from a competitor). Vibe's Shinesty case says "70% of purchases were missed on a 1-day window" [third-party, [vibe.co blog list, Aug 2026](https://www.vibe.co/blog/whats-new/fastest-growing-ad-channel-northbeam)]. Credited outcomes for CTV clearly depend heavily on window choice, which is the crux of the view-through debate [estimate].
- **Not found** (search budget exhausted): podcasts, LinkedIn posts or agency-practitioner threads on Verified Visits. **Gap.**

### 5.3 MNTN's response: third-party verification and holdouts [reported]

- **Incrementality.** A **10% holdout** is applied on Prospecting campaigns with an active conversion pixel. Results are scaled monthly ([help center, updated 2026-03-25](https://help.mountain.com/en/articles/11096577-understand-mntn-incrementality)). The tech page says "ghost-bidding" holdouts and A/B testing are in beta.
- **Measurement integrations launched in about 9 months:**

  | Date | Partner | What it does |
  |---|---|---|
  | 2025-10-21 | Haus | Incrementality |
  | 2025-11-20 | Northbeam | Multi-touch attribution (MTA) and media-mix modeling (MMM) |
  | 2025-12-16 | Freshpaint | HIPAA-compliant attribution |
  | 2026-02-13 / 2026-06-15 | HubSpot | Integration, then attribution |
  | 2026-06-30 | AppsFlyer v2 | App attribution |
  | 2026-07-08 | Upwave | Brand lift |
  | 2026-07-16 | WorkMagic | Geo-lift |
  | 2026-07-20 | Prescient AI | MMM |

  Sources: [release notes H2'25](https://help.mountain.com/en/articles/12590590-mntn-updates-july-december-2025), [H1'26](https://help.mountain.com/en/articles/13728265-mntn-updates-january-june-2026), [H2'26](https://help.mountain.com/en/articles/16046159-mntn-updates-july-december-2026).
- **Partner claims MNTN publishes** [third-party, as published by MNTN, unaudited; [tech page](https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/)]:
  - Rockerbox: "70% of MNTN advertisers see CPAs 18–33% below their top-spending acquisition channels."
  - Northbeam: "90% of MNTN-driven site traffic is net new."
- **Independent spend tracking cuts the other way.** Northbeam's H1'26 vs H1'25 tracked-spend growth among "emerging platforms": **Vibe +1,900%** [third-party, [Vibe blog, 2026-07-14](https://www.vibe.co/blog/whats-new/fastest-growing-ad-channel-northbeam)]. MNTN was **+29%**, per a Northbeam X post seen only via a search snippet in dossier G (low-to-medium confidence).

**Reading** [estimate]: opening MNTN to independent tools is the right defense against skepticism about view-through attribution. It also **commoditizes measurement**. Once Northbeam, Haus or Prescient grade MNTN and Vibe on the same scale, MNTN's proprietary attribution stops being a moat, and the contest moves to price, supply and AI optimization.

---

## 6. Employee sentiment

**Blind** ([reviews](https://www.teamblind.com/company/MNTN/reviews), accessed 2026-10-15) [third-party]:
- **4.2/5 from 13 reviews**, dated 2024-01-09 to 2026-04-29.
- Sub-scores: Career Growth 3.5, Work-Life Balance 4.5, Compensation/Benefits 3.9, Culture 4.6, Management 3.8.

| Date | Role | Rating | Key quote / theme |
|---|---|---|---|
| 2026-04-29 | Software Engineer I (current) | 5 | Pros: remote, "MNTN meets." Cons: "Low salaries and no stocks. No year bonus. No options to grow" |
| 2025-12-17 | Software Engineer (current) | 4 | "Upper management shifts priorities very frequently" |
| 2025-12-08 | Program Manager (current) | 3 | "Massive favoritism from leadership … Strategy is set by CEO and shifts every day" |
| 2025-06-29 | Full Stack Engineer (former) | 4 | "Great product but bad inventory"; "Jumped on the 'mention Ai for investor bait' bandwagon" |
| 2025-05-06 | Senior Engineer (current) | 5 | "Fully remote … Often minimal roadmap and it can change frequently" |
| 2025-03-22 | Account Executive (current) | 4 | Strong culture; executive decisions "don't feel transparent" |
| 2024-10-24 | Engineering Manager (current) | 3 | "Leadership likes to plan based on their intuition"; EMs absorbing PM work |
| 2024-01-09 | Software Engineer (current) | 4 | "People get fired unexpectedly pretty often" |

**Themes** [estimate]:
- *Positive:* work-life balance, remote work and offsites.
- *Recurring cons:* founder/CEO-centric, frequently shifting priorities; thin career paths.
- *AI:* one former engineer's "AI for investor bait" remark (June 2025) is the only AI-related employee comment found. It predates QuickFrame AI.
- *RIF:* no review mentions the April 2026 RIF or sales pressure.
- *Sample size:* tiny.

**Other employer signals:**
- Glassdoor, Indeed and RepVue were not accessible. RepVue's sales-org data would be the best quota-attainment signal. **Gap.**
- LinkedIn ([company page](https://www.linkedin.com/company/wearemntn/), accessed 2026-10-15) shows **134,880 followers** and **"924 employees"** [third-party]. That is about 2x the 451 FTEs reported, and likely includes contractors, QuickFrame creators and stale profiles.
- Built In shows "405 Total Employees" and "100% remote … Typical time on-site: None" ([Built In](https://builtin.com/company/mntn)) [third-party]. Its Associate AE listing says "In-Office or Remote," which conflicts with the on-site wording in the Greenhouse posting.
- The careers page also says "100% remote—work from anywhere you like" and cites Ad Age Best Places to Work 2024/2025 [reported, [mountain.com/careers](https://mountain.com/careers/)].

---

## 7. Product velocity as a ground-level signal [reported]

| Window | Logged releases | Measurement / reporting / integration share [estimate, my classification] | AI-flavored items |
|---|---|---|---|
| H2'25 | 15 | 11/15 | Comprehensive Reporting (modeled outcomes) |
| H1'26 | 17 | 7/17 | Goal Advisor; MNTN Matched narrowing |
| Jul-26 | 7 | 5/7 | **Media Plan GA** (AI network mix with "overnight" automation) |
| Aug 1 – Oct 15, 2026 | **0 logged** | — | Help articles exist for an **AI Widget Builder** (plain-language report building, updated 2026-08-24) and **political advertising** (updated 2026-09-30) |

Sources: help-center release notes (links in §5.3); [AI Widget Builder](https://help.mountain.com/en/articles/16600851-build-custom-reports-with-ai); [political advertising](https://help.mountain.com/en/articles/17177735-run-political-advertising-on-mntn).

**Reading** [estimate]:
- The cadence was healthy (~2.5–3 logged releases a month) through July 2026.
- The empty Aug–Oct 2026 log is more likely a documentation lag than a stoppage, since dated help articles exist. Still, re-check it.
- About 59% (23/39) of releases concern measurement, reporting or integrations. Product effort is going mainly into **proving** performance.
- The political-ad acceptance flow matters for the 2026 midterms (Q3/Q4 2026). Paparo suspected political ads boosted 2024 "a LOT" (§5.2).

---

## 8. Thesis implications: AI victim or AI winner?

**Points toward "AI winner" (cost structure):**
- Headcount fell 4.4% y/y while revenue rose 21% and customers 40% [reported].
- Revenue per FTE rose about **+34% y/y** on an ex-Maximum Effort TTM basis [estimate: $313.3M/451 = $695K vs $245.2M/472 = $519K].
- COR headcount fell 38% y/y [reported].
- Support is being redesigned around "AI deflection," and GTM around "agentic workflows" [reported].
- No net engineering hiring is visible, while the CEO claims AI-native engineering productivity [third-party transcript].
- **Model implication:** headcount growth of 0–5% a year with revenue growing about 20% supports structural opex leverage outside S&M.

**Points toward "AI victim" or share loss (demand side):**
- Every external footprint proxy (Tranco, Similarweb, BuiltWith, Northbeam) shows **Vibe.co, now Walmart-owned, AI-native self-serve with an MCP interface, at $50/day**, growing much faster than MNTN, and MNTN's footprint flat to down in 2026.
- MNTN's GTM has gone through hire → cut → re-hire inside 12 months.
- The new hiring targets agencies and unfamiliar "emerging verticals." That reads as a search for growth beyond a core DTC/SMB pool that AI-native and walled-garden competitors (dossiers E, F, G) are contesting.
- **Model implication:** S&M is unlikely to fall much below about 33–35% of revenue near-term. Growth deceleration risk is real.

**Attribution:**
- Skepticism is a persistent overhang (view-through, household-level matching, 7/14-day windows, opaque margin, modeled outcomes).
- MNTN's opening to third-party measurement reduces the tail risk of a credibility event. It also turns measurement into a level playing field, removing a differentiator.

**Net for this topic:** **≈ −0.5 on a −3 (victim) to +3 (winner) scale, low confidence.** Most of the alternative data is noisy. The only high-reliability items (SEC headcount and RIF data) are mildly positive on AI-driven efficiency. The lower-reliability external proxies are consistently negative on competitive momentum.

**What to watch in the Q3'26 print (early Nov 2026) and its 10-Q:**
1. Headcount at 2026-09-30, given the 21 open roles.
2. QuickFrame AI sign-ups for Q3 against Q2's ~37K.
3. Agency-sourced revenue share and partnership commissions.
4. Any political-ad contribution.
5. Whether the "workplace model" change (Austin on-site sales) is formalized.

---

## 9. Data gaps and reliability flags

- **Not accessible (HTTP 403/401/429) or blocked:** G2, Capterra, TrustRadius, Glassdoor, Indeed, Comparably, RepVue, Reddit, layoffs.fyi (Airtable embed), the Texas WARN page and the Wayback Machine (connection reset). As a result:
  - there is **no historical job-posting snapshot**;
  - there are **no review-site sentiment trends**;
  - there are **no Reddit practitioner threads**.
- **Web-search budget exhausted** before this topic started. Podcasts, LinkedIn posts and other trade-press items on Verified Visits skepticism were not searched.
- **Similarweb:** free-tier snapshot only (no monthly history); unreliable for low-traffic B2B sites.
- **Tranco:** a blended DNS/browser rank, not traffic, and not linear. It reflects the pixel and ad-serving footprint and has diverged from reported revenue.
- **BuiltWith/Wappalyzer:** crawler detection; no time series without a paid plan; the two sources disagree sharply (5,804 vs 300 live sites).
- **Google Trends:** ambiguous terms; low volumes for B2B ad-tech.
- **Mid-2026 functional headcount split** (S&M/CS, engineering) is not disclosed; my 150–170 S&M/CS figure is an estimate.
- **Northbeam "MNTN +29%"** figure comes only from a search snippet (dossier G).
- **Shopify install counts** are not published. HubSpot shows only the "100+" bucket.
- **Offshore or contractor labor** beyond the disclosed marketing-services contractor: not measurable.
- **The homepage calculator's implied $5.60 CPM** is unexplained.

---

## Sources

1. MNTN, Form 10-Q for Q2 2026, SEC, 2026-08-10. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm
2. MNTN, Form 10-Q for Q1 2026, SEC, 2026-05-11. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000040/mntn-20260331.htm
3. MNTN, Form 10-K for FY2025, SEC, 2026-02-19. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm
4. MNTN, Form 10-Q for Q3 2025, SEC, 2025-11-10. https://www.sec.gov/Archives/edgar/data/1891027/000189102725000022/mntn-20250930.htm
5. MNTN, Form 10-Q for Q2 2025, SEC, 2025-08-11. https://www.sec.gov/Archives/edgar/data/1891027/000189102725000012/mntn-20250630.htm
6. MNTN, 424B4 prospectus, SEC, 2025-05-22. https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm
7. MNTN, DRS/A (accession 0001104659-24-060066), SEC, 2024. https://www.sec.gov/Archives/edgar/data/1891027/000110465924060066/filename1.htm
8. MNTN, Form 8-K (director election), SEC, 2026-09-08. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000089/mntn-20260903.htm
9. SEC EDGAR, MNTN filing index (accessed 2026-10-15). https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001891027&type=&dateb=&owner=include&count=100
10. MNTN Q2 2026 earnings call transcript, The Motley Fool, 2026-08-11. https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/
11. MNTN Q1 2026 earnings call transcript, The Motley Fool, 2026-05-06. https://www.fool.com/earnings/call-transcripts/2026/05/06/mntn-mntn-q1-2026-earnings-transcript/
12. MNTN Q4 2025 earnings call transcript, The Motley Fool, 2026-02-10. https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/
13. MNTN Greenhouse job board API (21 postings), accessed 2026-10-15. https://boards-api.greenhouse.io/v1/boards/mntn/jobs (human view: https://job-boards.greenhouse.io/mntn)
14. MNTN Careers page, accessed 2026-10-15. https://mountain.com/careers/
15. MNTN homepage, accessed 2026-10-15. https://mountain.com/
16. MNTN press page, accessed 2026-10-15. https://mountain.com/press/
17. MNTN, "The technology that puts performance in Performance TV," Aug 2026. https://mountain.com/tech/the-technology-that-puts-performance-in-performance-tv/
18. MNTN Help Center, "Understand MNTN Attribution," updated 2026-04-03. https://help.mountain.com/en/articles/12608309-understand-mntn-attribution
19. MNTN Help Center, "Understand MNTN Incrementality," updated 2026-03-25. https://help.mountain.com/en/articles/11096577-understand-mntn-incrementality
20. MNTN Help Center, "Understand MNTN's Pricing Model," updated 2026-02-09. https://help.mountain.com/en/articles/8054978-understand-mntn-s-pricing-model
21. MNTN Help Center, "MNTN Updates: July–December 2025." https://help.mountain.com/en/articles/12590590-mntn-updates-july-december-2025
22. MNTN Help Center, "MNTN Updates: January–June 2026." https://help.mountain.com/en/articles/13728265-mntn-updates-january-june-2026
23. MNTN Help Center, "MNTN Updates: July–December 2026" (accessed 2026-10-15). https://help.mountain.com/en/articles/16046159-mntn-updates-july-december-2026
24. MNTN Help Center, "Build Custom Reports with AI," updated 2026-08-24. https://help.mountain.com/en/articles/16600851-build-custom-reports-with-ai
25. MNTN Help Center, "Run Political Advertising on MNTN," updated 2026-09-30. https://help.mountain.com/en/articles/17177735-run-political-advertising-on-mntn
26. MNTN Help Center, "Install Image Pixels" (px.mountain.com). https://help.mountain.com/en/articles/7251381-install-image-pixels
27. Similarweb, mountain.com / vibe.co / quickframe.com / tatari.tv overviews (Sep-2026 snapshot), accessed 2026-10-15. https://www.similarweb.com/website/mountain.com/ (and /vibe.co/, /quickframe.com/, /tatari.tv/)
28. Tranco list API and daily list downloads (2024-07-15 to 2026-10-14), accessed 2026-10-15. https://tranco-list.eu/api/ranks/domain/mountain.com ; https://tranco-list.eu/api/lists/date/2025-10-15
29. BuiltWith, MNTN / Vibe / tvScientific / Tatari / SteelHouse usage statistics, accessed 2026-10-15. https://trends.builtwith.com/analytics/MNTN (and /Vibe, /tvScientific, /Tatari, /SteelHouse)
30. Wappalyzer, "Websites using MNTN," accessed 2026-10-15. https://www.wappalyzer.com/technologies/advertising/mntn/
31. Google Trends (US, weekly, 2024-01-01 to 2026-10-14) via trends.google.com API, accessed 2026-10-15. https://trends.google.com/trends/
32. Shopify App Store, MNTN app and reviews, accessed 2026-10-15. https://apps.shopify.com/mntn/reviews
33. HubSpot App Marketplace, MNTN listing, accessed 2026-10-15. https://ecosystem.hubspot.com/marketplace/listing/mntn
34. Trustpilot, mountain.com reviews, accessed 2026-10-15. https://www.trustpilot.com/review/mountain.com
35. Blind, MNTN company reviews, accessed 2026-10-15. https://www.teamblind.com/company/MNTN/reviews
36. LinkedIn, MNTN company page, accessed 2026-10-15. https://www.linkedin.com/company/wearemntn/
37. Built In, MNTN company profile, accessed 2026-10-15. https://builtin.com/company/mntn
38. California EDD, WARN report (2026-07-01 to 2026-10-14), accessed 2026-10-15. https://edd.ca.gov/siteassets/files/jobs_and_training/warn/warn_report1.xlsx
39. Ari Paparo, "Moving MNTNs," Marketecture, 2025-03-03. https://news.marketecture.tv/p/moving-mntns
40. Ari Paparo, "Takeaways from Walmart's Vibe.co deal," Marketecture, 2026-06-29. https://news.marketecture.tv/p/takeaways-from-walmart-s-vibe-co-deal
41. Victoria McNally, "MNTN's SMB CTV Ad Business Is Growing Like Gangbusters," AdExchanger, 2025-11-05. https://www.adexchanger.com/tv/mntns-smb-ctv-ad-business-is-growing-like-gangbusters/
42. Victoria McNally, "MNTN Wants Its AI Video Ad Generator To Stand Apart From Its CTV Platform," AdExchanger, 2026-05-07. https://www.adexchanger.com/tv/mntn-wants-its-ai-video-ad-generator-to-stand-apart-from-its-ctv-platform/
43. Victoria McNally, "Why MNTN's CEO Isn't Sweating Media Consolidation," AdExchanger, 2026-08-07. https://www.adexchanger.com/ctv-roundup/why-mntns-ceo-isnt-sweating-media-consolidation/
44. Sam Bradley, "Universal Ads must pass the pizza test…," Digiday, 2026-05-28. https://digiday.com/media-buying/universal-ads-must-pass-the-pizza-test-if-its-to-steal-ad-dollars-from-social/
45. Vibe.co, "Vibe Named the Fastest-Growing Ad Channel on Northbeam," 2026-07-14. https://www.vibe.co/blog/whats-new/fastest-growing-ad-channel-northbeam
46. Internal cross-references: dossiers A (filings), B (calls), C (customers), G (competitors) and I (creative AI) in this research folder. These supply the Northbeam X-post figure, the Vibe/Walmart deal terms and the QuickFrame sign-up counts.

---

## Verification (adversarial check)

*Checked 2026-10-15 against primary sources. SEC documents were re-downloaded straight from EDGAR, the Greenhouse API was re-pulled, Tranco daily lists were re-downloaded, BuiltWith and Similarweb were re-fetched, Google Trends was re-pulled, and the MNTN homepage HTML and JavaScript were inspected. The web-search budget was exhausted, so every check used direct fetches.*

**Summary.** 13 of 14 findings are confirmed. One is **corrected materially**: the homepage-calculator CPM. Two findings need updating:

- The Northbeam MNTN +29% figure is now confirmed from a primary chart.
- The Q3'26 report date is now fixed at Nov 4, 2026.

| # | Finding | Verdict | Correct value / note | Evidence |
|---|---|---|---|---|
| 1 | FT headcount: 451 (Jun-26), 472 (Jun-25), 542 (Mar-26), 534 (Dec-25). Revenue +21% y/y; TTM customers +40% | **Confirmed** | The 10-Qs and 10-K give 451, 472, 542 and 534 verbatim. Q2'26 revenue was +20.6% ($82.5M vs $68.5M). The Q2'26 release: "Active Performance TV customers grew 40% year-over-year in the trailing twelve months" (4,225 vs 3,020). The arithmetic of −4.4% y/y and −16.8% q/q is correct. | [Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm); [Q2'25 10-Q](https://www.sec.gov/Archives/edgar/data/1891027/000189102725000012/mntn-20250630.htm); [Q2'26 release](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000070/mntnearningsrelease2026-q2.htm) |
| 2 | RIF approved 2026-04-28, ~76 employees; charge $1.491M (S&M 1,141 / COR 261 / T&D 64 / G&A 25 $K); completed by 2026-06-30 | **Confirmed** | Q1'26 10-Q Note 13: "reduction of the Company's workforce by approximately 76 employees, which has been substantially completed"; estimated charge ~$1.7M. Q2'26 10-Q Note 14 gives the line split exactly as stated and says the plan "was completed by June 30, 2026." The 14% share and the ~15 extra departures are correctly labeled [estimate]. | [Q1'26 10-Q](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000040/mntn-20260331.htm); [Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm) |
| 3 | COR headcount −38% y/y (Q2'26); T&D +13% (Q2) vs +23% (Q1); S&M average −7% (Q1); G&A +10% | **Confirmed** | All four are verbatim in the three-month MD&A. **Nuance:** the six-month MD&A gives S&M average headcount **−2%** for H1'26. If Q1 was −7%, Q2'26 average S&M headcount was roughly flat to +3% y/y [estimate], despite the April RIF. Also, T&D headcount was still **+13%** y/y, so "engineering frozen" (§2.3) describes open roles, not headcount. | [Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm); [Q1'26 10-Q](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000040/mntn-20260331.htm) |
| 4 | Ex-ME TTM revenue per FTE $695K vs $519K (+34%); FY23 $369K, FY25 $543K; customers per FTE 9.4 vs 6.4 | **Confirmed (arithmetic; label [estimate] is correct)** | Ex-ME quarters from the Q4'25 release are 53.4 + 64.2 + 59.1 + 68.5 = $245.2M. TTM Q2'26 = 70.0 + 87.1 + 73.7 + 82.5 = $313.3M. **Method caveat:** the denominator is the *post-RIF period-end* headcount (451), which flatters a TTM ratio. On a five-point average headcount (472/498/534/542/451 ≈ 499), TTM Q2'26 revenue per FTE is about **$627K**, not $695K [estimate]. Read the +34% as an upper bound. | [Q4'25 release (ex-ME table)](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000004/mntnearningsrelease2025-q4.htm); [Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm) |
| 5 | Greenhouse: 21 open; 17 first published Sep 1–Oct 13; 13 Revenue (5 agency, 4 Sales Executives plus a Head of Industry, 3 Austin inside sales); 6 Engineering; 1 Technology; 1 Marketing; 0 core software/ML | **Confirmed** | API `meta.total` = 21. Departments are Revenue 13, Engineering 6, Technology 1, Marketing 1. 17 postings have `first_published` between 2026-09-01 and 2026-10-13; the oldest is 2026-07-10. All 3 inside-sales roles say they work from the Austin office. None of the 6 Engineering-department roles is core software, ML or data science. **Label:** the "≈4.7% of headcount" is an [estimate] (21/451), not reported. **Corroboration:** MNTN appointed Frank Lee as SVP of Agency Partnerships on 2026-08-19 (IR press release). | [Greenhouse API](https://boards-api.greenhouse.io/v1/boards/mntn/jobs?content=true); [IR news feed](https://ir.mountain.com/news/default.aspx) |
| 6 | Tranco: mountain.com Q3'26 average 3,169 vs Q3'25 2,740; best 2,414 (Aug-25); vibe.co 20,433 → 12,194; gap 11.7x → 3.7x | **Confirmed** | Re-downloaded lists: 2024-10-15 (3,044 / 35,529), 2025-07-15 (2,865 / 21,245), 2025-08-15 (2,414 / 19,414), 2025-09-15 (2,940 / 20,640), 2025-10-15 (2,706 / 20,467), 2026-07-15 (3,161 / 12,949), 2026-08-15 (3,217 / 11,865), 2026-09-15 (3,128 / 11,767), 2026-10-14 (3,115 / 11,545). The averages and ratios recompute exactly. **Nuances:** (a) "Q3 average" means the mean of three mid-month 30-day lists, not daily data. (b) Tranco's providers are CrUX, Farsight, Majestic (backlinks), Cloudflare Radar and Umbrella, so it is not purely DNS and browser. (c) `filterPLD: on` folds subdomains such as px.mountain.com into mountain.com, which supports the pixel-footprint reading. | [Tranco rank API](https://tranco-list.eu/api/ranks/domain/mountain.com); [list config 2025-10-15](https://tranco-list.eu/api/lists/date/2025-10-15) |
| 7 | Similarweb (Sep-26): mountain.com 109.2K over the last 3 months, −12.8% m/m, #319,221; vibe.co 179.5K, +16.1%; quickframe.com 59.1K, −32.9%; tatari.tv 20.6K | **Confirmed** | Re-fetched with the same values. The "Total Visits Last 3 Months" label is confirmed on the quickframe.com and tatari.tv pages. The source is still a low-reliability panel estimate. | [Similarweb mountain.com](https://www.similarweb.com/website/mountain.com/); [vibe.co](https://www.similarweb.com/website/vibe.co/) |
| 8 | BuiltWith: MNTN 5,804 live (5,018 US), 7,513 expired (56%); Vibe 9,790 / 898; tvScientific 1,806; Tatari 507; Wappalyzer 300 | **Confirmed** | BuiltWith: "We know of 5,804 live websites using MNTN and an additional 7,513 sites that used MNTN historically and 5,018 websites in the United States." 7,513 / 13,317 = 56.4%. Vibe shows Total Live 9,790 and Expired 898; tvScientific 1,806; Tatari 507 (3,766 expired). Wappalyzer "tracks 300 live websites using MNTN." | [BuiltWith MNTN](https://trends.builtwith.com/analytics/MNTN); [BuiltWith Vibe](https://trends.builtwith.com/analytics/Vibe); [Wappalyzer](https://www.wappalyzer.com/technologies/advertising/mntn/) |
| 9 | Northbeam H1'26 vs H1'25 tracked spend: Vibe +1,900%, MNTN +29% (MNTN figure from a search snippet only) | **Confirmed, upgraded** | The Northbeam-credited chart embedded in Vibe's 2026-07-14 post shows **MNTN +29%**, alongside Vibe +1,900%, PostPilot +502%, Impact +149%, Snapchat +91% and LiveIntent +25%. Its caption reads "2026 YTD · year-over-year spend growth · platforms under $100M tracked spend … Jan–Jun 2026 vs Jan–Jun 2025." The MNTN figure no longer depends on a search snippet. Caveats remain: Vibe, a competitor, chose to publish the chart, and the MNTN–Northbeam integration only went GA on 2025-11-20, which can inflate "tracked" growth. | [Vibe blog](https://www.vibe.co/blog/whats-new/fastest-growing-ad-channel-northbeam); [chart image](https://www.datocms-assets.com/103753/1784217354-northbeam.jpeg) |
| 10 | Google Trends (US) "MNTN": peak 100 in IPO week (May 18–24, 2025); Q3'26 average 14.8; recent weeks 8–9; 2024 baseline ~7–9; "QuickFrame" ~0–1 | **Confirmed** | Re-pulled the weekly series for 2024-01-01 to 2026-10-14. The peak is the week of 2025-05-18 at 100. Q3'26 averages 14.8. The last four weeks read 11, 9, 9 and 8. The 2024 quarters read 7.0, 8.9, 7.8 and 7.5. QuickFrame reads 0–0.8. The 73K+ 1H26 sign-ups figure comes from the CEO on the Q2'26 call and is verified in dossier I. | [Google Trends](https://trends.google.com/trends/explore?geo=US&q=MNTN,QuickFrame&date=2024-01-01%202026-10-14) |
| 11 | Verified Visits: full-completion view; any household device; 7-day retargeting / 14-day prospecting defaults; "132 million households"; optional last-touch dedup; Comprehensive Reporting (Nov 2025) adds modeled outcomes | **Confirmed** | The help center (dated April 3, 2026) has each element verbatim, and the windows are customizable. The UTM/referrer exclusion applies only to "Last Touch Verified Visits" ("Source Validation Criteria"), not to standard Verified Visits. Release notes: Comprehensive Reporting released 11/19/25 "combines verified results with modeled outcomes for impressions, visits, conversions, and order value." | [Help center: attribution](https://help.mountain.com/en/articles/12608309-understand-mntn-attribution); [Release notes H2'25](https://help.mountain.com/en/articles/12590590-mntn-updates-july-december-2025) |
| 12 | Homepage calculator: $5K/month → 893K impressions, 580K households → implied CPM ~$5.60, "far below" the $15–35 premium-CTV range | **CORRECTED (material)** | "No upfront commitments. No minimums." is confirmed. **But 893K and 580K are static placeholder text in the server HTML. The page's own JavaScript overwrites them on load** (theme `build/index.js`: `CPM = 23.5 − 4.8·(1 − e^(−budget/300))`; reach = `85M·(1 − e^(−budget/2400))`). At the default $5K, a browser shows about **213K "Commercial views per month"** and **~177K households**. The implied CPM is **~$23.4** at $5K, falling to ~$22.1 at $100K and ~$18.9 at $1M a month. That sits **inside** the $15–35 premium-CTV range, not far below it. The impressions are labeled "Commercial views," so the Multi-Touch blending hypothesis also lacks support. **Drop the $5.60 CPM and the "remnant inventory" inference drawn from it** (§4.5, §9). | [mountain.com](https://mountain.com/) (HTML and `/wp-content/themes/mountain/build/index.js`) |
| 13 | Q3'26 not reported; last 8-K 2026-09-08 (director election); Q3'25 reported 2025-11-04, so an early-Nov print is likely | **Confirmed, updated** | EDGAR submissions show the last filing as a Form 4 on 2026-10-07. The last 8-K (2026-09-08, Item 5.02) is the election of Michael J. Katz. The Q3'25 8-K (Item 2.02) was dated 2025-11-04. **Update:** on 2026-10-14 MNTN announced by press release (no 8-K) that it **will report Q3 2026 results on November 4, 2026**, with a webcast at 4:30 pm ET. The date is now [reported], not [estimate]. | [EDGAR submissions](https://data.sec.gov/submissions/CIK0001891027.json); [8-K 2026-09-08](https://www.sec.gov/Archives/edgar/data/1891027/000189102726000089/mntn-20260903.htm); [IR press release](https://ir.mountain.com/news/news-details/2026/MNTN-To-Announce-Third-Quarter-2026-Financial-Results-on-November-4-2026/default.aspx) |
| 14 | Job-posting AI language: "self-service resolution, AI deflection" (Content Designer); "agentic workflows and AI-assisted tooling" (GTM Engineer); an "AI Engineering" team; "innovation that empowers, not replaces" in every posting | **Confirmed** | Verbatim in the API content. "AI Engineering" appears in one posting (Sr. Manager, GTM Systems Delivery) as a partner team. The "empowers, not replaces" boilerplate appears in 21 of 21 postings. | [Greenhouse API](https://boards-api.greenhouse.io/v1/boards/mntn/jobs?content=true) |

**Other items found during the check** (not in the original findings list):

- **Product activity, §7.** The help-center log for H2'26 still has no entries after 2026-07-23. However, MNTN issued a press release on **2026-09-09, "MNTN and Klaviyo Integrate Performance TV with CRM."** That supports the "documentation lag, not a stoppage" reading.
- **Press page, §2.2.** MNTN's IR feed shows no RIF press release, which is consistent with the dossier.

**Changes required in the body:**

1. §4.5, §9 and the scorecard: replace "~$5.60 implied CPM" with "~$23 implied CPM ($5K a month → ~213K commercial views and ~177K households, from the live calculator)", and drop the remnant-inventory inference.
2. §0, §5.3 and §9: upgrade the Northbeam MNTN +29% from "search snippet" to "Northbeam chart as published by Vibe."
3. Header and §8: the Q3'26 print is **Nov 4, 2026** [reported].
4. §2.4 and §8: describe +34% revenue per FTE as an upper bound, because it uses the post-RIF period-end headcount. On average headcount it is about $627K.
