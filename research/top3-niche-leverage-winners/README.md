# Who benefits most relative to their size? Leverage winners in the top-3 niches, 2026–2030

*Follow-up to [The fastest-growing niche industries, 2027–2030](../niche-growth-2027-2030/README.md). Data as of 15 October 2026. Not investment advice.*

**Niches covered** (sizes from the prior report):

| | Niche | 2026 revenue | 2030 revenue, central (range) |
|---|---|---|---|
| **N1** | Merchant HBM4/4E logic base dies | ~$0.6B | ~$7.5B ($4–14B) |
| **N2** | Ultra-high-power InP CW lasers and external-laser-source (ELS) modules for co-packaged / near-packaged optics (CPO/NPO) | ~$0.19B | ~$2.3B ($1.0–4.5B) |
| **N3** | Merchant scale-up switch silicon for non-NVLink accelerator racks | ~$0.9B | ~$8B ($3.5–14B) |

## How to read this report

**Definitions** (all figures in USD):

| Term | Definition |
|---|---|
| Base revenue | TTM total revenue through the latest reported quarter |
| Current niche revenue | CY2026E (it includes guided and forecast 2H26). TTM-actual niche revenue is shown in the deep dives. |
| Incremental | 2030 base-case niche revenue minus current niche revenue |
| Net incremental | Incremental minus the legacy revenue the niche cannibalizes by 2030 |
| **Revenue leverage** | Incremental ÷ base revenue, gross and net. **Net is the ranking metric.** |
| Profit leverage | (Incremental × niche gross margin − cannibalized revenue × its gross margin) ÷ TTM gross profit |
| Valuation lens | Net incremental ÷ current enterprise value |

