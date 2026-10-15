# MNTN critic pass: brief coverage, contradictions between dossiers, and weak sources (as of 2026-10-15)

I read these files in full: `00-evidence-pack.md` (all 15 dossiers and their verification sections), `00-model-output-v1.md`, `mntn/model/mntn_model.py`, `mntn/model/historicals.py`, and the three judge files (`P-judge_*.md`).

I made three new checks:
- **WebFetch** of the Adobe Firefly plans page.
- **FY25 10-K text search** (local copy at `dl_sec/10k2025.txt`). The ">$100K customers" count is not updated after the IPO. The only FY25 "active PTV customers" figure is +63.2%, which equals the trailing-12-month (TTM) count growth.
- **Q2'26 10-Q text search** (local copy at `dl_sec/10q2026q2.txt`). It says MNTN "is not currently a party to any material legal proceedings".

**Legend.**
- **FULL**: the pack answers the item.
- **PARTIAL**: some of the answer is missing.
- **NONE**: no answer.
- **(a)**: findable with one more targeted fetch.
- **(b)**: genuinely undisclosed or unavailable. The report must say so explicitly.

---

## 1. Coverage of every item in the brief

### Part 1: Understanding the business

- [x] **FULL: How MNTN makes money (what it charges for; gross vs net; cost of revenue).**
  - Pricing is a dynamic CPM with no separate tech or data fees. MNTN "keeps a share of your media spend" and says "we don't disclose our margin" [H; Help Center 2026-02-09].
  - It bills gross and books revenue net, as an agent [A; 10-K FY25].
  - Cost of revenue is hosting, data, third-party DSP platform fees, personnel and amortization of capitalized software [A].
  - Creative is about 1% of revenue [A; estimate].
  - Missing:
    - **Take rate.** (b) Undisclosed. The report must say only estimates exist.
    - **Tier pricing for Express, Pro and Premium.** (a) Partly findable. mountain.com says both "No minimums" and "as little as $2,000" [N]. Fetch https://mountain.com/express/ or search help.mountain.com for "Express".
    - **Size and accounting of agency cash-back rewards.** (b) Undisclosed.
