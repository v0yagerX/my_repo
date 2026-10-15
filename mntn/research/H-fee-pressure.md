# H. AI Threat 4: fee and take-rate pressure across CTV ad-buying platforms (MNTN)

*Dossier date: 2026-10-15. Labels: [reported] = company filing or release; [guidance] = company outlook; [third-party] = trade press, analysts or industry bodies; [estimate] = my own derivation, with the math shown. Q3 2026 results are **not** out yet. MNTN will report on **Nov 4, 2026** [reported, MNTN IR, 2026-10-14, https://ir.mountain.com/news/news-details/2026/MNTN-To-Announce-Third-Quarter-2026-Financial-Results-on-November-4-2026/default.aspx]. The last filing is the Q2'26 10-Q (filed 2026-08-10). The only 8-K since then (2026-09-08) is an Item 5.02 officer/director matter.*

*Research limitation: the shared web-search budget was used up early in this task. Everything below comes from documents opened directly: SEC EDGAR, MNTN IR and help center, competitor SEC filings, and AdExchanger and Digiday pages reached by browsing tag and listing pages. Some industry CPM series (IAB, eMarketer, Guideline) could not be retrieved and are listed as gaps.*

---

## 1. Bottom line

1. **Fee compression is real in 2026, but it is concentrated in the enterprise and agency DSP layer.** The Trade Desk (TTD) held a take rate of about 19–22% for seven years. In Q2'26 its revenue grew only **+3%** y/y, it cited "volume and other discounts in connection with joint business plans," it guided Q3'26 revenue to **≥$650M versus $739.4M a year earlier (about −12%)**, and it cut about **15%** of its workforce [reported, TTD 10-Q and 8-Ks]. Amazon DSP reportedly charges **0% on Amazon-owned programmatic guaranteed (PG) deals and about 1% on open-web inventory** [third-party]. Google's Buyer Direct reportedly caps ad-tech and data fees at about **10%** [third-party].
2. **No public evidence yet that this has reached MNTN.** Through Q2'26:
   - Gross margin rose from **72% (FY24) to 80% (Q2'26)** [reported].
   - Customer credit and concession allowances were flat at **$2.5M → $2.65M/yr** [reported].
   - AR per $ of net revenue fell from **0.96 to 0.73**. That points to a flat-to-*higher* implied take rate, not a lower one [estimate].
   - Q3'26 guidance implies **~25%** growth, an acceleration from 21% [guidance].
   - Revenue per active customer is falling: **$94K → $74K** TTM, ex-Maximum Effort (ex-ME). Management attributes this to down-market mix, and the same-customer "expansion rate" is **"well north of 115%"** [reported].
3. **MNTN's pricing model is structurally sheltered, but not immune.** MNTN charges a **dynamic CPM (dCPM)** and "keeps a share of your media spend." It does **not** disclose that margin and charges no separate tech or data fees [reported, MNTN Help Center, 2026-02-09]. My triangulated take rate (net revenue ÷ gross billings) is **~40–60%** [estimate], which is two to three times TTD's. SMB buyers judge on ROAS and CPA, not fee %, and top-10 customers are only **17%** of revenue [reported]. The risk comes through three routes:
   - **(a) Walled-garden SMB tools:** Amazon "Full-Funnel Campaigns" and the Ads Agent, Meta's reported CTV audience extension, Roku Ads Manager, and Pinterest/tvScientific. These bundle CTV at near-zero explicit fees.
   - **(b) MNTN's own move into agencies and enterprise:** agency-led accounts grew about 4x, and agencies get cash-back "rewards." Fee transparency is expected in that channel.
   - **(c) AI buying agents** that compare CPA across channels automatically.
4. **Verdict on this topic: a mild AI-victim tilt over the long term (about −1 on a −5 to +5 scale); neutral to slightly positive near term.**
   - **Probability of ≥2 pts take-rate compression:** about 15–25% by end-2027; about 45–55% by 2030 [estimate].
   - **Severe case:** a 5–10 pt cut by 2030 has about 20–25% probability [estimate].
   - **Sensitivity:** each 1 pt of take rate is about **1.7–2.2% of revenue** and about **1.5 pts of adj. EBITDA margin**, because MNTN's costs scale with volume, not net revenue [estimate, §8].
   - **Offset:** CTV CPM deflation (Roku price/impression **−12%**, Netflix CPMs roughly halved) gives MNTN room to keep its spread while still improving customer ROAS.

---

## 2. How MNTN actually monetizes (the mechanics)

| Element | What the record says | Label / source |
|---|---|---|
| Unit of pricing | "MNTN uses a dynamic CPM (dCPM) pricing model." Advertisers pay per thousand impressions served. The price adjusts in real time and prioritizes high-propensity users. | [reported] MNTN Help Center, "Understand MNTN's Pricing Model," 2026-02-09, https://help.mountain.com/en/articles/8054978-understand-mntn-s-pricing-model |
| Fee structure | "MNTN does not charge separate fees for services or technology." It keeps a share of media spend. "As a performance platform, we don't disclose our margin." The margin covers third-party audience targeting, the creative suite, analytics, cross-device attribution, ad serving and viewability. | same |
| Accounting | Revenue = "usage-based fees … based on their level of ad spend … **net of amounts paid to suppliers** for the cost of advertising inventory." MNTN bills customers **gross** and reports revenue **net** (agent). AR is recorded at gross billings. | [reported] FY2025 10-K, 2026-02-19 |
| Customer controls | The customer sets a budget (monthly or flighted, minimum 3-day flight) and a goal. There is "pricing limits" logic in automated buying. No stated minimum budget. | [reported] Help Center "Set Your Campaign Budget"; 10-K |
| Billing | Monthly in arrears. Credit card is the default (charged by the 10th of the following month). Net-30 invoicing for approved customers only. Invoices "reflect total monthly ad spend. Campaign-level charges are not itemized." | [reported] Help Center "Understand Billing and Payment," updated 2026-08-07 |
| Minimums | No minimum is stated publicly. Self-signup only asks whether the team manages "$100,000+ in annual marketing spend" to route users. Paid performance trials of ≤3 months count as customers. | [reported] MNTN blog (≈June 2025); 424B4 |
| Creative | QuickFrame "Creative-as-a-Subscription" credits are earned at spend thresholds or with annual contracts that carry minimum spend. Credits are deferred revenue: **$9.0M** (12/24) → **$5.5M** (12/25) → **$2.7M** (6/26). **$1.7M** of breakage from "expiration of unused creative credits associated with amended contracts" was booked in Q1'26. QuickFrame AI ads are now offered free. | [reported] 10-K; Q1'26 and Q2'26 10-Qs; MNTN signup page |
| Agency incentives | The Verified Performance Partner program gives "Rewards for Media Spend": credits redeemable "for creative services, media, or cash back," which scale with growth. | [reported] MNTN IR, 2025-09-29 |
| Earlier SEC description | The SEC asked in 2022 whether revenue is a "variable fee, a flat fee or both." MNTN revised its disclosure to "a variable fee based on the level of ad spend." | [reported] SEC comment letter 2022-01-13; MNTN response 2022-02-14 and 2022-03-29 |

**Interpretation.** MNTN is not a transparent "platform fee + add-ons" DSP like TTD (platform fee "generally based on a percentage of … total spend," plus value-added services [reported, TTD 10-K]). It is an **opaque, bundled spread**, closer to a managed ad network or a search/social auction from the advertiser's point of view. That matters for fee pressure in two ways:
- **Sheltering.** SMB customers who buy on ROAS or cost-per-visit cannot compare a fee %. MNTN's own partner release with PubMatic even advertises "clear cost structures without hidden markups" [reported, 2025-10-13], while its help center declines to disclose the margin.
- **Exposure.** Once a buyer's tools (agency audits, AI agents, or a rival quoting "0–1% fees") can isolate the media cost, a 40–60% spread is a very visible target.

---

## 3. What is MNTN's take rate? (Undisclosed. My triangulation.)

**Method [estimate]:**
- AR is recorded at gross billings [reported].
- Customers are billed monthly in arrears. Card customers are charged by the 10th; invoice customers are on Net 30 [reported].
- So at a quarter-end, AR ≈ the last month's gross billings for all customers plus the prior month's billings for invoice customers. AR ≈ M × (1 + x), where x is the invoice share (assumed 0–30%).
- Quarterly gross billings ≈ 3M. Take rate = quarterly revenue ÷ 3M.

| Quarter-end | AR [reported] | Qtr revenue [reported] | AR ÷ revenue | Implied take rate [estimate] |
|---|---|---|---|---|
| Q4'23 | $50.2M | ~$52.1M (derived from FY23/Q4'24 growth) | 0.96 | 35–45% |
| Q4'24 | $66.9M | $69.8M | 0.96 | 35–45% |
| Q1'25 | $65.8M | $64.5M | 1.02 | 33–42% |
| Q2'25 | $61.7M | $68.5M | 0.90 | 37–48% |
| Q3'25 | $57.7M | $70.0M | 0.82 | 40–53% |
| Q4'25 | $61.8M | $87.1M | 0.71 | 47–61% |
| Q1'26 | $56.3M | $73.7M | 0.76 | 44–57% |
| Q2'26 | $60.0M | $82.5M | 0.73 | 46–60% |

Example (Q2'26): 82.5 × (1.0 to 1.3) ÷ (3 × 60.0) = 46–60%.

**Cross-checks.**
- **Quo Vadis (Tom Triscari, 2025-05-27).** It derived **~$557M FY24 gross spend and a ~40% take rate** from trade payables, assuming 70 payable days [third-party, https://www.quovadisnews.com/p/119-mntn-ipo-valuation-update]. That is consistent with my 2024 range.
- **TTD's level would not fit the balance sheet.** At a TTD-like 20%, Q2'26 billings would be about $412M a quarter. That implies AR of at least about $137M, against $60M actually reported.

**Trend reading.** AR per $ of revenue fell about 24% (0.96 → 0.73). There are two explanations, and the data cannot separate them:
- **Higher take rate.** The implied take rate rose.
- **Payment-mix shift.** More small card-paying SMBs means a lower invoice share x. That alone could explain the move with a constant ~45% take.

Either way, **the receivables data shows no sign of take-rate compression.**

The same holds for AP & accrued, which fell from 0.91–1.02× quarterly revenue (2024–Q2'25) to **0.60–0.68×** (Q4'25–Q2'26) [reported AP: $63.6M at 12/24, $69.7M at 6/25, $59.5M at 12/25, $44.3M at 3/26, $53.8M at 6/26]. That is inconsistent with media cost rising as a share of net revenue.

---

## 4. Gross-margin trajectory (a *partial* take-rate proxy)

Revenue is already net of media, so GM measures hosting, data, platform-fee and creative costs against MNTN's spread. It is still informative. Those costs scale with **impressions and bid volume**, not net revenue. If MNTN were cutting its spread on unchanged volume, GM would *fall*.

| Period | Revenue | Cost of revenue | GM | Notes |
|---|---|---|---|---|
| FY2021 | $99.3M | $33.3M | 66.5% [reported/derived] | DRS/A 2023-05-12 |
| FY2022 | $134.2M | $61.8M | 54.0% | One-off hosting build-out and creative staffing |
| FY2023 | $176.3M | $52.9M | 70.0% | 424B4 |
| FY2024 | $225.6M | $64.1M | 71.6% (ex-ME 74.6%) | 424B4; Q4'25 release |
| FY2025 | $290.1M | $66.2M | 77.2% (ex-ME 77.9%) | 10-K; Q4'25 release |
| Q1'26 | $73.7M | $13.7M | 81% | Q1'26 release |
| Q2'26 | $82.5M | $16.2M | 80% | Q2'26 release |
| TTM Q2'26 (ex-ME) | $313.3M | — | 80.8% [estimate: GP $253.0M ÷ $313.3M] | Quarterly ex-ME GP from releases |

**Drivers.**
- Management: GM improvement came from the Maximum Effort divestiture, a switch of hosting provider (cutover in October 2025), and "a number of other initiatives." Core PTV contributed more than 300 bps in FY25 [reported, Q4'25 call, 2026-02-10].
- The long-term target stays **75–80%** GM and **35–40%** adj. EBITDA margin [guidance].
- Q2'26 COGS shows **"platform fees" down $0.6M y/y** and data/hosting vendor savings [reported, Q2'26 10-Q]. Fee compression *elsewhere* in the supply chain is lowering MNTN's own costs.

**Caveat.** A sharp drop in hosting cost could mask a modest spread cut. My sensitivity (§8) shows a 3 pt take-rate cut would take only about 1.3 pts off GM. So GM alone cannot rule out a 1–3 pt compression. It does rule out a large one.

---

## 5. Revenue per customer: falling, but explained by mix rather than price

| TTM ending | TTM revenue ex-ME [reported, summed] | TTM active PTV customers [reported] | Revenue per customer [estimate] |
|---|---|---|---|
| FY2023 | ~$157.4M (FY24 $209.3M ÷ 1.33) | 1,426 | ~$110K |
| Q2'24 | ~$177.0M | 1,746 | ~$101K |
| Q4'24 | $209.3M | 2,225 | $94.1K |
| Q2'25 | $245.2M | 3,020 | $81.2K |
| Q4'25 | $284.7M | 3,632 | $78.4K |
| Q1'26 | $299.3M | 3,874 | $77.3K |
| Q2'26 | $313.3M | 4,225 | $74.2K (−8.6% y/y) |

**Quarterly-active basis (cleaner).**
- Q2'26 active PTV customers grew **+24%** and revenue **+20.6%** [reported, 10-Q], so spend per active customer fell about **−3%** [estimate: 1.206 ÷ 1.24 − 1].
- Q1'26: customers +26%. Ex-ME revenue excluding the $1.7M breakage grew about +21.8% [estimate: (73.7 − 1.7) ÷ 59.1 − 1], so spend per customer fell about −3%.
- Every 10-Q since IPO attributes the decline to "a decrease in average spend per customer as we continued to expand our overall SMB footprint, including small businesses" [reported].

**Evidence that this is mix, not price:**
- SMB net revenue retention was **108% (FY24)** and **111% (Q1'25)** [reported, 424B4].
- The "expansion rate, which measures the spend of our current customers as compared to those same customers' spend a year earlier … remains well north of 115%" [reported, Q4'25 call].
- In Q1'25, small businesses were **12%** of PTV revenue and mid-sized businesses **79%** [reported, 424B4].
- The CFO said customer count "is entirely within our control, and is predominantly a function of how firmly we step on the accelerator to move down market" [reported, Q4'25 call].

**Evidence against cutting price or concessions:**
- The allowance for credits, chargebacks and "other customer concessions" (recorded as a revenue reduction) was **$2.65M in 2025 versus $2.50M in 2024**, under 1% of revenue [reported, 10-K].
- No disclosure mentions price cuts, CPM reductions or lower take.

**Evidence that MNTN *has* lowered the effective entry price (not the spread):**
- No published minimum spend.
- Free AI-generated TV ads (QuickFrame AI).
- Paid trials of ≤3 months.
- Agency cash-back rewards.
- Restructured creative-credit contracts.

These are customer-acquisition concessions. The agency rewards are the one item that may act like a rebate on the spread: their accounting and size are **not disclosed**.

---

## 6. The industry fee-pressure evidence (2024–2026)

### 6a. The Trade Desk: from a stable ~20% to visible stress in 2026

| Year | Revenue | Gross spend | Take rate [estimate = revenue ÷ gross spend] |
|---|---|---|---|
| 2018 | $477.3M | $2,350.9M | 20.3% |
| 2019 | $661.1M | $3,128.9M | 21.1% |
| 2020 | $836M | $4,199M | 19.9% |
| 2021 | $1,197M | $6,172M | 19.4% |
| 2022 | $1,578M | $7,741M | 20.4% |
| 2023 | $1,946M | $9,611M | 20.2% |
| 2024 | $2,444.8M | $12,040.9M | 20.3% |
| 2025 | $2,896.3M | $13,394.7M | 21.6% |

Sources: TTD 10-Ks for FY2019, FY2021, FY2023 and FY2025 [reported].

**FY2025.** Revenue +18% on gross spend +11%. The take rate *rose*, driven by "increased pricing associated with value-added services and data" and Kokai [reported, FY25 10-K].

**2026 break:**
- Q2'26 revenue was **$715.1M (+3%)**. Gross spend from **existing clients decreased**, partly offset by "volume and other discounts in connection with joint business plans and other strategic partnerships in an effort to drive future growth" [reported, Q2'26 10-Q, 2026-08-06].
- Q2'26 adj. EBITDA was **$241M (34% margin) versus $271M (39%)**. Q3'26 guidance is revenue **≥$650M** and adj. EBITDA **~$160M** [guidance, Q2'26 release]. That compares with Q3'25 revenue of **$739.4M** [reported]: about **−12% y/y** [estimate].
- The 2026-09-03 restructuring cuts about **15%** of the workforce, with **$39–51M** of charges [reported, 8-K Item 2.05].
- The CFO was terminated on 2026-01-24 [reported, 8-K].

**CEO view (third-party report).** On the Q2 call, Jeff Green said TTD "would consider changing its pricing" if that drove growth, but did not "expect the net take rate to change dramatically." He attacked Amazon's "zero-margin take rate" and Google Buyer Direct's roughly **10%** fee cap as "ad networks of 2006" [third-party, AdExchanger, 2026-08-07].

**Fee-stack criticism (third-party opinion).** Fraction Method (Sarah Caputo) cites:
- a buy-side platform fee "often in the mid-teens" percent of CPM;
- a **4.5%** OpenPath publisher fee (late 2024);
- Predictive Clearing bid-shading fees;
- an effective take rate of about 21%;
- WPP Media and Dentsu exiting OpenPath (per Adweek).

[third-party, AdExchanger op-ed 2026-03-04; podcast 2026-03-05]

### 6b. Amazon DSP (rebranded "DVA" under "Amazon Ads Agent," Sept 2026)

- **Fees:** "No fees on programmatic guaranteed deals for Amazon-owned media" and **"a 1% fee"** on open-web publishers. Amazon was "reportedly aiming to undercut" TTD's roughly 20%. Sources said Omnicom moved "a double-digit percentage" of expected Q3'25 spend from TTD to Amazon; TTD denied this [third-party, AdExchanger, 2025-11-18].
- **"1% programmatic guaranteed fees in some cases"** [third-party, AdExchanger, 2026-03-05].
- Amazon "discounts its DSP fees for advertisers buying third-party CTV inventory." Netflix inventory became buyable on Amazon DSP from Q4'25 in 12 markets [third-party, Digiday, 2025-09-10].
- **SMB-facing AI tools:**
  - Ads Agent users see **8% lower cost-per-impression and 6% lower CPA** [reported, Amazon Q2'26 release, 2026-07-30].
  - Amazon advertising revenue was **$19.8B, +26% y/y** [reported].
  - At unBoxed (2026-09-29), Amazon launched DVA+ (AI default) and **"Full-Funnel Campaigns"** to help "small advertisers or sellers expand into channels such as streaming TV" [third-party, AdExchanger, 2026-09-29].
- **Official fees:** Amazon publishes no DSP fee schedule. "Your current pricing structure is carried forward" into DVA+ [reported, advertising.amazon.com].
- **Auction transparency.** In Aug 2026 the FTC sued Amazon. It alleges sponsored-ads auctions described as second-price charged close to the full bid about 80% of the time, extracting more than $20B since 2019, with about 500,000 SMBs affected. Prime Video and DSP are excluded, and Amazon disputes the claims [third-party, AdExchanger, 2026-09-09]. This raises scrutiny of opaque SMB ad pricing generally, a governance-risk read-across to MNTN's undisclosed dCPM margin.

### 6c. Sell side, other DSPs and supply-path optimization (SPO)

- **Magnite:**
  - "Fee concessions may be more prevalent among CTV publishers where inventory is scarce and concentrated among large sellers."
  - Reserve auctions "generally involve lower fees."
  - "Our take rate … tends to be lower on CTV transactions."
  - [reported, Magnite FY25 10-K]
  - Even so, CTV contribution ex-TAC grew **+36% to $97.1M** in Q2'26 [reported, 2026-08-05]. Volume is outrunning fee pressure on the sell side.
- **PubMatic:** Q2'26 revenue **$78.6M (+11%)**. Its AgenticOS ran Spain's first fully agentic CTV campaign at **18% lower CPM than target** [reported, 2026-08-06]. This is a concrete example of AI agents pushing down the price paid.
- **Viant:** Q2'26 revenue **+34%** but contribution ex-TAC only **+24%** [reported, 2026-08-10]. Contribution ex-TAC as a share of revenue fell from **62.1% to 57.7%** [estimate: 60.2 ÷ 104.3 versus 48.4 ÷ 77.9]. Over 80% of Viant's CTV spend now runs through "Direct Access" (a direct supply path). The margin dip is consistent with SPO and pricing pressure, but mix could also explain it.
- **ANA:** The ANA's study estimated an **$88B** programmatic market with about **$22B (25%)** of waste: $10B made-for-advertising (MFA) plus $12B of "ad tech inefficiencies" [third-party, AdExchanger, 2023-12-07]. The 2024 benchmark cut MFA share from 15% to 4%. CTV was *not* covered by the earlier studies [third-party, AdExchanger, 2024-06-17]. Advertisers are auditing intermediary take, and CTV is the next frontier.
- **Agency direct trading:** "More agencies are working directly with media owner-sellers instead of using a DSP." Nathanson: "a strong incentive … to bypass middlemen" [third-party, AdExchanger, 2026-09-11].
- **Google ad-tech remedies.** Judge Brinkema's remedies ruling, around the first week of Sept 2026, did **not** order an AdX divestiture. It imposed behavioral remedies: publishers can set higher floors for some buyers including Google, more auction-data sharing, and no last look. The full opinion was due the following week [third-party, AdExchanger podcast, 2026-09-11]. Direct impact on MNTN is low, since MNTN buys CTV PMPs via direct network deals. Allowing higher floors marginally strengthens sellers' pricing power.

### 6d. CTV CPM trends: deflation is the dominant 2024–26 trend

| Data point | Value | Label / source |
|---|---|---|
| Prime Video ads by default (US) | Launched about 2024-01-29. Reported CPMs **$26–41**; 115M reach; ~1.5 min/hr observed ad load (Amazon pitched 2–3.5 min/hr) | [third-party] AdExchanger 2024-02-02 |
| Supply glut | "Streaming ad supply now outpaces demand," partly because "Amazon rais[ed] the rate of ads on Prime Video"; streamers launch at "sky-high CPMs" then roll back prices | [third-party] AdExchanger roundup citing Ad Age, 2024-10-04 |
| Netflix CPMs | About **$65** at the 2022 launch, **below $30** by Sept 2025; "stabilizing" by Feb 2026; Netflix ads ~$1.5B (3.3% of revenue) in 2025 | [third-party] Digiday 2025-09-10; 2026-02-24 |
| Roku average price per video impression | **−12%** y/y in Q2'26 on impressions **+40%** (1H26: −13% / +48%), "driven by changes in product and country mix" | [reported] Roku Q2'26 10-Q |
| Disney streaming | Impressions +8%, ad prices −4% (Q2 CY26); CFO cites supply-driven "pricing pressure" | [third-party] Digiday, 2026-08-12 |
| Upfronts | Streaming commitments **+30% to $17.2B** (versus $17.33B broadcast and cable) | [third-party] Digiday citing Variety, 2026-08-12 |

**Read-across.** Under dCPM with an undisclosed spread, falling media CPMs are a **cushion, not a threat**. MNTN can pass deflation through as better ROAS (its stated flywheel: networks "often reduce inventory prices to increase demand, thereby further enhancing ROAS for our customers" [reported, 10-K]) or keep part of it as margin. The CEO framed streaming "price war[s]" as good for performance demand as early as Dec 2022 [reported, MNTN newsroom citing CNBC]. MNTN also does **not buy open-market inventory**; it has direct deals with "effectively every streaming network in America" [third-party interview, AdExchanger, 2026-08-07].

---

## 7. How fee pressure could reach MNTN: channels, current evidence, timing

| Channel | Mechanism | Evidence today | Timing / probability [estimate] |
|---|---|---|---|
| 1. Walled-garden SMB CTV bundles | Amazon Full-Funnel / DVA+ and Ads Agent; Meta CTV "audience extension" via Magnite, FreeWheel and OEMs (reported, not launched); Roku Ads Manager; Pinterest-owned tvScientific; Vibe; Universal Ads; streamr.ai. These offer CTV inside tools SMBs already use, at 0–1% explicit fees or none. | Amazon launched Sept 2026 [third-party]. Meta is exploratory [third-party, Digiday 2026-04-27]. No MNTN churn data. | Main long-run vector. Material from 2027–28 if Meta productizes. |
| 2. MNTN's agency and enterprise push | Agencies audit fees and want rebates. Agency-led accounts grew about 4x in 2025; rewards include "cash back." Snap's Frank Lee was hired as SVP Agency Partnerships (2026-08-19). | [reported] Agency revenue share and rebate cost are undisclosed. | Gradual dilution of effective take, 2026–2030. Likely small, about 0.5–2 pts. |
| 3. AI buying agents and CPA comparison | Amazon Ads Agent (−8% CPM, −6% CPA claimed); PubMatic AgenticOS (−18% CPM vs target); TTD Kokai "Zuma." Agents optimize to outcome per $ across channels, which exposes a fat spread unless ROAS keeps up. | [reported/third-party] Nothing MNTN-specific yet. | 2027–2030. Probability rises with agent adoption. |
| 4. Supply-side consolidation | Fewer, bigger sellers (Paramount/WBD; Fox–Roku $22B reported [third-party headline, AdExchanger June 2026]) and higher-floor rights → firmer media cost. If SMB CPA ceilings are fixed, MNTN's spread is squeezed. | CPMs are currently *deflating* (§6d). | Low before 2028. Would show up as GM and take pressure. |
| 5. Transparency and regulation | FTC v. Amazon over SMB auction opacity; ANA scrutiny; MRC auction standards. MNTN invoices do not itemize campaign charges and the margin is undisclosed. | [third-party] No action against MNTN. | Tail risk; would force disclosure, which could then drive renegotiation. |

**What protects MNTN:**
- SMBs that are **95%+ new to TV** compare MNTN with search and social CPA, not with TTD fee %.
- Low concentration: no customer above 10%, and the top 10 are 17% [reported].
- A bundled service (targeting, attribution, AI creative) that a raw 1%-fee DSP does not provide.
- Direct network deals at "preferred pricing."
- CPM deflation.
- MNTN's own costs fall as supply-chain fees compress.

---

## 8. Quantifying the impact (static sensitivity) [estimate]

**Base:** FY26 guidance midpoint revenue **$352M** and adj. EBITDA **$98.5M** (28.0%) [guidance]. Cost of revenue is assumed at about 20% of revenue (~$70M) and volume-driven. Gross billings B = revenue ÷ T. A ΔT-point take-rate cut on unchanged billings removes B × ΔT of revenue, and the same dollars of EBITDA (no opex flex, no volume response).

| Take rate T (billings) | −1 pt | −3 pts | −5 pts | −10 pts |
|---|---|---|---|---|
| 45% ($782M) | Rev −$8M (−2.2%); EBITDA margin 26.3%; GM 79.5% | −$23M (−6.7%); 22.8%; 78.6% | −$39M (−11.1%); 19.0%; 77.5% | −$78M (−22.2%); 7.4%; 74.3% |
| 50% ($704M) | −$7M (−2.0%); 26.5%; 79.6% | −$21M (−6.0%); 23.4%; 78.7% | −$35M (−10.0%); 20.0%; 77.8% | −$70M (−20.0%); 10.0%; 75.0% |
| 60% ($587M) | −$6M (−1.7%); 26.8%; 79.7% | −$18M (−5.0%); 24.2%; 78.9% | −$29M (−8.3%); 21.4%; 78.2% | −$59M (−16.7%); 13.6%; 76.0% |

**2030 scenarios versus a no-compression path [estimate]:**
- **Bull, ~30%:** take flat or higher. MNTN keeps part of the CPM deflation, AI creative lowers cost-to-serve, and SMB buyers stay ROAS-driven. Revenue haircut 0%, or slightly positive.
- **Base, ~45–50%:** take falls 1–3 pts by 2030, via agency rebates, enterprise deals and selective matching against Amazon and Roku in competitive accounts. Revenue −2% to −6%; adj. EBITDA margin −1.5 to −4.5 pts before opex flex. Starts to show in 2027–28.
- **Bear, ~20–25%:** take falls 5–10 pts. Amazon Full-Funnel and a Meta CTV product make performance CTV a near-zero-fee feature inside SMBs' existing ad accounts, and AI agents expose MNTN's CPA versus alternatives. Revenue −10% to −20%; adj. EBITDA margin −8 to −18 pts before opex flex. Most plausible 2028–30.
- **Probability-weighted haircut to 2030 revenue:** about **4–7%**, central ~5.5% [estimate: 0.3×0 + 0.45×4% + 0.25×15%]. Adj. EBITDA margin: about **2–5 pts** after partial opex flex.
- **Caveat:** in practice a price cut would also raise volume (more customers and budget). These static numbers overstate the net damage in the base case and may understate it in the bear case, if the cut is forced by share loss.

---

## 9. Leading indicators (Q3'26 print on Nov 4, 2026, and after)

1. **Gross margin.** It should hold at or above 78–80% while revenue grows. A fall below the 75% floor without a cost explanation would be the first quantitative sign of spread compression.
2. **AR ÷ quarterly revenue** (0.73 in Q2'26). A sustained rise without a payment-mix explanation would suggest falling take.
3. **Revenue growth minus active-customer growth** (−3 pts in Q1–Q2'26). If it widens beyond −8 to −10 pts while the expansion rate stays above 115%, price rather than mix would be the likelier cause.
4. **Allowance additions** (~$2.65M/yr) and any new contra-revenue line for agency rewards.
5. **Management language:** any first mention of "pricing," "discounts," "rebates" or "take rate" (none so far). Also any disclosure of agency revenue share.
6. **Competitive launches:** a Meta CTV product; Amazon Full-Funnel adoption among SMB sellers; Roku Ads Manager pricing post-Fox.

---

## 10. Data gaps

- **The MNTN take rate, gross billings, CPMs charged and the margin are not disclosed.** The Help Center states it explicitly: "we don't disclose our margin." All take-rate figures here are AR- or AP-based estimates (±10 pts).
- **No public minimum-spend history.** It is not possible to document whether minimums were cut. Current materials state none.
- The size and accounting of agency "Rewards for Media Spend" (cash back) and the agency share of revenue are undisclosed.
- The SMB NRR / expansion rate has been disclosed only as "well north of 115%" (Q4'25). No cohort or churn data, and no Q1–Q2'26 update was found (only the Q4'25 call transcript was retrievable).
- **Amazon DSP fee levels are reported only via anonymous sources and trade press.** Amazon publishes no fee schedule.
- Current Prime Video CPMs (beyond the 2024 launch range), IAB/eMarketer programmatic CTV CPM series, and TTD's quarterly 2026 gross spend could not be retrieved.
- The ANA has not published a CTV-specific transparency or TrueK study, as far as I could find.
- The full text of the Google ad-tech remedies opinion was not reviewed; the summary comes from a trade podcast.
- Q1'26 and Q2'26 MNTN call transcripts and any investor-conference remarks on pricing were not retrievable (the search budget was exhausted).

---

## Sources

1. MNTN, Form 10-K FY2025, SEC, 2026-02-19. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm
2. MNTN, Form 10-Q Q2 2026, SEC, 2026-08-10. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm
3. MNTN, Form 10-Q Q1 2026, SEC, 2026-05-11. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000040/mntn-20260331.htm
4. MNTN, Form 10-Q Q3 2025, SEC, 2025-11-10. https://www.sec.gov/Archives/edgar/data/1891027/000189102725000022/mntn-20250930.htm
5. MNTN, Form 10-Q Q2 2025, SEC, 2025-08-11. https://www.sec.gov/Archives/edgar/data/1891027/000189102725000012/mntn-20250630.htm
6. MNTN, Q2 2026 earnings release (8-K Ex-99.1), 2026-08-04. https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm
7. MNTN, Q1 2026 earnings release, 2026-05-05. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000038/mntnearningsrelease2026-q1.htm
8. MNTN, Q4 2025 earnings release, 2026-02-10. https://www.sec.gov/Archives/edgar/data/1891027/000189102726000004/mntnearningsrelease2025-q4.htm
9. MNTN, Q3 2025 earnings release, 2025-11-04. https://www.sec.gov/Archives/edgar/data/1891027/000189102725000019/mntnearningsrelease2025-q3.htm
10. MNTN, 424B4 IPO prospectus, 2025-05-22. https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm
11. MNTN, DRS/A (FY2022 financials), 2023-05-12. https://www.sec.gov/Archives/edgar/data/1891027/000110465923059878/filename1.htm
12. SEC staff comment letter to MNTN, 2022-01-13. https://www.sec.gov/Archives/edgar/data/1891027/000000000022000466/filename1.pdf ; MNTN response letters 2022-02-14 and 2022-03-29: https://www.sec.gov/Archives/edgar/data/1891027/000110465922023056/filename1.htm , https://www.sec.gov/Archives/edgar/data/1891027/000110465922039496/filename1.htm
13. MNTN Q4 2025 earnings call transcript, The Motley Fool, 2026-02-10. https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/
14. MNTN Help Center, "Understand MNTN's Pricing Model," 2026-02-09. https://help.mountain.com/en/articles/8054978-understand-mntn-s-pricing-model
15. MNTN Help Center, "Understand Billing and Payment," updated 2026-08-07. https://help.mountain.com/en/articles/6512120-understand-billing-and-payment
16. MNTN Help Center, "Set Your Campaign Budget," n.d. https://help.mountain.com/en/articles/6512145-set-your-campaign-budget
17. MNTN blog, "Our Enhanced Self-Signup Flow Is Live," ≈June 2025. https://mountain.com/blog/our-enhanced-self-signup-flow-is-live/ ; signup page https://mountain.com/performance-tv/b2c/signup/
18. MNTN IR, "MNTN Agency-Led Accounts Grow 4x in 2025…," 2025-09-29. https://ir.mountain.com/news/news-details/2025/MNTN-Agency-Led-Accounts-Grow-4x-in-2025-as-Demand-for-Performance-TV-Surges/default.aspx
19. MNTN IR, "PubMatic and MNTN Partner…," 2025-10-13. https://ir.mountain.com/news/news-details/2025/PubMatic-and-MNTN-Partner-to-Expand-Premium-CTV-Market-Driving-Net-New-Advertiser-Demand-and-Unlocking-a-10-Publisher-Revenue-Lift-2025-UGsKbrwxD6/default.aspx
20. MNTN IR, "MNTN Appoints Frank Lee as SVP of Agency Partnerships," 2026-08-19. https://ir.mountain.com/news/news-details/2026/MNTN-Appoints-Frank-Lee-as-Senior-Vice-President-of-Agency-Partnerships/default.aspx
21. MNTN IR, "MNTN To Announce Third Quarter 2026 Financial Results on November 4, 2026," 2026-10-14. https://ir.mountain.com/news/news-details/2026/MNTN-To-Announce-Third-Quarter-2026-Financial-Results-on-November-4-2026/default.aspx
22. MNTN newsroom (CNBC interview), "Streaming ad services will have a price war, says MNTN CEO," ≈2022-12-30. https://mountain.com/news/streaming-ad-services-will-have-a-price-war-says-mntn-ceo/
23. Quo Vadis (Tom Triscari), "#119 MNTN IPO + Valuation Update," 2025-05-27. https://www.quovadisnews.com/p/119-mntn-ipo-valuation-update
24. The Trade Desk, Form 10-K FY2025, SEC, 2026-02-27. https://www.sec.gov/Archives/edgar/data/1671933/000167193326000014/ttd-20251231.htm
25. The Trade Desk, Form 10-K FY2023 (2024-02-15) https://www.sec.gov/Archives/edgar/data/1671933/000167193324000014/ttd-20231231.htm ; FY2021 (2022-02-16) https://www.sec.gov/Archives/edgar/data/1671933/000156459022005385/ttd-10k_20211231.htm ; FY2019 (2020-02-28) https://www.sec.gov/Archives/edgar/data/1671933/000156459020007498/ttd-10k_20191231.htm
26. The Trade Desk, Form 10-Q Q2 2026, 2026-08-06. https://www.sec.gov/Archives/edgar/data/1671933/000167193326000086/ttd-20260630.htm ; Q2 2026 release https://www.sec.gov/Archives/edgar/data/1671933/000167193326000085/ttd-20260806x8kexx991.htm ; Q3 2025 10-Q https://www.sec.gov/Archives/edgar/data/1671933/000167193325000144/ttd-20250930.htm
27. The Trade Desk, 8-K (Item 2.05 restructuring), 2026-09-04. https://www.sec.gov/Archives/edgar/data/1671933/000119312526382690/d118889d8k.htm ; 8-K (CFO change), 2026-01-26 https://www.sec.gov/Archives/edgar/data/1671933/000119312526021804/d20637d8k.htm
28. Magnite, Form 10-K FY2025, 2026-02-25. https://www.sec.gov/Archives/edgar/data/1595974/000159597426000007/mgni-20251231.htm ; Q2 2026 release, 2026-08-05 https://www.sec.gov/Archives/edgar/data/1595974/000162828026053334/a991-earningsq22026.htm
29. PubMatic, Q2 2026 release, 2026-08-06. https://www.sec.gov/Archives/edgar/data/1422930/000142293026000029/q226pressrelease.htm
30. Viant Technology, Q2 2026 release, 2026-08-10. https://www.sec.gov/Archives/edgar/data/1828791/000182879126000068/dsp-20260810xexx991.htm
31. Roku, Form 10-Q Q2 2026, 2026-08-06. https://www.sec.gov/Archives/edgar/data/1428439/000162828026054335/roku-20260630.htm ; Q2 2026 shareholder letter https://www.sec.gov/Archives/edgar/data/1428439/000162828026054321/a04fy2026q2exhibit991.htm
32. Amazon.com, Q2 2026 earnings release (8-K Ex-99.1), 2026-07-30. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm
33. Amazon Ads, Amazon DSP product page, accessed 2026-10-15. https://advertising.amazon.com/solutions/products/amazon-dsp
34. AdExchanger (A. Vargas), "Omnicom Allegedly Pivoted A Chunk Of Its Q3 Spend From The Trade Desk To Amazon," 2025-11-18. https://www.adexchanger.com/platforms/omnicom-allegedly-pivoted-a-chunk-of-its-q3-spend-from-the-trade-desk-to-amazon/
35. AdExchanger (S. Caputo, op-ed), "Why Amazon Is Gaining Ground In CTV And The Trade Desk Is Losing Its Lead," 2026-03-04. https://www.adexchanger.com/on-tv-and-video/why-amazon-is-gaining-ground-in-ctv-and-the-trade-desk-is-losing-its-lead/
36. AdExchanger (S. Sluis), "Will The Trade Desk Right-Size Its Margins?," 2026-03-05. https://www.adexchanger.com/the-big-story/will-the-trade-desk-right-size-its-margins/
37. AdExchanger (J. Hercher), "The Trade Desk's Revenue Growth Stalls As Big Brands Tighten Their Belts," 2026-08-07. https://www.adexchanger.com/programmatic/the-trade-desks-revenue-growth-stalls-as-big-brands-tighten-their-belts/
38. AdExchanger (J. Hercher), "Why Wall Street Turned Against The Trade Desk," 2026-09-11. https://www.adexchanger.com/platforms/why-wall-street-turned-against-the-trade-desk/
39. AdExchanger (J. Hercher), "Amazon Ads And The Amazon DSP Get An Agentic Rebrand," 2026-09-29. https://www.adexchanger.com/platforms/amazon-ads-and-the-amazon-dsp-get-an-agentic-rebrand/
40. AdExchanger (S. Caputo, op-ed), "The Amazon Ads Lawsuit Raises Questions About Auction Disclosure…," 2026-09-09. https://www.adexchanger.com/data-driven-thinking/the-amazon-ads-lawsuit-raises-questions-about-auction-disclosure-dsp-buyers-need-to-ask/
41. AdExchanger (S. Sluis), "Auctions In The Crosshairs" (podcast), 2026-09-11. https://www.adexchanger.com/the-big-story/auctions-in-the-crosshairs/
42. AdExchanger (V. McNally), "Why MNTN's CEO Isn't Sweating Media Consolidation," 2026-08-07. https://www.adexchanger.com/ctv-roundup/why-mntns-ceo-isnt-sweating-media-consolidation/
43. AdExchanger (A. Boyle), "Prime Video Went AVOD. But Is It Delivering…," 2024-02-02. https://www.adexchanger.com/ctv-roundup/prime-video-went-avod-but-is-it-delivering-on-its-promise-for-advertisers-and-consumers/
44. AdExchanger, Daily News Roundup (citing Ad Age on streaming supply and pricing), 2024-10-04. https://www.adexchanger.com/daily-news-roundup/friday-04102024/
45. AdExchanger (S. Sluis), "The Big Story: Programmatic Fog" (ANA study), 2023-12-07. https://www.adexchanger.com/the-big-story/the-big-story-programmatic-fog/
46. AdExchanger (A. Schiff), "The ANA Says Advertisers Are Spending Way Less On MFA…," 2024-06-17. https://www.adexchanger.com/marketers/the-ana-says-advertisers-are-spending-way-less-on-mfa-but-programmatic-aint-fully-transparent-yet/
47. AdExchanger, Daily News Roundup, "Is Full Transparency POSSIBLE?; Meta Makes Moves Into CTV Advertising," 2026-04-28. https://www.adexchanger.com/daily-news-roundup/is-full-transparency-possible-meta-makes-moves-into-ctv-advertising/
48. AdExchanger, tag page "CTV" (headline: Fox's $22B Roku acquisition podcast, 2026-06-18), accessed 2026-10-15. https://www.adexchanger.com/tag/ctv/
49. Digiday (S. Joseph, K. Scanlon), "Netflix turns to Amazon to make its ads easier to buy," 2025-09-10. https://digiday.com/marketing/netflix-turns-to-amazon-to-make-its-ads-easier-to-buy/
50. Digiday (S. Bradley), "What's behind Netflix's CTV market share jump," 2026-02-24. https://digiday.com/future-of-tv/whats-behind-netflixs-ctv-market-share-jump/
51. Digiday (T. Peterson), "Future of TV Briefing: In TV ad market's swing to streaming, cheap inventory is in demand," 2026-08-12. https://digiday.com/future-of-tv/future-of-tv-briefing-in-tv-ad-markets-swing-to-streaming-cheap-inventory-is-in-demand/
52. Digiday (R. Shields), "Meta eyes CTV expansion to fuel its next wave of ad growth," 2026-04-27. https://digiday.com/future-of-tv/meta-eyes-ctv-expansion-to-fuel-its-next-wave-of-ad-growth/

---

## Verification (adversarial check)

*Checked 2026-10-15 by an independent fact-checker. Primary filings were downloaded straight from SEC EDGAR and searched as text. Trade-press items were opened at the cited URL. The shared web-search budget ran out partway through, so the check for any Meta CTV launch after April 2026 relied on AdExchanger's Meta and CTV tag pages, not on open search.*

| # | Finding | Verdict | Correct value / note | Evidence |
|---|---|---|---|---|
| 1 | MNTN prices on dCPM, charges no separate fees, keeps an undisclosed margin | **Confirmed** | The page says verbatim: "MNTN uses a dynamic CPM (dCPM) pricing model"; "does not charge separate fees for services or technology"; "we retain a portion of your overall media spend as a margin"; "we don't disclose our margin." It was updated 2026-02-09. | https://help.mountain.com/en/articles/8054978-understand-mntn-s-pricing-model |
| 2 | Bills gross, reports revenue net (agent); AR recorded at gross billings; take rate and billings not disclosed | **Confirmed** | 10-K: "We bill our customers on a gross basis, inclusive of the cost of procuring the advertising inventory … revenue on a net basis which represents gross billings net of amounts we pay suppliers"; "we do not act as the principal"; "accounts receivable are recorded at the amount of gross billings." The 10-K gives no figure for gross billings or the take rate. | https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm |
| 3 | Implied take rate ~46–60% in Q2'26; Quo Vadis ~40% for FY24 on ~$557M gross spend | **Unverifiable** (estimate). Inputs and arithmetic check out. | Q2'26 AR $59,985K and revenue $82,537K are confirmed, so 82.5×(1.0–1.3)/(3×60.0) = 45.8–59.6%. Billing terms are confirmed: billed monthly for the prior month, cards charged "typically by the 10th," Net 30 for select customers. Quo Vadis does say $557M FY24 gross spend and a "40% take rate," derived from trade payables at an assumed 70 payable days. **Wrong source date:** the Quo Vadis post is dated **2025-05-27**, not 2026-08-10. An independent AP-based cross-check (Q2'26 AP & accrued of $53.8M at ~70 payable days) gives ~54%, inside the range. The invoice-share bound (0–30%) is an assumption; slower payers would push the take rate higher. | https://www.quovadisnews.com/p/119-mntn-ipo-valuation-update ; https://help.mountain.com/en/articles/6512120-understand-billing-and-payment ; https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm |
| 4 | GM: 66.5% FY21, 54.0% FY22, 70.0% FY23, 71.6% FY24 (74.6% ex-ME), 77.2% FY25, 81% Q1'26, 80% Q2'26; long-term target 75–80% | **Confirmed** (one rounding fix and two caveats) | FY21 is 65,974/99,305 = **66.4%**, not 66.5% (immaterial). FY22 54.0%, FY23 70.0%, FY24 71.6% (ex-ME 156.2/209.3 = 74.6%), FY25 77.2%, Q1'26 81%, Q2'26 80.3% all match. The 75–80% long-term GM target was reiterated on the Q4'25 call. **Caveats:** (a) GM has eased *sequentially* (82% Q4'25 → 81% Q1'26 → 80% Q2'26), so it is still expanding y/y but has not risen in the last two quarters. (b) Current GM already sits at or above the top of the target. The CFO said "we aspire to just have it be in the long-term range of 75 to 80," so management does not guide to further expansion. That leaves room for price or reinvestment without breaching the target. | https://www.sec.gov/Archives/edgar/data/1891027/000189102726000004/mntnearningsrelease2025-q4.htm ; https://www.sec.gov/Archives/edgar/data/1891027/000110465923059878/filename1.htm ; https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm ; https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/ |
| 5 | Revenue per TTM PTV customer ex-ME: ~$110K FY23, $94.1K FY24, $78.4K FY25, $74.2K TTM Q2'26 (−8.6% y/y); expansion "well north of 115%"; SMB NRR 108% FY24, 111% Q1'25 | **Confirmed** (estimate arithmetic) | Inputs: ex-ME revenue by quarter from the Q4'25 and Q2'26 releases; TTM customers of 1,426, 2,225, 3,020, 3,632 and 4,225. Results: 157.4/1,426 = $110.4K; $94.1K; $78.4K; 313.3/4,225 = $74.2K versus 245.2/3,020 = $81.2K, which is **−8.7%** (trivially different). SMB NRR of 108% and 111% is confirmed in the 424B4. The transcript confirms the "well north of 115%" quote. **Caveat:** the "expansion rate" "measures the spend of our current customers as compared to those same customers' spend a year earlier." It counts only surviving customers, excludes churn, and is not comparable to NRR. It is survivor-biased evidence for "mix, not price." | https://www.sec.gov/Archives/edgar/data/1891027/000189102726000004/mntnearningsrelease2025-q4.htm ; https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/ ; https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm |
| 6 | TTD: Q2'26 revenue +3% to $715.1M; existing-client spend fell; "volume and other discounts"; Q3 guide ≥$650M vs $739.4M; adj. EBITDA margin 34% vs 39%; ~15% workforce cut, $39–51M charges | **Confirmed** (numbers), with a framing caveat | Confirmed: Q2'26 revenue $715,057K vs $694,039K; adj. EBITDA $241M (34%) vs $271M (39%); Q3 guide "at least $650 million," with adj. EBITDA ~$160M; Q3'25 revenue $739,433K (so −12.1%); 8-K: ~15% of the workforce and $39–51M of cash charges, announced 2026-09-03. **Caveat:** the same 10-Q says revenue was *helped* by "a higher proportion of revenue earned from client spend due to increased pricing associated with value-added services" and by an accounting change (supplier components moved into platform operations rather than netted from revenue). The discounts only *partially offset* those gains. TTD's 2026 break is mainly a volume problem (existing-client spend), not a disclosed take-rate cut. The dossier's "fee compression is real in 2026" overstates what TTD disclosed. | https://www.sec.gov/Archives/edgar/data/1671933/000167193326000086/ttd-20260630.htm ; https://www.sec.gov/Archives/edgar/data/1671933/000167193326000085/ttd-20260806x8kexx991.htm ; https://www.sec.gov/Archives/edgar/data/1671933/000167193325000144/ttd-20250930.htm ; https://www.sec.gov/Archives/edgar/data/1671933/000119312526382690/d118889d8k.htm |
| 7 | Amazon DSP: 0% on owned-media PG and ~1% open web versus TTD ~20%; Omnicom shift alleged and TTD denied; fee discounts on third-party CTV, including Netflix from Q4'25 | **Confirmed** (third-party, anonymous sources) | AdExchanger (A. Vargas, 2025-11-18): "no fees for programmatic guaranteed deals on Amazon-owned media," 1% on open web, TTD "roughly 20%"; Omnicom moved "a double-digit share of its expected Q3 spend" per two anonymous sources. TTD "flatly denied" it; Omnicom did not confirm; Amazon declined to comment. Digiday (2025-09-10): Amazon discounts DSP fees for third-party CTV inventory, and Netflix inventory comes to Amazon DSP from Q4 in 12 markets. | https://www.adexchanger.com/platforms/omnicom-allegedly-pivoted-a-chunk-of-its-q3-spend-from-the-trade-desk-to-amazon/ ; https://digiday.com/marketing/netflix-turns-to-amazon-to-make-its-ads-easier-to-buy/ |
| 8 | Amazon Ads Agent: −8% cost per impression, −6% CPA; ads $19.8B (+26%); DVA+ and Full-Funnel Campaigns in Sept 2026 | **Confirmed**, with label caveats | Q2'26 release: advertising services $19,809M, +26%. "Advertisers using Ads Agent see 8% lower cost-per-impression and 6% lower cost-per-acquisition than those that don't use it." That is a user vs non-user comparison, not causal, and the release does **not** say it is SMB-specific. DVA+ and "Full-Funnel Campaigns" (for "small advertisers or sellers" expanding into streaming TV) come from **AdExchanger 2026-09-29 [third-party]**, not the cited Amazon release. That part is mislabeled "reported." The article gives no fee information. | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm ; https://www.adexchanger.com/platforms/amazon-ads-and-the-amazon-dsp-get-an-agentic-rebrand/ |
| 9 | CTV CPM deflation: Roku −12% Q2'26 (−13% 1H) on impressions +40% (+48%); Netflix ~$65 → <$30 by Sept 2025; Disney −4%; Prime Video $26–41 | **Confirmed**, with a label mix-up | Roku 10-Q: impressions +40% and +48%; average price per impression −12% and −13%, "driven by changes in product and country mix." That is a mix effect, not a like-for-like CPM cut. Netflix "CPMs debuted around $65 … at sub $30" (Digiday 2025-09-10). Disney impressions +8% and ad prices −4% (Digiday 2026-08-12). Prime Video CPMs "between $26 and $41" (AdExchanger 2024-02-02). **Mislabel:** the finding is tagged "reported," but only the Roku data are company-reported; Netflix, Disney and Prime are third-party. | https://www.sec.gov/Archives/edgar/data/1428439/000162828026054335/roku-20260630.htm ; https://digiday.com/marketing/netflix-turns-to-amazon-to-make-its-ads-easier-to-buy/ ; https://digiday.com/future-of-tv/future-of-tv-briefing-in-tv-ad-markets-swing-to-streaming-cheap-inventory-is-in-demand/ ; https://www.adexchanger.com/ctv-roundup/prime-video-went-avod-but-is-it-delivering-on-its-promise-for-advertisers-and-consumers/ |
| 10 | Meta is exploring CTV audience extension (Magnite, FreeWheel, OEMs), not launched; SMB CTV rivals | **Confirmed** | Digiday (R. Shields, 2026-04-27) reports CTV "audience extension" modeled on Audience Network, with Magnite, FreeWheel, OEMs and publishers named, and no product announced. It names tvScientific (Pinterest-owned) and Vibe as SMB performance-CTV rivals. Roku, Universal Ads and streamr.ai come from other sources, not this article. AdExchanger's Meta and CTV tag pages through 2026-10-15 show no Meta CTV launch; the 2026-10-15 "Ads Super Burst" item is TV-style buying in the Facebook and Instagram feeds, not CTV. This is a limited check because the search budget was exhausted. | https://digiday.com/future-of-tv/meta-eyes-ctv-expansion-to-fuel-its-next-wave-of-ad-growth/ ; https://www.adexchanger.com/tag/meta/ |
| 11 | Take-rate sensitivity on FY26 guide midpoints ($352M, $98.5M) | **Confirmed** (arithmetic on confirmed guidance) | FY26 guide: revenue $347–357M and adj. EBITDA $96–101M, so midpoints of $352M and $98.5M (28.0%). At T=50% (billings $704M): −1 pt = −$7.0M (−2.0%) and 26.5% margin; −5 pts = −$35.2M (−10%) and 20.0%; −10 pts = −$70.4M (−20%) and 10.0%. Revenue per point = 1/T = 1.67–2.22%. The margin hit per point is 1.2 pts at T=60% to 1.65 pts at T=45%, so "~1.5" is a mid-range figure. | https://www.sec.gov/Archives/edgar/data/1891027/000189102726000070/mntnearningsrelease2026-q2.htm |
| 12 | Probability-weighted 2030 haircut ~4–7% (central ~5.5%) | **Unverifiable** (judgment) | Central math checks: 0.30×0 + 0.45×4% + 0.25×15% = 5.55%. But the stated weight and impact ranges span **~3.0% to ~7.7%** (0.5×2% + 0.2×10% to 0.45×6% + 0.25×20%), so "4–7%" is narrower than the inputs support. **Source mislabel:** the cited MNTN 10-Q contains no such scenarios, and its date (2026-10-15) is wrong because the 10-Q was filed 2026-08-10. | n/a (own estimate) |
| 13 | AR ÷ quarterly revenue 0.96 (Q4'24) → 0.73 (Q2'26); AP & accrued ÷ revenue ~0.91–1.02 → 0.60–0.68 | **Confirmed** (data); the interpretation is unverifiable | AR: $66,900K (12/24) against Q4'24 revenue of $69.8M gives 0.96; $59,985K against $82,537K gives 0.73. AP & accrued: $63,564K (12/24) = 0.91×; $69,709K (6/25) = 1.02×; $59,543K (12/25) = 0.68×; $44,321K (3/26) = 0.60×; $53,818K (6/26) = 0.65×. Q3'25 was in between at 0.78×. **Caveat:** Q4'24 AR and revenue include Maximum Effort. A like-for-like post-divestiture comparison (Q2'25 at 0.90 → Q2'26 at 0.73) still shows the decline. Faster collections or supplier payments could also explain the ratios. | https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm ; https://www.sec.gov/Archives/edgar/data/1891027/000189102725000012/mntn-20250630.htm ; https://www.sec.gov/Archives/edgar/data/1891027/000189102726000040/mntn-20260331.htm |
| 14 | Q2'26 quarterly-active PTV customers +24% and revenue +20.6%, so spend per active customer ~−3% | **Confirmed** | 10-Q: "Active PTV customers increased 24%." Revenue rose $14.1M (20.6%), with PTV +$14.2M. 1.206/1.24 − 1 = −2.7%. TTM customers grew 39.9%, a different basis. Q1'26 quarterly-active customers rose 26%, and Q1 revenue included $1.7M of creative-credit breakage (confirmed). | https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm ; https://www.sec.gov/Archives/edgar/data/1891027/000189102726000040/mntn-20260331.htm |

**Net assessment.**
- **Reported facts hold up.** Every reported number checked (pricing model, accounting, gross margins, customer counts, receivables, payables, and the TTD, Amazon and Roku figures) matches the primary source. The only numeric fix is FY21 GM at 66.4% versus 66.5%.
- **Main corrections are framing and labels, not numbers:**
  - TTD's 2026 slowdown is disclosed as an existing-client volume problem. Its revenue share of spend was *helped* by pricing; discounts were only a partial offset.
  - MNTN's "expansion rate" is a survivor-only metric, not NRR.
  - Current GM is already at or above the 75–80% long-term target, and has eased sequentially for two quarters.
  - Source labels and dates need fixing: the Quo Vadis post is dated 2025-05-27; Amazon's DVA+ and Full-Funnel launches, and the Netflix, Disney and Prime CPMs, are third-party, not reported; the scenario finding cites a 10-Q that does not contain it.