- **Scenarios.** "Low / base / high" are niche scenarios. Cannibalization scales with each scenario, because more CPO adoption displaces more pluggables. For net-negative names, the high-adoption case is therefore the worst case.
- **Hard-signal gate.** A company is ranked only if at least one hard signal ties its revenue to the niche as defined:
  - a filing disclosure;
  - a named design win or qualification;
  - a 10%+ customer tied to the niche;
  - dedicated capacity;
  - numeric guidance; or
  - customer or partner confirmation.

  Companies whose exposure is attribution only (our estimate of their share of the niche's spend), or a pure option, are still shown and still get a leverage figure. They are marked "No" and given no rank. Customers, downstream system builders and adjacent products are listed separately and not ranked.
- **Claim labels:** [R] reported fact · [G] company guidance · [3P] third-party estimate · [E] own estimate.
- **Evidence limits.** Company websites and SEC EDGAR could not be fetched from this environment, and web search was capped per research round. Financials, guidance and consensus therefore come from search-result summaries of filings, releases and transcripts, plus Interactive Brokers price and volume data. Several TTM quarters and consensus figures are flagged "unverified" in the deep dives. Almost no company discloses niche-level revenue, so niche figures are [E] unless stated.

---

## 1. Summary

**Top 5 across all three niches by net revenue leverage.** These are the companies that pass the hard-signal gate. Only 6 of the 24 revenue-earning companies screened pass it; the sixth is COHR (-2.0%).

| # | Ticker | Niche(s) | Net revenue leverage, base (low – high) | Profit leverage | Net incremental ÷ EV | Confidence | One line |
|---|---|---|---|---|---|---|---|
| 1 | **ALAB** | N3 | **1.41x** (22.2% – 3.20x) | 1.23x | 3.5% | medium | Scorpio X is the only merchant PCIe scale-up switch in volume (Trainium-linked per sell-side [3P]). 2030 niche ~$2.25B vs $1.2B TTM revenue; keeping the Trainium4/5 socket against NVLink Fusion is the swing factor. |
| 2 | **LITE** | N2 | **14.4%** (4.0% – 28.9%) | 19.8% | 0.6% | medium | Lead merchant supplier of ultra-high-power CW lasers into NVIDIA CPO light sources (multi-hundred-million PO; ELS modules from 2H27). ~$875M by 2030, but ~$350M of pluggable-laser cannibalization roughly halves the gain. |
| 3 | **MRVL** | N3 | **7.6%** (1.5% – 15.8%) | 8.0% | 0.3% | low | UALink 115T and XConn switches make it a credible #3 (~9% of the 2030 niche), but no socket is named. Weak hard signal; the rest of Marvell drives the stock. |
| 4 | **TSM** | N1 | **4.0%** (1.8% – 8.4%) | 3.5% | 0.3% | medium | Sole merchant HBM base-die foundry (~92% share): ~$6.2B net incremental, the largest dollar gain in any of the three niches, but only ~4% of a $157B base. |
| 5 | **AVGO** | N3 | **3.0%** (0.7% – 8.6%) | 3.1% | 0.2% | medium | AMD Helios (12 Tomahawk 6 per rack) and Tomahawk Ultra make it the #1 dollar winner in scale-up switch silicon (~$3B by 2030), but that is ~3% of an $89B base. |

**Highest raw ratio that fails the gate: POET Technologies (POET).**
- Net revenue leverage is 3.72x, but only because TTM revenue is $1.7M.
- Its only named light-source customer, Celestial AI, cancelled every PO after Marvell acquired it (notice dated 23 April 2026). The remaining agreements are with unnamed parties.
- Net incremental niche revenue is ~$7M by 2030, or 3.8% of EV. Treat it as an option, not exposure.

**Key findings**

1. **Only one name has real, high leverage: Astera Labs.**
   - Net revenue leverage is 1.41x (0.22x–3.2x) and profit leverage 1.23x.
   - Everything else that passes the gate is below 15%.
   - In all three niches the dollars go to companies that are already large: TSMC, Broadcom and Lumentum.
2. **HBM base dies are a TSMC story, with no small-cap leverage.**
   - TSMC has ~92% of merchant supply and ~$6.2B of net incremental revenue, the largest dollar gain in any niche. That is still only ~4% of its base.
   - Every US-listed small or mid cap linked to the niche is attribution-only. FormFactor, Teradyne, Camtek and Onto get their HBM revenue from core dies, stacks and packaging, which are outside this niche.
3. **In CPO lasers, the net effect wipes out most of the story.** CPO light sources replace pluggable transceivers that these companies also sell.

   | Company | Gross leverage | Net leverage |
   |---|---|---|
   | Lumentum | 26% | 14% |
   | Coherent | +8% | −2% |
   | Applied Optoelectronics | +6.5% | −10% |
   | Fabrinet | +1% | −10% |

   AXT is the clearest case of price far ahead of exposure. Substrate is ~0.5% of the value of an ultra-high-power laser, so AXT gets about $5M of niche revenue by 2030. The stock is up ~1,100% in 12 months; that move is driven by pluggable InP demand and Chinese export permits, not by this niche.
4. **In scale-up switch silicon, the dollar list and the leverage list are the same three companies in a different order.**
   - Dollar ranking: Broadcom (~$2.6B net), Astera Labs (~$1.7B), Marvell (~$0.7B).
   - Leverage ranking: Astera Labs 1.41x, Marvell 7.6%, Broadcom 3.0%.
   - Credo is often bundled into this theme. Its active electrical cables (AECs) are an adjacent product, not switch silicon, so it is excluded.
5. **The valuation lens says none of this is cheap exposure.**
   - Even for Astera, the niche's net increment is only ~3.5% of EV. For Lumentum it is ~0.6%; for TSMC, Broadcom and Marvell it is under 0.5%.
   - These stocks price whole franchises. The niches cannot explain current valuations, and they are small relative to the expectations already priced in.
6. **How we compare with consensus** (consensus as verified in a separate check):
   - **Astera:** about in line for CY2027 ($2.90B vs $2.97B) and below for CY2028 ($3.55B vs $3.83B). The reason is a Trainium3-to-4 transition gap.
   - **Lumentum:** below for FY2028 ($8.5B vs $9.6–9.9B), because InP supply caps output.
   - **Marvell:** above pre-Investor-Day consensus for FY2028 ($19.3B vs $18.2B), but below management's ~$20B.
   - **POET:** far below for CY2027 ($25M vs $64–102M, effectively one analyst).

   Full table:

| Ticker | Period | Consensus revenue | Source (date) | Confidence | Note |
|---|---|---|---|---|---|
| ALAB | CY2027 (FY = calendar year, ends Dec-2027) | $3.0B | Yahoo Finance analysis tab (24 analysts; low $2.19B, high $3.68B) [3P]. MarketScreener shows $2,973M. TIKR says 2027 consensus is up 34% since 30-Jun to ~$2.97B. (~2026-10 (the TIKR post cites the 8-Oct-2026 close; Yahoo and MarketScreener snapshot dates unverified)) | medium-high (3 aggregators agree; all post-Q2-26) | Settles the dispute in favour of $2.97B. The $1.89B VCP Scanner table is stale: TIKR's +34% since 30-Jun implies ~$2.22B even before the raise [E, arithmetic], so drop $1.89B. Also on Yahoo: CY2026 ~$1.91B. The range is wide ($2.19-3.68B, high/low 1.68x). S&P Global poll has 26 analysts vs Yahoo's 24. TIKR attribution is from the search index and the page was not opened (WebFetch blocked). Also: https://finance.yahoo.com/quote/ALAB/analysis/ and https://ca.marketscreener.com/quote/stock/ASTERA-LABS-INC-167508773/finances/ |
| ALAB | CY2028 (FY = calendar year, ends Dec-2028) | $3.8B | TIKR (same post, ~$3.83B) and MarketScreener projected income statement (~$3.83B) [3P] (~2026-10 (TIKR post cites the 8-Oct-2026 close)) | medium (2 aggregators; analyst count not shown; thinner coverage) | StocksGuide shows ~$4.1B (from the deep dive, not re-verified). TIKR flags thinner, more cautious coverage beyond 2028. Use $3.83B as central and $3.8-4.1B as the aggregator range. |
| LITE | FY2027 (FY ends ~Jun/Jul-2027; Jul-2026 to Jun-2027, ~H2-CY26 + H1-CY27) | $6.3B | Yahoo Finance analysis tab: average $6.32B, 23 analysts, range $5.61-6.95B [3P]. StockAnalysis $6.3B ($5.6-7.2B). Trefis $6.3B (8-Oct, per deep dive). (Aug-Oct 2026 (after the Q4 FY26 print on 2026-08-11; snapshot dates approximate)) | high-medium (3 sources converge at ~$6.3B) | FQ1 FY27 guide is $1.225-1.275B [G]; Chartmill FQ1 consensus is ~$1.27B. The SWS $5.56B (June) and TickFlow $5.06B figures in the deep dive are pre-guide and stale. FY26 actual was $3.014B [R]. Next print is 2026-11-05. |
| LITE | FY2028 (FY ends ~Jun/Jul-2028; Jul-2027 to Jun-2028, ~H2-CY27 + H1-CY28) | $9.6B | Yahoo Finance analysis tab: average $9.61B, 21 analysts, range $7.25-11.03B [3P]. StockAnalysis $9.84B. TIKR $9,909M. (Aug-Oct 2026 (post-Q4 FY26; snapshot dates approximate)) | medium (3 sources; $9.6-9.9B spread) | Aggregator range is $9.61-9.91B. TickFlow's $7.25B in the deep dive equals Yahoo's low estimate, not the mean. SWS $8.37B (Jun) is stale. CY2028 needs FY29 consensus, which was not found, so CY2028 is UNVERIFIED. |
| LITE | CY2027 (calendarized: ~0.5 x FY27 + 0.5 x FY28) | $8.0B | Derived [E] from Yahoo FY27 $6.32B and FY28 $9.61B. Not a published calendar consensus. (2026-10-15 (derivation)) | low-medium (derived; no clean CY consensus exists) | A simple average gives $7.97B. A ramp-weighted version (FY27 H2 ≈ $6.32B minus ~$1.25B FQ1 minus ~$1.46B FQ2 [E] = ~$3.6B, plus FY28 H1 at ~45% of $9.61B = ~$4.3B) gives ~$7.9B. Use $7.9-8.3B (TIKR FY28 basis). This sits inside the deep dive's $7.0-8.0B interpolation, at the top of it. |
| MRVL | CY2027 ≈ FY2028 (FY ends ~29-Jan-2028; Feb-2027 to Jan-2028) | $18.2B | LSEG consensus cited by Reuters (via Yahoo Finance/Qz) at the 6-Oct-2026 Investor Day [3P] (2026-10-06 (snapshot taken BEFORE the Investor Day raise)) | medium (dated broker aggregate, but stale against the new guide) | Management raised its FY28 target from ~$18B to ~$20B [G] that day. No post-event consensus revision was found. Expect drift toward $19-20B [E, unverified]. Erste Group raised FY28 EPS to $6.10 from $5.38 (2026-10-15; Defense World/MarketBeat), which signals upward revisions. Also https://www.benzinga.com/node/62198187 |
| MRVL | CY2028 ≈ FY2029 (FY ends ~Jan-2029; Feb-2028 to Jan-2029) | $24.9B | UNVERIFIED. No aggregator figure found. [E] derived by geometric interpolation between LSEG FY28 $18.2B and the Reuters-cited FY31 consensus of $46.85B (Visible Alpha, 4 analysts). (2026-10-06 (inputs); derivation 2026-10-15) | unverified | NOT a consensus print. (46.85/18.2)^(1/3) = 1.37x a year gives FY29 ≈ $24.9B [E]. The deep dive's interpolation was $25-28B [E]. A management-implied path is ~$31B [E]: custom >$12B in FY29 [G], raised from >$10B. Replace this value with a Yahoo/FactSet FY29 figure when available. |
| TSM | CY2027 (FY = calendar year) | $232.1B | StockAnalysis 'Revenue Next Year' NT$7.38T (+35.3% on NT$5.45T for 2026) [3P], converted at NT$31.8/USD (~late Jul 2026 (search index shows the page ~80 days old, i.e. after Q2-26; exact date unverified)) | medium-low (single aggregator; stale vs the Q3-26 beat and Q4 guide) | Before the 15-Oct-2026 Q3 beat (NT$1.49T vs NT$1.47T expected) and the Q4 guide of $52.3-54.3B [G], so post-Q3 revisions are likely up [E]. Cross-check: US-based sell-side USD growth of +42% (2026) and +36.9% (2027) implies ~$238B on a ~$122.4B 2025 base [E]. Source attribution for those growth rates is unverified, and the 2025 base comes from model memory, not re-verified this run. The FX assumption alone moves the figure about ±3%. |
| TSM | CY2028 (FY = calendar year) | $280.0B | UNVERIFIED. No LSEG/FactSet/aggregator 2028 figure found. Placeholder is the midpoint of the deep dive's [E] implied range of $270-290B. (2026-10-15 (placeholder)) | unverified | NOT a consensus print. StockAnalysis 2028 cells were blank. A March-2026 Google Docs initiation (no named firm) is not usable. Visible Alpha covers only 2nm revenue (2nm passes 3nm by 2028). Treat $270-290B as an [E] band and replace it once a live source is checked. |
| AVGO | CY2027 ≈ FY2027 (FY ends ~1-Nov-2027; Nov-2026 to Oct-2027, leads the calendar year by ~2 months) | $173.5B | 24/7 Wall St: analysts forecast FY27 revenue of $173.5B (+64%) and EPS $19.38 [3P; provider not named] (2026-10-02 (post-Q3 FY26 print on 2026-09-02)) | medium-high (matches deep dive's $170.7-173.9B from Barchart/Yahoo) | Aggregator range is $170.7-173.9B. Consensus sits above management's $115B FY27 AI guide plus ~$50B non-AI, i.e. it embeds an AI beat. Calendarized CY2027 ≈ $180B [E, deep dive]. Next catalyst is FQ4 FY26 around 2026-12-09 (unverified). |
| AVGO | CY2028 ≈ FY2028 (FY ends ~Oct-2028; Nov-2027 to Oct-2028) | $225.0B | UNVERIFIED revenue consensus. [E] derived from: LSEG FY28 adj. EPS consensus of $25.86 (CNBC, 2026-09-02, pre-print), EPS-implied $225-260B per the deep dive; and a Substack back-out of Street FY28 AI of ~$162B, plus ~$51B non-AI ≈ $213B. (2026-09-02 (LSEG EPS); Substack date unverified) | unverified | NOT a consensus revenue print. The derived band is $213-260B; $225B is the low end of the EPS-implied range. Management's $230B is FY28 AI-semis revenue [G], not total, though some outlets misreport it as total. vcpscanner's $133.1B and Mizuho's old $124B are single-firm and stale. Also https://www.cnbc.com/2026/09/02/broadcom-avgo-q3-earnings-report-2026.html |
| POET | CY2027 (FY = calendar year) | $84M | StocksGuide $83.6M [3P]. Other aggregators: Simply Wall St $100M (1 analyst), TickFlow $80M, StocksGuide $102M (deep dive snapshot), another ~$64M. (~Jun-Jul 2026 (aggregator snapshots ~3-4 months old; before the Q2-26 print on 2026-08-13)) | low (1-4 analysts; aggregators disagree; pre-Q2/Lumilens) | Aggregator band is $64-102M; the median is ~$84M. Effectively a single revenue analyst. Q2-26 revenue was $569,925, beating a $500K FactSet estimate (MT Newswires), so FactSet coverage exists but no 2027 figure was seen. Not refreshed for the $50M Lumilens PO. No post-Q2 consensus found. SWS: https://simplywall.st/stocks/us/semiconductors/nasdaq-poet/poet-technologies/future |
| POET | CY2028 (FY = calendar year) | $204M | StocksGuide $204M [3P]. Simply Wall St $219M (1 analyst). (~Jun-Jul 2026 (snapshots ~3-4 months old; pre-Q2-26)) | low (1 analyst; conflicts with the deep dive) | CONFLICT: the deep dive's '~$65M' 2028 consensus (source unnamed) is about 3x below the $204-219M seen here, so treat 2028 as unverified within a $65-219M band. SWS's table is internally inconsistent (2027 revenue $100M, loss -$35M, vs a 3-analyst +$15M profit). 2028 coverage has n=1. |

---

## 2. Niche by niche

### 2.1 N1: Merchant HBM4/4E logic base dies

**a. Screening table** (every company found). Ranked companies pass the hard-signal gate; "—" marks attribution-only or option exposure.

| # | Ticker | Exch. | Role | Mkt cap | EV | Base rev (TTM) | Current niche rev, CY26E (% of total) | 2030 niche rev, low / base / high | Incremental (gross) | Cannibalized by 2030 | **Net revenue leverage**, low – base – high | Profit leverage | Niche GM vs company GM | Net incr. ÷ EV | Niche-specific hard signal | Conf. | Key evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **TSM** | NYSE | direct supplier | $2143.0B | $2063.0B | $156.6B | $600M (0.4%) | $3.4B / $6.9B / $14.0B | $6.3B | $100M | 1.8% – **4.0%** – 8.4% | 3.5% | 58% vs 66% | 0.3% | Yes | medium | Customer confirmation: Micron EVP Bhatia says TSMC will make Micron's HBM4E logic base dies, both standard and custom, ramping in 2027 [G, via TrendFo |
| — | **FORM** | NASDAQ | test/inspection | $8.4B | $8.1B | $902M | $3.0M (0.3%) | $3.0M / $16M / $95M | $13M | $5.0M | -0.1% – **0.9%** – 6.9% | 1.0% | 48% vs 43% | 0.1% | **No** (attribution/option) | low | Q2-26 DRAM revenue ~$85M, about two-thirds HBM, plus two HBM4 SmartMatrix adoptions [R, 8-K 2026-07-29]. All of this is core/stack test, which is out  |
| — | **TER** | NASDAQ | test/inspection | $53.8B | $53.6B | $4.5B | $20M (0.4%) | $24M / $45M / $84M | $25M | $10M | -0.0% – **0.3%** – 1.0% | 0.3% | 58% vs 57% | 0.0% | **No** (attribution/option) | low | Magnum 7H product scope includes HBM4/4E base-die wafer test [R, BusinessWire 2025-08-04]. Q2-26 memory test revenue was a record $212M, and managemen |
| — | **ASML** | Nasdaq | equipment | $626.2B | $617.2B | $44.2B | $48M (0.1%) | $30M / $110M / $250M | $62M | $0.0M | -0.0% – **0.1%** – 0.5% | 0.1% | 52% vs 54% | 0.0% | **No** (attribution/option) | low | TSMC's 1Q26 call reportedly lists HBM base dies among N3 customers and capacity adds [analyst summary, Silicon Analysts 2026-04-16]. |
| — | **NVMI** | NASDAQ | test/inspection | $10.4B | $9.5B | $938M | $11M (1.2%) | $4.0M / $12M / $25M | $1.0M | $0.0M | -0.7% – **0.1%** – 1.5% | 0.1% | 57% vs 57% | 0.0% | **No** (attribution/option) | low | An unnamed leading foundry selected Nova WMC for multiple advanced-packaging layers; WMC is deployed at memory and foundry customers, including for HB |
| — | **KLAC** | NASDAQ | equipment | $227.8B | $228.7B | $13.6B | $42M (0.3%) | $20M / $55M / $120M | $13M | $0.0M | -0.2% – **0.1%** – 0.6% | 0.1% | 60% vs 62% | 0.0% | **No** (attribution/option) | low | SPTS plus PCB/Component Inspection guided to grow more than 25% in CY2026 on HPC packaging [G, Nasdaq/Zacks]. |
| — | **AMAT** | NASDAQ | equipment | $343.7B | $341.2B | $30.9B | $135M (0.4%) | $50M / $140M / $300M | $5.0M | $0.0M | -0.3% – **0.0%** – 0.5% | 0.0% | 48% vs 49% | 0.0% | **No** (attribution/option) | low | Advanced-packaging revenue expected to grow more than 50% in CY2026 [G, Zacks; source URL malformed, unverified]. |
| — | **MRVL** | NASDAQ | IP/EDA/design services | $202.5B | $205.5B | $9.5B | $0.0M (0.0%) | $0.0M / $0.0M / $150M | $0.0M | $0.0M | 0.0% – **0.0%** – 1.6% | 0.0% | 45% vs 59% | 0.0% | **No** (attribution/option) | low | Custom HBM compute architecture announced with Micron, Samsung and SK hynix [R, Marvell PR 2024-12-10, stale]. |
| — | **LRCX** | NASDAQ | equipment | $348.0B | $345.2B | $23.2B | $150M (0.6%) | $50M / $140M / $300M | $-10M | $0.0M | -0.4% – **-0.0%** – 0.6% | -0.0% | 50% vs 50% | -0.0% | **No** (attribution/option) | low | Advanced packaging guided to grow more than 40% in 2026, citing TSV etch and electroplating leadership for HBM4/4E [G, MarketBeat 2026-01-28]. |
| — | **ONTO** | NYSE | test/inspection | $11.3B | $10.9B | $1.1B | $18M (1.6%) | $5.0M / $15M / $35M | $-3.0M | $0.0M | -1.2% – **-0.3%** – 1.5% | -0.3% | 54% vs 50% | -0.0% | **No** (attribution/option) | low | Volume purchase agreement of more than $240M with an HBM maker for Dragonfly bump metrology through 2027 [R, 8-K 2026-02]. |
| — | **CAMT** | NASDAQ | test/inspection | $6.1B | $5.8B | $508M | $15M (3.0%) | $3.0M / $10M / $25M | $-5.0M | $0.0M | -2.4% – **-1.0%** – 2.0% | -1.0% | 51% vs 50% | -0.1% | **No** (attribution/option) | low | More than $260M of orders and forecasts from two HBM makers for 3D metrology and 2D inspection over 2026-27 [R/G, Q1-26 call]. |

*Customers, downstream system builders and adjacent products (listed so they are not mistaken for niche earners; not ranked):*

| Ticker | Category | Role in this niche | Base rev (TTM) | Niche-linked revenue, CY26E → 2030 base | Ratio if it were counted | Why it is not ranked |
|---|---|---|---|---|---|---|
| MU | customer/downstream | customer (pays, does not earn) | $133.2B | $0.0M → $0.0M | 0.0% | Pays for the niche product, or embeds it in a system it sells at system margins |
| NVDA | customer/downstream | customer (pays, does not earn) | n/a | $0.0M → $0.0M | n/a | Pays for the niche product, or embeds it in a system it sells at system margins |

**b. Dollar winners vs leverage winners.** † = no niche-specific hard signal (attribution or option only).

| Rank | Top 5 dollar winners (net incremental niche revenue, 2030 base) | Net incremental | Its leverage | Top 5 leverage winners (net revenue leverage) | Leverage | Its net incremental |
|---|---|---|---|---|---|---|
| 1 | TSM | $6.2B | 4.0% | TSM | 4.0% | $6.2B |
| 2 | ASML † | $62M | 0.1% | FORM † | 0.9% | $8.0M |
| 3 | TER † | $15M | 0.3% | TER † | 0.3% | $15M |
| 4 | KLAC † | $13M | 0.1% | ASML † | 0.1% | $62M |
| 5 | FORM † | $8.0M | 0.9% | NVMI † | 0.1% | $1.0M |

The two lists barely differ, because there is effectively one supplier. TSMC is first on both. Everyone else is a rounding error under 1%: probe cards, testers, inspection and tools are attributed slices of the niche's own spend.

**c. Deep dives: the top 3 leverage winners.** TSMC passes the gate. FormFactor and Teradyne are attribution-only, but they are the next two by leverage.

#### TSM — Taiwan Semiconductor Manufacturing Co. (N1 merchant HBM4/4E base dies; N3 non-NVLink scale-up switch silicon, as foundry)
*Net revenue leverage: 0.043 (0.018–0.096) · Gross: 0.045 · Profit leverage: 0.038 · Net incremental ÷ EV: 0.33% · Confidence: medium*

**What it sells into the niche, and why customers choose it.** In N1, TSMC is the direct supplier, with about 92% of the merchant base-die pool (range 85–100%) [E]. It sells:
- N12FFC+ base-die wafers and known-good dies for SK hynix HBM4.
- N3P C-HBM4E custom dies, with the memory controller integrated.
- Micron HBM4E base dies, from 2027.
- TSV, micro-bumping, KGD sort and NRE.

Customers choose TSMC for three reasons. It is the only qualified merchant source of logic base dies. Its die is co-optimized with CoWoS and with the host XPU that TSMC already builds. And each stack must be requalified (6–12 months), which locks sourcing for a generation.

In N3, TSMC supplies the suppliers: N5/N4/N3 wafers plus CoWoS for Astera Scorpio X, Broadcom Tomahawk Ultra/TH6 and UALink/ESUN parts. It wins whoever takes the socket.

TSMC is the largest dollar winner in N1, but the gain is small against a $156.6B base.

**Evidence of real exposure.**
- [R] Q3-26 revenue was NT$1,494.24B ($46.72B), +41.2% YoY in USD (+50.9% in NT$). GM was 66.4%, and HPC was 68% of revenue. Base-die revenue is not disclosed (TSMC 6-K, 2026-10-15).
- [R] TSMC disclosed a C-HBM4E custom base die on N3P (TrendForce, 2025-12-01).
- [G] Micron says TSMC makes its HBM4E base dies, standard and custom, ramping in 2027 (TrendForce, 2026-05). One report says "towards the end of 2027" (TechRadar, date unverified).
- [3P] SK hynix's HBM4 base die is on TSMC 12nm. Its HBM4E die is reportedly on TSMC 3nm in 2027 (Seoul Economic Daily, 2026-04-18; not re-confirmed).
- [3P] SK hynix is weighing Intel as a second source because the TSMC die costs 3–4x a core die. This is partly disputed, and nothing is signed (Herald/TrendForce, 2026-08-31).
- [3P] An analyst summary of the 1Q26 call lists HBM base dies among TSMC's N3 customer categories. It gives no wpm or dollar figure, so this is a soft signal (Silicon Analysts, 2026-04-16).
- [R] Astera's 10-K says TSMC makes all of its ICs (2026-02). This is a generic foundry relationship.
- What is missing: no segment disclosure, no 10% customer tied to the niche, and no dollar figure. Every niche number below is therefore [E].

**Revenue build.** Base revenue is TTM Q4-25 to Q3-26: $156,550M. TTM gross profit is $103,017M (65.8%) [R].

| $M | TTM actual | CY2026E | 2027E | 2028E | 2030 low / base / high |
|---|---|---|---|---|---|
| N1 base dies | 450 | 600 | 2,900 | 4,000 | 3,400 / 6,900 / 14,000 |
| N3 switch (wafer + CoWoS) | 65 | 90 | 160 | 270 | 220 / 810 / 2,130 |
| Niche revenue | 515 | 690 | 3,060 | 4,270 | 3,620 / 7,710 / 16,130 |
| Cannibalized, 2030 | – | – | – | – | 150 / 250 / 450 |

- **N1 math.**
  - CY26: about 100% × the $0.6B pool (range $0.3–1.1B).
  - 2027E: 97% × $3.0B. The range is widened to $1.7–3.2B because Micron's HBM4E may arrive late in 2027.
  - 2028E: 95% × $4.2B.
  - 2030: base 92% × $7.5B; low 85% × $4B; high 100% × $14B.
  - Probability-weighted 2030: 92% × $6.2B = $5.7B. This is lower because node substitution (standard HBM4E staying on N12) is 50–60% likely.
  - Incremental: 6,900 − 600 = 6,300.
  - Cannibalization: $100M (range 0–400), for controller/PHY logic that moves out of TSMC-made ASICs.
  - Net incremental: 6,200.
  - Revenue leverage: gross 6,300 ÷ 156,550 = 4.02%; net 3.96% (probability-weighted 3.19%).
  - Profit leverage: (6,300 × 58% − 100 × 66%) ÷ 103,017 = 3.48%.
- **N3 math.**
  - 2030 base: $8B × 11% TSMC share of ASP (range 7–16%) × 92% foundry share = $810M. At a 90% foundry share it would be about $790M.
  - Low: $3.5B × 7% × 88%. High: $14B × 16% × 95%.
  - Incremental: 720.
  - Cannibalization: $150M (range 0–400), for NVSwitch wafers TSMC loses as non-NVLink domains take share. The draft called this a "wash", which implies a loss, so it cannot be zero.
  - Net incremental: 570.
  - Revenue leverage: gross 0.46%; net 0.36%.
  - Profit leverage: 570 × 62% ÷ 103,017 = 0.34%.
- **Combined.**
  - Gross revenue leverage: 7,020 ÷ 156,550 = 4.48%.
  - Net revenue leverage: 6,770 ÷ 156,550 = **4.32%** (range 1.78–9.58%).
  - Profit leverage: (3,588 + 353) ÷ 103,017 = **3.83%**.
  - Net incremental ÷ EV: 6,770 ÷ 2,063,000 = **0.33%** (0.36% on local-market EV).
  - Not deducted: while N3 is sold out, base-die wafers displace other N3 work, so the true gain in 2026–28 is smaller.

**Our estimate vs consensus.** Fiscal year = calendar year; converted at NT$31.8/USD.

| Period | Our total revenue | Consensus | Gap | Why |
|---|---|---|---|---|
| CY2026E | $176.1B (+44%) [R/G] | NT$5.45T ≈ $171B [3P] | +3% | Consensus predates the Q3 beat and the Q4 guide |
| CY2027E | $240B ($225–255B) [E] | NT$7.38T ≈ $232B [3P, unverified]; sell-side ~$211–247B | +3.4% (−3% to +10%) | Consensus implies ~3% QoQ growth off a $53.3B Q4 exit. We use ~4.8%, plus the N2 capacity doubling and the Jan-27 price rises [3P]. The niches add <1.5 pts |
| CY2028E | $288B ($250–325B) [E] | Unverified; ~$270–290B implied [E] | −1% to +7% | N2/A16, Arizona and CoWoS, against slowing capex |

- Rest of business: $236.9B in 2027 and $283.7B in 2028.
- The niches are 0.4% of revenue in 2026, 1.3% in 2027 and 1.5% in 2028.
- Correction: the draft's 4.5% QoQ growth gives $238B for 2027, not $242B.
- Citi's "40%+ by 2027" call is ambiguous, so it is dropped.

**Valuation.**
- Price and EV: $413.26 (IBKR, 2026-10-15), down 3.9% on the print [R]. ADR-basis market cap is $2.143T. EV is about $2.06T, using cash of ~$110B [3P] and debt of ~$30B [E].
- Local listing: TWSE NT$2,440 implies an ~8% ADR premium. On local prices, market cap is ~$1.98T and EV ~$1.90T.
- Sales multiples: EV/TTM sales 13.2x; EV/NTM sales 9.0x on ~$229B; EV/CY27 sales 8.6x on our estimate, 8.9x on consensus.
- Earnings multiples: CY26 EPS from actuals plus guidance is ~$17.6–17.9 [E], so the P/E is ~23.3x; the pre-print 24.6x is stale. Our CY27 EPS of ~$23.1 gives 17.9x; Erste's $22.26 gives 18.6x.
- History and peers: trailing P/E was 34–37x in June, against a five-year average of ~23x [3P]. TSMC still trades at a ~40–50% discount to NVDA/AVGO on forward earnings [3P, stale].
- Niche value: $6.77B × ~42% net margin × 18x, discounted, is ~$35–51B, or 1.6–2.4% of market cap.
- The price already embeds ~36% growth in 2027. Base dies do not move it.

**Risks.**
- **Customer concentration.**
  - Nvidia was 19% of 2025 revenue and Apple 17% [R].
  - N1 buyers are SK hynix (~55–65%) and Micron (~25–35%) [E].
  - If SK hynix moves 15% to Intel, TSMC loses $0.6B. If Micron re-insources, it loses $1.1–2.0B. Both together leave N1 at ~$4.3B and combined net leverage at 2.7%.
  - A 20% die-price concession would cut combined net leverage to 3.4%.
- **Capacity and execution.**
  - Base dies need 10–40k wafers per month on N3, about 4–17% of TSMC's N3 capacity [E].
  - The N2 ramp cost 130bp of gross margin [R].
  - 2026 capex is $60–64B [G].
  - Customers stockpiling known-good dies could force a 30–50% correction in 2028 [E].
- **Balance sheet.** Net cash is ~$80B [E], with no dilution. The risk is overbuilding capacity.
- **Competition.**
  - Samsung's captive SF4/SF2 base dies will be 20–45% of 2030 dies.
  - Intel could take 0–15% from 2028.
  - Intel's EMIB-T packaging threatens CoWoS content [3P, unverified].
  - SMIC serves only China.
- **Technology / design change.** If standard HBM4E stays on N12, 2030 N1 revenue is ~$4–6.5B. Base dies made on DRAM processes, and SoIC or HBF substitution, could shrink it further.
- **Expectations.** The stock is up 37% YTD and 36% over 12 months, and sits 15% below its high [R]. Taiwan geopolitics, Section 232 tariffs [3P] and NT$ strength add further risk.

**Bear case.** Probability ~25–30%.
- Niche: N1 2030 = 95% × $2.3B = $2.2B, and N3 = $0.18B. Net incremental is ~$1.6B: 1.0% net leverage, 0.9% profit leverage, 0.08% of EV.
- Company: CY28 revenue of $230–245B with 56–60% gross margin gives EPS of ~$19.5–21. At 13–15x, that is $255–310 per ADR, 25–38% below today.

**Catalysts and indicators (next 2–4 quarters).**
1. SK hynix Q3-26 call: the 12nm vs 3nm base-die split and Intel's status (late Oct 2026, date unverified).
2. Samsung Q3-26: captive vs TSMC base dies (~late Oct 2026).
3. TSMC October sales and Astera Q3 (~2026-11-10).
4. Micron FQ1-27 (HBM4E timing) and Broadcom FQ4 (Dec 2026).
5. Wafer price rises take effect [3P] (2027-01-01).
6. TSMC Q4-26 results and 2027 guidance (mid-Jan 2027).
7. Nvidia GTC (Mar 2027) and TSMC's Technology Symposium (Apr–May 2027).

**Confidence and weakest assumption.** Confidence is medium. Customers confirm the exposure, but its size is our estimate [E].
- Weakest assumption: die price and node mix ($29 per die in 2026, $45 blended in 2030). If standard HBM4E stays on N12 at $15–20 per die, the 2030 niche is ~$4B. N1 net leverage then falls to (0.92 × 4.0 − 0.7) ÷ 156.55 = 1.9%.
- Next weakest: the 2027 step to $2.9B, and the 11% N3 cost share.

**Sources.**
- TSMC, "3Q26 Earnings Release (Form 6-K)", 2026-10-15. https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm
- TSMC, "2Q26 Earnings Release (Form 6-K)", 2026-07. https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000451/a2q26e_withguidancexfinal.htm
- TrendForce, "TSMC 2Q26 net income soars 77% YoY", 2026-07-16. https://www.trendforce.com/news/2026/07/16/news-tsmc-2q26-net-income-soars-77-yoy-to-nt706-56b-record-eps-nt27-25-gross-margin-beats-forecast-at-67-7/
- Investing.com, "Earnings call transcript: TSMC beats Q3 2026 estimates as stock slips", 2026-10-15. https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695
- BigGo Finance, "TSMC Q3-26 call summary", 2026-10-15. https://finance.biggo.com/news/US_TSM_2026-10-15
- MarketBeat, "TSMC Q3 earnings call highlights", 2026-10-15. https://www.marketbeat.com/instant-alerts/transcript-taiwan-semiconductor-manufacturing-q3-earnings-call-highlights-2026-10-15/
- TrendForce, "TSMC unveils custom C-HBM4E details", 2025-12-01. https://www.trendforce.com/news/2025/12/01/news-tsmc-unveils-custom-c-hbm4e-details-n3p-logic-dies-reportedly-target-2x-efficiency-gain/
- TrendForce, "Micron: TSMC to make HBM4E base dies", 2026-05. https://www.trendforce.com/news/?p=58045
- TrendForce, "SK hynix reportedly weighs Intel for HBM4E base dies amid TSMC cost pressure", 2026-08-31. https://trendforce.com/news/2026/08/31/news-sk-hynix-reportedly-weighs-intel-for-hbm4e-base-dies-amid-tsmc-cost-pressure-and-supply-diversification
- Herald Business, "SK hynix weighs Intel for HBM4E base dies", 2026-08 (date unverified). https://biz.heraldcorp.com/article/10857005
- Seoul Economic Daily, "SK hynix teams up with TSMC on HBM4E, betting on 3nm process", 2026-04-18. https://en.sedaily.com/technology/2026/04/18/sk-hynix-teams-up-with-tsmc-on-hbm4e-betting-on-3nm-process
- Silicon Analysts, "TSMC 1Q26 earnings analysis", 2026-04-16. https://siliconanalysts.com/analysis/tsmc-1q26-earnings
- TechRadar, "Micron HBM4/HBM4E roadmap", date unverified. https://www.techradar.com/pro/micron-wants-a-bigger-slice-of-the-usd100-billion-hbm-market-with-its-2026-bound-hbm4-and-hbm4e-memory-solutions
- Taiwan News, "TSMC customer concentration", 2026 (date unverified). https://www.taiwannews.com.tw/news/6310676
- Astera Labs, "Form 10-K FY2025", 2026-02. https://www.sec.gov/Archives/edgar/data/1736297/000173629726000010/alab-20251231.htm
- StockAnalysis, "TSM forecast", accessed 2026-10-15. https://stockanalysis.com/stocks/tsm/forecast/
- Admiral Markets, "TSMC earnings Q3 2026 preview", 2026-10. https://admiralmarkets.com/analytics/traders-blog/tsmc-earnings-q3-2026-preview
- GuruFocus, "Citi projects over 40% revenue growth for TSMC by 2027", 2026-10-07. https://www.gurufocus.com/news/9114529/tsm-citi-analysts-project-over-40-revenue-growth-for-tsmc-by-2027
- MarketBeat, "Erste Group forecast for TSM earnings", 2026-10-13. https://www.marketbeat.com/instant-alerts/estimates-what-is-erste-group-banks-forecast-for-tsm-fy2026-earnings-2026-10-13/
- Gigazine, "TSMC price hike", 2026-07-22. https://gigazine.net/gsc_news/en/20260722-tsmc-price-hike/
- Reuters via Yahoo Finance, "Taiwan says US has no tariff timetable", 2026-05-28. https://finance.yahoo.com/economy/policy/articles/taiwan-says-us-no-timetable-055911200.html
- TickerLeague, "TSM P/E ratio", 2026-06. https://tickerleague.com/companies/TSM/financials/pe-ratio
- Interactive Brokers, market-data snapshots (TSM, 2330 TWSE), 2026-10-15. No public URL.


---

#### FORM — FormFactor, Inc. (N1: merchant HBM4/4E logic base dies, via base-die sort probe cards)
*Net revenue leverage: 0.009 (+0.9%; central band +0.6% to +1.2%; low −0.55%, high +9.6%) · Gross: 0.014 (+1.4%) · Profit leverage: 0.010 (+1.0%) · Net incremental ÷ EV: 0.10% · Confidence: low. NO HARD SIGNAL: attribution only.*

**What it sells into the niche, and why customers choose it.** FORM's only route into N1 is MEMS probe cards for known-good-die sort of base-die wafers, at TSMC or at a pre-stack step at the memory makers. That is a slice of the niche's spend (~0.8% of die value [E]), not die revenue. Customers pick FORM for parallel contact at HBM4's 10Gbps+ I/O and fine-pitch micro-bumps [G] and for its incumbency at the HBM makers. The logic base die cuts against it: sort moves from memory-maker DRAM flows, where FORM is strong, to TSMC logic sort, where CHPT, MPI, Technoprobe and MJC compete [E].

**Evidence of real exposure.** No signal is niche-specific. FORM is ranked but flagged attribution-only; do not cite it as an N1 beneficiary.
- [R] SK hynix was 22.9% of FY25 revenue (18.9% FY24), for HBM core/stack test, out of scope (FY25 10-K, Feb-2026).
- [R] TSMC was again a 10% customer in Q2-26; product mix undisclosed (StatementDog, 29-Jul-2026).
- [R] An "HPC leader" became a 10% customer in Q1-26 via networking cards (MarketBeat, 29-Apr-2026); GPU cards ship from Q3-26 [R/G] (Investing.com, 29-Jul-2026). Named as Nvidia only by [3P] (stock3).
- [R] Q2-26 DRAM was $85M, ~two-thirds HBM (~$57M, a peak quarter), plus two HBM4 SmartMatrix adoptions: all stack/core test (8-K, 29-Jul-2026).
- [G] Micron's HBM4E base dies move to TSMC (TrendForce, May-2026), the driver of FORM's cannibalization.
- [E] No FORM mention of "base die" found in Q3-25 to Q2-26 call coverage (negative search, unverified). The draft's unsourced "1,500th HBM card" and "Nvidia consigns its own cards" are dropped, so the 45% high-case share is unverified.

**Revenue build.**
| $M | TTM actual | CY2026E | 2027E | 2028E | 2030 low / base / high |
|---|---|---|---|---|---|
| N1 niche revenue [E] | ~1 (0–3) | ~3 (2–4) | ~10 | ~11 | 3 / 16 / 95 |
| Cannibalized legacy [E] | – | – | – | – | 5 (3–10) at ~50% GM |
- Math: niche value × probe intensity × FORM share. 2030 base blends value ($7.5B × 0.8% × 30% = $18M) and wafer (384k wafers × ~$125 × 30% = $14.4M) methods: **$16M (14–18)**; the draft wrongly read the lower wafer check as confirming $18M. Low $4B × 0.5% × 15% = $3M; high $14B × 1.5% × 45% = $95M. 2027 $3.2B × 1.0% × 30% ≈ $10M; 2028 ~$4.2B × 0.85% × 30% ≈ $11M.
- CY2026E widened from $2M to $2–4M (central $3M): cards are bought ahead of the fivefold 2027 step (~$1.5B × 0.9% × 30% ≈ $4M); no decisive evidence either way.
- Cannibalization: legacy DRAM-process base-die probing at SK hynix/Micron, $5M at ~50% GM, held fixed in corners since it does not depend on FORM's TSMC share.
- Revenue leverage: gross (16 − 3) / 902.2 = **+1.44%**; net (13 − 5) / 902.2 = **+0.89%** (band +0.55% to +1.22% over 2030 $14–18M and CY26 $2–4M). High: gross 92/902.2 = +10.2%, net 87/902.2 = +9.6% (+9.1% at $10M cannibalization). Low: gross 0.0%, net −5/902.2 = −0.55% (−1.1% at $10M).
- Profit leverage: (13 × 48% − 5 × 50%) / 389.2 = 3.74 / 389.2 = **+0.96%** (+0.88% on $426M non-GAAP GP; high +10.7%, low −0.64%).
- Net incremental ÷ EV: 8 / 8,081 = **0.10%** (high 1.08%, low −0.06%).
- Not counted: base-die BIST/DFT could cut contacts in FORM's ~$200M+/yr HBM stack test; a 5% erosion (≈ −$10M) would outweigh all of N1's net. Sign uncertain, since 10Gbps+ PHYs also raise intensity.

**Our estimate vs consensus.** FY ends the last Saturday of December (≈ calendar year); FY2028 has 53 weeks.
| Period | Our total revenue | Consensus | Gap | Why |
|---|---|---|---|---|
| FY2026 | ~$1.04B [E] | No verified Street figure. H1 $484.3M [R] plus the Q3 guide of $270M ± $10M [G] implies ~$1.03–1.05B | ~0% | Q4E ~$285M |
| FY2027 | ~$1.19B ($1.10–1.30B) [E] | None verified. A third-party $990M model is described as "below consensus", so Street is likely above ~$1.0B. Inferred $1.15–1.25B [E, unverified] | +19% vs $1.0B; −5% to +3% vs the inferred range | GPU cards from Q3-26; CPO Systems from the $48.5M Q2 record; Farmers Branch |
| FY2028 | ~$1.29B ($1.05–1.45B), incl. ~$24M from the 53rd week [E] | None found | n/a | DRAM −5% (digestion); Foundry & Logic +15% |

N1 is under 1% of revenue every year and explains none of the gap. Northland's $2.70 FY26 / $2.76 FY27 EPS (MarketBeat, 05-Aug-2026) implies Q4-26 EPS of $0.46 after H1's $1.38 and the $0.86 Q3 midpoint, so it is stale and not used. Our FY27 non-GAAP EPS is ~$3.70 [E].

**Valuation.** $107.51 (IBKR, 15-Oct-2026; −10.2% alongside TER, ONTO, MU, cause unverified) × 78.1M shares [3P] = $8.40B market cap; less $345.6M cash [R], plus ~$30M debt [3P] = EV $8.08B ($8.23B diluted). EV/TTM sales 9.0x, EV/NTM ~7.0x on ~$1.15B [E], EV/FY27E 6.8x; P/E ~31x NTM (~$3.50 [E]) and ~29x FY27E. History ~3–5x EV/sales and ~20–30x P/E [E, from memory, unverified]; peers ONTO ~9.8x, NVMI ~10.1x, CAMT ~11.5x, KLIC ~4.1x EV/TTM sales (not re-verified). At a normal-cycle 5x, today's EV needs ~$1.6B of revenue, roughly the unverified 2030 Investor Day target. Average price targets are ~$127–134 [3P, MarketBeat; dates differ]. N1 is worth 0.10% of EV.

**Risks.**
- **Customer concentration.** SK hynix 22.9% of FY25 [R]; TSMC and the HPC customer each 10%+ [R]; Nvidia plus SK hynix ~40% [3P]. A 30% SK hynix cut on HBM4E stack cards (dual-sourcing TSE, Point Engineering or MJC) = −$65–75M revenue (−7–8% of TTM), ~−$35M GP (~−9%) [E]. GPU cards only entered production in Q3-26, so one miss could cost the 10% status. In N1, TSMC's sort-vendor choice decides everything.
- **Capacity and execution.** Farmers Branch online Q4-26, accretive only when fully ramped in 2028 [G]; capex $140–170M [G]. Track non-GAAP GM (41.0% → 43.9% → 49.0% → 53.3%, Q3 guide ~54%), not the 38.4% → 50.7% GAAP swing, ~10.6pp of which was GAAP-only items in Q1-26 (nature unverified).
- **Balance sheet.** Net cash ~$316M, Q2 FCF $52.6M [R]; no convertibles or ATM found.
- **Competition (incl. Asian suppliers).** CHPT and MPI (near TSMC), Technoprobe, MJC (R&D ¥6.6B → ¥8.5B [3P]), TSE, Point Engineering; MPI-v-Technoprobe patent suit (Apr-2026) [3P]; 5–10%/yr price-downs [E]; tariffs.
- **Technology / design change.** Hybrid bonding restricts probe marks; BIST and IEEE 1500/1838 cut contacts; pre-stack sort may give way to KGSD test; SoIC could fold the base die into the XPU.
- **Expectations.** +159% over 12 months, ~+93% YTD, 33% below the $160.27 June high; ~9x TTM sales; the Q3 guide sat ~10% above the pre-guide $246.2M consensus; insider selling flagged [3P].

**Bear case.** N1: $2.3B × 0.6% × 15% ≈ $2M in 2030, net incremental ≈ −$6M: net leverage −0.66%, profit −0.76%, −0.07% of EV. Company [E]: 2028 memory digestion (DRAM probe −30%), GPU share to Technoprobe/MPI and a later CPO ramp put FY27 at ~$1.02B and FY28 at ~$0.95B, GM ~47%, EPS ~$2.20: ~$48 at 22x or ~$59 at 4.5x EV/sales plus net cash, 45–55% below today.

**Catalysts and indicators (next 2–4 quarters).**
1. TSMC Q3-26 call: base-die nodes and 2027 capacity (15-Oct-2026).
2. FORM Q3-26 results and Q4 guide: GPU shipments, HBM/DDR mix, CPO, Farmers Branch, any base-die comment (28-Oct-2026) [R].
3. SK hynix Q3-26 call: HBM4E base-die node split and the Intel second source (late Oct-2026).
4. Farmers Branch coming online (Q4-26) [G]; Micron FQ1-27 on timing of HBM4E base dies at TSMC (Dec-2026).
5. FORM Q4-26 results and the FY26 10-K's 10% customer list (Feb-2027); Nvidia GTC on NVHBM timing (Mar-2027).
6. 2028 HBM pricing and hyperscaler capex guidance (2Q–3Q27).

**Confidence and weakest assumption.** Low. The weakest input is FORM's ~30% share (15–45%) of TSMC base-die sort spend times ~0.8% probe intensity (0.5–1.5%); no disclosure, named win or qualification backs either. A 2x error puts 2030 at $8–32M and net leverage at 0% to +2.7%, so the conclusion holds. On the N1 file's figures FORM trails TSM (+4.1%) and edges MRVL (+0.6%) and TER (+0.5%), inside the error band. Its real AI exposure (HBM stack test, GPU cards, CPO) lies outside N1.

**Sources.**
- FormFactor / SEC, "Q2 2026 results (8-K Ex.99.01)", 2026-07-29. https://www.sec.gov/Archives/edgar/data/0001039399/000103939926000030/ex9901-earningsreleasexq226.htm
- FormFactor / SEC, "Q1 2026 results (8-K Ex.99.01)", 2026-04-29. https://www.sec.gov/Archives/edgar/data/0001039399/000103939926000020/ex9901-earningsreleasexq126.htm
- FormFactor / SEC, "Q3 2025 results (8-K Ex.99.01)", 2025-10-29. https://www.sec.gov/Archives/edgar/data/1039399/000103939925000110/ex9901-earningsreleasexq325.htm
- FormFactor, "Reports 2025 Fourth Quarter Results", 2026-02-04. https://investors.formfactor.com/news-releases/news-release-details/formfactor-inc-reports-2025-fourth-quarter-results/
- FormFactor / SEC, "FY2025 Form 10-K", 2026-02. https://www.sec.gov/Archives/edgar/data/1039399/000103939926000009/form-20251227.htm
- FormFactor, "FormFactor to Host Upcoming Investor Day", 2026-03-05. https://investors.formfactor.com/news-releases/news-release-details/formfactor-host-upcoming-investor-day
- FormFactor via Finviz, "To announce Q3 2026 results on October 28th", 2026-10-07. https://finviz.com/news/400007/formfactor-to-announce-third-quarter-2026-financial-results-on-october-28th
- Investing.com, "FormFactor Q2 2026 earnings call transcript", 2026-07-29. https://www.investing.com/news/transcripts/earnings-call-transcript-formfactor-beats-q2-2026-estimates-shares-jump-after-hours-93CH-4821881
- MarketBeat, "FormFactor Q2 earnings call highlights", 2026-07-29. https://www.marketbeat.com/instant-alerts/formfactor-q2-earnings-call-highlights-2026-07-29/
- MarketBeat, "FormFactor Q1 2026 earnings call transcript", 2026-04-29. https://www.marketbeat.com/earnings/reports/2026-4-29-formfactor-inc-stock/
- MarketBeat, "Northland Securities estimates FormFactor Q3 earnings", 2026-08-05. https://www.marketbeat.com/instant-alerts/northland-securities-estimates-formfactor-q3-earnings-2026-08-05/
- StatementDog, "FORM Q2-26 earnings call summary", 2026-07-29. https://statementdog.com/analysis/FORM/earnings_calls/316581
- Insider Monkey, "FormFactor Q4 2025 earnings call transcript", 2026-02-04. https://www.insidermonkey.com/blog/formfactor-inc-nasdaqform-q4-2025-earnings-call-transcript-1689489/
- stock3, "Nvidia, SK hynix: 40% des Umsatzes dieser Aktie", 2026 (exact date unverified). https://stock3.com/news/nvidia-sk-hynix-40-des-umsatzes-dieser-aktie-17050837
- TrendForce, "Micron EVP: TSMC to make HBM4E logic dies", 2026-05. https://www.trendforce.com/news/?p=58045
- DigiTimes, "Micronics Japan R&D for HBM/logic probe cards", 2025-12-01. https://www.digitimes.com/news/a20251201PD210.html
- Bloomberg Law, "MPI Corp says Italian semiconductor firm infringes patents", 2026-04. https://news.bloomberglaw.com/ip-law/mpi-corp-says-italian-semiconductor-firm-infringes-patents
- AnandTech, "TSMC readies HBM4 base dies at 12nm and 5nm", 2024-05. https://ns2.anandtech.com/print/21395/tsmc-readies-hbm4-base-dies-at-12nm-and-5nm
- PitchBook, "FormFactor profile", 2026-08-04. https://pitchbook.com/profiles/company/41514-22
- vcpscanner, "FORM estimates", undated. https://www.vcpscanner.com/valuation/form/estimates
- Interactive Brokers MCP, price snapshot and company connections, 2026-10-15. (no public URL)


---

#### TER — Teradyne, Inc. (N1: merchant HBM4/4E logic base dies, via base-die wafer test)
*Net revenue leverage: 0.003 (−0.001 to 0.012) · Gross: 0.006 (0.001–0.014) · Profit leverage: 0.003 (−0.001 to 0.012) · Net incremental ÷ EV: 0.03% (−0.01 to 0.10%) · Confidence: low · NO NICHE-SPECIFIC HARD SIGNAL: attribution only*

**What it sells into the niche, and why customers choose it.** TER does not make base dies. It sells tester time on foundry-made base-die wafers, worth ~1.5% of die value [E], at one of two steps:
- pre-stack wafer test on Magnum 7H at the memory maker (TER's natural position);
- KGD sort at TSMC on UltraFLEX/UltraFLEXplus, where Advantest's V93000 leads.

Magnum 7H wins for three reasons [R]:
- one platform covers memory and at-speed logic (up to 9,216 digital pins);
- it has an installed base at "the largest HBM manufacturers";
- one flow runs from base-die wafer test to KGSD.

UltraFLEXplus UltraPort-PCIe6 targets earlier KGD insertion [R].

The problem: base dies are moving to foundry logic sort. SK hynix's HBM4 dies are on TSMC N12, and Micron's HBM4E dies go to TSMC from 2027 [G, TrendForce]. Both pull base-die test into TSMC's sort step.

Outside N1: HBM stack, DRAM, SoC and CPO test, and robotics. These make up most of the ~70% of revenue management ties to AI [G/R].

**Evidence of real exposure.**
- [R] The Magnum 7H release (Business Wire, 2025-08-04) and product page list "HBM base die wafer test" through HBM4E. This is scope, not a win, and it includes DRAM-process dies that N1 excludes.
- [R] Q2-26 call (2026-07-29): "a highlight in memory is the growth in HBM-based die test". There is no number, customer or named speaker, and it may mean die-level test.
- [R] Q2-26 memory revenue was a record $212M of $1,329M, with no base-die split. The FY25 10-K's 19%, 12% and 10% customers are unnamed.
- [3P] Advantest holds >50% of memory test; TER has ~30% of server memory test (AInvest).
- [3P] Digital Frontier and UniTest won KRW 247.8–283.9B (~$180–205M [E]) of SK hynix HBM4 wafer-tester orders in 2026 (DigiTimes; Xenospectrum/ETNews). Scope is unverified, probably core/burn-in.
- Gaps: no named order, qualification, dollar figure, 10% customer or dedicated capacity. Fourteen searches found none.

**Revenue build.**
| $M | TTM actual | CY2026E | 2027E | 2028E | 2030 low / base / high |
|---|---|---|---|---|---|
| N1 niche value (N1 file) [E] | – | 600 | 3,200 | ~4,200 | 4,000 / 7,500 / 14,000 |
| Test intensity × TER share [E] | – | ~1.5% of 2027 value × 45% | 1.6% × 40% | 1.4% × 40% | 1.5% × 40% |
| TER N1 revenue [E] | not disclosed | 20 (8–35) | 20 (10–40) | 24 (10–45) | 24 / 45 / 84 (corners 10 / 193) |
| Cannibalized legacy [E] | – | – | – | – | 10 (5–20) |
| % of TER revenue | – | ~0.4% | ~0.4% | ~0.4% | – |

- Math:
  - CY26: 1.5% × $3.2B ≈ $48M of industry tester buys, × 45% ≈ $20M.
    - The skeptic showed this is mis-keyed: CY26 uses next year's value while 2027–30 use their own, and nothing supports the implied 7–8% of 2026 value.
    - The CY26 range alone moves NET leverage from 0.000 to 0.006. Own-year keying ($5.4M) gives 0.007.
  - 2030 base: $7.5B × 1.5% × 40% = $45M. Share is cut from the mapper's 45% for three reasons: no win, Korean localization, and Micron's dies moving to TSMC.
  - Range (skeptic fix, moving only the niche value): $24M on $4.0B, $84M on $14B. The draft's corners, with all three inputs at extremes, are $10M and $193M.
  - Cannibalization ~$10M (5–20) at ~58% GM: Magnum tests of DRAM-process base dies, displaced to TSMC sort.
- Leverage:
  - Incremental = 45 − 20 = $25M. **Gross** = 25 ÷ 4,463.2 = 0.006.
  - NET incremental = $15M. **NET** = 0.003.
  - Low: (24 − 20 − 10) ÷ 4,463.2 = −0.001. High: (84 − 20 − 10) ÷ 4,463.2 = 0.012. Corners: −0.005 / 0.037.
  - Skeptic's unit cross-check (test time scales with die count): (20 + 10) × 1.85 × 40/45 ≈ $49M in 2030, NET 0.004.
- **Profit leverage** = (25 − 10) × 0.58 ÷ 2,566 = 8.7 ÷ 2,566 = 0.003.
  - TTM gross profit is unreconciled: Q2-26 alone was $794.6M at 59.8% [R].
  - At $2,650M the answer is unchanged.
- **Net incremental ÷ EV** = 15 ÷ 53,600 = 0.03%.
- TTM base: Q3-25 $769.2M + Q4-25 $1,083M (both not re-verified) + Q1-26 $1,282M + Q2-26 $1,329M [R] = $4,463.2M.

**Our estimate vs consensus.** Fiscal year = calendar year.
| Period | Our total revenue | Consensus | Gap | Why |
|---|---|---|---|---|
| FY26 | ~$5.25B (5.15–5.4) | ~$5.1–5.3B implied [E]; EPS $8.86 (MarketBeat) | −1% to +3% | Build: H1 $2,611M + Q3 $1.30B (top of guide; TER beat the top in Q1 and Q2) + Q4E $1.35B |
| FY27 | ~$5.5B (4.9–6.1); EPS ~$9.3 | EPS $11.75 (11 analysts, $9.39–13.58; Trefis 09-15), implying ~$6.1–6.3B [E] | −10% to −13%; EPS −21% | Memory flat to +10% after +40%; GM pressure from memory pricing |
| FY28 | ~$6.1B (4.9–7.2) | ~$6.9–7.0B (11 analysts); EPS ~$11.9 (TickFlow, unverified) | −12% | 2028 HBM digestion; ATE cyclicality |

- The skeptic replaced the draft's stale FY27 EPS ($9.00–9.43) with $11.75.
  - Implied revenue: 11.75 × 157.5M = $1,851M net ÷ 0.85 = $2,177M pre-tax, + $1.4–1.5B opex = $3.58–3.68B gross profit, ÷ 58.5% GM = $6.1–6.3B.
  - The gap widens from −2% to −10% to −13%.
- FY28 consensus is internally inconsistent (+1% EPS on +24% revenue). N1 explains none of any gap.

**Valuation.**
- Price $341.64 (IBKR, 2026-10-15 intraday, −4.95%). The cause is unverified, and the skeptic's re-check failed.
- Market cap ~$53.8B on ~157.5M diluted shares (Q1-26 net income ÷ EPS).
- EV ≈ $53.6B ($53.3–53.9B): market cap less $517M cash (2026-06-28 [3P]), plus $0–0.6B debt (unverified). The Technoprobe stake is not subtracted.
- EV/sales: 12.0x TTM, 10.2x CY26E, ~9.8x NTM, 9.7x our CY27 (8.6x consensus-implied).
- P/E: 38.6x the current-year $8.86; 29x CY27 consensus (37x on ours).
- History is ~20–30x forward P/E and ~4–7x EV/sales [E, unverified].
- MarketBeat's average target is $396.80 [3P], 16% above the price.
- At 10x sales, N1's $15M net increment is worth ~$0.15B, ~0.3% of EV.

**Risks.**
- **Customer concentration.**
  - The top five direct customers were 44% of FY25 revenue [R].
  - By geography, Taiwan was 36%, and China and Korea 14% each [R].
  - In N1, two memory makers and TSMC decide where sort happens.
- **Capacity and execution.**
  - Revenue grew 104% y/y in Q2-26.
  - The Q3 guide midpoint is down sequentially.
  - Memory pricing pressure on GM was flagged.
- **Balance sheet.**
  - Cash is only $517M, and debt is unverified.
  - Q2 FCF was $378M, against $89M of buybacks and dividends [3P].
  - No converts were found.
- **Competition.**
  - Advantest leads memory test and TSMC logic sort.
  - SK hynix is localizing with UniTest and Digital Frontier.
- **Technology and design change.**
  - TSMC KGD consolidation removes the Magnum step.
  - BIST/DFT cuts tester time.
  - SoIC DRAM-on-logic could absorb the base die.
  - Upside: NVHBM moves the controller into the base die.
- **Expectations.**
  - The stock is up 144% over 12 months and 30% below its $487.91 high [R, IBKR].
  - FY27 consensus EPS exceeds management's $9.50–11 target model [G].
  - Memory equities are 29–56% off their June peaks.

**Bear case.**
- N1: the $2.3B bear niche × 1.0% × 20% ≈ $5M in 2030.
  - NET incremental is −$25M, so NET leverage is −0.006.
  - That is −0.05% of EV.
- Company [E]:
  - AI capex digestion plus an HBM correction puts FY28 at ~$4.4B.
  - At 55% GM and $1.3B opex, EPS is ~$6.0.
  - At 25–30x that is $150–180, 47–56% below today.

**Catalysts and indicators (next 2–4 quarters).**
1. TSMC Q3-26 call (2026-10-15) and SK hynix Q3-26 (late Oct): base-die nodes, HBM4E 12nm vs 3nm split, tester localization.
2. TER Q3-26 (~Oct 27–29, not confirmed): memory vs $212M, any quantified base-die comment.
3. Advantest H1 FY3/27 (late Oct, unverified): HBM and SoC test share.
4. Micron FQ1-27 (Dec 2026): HBM4E on TSMC base dies.
5. TER Q4-26 (late Jan 2027) and 10-K customer list (Feb 2027).
6. Nvidia GTC (Mar 2027): NVHBM stack specs.

**Confidence and weakest assumption.**
- Confidence is low: attribution only.
- The weakest assumptions are two:
  - test intensity (~1.5%, 1.0–2.5%) × TER's ~40% share (25–55%), with the sort location unresolved;
  - the CY26 base, which alone moves NET leverage across 0.000–0.007.
- Even a 3x error (2030 at $135M) gives NET leverage of 0.024. N1 is immaterial to TER.

**Sources.**
- SEC, "Teradyne 8-K Ex.99.1, Q2-26 results", 2026-07-28. https://www.sec.gov/Archives/edgar/data/0000097210/000119312526321933/ter-ex99_1.htm
- SEC, "Teradyne 8-K Ex.99.1, Q1-26 results", 2026-04-28. https://www.sec.gov/Archives/edgar/data/0000097210/000119312526188706/ter-ex99_1.htm
- SEC, "Teradyne Form 10-K FY2025", 2026-02. https://www.sec.gov/Archives/edgar/data/97210/000119312526059002/ter-20251231.htm
- Business Wire, "Teradyne Magnum 7H release", 2025-08-04. https://www.businesswire.com/news/home/20250804458862/en
- Teradyne, "Magnum 7H product page", undated. https://www.teradyne.com/products/magnum-7h/
- Teradyne IR, "UltraFLEXplus UltraPort-PCIe6 press release", date unverified. https://investors.teradyne.com/news-events/press-releases/detail/447
- MarketBeat, "Teradyne Q2-26 earnings call transcript", 2026-07-29. https://www.marketbeat.com/earnings/reports/2026-7-29-teradyne-inc-stock/
- MarketBeat, "Teradyne Q2 earnings call highlights", 2026-07-29. https://www.marketbeat.com/instant-alerts/teradyne-q2-earnings-call-highlights-2026-07-29/
- Quartr, "Teradyne Q2 2026 event", 2026-07. https://quartr.com/events/teradyne-inc-ter-q2-2026_3sxGdnf8
- MarketBeat, "Northland Securities raises earnings estimates for Teradyne", 2026-08-03. https://www.marketbeat.com/instant-alerts/northland-securities-raises-earnings-estimates-for-teradyne-2026-08-03/
- Trefis, "Teradyne looks expensive until you price the AI chips it has not tested yet", 2026-09-15. https://www.trefis.com/stock/ter/articles/615395/teradyne-looks-expensive-until-you-price-the-ai-chips-it-has-not-tested-yet/2026-09-15
- Barchart, "What to expect from Teradyne's next quarterly earnings report", date unverified. https://www.barchart.com/story/news/3288580/what-to-expect-from-teradynes-next-quarterly-earnings-report
- TickFlow, "TER forecast", date unverified. https://tickflow.io/stock/TER/forecast
- DigiTimes, "tester" tag page, 2026-07-30. https://www.digitimes.com/tag/tester/0012941.html
- Xenospectrum, "China memory testing and HBM equipment" (citing ETNews), 2026 (date unverified). https://xenospectrum.com/en/china-memory-testing-hbm-equipment/
- AInvest, "The memory boom's real winner", 2026 (date unverified). https://www.ainvest.com/news/memory-boom-real-winner-doesn-memory-2608/
- TrendForce, "Micron HBM4E base dies at TSMC", 2026-05. https://www.trendforce.com/news/?p=58045
- Business Wire, "Teradyne Q3-2025 results date announcement", 2025-10-15. https://www.businesswire.com/news/home/20251015760992/en
- Interactive Brokers, market-data snapshot, 2026-10-15 (no public URL).
- N1 niche file: research/niche-growth-2027-2030/README.md, section 4.1 (local).


---

### 2.2 N2: Ultra-high-power InP CW lasers and ELS modules for CPO/NPO

**a. Screening table.**

| # | Ticker | Exch. | Role | Mkt cap | EV | Base rev (TTM) | Current niche rev, CY26E (% of total) | 2030 niche rev, low / base / high | Incremental (gross) | Cannibalized by 2030 | **Net revenue leverage**, low – base – high | Profit leverage | Niche GM vs company GM | Net incr. ÷ EV | Niche-specific hard signal | Conf. | Key evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **LITE** | NASDAQ | direct supplier | $77.8B | $77.2B | $3.0B | $90M (3.0%) | $350M / $875M / $1.6B | $785M | $350M | 4.0% – **14.4%** – 28.9% | 19.8% | 55% vs 46% | 0.6% | Yes | medium | The Q4 FY26 8-K cites 'increasing demand for ultra-high-power CPO lasers, an initial order for ELS modules' and says Lumentum is on track for meaningf |
| 2 | **COHR** | NYSE | direct supplier | $39.2B | $40.5B | $7.1B | $15M (0.2%) | $200M / $575M / $1.2B | $560M | $700M | -0.8% – **-2.0%** – -3.9% | 0.7% | 50% vs 38% | -0.3% | Yes | medium | The Sherman, TX 6-inch InP fab is ramping UHP CW lasers for CPO, and CPO starts contributing revenue in FQ2 FY27 (the Dec-2026 quarter) [G, Coherent Q |
| — | **POET** | NASDAQ | potential entrant | $966M | $170M | $1.7M | $0.3M (17%) | $0.0M / $7.0M / $50M | $6.7M | $0.3M | -17.4% – **3.72x** – 27.65x | 2.55x | 35% vs 50% | 3.8% | **No** (attribution/option) | low | An ELS-engine development agreement with an unnamed 'Tier 1 laser company' [Q2-26 release, 2026-08-13] and an unnamed 'significant NRE agreement for E |
| — | **AXTI** | NASDAQ | materials/consumables | $3.7B | $3.1B | $126M | $1.2M (1.0%) | $1.0M / $5.0M / $18M | $3.8M | $2.8M | -0.6% – **0.8%** – 5.4% | 1.0% | 42% vs 32% | 0.0% | **No** (attribution/option) | low | Lumentum InP capacity reservation through 2031 ($43.5M deposits) and Coherent 6-inch InP supply agreement [R, 8-Ks 2026-07]; neither names an applicat |
| — | **VECO** | NASDAQ | equipment | $2.7B | $2.5B | $683M | $6.0M (0.9%) | $3.0M / $15M / $45M | $9.0M | $8.0M | -0.7% – **0.1%** – 2.2% | 0.2% | 45% vs 39% | 0.0% | **No** (attribution/option) | low | More than $250M of Spector IBD, Lumina MOCVD and WaferEtch orders from multiple unnamed customers for InP laser manufacturing [R/G, 2026-05-26]. |
| — | **ASX** | NYSE | contract manufacturing/assembly | $91.4B | $98.5B | $22.7B | $1.0M (0.0%) | $0.0M / $25M / $80M | $24M | $0.0M | -0.0% – **0.1%** – 0.3% | 0.1% | 22% vs 19% | 0.0% | **No** (attribution/option) | low | USI's subsidiary released a UHP ELSFP series: samples 4Q25-2Q26, trial production 3Q-4Q26, mass production 1Q27 [G, secondhand Chinese press]. USI's a |
| — | **GLW** | NYSE | materials/consumables | $115.7B | $121.8B | $17.0B | $0.6M (0.0%) | $1.0M / $8.0M / $45M | $7.4M | $0.0M | 0.0% – **0.0%** – 0.3% | 0.0% | 40% vs 36% | 0.0% | **No** (attribution/option) | low | Corning positions its PM fiber and FAUs between external lasers and PICs and targets a ~$10B photonics platform by 2030 [G]. |
| — | **FN** | NYSE | contract manufacturing/assembly | $13.7B | $12.8B | $4.6B | $3.0M (0.1%) | $5.0M / $45M / $175M | $42M | $500M | -1.2% – **-9.9%** – -38.2% | -9.8% | 13% vs 12% | -3.6% | **No** (attribution/option) | low | Nvidia was 16.3% of FY26 revenue [R, 10-K]. |
| — | **AAOI** | NASDAQ | potential entrant | $6.6B | $6.3B | $596M | $1.0M (0.2%) | $0.0M / $40M / $160M | $39M | $100M | -0.2% – **-10.2%** – -40.4% | -4.4% | 55% vs 29% | -1.0% | **No** (attribution/option) | low | Launch of a 400 mW narrow-linewidth 1310 nm DFB for SiPh/CPO [R, 2025-12-18], plus 55-65% ELS gross-margin guidance as production ramps in 2027 [G, Q2 |

*Customers, downstream system builders and adjacent products (listed so they are not mistaken for niche earners; not ranked):*

| Ticker | Category | Role in this niche | Base rev (TTM) | Niche-linked revenue, CY26E → 2030 base | Ratio if it were counted | Why it is not ranked |
|---|---|---|---|---|---|---|
| NVDA | customer/downstream | customer (pays, does not earn) | n/a | $0.0M → $0.0M | n/a | Pays for the niche product, or embeds it in a system it sells at system margins |
| AVGO | customer/downstream | customer (pays, does not earn) | $89.1B | $0.0M → $0.0M | 0.0% | Pays for the niche product, or embeds it in a system it sells at system margins |
| MRVL | customer/downstream | customer (pays, does not earn) | $9.5B | $0.0M → $0.0M | 0.0% | Pays for the niche product, or embeds it in a system it sells at system margins |
| CLS | customer/downstream | customer (pays, does not earn) | $15.6B | $0.0M → $0.0M | 0.0% | Pays for the niche product, or embeds it in a system it sells at system margins |

*Two notes on cannibalization:*
- *It is attributed to the CPO transition that this niche is part of. CPO light sources and engines displace pluggable transceivers and their lasers.*
- *For contract manufacturers such as Fabrinet, CPO engine and switch assembly outside this niche may offset part of the loss. That offset is not counted here.*

**b. Dollar winners vs leverage winners.** † = no niche-specific hard signal.

| Rank | Top 5 dollar winners (net incremental niche revenue, 2030 base) | Net incremental | Its leverage | Top 5 leverage winners (net revenue leverage) | Leverage | Its net incremental |
|---|---|---|---|---|---|---|
| 1 | LITE | $435M | 14.4% | POET † | 3.72x | $6.4M |
| 2 | ASX † | $24M | 0.1% | LITE | 14.4% | $435M |
| 3 | GLW † | $7.4M | 0.0% | AXTI † | 0.8% | $1.0M |
| 4 | POET † | $6.4M | 3.72x | VECO † | 0.1% | $1.0M |
| 5 | AXTI † | $1.0M | 0.8% | ASX † | 0.1% | $24M |

**c. Deep dives.**
- Lumentum is the only gate-passing name with positive net leverage.
- POET, AXT and Veeco follow by leverage, all without a niche-specific hard signal. All three are covered because each is widely held as a "CPO play".

#### LITE — Lumentum Holdings Inc. (N2: UHP InP CW lasers + ELS modules for CPO/NPO)
*Net revenue leverage: 0.14 (0.04–0.30) · Gross: 0.26 (0.09–0.50) · Profit leverage: 0.20 (0.04–0.40; 0.22 on GAAP gross profit) · Net incremental ÷ EV: 0.56% (0.14–1.18%) · Confidence: medium*

**What it sells into the niche, and why customers choose it.** Lumentum sells ultra-high-power (200–400+ mW) 1310 nm InP CW-DFB chips. They go into the external light sources of Nvidia's Spectrum-X/Quantum-X Photonics CPO switches, where Lumentum is the leading merchant vendor. From 2H CY2027 it adds two products [G]:
- its own ELS modules, at roughly 2–2.5x the chip content;
- UHP chips for scale-up and NPO.

Customers choose it because it is the only merchant vendor with volume-qualified UHP parts and booked POs. The qualification barrier is reliability at high drive current and 55–70°C, plus low RIN and narrow linewidth, and Lumentum builds on its datacom EML franchise to clear it.

Excluded from N2 and modelled separately: OCS, pluggable EML/CW chips, Cloud Light transceivers, and in-module mid-power NPO lasers.

**Evidence of real exposure.**
- [R] The Q4 FY26 8-K quotes the CEO on "increasing demand for ultra-high-power CPO lasers, an initial order for ELS modules". The deck says UHP CPO shipments grew and the company is "on track to deliver meaningful revenue exiting CY2026" (SEC 8-K and Q4 deck, 2026-08-11).
- [G] Booked orders described on calls:
  - the "largest single purchase commitment in company history" for UHP lasers (MarketBeat, 2025-08-12);
  - a further multi-hundred-million-dollar scale-out UHP PO shipping 1H CY2027 (AOL/Motley Fool, 2026-02-03);
  - scale-up UHP volume shipments in 2H CY2027 (MarketBeat, 2026-08-11).
- [R] Nvidia invested $2B. The deal includes a multibillion purchase commitment, capacity and access rights for laser **and** optical-networking products, and a new US fab. Coherent received a matching $2B (Reuters/Yahoo; SiliconANGLE, 2026-03-02).
  - The preferred-share structure and the "nonexclusive" wording are not re-confirmed.
  - Because the commitment covers more than N2, it cannot size the niche.
- [G] InP is fully allocated, shipments run >30% short of demand, capacity is rising 40%, and the Greensboro fab qualifies in 2027 (Semiconductor Today, 2026-08-19; LetsDataScience, 2026-03).
- Gaps:
  - no CPO/UHP revenue is disclosed;
  - no PO carries a named customer or a dollar value;
  - the 10% customers (A 26.6%, B 15.0%) are unnamed.

**Revenue build.**
| $M | TTM actual (FY26) | CY2026E | 2027E | 2028E | 2030 low / base / high |
|---|---|---|---|---|---|
| Niche revenue [E] | 25 (15–40) | 90 (60–120) | 450 (300–700) | 540 (350–950) | 350 / 875 / 1,600 |
| Cannibalized legacy [E] | – | – | – | – | 150 / 350 / 700 |
| % of LITE revenue | ~1% | ~2% | ~6% | ~6% | – |

- Math, share × niche size:
  - CY26: ~47% × $0.19B = $90M.
  - CY27: 41% × $1.1B = $450M. GF Securities' $427M CPO-laser figure [3P] sits inside our range.
  - CY28: **39%** × $1.4B = $540M. The skeptic corrected the draft's 43%, which had share rising into the 2028 capacity wave.
  - 2030 base: 38% × $2.3B = $875M (about 21M emitters × ~$42). Low: 35% × $1.0B. High: ~36% × $4.5B.
  - The probability-weighted niche ($1.84B) gives about $700M.
- Cannibalization (skeptic's arithmetic fix), about **$350M** at 45% GM:
  - Pluggable lasers: 15M 1.6T-equivalents × $42.5 × 35% share = $223M.
  - Transceivers: 15M × $350 × 5.5% share = $289M.
  - Together $512M × 0.7 truly displaced = $358M, less about $25M of internal chips that would otherwise be counted twice.
- Leverage:
  - Incremental = 875 − 90 = $785M. **Gross leverage** = 785 ÷ 3,014 = 0.26.
  - NET incremental = 785 − 350 = $435M. **NET leverage** = 0.14.
  - Low: (350 − 90 − 150) ÷ 3,014 = 0.04. High: (1,600 − 90 − 600) ÷ 3,014 = 0.30. Probability-weighted: about 0.11.
- **Profit leverage** = (785 × 0.55 − 350 × 0.45) ÷ 1,386 non-GAAP TTM gross profit = 274 ÷ 1,386 = 0.20.
  - On GAAP gross profit ($1,255.9M): 0.22.
  - At a 48% niche GM: 0.16. At 58%: 0.21.
- **Net incremental ÷ EV** = 435 ÷ 77,250 = 0.56%.
- Period flag: on Nov-5, FQ1 FY27 (~$1.25B) replaces $533.8M in the TTM. The base becomes about $3,730M, so NET leverage falls to 0.12 and gross to 0.21 with no change in the business.

**Our estimate vs consensus.** The fiscal year ends on the Saturday nearest June 30, so FY27 runs Jul-2026 to Jun-2027.
| Period | Our total revenue | Consensus | Gap | Why |
|---|---|---|---|---|
| FY27 | $6.1B (5.6–6.6) | $6.3B Trefis (10/08); $5.56B SWS (Jun); $5.06B TickFlow | −3% / +10% / +21% | We cap revenue at InP supply. Figures below $5.3B predate the guide. |
| FY28 | $8.5B (6.8–9.8) | ~$9.8B Trefis-implied; $8.37B SWS; $7.25B TickFlow | −13% / +2% / +17% | Mid-range. We model capacity-gated InP, slowing transceivers and a narrow N2. |
| CY27 / CY28 | $7.3B / $9.4B | ~$7.0–8.0B CY27 [E, interpolated] | −9% to +4% | There is no clean calendar-year consensus. |
| EPS FY27 / FY28 | ~$21–22 / ~$31 | $16.10–16.67 / $23.60–26.40 (stale); TD Cowen FY28 >$30 | Above | We carry the guided ~40% operating margin. |

- CY27 build: N2 $0.45B + InP components ex-N2 $3.55B + transceivers $2.1B + OCS $0.95B + other $0.25B = $7.3B.
- Because InP is sold out, about $0.1–0.3B of CY27–28 N2 revenue may be mix shift away from EML wafers rather than additive. That is a 1–3% downside to our totals.

**Valuation.**
- Price: $850.03 (IBKR, 2026-10-15 intraday, −5.2%).
- Market cap: about $77.8B on 91.5M as-converted shares.
- EV ≈ $77.3B: market cap + ~$2.2B debt (unverified) − $2.7B cash. EV is $77–81B if the remaining converts are counted as equity.
- EV/NTM sales is 11.4x on our $6.75B; it is 12.3x on FY27 consensus and 9.1x on our FY28.
- P/E is about 40x FY27 and 27x FY28 on our EPS. On the stale consensus it is 51x and 32x.
- Before the AI cycle, LITE traded at about 2–4x EV/sales and 12–25x forward P/E [E, unverified]. COHR, at $238.50, is 46% below its high.
- The price assumes the whole AI-optics complex keeps compounding. At 10x sales, N2's net increment is worth about $4.4B, or about 6% of EV. N2 is a second-order driver of the valuation.

**Risks.**
- **Customer concentration.**
  - Customers A and B are 41.6% of revenue [R].
  - N2 is more than 80% one Nvidia program in 2026–27 [E], and Nvidia funded Coherent equally.
  - A 25–30% 2030 share instead of 38% gives NET leverage of 0.04–0.08.
  - A 30% cut in Customer A's purchases would cost about 8% of revenue.
- **Capacity and execution.**
  - If the 1H27 PO slips, CY27 N2 falls to about $250–300M.
  - ELS modules are a new manufacturing step.
  - If Greensboro qualification slips past 2027, 2028 output is capped.
- **Balance sheet.**
  - Net cash is about +$0.5B [E].
  - The Q4 FY26 convert exchanges caused a $7.76B non-cash loss and issued about 10.6M shares [R].
  - Remaining converts plus the Nvidia preferred imply 5–10% dilution.
  - Nvidia's pricing terms are not disclosed.
- **Competition.**
  - Coherent makes 400 mW parts on 6-inch InP and expects CPO revenue from Oct–Dec 2026 [G].
  - Sumitomo, Furukawa and Mitsubishi are followers; Yuanjie has 400 mW parts in validation [3P]; Broadcom may source captively.
  - Selling its own ELS modules puts LITE in channel conflict with its chip customers.
  - UHP ASPs could fall 15–25% a year from 2028 [E].
- **Technology and design change.**
  - On-PIC lasers and VLSP/comb light sources could remove the external light source.
  - 400G per lane halves the emitters needed per Tb/s.
  - NPO may use in-module mid-power lasers, which fall outside N2.
  - Scale-up may stay on copper into 2029+.
- **Expectations.**
  - The stock is up 423% in 12 months and 26% below its high.
  - The 13-week low of $594.84 shows swings of about ±50% within a quarter.
  - The Oct-12 −10% was a sector-wide sell-off (24/7 Wall St). Today's move is unexplained.

**Bear case.**
- N2: weak engine yields, copper staying in scale-up and the 2028 capacity wave cut ASPs by about 40%. N2 revenue reaches $350M in 2030, so NET leverage is 0.04 and profit leverage 0.04.
- Company: a 2028 capex slowdown and a double-order unwind take CY28 revenue to $6.0–6.5B at about a 30% operating margin, or about $16 of EPS.
- At 20–25x, that is $325–405 a share, 52–62% below today's price.
- Probability: about 25–30% [E].
- Bull case, for symmetry: if NPO tracks GF's forecast, FY28 EPS is about $38, worth about $1,140 at 30x.

**Catalysts and indicators (next 2–4 quarters).**
1. LITE FQ1 FY27 (2026-11-05): the first OCS quarter above $100M, the FQ2 guide (we model about $1.46B), any CPO dollar figure, and timing of the 1H27 PO.
2. Coherent FQ1 FY27 (Nov-2026, date unverified): whether its CPO revenue starts on time.
3. Nvidia FQ3 FY27 (late Nov-2026): Photonics switch shipment commentary.
4. LITE FQ2 FY27 (early Feb-2027): the test of "meaningful CPO revenue exiting CY2026". A warning sign is a CQ4-26 CPO run-rate below about $40M.
5. OFC 2027 (Mar-2027): NPO design wins, plus integrated-laser and VLSP demos.
6. 1H/2H CY2027: delivery on the POs and the ELS module ramp [G]; Greensboro qualification and HSR clearance for Nvidia's conversion.

**Confidence and weakest assumption.**
- Confidence is medium. The exposure is real and specific to the niche (SEC-filed product language, booked POs, customer equity, dedicated capacity), but every niche dollar is [E].
- The weakest assumptions are two:
  - that LITE holds a 38% share at about $42 per emitter through the 2028 capacity wave;
  - where the niche boundary sits. GF's NPO-laser forecast for 2028 ($2.55B [3P]) exceeds the entire 2030 N2 niche, so classification alone could move NET leverage 2–3x either way.

**Sources.**
- SEC, "Lumentum 8-K Ex.99.1, Q4/FY2026 results", 2026-08-11. https://www.sec.gov/Archives/edgar/data/0001633978/000162828026055726/lite_ex991xq4fy26.htm
- Lumentum, "Q4 FY26 Earnings Presentation", 2026-08-11. https://s21.q4cdn.com/377324469/files/doc_financials/2026/q4/Q4-FY26-Earnings-Presentation_final.pdf
- SEC, "Lumentum 8-K Ex.99.1, Q3 FY26 results", 2026-05-05. https://www.sec.gov/Archives/edgar/data/0001633978/000162828026030530/lite_ex991xq3fy26.htm
- SEC, "Lumentum Form 10-K FY2026", 2026-08. https://www.sec.gov/Archives/edgar/data/0001633978/000162828026057358/lite-20260627.htm
- Yahoo Finance/Reuters, "Nvidia to invest $2 billion each in Lumentum, Coherent", 2026-03-02. https://finance.yahoo.com/news/nvidia-invest-4-billion-photonic-131110099.html
- SiliconANGLE, "Nvidia invests $4B in co-packaged optics suppliers Lumentum, Coherent", 2026-03-02. https://siliconangle.com/2026/03/02/nvidia-invests-4b-co-packaged-optics-suppliers-lumentum-coherent/
- MarketBeat, "Lumentum Q4 earnings call highlights", 2026-08-11. https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/
- MarketBeat, "Lumentum Q3 earnings call highlights", 2026-05-05. https://www.marketbeat.com/instant-alerts/lumentum-q3-earnings-call-highlights-2026-05-05/
- AOL/Motley Fool, "Lumentum (LITE) Q2 2026 earnings call transcript", 2026-02-03. https://www.aol.com/articles/lumentum-lite-q2-2026-earnings-234107096.html
- MarketBeat, "Lumentum Q4 FY2025 earnings call transcript", 2025-08-12. https://www.marketbeat.com/earnings/reports/2025-8-12-lumentum-holdings-inc-stock
- Semiconductor Today, "Lumentum" news item, 2026-08-19. https://semiconductor-today.com/news_items/2026/aug/lumentum-190826.shtml
- LetsDataScience, "Lumentum targets $8B annual revenue run-rate", 2026-03 (date unverified). https://letsdatascience.com/news/lumentum-targets-8b-annual-revenue-runrate-55b28c7c
- TradingView/Seeking Alpha, "Lumentum's outlook brightens on Nvidia's co-packaged optics scale-out: GF", 2026 (date unverified). https://www.tradingview.com/news/seekingalpha:9a12ce4f9094b:0-lumentum-s-outlook-brightens-on-nvidia-s-co-packaged-optics-scale-out-gf/
- X, @AGTPinsights post, 2026-09-24. https://x.com/AGTPinsights/status/2105956968351543735
- Trefis, "What is the true hidden price of Lumentum stock", 2026-10-08. https://www.trefis.com/stock/lite/articles/617928/what-is-the-true-hidden-price-of-lumentum-stock/2026-10-08
- Barchart, "Analysts are upping their price targets on Lumentum stock", 2026 (date unverified). https://www.barchart.com/story/news/3875971/analysts-are-upping-their-price-targets-on-lumentum-stock-here-s-why
- Lumentum IR, "Reporting date for fiscal Q1 2027 results", 2026-10-05. https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Reporting-Date-for-Fiscal-First-Quarter-2027-Financial-Results/default.aspx
- 24/7 Wall St, "Lumentum falls 10% as optics selloff hits", 2026-10-12. https://247wallst.com/investing/2026/10/12/lumentum-falls-10-as-optics-selloff-hits-hardest-where-capacity-is-sold-out-applied-optoelectronics-drops-7-coherent-slides-7/
- Interactive Brokers, market-data snapshot, 2026-10-15 (no public URL).
- Simply Wall St and TickFlow consensus snapshots (URLs not captured in inputs).


---

#### POET — POET Technologies Inc. (N2: ultra-high-power InP CW lasers + ELS modules for CPO/NPO)
*Net revenue leverage: 3.72 (−0.35 to 28.7) · Gross: 3.90 · Profit leverage: 2.55 · Net incremental ÷ EV: 3.8% · Confidence: low. POET is an option with no current hard signal, and the ratio is driven by a $1.72M revenue base.*

**What it sells into the niche, and why customers choose it.** POET has no laser fab. It assembles bought-in InP chips (Sivers high-power DFBs, possibly an unnamed Tier-1 partner's) on its Optical Interposer: Starlight (2023, for Celestial AI), the Blazar hybrid multi-wavelength laser (OFC 2026) and a Sivers-POET ELS module. Wafer-level passive alignment promises a smaller, cheaper multi-wavelength source, an edge that matters most in optical I/O and scale-up and least in the single-wavelength ELSFP format Nvidia and Broadcom favor. **As of 2026-10-15 POET has no production N2 customer.**

**Evidence of real exposure.**
- [R] Marvell (owner of Celestial AI) cancelled every Celestial PO, including the 2023 Starlight initial-production PO, citing breach of confidentiality. Notice was received 2026-04-23 and disclosed 2026-04-27 (POET; Sherwood News). The stock fell ~47% in one session [3P, Motley Fool].
- [R] After Q2-26: an ELS-engine development agreement with an unnamed "Tier 1 laser company" and an exclusive supply deal for a Blazar power-boosting component (Q2-26 release, 2026-08-13). No counterparty, value or date; the skeptic could not independently find the Tier-1 item.
- [G] AGM, 2026-06-30: an unnamed "significant NRE agreement for ELS applications", and Blazar "deployment at scale in 2028".
- [G, stale] Sivers-POET ELS prototypes in 1H26 and production readiness by end-2026 (guided 2025-09-29). No 2026 confirmation was found.
- No ELS numeric guidance exists, and no 10%+ customer is tied to N2. The capacity and unit targets refer to optical engines.
- **Verdict:** in CY2026E, POET is an entrant/option in N2, not an exposed company.

**Revenue build.**

| $M | TTM actual | CY2026E | 2027E | 2028E | 2030 low / base / high |
|---|---|---|---|---|---|
| Niche revenue (N2) | 0.2 (0–0.6) [E] | 0.3 (0.1–1.0) [E] | 1 [E] | 3 (0.5–15) [E] | 0 / 7 / 50 [E] |

- **Base revenue: $1.72M TTM, Q3-25 to Q2-26** (range $1.68–1.76M).
  - Reported [R]: Q4-25 $0.341M, Q1-26 $0.503M and Q2-26 $0.570M.
  - Estimated [E]: Q3-25 ~$0.30M, bounded by Q2-25 ($0.268M) and Q4-25.
  - The draft's $1.83M used an estimated $0.44M for Q4-25. The niche split is all [E]; POET reports no segments.
- **Share of niche.**
  - 2028E: ~0.2% × ~$1.4B [E bridge] ≈ $3M.
  - 2030 base: 0.30% × $2.3B = $6.9M ≈ $7M. Check: 30% probability of a production ELS win by 2028 × $20M, plus 70% × $1M, gives $6.7M.
  - The draft used a 35% probability ($8M) and the skeptic 25% ($6M). Neither has decisive evidence, so I take the midpoint and carry a $6–8M band.
  - 2030 low = $0 (0% of $1.0B). 2030 high = 1.1% × $4.5B = $50M.
- **Cannibalization (skeptic correction).** CPO displaces ~20% (15–30%) of ~$1.5M of TTM pluggable-engine revenue, or $0.3M at ~50% gross margin. This is how the N2 file treats peers.
- **Revenue leverage.** Incremental = 7 − 0.3 = $6.7M. Net incremental = 6.7 − 0.3 = $6.4M.
  - Gross: 6.7 ÷ 1.72 = 3.90x.
  - Net: 6.4 ÷ 1.72 = 3.72x. Low = (0 − 0.6) ÷ 1.72 = −0.35x; high = (50 − 0.6) ÷ 1.72 = 28.7x; the $6–8M band gives 3.14–4.30x.
- **Profit leverage.** (6.7 × 35% − 0.3 × 50%) ÷ 0.86 = 2.55x.
  - TTM gross profit is unverified: 50% × $1.72M, range $0.4–1.2M, which gives 1.8–5.5x.
  - $2.2M of incremental gross profit is trivial next to $45–60M a year of opex.
- **Valuation lens.** 6.4 ÷ $170M EV = 3.8%, or 3.3–3.5% on a post-Q3 EV of $182–195M.
- **Fragility.** The ratio falls quickly as non-N2 revenue grows.
  - A $1.5M Q3-26 would lift TTM to $2.91M and cut net leverage to 2.2x.
  - Our CY2026E of $3.5M would cut it to 1.8x.
  - The #1 N2 rank (vs LITE ~0.16x [E, N2 file]) measures how small the base is, not proven exposure. Flag it.

**Our estimate vs consensus.**

| Period | Our total revenue | Consensus | Gap | Why |
|---|---|---|---|---|
| CY2026 | $3.5M (2.5–7) | ~$9M StockAlarm; $10.2M Stocksguide | −61% / −66% | H1 was $1.07M [R], so consensus needs a ~7x step-up in H2. Management calls 2H26 "substantial qualification shipments." |
| CY2027 | $25M (8–55) | ~$64M; $80M TickFlow; $102M Stocksguide | −61% to −75% | We book only ~30% of the $50M Lumilens PO in 2027. Samples arrive late 2026, and fulfillment is contingent on qualification and scale-up [R]. |
| CY2028 | $48M (12–120) | Conflicting: ~$65M (unnamed source) vs $204–219M (StocksGuide / Simply Wall St, pre-Q2-26, one analyst) | −26% to −78% | Lumilens $30M, other engines $12M, NRE $3M, N2 $3M. We converge if Lumilens reaches ~$100M a year. |

FY = calendar year (verified). "Consensus" is a single revenue analyst, and its $5.75 price target is stale: the last action was in Dec-2025, before the cancellation, the Lumilens PO and the $400M raise [3P, low reliability]. N2 is only ~4–6% of our 2027–28E revenue. The investment case is optical engines, not ELS.

**Valuation.**
- **Enterprise value.**
  - Market cap is $5.61 (IBKR, 2026-10-15) × ~172.2M shares [3P] = $966M.
  - Cash and short-term investments are $796.3M at 6/30 [R], with no debt.
  - EV is therefore ~$170M, or $182–195M after estimated Q3 burn [E].
  - Because EV is a small residual, a ±10% price move changes it by ±57%.
- **Multiples.**
  - EV/TTM sales ~99x; P/S ~560x.
  - EV/NTM sales ~12x on our numbers, vs ~4x on consensus.
  - EV/2027E 6.8x; EV/2028E 3.5x (2.6x on consensus).
- **Earnings and history.** Forward P/E is not meaningful: net losses were $11.3M in Q2-26 and $12.3M in Q1-26 [R], with no profit modeled through 2028 (LITE trades at ~25x FY28E EPS [E]). The stock is down ~40% over 12 months and ~73% from its $20.81 May-2026 high, below its 26-week low of $5.775 [R, IBKR].
- **What the price implies.** The market values the operating business at ~$170M. That is cheap if Lumilens converts, but expensive if it does not, because burn of $50–100M a year erodes the cash.
- **N2 option.** $7M × 2–4x EV/sales ÷ 1.15⁴ = $8–16M, or 4.7–9.4% of EV. The draft's $10–25M was an arithmetic error.

**Risks.**
- **Customer concentration.**
  - N2 has lost 100% of its named customers, and Marvell is publicly hostile.
  - Lumilens is ~60% of our 2027–28E revenue. A one-year slip cuts 2027E to ~$10M and 2028E to $18–25M.
- **Capacity and execution.**
  - Guidance goes from <$1M of quarterly revenue to 1M units a month by end-2027 [G].
  - Earlier guidance slipped: light-source volume in Q2-26 and Sivers prototypes in 1H26.
  - No InP fab, so POET depends on Sivers; one unverified report says new-customer intake is frozen [3P].
  - Hybrid UHP reliability qualification takes ~12–18 months [E], which leaves little slack before 2028.
- **Balance sheet.**
  - Cash is ample, but shares rose 30% in nine months, plus ~42M out-of-the-money warrants.
  - Class actions and the Night Market short report are outstanding [3P], with an estimated $10–50M of exposure [E].
- **Competition, including Asian suppliers.**
  - Integrated laser makers: Lumentum, Coherent, Sumitomo and Furukawa.
  - Module assemblers: USI/EugenLight (mass production 1Q27), TFC, Browave, Lian-Jun and InnoLight/Eoptolink.
- **Technology and design change.**
  - If ELS standardizes on single-wavelength ELSFP, value shifts to chip makers and high-volume assemblers.
  - Optical I/O may move to on-PIC heterogeneous or quantum-dot lasers (Tower/Quintessent, Scintil), comb sources or Lightmatter's VLSP.
  - If the Tier-1 partner owns the chip and the customer, POET may book only 20–40% of module value, more than halving the 2030 base.
- **Disclosure.** After the confidentiality dispute, customers will demand anonymity, so hard signals will lag real wins.
- **Expectations.** The stock is retail-heavy, with $56.2M ADV against a $966M market cap. Price targets range from $3.50 to $20.25.

**Bear case.** N2 revenue stays ~$0 through 2030. Lumilens slips to 2028 or fails, so revenue is $5–8M in 2027 and $10–15M in 2028. Burn of $70–100M a year leaves $550–620M of cash by end-2028, before $10–50M of legal costs. If equity is worth its cash, that is $3.20–3.60 a share (−36% to −43%). At 0.8x net cash it is $2.56–2.88 (−49% to −54%). N2 net leverage would be −0.35x. We put the probability that N2 never reaches production revenue by 2030 at ~40–50% [E].

**Catalysts and indicators (next 2–4 quarters).**
1. **Q3-26 results (~mid-Nov 2026 [E]).** Revenue above $1.5M would validate the ramp; below $0.8M would confirm slippage. Also watch the Sivers and Tier-1 ELS status and cash. The report resets both base revenue and EV.
2. **Lumilens engineering samples (late 2026 [G]).**
3. **Sivers-POET ELS "production readiness" (end-2026 [G]).**
4. **OFC 2027 (~Mar 2027).** Naming the Tier-1 partner or any ELS customer would be the most important N2 hard signal.
5. **FY2026 results (~Mar–Apr 2027 [E]).** Watch for 2027 guidance and capacity progress.
6. **Negative watch.** Further cancellations, an equity raise, class-action rulings, or confirmation of the customer freeze.

**Confidence and weakest assumption.** Confidence is low. The weakest assumption is that the unnamed NRE customer or the Tier-1 laser agreement becomes a production ELS win by 2028, which underpins the $3M 2028E and the $7M 2030 base. No counterparty is named, valued or dated, and the only named customer cancelled. A secondary weakness is that the TTM niche split and the gross profit cannot be verified.

**Sources.**
- POET Technologies, "Q2 2026 results" (Form 6-K Ex.99.1), 2026-08-13. https://www.sec.gov/Archives/edgar/data/0001437424/000117184326005485/exh_991.htm
- POET via Barchart, "POET Technologies Reports Second Quarter 2026 Results…", 2026-08-13. https://www.barchart.com/story/news/4207823/poet-technologies-reports-second-quarter-2026-results-revenue-up-112-year-over-year-in-sixth-consecutive-quarter-of-sequential-growth
- POET Technologies, "Reports Fourth Quarter 2025 Financial Results", ~2026-04-01. https://www.poet-technologies.com/news/poet-technologies-reports-fourth-quarter-2025-financial-results
- POET Technologies, "Provides Purchase Order Update", 2026-04-27. https://poet-technologies.com/news/poet-technologies-provides-purchase-order-update
- Sherwood News, "Marvell cancels order with POET citing breach of confidentiality", 2026-04. https://sherwood.news/markets/marvell-cancels-order-with-poet-citing-breach-of-confidentiality/
- Motley Fool, "POET Technologies stock crashed after Marvell cancellation", 2026-04-27. https://www.fool.com/investing/2026/04/27/poet-technologies-stock-crashed-after-marvell-canc/
- POET via Barchart, "Recaps Highlights of CEO's Update… 2026 AGM", 2026-06-30. https://www.barchart.com/story/news/3052173/poet-technologies-recaps-highlights-of-ceos-update-on-commercial-activities-and-provides-results-of-2026-agm
- POET Technologies, Lumilens agreement (Form 6-K), 2026-05-14. https://www.sec.gov/Archives/edgar/data/0001437424/000117184326003413/exh_991.htm
- POET Technologies, "US$400 million registered direct offering", 2026-05-15. https://poet-technologies.com/news/poet-technologies-secures-financing-of-us-400-million-in-a-registered-direct-offering-of-common-shares-and-warrant
- POET Technologies, "Collaborate with Sivers on external light sources for CPO", 2025-09-29. https://www.poet-technologies.com/news/poet-technologies-and-sivers-semiconductors-collaborate-on-external-light-sources-for-co-packaged-optics-and-next-generation-ai-market
- POET Technologies, "Demonstrate hybrid laser… at OFC", 2026-03-10. https://www.poet-technologies.com/news/poet-to-demonstrate-extraordinary-hybrid-laser-and-next-generation-high-powered-light-sources-for-ai-applications-at-ofc-conference
- StockAlarm, "POET analyst estimates", accessed 2026-10-15. https://pro.stockalarm.io/quote/POET/analysts
- TickFlow, "POET forecast", accessed 2026-10-15. https://tickflow.io/stock/POET/forecast
- Motley Fool, "Why POET Technologies stock keeps falling", 2026-05-29. https://fool.com/investing/2026/05/29/why-poet-technologies-stock-keeps-falling/
- Trading-Treff, "Auftragsstopp nach Kapazitätsgrenze" (unverified), ~2026-06/07. https://trading-treff.de/wirtschaft/poet-technologies-aktie-auftragsstopp-nach-kapazitaetsgrenze
- Interactive Brokers, market-data snapshot (contract 547618418), 2026-10-15. No public URL.


---

#### AXTI — AXT Inc (N2, supplier-tier attribution: InP substrates beneath UHP CW lasers and ELS)
*Net revenue leverage: 0.008 (−0.006 to 0.08) · Gross: 0.030 · Profit leverage: 0.010 · Net incremental ÷ EV: 0.03% · Confidence: low*

**What it sells into the niche, and why customers choose it.**

AXT sells VGF-grown InP substrates (2- to 6-inch), all made in China by Beijing Tongmei and its JVs. Ultra-high-power CW-DFB chips are grown on these wafers. Customers choose AXT for three reasons:
- It is one of three merchant suppliers at scale: AXT ~36%, Sumitomo ~42% (largely captive), JX ~13% [3P].
- It offers 6-inch wafers.
- It is adding capacity faster than its peers [G].

Caveat: the N2 definition excludes substrates and epi, so AXT's strict niche revenue is $0. Everything below is a supplier-tier attribution that already sits inside laser makers' COGS. **We recommend footnoting AXTI rather than ranking it.** On corrected numbers it would drop from #3 to #4, behind VECO (0.013), in any case.

**Evidence of real exposure.**
- [R] Q2-26 revenue was $47.6M (+164% y/y). InP was a record $30.7M, "primarily data center", with no split by application (8-K, 2026-07-30).
- [R] Lumentum capacity reservation: minimum annual InP volumes through 2031-12-31.
  - A $43.5M deposit lands in Q3-26, plus a second $43.5M in 2028.
  - AXT must refund the deposits if it fails to deliver the minimum.
  - The agreement names no application (8-K, 2026-07).
- [R] Coherent 6-inch InP development and supply agreement: 3-year term, $22.3M prepayment refundable at Coherent's option (8-K, 2026-07-02).
  - The link to N2 is only an inference. Coherent says it is ramping UHP CW lasers on 6-inch InP in Sherman, TX, with CPO revenue from Oct–Dec 2026 [G, carried from the prior report].
- [R] Nanjing Casela committed ~$25.4M for CY27. Casela makes pluggable and PON lasers, so this has no N2 link (Zacks, 2026-08).
- [G] InP capacity targets are ~$60M/quarter by YE26 and ~$130M/quarter by YE27. Backlog is >$100M (Q2 call, 2026-07-30).

These signals are real, but all of them would exist even if CPO never shipped. They track EML/DML and SiPh-CW pluggables, which make up ~95% of the InP mix.

**Revenue build.**

| $M | TTM actual | CY2026E | 2027E | 2028E | 2030 low / base / high |
|---|---|---|---|---|---|
| Niche revenue (N2 substrate) | 0.5 (0.3–1) | 1.2 (1.0–1.5) | 3.5 (3–4) | 4.5 (4–5) | 1 / 5 / 18 |
| Cannibalized legacy InP | – | – | – | – | 0.6 / 2.8 / 6.6 |
| N2 as % of AXT InP | ~0.8% | ~0.8% | ~1% | ~1% | ~0.2% / 1–1.25% / ~4% |

- **Base.** Q3-25 $28.0M + Q4-25 $23.0M + Q1-26 $26.9M + Q2-26 $47.6M = **$125.5M** [R].
  - TTM gross profit is $40.4M (32%) [R]. The Q2 margin of ~45% comes from a single secondary source.
  - TTM InP is ~$65M. Q3-25 InP of $13.1M comes from a secondary summary.
- **Industry N2 substrate spend** = emitters ÷ good dies per 3-inch-equivalent wafer × ASP × qualification overhead. AXT's share is 30–35%.
- **2030 base:** 55M ÷ 2,500 = 22k wafers × $525 × 1.4 = $16M, × 30–35% = **~$5M**.
  - The draft had $7M at $650 and 35%.
  - The $2,300 2-inch spot quote [3P, unverified] is a shortage price. A 3-inch wafer has ~2.25× the area, so the quote cannot anchor any specific ASP; we use the $400–650 midpoint.
- **2030 high:** 120M ÷ 2,500 × $700 × 1.5 × 36% = **~$18M**. The draft's $30M paired peak demand with worst-case yield; that stacked tail is still possible.
- **2030 low:** 23M ÷ 3,500 × $400 × 1.3 × 25% = **~$1M**.
- **CY26E** includes a 1–2 quarter substrate lead ahead of the 1H27 laser builds.
- **Cannibalization.** CPO receivers are Ge-on-Si, so the InP photodetectors disappear. CPO also uses ~0.5–0.7× the InP laser area per Tb/s of an EML pluggable.
  - Base: 0.5 scale-out share × 1.125 area ratio × $5M = **$2.8M**, at the same ~42% gross margin.
  - High: about one-third scale-out gives ~$6.6M. Low: ~$0.6M.
- **Base-case leverage.**
  - Incremental = 5.0 − 1.2 = $3.8M. Net = 3.8 − 2.8 = $1.0M.
  - Gross revenue leverage = 3.8 ÷ 125.5 = **0.030**. Net = 1.0 ÷ 125.5 = **0.008**.
  - Profit leverage = (3.8×0.42 − 2.8×0.42) ÷ 40.4 = **0.010**.
  - Net incremental ÷ EV = 1.0 ÷ 3,057 = **0.03%**.
- **Low and high cases.**
  - Low: net −0.76 → −0.006 (gross −0.002).
  - High: gross 16.8 → 0.13, net 10.2 → 0.08, profit 0.11, ÷ EV 0.33%.
- **TTM distortion.** The TTM base is about half the run-rate (the Q3 guide × 4 is ~$264M at ~45% gross margin). On a run-rate base, every ratio roughly halves.

**Our estimate vs consensus** (FY = calendar year).

| Period | Our total revenue | Consensus | Gap | Why |
|---|---|---|---|---|
| CY2026E | ~$215M (26.9A + 47.6A + 66 [G] + ~75) | ~$218M (TIKR-derived) | −1% | In line |
| CY2027E | $405M ($260–480M) | ~$461M (TIKR, 2026-09-30, 3–7 analysts) | −12% | We take ~85% of the InP capacity build (yield lag, permits). If the $130M/quarter target is total-company, the Street is above capacity |
| CY2028E | $515M ($300–650M) | No reliable consensus | n/a | JX and Chinese supply cut InP ASP 10–15% |
| CY27 EPS | ~$1.58 [E] | Unverified. The $1.59 figure is NTM, not CY27 | likely −15–20% | The draft's "in line" claim mixed periods |

N2 accounts for ~$3.5–4.5M a year, so it explains none of the gap.

**Valuation.**
- **Price and EV.** $57.12 (IBKR, 2026-10-15 intraday, −7.3%; $53.98 earlier in the day) × 65.4M shares [3P] = $3.74B market cap.
  - Less $748.8M of cash and investments [R], plus ~$70M of China bank loans [3P], gives **EV ≈ $3.06B**.
  - Adding noncontrolling interests and Coherent's refundable prepayment gives ~$3.1–3.2B.
- **Sales multiples.**
  - EV/TTM sales: 24.4×.
  - EV/NTM sales: 8.5× on our ~$360M, or 7.6× on the Street's ~$400M.
  - EV/CY27 sales: 6.6× on consensus, 7.5× on ours.
- **Earnings multiples.** ~36× our CY27 EPS, ~30× CY28E ($1.90).
- **History and peers.** In 2023–25 AXT traded at 1–3× EV/sales and had no meaningful P/E. LITE trades at ~23× FY28E (derived).
- **What the price implies.** AXT fills ~$130M/quarter of capacity at near-shortage pricing, with permits flowing.
- **N2's share of value.** 2030 N2 gross profit (~$2M) capitalized at 15–20× is ~$30–40M, about 1% of EV.

**Risks.**
- **Customer concentration.**
  - Lumentum and Coherent together are ~30–40% of 2027 InP [E]. The list of >10% customers is unverified.
  - If one top-2 customer dual-sources half its volume to JX in 2028, AXT loses $40–70M (8–14% of CY28E).
  - The Lumentum deposits are refundable on under-delivery, which makes them contingent debt.
- **Capacity and execution.**
  - InP must rise ~4× in 18 months. A two-quarter slip removes $60–90M from CY27.
  - Bullwhip risk: AXT sits two tiers above the ELS, and prepayments are being signed at peak shortage.
- **Balance sheet and dilution.**
  - $632.5M was raised gross at $64.25 (net unverified), and FCF is expected negative in 2026–27 [3P].
  - The Tongmei listing reportedly moved to Hong Kong (secondary source), which dilutes AXT's stake in its only operating asset.
  - Cash is concentrated in China.
- **Competition, including Asian suppliers.**
  - JX plans ¥120B for up to 10× InP capacity, explicitly targeting CPO [3P]. Sumitomo is captive.
  - Chinese substrate makers can serve domestic laser makers without permits.
  - Shortage pricing could reverse 30–50% by 2028–29, and the LTA price terms are unknown.
- **Technology and design change.**
  - The shift from EML to SiPh CW cuts InP area per Tb/s to ~1/3.
  - CPO removes InP photodetectors, so N2 is neutral-to-negative for AXT.
  - 6-inch wafers and 400 mW emitters cut wafers per Tb/s.
- **Policy, on both sides.**
  - Since 2025-02-04, all InP exports have needed a MOFCOM license. US permits were unissued as of the Apr-2026 424B5 [R], and the Q2-25 and Q4-25 shortfalls were permit-driven [R].
  - A two-quarter freeze would cost $70–150M (17–37%) of CY27.
  - The only N2-linked flow, Coherent's Sherman fab, needs the US permit.
  - US-side risks: the FCC Covered List, the Entity List and non-China sourcing mandates. All of AXT's production is in China.
- **Expectations.**
  - The stock is up +1,097% vs $4.77 a year ago yet −60% from its $143.16 high.
  - It repeatedly falls 10–12% in a day with LITE and COHR.

**Bear case** (~30% [E]).
- Permits stall for two quarters in 1H27, the ramp slips two quarters, and 2028 InP ASP falls 25%.
- Revenue: CY27 ~$260M (−44% vs consensus), CY28 ~$300M.
- EPS: ~$0.70–0.80.
- Value: **$18–25/share (−56% to −68%)**.
- N2 contributes ~$0.5–1M in this case.

Bull: permits are granted and capacity arrives on time, giving CY28 ~$650M and EPS ~$3, worth ~$90 (+58%).

**Catalysts and indicators (next 2–4 quarters).**
1. Q3-26 results (~2026-10-29, per TIKR, not company-confirmed). Watch results vs the $66M / $0.30–0.32 guide, the Q4 guide vs $77.45M, US permit status and receipt of the Lumentum deposit.
2. ~2026-11 (date unverified): China's suspension of its Oct-2025 controls lapses or is renewed. 2026-11-27: the suspension of China's US-specific Ga/Ge/Sb ban expires.
3. Nov-2026: Coherent and Lumentum FQ1 FY27 results. Watch CPO revenue start and 6-inch progress.
4. 2026-12-31: Casela's prepayment balance is due, and capacity should reach ~$60M/quarter.
5. ~Feb-2027: Q4-26 results and the 2027 capacity plan. Mar-2027: OFC.

**Confidence and weakest assumption.**

Confidence is low. The weakest number is substrate dollars per UHP emitter: die yield × ASP × overhead swings 2030 N2 from $1M to $18M, with a ~$30M tail.

The conclusion holds across that range. N2 stays at ≤~4% of AXT's InP revenue, and net leverage rounds to zero. For the stock, the weakest assumption is that MOFCOM keeps issuing non-China permits while capacity quadruples.

**Sources.**
- AXT Inc., "Q2 2026 8-K Ex.99", 2026-07-30. https://www.sec.gov/Archives/edgar/data/0001051627/000143774926025061/ex_974537.htm
- AXT Inc., "Form 8-K (Coherent 6-inch agreement)", 2026-07-02. https://www.sec.gov/Archives/edgar/data/0001051627/000143774926022557/axti20260630_8k.htm
- AXT Inc., "Form 8-K (Lumentum capacity reservation)", 2026-07. https://www.sec.gov/Archives/edgar/data/0001051627/000143774926024883/axti20260715_8k.htm
- AXT Inc., "Form 10-Q Q2 2026", 2026. https://www.sec.gov/Archives/edgar/data/0001051627/000143774926027677/axti20260630_10q.htm
- AXT Inc., "Form 424B5", 2026-04. https://www.sec.gov/Archives/edgar/data/0001051627/000121390026046176/ea0287123-424b5_axtinc.htm
- Business Wire, "AXT Q3 2025 Results", 2025-10-30. https://www.businesswire.com/news/home/20251030779326/en/axt-inc.-announces-third-quarter-2025-financial-results/
- Business Wire, "AXT Q4/FY2025 Results", 2026-02-19. https://www.businesswire.com/news/home/20260219561660/en/AXT-Inc.-Announces-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results
- Quartr, "AXT Q3 2025", 2025-10-30. https://quartr.com/events/axt-inc-axti-q3-2025_3seB4owB
- MarketBeat, "AXT Issues Q3 2026 Guidance", 2026-07-30. https://www.marketbeat.com/instant-alerts/axt-nasdaqaxti-issues-q3-2026-earnings-guidance-2026-07-30/
- MarketBeat, "AXT Q2 Earnings Call Highlights", 2026-07-30. https://www.marketbeat.com/instant-alerts/axt-q2-earnings-call-highlights-2026-07-30/
- Motley Fool, "AXT Q2 2026 Earnings Call Transcript", 2026-08. https://www.fool.com/earnings/call-transcripts/2026/08/03/axt-axti-q2-2026-earnings-call-transcript/
- Semiconductor Today, "AXT–Lumentum", 2026-07-30. https://semiconductor-today.com/news_items/2026/jul/axt-lumentum-300726.shtml
- Zacks, "AXT's InP demand is surging", 2026-08. https://www.zacks.com/stock/news/2977127/axts-inp-demand-is-surging-can-it-become-a-long-term-growth-driver
- Eastern Progress (Zacks), "AXTI Q2 earnings beat", 2026-07/08. https://www.easternprogress.com/axti-q2-earnings-beat-on-record-inp-demand-revenues-rise-y-y/article_c6eeb316-3732-56b0-9792-583786bf08e3.html
- Global Semi Research, "China's indium phosphide surge", 2026. https://globalsemiresearch.substack.com/p/chinas-indium-phosphide-surge
- TrendForce, "JX Advanced Metals to invest JPY120B in InP", 2026-06-16. https://www.trendforce.com/news/2026/06/16/news-jx-advanced-metals-to-invest-jpy-120b-through-fy2030-expand-inp-capacity-up-to-10x-as-cpo-demand-accelerates/
- TIKR, "AXT stock fell 10% in a day…", 2026-10-09. https://www.tikr.com/blog/axt-stock-fell-10-in-a-day-even-as-analysts-more-than-doubled-their-2027-revenue-estimates-heres-where-the-stock-could-go
- Motley Fool, "Coherent Q4 FY2026 Earnings Call Transcript", 2026-08. https://www.fool.com/earnings/call-transcripts/2026/08/19/coherent-cohr-q4-2026-earnings-call-transcript/
- Fastmarkets, "China suspends export prohibition…", 2025-11-09. https://fastmarkets.com/insights/china-suspends-export-prohibition-on-superhard-materials-us
- Barchart, "AXT announces closing of public offering", 2026-04-22. https://www.barchart.com/story/news/36832772/axt-announces-closing-of-public-offering-of-common-stock-and-full-exercise-of-underwriters-option-to-purchase-additional-shares
- Interactive Brokers, "MCP price snapshot AXTI", 2026-10-15. No public URL.


---

#### VECO — Veeco Instruments Inc. (N2, equipment-tier attribution: InP-laser fab tools beneath UHP CW lasers and ELS; all-stock merger into Axcelis pending)
*Net revenue leverage: 0.0015 (−0.0067 to 0.031) · Gross: 0.013 (−0.004 to 0.057) · Profit leverage: 0.0017 (−0.008 to 0.036) · Net incremental ÷ EV: 0.04% (−0.18 to 0.83%) · Confidence: low · NO NICHE-SPECIFIC HARD SIGNAL: attribution only*

**What it sells into the niche, and why customers choose it.** Three tool lines go into InP laser fabs, none of them UHP-specific:
- Spector ion-beam deposition (IBD) for facet coatings, which is most of the InP order book [R]. Low-absorption coatings matter more at 200–400 mW [E].
- Lumina+ As/P MOCVD. Management cites the largest batch and lowest cost per wafer [G], but Veeco is the challenger to Aixtron (Q2-26 orders €214.5M, ~75% opto; multiple Lumentum G10-AsP orders [R]).
- WaferEtch/WaferStorm wet processing.

The same tools serve EML and SiPh-CW pluggable lasers, which make up most of today's InP capacity additions.

**Evidence of real exposure.**
- [R] >$250M of Spector, Lumina and WaferEtch orders from multiple unnamed customers (release dated 2026-05-05; Semiconductor Today, LEDinside, Yole).
  - The release refers to "InP laser production for silicon photonics", coatings "required for high-power laser operation", and buyers that make "800G and 1.6T optical transceivers".
  - That wording describes SiPh-pluggable CW lasers (≤~150 mW). These are outside N2 but share BH-DFB lines, so the orders are adjacent, not niche-specific. CPO, NPO, ELS and UHP are not mentioned.
- [G] Q2-26 call:
  - a $700M 2030 InP-laser SAM across EML pluggables, SiPh pluggables and NPO/CPO, with no split;
  - an unnamed "global leader in optical and photonics technologies" chose Lumina+ for datacom lasers;
  - "significant backlog for 2027".
- [R/G] Compound semi was $21M in Q2-26 (11% of revenue) and is guided to roughly double in CY26. The main InP ramp is Q1-27.
- Gaps: no UHP/ELS order, qualification or customer; no 10% customer tied to N2; no InP segment. The N2 share is pure [E].

**Revenue build.**
| $M | TTM actual | CY2026E | 2027E | 2028E | 2030 low / base / high |
|---|---|---|---|---|---|
| InP-laser tool revenue [E] | not disclosed | 65 (50–90) | 180 (140–240) | 160 (110–230) | 40 / 100 / 200 |
| × N2 (UHP) share [E] | – | ~10% | ~14% | ~14% | 8% / 15% / 22% |
| N2 niche revenue [E] | ~0 | 6 (3–12) | 25 (15–45) | 22 (8–45) | 3 / 15 / 45 |
| Cannibalized legacy [E] | – | – | – | – | 1.6 / 8 / 18 |
| % of VECO revenue | – | ~0.8% | ~2.7% | ~2.2% | – |

- Math, InP-laser tool revenue × UHP share:
  - CY26: compound semi doubles to ~$110–130M (H1 ~$40M). That implies $50–90M of InP tools shipping from Q3, × ~10% = $6M. On the skeptic's $50M it is $5M, which is immaterial.
  - 2027: ~70% of the book plus follow-ons = $180M × 14% = $25M, the peak year.
  - 2028: tools for the InP capacity wave (Lumentum Greensboro, Coherent 6-inch, Furukawa, Yuanjie) = $160M × 14% = $22M.
  - 2030: the $700M SAM [G], cut to a $40–200M Veeco take, × 8–22%. Cross-check: $1–2B cumulative niche capex × 70% equipment × 20–30% in Veeco's categories × 30–40% share ≈ $10–40M a year.
- Cannibalization, **$8M** at 45% GM. The skeptic corrected the draft's $6M:
  - Pluggables use 1.4–2x more InP area and more emitters per Tb/s. So each $1 of scale-out UHP tool demand displaces *more* than $1 of pluggable-laser tool demand; the draft's 0.8x ratio ran the wrong way.
  - Net of a UHP yield penalty, the ratio is ~1.1x: 0.5 scale-out share × 1.1 × $15M ≈ $8M. Low: 0.5 × 1.1 × 3 = 1.6. High: 0.4 × 1.0 × 45 = 18.
- Leverage:
  - Incremental = 15 − 6 = $9M. **Gross** = 9 ÷ 682.7 = 0.013.
  - NET incremental = 9 − 8 = $1M. **NET** = 0.0015. Low: (3 − 6 − 1.6) ÷ 682.7 = −0.0067. High: (45 − 6 − 18) ÷ 682.7 = 0.031.
  - **Profit** = (9 × 0.45 − 8 × 0.45) ÷ 266 = 0.0017.
  - **Net incremental ÷ EV** = 1 ÷ 2,545 = 0.04%.
- TTM base = Q3-25 $165.9M (derived from FY25 $664.3M) + Q4-25 $165.0M + Q1-26 $158.3M + Q2-26 $193.5M [R] = $682.7M. Gross profit is ~$266M at 39% [E]; Q2 GAAP gross margin was 38.7% [R].
- Rank: VECO falls from #3 in the mapper (0.013, no cannibalization) to #4 in N2, below AXTI (0.008) and just above ASX (0.001).
- Post-merger, on ~$1.53B combined TTM (ACLS unverified), NET leverage is 0.0007.

**Our estimate vs consensus.** The fiscal year is the calendar year.
| Period | Our total revenue | Consensus | Gap | Why |
|---|---|---|---|---|
| CY26 | ~$795M (guide $780–810M [G]) | $776.9M Yahoo (4 analysts, mid-Sep, unverified) | +2% | Consensus is below the raised guide, so it is stale |
| CY27 | ~$940M (850–1,050) | $1.02B Yahoo; $868M Tickflow (1 analyst); ~$1.1B StocksGuide | −8% / +8% / −15% | Yahoo implies more AP or follow-on InP growth than we model [E] |
| CY28 | ~$990M (820–1,150) | None found | – | Standalone consensus lapses if the merger closes |
| EPS CY26/27/28 | $1.36–1.61 [G] / ~$2.15 / ~$2.35 | $2.11 CY27 (Tickflow) | In line | CY27 is ~$1.90–2.05 if the converts dilute |

- CY27 build: Semi $600–660M + Compound $170–250M + Storage/Scientific $80–110M.
- The skeptic flipped the sign: we are ~8% below the four-analyst mean, not above it.
- N2 is 2–3% of revenue and explains none of the gap. The InP book as a whole (~$180M) does.

**Valuation.**
- Price: $44.93 (IBKR, 2026-10-15 intraday) × 60.5M shares (unverified) = ~$2,718M market cap.
- EV ≈ $2,545M: market cap + $256.5M converts at par (unverified) − $429.4M cash and investments [R]. Net cash is ~$173M. EV is $2.51–2.76B if the converts are counted as equity.
- Multiples:
  - EV/sales is 3.73x TTM, 3.20x the CY26 guide midpoint and 2.7x our CY27.
  - P/E is ~30x the CY26 EPS guide midpoint, ~21x CY27 and ~19x CY28 (basic shares).
  - Sales multiples sit above VECO's 2019–25 range of ~1.3–3x [E, unverified].
- Deal [R]: all-stock, 0.3575 ACLS per VECO (2025-10-01). Both shareholder votes passed on 2026-02-06. China's SAMR is the last approval, and closer scrutiny has been reported [3P] (ION, Mar-2026). The companies still guide to a 2H26 close.
- The deal sets the price, but with a premium:
  - 0.3575 × ACLS $113.57 = $40.60, so VECO trades **10.7% above** deal value (8.1% at prior closes).
  - The premium opened after the May InP release and peaked at ~+20% in June [IBKR; computed].
  - Clearance alone implies ~−10% vs ACLS.
- N2's net 2030 gross profit is ~$3M. At 15–20x that is ~$50–65M, about 2% of EV.

**Risks.**
- **Customer concentration:** the InP buyers are unnamed. One pausing in 2027 would remove $30–60M (3–6% of CY27).
- **Capacity and execution:** expanding IBD capacity ~10x and AP/SiPh capacity more than 2x costs ~75bp of gross margin [G, not re-verified]. InP shipments are back-end loaded.
- **Balance sheet:** low risk. Net cash is ~$173M; the converts would cause ~6–16% dilution if converted [E].
- **Competition, including Asian suppliers:** Aixtron is the MOCVD incumbent, and AMEC and Japanese/Chinese coating vendors gain as Chinese laser fabs localize. SAMR could impose remedies.
- **Technology:** 400 mW emitters, 400G lanes and 6-inch InP all cut tools needed per Tb/s. Heterogeneous or quantum-dot lasers on SiPh bypass InP fabs. CPO cannibalizes pluggable-laser tool demand at ≥1x.
- **Expectations:** the stock is +57% over 12 months but −48% from its $86.63 June high. Sell-side is Hold, with a $40.60 average target (MarketBeat, Aug-2026). The 8–11% premium is spread risk.

**Bear case.**
- N2: the InP book is a 2026–27 pull-forward. Tool digestion in 2029–30 and Chinese localization leave 2030 N2 at ~$0–3M, so NET leverage turns negative.
- Company: CY27 ~$820M (−20% vs Yahoo) and EPS ~$1.50.
- Standalone at 17x is ≈ $25.5. On the deal path, the premium collapses and ACLS de-rates 25%, giving ≈ $30.
- **Bear value $25–31 (−31% to −43%), ~30% probability [E].**
- Bull case, for symmetry: EPS ~$2.7, worth ~$67 standalone at 25x or ~$54 via the deal at ACLS $150.

**Catalysts and indicators (next 2–4 quarters).**
1. SAMR decision. There is no date; it can come any time up to the extended outside date of 2027-06-30 (extension presumed, unverified). A close retires the ticker.
2. Veeco Q3-26, ~early Nov (date unverified). Guide: $200–220M. Compound semi must run at ~$35–45M a quarter; watch for follow-on InP orders.
3. Aixtron Q3 orders and Axcelis Q3-26: the MOCVD share read-across and deal timing.
4. Lumentum and Coherent FQ1 FY27 (Nov-2026): InP capex and the start of UHP/CPO revenue.
5. FY26 results (~Feb-2027), OFC 2027 and Q1-27 results, when the main InP ramp is guided.

**Confidence and weakest assumption.**
- Confidence is low. The InP signals are real, but they sit one supply-chain tier and one product boundary away from N2.
- The weakest assumption is the UHP share of Veeco's InP-tool demand (8–22%). Veeco's stated buyers make pluggables.
- Second is the cannibalization ratio. NET leverage is 0.013 at 0x, 0.0044 at 0.4x, 0.0015 at 1.1x and −0.003 at 1.5x.
- Third is timing: N2 tool revenue peaks in 2027–28.
- In every case N2 stays at ≤~5% of revenue (≤~3% after the merger). VECO is a merger-spread and semicap story, not an N2 vehicle.

**Sources.**
- Semiconductor Today, "Veeco InP-laser equipment orders" (Veeco release dated 2026-05-05), 2026-05-06. https://semiconductor-today.com/news_items/2026/may/veeco-060526.shtml
- LEDinside, "$250 Million+ in Equipment Orders for Manufacturing Indium Phosphide Lasers" (republished release), 2026-05-26. https://ledinside.com/news/2026/5/2026_05_26_01
- Yole Group, "Veeco announces $250 million+ in equipment orders for manufacturing indium phosphide lasers" (repost), 2026-05 (date unverified). https://yolegroup.com/industry-news/veeco-announces-250-million-in-equipment-orders-for-manufacturing-indium-phosphide-lasers/
- Laser Focus World, repost of the 2026-05-05 release (full URL not captured in inputs).
- SEC, "Veeco 8-K Ex.99.1, Q2-26 results", 2026-08-05. https://www.sec.gov/Archives/edgar/data/0000103145/000110465926091118/veco-20260805xex99d1.htm
- Barchart, "Veeco reports second quarter 2026 financial results", 2026-08 (cash and investments; via search summary). https://barchart.com/story/news/3672987/veeco-reports-second-quarter-2026-financial-results
- Quartr, "Veeco Instruments Q2 2026" event page, 2026-08. https://quartr.com/events/veeco-instruments-inc-veco-q2-2026_ofuH3zSv
- Semiconductor Today, Veeco Q2-26 results item, 2026-08-12. https://www.semiconductor-today.com/news_items/2026/aug/veeco-120826.shtml
- MarketBeat, "Veeco Instruments Q2 earnings call highlights", 2026-08-06. https://www.marketbeat.com/instant-alerts/veeco-instruments-q2-earnings-call-highlights-2026-08-06/
- Motley Fool, "Veeco (VECO) Q2 2026 earnings call transcript", 2026-08-12 (call 2026-08-05). https://www.fool.com/earnings/call-transcripts/2026/08/12/veeco-veco-q2-2026-earnings-call-transcript/
- Stock Titan, "Veeco reports fourth quarter and fiscal year 2025 financial results", 2026-02. https://www.stocktitan.net/news/VECO/veeco-reports-fourth-quarter-and-fiscal-year-2025-financial-ai8poirtut4a.html
- Stock Titan, "Veeco 10-Q, Q2-26" summary, 2026-08. https://www.stocktitan.net/sec-filings/VECO/10-q-veeco-instruments-inc-quarterly-earnings-report-e9603a2aa3e9.html
- Axcelis IR, "Axcelis Technologies and Veeco Instruments combine", 2025-10-01. https://investor.axcelis.com/news-releases/news-release-details/axcelis-technologies-and-veeco-instruments-combine-creating/
- Veeco IR, "Veeco stockholders approve merger with Axcelis", 2026-02-06. https://ir.veeco.com/news-and-events/news-details/2026/Veeco-Stockholders-Approve-Merger-with-Axcelis/default.aspx
- ION Analytics DealReporter, "Veeco/Axcelis faces closer China antitrust scrutiny amid possible complaints", 2026-03. https://ionanalytics.com/insights/dealreporter/veeco-axcelis-faces-closer-china-antitrust-scrutiny-amid-possible-complaints/
- SEC, "Axcelis 8-K Ex.99.1, Q2-26 results", 2026-08. https://www.sec.gov/Archives/edgar/data/0001113232/000110465926091697/tm2622315d1_ex99-1.htm
- Aixtron IR, "Strong momentum in optoelectronics continues", 2026-07-30. https://www.aixtron.com/en/investors/Strong%20momentum%20in%20optoelectronics%20continues_n14146
- Deutsche Boerse/Aixtron, "AIXTRON receives multiple orders for G10-AsP MOCVD systems from Lumentum", 2026-05. https://live.deutsche-boerse.com/news/AIXTRON-receives-multiple-orders-for-G10-AsP-MOCVD-Systems-from-Lumentum-to-support-expansion-of-High-Speed-Optical-Solutions-for-AI-Networks-12201f09-f0ac-4b41-b535-8991bbb0f139
- MarketBeat, "Veeco receives average recommendation of Hold from analysts", 2026-08-06. https://www.marketbeat.com/instant-alerts/veeco-instruments-inc-nasdaqveco-receives-average-recommendation-of-hold-from-analysts-2026-08-06/
- Tickflow, "VECO forecast", 2026-08-01. https://tickflow.io/stock/VECO/forecast
- Yahoo Finance, "VECO analysis" (mid-Sep-2026 snapshot via search summary, unverified). https://finance.yahoo.com/quote/VECO/analysis/
- Interactive Brokers, market-data snapshots and weekly closes, 2026-10-15 (no public URL).
- StocksGuide consensus and Zacks (via Eastern Progress) Q2 summary (URLs not captured in inputs).


---

### 2.3 N3: Merchant scale-up switch silicon (non-NVLink XPU domains)

**a. Screening table.**

| # | Ticker | Exch. | Role | Mkt cap | EV | Base rev (TTM) | Current niche rev, CY26E (% of total) | 2030 niche rev, low / base / high | Incremental (gross) | Cannibalized by 2030 | **Net revenue leverage**, low – base – high | Profit leverage | Niche GM vs company GM | Net incr. ÷ EV | Niche-specific hard signal | Conf. | Key evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ALAB** | NASDAQ | direct supplier | $49.3B | $48.0B | $1.2B | $450M (37%) | $750M / $2.2B / $4.5B | $1.8B | $100M | 22.2% – **1.41x** – 3.20x | 1.23x | 66% vs 75% | 3.5% | Yes | medium | Scorpio X, a dedicated PCIe-6 scale-up switch, is in volume production at initial customers and drives the Q3-26 guide of $540-560M (+40% QoQ) [G/R, 8 |
| 2 | **MRVL** | NASDAQ | direct supplier | $202.5B | $205.5B | $9.5B | $5.0M (0.1%) | $150M / $720M / $1.5B | $715M | $0.0M | 1.5% – **7.6%** – 15.8% | 8.0% | 62% vs 59% | 0.3% | Yes | low | Weak: ~$540M XConn acquisition for scale-up switching with ~$100M FY28 revenue guided (all uses) [G]; UALink 115T samples 2H FY27, volume FY28 [G]. No |
| 3 | **AVGO** | NASDAQ | direct supplier | $1650.0B | $1689.0B | $89.1B | $350M (0.4%) | $1.0B / $3.0B / $8.0B | $2.6B | $0.0M | 0.7% – **3.0%** – 8.6% | 3.1% | 72% vs 68% | 0.2% | Yes | medium | Named design win: the AMD Helios scale-up fabric uses 12 Broadcom TH6 per 72-GPU rack [R, ServeTheHome 2026-10]. Partner confirmation: Celestica's DS6 |
| — | **AMKR** | NASDAQ | contract manufacturing/assembly | $10.5B | $10.5B | $7.5B | $13M (0.2%) | $21M / $118M / $390M | $105M | $0.0M | 0.1% – **1.4%** – 5.1% | 1.5% | 16% vs 15% | 1.0% | **No** (attribution/option) | low | Astera's 10-K names Amkor as an assembly, packaging and test supplier [R, 2026-02]. |
| — | **ASX** | NYSE | contract manufacturing/assembly | $91.4B | $98.5B | $22.7B | $24M (0.1%) | $47M / $216M / $670M | $192M | $0.0M | 0.1% – **0.8%** – 2.8% | 1.0% | 24% vs 19% | 0.2% | **No** (attribution/option) | medium | Astera's 10-K names ASE (and Amkor) as its assembly, packaging and test suppliers [R, 2026-02]. |
| — | **TSM** | NYSE | supplier to supplier | $2143.0B | $2063.0B | $156.6B | $90M (0.1%) | $220M / $810M / $2.1B | $720M | $150M | 0.1% – **0.4%** – 1.1% | 0.3% | 62% vs 66% | 0.0% | **No** (attribution/option) | medium | Astera's 10-K: Astera is fabless and TSMC manufactures all of its ICs [R, 2026-02]. |
| — | **SNPS** | NASDAQ | IP/EDA/design services | $90.2B | $97.5B | $9.4B | $10M (0.1%) | $5.0M / $40M / $120M | $30M | $0.0M | -0.1% – **0.3%** – 1.2% | 0.3% | 80% vs 77% | 0.0% | **No** (attribution/option) | low | The UALink and Ultra Ethernet IP launch named AMD, Astera, Juniper, Tenstorrent and XConn as collaborators [R, Dec-2024, stale]. |

*Customers, downstream system builders and adjacent products (listed so they are not mistaken for niche earners; not ranked):*

| Ticker | Category | Role in this niche | Base rev (TTM) | Niche-linked revenue, CY26E → 2030 base | Ratio if it were counted | Why it is not ranked |
|---|---|---|---|---|---|---|
| CRDO | adjacent | systems | $1.6B | $300M → $750M | 28.3% | Sells a complementary product into the same racks, not the niche product |
| CLS | customer/downstream | systems | $15.6B | $200M → $2.0B | 11.5% | Pays for the niche product, or embeds it in a system it sells at system margins |
| ANET | customer/downstream | systems | $10.5B | $0.0M → $1.0B | 9.5% | Pays for the niche product, or embeds it in a system it sells at system margins |
| HPE | customer/downstream | systems | $42.3B | $20M → $450M | 1.0% | Pays for the niche product, or embeds it in a system it sells at system margins |
| AMD | customer/downstream | customer (pays, does not earn) | n/a | $0.0M → $0.0M | n/a | Pays for the niche product, or embeds it in a system it sells at system margins |
| AMZN | customer/downstream | customer (pays, does not earn) | n/a | $0.0M → $0.0M | n/a | Pays for the niche product, or embeds it in a system it sells at system margins |

**b. Dollar winners vs leverage winners.** † = no niche-specific hard signal.

| Rank | Top 5 dollar winners (net incremental niche revenue, 2030 base) | Net incremental | Its leverage | Top 5 leverage winners (net revenue leverage) | Leverage | Its net incremental |
|---|---|---|---|---|---|---|
| 1 | AVGO | $2.6B | 3.0% | ALAB | 1.41x | $1.7B |
| 2 | ALAB | $1.7B | 1.41x | MRVL | 7.6% | $715M |
| 3 | MRVL | $715M | 7.6% | AVGO | 3.0% | $2.6B |
| 4 | TSM † | $570M | 0.4% | AMKR † | 1.4% | $105M |
| 5 | ASX † | $192M | 0.8% | ASX † | 0.8% | $192M |

**c. Deep dives: the top 3 leverage winners.**

#### ALAB — Astera Labs, Inc. (N3: merchant scale-up switch silicon for non-NVLink XPU domains)
*Net revenue leverage: 1.41x (0.21–3.24x) · Gross: 1.50x · Profit leverage: 1.23x · Net incremental ÷ EV: 3.5% · Confidence: medium*

**What it sells into the niche, and why customers choose it.** Astera sells Scorpio X 320-lane PCIe-6 switches, which connect XPUs inside a scale-up domain. UALink parts follow in 2027 [G]; an Ethernet/ESUN switch exists only on the roadmap. Customers choose it for two reasons. It is the only merchant PCIe scale-up switch we know of that ships in volume [E], and Astera is the AWS incumbent. Scorpio P, Aries, Taurus and Leo are excluded.

**Evidence of real exposure.**
- [G] The Scorpio X ramp drives the Q3-26 guide of $540–560M (+40% QoQ). Scorpio becomes the largest product family in Q3. X is in volume production at its first customers (8-K Ex.99.1; Futurum, 4-Aug-2026).
- [G] X passes P in Q3. Engagements rose from ~10 to the high teens, and several design wins are expected by year-end (Yahoo Finance, Aug-2026; TIKR, Sep-2026).
- [R] Amazon warrant: 3,262,299 shares at $142.82. It vests on up to $6.5B of purchases of smart-fabric switches, signal-conditioning and optical-engine products (8-K, Feb-2026). It confirms Amazon as a switch customer. But it is a cap, not a commitment, and it also covers Scorpio P.
- [3P] Jefferies and Morgan Stanley attribute Trainium3 scale-up switching to Scorpio X; AWS has not confirmed it (TheFly; Investing.com, Dec-2025).
- [R] Q2-26 customers above 10%: A 29%, B 25%, C 15% (10-Q). These are bill-to entities with no stated link to the niche.
- Missing: no niche or Scorpio-family revenue is disclosed, and no design win is named. Every niche dollar below is [E].

**Revenue build.**
| $M | TTM actual | CY2026E | 2027E | 2028E | 2030 low / base / high |
|---|---|---|---|---|---|
| Niche revenue (Scorpio X) | ~65 (40–95) | ~450 (320–550) | ~1,000 (750–1,300) | ~1,300 (600–2,000) | 750 / 2,250 / 4,500 |
| Share of N3 | n/m | ~50% of ~$0.9B | ~48% of ~$2.1B | ~38% of ~$3.4B | 25% of ~$3B bear niche / 28% of $8B / 32% of $14B |

- **Inputs.**
  - TTM build [E]: Q3-25 $0–5M, Q4-25 $3–10M, Q1-26 $6–19M, Q2-26 $30–60M.
  - CY2026E: Q1 $12M + Q2 $45M + Q3 ~$160M + Q4 ~$225M. Guidance only forces Q3 X above ~$100–110M, which is why the low is $320M.
  - Base revenue = $230.6M + $270.6M + $308.4M + $392.4M = $1,202.0M [R].
  - TTM gross profit is ~$900M ($895–905M). It mixes GAAP and non-GAAP quarterly margins.
- **Incremental and net.**
  - Incremental = 2,250 − 450 = $1,800M.
  - Cannibalization is ~$100M ($50–150M) [E], from fewer Aries retimers in switched domains, at 77% gross margin.
  - Net incremental = $1,700M.
- **Revenue leverage.**
  - Gross = 1,800 ÷ 1,202 = 1.50x (0.25–3.37x).
  - Net = 1,700 ÷ 1,202 = 1.41x (low 250 ÷ 1,202 = 0.21x; high 3,900 ÷ 1,202 = 3.24x).
- **Profit leverage** = (1,800 × 66% − 100 × 77%) ÷ 900 = 1.23x.
  - It ranges from 1.15x to 1.31x at 62–70% gross margin. The low case gives 0.18x and the high case 2.82x.
  - The 66% is backed out of the Q3 guide: (550×72% − 392.4×73.7% − 42.6×73.7%) ÷ 115 = 65.6%.
- **Net incremental ÷ EV** = 1,700 ÷ 48,000 = 3.5% (0.5–8.1%; 3.3% on diluted EV).
- **Base share is disputed.** $2.25B stays the central case, with a base band of $2.0–2.4B, because neither side has decisive evidence.
  - The skeptic uses 25% ($2.0B; net 1.21x). The argument: Ethernet is ~half the 2030 TAM [G] and Astera ships nothing there, so 28% overall means ~50–56% of the PCIe/UALink half.
  - The niche file uses 30% ($2.4B; net 1.54x).
  - This replaces the niche file's 1.62x, which was a gross figure on a $1,190M base.
- **Denominator flag.** Net leverage is 0.89x on CY2026E revenue ($1.91B) and 0.65x on NTM revenue (~$2.6B). ALAB still ranks first in N3 even at the 0.21x low.

**Our estimate vs consensus.**
| Period | Our total revenue | Consensus | Gap | Why |
|---|---|---|---|---|
| CY2026 | ~$1.91B | ~$1.91B (TIKR) | ~0% | H1 $700.8M [R] + Q3 $550M [G] + Q4 ~$640–680M [E] |
| CY2027 | ~$2.90B ($2.5–3.3B) | ~$2.97B (Yahoo, 24 analysts; confirmed by MarketScreener and TIKR, Oct-2026) | −2% | Scorpio X ~$1.0B; rest of business +30% |
| CY2028 | ~$3.55B ($2.8–4.4B) | ~$3.83B (TIKR); ~$4.1B (StocksGuide) | −7% to −13% | Trainium3→4 air pocket; rest of business +20% |

Fiscal year equals calendar year. A separate consensus check (Oct-2026) confirmed the post-raise CY2027 figure of ~$2.97B across three aggregators [3P]; the $1.89B VCP Scanner table (1-Aug-2026) predates the raise and is stale.

**Valuation.**
- **EV.** $284.00 (IBKR, 15-Oct) × 173.49M basic shares gives a $49.3B market cap. Subtract ~$1.3B of cash and securities [R, 10-Q] and add ~$32M of leases (there is no funded debt): EV is ~$48.0B, or $51.3B diluted.
- **Sales multiples.** EV/TTM ~40x; EV/CY2026E ~25x; EV/NTM ~18x (~$2.6–2.7B); EV/CY2027 consensus ~16x (~21x on $2.3B).
- **Earnings multiples.** Forward P/E is ~48–55x on NTM non-GAAP EPS of ~$5.2–5.9 [E] (Q3 guide $1.16–1.21 [G]). On our CY2027 EPS of $6.0–6.5 [E] it is ~44–47x.
- **Against history and peers.** That is the lower half of its 52-week band: ~30–35x at the $97.89 low and ~100–110x at the $499.48 peak [E]. It is a premium to AVGO (~30–38x) and MRVL (~25–35x), and at or above CRDO (~40–55x) [E, unverified].
- **What the price implies.** The N3 net increment is only 3.5% of EV. The price therefore relies on the whole connectivity franchise compounding at more than 40% a year through 2028.

**Risks.**
- **Customer concentration.**
  - The top three bill-to customers were 69% of Q2-26 revenue [R]. AWS-linked demand is ~40–55% of revenue and ~65–80% of Scorpio X [E].
  - Losing the Trainium4/5 socket would cut 2028 revenue by $0.5–0.9B and 2030 Scorpio X by $1.2–1.6B. A 50/50 dual source would cost $0.25–0.45B in 2028.
  - Trainium demand leans on one anchor tenant (Anthropic) [3P]. Warrant contra-revenue also reduces reported revenue.
- **Capacity and execution.**
  - Foundry and OSAT capacity does not bind. Customer volume does: Trainium units are gated by N3, CoWoS and HBM.
  - Execution risks:
    - a +40% QoQ ramp of first-generation parts;
    - first-pass UALink silicon, only in labs in late 2026 [3P];
    - ABF substrate supply;
    - gross margin slipping from 73.7% to ~72%.
- **Balance sheet.**
  - Net cash is ~$1.3B, and we found no convertibles or ATM program.
  - The dilution overhang is ~6.6% (basic shares vs ~185M diluted). The Feb-2026 Amazon warrant is ~1.9% of shares (~$0.46B intrinsic).
- **Competition.**
  - NVIDIA: NVLink Fusion on hybrid Trainium4 racks [R].
  - Broadcom: Tomahawk Ultra/TH6 Ethernet scale-up, bundled with its XPUs.
  - Marvell: XConn, and UALink 115T with volume in FY28 [G].
  - Others: Upscale AI, Cornelis, and AWS in-house parts via Alchip/GUC.
  - Asian suppliers (Centec in switches, Montage in retimers) are mostly China-only. Separately, shipments to China-sited ODMs (~29% of Q1-26 per prior work; not re-verified) add tariff and export-control risk.
- **Technology and design change.**
  - The PCIe-to-UALink/ESUN move at Trainium4 makes every socket contestable.
  - Any of these would remove content: 64-card domains [3P], switching absorbed into XPU I/O chiplets, or optical switching.
  - $/Tbps falls ~25–35% per generation [E]. At a 60% niche gross margin, profit leverage drops to ~1.1x.
- **Expectations.**
  - The stock is +66.5% over 12 months, −43% from its peak, and ~18% below its $347 level on 8-Oct [3P, TIKR].
  - The Q2 beat-and-raise sold off [3P, Trefis].
  - Two 2x single-stock ETFs signal crowding.

**Bear case (~25–30%).**
- **Trigger.**
  - Hybrid Trainium4 racks run on NVLink switch trays [R].
  - Native-UALink racks are split with Marvell or in-house parts.
  - Domains shrink to 64 cards.
  - Engagements slip.
  - ODMs digest inventory.
- **Revenue.**
  - Scorpio X is ~$0.75B in 2027, ~$0.6B in 2028 and ~$0.75B in 2030.
  - The rest of the business is $1.55B in 2027 and $1.7B in 2028.
  - Total revenue is ~$2.3B in both 2027 (−23% vs consensus) and 2028 (−40%).
- **Value.**
  - CY2028 EPS is ~$3.5–4.0 at a 35% operating margin.
  - At 30–35x that gives ~$105–140; an 8x EV/sales cross-check gives ~$106. That is −51% to −63% from $284.
  - Net leverage falls to 0.21x and net incremental ÷ EV to 0.5%.

**Catalysts and indicators (next 2–4 quarters).**
1. **3-Nov-2026: Q3-26 results and Q4 guide.** A Q4 guide of $650M or more is constructive (consensus implies ~$660M); below $600M is bearish. Watch for:
   - confirmation that Scorpio is the largest family;
   - a second Scorpio X customer;
   - 10-Q customer percentages;
   - warrant contra-revenue.
2. **Q4-2026.**
   - First UALink switch silicon from Astera and Upscale [3P].
   - Aries 7 sampling [G].
   - Scorpio P at two more hyperscalers [G].
   - The Scorpio PCIe-over-optics demo at OCP, 12–15 Oct [R].
3. **Early Dec-2026: AWS re:Invent (date unverified).** Watch the Trainium4 switch architecture: the mix of native UALink vs NVLink Fusion, and the domain size.
4. **Dec-2026: Broadcom FQ4.** Tomahawk Ultra scale-up deployments.
5. **Feb-2027: Q4-26 results and 10-K.**
   - Full-year customer concentration.
   - Warrant tranches.
   - Design-win conversions.
   - The CY2027 outlook.
6. **H1-2027.**
   - Taiwan supply-chain reads on Trainium4 switch trays.
   - Marvell UALink 115T sampling [G].
   - AMD Helios volumes.

**Confidence and weakest assumption.** Confidence is medium.
- **Why the exposure is real.** Scorpio X is a dedicated product that drives a numeric guide, and Amazon is a contractual switch customer.
- **Why the size is uncertain.** Every niche dollar is [E], and Astera may never split X from P.
- **Weakest assumption.** The 2028–30 share path, falling from 38% to 28%. It needs native-UALink Trainium4/5 sockets plus 2–3 non-AWS XPU programs. If AWS's native racks go in-house or to Marvell, 2030 Scorpio X falls to $0.75–1.0B and net leverage to ~0.2–0.4x.
- **Secondary.** Post-raise consensus is unverified.

**Sources.**
- Astera Labs, "Astera Labs Reports Second Quarter 2026 Financial Results", 2026-08-04. https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-reports-second-quarter-2026-financial-results
- SEC EDGAR, Astera Labs 8-K Ex.99.1 (Q2-26), 2026-08-04. https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000033/q226exhibit991.htm
- SEC EDGAR, Astera Labs 8-K Ex.99.1 (Q4/FY2025), 2026-02-10. https://www.sec.gov/Archives/edgar/data/1736297/000173629726000005/q425exhibit991.htm
- SEC EDGAR, Astera Labs Form 10-Q (Q2-26), 2026-08. https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000035/alab-20260630.htm
- SEC EDGAR, Astera Labs Form 8-K (Amazon warrant), 2026-02. https://www.sec.gov/Archives/edgar/data/1736297/000110465926012606/tm265461d1_8k.htm
- Futurum Group, "Astera Labs Q2 FY 2026 Earnings Pull Scorpio Switch Leadership Forward", 2026-08-04. https://futurumgroup.com/insights/astera-labs-q2-fy-2026-earnings-pull-scorpio-switch-leadership-forward/
- Yahoo Finance, ALAB Q2-2026 earnings call highlights, 2026-08. https://finance.yahoo.com/markets/stocks/articles/astera-labs-inc-alab-q2-050348738.html
- TIKR, "Astera Labs' Scorpio X Is Already in Volume Production. Citi Showed How Fast the Customer List Is Growing", 2026-09. https://www.tikr.com/blog/astera-labs-scorpio-x-is-already-in-volume-production-citi-showed-how-fast-the-customer-list-is-growing
- NVIDIA Developer Blog, "AWS Integrates AI Infrastructure with NVIDIA NVLink Fusion for Trainium4 Deployment", 2025-12. https://developer.nvidia.com/blog/aws-integrates-ai-infrastructure-with-nvidia-nvlink-fusion-for-trainium4-deployment/
- Investing.com, "Amazon adopts NVLink Fusion for Trainium4, Astera Labs stock unfairly hit", 2025-12. https://www.investing.com/news/analyst-ratings/amazon-adopts-nvlink-fusion-for-trainium4-astera-labs-stock-unfairly-hit-93CH-4387782
- TipRanks/TheFly, "NVLink/Trainium4 re:Invent mention not negative for Astera Labs, says Jefferies", 2025-12. https://www.tipranks.com/news/the-fly/nvlink-trainium4-reinvent-mention-not-negative-for-astera-labs-says-jefferies-thefly
- Finviz (company PR), "Astera Labs Announces Conference Call to Review Third Quarter 2026 Financial Results", 2026-10-06. https://finviz.com/news/399499/astera-labs-announces-conference-call-to-review-third-quarter-2026-financial-results
- Yahoo Finance, ALAB analysis (consensus), accessed 2026-10. https://finance.yahoo.com/quote/ALAB/analysis/
- VCP Scanner, ALAB estimates, 2026-08-01 (page attribution unverified). https://www.vcpscanner.com/valuation/alab/estimates
- HPCwire, first UALink products, 2026-09. https://www.hpcwire.com/?p=197496
- Lumentum, "Lumentum, Astera Labs and Corning to Demonstrate 1060 nm VCSEL-Based PCIe-over-Optics for AI Rack-Scale Connectivity at the 2026 OCP Global Summit", 2026-10. https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Astera-Labs-and-Corning-to-Demonstrate-1060-nm-VCSEL-Based-PCIe-over-Optics-for-AI-Rack-Scale-Connectivity-at-the-2026-OCP-Global-Summit/default.aspx
- Trefis, "Astera Labs Beat and Guided Higher, Then Fell Because the Rally Came First", 2026-08-06. https://www.trefis.com/stock/alab/articles/610418/astera-labs-beat-and-guided-higher-then-fell-because-the-rally-came-first/2026-08-06
- Interactive Brokers, ALAB price snapshot (contract 692196414), 2026-10-15. No public URL.


---

#### MRVL — Marvell Technology, Inc. (N3 merchant scale-up switch; N1 custom HBM base die, unconfirmed; N2 customer only)
*Net revenue leverage: 0.076 (0.015–0.174) · Gross: 0.076 · Profit leverage: 0.080 (0.016–0.178; 0.092 on GAAP gross profit) · Net incremental ÷ EV: 0.35% (0.07–0.80%) · Confidence: low*

**What it sells into the niche, and why customers choose it.** In N3, Marvell is the third merchant source, behind Broadcom (Ethernet scale-up) and Astera (PCIe/UALink). It sells three things:
- XConn-derived PCIe/CXL switches (Structera S; launch date unverified).
- UALink 115T/57T switches that sample in 2H FY27.
- Teralynx-lineage Ethernet for ESUN.

Customers would pick it as a protocol-neutral second source that is already inside their custom-XPU programs (Trainium, Maia), so the switch and the XPU can be co-designed. In N1 it offers custom-HBM base-die design and IP, but no program has been named. In N2 it is a buyer of external laser sources for Celestial AI's Photonic Fabric and its own light engines; it sells no lasers.

**Evidence of real exposure.**
- [G] UALink 115T/57T samples in 2H FY27 (Aug-2026 to Jan-2027), with volume in FY28. Marvell is working with customers on ESUN (MarketBeat, Q4 FY26 call, 2026-03-05).
- [R/G] XConn (~$540M) closed Feb-2026. First revenue comes in Q3 FY27, a ~$50M annualized rate by Q4 FY27 and ~$100M in FY28 across all uses. Most of that is CXL/PCIe fan-out rather than XPU fabric (Marvell, 2026-01-06).
- [R] Marvell is an ESUN founding member (Converge Digest, 2025-10, stale).
- [R] The OCP-2026 demo list (Teralynx T100, Structera CXL, Ara, COLORZ) includes no UALink switch (Marvell, 2026-10-08).
- [G] At Investor Day Marvell said it supports NVLink, UALink and Ethernet scale-up, but gave no scale-up switch revenue figure (StockAnalysis transcript, 2026-10-06).
- [R] NVDA's $2B convertible preferred came with an NVLink Fusion supply deal. That steers Marvell's scale-up content toward NVLink, which is outside N3 (DCD, 2026-03-31).
- [R, stale] Marvell announced a custom HBM architecture with Micron, Samsung and SK hynix (Marvell, 2024-12-10). No customer has been named in the 22 months since.
- Missing: a named N3 socket or qualification, a segment disclosure, and a 10%+ customer tied to the niche. The exposure is real at the product level but unconfirmed at the revenue level.

**Revenue build.**
| $M | TTM actual | CY2026E | 2027E | 2028E | 2030 low / base / high |
|---|---|---|---|---|---|
| N3 scale-up switch | 0 (0–2) | 5 (2–12) | 50 (15–150) | 170 (50–500) | 150 / 720 / 1,500 |
| N1 HBM base die (option) | 0 | 0 | 0 | 0 | 0 / 0 / 150 |
| N2 ELS (customer) | 0 | 0 | 0 | 0 | 0 / 0 / 0 |
| **Niche revenue** | **0** | **5** | **50** | **170** | **150 / 720 / 1,650** |

- **Base revenue [R]:** 2,075 + 2,219 + 2,418 + 2,739 = $9,451M. This covers Q3 FY26 to Q2 FY27, the same window as the TTM niche column.
- **N3 TTM and CY26:** TTM is ~$0 because XConn revenue starts in Q3 FY27, after the window. CY26 = ~$10–15M of all-use XConn revenue × a 25–50% XPU-fabric share; UALink samples add ~$0.
- **N3 2027:** XConn ~$100M × 30–50%, plus $0–25M of UALink.
- **N3 2030:**
  - Base: 9% × $8B = $720M [E]. No socket is named, and a 7% share would give $560M.
  - Low: 5% × a $3B bear niche = $150M.
  - High: 10.7% × $14B = $1.5B. The draft's $2.0B high pushed the niche allocation to 104% (ALAB 4.5 + AVGO 6.0 + MRVL 2.0 + ~$2.0B private/China/other), so it is cut.
- **N1:** 0 in the base. There is no hard signal, and design NRE sits outside the foundry-defined niche. The draft's $60M is option value (+0.6pt of revenue leverage).
- **Cannibalization = 0, so net = gross.** Moving sockets from XConn to UALink is share shift inside the niche. NVLink Fusion, Photonic Fabric and in-house switches cap Marvell's share without displacing legacy revenue. The CPO threat to pluggable DSPs ($0.5–2B of 2030 revenue [E]) falls outside N2 niche revenue.
- **Revenue leverage:** incremental = 720 − 5 = $715M, and 715 ÷ 9,451 = 7.6%.
  - Low: 145 ÷ 9,451 = 1.5%.
  - High: (1,495 + 150) ÷ 9,451 = 17.4%; N3 alone is 15.8%.
- **Profit leverage:** 715 × 62% = $443M. Divided by non-GAAP TTM gross profit of ~$5,576M (9,451 × 59%), that is 7.95%.
  - Low: 1.6%.
  - High: 17.8%, including N1 at a 45% margin.
  - On GAAP gross profit (~$4,820M) it would be 9.2%, but that divides a product margin by a GAAP base.
- **Valuation lens:** 715 ÷ 205,543 = 0.35% of EV (low 0.07%, high 0.80%).

**Our estimate vs consensus.**
| Period | Our total revenue | Consensus | Gap | Why |
|---|---|---|---|---|
| FY28 (≈CY27) | $19.3B (17.5–21.0) [E] | $18.1–18.2B before Investor Day [3P]; guide ~$20B [G] | +6% vs consensus; −3.5% vs guide | We haircut custom XPU (~$6.0B) and optics timing; niches add $50M (0.3%) |
| FY29 (≈CY28) | $26.4B (22–31) [E] | Not verified; ~$25–28B interpolated [E]; ~$31B implied by management [E] | ≈ in line; −15% vs management path | Custom $9.0B vs a reported >$12B FY29 target [G, secondary]; DSP slowdown as CPO starts; niches $170M |
| FY31 (≈CY30) | not modeled | $46.85B (Visible Alpha, 4 analysts) [3P]; guide $70–90B [G] | — | — |

The whole gap comes from the rest of the business; the niches are within rounding.

**Valuation.** All figures use $230.90 (IBKR, 2026-10-15 intraday, −5.9% on the day). Earlier prints that day ran $230.5–234.9.
- **Market cap:** $202.5B on 876.9M shares.
- **EV:** $205.5B = market cap + $5.0B of notes (May-2026 10-Q) − $3.93B of cash (Aug-2026) + the $2.0B preferred at face. With the preferred as-converted it is $208.2B (conversion terms unverified).
- **Sales multiples:** 21.7x EV/TTM, ~13.2x EV/NTM (NTM ~$15.55B [E]) and 10.6x EV/FY28E (10.3x on guidance).
- **P/E:** ~55–56x FY27E ($4.1–4.2), ~43x NTM and 32–37x FY28E ($6.3–7.2).
- **History and peers:** history is ~25–40x P/E and 7–11x EV/NTM sales [E, unverified]. Peers trade at ~12x (AVGO) and 16–19x (ALAB) EV/NTM [E]. Marvell is priced near AVGO on sales, with ~10pt lower gross margin.
- **What the price implies:** ~24x our FY29E EPS (~$9.45) but ~7.7x the $30+ FY31 target. The market is paying for the FY29 ramp and heavily discounting FY31.
- **Niche value:** at 10x sales, N3 would be worth ~$7.2B, or 3.5% of EV (~$8/share).

**Risks.**
- **Customer concentration.**
  - In FY26, Distributor A was 37% of revenue, Customer A 14% and the top 10 82% [3P summary of 10-K].
  - Losing the Trainium successor would remove $2–4B of FY29 revenue [E].
  - AWS said Trainium4 will support NVLink Fusion. Whether its scale-up switch is NVLink, merchant UALink or in-house is unresolved [3P, unverified].
  - N3 is binary: a miss means $150M in 2030.
- **Capacity and execution.** TSMC N3 is tight, and Marvell's switches compete with its own XPUs for wafers. A one-generation UALink slip cuts 2027–28E N3 to ~$15M / ~$60M. Q4 FY27 needs ~$3.7B to reach the FY27 guide.
- **Balance sheet.** Net debt is ~$1.1B, and the preferred adds 1–2.5% dilution [E]. The Celestial AI earn-out (up to $2.25B) and amortization keep GAAP EPS thin.
- **Competition.**
  - N3: Broadcom (Tomahawk Ultra/TH6/TH7, which it can bundle with its XPUs), Astera, Upscale AI SkyHammer (Q4-26), Cornelis, Microchip, China's Centec (raising RMB 3.18B), and in-house switches via Alchip/GUC.
  - N1: Nvidia's NVHBM, the memory makers, GUC, Alchip and MediaTek.
- **Technology and design change.**
  - NVLink Fusion: Marvell is itself a Fusion partner, so wins can land outside N3.
  - Broadcom has left UALink, AMD Helios runs UALink-over-Ethernet, and UALink 2.0 (Apr-2026) shortens the life of 115T parts.
  - Switchless and optical topologies, including Marvell's own Photonic Fabric.
  - Attribution: Teralynx dies serve both scale-out and scale-up, so filings will never confirm N3 revenue.
  - CPO threatens the pluggable DSP franchise.
- **Expectations.** The stock is +162% over 12 months and +172% YTD, and sits 30% below its $329.80 high. It trades above its own multiple history. Management's targets need ~54–61% CAGR, so an AI capex pause would hurt.

**Bear case (~25% [E]).**
- **N3:** AWS stays on Fusion and AMD/Meta stay on Broadcom Ethernet. Marvell gets 3–5% of a ~$3B niche = $90–150M, for revenue leverage of ~0.9–1.5%.
- **Company:** the custom ramp slips a generation, and FY28 revenue is $16.5–17.5B with EPS of ~$5.0.
  - At 25x that is $125/share. At 7x EV/sales: $119B of EV, less $1.1B of net debt and the $2B preferred, is ~$132/share.
  - Bear value is $125–135 (−42% to −46%), near the 26-week low of $128.39.

**Catalysts and indicators (next 2–4 quarters).**
1. OCP Global Summit (2026-10-12 to 15): any UALink/ESUN demo or named customer.
2. SK hynix Q3 call (late Oct-2026): who designs the HBM4E custom base dies.
3. Astera Q3 (~2026-11-10): Scorpio X and UALink timing.
4. Marvell Q3 FY27 (~early Dec-2026, date unverified): the guide is $3.15B ±5% and EPS $1.10. Watch for UALink sample confirmation, first XConn revenue and a Q4 guide of ≥$3.6B.
5. AWS re:Invent (early Dec-2026): the Trainium4 scale-up fabric.
6. Broadcom FQ4 (~2026-12-11): Tomahawk Ultra scale-up deployments.
7. Marvell FY28 outlook (~Mar-2027).
8. Nvidia GTC (Mar-2027): NVLink Fusion partners.

**Confidence and weakest assumption.** Confidence is low. The N3 base assumes Marvell wins at least one volume non-NVLink socket by FY28–29 and reaches 9% of an $8B niche. Four things weigh against it:
- No customer has been named.
- UALink was missing at OCP.
- Broadcom and Astera are the incumbents.
- Marvell's own Fusion, Photonic Fabric and custom-ASIC routes would book the same sockets outside N3.

Each point of 2030 share is $80M, or 0.85pt of revenue leverage. Even the high case is under 1% of EV, so the niches do not drive the stock.

**Sources.**
- Marvell, "Reports Fourth Quarter and Fiscal Year 2026 Financial Results", 2026-03-05. https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results
- Zacks, "MRVL Q2 Earnings Beat on Data Center Strength, Outlook Raised", 2026-08-28. https://www.zacks.com/stock/news/2981826/mrvl-q2-earnings-beat-on-data-center-strength-outlook-raised
- MarketBeat, "Marvell Technology Q4 Earnings Call Highlights", 2026-03-05. https://www.marketbeat.com/instant-alerts/marvell-technology-q4-earnings-call-highlights-2026-03-05/
- Marvell, "Marvell to Acquire XConn Technologies", 2026-01-06. https://investor.marvell.com/news-events/press-releases/detail/1004/marvell-to-acquire-xconn-technologies-expanding-leadership-in-ai-data-center-connectivity
- Marvell, "Marvell to Showcase Open AI Infrastructure Solutions at OCP Global Summit 2026", 2026-10-08. https://investor.marvell.com/news-events/press-releases/detail/1036/marvell-to-showcase-open-ai-infrastructure-solutions-at-ocp-global-summit-2026
- StockAnalysis, "MRVL Investor Day 2026 transcript", 2026-10-06. https://stockanalysis.com/stocks/mrvl/transcripts/724088-investor-day-2026/
- Benzinga, "Marvell Stock Rallies as Investor Day Targets Smash Wall Street Estimates", 2026-10-06. https://www.benzinga.com/node/62198187
- Quartz, "Marvell raises fiscal 2031 revenue target at investor day", 2026-10-06. https://qz.com/marvell-investor-day-fiscal-2031-revenue-target-100626
- DatacenterDynamics, "Nvidia invests $2bn in Marvell as part of wider NVLink Fusion deal", 2026-03-31. https://datacenterdynamics.com/en/news/nvidia-invests-2bn-in-marvell-as-part-of-wider-nvlink-fusion-deal
- Marvell, "Custom HBM compute architecture", 2024-12-10. https://www.marvell.com/company/newsroom/marvell-announces-breakthrough-custom-hbm-compute-architecture.html
- SEC, Marvell 10-Q Q2 FY27, 2026-08/09. https://www.sec.gov/Archives/edgar/data/0001835632/000183563226000025/mrvl-20260801.htm
- Converge Digest, "OCP launches ESUN for Ethernet for scale-up", 2025-10. https://convergedigest.com/ocp-launches-esun-for-ethernet-for-scale-up/
- Autobound, "Marvell FY2026 10-K summary", 2026-03. https://www.autobound.ai/companies/marvell/10-k
- Interactive Brokers MCP price snapshot (contract 483492393), 2026-10-15. No public URL.


---

#### AVGO — Broadcom Inc. (N3 primary; N2 captive/customer only; N1 false positive)
*Net revenue leverage: 0.030 (0.007–0.086) · Gross: 0.030 · Profit leverage: 0.031 (0.008–0.090) · Net incremental ÷ EV: 0.16% (0.04–0.45%) · Confidence: medium (exposure is real; magnitude is undisclosed)*

**What it sells into the niche, and why customers choose it.**

Broadcom sells Ethernet switch ICs that serve as the XPU-to-XPU scale-up fabric:
- **Tomahawk Ultra:** 51.2T, Scale-Up Ethernet (SUE), under 400 ns XPU-to-XPU latency, 10-byte header [R].
- **Tomahawk 6:** 102.4T with 200G SerDes, used in scale-up trays.
- **Tomahawk 7:** 200T, taped out [G].

AMD Helios uses 12 TH6 per 72-GPU rack over UALink-over-Ethernet [R]. Customers choose Broadcom for four reasons:
- In 2026 it was the only shipping high-radix 200G switch with scale-up features, because native UALink parts were not in volume [3P].
- It uses standard Ethernet optics, copper and tooling.
- It authored SUE-T/ESUN.
- It can bundle the switch with its own XPUs for OpenAI and Meta.

Our N3 definition explicitly includes Tomahawk in scale-up trays and OpenAI–Broadcom racks, so bundled switches count at IC value. Anthropic's TPU racks run on Google ICI, which is a captive fabric and is excluded. The limits: Broadcom has left UALink, and in its own racks the switch is an undisclosed, bundled line item.

The other two niches contribute nothing:
- **N2:** TH6-Davisson CPO uses field-replaceable ELSFP lasers from an unnamed vendor [R]. Broadcom showed an in-house CW laser in 2024 [3P], but no separately priced ELS sales are verified, so N2 is 0.
- **N1:** Broadcom buys HBM rather than selling base dies. HBM4/4E base dies come from SK hynix, Samsung and Micron on TSMC logic [3P], so N1 is 0.

**Evidence of real exposure.**
- [R] AMD Helios has 6 trays × 2 TH6, so all 12 Broadcom ASICs connect to every GPU in the rack. The tray bandwidth math checks (ServeTheHome, Oct-2026). HPE/Juniper's UALoE tray is "built with Broadcom" (HPE/BusinessWire, 2025-12-02, as cited in review; not re-read).
- [R] Celestica's DS6010 dual-TH6 tray is "fully qualified" for Helios (Celestica, 2026).
- [G] Tomahawk Ultra began scale-up deployment in FQ3 and ramps in FY27. Some XPU customers moved from TH5 to TH6 or Tomahawk Ultra, and TH7 has taped out (Q3 FY26 call, 2026-09-02).
- [G]/[3P] OpenAI will deploy 1.3 GW of Jalapeño in 2027 and more than 5 GW in 2028, in Broadcom-built Ethernet racks (StatementDog; Benzinga, Sep-2026).
- [3P] Hyperscalers used TH5 Ultra/TH6 with SUE for scale-up in 2026 because no UALink option existed (NGI brief, 2026).
- Not counted: "TH6 at nearly all XPU hyperscalers" (mostly scale-out), AI networking growth of more than 2.5x, and the Anthropic TPU racks. Broadcom has disclosed no scale-up revenue, volume or ASP.

**Revenue build.**

| $M | TTM actual | CY2026E | 2027E | 2028E | 2030 low / base / high |
|---|---|---|---|---|---|
| N3 scale-up switch | ~175 (50–450) | 350 (150–700) | 1,200 (500–2,400) | 1,800 (700–5,000) | 1,000 / 3,000 / 8,000 |
| N2 UHP laser / ELS | 0 | 0 | 0 | 0 | 0 / 0 / 150 |
| N1 HBM4 base die | 0 | 0 | 0 | 0 | 0 / 0 / 0 |

- **TTM (Aug 4, 2025 to Aug 2, 2026):** mostly TH5/TH6 in custom-XPU scale-up. Helios shipments began in Q3-CY26, mostly after the TTM close.
- **CY2026E:** Helios at 0.5–2k racks × 12 TH6 × ~$8–15k ASP (unverified), plus custom-XPU scale-up, gives about $350M, roughly 39% of the ~$0.9B niche.
- **2027–28 (bottom-up):** Helios in 2027 is 7–11k racks × 12 × $8–12k = $0.7–1.6B, plus OpenAI and Meta racks.
  - This implies Broadcom takes 50–77% of the path-consistent 2027 niche ($1.55–2.39B) and 50–67% of the 2028 niche ($2.68–3.58B).
  - The draft's "~44% of $2.7B/$4.3B" overstated the 2027–28 niche relative to the prior report's growth paths, so it is withdrawn.
  - Broadcom's high early share is a real tension: if its AI plan holds, the niche's early years are too small.
- **2030:**
  - Base: 37.5% × $8B = $3.0B.
  - Low: 33% × $3B = $1.0B.
  - High: ~57% × $14B = $8.0B, raised from $6.0B because OpenAI/Meta Ethernet racks were under-modeled. OpenAI at 5 GW × 0.4–0.6M XPUs/GW × $0.5–1.5k, plus AMD at 3–5 GW × ~0.29M GPUs/GW × $1.3–2.5k, gives $2–8B as early as 2028 [E].
- **Cannibalization:** $0 (range 0–200). PEX is complementary, and reuse of the same die in scale-out is an attribution question, not cannibalization.
- **Incremental:** 3,000 − 350 = 2,650 (low 650; high 7,650). Net incremental = 2,650.
- **Gross = net revenue leverage:** 2,650 ÷ 89,104 = **2.97%** (low 0.73%, high 8.59%). The N2 high case would add 0.17 pp; $200M of cannibalization would lower net to 2.75%.
- **Profit leverage:** 2,650 × 72% ÷ 61,000 = 1,908 ÷ 61,000 = **3.13%** (low 0.77%, high 9.03%).
  - The 72% niche margin [E] is *below* the ~73% FQ4 company non-GAAP guide.
  - At a 60% bundled-pricing margin, profit leverage would be 2.6%.
  - On a gross-profit denominator of $60–63B, it would be 3.0–3.2%.
- **Net incremental ÷ EV:** 2,650 ÷ 1,689,000 = **0.16%** (low 0.04%, high 0.45%).
- **Base revenue:** 18,015 + 19,311 + 22,187 + 29,591 = $89,104M [R].

**Our estimate vs consensus.** The fiscal year ends near Oct 31, so FY27 runs from Nov-2026 to Oct-2027 and leads the calendar year by about 2 months.

| Period | Our total revenue | Consensus | Gap | Why |
|---|---|---|---|---|
| FY26 | $105.9B (guide-derived) | ~$106B | ~0% | Guide |
| FY27 | $165B (150–180) | $170.7–173.9B (Barchart; Yahoo) | −3% to −5% | AI $115B guide at face value; non-AI $47–53B because software ($6.8B→$8.75B in two quarters) looks lumpy; consensus embeds a ~$6B AI beat |
| FY28 | $256B (210–290) | Revenue unverified; EPS-implied ~$225–260B (LSEG EPS $25.86) | −2% to +14% | AI $205B (11% haircut to the $230B guide for concentration/financing); non-AI ~$51B |

CY2027 is about $180B [E]. N3 is about 0.7% of FY27E and FY28E revenue, so the niches explain none of the gap.

**Valuation.**
- **EV ≈ $1,689B:** market cap ≈ $1,650B ($338.15 [IBKR, 2026-10-15] × ~4.88B diluted shares), plus ~$63B debt [E], less $24.0B cash [R]. The range is $1,645–1,700B, or about $1,725B including the mostly backstopped ~$35B XPV SPV [3P].
- **Sales multiples:** EV/TTM sales 19.0x, EV/NTM sales ~11x (NTM ~$150–157B [E]), EV/FY27 consensus sales 9.7–9.9x.
- **Earnings multiples:** P/E is 17.4x FY27 consensus EPS of $19.39 and 13.1x LSEG FY28 EPS [3P]. TradingKey shows ~21x forward.
- **History and peers [E, from memory, unverified]:** forward P/E of 25–40x in 2024–25; peers at 22–30x.
- **Dividend yield:** 0.75% [R].
- **What the price implies:** 13x FY28 EPS discounts substantial slippage in the $230B AI plan and SPV risk; N3 is not priced at all.
- **Capitalized N3:** (2,650 × 72% − ~200 opex) × 85% ≈ $1.45B of net income. At 18x that is $26B, or ~$18B discounted 4 years at 10%, about 1.1% of market cap.

**Risks.**
- **Customer concentration:**
  - The top-5 end customers were ~45% of FQ2-26 revenue, and one distributor was 42% [R].
  - Each 1 GW deferral costs 6–9% of FY27E revenue [E].
  - AMD is ~35–70% of 2027–28 N3 revenue [E; widened from 60–75%]. A 50/50 dual-source with native UALink on MI500+ would take 2030 N3 to $2.0–2.5B; full loss of AMD would take it to $0.9–2.0B.
  - OpenAI's funding is a single point of failure for both its Jalapeño racks and its Helios racks.
- **Capacity and execution:** supply is "secured" [G], but switch dies compete with XPUs for N3/CoWoS capacity. TH7 must land in 2027.
- **Balance sheet:**
  - Net debt is ~$39B, under 1x annualized FCF (FQ3 FCF $13.7B [R]).
  - SPV guarantees ($35B done, $60–100B in talks [3P]) take adjusted net debt to ~$100–130B [E].
  - Credit default swap (CDS) spreads were reported at a record [3P].
  - SBC is offset by the $10B buyback.
- **Competition:**
  - NVLink Fusion, with AWS Trainium4 committed [R].
  - Native UALink from Astera, Marvell (115T) and Upscale.
  - Cisco G300/G302 and other ESUN members.
  - Taiwan ASIC houses (Alchip, GUC) with in-house switches; MediaTek on TPU.
  - Centec, but confined to China.
  - $/Tbps falls an estimated 25–35% per generation.
- **Technology and design change:**
  - AMD, a UALink founder, could go native UALink.
  - A switch chiplet inside the XPU would move the revenue out of N3.
  - Switchless and photonic fabrics.
  - Bundled pricing makes N3 unfalsifiable.
- **Expectations:**
  - The stock is −4.1% over 12 months while revenue grew 86%.
  - It is −32% from the $494.23 high and near the 13-week low of $335.82 [R].
  - The FQ4 guide was slightly below consensus [3P].
  - FY27 consensus already sits above the AI guide.

**Bear case.**
- **N3 bear (~30%):** the 2030 niche is ~$3B and Broadcom keeps 33%, or $1.0B. Net incremental is $650M, giving net revenue leverage of 0.73%, profit leverage of 0.77% and net incremental ÷ EV of 0.04%. In the tail case ($0.5B), leverage is 0.17%.
- **Stock bear:**
  - FY28 AI comes in at $150B as GW deployments slip under financing stress, so total revenue is ~$200B (−22% vs our base).
  - Non-GAAP gross margin falls to ~70% and FY28 EPS to $19–20.
  - At 14x that is $266–280 per share (−17% to −21%); at 12x it is ~$234 (−31%).
  - N3 is under 0.5% of this downside.

**Catalysts and indicators (next 2–4 quarters).**
1. OCP Summit (2026-10-12 to 15): ESUN/SUE-T progress and Tomahawk Ultra systems.
2. AMD Q3-26 results (~early Nov-2026, unverified): Helios rack counts × 12 TH6.
3. Astera Q3-26 (~2026-11-10, unverified): timing of native UALink switches.
4. Broadcom FQ4 FY26 (~mid-Dec-2026, unverified): the $34.8B/$21.7B guide, FY27 AI of $115B, named Tomahawk Ultra scale-up deployments, TH7, and the software run-rate.
5. SPV closings (H2-26 to 2027).
6. H1-2027: Anthropic's first GW on MI450, and the Trainium4 switch-tray bill of materials.
7. ~Mar-2027: Broadcom FQ1 FY27 and OFC 2027.
8. 2027: the fabric in OpenAI's 1.3 GW Jalapeño racks, AMD's MI500 fabric choice, and Marvell UALink sampling.

**Confidence and weakest assumption.** Confidence is medium on exposure (a named win, partner qualification and guidance) and low on magnitude, because every N3 dollar is [E].
- **Weakest assumption:** that Helios-class racks stay on Broadcom Ethernet through MI500/MI600, at ~$8–15k of IC value per switch.
- **Second:** that bundled switches in Broadcom-built racks count at IC value. If they are ruled captive, 2030 N3 falls to $1.5–2.5B and net leverage to 1.3–2.4%.
- **Third:** that the plan and the niche can both be right. If the $230B plan holds, leverage drifts toward 8.6%.

None of these changes the verdict: AVGO is a large-dollar, low-leverage beneficiary.

**Sources.**
- Broadcom, "8-K Ex.99 Q3 FY2026 results", 2026-09-02. https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm
- Broadcom, "8-K Ex.99 Q1 FY2026 results", 2026-03-04. https://www.sec.gov/Archives/edgar/data/1730168/000173016826000011/avgo-02012026x8kxex99.htm
- Broadcom, "Form 10-Q, quarter ended Aug 2, 2026", 2026-09-09. https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000080/avgo-20260802.htm
- Broadcom, "Form 10-Q, quarter ended May 3, 2026", 2026-06. https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000054/avgo-20260503.htm
- Broadcom, "Form 10-K FY2025", 2025-12. https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm
- Nasdaq, "Broadcom Q3 Earnings Call Highlights", 2026-09. https://www.nasdaq.com/articles/broadcom-q3-earnings-call-highlights
- Motley Fool, "Broadcom Q3 2026 earnings call transcript", 2026-09-09. https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/
- StatementDog, "AVGO earnings call", 2026-09. https://statementdog.com/analysis/AVGO/earnings_calls/318718
- Pulse2, "Broadcom Q3 fiscal 2026 revenue jumps 86%", 2026-09. https://pulse2.com/broadcom-q3-fiscal-2026-revenue-jumps-86-to-29-6-billion-as-ai-semiconductor-revenue-reaches-16-7-billion/
- ServeTheHome, "AMD Helios Architecture Deep Dive", 2026-10. https://www.servethehome.com/amd-helios-architecture-deep-dive-amd-broadcom-hardware-combined/5/
- Celestica, "DS6010", 2026. https://cls.celestica.com/hardware-platforms/ds6010/
- Broadcom IR, "Broadcom Ships Tomahawk Ultra", 2025-07-15. https://investors.broadcom.com/news-releases/news-release-details/broadcom-ships-tomahawk-ultra-reimagining-ethernet-switch-hpc
- NGI, "Data Center Networking in 2026", 2026. https://cdn.asp.events/CLIENT_Kisaco_R_E0D4AD69_B740_B124_D2ADF5A777880773/sites/AI-Infra-Summit-2026/media/libraries/sponsor-editorial/9372-2026-ngi-data-center-networking-report-rev-a3-1-.pdf
- CNBC, "Broadcom CEO: AI revenue targets haven't changed", 2026-09-14. https://www.cnbc.com/2026/09/14/broadcom-ceo-on-anthropics-slowdown-push-ai-revenue-targets-havent-changed.html
- Yahoo Finance/Benzinga, "Broadcom Sees $230B In AI Revenue By 2028", 2026-09. https://finance.yahoo.com/technology/ai/articles/broadcom-sees-230b-ai-revenue-023424926.html
- Yahoo Finance, "AVGO analysis", accessed 2026-10. https://finance.yahoo.com/quote/AVGO/analysis/
- Barchart, "Broadcom's sell-off is overdone", 2026. https://www.barchart.com/story/news/2377872/broadcom-s-sell-off-is-overdone-based-on-its-fcf-margins-avgo-could-be-worth-double
- TradingKey, "Broadcom stock forecast", 2026-10-09. https://www.tradingkey.com/analysis/stocks/us-stocks/262207856-broadcom-avgo-stock-forecast-october-9-2026-tradingkey
- TradingKey, "AMD after Advancing AI 2026", 2026-07-24. https://www.tradingkey.com/analysis/stocks/us-stocks/262052722-amd-stock-forecast-july-24-2026-advancing-ai-helios-anthropic-earnings-tradingkey
- The Next Web, "Broadcom $60bn AI chip debt", 2026-08. https://thenextweb.com/news/broadcom-60bn-ai-chip-debt-anthropic
- Shacknews, "AMD Helios shipping Q3 2026", 2026-08. https://www.shacknews.com/article/150249/amd-helios-ai-system-shipping-q3-2026
- StorageReview, "Broadcom ships Tomahawk 6 Davisson CPO", 2025-10. https://www.storagereview.com/news/broadcom-ships-tomahawk-6-davisson-cpo-ethernet-switch-doubling-bandwidth-to-102-4-tb-s-for-ai-fabrics
- TrendForce, "Samsung's custom HBM4E design", 2026-01-23. https://www.trendforce.com/news/2026/01/23/news-samsungs-custom-hbm4e-design-reportedly-aimed-for-mid-2026-parallels-sk-hynix-and-micron/
- Finviz/Reuters, "Broadcom shares slip as Q4 forecast falls below estimates", 2026-09-02. https://finviz.com/news/388461/broadcom-shares-slip-as-q4-revenue-forecast-falls-below-estimates
- Interactive Brokers, market data snapshot, 2026-10-15 (no public URL).
- Prior report, N3 niche file L07.md, 2026-10-15 (local file).


---

## 3. Multi-niche winners

Companies with a role in two or all three niches. Combined net incremental counts only the niches where the company earns revenue.

| Ticker | Niches and roles | Combined net incremental (2030 base) | Combined net revenue leverage | Comment |
|---|---|---|---|---|
| **MRVL** | N1: IP/EDA/design services (no hard signal); N2: customer (pays, does not earn); N3: direct supplier | $715M | 7.6% | Only company with a role in all three niches. Scale-up switch silicon: earner (UALink 115T, XConn). HBM base dies: option only (custom base-die design, no named win; base case $0). CPO lasers: a customer that buys light sources for Celestial AI Photonic Fabric. Scale-up switching drives all of its leverage. |
| **TSM** | N1: direct supplier; N3: supplier to supplier (no hard signal) | $6.8B | 4.3% | HBM base dies: direct supplier (~92% share). Switch silicon: makes the wafers and CoWoS packaging for every merchant switch die (~11% of switch ASP; attribution only). It wins whoever takes the socket. The switch-silicon gain partly displaces NVSwitch wafers it also makes. |
| **NVDA** | N1: customer (pays, does not earn); N2: customer (pays, does not earn) | $0.0M | n/a | A customer in HBM base dies (pays through HBM; NVHBM design) and in CPO lasers (buys light sources for Spectrum-X / Quantum-X Photonics). In scale-up switch silicon it is the substitute (NVLink / NVLink Fusion). It earns no revenue in any of the three niches. |
| **ASX** | N2: contract manufacturing/assembly (no hard signal); N3: contract manufacturing/assembly (no hard signal) | $216M | 1.0% | ASE/USI: packages switch dies (attribution only) and, via USI, has a UHP ELSFP product line reported in secondhand Chinese press. Neither has a niche-specific hard signal; about 1% of revenue combined. |
| **AVGO** | N2: customer (pays, does not earn); N3: direct supplier | $2.6B | 3.0% | Scale-up switch silicon: earner (Tomahawk Ultra / TH6). CPO lasers: buyer, or captive maker, of light sources for its Davisson CPO switches; no merchant ELS sales verified. False positive in HBM base dies. |
| **CLS** | N2: customer (pays, does not earn); N3: systems | $0.0M | 0.0% | Downstream. It builds AMD Helios scale-up switch trays (a named win) and is evaluating CPO assembly. That is tray revenue at ~11% gross margin, not niche revenue. |

**Bottom line:**
- No company is a meaningful winner in more than one of these niches.
- Marvell is the only name touching all three, and only scale-up switching adds revenue.
- TSMC is the only company with meaningful revenue in two niches: HBM base dies directly, and switch silicon as the foundry, whoever wins the socket. ASE's two exposures are both attribution-only and come to about 1% of revenue.

---

## 4. False positives: popular AI plays with less niche exposure than the market assumes

**How we tested.** A company counts only when a hard signal ties its revenue to the niche as defined (N1 merchant base-die wafers, KGD and NRE; N2 200 mW-plus InP CW lasers and ELS modules; N3 merchant scale-up switch ICs). NET revenue leverage subtracts the legacy revenue each niche cannibalizes. Niche figures are [E] unless labelled. 12-month performance is IBKR last price over the open 52 weeks ago, minus 1, on 2026-10-15. For scale, the real winners are LITE at +14.4% net (N2), ALAB at +141% net, or 1.41x (N3), and TSM at about +4.0% net in N1 (+4.3% including N3).

| Ticker | Niche / role | 12m | TTM rev $M | Niche TTM / CY26E $M | Niche 2030 base (range) $M | Cannibalized 2030 $M | NET rev. leverage (gross) | Profit leverage |
|---|---|---|---|---|---|---|---|---|
| AXTI | N2 substrate | +1,106% | 126 | ~0.5 / 1.2 | 5 (1-18) | 2.8 | +0.8% (+3.0%) | +1.0% |
| COHR | N2 supplier | +122% | 7,120 | 0-5 / 15 | 575 (200-1,200) | 700 | -2.0% (+7.9%) | 0 to +0.7% |
| AAOI | N2 entrant | +174% | 596 | 0 / 1 | 40 (0-160) | 100 | -10.2% (+6.5%) | -4.4% |
| FN | N2 assembly | -0.4% | 4,640 | ~1 / 3 net | 45 net (5-175) | 500 | -9.9% (+0.9%) | -9.8% |
| AEHR | N2/N1 burn-in | +141% | 50 | 0 / 0 | 0 (no niche order found) | 0 | 0 | 0 |
| MU | N1 customer | +354% | 133,190 | 0 / 0 | 0; pays $1.1-2.0B/yr for dies | 0 | 0 | 0 (die-cost headwind -0.5 to -1.5%) |
| INTC | N1 entrant (unconfirmed) | +159% | 57,050 | 0 / 0 | 225 (0-1,100) | 0 | +0.4% (max +1.9%) | +0.4% |
| RMBS (SNPS, CDNS) | N1/N3 host-side IP | -8.7% | 756 | 0 / ~0 | 1-5 | 0 | +0.1 to +0.7% | ~+0.5% |
| CRDO | N3 adjacent (AECs) | +24% | 1,591 | 0 / 0 in-niche (~300 adjacent) | 0 in-niche (750 adjacent; 100-2,800) | AECs at risk to passive copper and CPO | 0 in-niche (adjacent +28%, low -13%) | n/m |
| MCHP | N3 PCIe fan-out | +9.4% | 5,123 | ~0 / 0-5 | ~25 (0-80) | 0 | +0.4% | +0.4% |

**AXTI is the clearest false positive.** The story is that InP is the CPO bottleneck and AXT is the US-listed InP substrate maker. Q2-26 InP revenue hit a record $30.7M of $47.6M [R]. AXT has long-term agreements with Coherent, Lumentum and Casela, including $47.7M of wafer prepayments [R, via call summary]. But that demand comes from pluggable transceiver lasers. A 3-inch-equivalent wafer costs about $525 and yields about 2,500 UHP dies worth about $105k as lasers [E], so substrate, including qualification overhead, is about 0.7% of niche value. That works out to about $5M for AXT in 2030 [E], about 1% of its $461M CY27 consensus [3P]. CPO also cuts InP laser area per Tb/s to about 0.5-0.7x that of an EML pluggable and removes InP photodetectors, which cannibalizes about $2.8M of legacy InP by 2030 [E] and leaves net leverage at only +0.8%. At 24.4x EV/TTM sales, the stock is priced on the pluggable cycle and Chinese export permits. *It would become real if* 6-inch UHP lines disclosed AXT as a main substrate source. Even then, our high case is only $18M.

**COHR is a real supplier with negative net exposure.** The story is Nvidia's $2B stake plus a purchase commitment [R]. Coherent's niche revenue is real: CPO revenue starts in the December 2026 quarter [G], and its Texas 6-inch InP fab is ramping UHP CW lasers [G]. But Coherent is also a top-two 800G/1.6T pluggable vendor [E]. By 2030, scale-out CPO removes about $0.5-1.05B of its transceiver revenue (base $0.7B) [E], which is more than its $560M niche increment. *It would become real if* CPO lands mostly in scale-up, where it replaces copper rather than Coherent's pluggables. Other paths: a niche share above about 35%, or CPO FAU/PIC content (outside this niche) offsetting the loss.

**AAOI has a product launch, not a design win.** The story is a US-made 400 mW laser with 55-65% ELS gross margins [G]. The part is real [R], but we found no qualification at Nvidia, Broadcom or any hyperscaler, and CY26 niche revenue is samples. Its pluggables for Amazon and Microsoft, about $100M at risk by 2030 [E], are exactly what CPO displaces. *It would become real with* a named qualification and production PO. In the 3.5%-share high case, net leverage turns to +10%.

**FN shows the assembler's dilemma.** The story is that Nvidia, a 16.3% customer [R], uses Fabrinet to build CPO. In-niche value-add is small, about $45M net by 2030, because Lumentum and Coherent build ELS in-house. Meanwhile about $0.5B of pluggable assembly is at risk [E]. Flat over 12 months and 49% below its high, the stock already prices some of this. *It would become real with* disclosed outsourced ELS builds. The real offset, CPO engine assembly, sits outside this niche.

**AEHR does burn-in for the substitute.** Its 2026 follow-on orders (March, June and August, all from one unnamed lead customer) are for silicon-photonics PIC wafers [R]. None are for discrete InP UHP lasers. HBM burn-in is still only "interest", and it would fall outside N1 anyway. Integrated-laser SiPh competes with N2. The FY27 guide of $130-150M [G] is real growth, not niche growth. *It would become real with* a named order to burn in UHP CW-DFB or ELS lasers.

**MU is a customer, not a supplier.** Micron says its HBM4E base die, both standard and NVHBM, uses a foundry process [G, via secondary summary], which means it buys from TSMC. Niche revenue is zero. By 2030 Micron pays about $1.1-2.0B a year for dies [E], at about $30-55 each versus $10-20 for its in-house dies [E]. That is a 0.5-1.5% gross-profit headwind unless HBM4E pricing absorbs it. Micron wins on HBM, but the base die moves value to TSMC. *It turns positive only if* custom-HBM price premiums are disclosed above the die cost.

**INTC is an unconfirmed second source.** Reports of 31-Aug-26 said SK hynix was weighing Intel for HBM4E base dies. SK hynix said "some of the reports are not true", and the plan remains at the evaluation stage [R]. Even a 3-15% share from 2028 adds $0.2-1.1B to $57B of revenue: +0.4% in the base case and +1.9% at best. *It would become real with* a signed, qualified contract, probably decided in 2027.

**RMBS, SNPS and CDNS sell host-side IP.** Rambus's HBM4E controller (March 2026) is pitched for "an AI SoC or a custom base die" [R], but it has no named base-die licensee. Such a license is worth about $1-5M a year [E] against $756M of revenue. Synopsys and Cadence HBM IP is host-side, and base-die EDA seats are under $10M industry-wide [E]. In N3 the whole licensable IP pool is about $64M in 2030 [E]; Synopsys gets about $40M (+0.3%). *It would become real with* a named custom base-die license that pays per-die royalties.

**CRDO is adjacent, not switch silicon.** The story is that every scale-up rack is wired with Credo AECs. AECs connect trays to switch trays, so N3 revenue is zero. Adjacent scale-up AEC revenue is about $300M in CY26 [E]; the split is undisclosed, and four customers account for 33%, 28%, 13% and 10% of revenue [R]. AMD Helios uses a passive cabled backplane, and CPO is a threat after 2028, which gives the -13% low case. The stock is 45% below its 52-week high. *It would become real with* disclosed AEC attach in non-NVLink scale-up racks, or with Credo fabric silicon.

**MCHP sells PCIe fan-out, not XPU fabric.** Switchtec Gen 6 was guided to initial production in June 2026, with volume toward year-end [G]. We found no XPU-to-XPU design win; its use is CPU-GPU and storage fan-out. Niche revenue is at most $80M even in 2030's high case [E], under 2% of its $5.1B revenue. *It would become real with* a named UALink or PCIe scale-up socket.

**Also screened.**
- TSEM (+175%): its integrated-laser SiPh platforms are a substitute for N2, so niche revenue is zero.
- NVDA (+17%): a customer in N1 and N2, and a substitute in N3 through NVLink Fusion, which AWS has committed to for Trainium4 [R].
- CAMT and ONTO: N1 revenue leverage of -1.0% and -0.3%, because base-die inspection spend peaks in 2026-27.

---

## 5. Sources

**421 distinct sources** are cited across the deep dives, chain maps, financial-data collection, consensus check and false-positives analysis. Each deep dive also ends with its own source list.

Source-quality notes:
- Many links are secondary write-ups of primary documents (earnings-call summaries, aggregator pages), because primary sites could not be fetched from this environment.
- Prices, 90-day dollar volume and 52-week statistics are from Interactive Brokers market data, pulled 14–15 October 2026.

**Deep dive: ALAB**

- Astera Labs IR, "Astera Labs Reports Second Quarter 2026 Financial Results", 2026-08-04. https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-reports-second-quarter-2026-financial-results
- SEC EDGAR, "Astera Labs 8-K Ex.99.1 (Q2-26 earnings release)", 2026-08-04. https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000033/q226exhibit991.htm
- SEC EDGAR, "Astera Labs 8-K Ex.99.1 (Q4 and FY2025 results)", 2026-02-10. https://www.sec.gov/Archives/edgar/data/1736297/000173629726000005/q425exhibit991.htm
- SEC EDGAR, "Astera Labs Form 10-Q for the quarter ended 30-Jun-2026", 2026-08. https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000035/alab-20260630.htm
- SEC EDGAR, "Astera Labs Form 8-K (Amazon warrant)", 2026-02-05. https://www.sec.gov/Archives/edgar/data/1736297/000110465926012606/tm265461d1_8k.htm
- Futurum Group, "Astera Labs Q2 FY 2026 Earnings Pull Scorpio Switch Leadership Forward", 2026-08-04. https://futurumgroup.com/insights/astera-labs-q2-fy-2026-earnings-pull-scorpio-switch-leadership-forward/
- Yahoo Finance, "Astera Labs (ALAB) Q2 2026 earnings call highlights", 2026-08. https://finance.yahoo.com/markets/stocks/articles/astera-labs-inc-alab-q2-050348738.html
- TIKR, "Astera Labs' Scorpio X Is Already in Volume Production. Citi Showed How Fast the Customer List Is Growing", 2026-09. https://www.tikr.com/blog/astera-labs-scorpio-x-is-already-in-volume-production-citi-showed-how-fast-the-customer-list-is-growing
- NVIDIA Developer Blog, "AWS Integrates AI Infrastructure with NVIDIA NVLink Fusion for Trainium4 Deployment", 2025-12. https://developer.nvidia.com/blog/aws-integrates-ai-infrastructure-with-nvidia-nvlink-fusion-for-trainium4-deployment/
- Investing.com, "Amazon adopts NVLink Fusion for Trainium4, Astera Labs stock unfairly hit", 2025-12. https://www.investing.com/news/analyst-ratings/amazon-adopts-nvlink-fusion-for-trainium4-astera-labs-stock-unfairly-hit-93CH-4387782
- TipRanks / TheFly, "NVLink/Trainium4 re:Invent mention not negative for Astera Labs, says Jefferies", 2025-12. https://www.tipranks.com/news/the-fly/nvlink-trainium4-reinvent-mention-not-negative-for-astera-labs-says-jefferies-thefly
- Finviz (company PR reprint), "Astera Labs Announces Conference Call to Review Third Quarter 2026 Financial Results", 2026-10-06. https://finviz.com/news/399499/astera-labs-announces-conference-call-to-review-third-quarter-2026-financial-results
- Yahoo Finance, "ALAB analysis (analyst estimates)", 2026-10 (accessed). https://finance.yahoo.com/quote/ALAB/analysis/
- VCP Scanner, "ALAB estimates (pre-raise dated consensus table; page attribution unverified)", 2026-08-01. https://www.vcpscanner.com/valuation/alab/estimates
- HPCwire, "First UALink products late 2026 / early 2027", 2026-09. https://www.hpcwire.com/?p=197496
- Converge Digest, "Astera Labs Q1 revenue jumps 93%, AI fabric growth", 2026-05. https://convergedigest.com/astera-labs-q1-revenue-jumps-93-ai-fabric-growth/
- Lumentum, "Lumentum, Astera Labs and Corning to Demonstrate 1060 nm VCSEL-Based PCIe-over-Optics for AI Rack-Scale Connectivity at the 2026 OCP Global Summit", 2026-10. https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Astera-Labs-and-Corning-to-Demonstrate-1060-nm-VCSEL-Based-PCIe-over-Optics-for-AI-Rack-Scale-Connectivity-at-the-2026-OCP-Global-Summit/default.aspx
- Trefis, "Astera Labs Beat and Guided Higher, Then Fell Because the Rally Came First", 2026-08-06. https://www.trefis.com/stock/alab/articles/610418/astera-labs-beat-and-guided-higher-then-fell-because-the-rally-came-first/2026-08-06
- Interactive Brokers (MCP), "ALAB price snapshot, contract 692196414", 2026-10-15. n/a (IBKR MCP data, no public URL)

**Deep dive: MRVL**

- Marvell, "Marvell Technology, Inc. Reports Fourth Quarter and Fiscal Year 2026 Financial Results", 2026-03-05. https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results
- SEC / Marvell, "Q4 FY26 8-K Exhibit 99.1", 2026-03-05. https://www.sec.gov/Archives/edgar/data/1835632/000183563226000006/q426_8kx1312026ex-991.htm
- Zacks, "MRVL Q2 Earnings Beat on Data Center Strength, Outlook Raised", 2026-08-28. https://www.zacks.com/stock/news/2981826/mrvl-q2-earnings-beat-on-data-center-strength-outlook-raised
- Futurum, "Marvell Q2 FY 2027: Connectivity and Custom Silicon Fuel AI Growth", 2026-08-28. https://futurumgroup.com/insights/marvell-q2-fy-2027-connectivity-and-custom-silicon-fuel-ai-growth/
- MarketBeat, "Marvell Technology Q4 Earnings Call Highlights", 2026-03-05. https://www.marketbeat.com/instant-alerts/marvell-technology-q4-earnings-call-highlights-2026-03-05/
- Marvell, "Marvell to Acquire XConn Technologies, Expanding Leadership in AI Data Center Connectivity", 2026-01-06. https://investor.marvell.com/news-events/press-releases/detail/1004/marvell-to-acquire-xconn-technologies-expanding-leadership-in-ai-data-center-connectivity
- Marvell, "Marvell Completes Acquisition of XConn Technologies", 2026-02. https://investor.marvell.com/news-events/press-releases/detail/1007/marvell-completes-acquisition-of-xconn-technologies
- Pulse 2.0, "Marvell to buy XConn for $540 million to deepen PCIe/CXL switching and UALink push", 2026-01. https://pulse2.com/marvell-to-buy-xconn-for-540-million-to-deepen-pcie-cxl-switching-and-ualink-push
- Marvell, "Marvell to Showcase Open AI Infrastructure Solutions at OCP Global Summit 2026", 2026-10-08. https://investor.marvell.com/news-events/press-releases/detail/1036/marvell-to-showcase-open-ai-infrastructure-solutions-at-ocp-global-summit-2026
- StockAnalysis, "MRVL Investor Day 2026 transcript", 2026-10-06. https://stockanalysis.com/stocks/mrvl/transcripts/724088-investor-day-2026/
- Quartz, "Marvell raises fiscal 2031 revenue target at investor day", 2026-10-06. https://qz.com/marvell-investor-day-fiscal-2031-revenue-target-100626
- Benzinga, "Marvell Stock Rallies as Investor Day Targets Smash Wall Street Estimates", 2026-10-06. https://www.benzinga.com/node/62198187
- Investing.com, "Marvell Technology stock rallies following ambitious investor day targets", 2026-10-06. https://www.investing.com/news/stock-market-news/marvell-technology-stock-rallies-following-ambitious-investor-day-targets-4934767
- SimpleTechTrend, "Marvell Investor Day 2026: An $80B Bet on Connectivity", 2026-10 (approx.). https://www.simpletechtrend.com/en/post/marvell-investor-day-2026-connectivity-scale-up-optics-en
- DatacenterDynamics, "Nvidia invests $2bn in Marvell as part of wider NVLink Fusion deal", 2026-03-31. https://datacenterdynamics.com/en/news/nvidia-invests-2bn-in-marvell-as-part-of-wider-nvlink-fusion-deal
- Bloomberg, "Nvidia Invests $2 Billion in Marvell in AI Pact, Sparking Rally", 2026-03-31. https://www.bloomberg.com/news/articles/2026-03-31/nvidia-invests-2-billion-in-marvell-announces-partnership
- Yahoo Finance (Reuters), "Nvidia invests $2 billion in Marvell", 2026-03-31. https://finance.yahoo.com/news/nvidia-invests-2-billion-marvell-121325616.html
- Marvell, "Marvell Announces Breakthrough Custom HBM Compute Architecture", 2024-12-10. https://www.marvell.com/company/newsroom/marvell-announces-breakthrough-custom-hbm-compute-architecture.html
- SEC / Marvell, "Form 10-Q, Q2 FY27 (period ended 2026-08-01)", 2026-08 to 09. https://www.sec.gov/Archives/edgar/data/0001835632/000183563226000025/mrvl-20260801.htm
- SEC / Marvell, "Form 10-Q, Q1 FY27 (period ended 2026-05-02)", 2026-05 to 06. https://www.sec.gov/Archives/edgar/data/0001835632/000183563226000019/mrvl-20260502.htm
- Autobound, "Marvell FY2026 10-K summary", 2026-03. https://www.autobound.ai/companies/marvell/10-k
- Marvell, "Marvell Completes Acquisition of Celestial AI", 2026-02-02. https://investor.marvell.com/news-events/press-releases/detail/1005/marvell-completes-acquisition-of-celestial-ai
- Signal Integrity Journal, "POET Technologies Introduces POET Starlight for the AI Market and Receives Advanced Purchase Order from Celestial AI", 2023-10. https://www.signalintegrityjournal.com/articles/3122-poet-technologies-introduces-poet-starlight-for-the-artificial-intelligence-market-and-receives-advanced-purchase-order-from-celestial-ai
- Converge Digest, "OCP launches ESUN for Ethernet for scale-up", 2025-10. https://convergedigest.com/ocp-launches-esun-for-ethernet-for-scale-up/
- StreetInsider, "Marvell Technology shares fall on valuation concerns", 2026-10-14. https://www.streetinsider.com/Investing/Marvell+Technology+shares+fall+on+valuation+concerns/27174917.html
- Interactive Brokers (MCP), "MRVL price snapshot and company connections (contract 483492393)", 2026-10-15. n/a (IBKR MCP data; no public URL)

**Deep dive: AVGO**

- Broadcom (SEC), "8-K Ex.99 Q3 FY2026 results", 2026-09-02. https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm
- Broadcom (SEC), "8-K Ex.99 Q1 FY2026 results", 2026-03-04. https://www.sec.gov/Archives/edgar/data/1730168/000173016826000011/avgo-02012026x8kxex99.htm
- Broadcom (SEC), "Form 10-Q, quarter ended Aug 2, 2026", 2026-09-09. https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000080/avgo-20260802.htm
- Broadcom (SEC), "Form 10-Q, quarter ended May 3, 2026", 2026-06. https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000054/avgo-20260503.htm
- Broadcom (SEC), "Form 10-K FY2025", 2025-12. https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm
- Nasdaq, "Broadcom Q3 Earnings Call Highlights", 2026-09. https://www.nasdaq.com/articles/broadcom-q3-earnings-call-highlights
- Motley Fool, "Broadcom (AVGO) Q3 2026 earnings call transcript", 2026-09-09. https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/
- StatementDog, "AVGO earnings call summary", 2026-09. https://statementdog.com/analysis/AVGO/earnings_calls/318718
- Pulse2, "Broadcom Q3 fiscal 2026 revenue jumps 86% to $29.6 billion", 2026-09. https://pulse2.com/broadcom-q3-fiscal-2026-revenue-jumps-86-to-29-6-billion-as-ai-semiconductor-revenue-reaches-16-7-billion/
- ServeTheHome, "AMD Helios Architecture Deep Dive (p.4)", 2026-10. https://www.servethehome.com/amd-helios-architecture-deep-dive-amd-broadcom-hardware-combined/4/
- ServeTheHome, "AMD Helios Architecture Deep Dive (p.5)", 2026-10. https://www.servethehome.com/amd-helios-architecture-deep-dive-amd-broadcom-hardware-combined/5/
- Celestica, "DS6010 product page", 2026. https://cls.celestica.com/hardware-platforms/ds6010/
- Broadcom IR, "Broadcom Ships Tomahawk Ultra", 2025-07-15. https://investors.broadcom.com/news-releases/news-release-details/broadcom-ships-tomahawk-ultra-reimagining-ethernet-switch-hpc
- NGI / AI Infra Summit, "Data Center Networking in 2026", 2026. https://cdn.asp.events/CLIENT_Kisaco_R_E0D4AD69_B740_B124_D2ADF5A777880773/sites/AI-Infra-Summit-2026/media/libraries/sponsor-editorial/9372-2026-ngi-data-center-networking-report-rev-a3-1-.pdf
- CNBC, "Broadcom CEO on Anthropic's slowdown push: AI revenue targets haven't changed", 2026-09-14. https://www.cnbc.com/2026/09/14/broadcom-ceo-on-anthropics-slowdown-push-ai-revenue-targets-havent-changed.html
- Yahoo Finance (Benzinga), "Broadcom Sees $230B In AI Revenue By 2028", 2026-09. https://finance.yahoo.com/technology/ai/articles/broadcom-sees-230b-ai-revenue-023424926.html
- Yahoo Finance, "AVGO analysis", 2026-10. https://finance.yahoo.com/quote/AVGO/analysis/
- Barchart, "Broadcom's sell-off is overdone based on its FCF margins", 2026. https://www.barchart.com/story/news/2377872/broadcom-s-sell-off-is-overdone-based-on-its-fcf-margins-avgo-could-be-worth-double
- TradingKey, "Broadcom (AVGO) stock forecast", 2026-10-09. https://www.tradingkey.com/analysis/stocks/us-stocks/262207856-broadcom-avgo-stock-forecast-october-9-2026-tradingkey
- TradingKey, "AMD stock forecast after Advancing AI 2026", 2026-07-24. https://www.tradingkey.com/analysis/stocks/us-stocks/262052722-amd-stock-forecast-july-24-2026-advancing-ai-helios-anthropic-earnings-tradingkey
- The Next Web, "Broadcom $60bn AI chip debt for Anthropic", 2026-08. https://thenextweb.com/news/broadcom-60bn-ai-chip-debt-anthropic
- Shacknews, "AMD Helios AI system shipping Q3 2026", 2026-08. https://www.shacknews.com/article/150249/amd-helios-ai-system-shipping-q3-2026
- StorageReview, "Broadcom ships Tomahawk 6 Davisson CPO Ethernet switch", 2025-10. https://www.storagereview.com/news/broadcom-ships-tomahawk-6-davisson-cpo-ethernet-switch-doubling-bandwidth-to-102-4-tb-s-for-ai-fabrics
- TrendForce, "Samsung's custom HBM4E design reportedly aimed for mid-2026", 2026-01-23. https://www.trendforce.com/news/2026/01/23/news-samsungs-custom-hbm4e-design-reportedly-aimed-for-mid-2026-parallels-sk-hynix-and-micron/
- Finviz (Reuters), "Broadcom shares slip as Q4 revenue forecast falls below estimates", 2026-09-02. https://finviz.com/news/388461/broadcom-shares-slip-as-q4-revenue-forecast-falls-below-estimates
- Interactive Brokers, "AVGO market data snapshot (contract 313130367)", 2026-10-15. IBKR MCP data (no public URL)
- Internal prior report, "N3 niche file L07.md", 2026-10-15. local file: /tmp/claude-0/-home-user-my-repo/350fdcc3-501b-5ea9-949a-10bbbedab992/scratchpad/deep/L07.md

**Deep dive: LITE**

- SEC (Lumentum 8-K Ex.99.1), "Lumentum Q4 / FY2026 results", 2026-08-11. https://www.sec.gov/Archives/edgar/data/0001633978/000162828026055726/lite_ex991xq4fy26.htm
- Lumentum, "Q4 FY26 Earnings Presentation", 2026-08-11. https://s21.q4cdn.com/377324469/files/doc_financials/2026/q4/Q4-FY26-Earnings-Presentation_final.pdf
- SEC (Lumentum 8-K Ex.99.1), "Lumentum Q3 FY26 results", 2026-05-05. https://www.sec.gov/Archives/edgar/data/0001633978/000162828026030530/lite_ex991xq3fy26.htm
- SEC (Lumentum 10-K), "Lumentum Holdings Form 10-K FY2026", 2026-08. https://www.sec.gov/Archives/edgar/data/0001633978/000162828026057358/lite-20260627.htm
- Yahoo Finance / Reuters, "Nvidia to invest $2 billion each in Lumentum, Coherent", 2026-03-02. https://finance.yahoo.com/news/nvidia-invest-4-billion-photonic-131110099.html
- SiliconANGLE, "Nvidia invests $4B in co-packaged optics suppliers Lumentum, Coherent", 2026-03-02. https://siliconangle.com/2026/03/02/nvidia-invests-4b-co-packaged-optics-suppliers-lumentum-coherent/
- MarketBeat, "Lumentum Q4 earnings call highlights", 2026-08-11. https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/
- MarketBeat, "Lumentum Q3 earnings call highlights", 2026-05-05. https://www.marketbeat.com/instant-alerts/lumentum-q3-earnings-call-highlights-2026-05-05/
- AOL / Motley Fool, "Lumentum (LITE) Q2 2026 earnings call transcript", 2026-02-03. https://www.aol.com/articles/lumentum-lite-q2-2026-earnings-234107096.html
- MarketBeat, "Lumentum Q4 FY2025 earnings call transcript", 2025-08-12. https://www.marketbeat.com/earnings/reports/2025-8-12-lumentum-holdings-inc-stock
- Semiconductor Today, "Lumentum news item (transceivers to double, EML growth, supply gap)", 2026-08-19. https://semiconductor-today.com/news_items/2026/aug/lumentum-190826.shtml
- LetsDataScience, "Lumentum targets $8B annual revenue run-rate", 2026-03 (exact date unverified). https://letsdatascience.com/news/lumentum-targets-8b-annual-revenue-runrate-55b28c7c
- Nasdaq / Zacks, "Bull of the Day: Lumentum (LITE)", 2026 (undated). https://www.nasdaq.com/articles/bull-day-lumentum-lite-0
- TradingView / Seeking Alpha, "Lumentum's outlook brightens on Nvidia's co-packaged optics scale-out: GF", 2026 (exact date unverified). https://www.tradingview.com/news/seekingalpha:9a12ce4f9094b:0-lumentum-s-outlook-brightens-on-nvidia-s-co-packaged-optics-scale-out-gf/
- X (@AGTPinsights), "Post on Lumentum CEO remarks at the Global Photonics Economic Forum", 2026-09-24. https://x.com/AGTPinsights/status/2105956968351543735
- Trefis, "What is the true hidden price of Lumentum stock", 2026-10-08. https://www.trefis.com/stock/lite/articles/617928/what-is-the-true-hidden-price-of-lumentum-stock/2026-10-08
- Barchart, "Analysts are upping their price targets on Lumentum stock, here's why", 2026 (exact date unverified). https://www.barchart.com/story/news/3875971/analysts-are-upping-their-price-targets-on-lumentum-stock-here-s-why
- Lumentum Investor Relations, "Lumentum announces reporting date for fiscal first quarter 2027 results", 2026-10-05. https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Reporting-Date-for-Fiscal-First-Quarter-2027-Financial-Results/default.aspx
- 24/7 Wall St, "Lumentum falls 10% as optics selloff hits hardest where capacity is sold out", 2026-10-12. https://247wallst.com/investing/2026/10/12/lumentum-falls-10-as-optics-selloff-hits-hardest-where-capacity-is-sold-out-applied-optoelectronics-drops-7-coherent-slides-7/
- Interactive Brokers, "Market-data snapshot, LITE (conid 201113895)", 2026-10-15. n/a: IBKR data has no public URL

**Deep dive: VECO**

- Semiconductor Today, "Veeco InP-laser equipment orders (Veeco release dated 2026-05-05)", 2026-05-06. https://semiconductor-today.com/news_items/2026/may/veeco-060526.shtml
- LEDinside, "$250 Million+ in Equipment Orders for Manufacturing Indium Phosphide Lasers", 2026-05-26. https://ledinside.com/news/2026/5/2026_05_26_01
- Yole Group, "Veeco announces $250 million+ in equipment orders for manufacturing indium phosphide lasers (repost)", 2026-05. https://yolegroup.com/industry-news/veeco-announces-250-million-in-equipment-orders-for-manufacturing-indium-phosphide-lasers/
- SEC, "Veeco 8-K Ex.99.1, Q2-26 results", 2026-08-05. https://www.sec.gov/Archives/edgar/data/0000103145/000110465926091118/veco-20260805xex99d1.htm
- Barchart, "Veeco reports second quarter 2026 financial results", 2026-08. https://barchart.com/story/news/3672987/veeco-reports-second-quarter-2026-financial-results
- Quartr, "Veeco Instruments Q2 2026 event page", 2026-08. https://quartr.com/events/veeco-instruments-inc-veco-q2-2026_ofuH3zSv
- Semiconductor Today, "Veeco Q2-26 results item", 2026-08-12. https://www.semiconductor-today.com/news_items/2026/aug/veeco-120826.shtml
- MarketBeat, "Veeco Instruments Q2 earnings call highlights", 2026-08-06. https://www.marketbeat.com/instant-alerts/veeco-instruments-q2-earnings-call-highlights-2026-08-06/
- Motley Fool, "Veeco (VECO) Q2 2026 earnings call transcript", 2026-08-12. https://www.fool.com/earnings/call-transcripts/2026/08/12/veeco-veco-q2-2026-earnings-call-transcript/
- Stock Titan, "Veeco reports fourth quarter and fiscal year 2025 financial results", 2026-02. https://www.stocktitan.net/news/VECO/veeco-reports-fourth-quarter-and-fiscal-year-2025-financial-ai8poirtut4a.html
- Stock Titan, "Veeco 10-Q Q2-26 summary", 2026-08. https://www.stocktitan.net/sec-filings/VECO/10-q-veeco-instruments-inc-quarterly-earnings-report-e9603a2aa3e9.html
- Axcelis IR, "Axcelis Technologies and Veeco Instruments combine", 2025-10-01. https://investor.axcelis.com/news-releases/news-release-details/axcelis-technologies-and-veeco-instruments-combine-creating/
- Veeco IR, "Veeco stockholders approve merger with Axcelis", 2026-02-06. https://ir.veeco.com/news-and-events/news-details/2026/Veeco-Stockholders-Approve-Merger-with-Axcelis/default.aspx
- ION Analytics DealReporter, "Veeco/Axcelis faces closer China antitrust scrutiny amid possible complaints", 2026-03. https://ionanalytics.com/insights/dealreporter/veeco-axcelis-faces-closer-china-antitrust-scrutiny-amid-possible-complaints/
- SEC, "Axcelis 8-K Ex.99.1, Q2-26 results", 2026-08. https://www.sec.gov/Archives/edgar/data/0001113232/000110465926091697/tm2622315d1_ex99-1.htm
- Aixtron IR, "Strong momentum in optoelectronics continues", 2026-07-30. https://www.aixtron.com/en/investors/Strong%20momentum%20in%20optoelectronics%20continues_n14146
- Deutsche Boerse / Aixtron, "AIXTRON receives multiple orders for G10-AsP MOCVD systems from Lumentum", 2026-05. https://live.deutsche-boerse.com/news/AIXTRON-receives-multiple-orders-for-G10-AsP-MOCVD-Systems-from-Lumentum-to-support-expansion-of-High-Speed-Optical-Solutions-for-AI-Networks-12201f09-f0ac-4b41-b535-8991bbb0f139
- MarketBeat, "Veeco receives average recommendation of Hold from analysts", 2026-08-06. https://www.marketbeat.com/instant-alerts/veeco-instruments-inc-nasdaqveco-receives-average-recommendation-of-hold-from-analysts-2026-08-06/
- Tickflow, "VECO forecast", 2026-08-01. https://tickflow.io/stock/VECO/forecast
- Yahoo Finance, "VECO analysis (mid-Sep-2026 snapshot via search summary, unverified)", 2026-09. https://finance.yahoo.com/quote/VECO/analysis/
- Interactive Brokers, "Market-data snapshots and weekly closes (VECO, ACLS)", 2026-10-15. IBKR company data (no public URL)

**Deep dive: AXTI**

- AXT Inc. (SEC), "Q2 2026 8-K Ex.99", 2026-07-30. https://www.sec.gov/Archives/edgar/data/0001051627/000143774926025061/ex_974537.htm
- AXT Inc. (SEC), "Form 8-K (Coherent 6-inch InP agreement)", 2026-07-02. https://www.sec.gov/Archives/edgar/data/0001051627/000143774926022557/axti20260630_8k.htm
- AXT Inc. (SEC), "Form 8-K (Lumentum capacity reservation)", 2026-07. https://www.sec.gov/Archives/edgar/data/0001051627/000143774926024883/axti20260715_8k.htm
- AXT Inc. (SEC), "Form 10-Q Q2 2026", 2026. https://www.sec.gov/Archives/edgar/data/0001051627/000143774926027677/axti20260630_10q.htm
- AXT Inc. (SEC), "Form 424B5 prospectus supplement", 2026-04. https://www.sec.gov/Archives/edgar/data/0001051627/000121390026046176/ea0287123-424b5_axtinc.htm
- Business Wire, "AXT Inc. Announces Third Quarter 2025 Financial Results", 2025-10-30. https://www.businesswire.com/news/home/20251030779326/en/axt-inc.-announces-third-quarter-2025-financial-results/
- Business Wire, "AXT Inc. Announces Fourth Quarter and Fiscal Year 2025 Financial Results", 2026-02-19. https://www.businesswire.com/news/home/20260219561660/en/AXT-Inc.-Announces-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results
- Quartr, "AXT Inc Q3 2025 event", 2025-10-30. https://quartr.com/events/axt-inc-axti-q3-2025_3seB4owB
- MarketBeat, "AXT Issues Q3 2026 Earnings Guidance", 2026-07-30. https://www.marketbeat.com/instant-alerts/axt-nasdaqaxti-issues-q3-2026-earnings-guidance-2026-07-30/
- MarketBeat, "AXT Q2 Earnings Call Highlights", 2026-07-30. https://www.marketbeat.com/instant-alerts/axt-q2-earnings-call-highlights-2026-07-30/
- MarketBeat, "AXT Inc Q1 2026 earnings report", 2026-04-30. https://www.marketbeat.com/earnings/reports/2026-4-30-axt-inc-stock/
- Motley Fool, "AXT (AXTI) Q2 2026 Earnings Call Transcript", 2026-08. https://www.fool.com/earnings/call-transcripts/2026/08/03/axt-axti-q2-2026-earnings-call-transcript/
- Semiconductor Today, "AXT and Lumentum capacity reservation", 2026-07-30. https://semiconductor-today.com/news_items/2026/jul/axt-lumentum-300726.shtml
- Zacks, "AXT's InP demand is surging: can it become a long-term growth driver", 2026-08 (approx.). https://www.zacks.com/stock/news/2977127/axts-inp-demand-is-surging-can-it-become-a-long-term-growth-driver
- Eastern Progress (Zacks syndication), "AXTI Q2 earnings beat on record InP demand", 2026-07/08. https://www.easternprogress.com/axti-q2-earnings-beat-on-record-inp-demand-revenues-rise-y-y/article_c6eeb316-3732-56b0-9792-583786bf08e3.html
- Global Semi Research (Substack), "China's indium phosphide surge", 2026 (unverified). https://globalsemiresearch.substack.com/p/chinas-indium-phosphide-surge
- TrendForce, "JX Advanced Metals to invest JPY120B through FY2030, expand InP capacity up to 10x as CPO demand accelerates", 2026-06-16. https://www.trendforce.com/news/2026/06/16/news-jx-advanced-metals-to-invest-jpy-120b-through-fy2030-expand-inp-capacity-up-to-10x-as-cpo-demand-accelerates/
- TIKR, "AXT stock fell 10% in a day even as analysts more than doubled their 2027 revenue estimates", 2026-10-09. https://www.tikr.com/blog/axt-stock-fell-10-in-a-day-even-as-analysts-more-than-doubled-their-2027-revenue-estimates-heres-where-the-stock-could-go
- TIKR, "AXTI stock jumped 11% yesterday: the index nod wasn't the whole story", 2026-09. https://www.tikr.com/zh/blog/axti-stock-jumped-11-yesterday-the-index-nod-wasnt-the-whole-story
- Motley Fool, "Coherent (COHR) Q4 2026 Earnings Call Transcript", 2026-08. https://www.fool.com/earnings/call-transcripts/2026/08/19/coherent-cohr-q4-2026-earnings-call-transcript/
- Fastmarkets, "China suspends export prohibition on superhard materials to US", 2025-11-09. https://fastmarkets.com/insights/china-suspends-export-prohibition-on-superhard-materials-us
- Barchart / AXT press release, "AXT announces closing of public offering of common stock and full exercise of underwriters' option", 2026-04-22. https://www.barchart.com/story/news/36832772/axt-announces-closing-of-public-offering-of-common-stock-and-full-exercise-of-underwriters-option-to-purchase-additional-shares
- Interactive Brokers MCP, "AXTI price snapshot (contract 4726868)", 2026-10-15. no public URL (IBKR MCP data)

**Deep dive: POET**

- POET Technologies (SEC EDGAR), "Form 6-K Ex.99.1 - Q2 2026 results", 2026-08-13. https://www.sec.gov/Archives/edgar/data/0001437424/000117184326005485/exh_991.htm
- POET Technologies via Barchart, "POET Technologies Reports Second Quarter 2026 Results, Revenue Up 112% Year-Over-Year", 2026-08-13. https://www.barchart.com/story/news/4207823/poet-technologies-reports-second-quarter-2026-results-revenue-up-112-year-over-year-in-sixth-consecutive-quarter-of-sequential-growth
- POET Technologies, "POET Technologies Reports Fourth Quarter 2025 Financial Results", 2026-04-01 (approx.). https://www.poet-technologies.com/news/poet-technologies-reports-fourth-quarter-2025-financial-results
- POET Technologies, "POET Technologies Provides Purchase Order Update", 2026-04-27. https://poet-technologies.com/news/poet-technologies-provides-purchase-order-update
- Sherwood News, "Marvell cancels order with POET citing breach of confidentiality", 2026-04. https://sherwood.news/markets/marvell-cancels-order-with-poet-citing-breach-of-confidentiality/
- Motley Fool, "POET Technologies stock crashed after Marvell cancellation", 2026-04-27. https://www.fool.com/investing/2026/04/27/poet-technologies-stock-crashed-after-marvell-canc/
- POET Technologies via Barchart, "POET Technologies Recaps Highlights of CEO's Update on Commercial Activities and Provides Results of 2026 AGM", 2026-06-30. https://www.barchart.com/story/news/3052173/poet-technologies-recaps-highlights-of-ceos-update-on-commercial-activities-and-provides-results-of-2026-agm
- POET Technologies (SEC EDGAR), "Form 6-K - Lumilens agreement", 2026-05-14. https://www.sec.gov/Archives/edgar/data/0001437424/000117184326003413/exh_991.htm
- POET Technologies, "POET Technologies Secures Financing of US$400 Million in a Registered Direct Offering", 2026-05-15. https://poet-technologies.com/news/poet-technologies-secures-financing-of-us-400-million-in-a-registered-direct-offering-of-common-shares-and-warrant
- POET Technologies, "POET Technologies and Sivers Semiconductors Collaborate on External Light Sources for Co-Packaged Optics", 2025-09-29. https://www.poet-technologies.com/news/poet-technologies-and-sivers-semiconductors-collaborate-on-external-light-sources-for-co-packaged-optics-and-next-generation-ai-market
- POET Technologies, "POET to Demonstrate Hybrid Laser and Next-Generation High-Powered Light Sources at OFC", 2026-03-10. https://www.poet-technologies.com/news/poet-to-demonstrate-extraordinary-hybrid-laser-and-next-generation-high-powered-light-sources-for-ai-applications-at-ofc-conference
- POET Technologies, "POET Technologies Receives $5 Million Production Order for 800G Optical Engines", 2025-10-22. https://www.poet-technologies.com/news/poet-technologies-receives-5-million-production-order-for-800g-optical-engines
- StockAlarm, "POET analyst estimates", 2026-10-15 (accessed). https://pro.stockalarm.io/quote/POET/analysts
- TickFlow, "POET forecast", 2026-10-15 (accessed). https://tickflow.io/stock/POET/forecast
- AlphaQuery, "POET quarterly common shares outstanding", 2026-10-15 (accessed). https://www.alphaquery.com/stock/POET/fundamentals/quarterly/common-shares-outstanding
- Motley Fool, "Why POET Technologies stock keeps falling", 2026-05-29. https://fool.com/investing/2026/05/29/why-poet-technologies-stock-keeps-falling/
- Trading-Treff, "POET Technologies Aktie: Auftragsstopp nach Kapazitätsgrenze (unverified)", 2026-06/07 (approx.). https://trading-treff.de/wirtschaft/poet-technologies-aktie-auftragsstopp-nach-kapazitaetsgrenze

**Deep dive: TSM**

- TSMC (SEC Form 6-K), "3Q26 Earnings Release", 2026-10-15. https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm
- TSMC (SEC Form 6-K), "2Q26 Earnings Release", 2026-07. https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000451/a2q26e_withguidancexfinal.htm
- TrendForce, "TSMC 2Q26 net income soars 77% YoY; gross margin 67.7%", 2026-07-16. https://www.trendforce.com/news/2026/07/16/news-tsmc-2q26-net-income-soars-77-yoy-to-nt706-56b-record-eps-nt27-25-gross-margin-beats-forecast-at-67-7/
- Investing.com, "Earnings call transcript: TSMC beats Q3 2026 estimates as stock slips", 2026-10-15. https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695
- BigGo Finance, "TSMC Q3-26 call summary", 2026-10-15. https://finance.biggo.com/news/US_TSM_2026-10-15
- MarketBeat, "Taiwan Semiconductor Manufacturing Q3 earnings call highlights", 2026-10-15. https://www.marketbeat.com/instant-alerts/transcript-taiwan-semiconductor-manufacturing-q3-earnings-call-highlights-2026-10-15/
- TrendForce, "TSMC unveils custom C-HBM4E details; N3P logic dies", 2025-12-01. https://www.trendforce.com/news/2025/12/01/news-tsmc-unveils-custom-c-hbm4e-details-n3p-logic-dies-reportedly-target-2x-efficiency-gain/
- TrendForce, "Micron: TSMC to make HBM4E logic base dies", 2026-05. https://www.trendforce.com/news/?p=58045
- TrendForce, "SK hynix reportedly weighs Intel for HBM4E base dies amid TSMC cost pressure and supply diversification", 2026-08-31. https://trendforce.com/news/2026/08/31/news-sk-hynix-reportedly-weighs-intel-for-hbm4e-base-dies-amid-tsmc-cost-pressure-and-supply-diversification
- Herald Business, "SK hynix weighs Intel Foundry for HBM4E base dies (date unverified)", 2026-08. https://biz.heraldcorp.com/article/10857005
- Seoul Economic Daily, "SK hynix teams up with TSMC on HBM4E, betting on 3nm process", 2026-04-18. https://en.sedaily.com/technology/2026/04/18/sk-hynix-teams-up-with-tsmc-on-hbm4e-betting-on-3nm-process
- Silicon Analysts, "TSMC 1Q26 earnings analysis", 2026-04-16. https://siliconanalysts.com/analysis/tsmc-1q26-earnings
- FourWeekMBA, "Nvidia NVHBM moves memory control into the HBM base die", 2026-09-30. https://fourweekmba.com/ai-nvidia-nvhbm-moves-memory-control-into-the-hbm-base-die/
- TechRadar, "Micron wants a bigger slice of the $100 billion HBM market with HBM4 and HBM4E", date not verified. https://www.techradar.com/pro/micron-wants-a-bigger-slice-of-the-usd100-billion-hbm-market-with-its-2026-bound-hbm4-and-hbm4e-memory-solutions
- Taiwan News, "TSMC customer concentration per annual filing (date unverified)", 2026. https://www.taiwannews.com.tw/news/6310676
- VectorShift, "TSMC Q4-25 earnings summary", 2026-01-15. https://vectorshift.ai/research/companies/taiwan-semiconductor-manufacturing-co/earnings/2025-q4
- StockAnalysis, "TSM forecast", 2026-10-15 (accessed). https://stockanalysis.com/stocks/tsm/forecast/
- Admiral Markets, "TSMC earnings Q3 2026 preview", 2026-10. https://admiralmarkets.com/analytics/traders-blog/tsmc-earnings-q3-2026-preview
- Yahoo Finance, "TSMC (TSM) gets price target (JPMorgan)", 2026-01. https://nz.finance.yahoo.com/news/tsmc-tsm-gets-price-target-210710185.html
- GuruFocus, "Citi analysts project over 40% revenue growth for TSMC by 2027", 2026-10-07. https://www.gurufocus.com/news/9114529/tsm-citi-analysts-project-over-40-revenue-growth-for-tsmc-by-2027
- MarketBeat, "Erste Group forecast for TSM FY2026 earnings", 2026-10-13. https://www.marketbeat.com/instant-alerts/estimates-what-is-erste-group-banks-forecast-for-tsm-fy2026-earnings-2026-10-13/
- Gigazine, "TSMC price hike reports", 2026-07-22. https://gigazine.net/gsc_news/en/20260722-tsmc-price-hike/
- Astera Labs (SEC), "Form 10-K FY2025", 2026-02. https://www.sec.gov/Archives/edgar/data/1736297/000173629726000010/alab-20251231.htm
- Naddod, "Broadcom Tomahawk Ultra: new chip for scale-up Ethernet", 2025-07 (approx.). https://www.naddod.com/ja/blog/broadcom-tomahawk-ultra-new-chip-for-scale-up-ethernet
- Reuters via Yahoo Finance, "Taiwan says US has no timetable on chip tariffs", 2026-05-28. https://finance.yahoo.com/economy/policy/articles/taiwan-says-us-no-timetable-055911200.html
- TickerLeague, "TSM P/E ratio", 2026-06. https://tickerleague.com/companies/TSM/financials/pe-ratio

**Deep dive: FORM**

- FormFactor / SEC 8-K Ex.99.01, "FormFactor, Inc. Reports 2026 Second Quarter Results", 2026-07-29. https://www.sec.gov/Archives/edgar/data/0001039399/000103939926000030/ex9901-earningsreleasexq226.htm
- FormFactor / SEC 8-K Ex.99.01, "FormFactor, Inc. Reports 2026 First Quarter Results", 2026-04-29. https://www.sec.gov/Archives/edgar/data/0001039399/000103939926000020/ex9901-earningsreleasexq126.htm
- FormFactor / SEC 8-K Ex.99.01, "FormFactor, Inc. Reports 2025 Third Quarter Results", 2025-10-29. https://www.sec.gov/Archives/edgar/data/1039399/000103939925000110/ex9901-earningsreleasexq325.htm
- FormFactor, "FormFactor, Inc. Reports 2025 Fourth Quarter Results", 2026-02-04. https://investors.formfactor.com/news-releases/news-release-details/formfactor-inc-reports-2025-fourth-quarter-results/
- FormFactor / SEC, "FormFactor FY2025 Form 10-K (fiscal year ended 2025-12-27)", 2026-02. https://www.sec.gov/Archives/edgar/data/1039399/000103939926000009/form-20251227.htm
- FormFactor, "FormFactor to Host Upcoming Investor Day", 2026-03-05. https://investors.formfactor.com/news-releases/news-release-details/formfactor-host-upcoming-investor-day
- FormFactor via Finviz, "FormFactor to Announce Third Quarter 2026 Financial Results on October 28th", 2026-10-07. https://finviz.com/news/400007/formfactor-to-announce-third-quarter-2026-financial-results-on-october-28th
- Investing.com, "Earnings call transcript: FormFactor beats Q2 2026 estimates", 2026-07-29. https://www.investing.com/news/transcripts/earnings-call-transcript-formfactor-beats-q2-2026-estimates-shares-jump-after-hours-93CH-4821881
- MarketBeat, "FormFactor Q2 earnings call highlights", 2026-07-29. https://www.marketbeat.com/instant-alerts/formfactor-q2-earnings-call-highlights-2026-07-29/
- MarketBeat, "FormFactor Q1 2026 earnings call transcript", 2026-04-29. https://www.marketbeat.com/earnings/reports/2026-4-29-formfactor-inc-stock/
- MarketBeat, "Northland Securities estimates FormFactor Q3 earnings", 2026-08-05. https://www.marketbeat.com/instant-alerts/northland-securities-estimates-formfactor-q3-earnings-2026-08-05/
- StatementDog, "FORM Q2-26 earnings call summary", 2026-07-29. https://statementdog.com/analysis/FORM/earnings_calls/316581
- Insider Monkey, "FormFactor Q4 2025 earnings call transcript", 2026-02-04. https://www.insidermonkey.com/blog/formfactor-inc-nasdaqform-q4-2025-earnings-call-transcript-1689489/
- ROIC.ai, "FormFactor Q4-25 transcript", 2026-02. https://www.roic.ai/quote/FORM/transcripts/2025-year/4-quarter
- stock3, "Nvidia, SK hynix: 40% des Umsatzes dieser Aktie", 2026 (exact date unverified). https://stock3.com/news/nvidia-sk-hynix-40-des-umsatzes-dieser-aktie-17050837
- DigiTimes, "Micronics Japan raises R&D for next-gen HBM and logic probe cards", 2025-12-01. https://www.digitimes.com/news/a20251201PD210.html
- Bloomberg Law, "MPI Corp says Italian semiconductor firm infringes patents", 2026-04. https://news.bloomberglaw.com/ip-law/mpi-corp-says-italian-semiconductor-firm-infringes-patents
- AnandTech, "TSMC readies HBM4 base dies at 12nm and 5nm", 2024-05. https://ns2.anandtech.com/print/21395/tsmc-readies-hbm4-base-dies-at-12nm-and-5nm
- PitchBook, "FormFactor company profile", 2026-08-04. https://pitchbook.com/profiles/company/41514-22
- vcpscanner, "FORM estimates", undated. https://www.vcpscanner.com/valuation/form/estimates

**Deep dive: TER**

- SEC, "Teradyne 8-K Ex.99.1, Q2-26 results", 2026-07-28. https://www.sec.gov/Archives/edgar/data/0000097210/000119312526321933/ter-ex99_1.htm
- SEC, "Teradyne 8-K Ex.99.1, Q1-26 results", 2026-04-28. https://www.sec.gov/Archives/edgar/data/0000097210/000119312526188706/ter-ex99_1.htm
- SEC, "Teradyne Form 10-K FY2025", 2026-02. https://www.sec.gov/Archives/edgar/data/97210/000119312526059002/ter-20251231.htm
- Business Wire, "Teradyne Magnum 7H release", 2025-08-04. https://www.businesswire.com/news/home/20250804458862/en
- Teradyne, "Magnum 7H product page", undated. https://www.teradyne.com/products/magnum-7h/
- Teradyne IR, "UltraFLEXplus UltraPort-PCIe6 press release", unverified. https://investors.teradyne.com/news-events/press-releases/detail/447
- MarketBeat, "Teradyne Q2-26 earnings call transcript", 2026-07-29. https://www.marketbeat.com/earnings/reports/2026-7-29-teradyne-inc-stock/
- MarketBeat, "Teradyne Q2 earnings call highlights", 2026-07-29. https://www.marketbeat.com/instant-alerts/teradyne-q2-earnings-call-highlights-2026-07-29/
- Quartr, "Teradyne Q2 2026 event", 2026-07. https://quartr.com/events/teradyne-inc-ter-q2-2026_3sxGdnf8
- MarketBeat, "Northland Securities raises earnings estimates for Teradyne", 2026-08-03. https://www.marketbeat.com/instant-alerts/northland-securities-raises-earnings-estimates-for-teradyne-2026-08-03/
- Trefis, "Teradyne looks expensive until you price the AI chips it has not tested yet", 2026-09-15. https://www.trefis.com/stock/ter/articles/615395/teradyne-looks-expensive-until-you-price-the-ai-chips-it-has-not-tested-yet/2026-09-15
- Barchart, "What to expect from Teradyne's next quarterly earnings report", unverified. https://www.barchart.com/story/news/3288580/what-to-expect-from-teradynes-next-quarterly-earnings-report
- TickFlow, "TER forecast", unverified. https://tickflow.io/stock/TER/forecast
- DigiTimes, "tester tag page", 2026-07-30. https://www.digitimes.com/tag/tester/0012941.html
- Xenospectrum, "China memory testing and HBM equipment (citing ETNews)", 2026 (unverified). https://xenospectrum.com/en/china-memory-testing-hbm-equipment/
- AInvest, "The memory boom's real winner", 2026 (unverified). https://www.ainvest.com/news/memory-boom-real-winner-doesn-memory-2608/
- Business Wire, "Teradyne Q3-2025 results date announcement", 2025-10-15. https://www.businesswire.com/news/home/20251015760992/en
- Interactive Brokers, "Market-data snapshot (no public URL)", 2026-10-15. n/a
- Local research file, "N1 niche file: research/niche-growth-2027-2030/README.md section 4.1", 2026-10. n/a (local file)

**Chain map: Merchant HBM4/4E logic base dies**

- Prior report deep dive (local file), "Merchant HBM logic base dies, L15 deep dive", 2026-10-14. file:///tmp/claude-0/-home-user-my-repo/350fdcc3-501b-5ea9-949a-10bbbedab992/scratchpad/deep/L15.md
- Counterpoint Research, "The $Trillion Bottleneck: NVIDIA's NVHBM and the Fight for the Base Die", 2026-09-01. https://counterpointresearch.com/en/reports/the-trillion-dollar-bottleneck-nvidias-nvhbm-fight-for-base-die
- Counterpoint Research, "The trillion dollar bottleneck: Nvidia's NVHBM fight for base die (blog)", 2026-09. https://counterpointresearch.com/en/insights/the-trillion-dollar-bottleneck-nvidias-nvhbm-fight-for-base-die-blog
- Profesional Review, "HBM4E: SK hynix and Intel Foundry", 2026-09-01. https://www.profesionalreview.com/2026/09/01/hbm4e-sk-hynix-intel-foundry-memorias/
- Marvell, "Marvell Announces Breakthrough Custom HBM Compute Architecture to Optimize Cloud AI Accelerators", 2024-12-10. https://investor.marvell.com/news-events/press-releases/detail/117/marvell-announces-breakthrough-custom-hbm-compute-architecture-to-optimize-cloud-ai-accelerators
- MarketBeat, "Marvell Technology earnings call transcript", 2025-05-29. https://www.marketbeat.com/earnings/reports/2025-5-29-marvell-technology-group-ltd-stock
- MarketBeat, "Camtek Q1 2026 earnings call transcript", 2026-05-12. https://www.marketbeat.com/earnings/reports/2026-5-12-camtek-ltd-stock/
- StatementDog, "Camtek (CAMT) 2026 Q2 earnings call transcript", 2026-08. https://statementdog.com/analysis/CAMT/earnings_calls/317605
- Onto Innovation / SEC, "8-K Exhibit 99.1 (Q4-25 results; HBM VPA >$240M)", 2026-02. https://www.sec.gov/Archives/edgar/data/704532/000119312526059380/onto-ex99_1.htm
- MarketBeat, "Onto Innovation Q2 earnings call highlights", 2026-08-08. https://www.marketbeat.com/instant-alerts/onto-innovation-q2-earnings-call-highlights-2026-08-08/
- Nova, "Nova WMC expanding adoption across the most advanced packaging processes", 2026-07-02. https://www.novami.com/investors/press-releases/nova-wmc-expanding-adoption-across-the-most-advanced-packaging-processes/
- Nasdaq / Zacks, "KLA gains from advanced packaging: can it outpace ONTO and AMAT?", 2026. https://www.nasdaq.com/articles/kla-gains-advanced-packaging-can-it-outpace-amat
- MarketBeat, "Lam Research Q2 (FY26) earnings call highlights", 2026-01-28. https://www.marketbeat.com/instant-alerts/lam-research-q2-earnings-call-highlights-2026-01-28/
- Zacks, "Applied Materials advanced packaging >50% growth in CY2026 (URL as returned by search; malformed)", 2026. https://www.zacks.com/stock/news/2972562/{https:/www.zackstrade.com/2019-1-dollar}
- Business Wire / Rambus, "Rambus sets new benchmark for AI memory performance with HBM4E controller IP", 2026-03-04. https://www.businesswire.com/news/home/20260304595773/en/Rambus-Sets-New-Benchmark-for-AI-Memory-Performance-with-Industry-Leadi
- Guru3D, "Rambus ships HBM4E controller IP rated for 16 Gbps per pin (SoC or custom base die)", 2026-03. https://www.guru3d.com/story/rambus-ships-hbm4e-controller-ip-rated-for-16-gbps-per-pin/
- Nasdaq, "Can AEHR turn AI processor tests into long-term revenue streams?", 2026. https://www.nasdaq.com/articles/can-aehr-turn-ai-processor-tests-long-term-revenue-streams
- Broadcom, "Broadcom delivers industry's first 3.5D F2F technology for AI XPUs", 2024-12-05. https://investors.broadcom.com/news-releases/news-release-details/broadcom-delivers-industrys-first-35d-f2f-technology-ai-xpus
- TechRadar, "SK hynix teams up with TSMC to advance HBM development (HBM4 base-die partnership)", 2024-04. https://www.techradar.com/pro/samsungs-archrival-strikes-crucial-partnership-with-nvidias-closest-ally-to-deliver-key-next-gen-memory-sk-hynix-teams-up-with-tsmc-to-advance-hbm-development-but-could-this-move-encourage-tsmc-to-become-like-intel
- Asia Economy, "[Chiptalk] TSMC holding the fate of Samsung and SK HBM... base die rising as a power player", 2024-11-28. https://view.asiae.co.kr/en/article/2024112815213620837
- heise online, "Nvidia GTC 2026 roadmap (Feynman custom HBM)", 2026-03. https://heise.de/-11214678
- KGI, "TSMC (2330 TT) 1Q26 note", 2026-04-16. https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/tsmc_2330-tt_16042026e.pdf

**Chain map: Ultra-high-power InP CW lasers + ELS modules for CPO/NPO**

- Lumentum IR, "Lumentum Announces Fourth Quarter and Full Fiscal Year 2026 Results", 2026-08-11. https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Fourth-Quarter-and-Full-Fiscal-Year-2026-Results/default.aspx
- Zacks, "Lumentum Q4 earnings call focuses on AI optics, OCS, NPO ramps", 2026-08-11. https://www.zacks.com/stock/news/2973530/lumentum-q4-earnings-call-focuses-on-ai-optics-ocs-npo-ramps
- Coherent, "Fourth quarter and fiscal year 2026 results", 2026-08-12. https://www.coherent.com/news/press-releases/fourth-quarter-and-fiscal-year-2026-results
- Futurum, "Coherent Q4 FY 2026 Earnings: 1.6T Transceivers Ramp, CPO Revenue Approaches", 2026-08. https://futurumgroup.com/insights/coherent-q4-fy-2026-earnings-1-6t-transceivers-ramp-cpo-revenue-approaches/
- Futurum, "Coherent's $23 Billion Growth Opportunity Lifted by NVIDIA's Optical Ambitions", 2026. https://futurumgroup.com/insights/coherents-23-billion-growth-opportunity-lifted-by-nvidias-optical-ambitions/
- Barchart (AOI PR), "AOI introduces new ultra high power semiconductor laser to support silicon photonics and CPO", 2025-12-18. https://www.barchart.com/story/news/36692023/aoi-introduces-new-ultra-high-power-semiconductor-laser-to-support-silicon-photonics-and-cpo
- GuruFocus, "Applied Optoelectronics Q2 2026 earnings call highlights", 2026-08-06. https://www.gurufocus.com/news/9015363/applied-optoelectronics-inc-aaoi-q2-2026-earnings-call-highlights-record-revenue-and-aidriven-growth-propel-return-to-profitability
- LEDinside, "Veeco Announces $250 Million+ in Equipment Orders for Manufacturing Indium Phosphide Lasers", 2026-05-26. https://www.ledinside.com/news/2026/08/2026_05_26_01
- Axcelis / SEC, "Form 10-Q for period ended 2026-06-30 (Veeco merger status)", 2026-08. https://www.sec.gov/Archives/edgar/data/0001113232/000110465926091999/acls-20260630x10q.htm
- Aehr Test Systems, "Aehr receives follow-on order for wafer-level burn-in systems powering AI optical I/O", 2026-03-03. https://www.aehr.com/2026/03/aehr-receives-follow-on-order-for-fully-automated-wafer-level-burn-in-systems-powering-ai-optical-i-o-and-data-center-interconnects/
- Fabrinet / SEC, "Form 10-K FY2026", 2026-08. https://www.sec.gov/Archives/edgar/data/0001408710/000140871026000028/fn-20260626.htm
- Nasdaq/Zacks, "FN's Optical Communications Revenues Accelerate: What's Ahead?", 2026. https://www.nasdaq.com/articles/fns-optical-communications-revenues-accelerate-whats-ahead
- Cailian Press, "USI subsidiary releases UHP ELSFP series (Chinese)", 2026-08-28 (year inferred). https://www.cls.cn/detail/2467214
- PR Newswire Asia, "USI (Shanghai 601231) releases incl. EugenLight controlling-stake acquisition", 2026-01. https://en.prnasia.com/ticker/Shanghai+601231_0.shtml
- UAnalyze, "ELSFP supply chain", 2026-09. https://uanalyze.com.tw/articles/8331255940
- Corning, "What is Co-Packaged Optics?", 2026. https://www.corning.com/optical-communications/worldwide/en/home/the-signal-network-blog/what-is-co-packaged-optics.html
- Borecraft, "Nvidia's fiber optics and copper partnership", 2026-05-12. https://borecraft.com/2026/05/12/nvidias-fiber-optics-and-copper-partnership/
- The Next Platform, "The third time will be the charm for Broadcom switch co-packaged optics", 2025-10-17. https://www.nextplatform.com/2025/10/17/the-third-time-will-be-the-charm-for-broadcom-switch-co-packaged-optics/
- Broadcom, "Enabling AI infrastructure: Davisson briefing", 2025. https://docs.broadcom.com/doc/enabling-ai-infrastructure-davisson-briefing
- EE Times Japan, "FUJI, Broadcom and Celestica CPO assembly evaluation", 2026-10-09. https://eetimes.itmedia.co.jp/ee/articles/2610/09/news046.html
- NVIDIA, "Scaling AI factories with co-packaged optics for better power efficiency", 2025. https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/
- 10jqka, "Nvidia CPO volume production", 2026-08-18. https://stock.10jqka.com.cn/20260818/c679027648.shtml
- Cignal AI, "ELSFP module market to exceed $1.5 billion by 2030", 2026-05. https://cignal.ai/2026/05/elsfp-module-market-to-exceed-1-5-billion-by-2030/
- TE Connectivity, "Support for 102.4T CPO systems with ELSFP", 2026. https://www.te.com/en/products/connectors/pluggable-connectors-cages/intersection/elsfp.html
- Converge Digest, "Quantifi Photonics intros ELSFP for CPO and PIC testing", 2026-01. https://convergedigest.com/quantifi-photonics-intros-elsfp-for-cpo-and-pic-testing/
- Teradyne / SEC, "Form 10-Q (Quantifi purchase accounting)", 2026. https://www.sec.gov/Archives/edgar/data/0000097210/000119312526201058/ter-20260329.htm
- SEMICON Taiwan, "Startups stage 2026: LiVe Optronics", 2026. https://semicontaiwan.org/en/startups_stage2026_LiVeOptronics
- Prior report, "Deep dive L01 (niche sizing, supplier shares)", 2026-10. local file: /tmp/claude-0/-home-user-my-repo/350fdcc3-501b-5ea9-949a-10bbbedab992/scratchpad/deep/L01.md

**Chain map: Merchant scale-up switch silicon (non-NVLink XPU domains)**

- Prior report (local), "L07 deep dive: Merchant scale-up switch silicon for non-NVLink XPU domains", 2026-10. file:///tmp/claude-0/-home-user-my-repo/350fdcc3-501b-5ea9-949a-10bbbedab992/scratchpad/deep/L07.md
- Astera Labs, "Astera Labs Broadens Scorpio X-Series Smart Fabric Switch Roadmap", 2026-01-22. https://www.asteralabs.com/news/astera-labs-broadens-scorpio-x-series-smart-fabric-switch-roadmap-to-address-expanding-scale-up-market-opportunities/
- TipRanks, "Astera Labs Grants Amazon Strategic Performance-Based Warrant Investment", 2026-02. https://www.tipranks.com/news/company-announcements/astera-labs-grants-amazon-strategic-performance-based-warrant-investment
- Business News Today, "Astera Labs Scorpio ramp tested by the Amazon warrant agreement", 2026 (date unverified). https://business-news-today.com/astera-labs-nasdaq-alab-scorpio-ramp-tested-by-the-amazon-warrant-agreement/
- MarketBeat, "Astera Labs Q4 Earnings Call Highlights", 2026-02-10. https://www.marketbeat.com/instant-alerts/astera-labs-q4-earnings-call-highlights-2026-02-10/
- MarketBeat, "Astera Labs Touts AI Infrastructure Tailwinds at Morgan Stanley Conference", 2026-03-03. https://www.marketbeat.com/instant-alerts/astera-labs-touts-ai-infrastructure-tailwinds-highlights-scorpio-switch-ramp-at-morgan-stanley-conference-2026-03-03/
- Converge Digest, "Broadcom ships Tomahawk Ultra to power AI scale-up", 2025-07. https://convergedigest.com/broadcom-ships-tomahawk-ultra-to-power-ai-scale-up/
- AMD, "AMD and Celestica Announce Collaboration to Advance the Next Era of AI with Helios Rack-Scale AI Platform", 2026-03-16. https://www.amd.com/en/newsroom/press-releases/2026-3-16-amd-and-celestica-announce-collaboration-to-a.html
- deluisio.com, "204.8T of switching capacity per tray in the AMD Helios AI rack (HPE Juniper QFX5252)", 2026-06-19. https://deluisio.com/technology/2026/06/19/204-8t-of-switching-capacity-per-tray-in-the-amd-helios-ai-rack/
- The Register, "HPE AMD Helios racks", 2025-12-02. https://www.theregister.com/2025/12/02/hpe_amd_helios_racks/
- Yahoo Finance, "Marvell Technology Q4 Earnings Call", 2026-03. https://finance.yahoo.com/news/marvell-technology-q4-earnings-call-031005384.html
- TheStreet Pro, "Marvell makes another move to position for what's ahead (XConn ~$100M FY28)", 2026-01. https://pro.thestreet.com/portfolio/marvell-makes-another-move-to-position-for-whats-ahead
- Pulse2, "Marvell: Data Center Revenue Growth Accelerates to 46%, Record $2.74 Billion Quarter", 2026-08-27. https://pulse2.com/marvell-data-center-revenue-growth-accelerates-to-46-as-ai-demand-drives-record-2-74-billion-quarter/
- Mitrade, "Credo (CRDO) Fiscal Q1 2027 Earnings Call: Revenue Jumps 115%", 2026-09-02. https://www.mitrade.com/insights/news/live-news/article-0-2050680-20260902
- Crypto Briefing, "Credo reports Q1 FY27 earnings, guides optical revenue above $600M", 2026-09. https://cryptobriefing.com/credo-q1-fy27-earnings-optical-revenue/
- Arista Networks, "Arista Announces Rack-Scale Architectures for Scale-Up and Scale-Out AI Fabrics", 2026-10-07. https://www.arista.com/en/company/news/press-release/24818-pr-20261007
- Network World, "Arista steps up its Ethernet challenge to Nvidia's AI scale-up networking fabric", 2026-10. https://www.networkworld.com/article/4232036/arista-steps-up-its-ethernet-challenge-to-nvidias-ai-scale-up-networking-fabric.html
- Vectorshift, "Arista Networks Q1-2026 earnings management commentary", 2026-05. https://vectorshift.ai/research/companies/arista-networks/earnings/2026-q1
- Cisco, "Cisco Announces New Silicon One G300 Advanced Systems and Optics", 2026-02-10. https://investor.cisco.com/files/doc_news/Cisco-Announces-New-Silicon-One-G300-Advanced-Systems-and-Optics-to-Power-and-Scale-AI-Data-Centers-for-the-Agentic-Era-2026.pdf
- Cisco, "Cisco Advances Scalability and Openness at OCP 2026", 2026-10-12. https://s21.q4cdn.com/812015656/files/doc_news/Cisco-Advances-Scalability-and-Openness-at-OCP-2026-2026.pdf
- Embedded.com, "Microchip Launches Industry's First 3nm PCIe Gen 6 Switches for AI and HPC", 2025-10. https://www.embedded.com/?p=4498707
- Bullfincher, "Microchip FY2026 Q2 earnings call", 2025-11. https://bullfincher.io/companies/microchip-technology-incorporated/earnings-call/fy2026-q2
- Futurum Group, "Teradyne Q2 FY 2026 Doubles Semiconductor Test Revenue on AI Compute and Memory Demand", 2026-07-29. https://futurumgroup.com/insights/teradyne-q2-fy-2026-doubles-semiconductor-test-revenue-on-ai-compute-and-memory-demand/
- EE Journal, "Synopsys Announces Industry's First Ultra Ethernet and UALink IP Solutions", 2024-12. https://eejournal.com/industry_news/synopsys-announces-industrys-first-ultra-ethernet-and-ualink-ip-solutions-to-connect-massive-ai-accelerator-clusters
- Synopsys, "UALink IP product page", 2026 (undated). https://synopsys.com/designware-ip/interface-ip/ualink.html
- Cadence (blog), "Industry-first UALink 200G controller and PHY running in 3nm", 2026-04. https://community.cadence.com/cadence_blogs_8/b/data-center/posts/industry-first-ualink-200g-controller-and-phy-running-in-3nm
- Open Compute Project, "Introducing ESUN: Advancing Ethernet for Scale-Up AI Infrastructure at OCP", 2025-10. https://www.opencompute.org/blog/introducing-esun-advancing-ethernet-for-scale-up-ai-infrastructure-at-ocp
- UfiSpace, "Join UfiSpace at OCP Global Summit 2026", 2026-10. https://www.ufispace.com/company/events/join-ufispace-at-ocp-global-summit-2026
- Digitimes, "TSMC shifts part of CoWoS orders to ASE and Amkor (paywalled)", 2026-01-05. https://www.digitimes.com/news/a20260105PD209.html
- AWS, "Trainium3 Architecture (Neuron docs)", 2026. https://awsdocs-neuron.readthedocs-hosted.com/en/v2.28.1/about-neuron/arch/neuron-hardware/trn3-arch.html
- Zaikei, "Trainium4 NVLink Fusion support", 2026-08-28. https://www.zaikei.co.jp/article/20260828/867754.html
- The Register, "Upscale SkyHammer", 2026-01-22. https://www.theregister.com/2026/01/22/upscale_skyhammer_nvidia/
- HPCwire/AIwire, "Cornelis to build scale-up interconnect using UALink and ESUN", 2026-09-14. https://www.hpcwire.com/aiwire/2026/09/14/cornelis-to-build-scale-up-interconnect-using-ualink-and-esun/
- 10jqka, "Centec placement for scale-up switch chips", 2026-09-02. https://stock.10jqka.com.cn/20260902/c679540905.shtml

**False positives**

- Benzinga, "Broadcom and Marvell poised for growth as Nvidia's CPO push faces delays, analyst reveals (BofA on CPO vs pluggables)", 2025-04. https://www.benzinga.com/25/04/44653936/broadcom-and-marvell-poised-for-growth-as-nvidias-cpo-push-faces-delays-analyst-reveals?nid=44665469
- SentiSense, "Aehr Test Systems stock surges 18% on silicon photonics order", 2026-06-17. https://app.sentisense.ai/stories/aehr-test-systems-stock-surges-18-percent-on-silicon-photonics-order-06172026
- Semiconductor Today, "Aehr follow-on production order from lead silicon photonics customer", 2026-08-04. https://semiconductor-today.com/news_items/2026/aug/aehr-040826.shtml
- Trefis, "Does the drop in Credo stock change anything?", 2026-10-13. https://www.trefis.com/articles/618478/does-the-drop-in-credo-stock-change-anything/2026-10-13?.tsrc=rss
- ASML / SEC, "Form 6-K: ASML reports EUR11.7 billion total net sales and EUR5.0 billion net income in Q3 2026", 2026-10-14. https://www.sec.gov/Archives/edgar/data/0000937966/000162828026065813/pressreleasefinancialresul.htm
- ASML, "ASML reports EUR8.8 billion total net sales and EUR2.8 billion net income in Q1 2026 (incl. Q4-25 comparison column)", 2026-04-15. https://www.asml.com/en/news/press-releases/2026/q1-2026-financial-results
- ASML, "ASML reports EUR9.3 billion total net sales and EUR2.9 billion net income in Q2 2026", 2026-07-15. https://www.asml.com/news/press-releases/2026/q2-2026-financial-results
- HPE / SEC, "Form 8-K Ex.99.1: HPE fiscal 2026 third quarter results", 2026-09. https://www.sec.gov/Archives/edgar/data/0001645590/000164559026000078/ex-991x922026x8k.htm
- Constellation Research, "HPE delivers strong Q3, ups fiscal 2026 outlook due to AI demand", 2026-09. https://www.constellationr.com/insights/news/hpe-delivers-strong-q3-ups-fiscal-2026-outlook-due-ai-demand

**Consensus check**

- Yahoo Finance analysis tab (24 analysts; low $2.19B, high $3.68B) [3P]. MarketScreener shows $2,973M. TIKR says 2027 consensus is up 34% since 30-Jun to ~$2.97B., "ALAB consensus revenue, CY2027 (FY = calendar year, ends Dec-2027)", ~2026-10 (the TIKR post cites the 8-Oct-2026 close; Yahoo and MarketScreener snapshot dates unverified). https://www.tikr.com/blog/astera-labs-stock-fell-9-in-a-day-as-an-openai-revenue-report-hit-chip-stocks-heres-where-the-stock-could-go-by-2030
- TIKR (same post, ~$3.83B) and MarketScreener projected income statement (~$3.83B) [3P], "ALAB consensus revenue, CY2028 (FY = calendar year, ends Dec-2028)", ~2026-10 (TIKR post cites the 8-Oct-2026 close). https://ca.marketscreener.com/quote/stock/ASTERA-LABS-INC-167508773/finances/
- Yahoo Finance analysis tab: average $6.32B, 23 analysts, range $5.61-6.95B [3P]. StockAnalysis $6.3B ($5.6-7.2B). Trefis $6.3B (8-Oct, per deep dive)., "LITE consensus revenue, FY2027 (FY ends ~Jun/Jul-2027; Jul-2026 to Jun-2027, ~H2-CY26 + H1-CY27)", Aug-Oct 2026 (after the Q4 FY26 print on 2026-08-11; snapshot dates approximate). https://finance.yahoo.com/quote/LITE/analysis/
- Yahoo Finance analysis tab: average $9.61B, 21 analysts, range $7.25-11.03B [3P]. StockAnalysis $9.84B. TIKR $9,909M., "LITE consensus revenue, FY2028 (FY ends ~Jun/Jul-2028; Jul-2027 to Jun-2028, ~H2-CY27 + H1-CY28)", Aug-Oct 2026 (post-Q4 FY26; snapshot dates approximate). https://stockanalysis.com/stocks/lite/forecast/
- LSEG consensus cited by Reuters (via Yahoo Finance/Qz) at the 6-Oct-2026 Investor Day [3P], "MRVL consensus revenue, CY2027 ≈ FY2028 (FY ends ~29-Jan-2028; Feb-2027 to Jan-2028)", 2026-10-06 (snapshot taken BEFORE the Investor Day raise). https://finance.yahoo.com/markets/stocks/articles/marvell-raises-fiscal-2031-revenue-195457586.html
- UNVERIFIED. No LSEG/FactSet/aggregator 2028 figure found. Placeholder is the midpoint of the deep dive's [E] implied range of $270-290B., "TSM consensus revenue, CY2028 (FY = calendar year)", 2026-10-15 (placeholder). n/a (no source found)
- 24/7 Wall St: analysts forecast FY27 revenue of $173.5B (+64%) and EPS $19.38 [3P; provider not named], "AVGO consensus revenue, CY2027 ≈ FY2027 (FY ends ~1-Nov-2027; Nov-2026 to Oct-2027, leads the calendar year by ~2 months)", 2026-10-02 (post-Q3 FY26 print on 2026-09-02). https://247wallst.com/investing/2026/10/02/prediction-broadcom-stock-could-be-much-higher-by-2027/
- UNVERIFIED revenue consensus. [E] derived from: LSEG FY28 adj. EPS consensus of $25.86 (CNBC, 2026-09-02, pre-print), EPS-implied $225-260B per the deep dive; and a Substack back-out of Street FY28 AI of ~$162B, plus ~$51B non-AI ≈ $213B., "AVGO consensus revenue, CY2028 ≈ FY2028 (FY ends ~Oct-2028; Nov-2027 to Oct-2028)", 2026-09-02 (LSEG EPS); Substack date unverified. https://jpthoughtsandgrowth.substack.com/p/broadcom-consensus-models-the-guidance
- StocksGuide $83.6M [3P]. Other aggregators: Simply Wall St $100M (1 analyst), TickFlow $80M, StocksGuide $102M (deep dive snapshot), another ~$64M., "POET consensus revenue, CY2027 (FY = calendar year)", ~Jun-Jul 2026 (aggregator snapshots ~3-4 months old; before the Q2-26 print on 2026-08-13). https://stocksguide.com/en/forecast/Poet-Technologies-CA73044W3021
- StocksGuide $204M [3P]. Simply Wall St $219M (1 analyst)., "POET consensus revenue, CY2028 (FY = calendar year)", ~Jun-Jul 2026 (snapshots ~3-4 months old; pre-Q2-26). https://simplywall.st/stocks/us/semiconductors/nasdaq-poet/poet-technologies/future

**Financial data**

- TSMC via SEC (Form 6-K), "TSMC 1Q26 earnings release with guidance", 2026-04. https://www.sec.gov/Archives/edgar/data/1046179/000104617926000199/a1q26e_withguidancexfinal.htm
- Broadcom via SEC (8-K Ex.99), "Broadcom Q2 FY2026 financial results", 2026-06. https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000051/avgo-05032026x8kxex99.htm
- Intel / Business Wire, "Intel Reports Second-Quarter 2026 Financial Results", 2026-07-23. https://www.businesswire.com/news/home/20260723707213/en/
- Intel via SEC (Form 10-Q), "Intel 10-Q for quarter ended June 27, 2026", 2026-07. https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000157/intc-20260627.htm
- Intel / Business Wire, "Intel Reports First-Quarter 2026 Financial Results", 2026-04-23. https://www.businesswire.com/news/home/20260423038467/en/Intel-Reports-First-Quarter-2026-Financial-Results
- Micron via SEC (8-K Ex.99.1), "Micron fiscal Q4 2026 press release", 2026-09-30. https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000018/a2026q4ex991-pressrelease.htm
- Micron via SEC (8-K Ex.99.1), "Micron fiscal Q3 2026 press release", 2026-06. https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000013/a2026q3ex991-pressrelease.htm
- Micron (q4cdn), "Micron Fiscal Q4 2026 Earnings Call Prepared Remarks", 2026-09-30. https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf
- Applied Materials via SEC (8-K Ex.99.1), "Applied Materials Q3 2026 earnings release", 2026-08-13. https://www.sec.gov/Archives/edgar/data/0000006951/000162828026056699/exhibit991q32026earningsre.htm
- Applied Materials, "Applied Materials Announces Third Quarter 2026 Results", 2026-08-13. https://www.appliedmaterials.com/us/en/newsroom/press-releases/081326-applied-materials-announces-third-quarter-2026-results.html
- Nasdaq, "Applied Materials Q3 earnings call highlights", 2026-08. https://www.nasdaq.com/articles/applied-materials-q3-earnings-call-highlights
- Lam Research via SEC (8-K Ex.99.1), "Lam Research results for quarter ended June 28, 2026", 2026-07-29. https://www.sec.gov/Archives/edgar/data/0000707549/000070754926000033/lrcx_exhibitx991xq4x2026.htm
- Lam Research via SEC (Form 10-K), "Lam Research FY2026 Form 10-K", 2026-08. https://www.sec.gov/Archives/edgar/data/0000707549/000070754926000037/lrcx-20260628.htm
- Lam Research via SEC (8-K Ex.99.1), "Lam Research results for March 2026 quarter", 2026-04. https://www.sec.gov/Archives/edgar/data/0000707549/000070754926000020/lrcx_exhibitx991xq3x2026.htm
- KLA via SEC (8-K Ex.99.1), "KLA Corporation Reports Fiscal 2026 Fourth Quarter and Full Year Results", 2026-07-28. https://www.sec.gov/Archives/edgar/data/0000319201/000031920126000024/exhibit991earningsrelease7.htm
- TIKR, "KLA Corporation's Q4 earnings hit a record $3.66 billion; the guide points higher still", 2026-07. https://www.tikr.com/blog/kla-corporations-q4-earnings-hit-a-record-3-66-billion-the-guide-points-higher-still
- I-Connect007, "KLA Reports Strong Q4 and FY 2026 Results; Revenue Hits $3.66B", 2026-07. https://iconnect007.com/article/150980/kla-reports-strong-q4-and-fy-2026-results-revenue-hits-366b/150977/aep
- Nasdaq, "Cisco Systems Q4 earnings call highlights", 2026-08-12. https://www.nasdaq.com/articles/cisco-systems-q4-earnings-call-highlights
- MarketBeat, "Cisco Systems Q4 earnings call highlights", 2026-08-12. https://www.marketbeat.com/instant-alerts/cisco-systems-q4-earnings-call-highlights-2026-08-12/
- ITdaily, "Cisco records record fiscal year 2026 with strong growth and AI momentum", 2026-08. https://itdaily.com/news/business/cisco-posts-record-year-in-2026-with-strong-growth-and-ai-momentum/
- Synopsys (press release), "Synopsys Posts Financial Results for Third Quarter Fiscal Year 2026", 2026-08-26. https://news.synopsys.com/2026-08-26-Synopsys-Posts-Financial-Results-for-Third-Quarter-Fiscal-Year-2026
- SEC EDGAR, "Synopsys Form 8-K Ex.99.1 Q3 FY2026", 2026-08-26. https://www.sec.gov/Archives/edgar/data/0000883241/000119312526368620/d157153dex991.htm
- Zacks via Finviz, "Synopsys Q1 Earnings Surpass Estimates, Revenues Rise Y/Y", 2026-02 (approx.). https://finviz.com/news/323508/synopsys-q1-earnings-surpass-estimates-revenues-rise-yy
- SEC EDGAR, "Cadence Form 8-K Ex.99.01 Q2 2026 results", 2026-07-27. https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000089/cdns07272026ex9901.htm
- TIKR, "Cadence's Q2 earnings beat every guidance line; the backlog explains why", 2026-07 (approx.). https://www.tikr.com/blog/cadences-q2-earnings-beat-every-guidance-line-the-backlog-explains-why
- MarketBeat, "Cadence Design Systems Q2 earnings call highlights", 2026-07-27. https://www.marketbeat.com/instant-alerts/cadence-design-systems-q2-earnings-call-highlights-2026-07-27/
- SEC EDGAR, "Corning Form 8-K Ex.99 Q2 2026", 2026-07-28. https://www.sec.gov/Archives/edgar/data/0000024741/000002474126000253/glw-20260728xex99xq22026.htm
- Business Wire, "Corning's Strong Second-Quarter 2026 Financial Results Demonstrate Progress on Recently Upgraded Springboard Plan", 2026-07-28. https://www.businesswire.com/news/home/20260727590976/en/Cornings-Strong-Second-Quarter-2026-Financial-Results1-Demonstrate-Progress-on-Recently-Upgraded-Springboard-Plan
- SEC EDGAR, "Corning Form 8-K Ex.99.1 Q1 2026", 2026-04-28. https://www.sec.gov/Archives/edgar/data/0000024741/000002474126000198/glw-20260328xex991xq12026.htm
- SEC EDGAR, "Keysight Form 8-K Ex.99.1 Q3 FY2026 press release", 2026-08-18. https://www.sec.gov/Archives/edgar/data/0001601046/000160104626000029/exhibit991-q326pressrelease.htm
- Keysight IR, "Q3 26 Results Presentation", 2026-08-18. https://s22.q4cdn.com/444849635/files/doc_earnings/2026/q3/presentation/Q3-26-Results-Presentation.pdf
- Nasdaq/Zacks, "Keysight Q3 Earnings Beat Estimates, Revenues Up Y/Y on Solid Demand", 2026-08 (approx.). https://www.nasdaq.com/articles/keysight-q3-earnings-beat-estimates-revenues-y-y-solid-demand
- SEC EDGAR, "Jabil Form 8-K Ex.99.1 Q4 and FY2026 results", 2026-09-30. https://www.sec.gov/Archives/edgar/data/0000898293/000162828026063890/jbl-20260930ex991.htm
- Pulse 2.0, "Jabil Reports Q4 Revenue Of $10.6 Billion And FY2026 Revenue Of $36 Billion", 2026-09-30. https://pulse2.com/jabil-reports-q4-revenue-of-10-6-billion-and-fy2026-revenue-of-36-billion/
- Finviz, "Jabil shares fall 4% despite fourth quarter earnings beat and higher fiscal 2027 outlook", 2026-09-30. https://finviz.com/news/397095/jabil-shares-fall-4-despite-fourth-quarter-earnings-beat-and-higher-fiscal-2027-outlook
- SEC EDGAR, "Arista Networks Form 8-K Ex.99.1 Q2 2026 earnings release", 2026-08-04. https://www.sec.gov/Archives/edgar/data/0001596532/000159653226000174/ex991q226-earningsrelease.htm
- Business Wire, "Arista Networks, Inc. Reports Second Quarter 2026 Financial Results", 2026-08-04. https://www.businesswire.com/news/home/20260804130700/en/
- SEC EDGAR, "Microchip Form 8-K Ex.99.1 Q1 FY2027 results", 2026-08-06. https://www.sec.gov/Archives/edgar/data/0000827054/000082705426000037/exhibit991q1fy27.htm
- Futurum Group, "Microchip Q1 FY 2027 Earnings Beat as Data Center Exposure Nears $1 Billion", 2026-08 (approx.). https://futurumgroup.com/insights/microchip-q1-fy-2027-earnings-beat-as-data-center-exposure-nears-1-billion/
- Marvell IR, "Marvell Technology, Inc. Reports Second Quarter of Fiscal Year 2027 Financial Results", 2026-08-27 (approx.). https://investor.marvell.com/news-events/press-releases/detail/1031/marvell-technology-inc-reports-second-quarter-of-fiscal-year-2027-financial-results
- Marvell IR, "Marvell Technology, Inc. Reports First Quarter of Fiscal Year 2027 Financial Results", 2026-05-27. https://investor.marvell.com/news-events/press-releases/detail/1023/marvell-technology-inc-reports-first-quarter-of-fiscal-year-2027-financial-results
- StorageNewsletter, "Marvell Technology fiscal 2Q27 financial results", 2026-08-28. https://www.storagenewsletter.com/2026/08/28/marvell-technology-fiscal-2q27-financial-results/
- Astera Labs, "Astera Labs Reports First Quarter 2026 Financial Results", 2026-05-05. https://www.asteralabs.com/news/astera-labs-reports-first-quarter-2026-financial-results/
- SEC EDGAR, "Credo Form 8-K Ex.99.1 Q1 FY2027 results", 2026-09-01. https://www.sec.gov/Archives/edgar/data/0001807794/000162828026059795/credoq12027ex-991.htm
- SEC EDGAR, "Credo Form 8-K Ex.99.1 Q4 and FY2026 results", 2026-06-01. https://www.sec.gov/Archives/edgar/data/0001807794/000162828026039474/credoq42026ex-991.htm
- Pulse 2.0, "Credo Reports Q1 Fiscal 2027 Revenue Of $479 Million, Up 115% Year Over Year", 2026-09. https://pulse2.com/credo-reports-q1-fiscal-2027-revenue-of-479-million-up-115-year-over-year/
- SEC EDGAR, "Rambus Form 8-K Ex.99.1 Q2 2026 results", 2026-07-27. https://www.sec.gov/Archives/edgar/data/0000917273/000119312526318063/rmbs-ex99_1.htm
- SEC EDGAR, "Rambus Form 8-K Ex.99.1 Q1 2026 results", 2026-04-27. https://www.sec.gov/Archives/edgar/data/0000917273/000119312526182076/rmbs-ex99_1.htm
- Business Wire, "Rambus Reports Fourth Quarter and Fiscal Year 2025 Financial Results", 2026-02-02. https://www.businesswire.com/news/home/20260202262886/en
- SEC EDGAR, "Amkor Form 8-K Ex.99.1 Q2 2026 results", 2026-07-27. https://www.sec.gov/Archives/edgar/data/0001047127/000104712726000043/amkr6302026erex-991.htm
- SEC EDGAR, "Amkor Form 8-K Ex.99.1 Q1 2026 results", 2026-04-27. https://www.sec.gov/Archives/edgar/data/0001047127/000104712726000017/amkr3312026erex-991.htm
- Business Wire, "Amkor Technology Reports Financial Results for the Second Quarter 2026", 2026-07-27. https://www.businesswire.com/news/home/20260727961778/en/
- Stock Titan, "ASE Technology Holding Reports Unaudited Consolidated Financial Results for 2Q 2026", 2026-07-30. https://www.stocktitan.net/news/TWSE/ase-technology-holding-co-ltd-reports-its-unaudited-consolidated-0frswijrzm2y.html
- Barchart / PR Newswire, "ASE Technology Holding Co., Ltd. Reports Its Unaudited Consolidated Financial Results for the Second Quarter of 2026", 2026-07-30. https://www.barchart.com/story/news/3543158/ase-technology-holding-co-ltd-reports-its-unaudited-consolidated-financial-results-for-the-second-quarter-of-2026
- Seeking Alpha / PR Newswire, "ASE Technology Holding Reports Unaudited Consolidated Financial Results for the First Quarter of 2026", 2026-04-29. https://seekingalpha.com/pr/20491809
- Celestica IR, "Celestica Announces Second Quarter 2026 Financial Results", 2026-07-27. https://corporate.celestica.com/node/17606
- SEC EDGAR, "Celestica 8-K Q2 2026 press release with condensed financial statements", 2026-07-27. https://www.sec.gov/Archives/edgar/data/0001030894/000103089426000043/cls-20260630prcondensedfs.htm
- Celestica IR, "Celestica Announces First Quarter 2026 Financial Results", 2026-04-27. https://celestica.gcs-web.com/node/17386
- TipRanks, "Lumentum reduces convertible debt through private share exchange", 2026-05-29. https://www.tipranks.com/news/company-announcements/lumentum-reduces-convertible-debt-through-private-share-exchange
- SEC (Coherent 8-K Ex.99.1), "Coherent Corp. Reports Fourth Quarter and Full Year Fiscal 2026 Results", 2026-08-12. https://www.sec.gov/Archives/edgar/data/0000820318/000119312526346860/d128030dex991.htm
- SEC (Coherent ARS), "Coherent Corp. Form ARS FY2026", 2026. https://www.sec.gov/Archives/edgar/data/0000820318/000110465926114851/tm264290d2_ars.pdf
- SEC (Fabrinet 8-K Ex.99.1), "Fabrinet Announces Fourth Quarter and Fiscal Year 2026 Financial Results", 2026-08-17. https://www.sec.gov/Archives/edgar/data/0001408710/000140871026000026/fn-2026811xex991q426.htm
- Nasdaq, "Fabrinet Q4 Earnings Call Highlights", 2026-08. https://www.nasdaq.com/articles/fabrinet-q4-earnings-call-highlights
- Finviz, "Fabrinet Shares Slide Despite Earnings Beat as Margins and Cash Flow Disappoint", 2026-08-18. https://finviz.com/news/383079/fabrinet-shares-slide-despite-earnings-beat-as-margins-and-cash-flow-disappoint
- SEC (MACOM 8-K Ex.99.1), "MACOM Reports Fiscal Third Quarter 2026 Financial Results", 2026-08. https://www.sec.gov/Archives/edgar/data/0001493594/000149359426000036/ex99_1earningsreleaseq3fy26.htm
- SEC (MACOM 10-Q), "MACOM Form 10-Q for quarter ended 2026-07-03", 2026-08. https://www.sec.gov/Archives/edgar/data/0001493594/000149359426000038/mtsi-20260703.htm
- Webull, "MACOM (MTSI) Q3 2026 Earnings Call Transcript", 2026-08. https://www.webull.com/news/15396902106440704
- Simply Wall St, "Teradyne Future Growth", unverified. https://simplywall.st/stocks/ch/semiconductors/vtx-ter/teradyne-shares/future
- SEC (Entegris 8-K Ex.99.1), "Entegris Reports Results for Second Quarter of 2026", 2026-08-04. https://www.sec.gov/Archives/edgar/data/0001101302/000110130226000146/entgq22026ex991.htm
- SEC (Entegris 8-K Ex.99.1), "Entegris Reports Results for First Quarter of 2026", 2026-04-30. https://www.sec.gov/Archives/edgar/data/0001101302/000110130226000099/entgq12026ex991.htm
- MarketBeat, "Entegris Q2 Earnings Call Highlights", 2026-08-04. https://www.marketbeat.com/instant-alerts/entegris-q2-earnings-call-highlights-2026-08-04/
- Barchart / AXT press release, "AXT Inc Announces Second Quarter 2026 Financial Results", 2026-07-30. https://www.barchart.com/story/news/3560661/axt-inc-announces-second-quarter-2026-financial-results
- Quartr, "AXT (AXTI) Q2 2026 earnings summary", 2026-07-30. https://quartr.com/events/axt-inc-axti-q2-2026_3seBRzq2
- Applied Optoelectronics IR, "Applied Optoelectronics Reports Second Quarter 2026 Results", 2026-08-06. https://appliedoptoelectronics.gcs-web.com/node/17506
- Applied Optoelectronics IR, "Applied Optoelectronics Reports First Quarter 2026 Results", 2026-05-07. https://appliedoptoelectronics.gcs-web.com/node/17011
- Panabee, "Applied Optoelectronics: 69% Revenue Surge Collides with Margin and Concentration Risks", 2026-08. https://www.panabee.com/news/applied-optoelectronics-earnings-q2-2026-report
- SEC EDGAR, "Aehr Test Systems Form 8-K Exhibit 99.1 (FY2026 Q4 and full-year results)", 2026-07-14. https://www.sec.gov/Archives/edgar/data/0001040470/000165495426006655/aehr_ex991.htm
- Aehr Test Systems, "Aehr Test Systems Reports Fiscal 2026 Fourth Quarter and Full Year Financial Results with record quarterly bookings and $100 million effective backlog", 2026-07-14. https://www.aehr.com/2026/07/aehr-test-systems-reports-fiscal-2026-fourth-quarter-and-full-year-financial-results-with-record-quarterly-bookings-and-100-million-effective-backlog/embed/
- Nasdaq, "Aehr Test Systems Q4 earnings call highlights", 2026-07-15. https://www.nasdaq.com/articles/aehr-test-systems-q4-earnings-call-highlights
- GlobeNewswire / Veeco, "Veeco Reports First Quarter 2026 Financial Results", 2026-05-05. https://www.globenewswire.com/news-release/2026/05/05/3288214/0/en/Veeco-Reports-First-Quarter-2026-Financial-Results.html
- Panabee, "AI-Driven Growth Offsets Margin Compression at Veeco", 2026-08. https://www.panabee.com/news/veeco-instruments-earnings-q2-2026-report
- SEC EDGAR, "Cohu Inc Form 8-K exhibit (Q2 2026 results)", 2026-07-30. https://www.sec.gov/Archives/edgar/data/0000021535/000143774926025053/ex_994647.htm
- MarketBeat, "Cohu Q2 earnings call highlights", 2026-07-30. https://www.marketbeat.com/instant-alerts/cohu-q2-earnings-call-highlights-2026-07-30/
- SEC EDGAR, "Cohu Inc Form 8-K exhibit (Q1 2026 results)", 2026-04-30. https://www.sec.gov/Archives/edgar/data/0000021535/000143774926014188/ex_952461.htm
- MarketBeat, "FormFactor (NASDAQ:FORM) updates Q3 2026 earnings guidance", 2026-07-29. https://www.marketbeat.com/instant-alerts/formfactor-nasdaqform-updates-q3-2026-earnings-guidance-2026-07-29/
- PR Newswire / Camtek, "Camtek Announces Results for the Second Quarter of 2026", 2026-08-10. https://www.prnewswire.com/il/news-releases/camtek-announces-results-for-the-second-quarter-of-2026-302847042.html
- SEC 6-K, "Camtek Ltd Form 6-K FY2026", 2026-08. https://www.sec.gov/Archives/edgar/data/0001109138/000117891326003975/zk2635905.htm
- Finviz / Camtek, "Camtek Announces Record Results for the Fourth Quarter & Full Year 2025", 2026-02-18. https://finviz.com/news/313937/camtek-announces-record-results-for-the-fourth-quarter-full-year-2025
- Business Wire / Onto Innovation, "Onto Innovation Reports 2026 Second Quarter Results", 2026-08-06. https://secure.businesswire.com/news/home/20260806980504/en/Onto-Innovation-Reports-2026-Second-Quarter-Results
- Onto Innovation (q4cdn), "Onto Innovation Reports 2026 First Quarter Results", 2026-05-05. https://s24.q4cdn.com/480160064/files/doc_news/Onto-Innovation-Reports-2026-First-Quarter-Results-2026.pdf
- Onto Innovation (q4cdn), "Onto Innovation Reports 2025 Fourth Quarter and Full Year Results", 2026-02-19. https://s24.q4cdn.com/480160064/files/doc_news/Onto-Innovation-Reports-2025-Fourth-Quarter-and-Full-Year-Results-2026.pdf
- PR Newswire / Nova, "Nova Reports Record Second Quarter 2026 Financial Results", 2026-08-06. https://www.prnewswire.com/il/news-releases/nova-reports-record-second-quarter-2026-financial-results-302844852.html
- SEC 6-K, "Nova Ltd Form 6-K FY2026", 2026-08-06. https://www.sec.gov/Archives/edgar/data/0001109345/000117891326003892/zk2635873.htm
- Nova, "Nova Reports Fourth Quarter and Record Full Year 2025 Results", 2026-02-12. https://www.novami.com/investors/press-releases/nova-reports-fourth-quarter-and-record-full-year-2025-results/
- SEC 6-K Ex.99-1 / Tower Semiconductor, "Tower Semiconductor Q2 2026 results ($460M record revenue, 24% YoY)", 2026-08-04. https://www.sec.gov/Archives/edgar/data/0000928876/000117891326003776/exhibit_99-1.htm
- SEC 6-K Ex.99-1 / Tower Semiconductor, "Tower Semiconductor Reports First Quarter 2026 Financial Results", 2026-05-13. https://www.sec.gov/Archives/edgar/data/0000928876/000117891326002607/exhibit_99-1.htm
- Tower Semiconductor, "Tower Semiconductor Reports Record Revenue for the Fourth Quarter of 2025", 2026-02-11. https://jp.towersemi.com/2026/02/11/02112026/
- SEC 8-K Ex.99.1 / Kulicke & Soffa, "Kulicke & Soffa Reports Third Quarter 2026 Results", 2026-08. https://www.sec.gov/Archives/edgar/data/0000056978/000005697826000030/ex991liveq32026.htm
- SEC 8-K Ex.99.1 / Kulicke & Soffa, "Kulicke & Soffa Reports First Quarter 2026 Results", 2026-02-04. https://www.sec.gov/Archives/edgar/data/56978/000005697826000010/ex991liveq12026.htm
- Stock Titan, "Kulicke & Soffa Reports Third Quarter 2026 Results", 2026-08. https://www.stocktitan.net/news/KLIC/kulicke-soffa-reports-third-quarter-2026-1zzzy02l3csw.html


---

## Appendix — method and data

**Pipeline.** The analysis was run by 43 analyst agents in four rounds:
1. **Mapping and financials.** Three chain-mappers, one per niche, allocated each niche's 2030 size across suppliers by realistic share. Six financial-data collectors gathered TTM revenue, gross profit, market cap, EV, ADV and 12-month performance.
2. **Deep dives.** Ten deep dives, each with three passes: a researcher, an independent skeptic who checked the load-bearing numbers, the hard signals and consensus, and an editor who recomputed every metric from the final numbers.
3. **Checks.** A consensus-verification pass, a hard-signal audit of every screened company, and a false-positives analyst.
4. **Tables.** The final tables are computed in code from the mapper and deep-dive numbers, so every leverage figure uses the same definitions.

**Hard-signal audit.** The audit was strict. One editorial override: Marvell in N3 counts as a weak pass. Its ~$540M acquisition of XConn was made for scale-up switching, and Marvell guided ~$100M of FY28 revenue from it, which meets the "management guidance with numbers" test. No named socket exists yet.

**Data files.** [`data/screening_all_niches.csv`](data/screening_all_niches.csv) holds every company–niche row with all inputs and computed metrics.