- [ ] **PARTIAL: Customer mix by size.**
  - What exists: small-business share of revenue about 6% (FY24/Q4'24), 12% (Q1'25) and about 15% (Q3'25); mid-sized 79–86%; SMBs 91–92% of PTV revenue [C, J; 424B4, AdExchanger].
  - (b) Customer counts by size, size definitions and any 2026 mix are undisclosed.
  - (b) Customers with more than $100K of net revenue are disclosed only for FY23 (297) and FY24 (421). I confirmed by text search that the FY25 10-K has no update.
- [ ] **PARTIAL: Retention and NRR.** The last real NRR was SMB NRR of 108% (FY24) and 111% (Q1'25) [C; 424B4]. Since the IPO there is only a survivor-based, verbal "expansion rate well north of 115%" (b).
- [ ] **NONE: Cohorts.** (b) Never disclosed. C checked the S-1 and all later filings.
- [x] **FULL: Concentration.** Top-10 customers were about 17% of FY25 revenue and about 20% of 1H26. No customer exceeds 10% [A, C].
- [x] **FULL, with definitional caveats: Revenue per customer by quarter, and whether falling spend is a deliberate move to smaller customers or pricing pressure.**
  - The TTM series runs Q4'24 to Q2'26 [C]. In-period customer growth is available for Q1'25 to Q2'26.
  - (b) Q4'25 in-quarter growth is undisclosed; the 10-K gives only the annual +63.2%, which is the TTM growth.
  - (b) A TTM series before Q4'24 needs 2023 quarterly revenue, which is not public [J].
  - The answer the evidence supports:
    - In 2025 the fall was deliberate down-market mix: spend per in-period customer fell 21–27%.
    - In 2026 the gap between customer and revenue growth is mostly the TTM-versus-in-period lag plus a real slowdown in winning customers [C; verification #4].
    - Pricing or take-rate pressure is unproven and cannot be measured without a take rate.
- [ ] **PARTIAL: Supply.**
  - Covered: direct deals plus SSPs (PubMatic, Magnite); >99% private-marketplace (PMP) deals per the CEO; named networks [D, B]; reliance on multiple unnamed DSP vendors [F; 10-K].
  - Missing:
    - (b) Supplier concentration and DSP vendor identities.
    - **Netflix access** is contested. (a) Query "MNTN Netflix inventory 2026", or check MNTN's network/inventory page. Even then, report it as contested.
    - YouTube and Amazon: there is no evidence of access.
- [x] **FULL (qualitative): Moat test (conversion data, attribution, integrations, ease of use, creative tools, brand).** Sources are D, F, G, I, M and N, plus the strategy judge's table. (b) Win/loss rates and churn are undisclosed.
- [x] **FULL: Growth, the slowdown and guidance reliability.**
  - Growth by period: FY25 ex-ME +36.0%; Q1'26 ex-ME +25% (about 21.8% without the $1.7M expired creative credits); Q2'26 +21% [A, B].
  - Guidance lands 0.0% to +1.9% above the midpoint. The average is +0.97%, or +0.4% excluding the credits [B; verification].
  - **Basis to state in the report.** The brief's "2025 ~36%" and "2026 ~24%" are ex-Maximum Effort (ME) figures. On GAAP the numbers are +28.6% and +21.3% (guidance midpoint) [J, O].

### Part 2: AI threats (mechanism / evidence / likelihood / timing / revenue impact / margin impact)

| # | Threat | Status | What exists | What is missing |
|---|---|---|---|---|
| 1 | Walled gardens (and why an SMB would choose MNTN) | **FULL** | [E]. Scenarios at 40/45/15% give 2030 revenue of $705M / **$553M** (corrected from $555M) / $410M. Weighted ≈ **$592M** [estimate]. Margin plateaus at 28–32% in B and falls to the low 20s in C. | (b) Amazon and Google do not disclose SMB CTV adoption; Meta has no CTV roadmap. |
| 2 | Agentic buying | **FULL** | [F]. Weighted 2030 effect **−8.7%**. Range **−6.5% to −10.9%** (corrected; −5% to −12% was the base-case range). Margin: each 1% of revenue lost ≈ 3.6% of EBITDA. Timing: pilots 2026, pricing pressure 2027, material 2028–30. | (b) No platform discloses agentic dollar volume; MNTN's MCP usage is undisclosed. |
| 3 | Cheaper competition (AI-native and established) | **PARTIAL** | [G]. Vibe: $50/day, $15–35 simulator CPM, 10,000+ advertisers. Universal Ads: no minimum. Adwave: $30/day. Paramount: from $7 CPM. Base: growth fades to mid-teens; 0–3 points of take-rate or gross-margin erosion. | No explicit probability; derive one from G's base/bear wording. Funding and traction of AI-native startups (Adwave, Olyzon, StackAdapt, Madhive) unverified. G did not research YouTube/Google Ads SMB TV in depth (E covers it partly). |
| 4 | Fee pressure | **FULL** | [H]. Weighted haircut **~3.0–7.7% of 2030 revenue** (central 5.55%; corrected from 4–7%). Margin −2 to −5 points. | Use the verified framing for The Trade Desk: its 2026 slowdown is mainly lower existing-client volume, not a disclosed take-rate cut. |
| 5 | Creative commoditization (Veo, Sora, Runway, Firefly vs QuickFrame AI) | **Now FULL** on revenue; **PARTIAL** on margin | [I]. Veo 3.1 at $0.08–0.40/s. Sora API removed 2026-09-24. Runway is in the full dossier I (not the pack): $15/$35/$95 a month, about $0.19/s on Pro [third-party]. **Firefly fetched now:** Standard $9.99/mo (up to 20 five-second videos), Pro $19.99 (40), Pro Plus $49.99 (100), Premium $199.99 (unlimited). That is about **$0.10 per second** of video on every capped tier; resolution is not stated [third-party list price; adobe.com/products/firefly/plans.html, accessed 2026-10-15]. Likelihood ~80%; timing 2026–28. | (b) Where AI inference cost is booked and how much it is. Margin impact is unquantified beyond the CEO's "essentially gross margin neutral". |
| 6 | Budget migration to AI assistants and AI search ads | **PARTIAL** | [J]. Growth drag 0 to −1 point a year (base) and −2 to −3 points (bear). | Margin impact not quantified. The verifier says the base may be optimistic because MNTN's budgets come from search and social, the pools AI ads take from. (b) No survey of SMB reallocation away from CTV. |

### Part 3: AI upside (same format)

| # | Upside | Status | Notes |
|---|---|---|---|
| 1 | Market expansion; QuickFrame AI signup-to-paying conversion | **PARTIAL** | **(b) Conversion is undisclosed.** Arithmetic caps it at about 1–3% [I; estimate]. Express converts about 3–10% [estimate]. 95–97% of customers are first-time TV advertisers, which **pre-dates** the AI launch [I]. Probabilities: ~65% for higher customer counts, ~45% for revenue re-accelerating above 25% [I]; N's hypothesis H1 ~45%. |
| 2 | Better results leading to more spend per customer | **PARTIAL** | All performance-lift claims are self-reported. The only third-party evidence is a 32-advertiser Northbeam beta and an undated Rockerbox stat relayed by MNTN [N]. Nothing links them to spend per customer. (b) No independent lift studies. N's H2 ~60%. |
| 3 | Margins (AI lowering cost; R&D payoff) | **FULL** | Answer: not yet. T&D +52%. Gross-margin gains are not from AI. The −38% cost-of-revenue headcount came from the restructuring [N; corrected bridge; M]. N's H3 ~30%. |
| 4 | Distribution through Adobe, Google, HubSpot | **FULL** | Answer: not a default channel. Adobe's own docs omit MNTN; HubSpot shows 100+ installs; MNTN's MCP is in beta [N, F]. N's H4 ~25%. |
| 5 | Data flywheel | **PARTIAL** | Scale is documented: 81M conversions and 565M verified visits [N; 424B4]. **(b) No evidence that performance improves as data grows.** IP is weak ("minimal patent protection", no MRC accreditation). N's H5 ~50%. |

### Part 4: Verdict and analogs

- [x] **Evidence: FULL.** The analogs cover AppLovin, The Trade Desk, Roku, Magnite, PubMatic, Criteo, Teads, DV, IAS and Innovid [O]. The judges supply signposts for the next 4–8 quarters.
- [ ] **Consistency: PARTIAL.** Three things need fixing; see Section 2, rows V1–V3:
  1. Dossier scores use three scales (−5..+5, −3..+3, −2..+2).
  2. The judges disagree.
  3. The model's scenario probabilities do not match the verdict probabilities.

### Part 5: Financial projections (model v1)

| Requirement | Status | Note |
|---|---|---|
| Customers × revenue per customer, split by size | PARTIAL | The split is a model calibration, labeled [estimate]. MNTN discloses no counts by size, and the calibration looks inconsistent (see M3). |
| New products: Express, Premium, QuickFrame monetization | PARTIAL | Express sits inside "small"; Premium is "upper"; QuickFrame AI is $1–7M in the base case. (b) Tier pricing and definitions undisclosed. |
| Gross margin; each opex line; SBC; adj. EBITDA; GAAP operating income; interest; taxes | FULL | FY25 bases tie to filings (T&D 17.0%, S&M 31.2%, G&A 19.9%). Book tax rate 26% with low cash tax is consistent with A. |
| Share count (buybacks vs dilution) | PARTIAL | Buybacks are assumed in every scenario; execution is undisclosed (M4). |
| NOLs and valuation-allowance (VA) normalization | PARTIAL | No further VA release is correctly assumed. The FY25 normalized GAAP EPS is not shown (M6). |
| 2026E–2030E revenue, adj. EBITDA, GAAP EPS, adj. EPS, FCF/share | FULL | |
| Bear/Base/Bull with probabilities, probability-weighted | FULL in form, PARTIAL in consistency | See M1 and M2. |
| Consensus and management LT targets, with every gap explained | PARTIAL | (b) No free FY28–30 consensus (StockAnalysis 2028+ is paywalled) and no free EBITDA consensus (FY27 $115–130M is backed out of price-target math). (b) Management has given **no revenue LT target**: there was no investor day, and the targets are verbal (GM 75–80%, adj. EBITDA 35–40%). Gaps to explain: M5 and M7. |
| Reverse-engineer the current price | FULL | Reconcile with K's corrected reverse DCF (M11). |
| Value each scenario with peer multiples | PARTIAL | Only EV/EBITDA (4x/7x/11x). EV/Sales and P/E cross-checks are missing; `pe_exit` is defined in the code but never used (M9). |
| Sensitivity: revenue growth vs EBITDA margin | FULL | |

### Part 6: Non-AI risks

- [x] **FULL: SMB ad spend in a downturn** [J].
  - Ad-recession probability 20–30%; trough-year growth about −20% to +8%. Use this range: J's §0 "−10% to +10%" is internally inconsistent.
  - (b) MNTN's own sensitivity to a downturn has never been observed, because 2022 quarterly data is not public.
- [ ] **PARTIAL: One-offs in year-over-year comparisons.**
  - **Maximum Effort:** FY26 GAAP growth is understated by about 2.3 points; no effect in 2027 [J].
  - **Q1'26 creative credits:** $1.7M recognized.
  - **Midterm political ads:** (b) political revenue is undisclosed. The CEO says exposure is immaterial. One open point: M found an MNTN help article on political advertising dated 2026-09-30, so MNTN may be actively selling 2026 midterm ads, which would make the Q4'27 comparison harder. (a) Search help.mountain.com for "political".
  - **World Cup:** (b) revenue undisclosed.
- [x] **FULL: TV inventory costs** [D, H].
- [x] **FULL: Insider selling and share structure** [L].
- [x] **FULL: SBC** [A, L].
- [x] **FULL, with a caveat: Quarters where EPS missed** [K]. Q2'25 and Q2'26 missed. Whether Q1'26 beat or missed depends on the data vendor (b).

### Evidence standards and output sections

- **Dated links:** present across the dossiers. Rockerbox is undated; several sources are snippet-level (see Section 3).
- **Not yet written:** the strongest bull and bear cases (bull-case-draft.md, premortem/ and redteam/ exist in the scratchpad; I did not review them), the two pre-mortems, and the bottom line. The evidence for all of them is present.
- **Scorecard:** the judges supply candidates, but some thresholds conflict (V4).

### Fetches done and still worth doing

- **Done:** Firefly pricing (above). FY25 10-K: no update to >$100K customers (b). Q2'26 10-Q: litigation not material and its nature undisclosed (b).
- **Still worth one fetch each:**
  1. MNTN Express pricing and minimum: https://mountain.com/express/.
  2. MNTN political-ads help article: help.mountain.com, search "political".
  3. Netflix access: query "MNTN Netflix inventory 2026". Expect it to stay contested.
- **Do not attempt:**
  - eMarketer (HTTP 403).
  - FY28–30 consensus (paywalled).
  - Buyback execution: it appears in the Q3 10-Q, expected around Nov 9–10, 2026 [estimate], and possibly in the Nov 4 release.

---

## 2. Contradictions between dossiers, and the value to use

### High impact

| # | Topic | Conflicting values | Use this |
|---|---|---|---|
| C1 | **Take rate** | A: 35–50%. Its receivables-based ~46% is an *upper bound*, because card-paying SMBs reduce receivables. H: 40–60%. Its receivables method treats ~46% as the *floor*; a payables cross-check gives ~54%. Quo Vadis: ~40% on FY24 (dated **2025-05-27**; H's 2026-08-10 date is wrong). M: Paparo relays an "81%" figure he doubts. | "Undisclosed; estimates span ~35–60%, central ~45% [estimate; low confidence]." The two dossiers adjust for the card-payer effect in opposite directions, so give a range, not a point. Run sensitivity at 40% and 50%. |
| C2 | **Take-rate sensitivity units** | F: "1% compression = −3.6% EBITDA". That means 1% of revenue. H: "1 point = 1.7–2.2% of revenue ≈ 1.5 points of EBITDA margin". | Both are right in different units. Always say "percentage points of take rate". 1 point = 2.0% of revenue at a 50% take rate and 2.5% at 40%, which is ~7% of FY26 EBITDA at 50%. |
| C3 | **Revenue per customer decline** | −8.7% (C, G: TTM ex-ME revenue per TTM customer); −8.6% (N, H); −9% (A, J); **−14%** (E, corrected; it mixes bases); −14% (C's quarterly "ARPU" method, which rests on an auto-transcript); about −3% (B, H, per quarterly-active customer); I's $101K → $80K → $74K includes ME revenue; H's FY23 ~$110K (ex-ME) vs A/C's ~$106K (PTV basis). | Headline: **$81.2K → $74.2K, −8.7% y/y** [estimate; C]. Underlying: spend per in-period active customer **−2.5% (Q2'26) and −3% to −4% (1H26)** [estimate; C verification], against −21% to −27% in 2025. Drop −14% and I's series. Always name the basis. The model's "77.6 (PTV)" FY25 figure vs C's $78.4K (ex-ME) is a basis difference to label. |
| C4 | **Small-business share** | C reads the 424B4 as mid-sized 86% / small ~6%. J and C's verification give the literal reading: mid ~79% / small ~13%. B and I attribute "6%" to Q4'24 via AdExchanger. | "SMBs 91–92% of PTV revenue [reported; 424B4]; small businesses ~6% (FY24) → 12% (Q1'25) [reported] → ~15% (Q3'25) [third-party; CEO via AdExchanger]." Footnote the 424B4 ambiguity. The model's ~13% for FY25 fits either reading. |
| C5 | **Stock reaction after Q1'26** | B: "+7.4% regular session, +2.4% after hours to $10.83" (Investing.com). K: **−22.8%** ($11.36 → $8.77, May 6; Yahoo chart). The task's price data matches K. | **−22.8%** close to close. Drop B's figure; it most likely comes from an auto-generated summary error. All-time-low close $7.78 on May 15 (52-week intraday low $7.68). |
| C6 | **Stock reaction after Q2'26** | B: −8% after hours ($10.02 → $9.24). K: **+3.8%** ($10.05 → $10.43). | Both are true. The after-hours drop reversed; **close to close +3.8% on Aug 5**. Then +34% to $13.46 on Sep 3, and about −30% to ~$9.40 on Oct 14. |
| C7 | **Stock reaction to the FY26 guide (Feb)** | B: "could not verify". K: +37.1% ($8.13 → $11.15). | Use K [third-party market data]. Caveat that "the stock reacts to guidance, not EPS" has a counterexample: Aug 6, 2025, −17.9% after an above-Street guide [K verification]. |
| C8 | **Q3 report date** | D: "unverified". F: "could not be confirmed". M: first "likely early Nov", later upgraded. Nine dossiers: Nov 4. | **Nov 4, 2026, after the close, webcast 4:30pm ET** [reported; MNTN IR PDF, 2026-10-14]. Q3 10-Q around Nov 9–10 [estimate]. |
| C9 | **Walmart–Vibe price** | F: "~$1.4B per trade reports (unverified)". G and O: $1.2B cash plus ~$180M retention. E: "close by end FY27" (stale). | "~$1.2B cash plus ~$180M retention (~$1.38B all-in) [third-party; WSJ via The Current, 2026-07-08]; Walmart disclosed no terms; closed Aug 4, 2026 [reported]." That is ~12x (13.8x with retention) a stale, undefined "$100M ARR" claim, and about 2.3–2.6x MNTN's $529M EV. |
| C10 | **eMarketer and other CTV forecasts** | D: $33.4B (2025) / $37.95B (2026, "+14.5%") / $46.89B (2028) / $51–53.4B (2029). Verification: only $33.4B is confirmed (Nov-2024 vintage, cited in the 424B4). The stated growth is really +13.6%; PubMatic cites $36.87B for 2025; the 2029 range mixes vintages. IAB: $29.3B, +11% (May); +13.8% (Jan, via Brainlabs, used by E and F); +15.6% (Sept). WPP: US streaming TV $27.6B, +21.5%. Madison & Wall: digital TV +3%. | Anchor the market level and growth on **IAB** (primary and dated). Show eMarketer as an upper reference from **one** vintage. Label 2030 at $56–59B as [estimate, extrapolated from unverified snippets]. Growth: +11–16% in 2026, ~10–12% a year in 2027–30 [estimate]. MNTN share is ~0.9% (eMarketer) or ~1.2% (IAB) on **net** revenue, and about 2% on estimated gross billings. D's ratios compare net revenue with gross spend; say so. |
| C11 | **Customer growth metric** | TTM +40% vs in-period +24%. The 10-Q says only "between the periods in comparison"; the three-month basis is explicit only in the Q3'25 10-Q [B, C verification]. E calls the ">115% expansion rate" NRR. | "Active PTV customers in the period +24% [reported; window inferred]." Never call the expansion rate NRR, and do not compare it with SMB NRR of 111%. |
| C12 | **Pinterest–tvScientific** | E: "expected close 1H26, not confirmed". G: closed **Feb 17, 2026, $465.1M** [reported; PINS 10-Q]. | Use G. The ~8–9x net-revenue multiple is weak: the same Digiday source misstated the deal price [O verification]. |
| C13 | **Supply reach** | D: YouTube, Netflix and Amazon (~54% of streaming) are inaccessible. D's verification: Amazon is #4, not #3, and the CEO says buys "go across" Netflix. | "No evidence of access to YouTube or Amazon (**~38%** of streaming time). Netflix is contested: CEO claim vs Netflix's programmatic partner list, which excludes MNTN." Use 54% only as an upper bound. |
| C14 | **Amazon–Roku 80M households** | D: "Roku (~80M households)". E's verification: that is the **combined** Amazon plus Roku reach (ComScore). | Combined. |

### Model and verdict consistency (new findings from this pass)

| # | Issue | Recommendation |
|---|---|---|
| V1 | Judges disagree. The financial judge says **Neutral** (55%). The industry and strategy judges say **At Risk** (55% each). Averaged bucket probabilities: Victim ~13%, At Risk ~45%, Neutral ~32%, Beneficiary ~9%, Winner ~1%. | Verdict: **At Risk, low-to-medium confidence (~45–55%), with Neutral a close second.** State why the financial lens differs: no damage shows in the reported numbers yet. |
| V2 | Dossier scores use −5..+5 (A, B, C, D, F, H, J, N, O), −3..+3 (I, M) and −2..+2 (strategy judge). | Normalize them before any comparison, or leave them out of the report. |
| V3 | **Scenario weights do not match the verdict.** The model's bear ("AI victim") carries 30% against ~13% Victim across the judges. The bull ("AI winner") carries 20% against ~10% Beneficiary plus Winner. | Either relabel the bear as a "compound At Risk/Victim and 2027 ad recession" case with an explicit bridge, or reweight it to roughly 15–20%. |
| V4 | **Scorecard threshold conflict.** The industry judge treats "receivables/revenue staying at **0.70 or above**" as a positive sign. In H's logic and the financial judge's, a *rising* ratio means more gross billings per net dollar, i.e. a lower take rate. Gross-margin break level: <76% (financial and industry judges) vs <75% (strategy judge). | Use the financial judge's direction: ≤0.80 confirms; ≥0.90 with unchanged billing terms breaks. Gross-margin break: <76% for two quarters. |

### Minor (fix wording)

- **Headcount:** L and N call mid-2026 headcount undisclosed. It is **451 at Jun 30, 2026** [reported; Q2'26 10-Q; B, M]. Revenue per FTE of $695K is an upper bound; it is ~$627K on average headcount [M verification].
- **Gross-margin drivers:** H and the original N credit hosting plus the ME divestiture. Use N's corrected Q2 bridge instead: revenue leverage, platform fees −$0.6M, personnel −$0.4M, amortization +$1.2M; ME is not a driver.
- **Deferred revenue:** "creative-credit deferred revenue $9.0M → $2.7M" is really **total** deferred revenue. Like for like it is $6.4M → $5.5M → $2.7M. The filing does not call the $1.7M "one-time" [I verification].
- **1H26 underlying growth:** I's ~16% is GAAP with ME in the base; B's ~21.1% is ex-ME. Use the ex-ME figure.
- **EV/EBITDA:** dossiers give 5.8x (A), 5.4x (K), 5.3–5.8x (G) and 4.5–5.2x (O). Use one table at **$10.25**:
  - Basic EV **$529M** = **5.4x** the FY26 guide midpoint and **~4.3x** FY27 EBITDA backed out of price-target math.
  - Diluted EV $569M = 5.8x and 4.6x.
  - At the $9.40 prior close, EV is $466M = 4.7x and 3.8x.
  - The buyback is 13.0% of shares at $10.25 and 14.2% at $9.40.
- **Share count:** B's ~74.2M and G's 73.9M are superseded by **74.80M basic** (Jul 31 cover) and **78.64M diluted** (Q2'26 weighted average).
- **Option strike:** ~$9.3 is superseded by **~$9.0 on ~14.6M non-performance options** [A verification]. The CEO's performance options are **not** "deep out of the money": they have a $3.79 strike and are gated by price hurdles from $25.40 to $508.04 [K verification].
- **Qualcomm sales:** A says execution is unconfirmed. L confirms it through the 13G/A: 147K shares left at Jun 30, 2026, so ~4.98M sold. Use L.
- **Northbeam "MNTN +29%":** G's verifier could not verify it (HTTP 402). M's verifier found it in a Northbeam-credited chart on Vibe's blog (2026-07-14). Use it, labeled [third-party, published by a competitor; low-to-medium confidence].
- **Supply claims:** ">99% PMP" (CEO) vs "98% direct" vs "100+ / 150+ / 200+ networks" (MNTN pages). Cite ">99% PMP [management claim]" and avoid a specific network count.
- **First-time TV advertisers:** 95% (10-K) / 96% (424B4) / 97% (CEO on the Q3'25 call) / ">90%" (HubSpot press release). Use **~95% [reported; 10-K FY25]**, and note it pre-dates QuickFrame AI.
- **Long-term S&M target:** 25–30% (Q4'25 transcript) vs 20–25% (garbled Q2'25 auto-transcript). Use 25–30% with a caveat.
- **Express conversion:** 1.4–14% (C) vs 3–10% (N, I). Use **~3–10% [estimate, if 200–700 payers]**.
- **QuickFrame AI pricing:** the CEO says "free" while the site lists $39/$99/$250 tiers. Present both. The help center says the first video is free and new PTV advertisers get three free AI TV ads.
- **QuickFrame AI beta date:** Oct 29 vs Oct 30, 2025. Say "late Oct 2025".
- **Reverse DCF:** K's −0.5% to −3.5% is superseded by **−0.4% to −2.2%** before SBC and **+2.8% to +4.7%** after SBC. The model gives 0.6% CAGR at a 30% margin. Headline: "the price implies roughly 0–5% growth".
- **The Trade Desk framing:** "fee compression is real in 2026" is overstated. The verified version: value-added pricing and an accounting change helped TTD's revenue share; its slowdown is mainly existing-client volume.
- **J's downturn range:** §0 says −10% to +10%. Use −20% to +8%.
- **SBC as a share of FY26 EBITDA:** 26–28% is superseded by 25–29% [L verification].
- **Homepage CPM:** ~$5.60 is superseded by **~$23.4** from the live calculator. Drop the "remnant inventory" inference [M verification].
- **Roku price per impression (−12%):** H's verification says it reflects product and country mix. Caveat it wherever it is used as evidence of CTV CPM deflation.
- **Amazon Full-Funnel/DVA+ timing:** Q1'26 (E) vs Sept 2026 (H, which actually rests on AdExchanger). Say "rolled out during 2026".
- **Q2'26 EPS consensus:** say "missed every vendor series ($0.09 vs $0.15–0.22)".
- **O's control premium:** at the $9.40 prior close, a 25–35% premium gives $11.75–12.70.
- **Wurl multiple:** ~8x, not ~10x.

### Model v1 defects against the evidence (priority order)

- **M1. Bear case more severe than any single dossier's bear.** Bear 2030 revenue of $290M (below FY25) is harsher than:
  - E's severe case: $410M at 15%.
  - D's 1%-share marker: $560–590M.
  - F's victim case: −25% to −40% at 20%.
  - H's bear: −10% to −20% at 20–25%.
  
  The model's probability-weighted 2030 revenue ($566M) also sits below E's walled-garden-only weighted figure (~$592M). Either bridge the bear explicitly (stacked threats plus recession) or soften it or its weight (see V3).
- **M2. Bear FY26 below guidance.** Bear FY26 revenue of $344.2M implies 2H26 growth of +19.6%, and bear EBITDA is $92.9M. Both sit **below the guidance lows** ($347M and $96M). MNTN's record is landing 0.0–1.9% above the guidance midpoint [B]. Set bear FY26 near the guide low unless there is a stated reason not to.
- **M3. Size split looks miscalibrated.**
  - The model has 1,182 customers averaging at least $200K (mid plus upper, 33% of the TTM count) in FY25.
  - But only **421 customers exceeded $100K in FY24 (19% of 2,225)** [C; 424B4], and the average fell about 16% in FY25.
  - The small-business $15K per customer comes from a CEO remark whose gross-vs-net basis is unclear [B, N]. It is consistent with a ~13% small-business revenue share only if it is roughly net; if it were gross, the implied small-customer count would exceed total customers.
  - Recalibrate, or label the split clearly as [estimate].
- **M4. Buybacks assumed everywhere.** The model has $30M (2026) and $70M (2027) in **every** scenario, but execution is undisclosed [L].
  - Bear diluted shares fall 22% (77.4M → 60.7M), which props up bear EPS.
  - The bear 2027 buyback ($70M) exceeds bear FCF ($64M).
  - Add a no-buyback case. Per L, that means +1.5–3% a year of dilution.
- **M5. Adjusted EPS vs consensus.** Base adjusted EPS of $0.90 (FY26) and $1.14 (FY27) compares with Yahoo "normalized" $1.05/$1.31 (2 analysts, definition unknown) **and** MarketBeat $0.87/$1.19 [K]. Present consensus as a range ($0.87–1.05 and $1.19–1.31). The model falls inside it, so do not call the difference a "below-Street" gap.
- **M6. FY25 not normalized.** FY25 GAAP EPS of −$0.13 uses 50.9M weighted shares (much of the year was pre-IPO). It includes a $26.4M loss on debt extinguishment and a $9.6M tax benefit from the VA release [A]. Show normalized FY25 and TTM figures: TTM GAAP EPS is $0.71 reported and ~$0.52 normalized [K]. State that no further VA release is expected ($0.7M remains).
- **M7. Gaps to management targets.** Base 2030 adj. EBITDA margin of 33.5% is below management's 35–40% target. Base S&M falls to 25.8% of revenue by 2030, against:
  - N's H4: don't cut S&M for AI distribution before evidence appears.
  - G and M: 30–35% near term.
  
  Explain both gaps.
- **M8. QuickFrame AI in the base case.** The base includes $1–7M of QuickFrame AI revenue; N says exclude it from the base. Immaterial, but label it.
- **M9. Valuation multiples.** Add EV/Sales (peer median ~2.15x NTM) and P/E per scenario. Note that base 7x EV/EBITDA is below the peer median (~7.75x) and below precedent deals (8–9x) [O].
- **M10. Price basis.** The model uses $10.25; the pack uses $10.24, $10.28 and $10.32. Also show the $9.40 prior close.
- **M11. Reverse DCF reconciliation.** See the reverse-DCF bullet in the minor list.
- **M12. D's market-share markers.** D's "1.5% share = base" marker ($840–890M) is about the model's **bull** case. It is not risk-adjusted and compares net revenue with gross spend; do not present it as a base.

---

## 3. Claims resting on weak sources (the report must caveat these)

**Management statements known only from third-party or machine transcripts** (no official transcript checked):
- [ ] **All call and conference quotes.** Sources are Motley Fool, Investing.com and AOL. The Q1'26 Motley Fool page is corrupted (it mixes in AtriCure text). The Investing.com Canaccord page is auto-written and has date errors.
- [ ] **Q2'25 call** (garbled Equibles auto-transcript only): Amazon "not competing"; 15% wallet share; minimum spend "$25K → ?"; S&M target 20–25%.
- [ ] **CFO's "ARPU $20,904"** (Q3'25, Equibles auto-transcript).
- [ ] **Long-term targets:** adj. EBITDA 35–40%, gross margin 75–80%, S&M 25–30%. All verbal; there was no investor day.
- [ ] **"Expansion rate well north of 115%":** verbal, undefined, survivor-based.
- [ ] **Express:** ">7,000 signups" and "hundreds paying". The CEO's "~$15K/yr" (small business) and "deep six figures" (mid-market) have unclear gross-vs-net basis.
- [ ] **QuickFrame AI:** 73K signups; "nearly all Express and 30–40% of mid-market use it"; "essentially gross margin neutral".
- [ ] **Other CEO claims:**
  - ">99% PMP"
  - "never lost a head-to-head test"
  - Pinterest/tvScientific "not competitive"
  - "LTV/CAC handily double digits"
  - buys "go across" Netflix
  - inbound ~77% of revenue
- [ ] **CEO's "$100M FCF":** contradicted by 1H26 FCF of $27.0M. Do not use it as an input.
- [ ] **Small business ~15% of revenue (Q3'25):** AdExchanger relaying the CEO.

**Company or vendor marketing claims:**
- [ ] **MNTN performance claims:**
  - MNTN Matched: 2–7x traffic and 2–3x ROAS, inconsistent across MNTN's own pages.
  - Intent scoring: +44% ROAS, described as "estimated" from a controlled rollout.
  - "129% lower CPA": could not be located.
  - Rockerbox (70% of advertisers, CPAs 18–33% lower): undated and relayed by MNTN.
  - Northbeam beta: n=32, in an MNTN press release.
- [ ] **MNTN coverage and IP claims:** 99%+ of US CTV households / 132M households / ~120M households; 98% direct; 100/150/200+ networks; "patented" Verified Visits (the 10-K says "minimal patent protection"); inventory cost down ~8% a quarter (prospectus).
- [ ] **Partnerships:** Adobe GenStudio integration and Google "early adopter" status are MNTN claims only, and Adobe's own docs omit MNTN.
- [ ] **Platform and competitor claims:**
  - Amazon Ads Agent: −8% CPM, −6% CPA.
  - Google: +7% conversions (internal experiment).
  - TTD: 32% CPA improvement (attributed to Zuma's modeling).
  - PubMatic: CPM 18% below target; +14% unique advertisers.
  - Butler/Till: 5.5x lower supply-chain cost (a multi-channel campaign).
  - Vibe: "$100M ARR" (undefined), 1,000+ MCP brands, MCP buying a "large portion of spend".
  - Paramount: CTV from a $7 CPM.
  - Universal Ads: 90% of US households (its linear self-serve covers Comcast-owned inventory only).
  - Roku, Paramount and Disney: $500 minimums (from third-party blogs).
  - Disney Campaign Manager: 4,200 brands (Jan 2024; stale).

**Snippets, secondary sources and blocked pages:**
- [ ] **Forecasts:**
  - eMarketer CTV figures (403; mixed vintages) and the AI-search ad path ($26B by 2029; the share path comes via Tech Monitor).
  - PwC 2030 (secondary source).
  - IAB +13.8% (via Brainlabs) and the Sept +12.3% (from a listing page).
- [ ] **AI ads:** OpenAI's ad-revenue plan ($2.5B → ~$100B; Axios via snippets, 403). ChatGPT's $1B run-rate (MediaPost relaying OpenAI). Meta "Muse" and Rufus figures (snippets).
- [ ] **Fees:** Amazon DSP 0% / ~1% (anonymous trade-press sources). The Omnicom shift from TTD to Amazon (alleged; TTD denied it). Google Buyer Direct ~10% cap (trade press). Removal of Amazon DSP minimums (agency blogs).
- [ ] **Deal values:** Walmart–Vibe price (WSJ via The Current). tvScientific ~$50M net revenue (unnamed Digiday sources).
- [ ] **Other single or unverified sources:**
  - Traditional production cost of $10K–$500K (a single aggregator).
  - YouTube's July-2025 share of 13.4% (secondary).
  - Kantar 2009 −12.3% (unverified).
  - Madhive, StackAdapt, Adwave and Olyzon figures (unverified).
  - The cause of AppLovin's −19.7% day (plaintiff-firm summary).
  - The "SMBs lack TV-grade creative" quote, which joins two separate CEO answers.

**Low-reliability alternative data:**
- [ ] Tranco ranks.
- [ ] Similarweb: one snapshot; quickframe.com −33% month on month conflicts with Tranco.
- [ ] BuiltWith (5,804 live sites) vs Wappalyzer (300).
- [ ] Google Trends: ambiguous search terms.
- [ ] Review counts: Blind (n=13), Trustpilot (n=2), Shopify (9 reviews), HubSpot ("100+" bucket).
- [ ] Northbeam: Vibe +1,900% vs MNTN +29%, published by Vibe, a competitor.
- [ ] Ari Paparo's commentary: he sits on Vibe's board.

**Consensus and market data:**
- [ ] "Normalized" EPS from two analysts, definition unknown; EPS series conflict across vendors.
- [ ] FY27 EBITDA backed out of price-target math.
- [ ] MarketBeat quarterly consensus (an aggregator).
- [ ] Price-target list does not reconcile with S&P's $18.10 mean and $13 low. Evercore's $22 rests on MarketBeat alone. Raymond James $15 vs $14 is unresolved.
- [ ] Causes of these stock moves are not attributed by the press: Aug 6, 2025 (−17.9%); Sep 3 to Oct 14, 2026 (−30%); Oct 15 (+9%).
- [ ] The current price comes from a single page fetch or IBKR snapshot.

**Analyst estimates that must keep [estimate] and a low-confidence label:**
- [ ] Take rate of 35–60%.
- [ ] Agentic buying under 1% of US CTV spend.
- [ ] All scenario probabilities (E, F, H, I, J, N).
- [ ] Growth drag from AI ads, in points per year.
- [ ] Downturn scenarios.
- [ ] Inference cost of $1.1–8.8M per half-year.
- [ ] QuickFrame AI ARR of $2–5M.
- [ ] 2030 CTV market of $56–59B.
- [ ] Express conversion of 3–10%.
- [ ] "16 of 19 points of the gap are definitional": arithmetic, not proof of cause.
- [ ] Revenue per FTE of $695K: an upper bound.
- [ ] The model's size split of customers and revenue per customer.