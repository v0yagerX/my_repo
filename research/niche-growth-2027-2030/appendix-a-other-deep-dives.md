# Appendix A — Deep dives on the other deep-dived niches

These niches went through the same pipeline as the top 10 (deep-dive researcher, independent fact-check and quant rebuild, independent bear case, editor integration, three-lens re-score) but did not make the final top 10 under the ranking rule in Section 3.3 of the main report. Labels: [R] reported fact, [G] company guidance, [3P] third-party estimate, [E] own estimate; [STALE yyyy-mm] marks figures published before ~Oct 2025.

- A.1 · LEAP aftermarket OEM hot-section/LLP material (L43) — prob-weighted CAGR 26%; passes gate, ranked below #10
- A.2 · OSAT-outsourced CoWoS-class 2.5D packaging (L19) — prob-weighted CAGR 24%; passes gate, ranked below #10
- A.3 · PAC-3 MSE / THAAD interceptor rocket motors (L30) — prob-weighted CAGR 22%; passes gate, ranked below #10
- A.4 · Low-CTE T-glass cloth/yarn for IC substrates (L18) — prob-weighted CAGR 17%; passes gate, ranked below #10
- A.5 · AC-to-800 VDC conversion for AI data halls (L08) — prob-weighted CAGR 110%; below the quality/size gate
- A.6 · Vertical power-delivery modules for AI XPUs (L10) — prob-weighted CAGR 70%; below the quality/size gate
- A.7 · New-build NA/EU sintered NdFeB magnets (L45) — prob-weighted CAGR 56%; below the quality/size gate
- A.8 · Expendable small turbojets (<=400 lbf) (L31) — prob-weighted CAGR 27%; below the quality/size gate

### A.1 · CFM LEAP aftermarket OEM new-make hot-section material, LLP stacks and HPT durability-kit hardware
*Megatrend: Narrowbody fleet growth and ageing (LEAP aftermarket ramp) | 2026 -> 2030 revenue: $1.7-3.9B -> $3.5-12B | CAGR: 20-32% (base ~28%; bear ~14-19%) | Growth mix: ~80% volume / ~20% price | Confidence: medium*

**Definition.**
- **In:** new-make parts from CFM (GE Aerospace / Safran) that are used in, or sold for, off-wing LEAP-1A/-1B/-1C shop visits. They are valued at catalog price, or at contract-implied value under RPFH/TrueChoice. The niche covers both CFM's external channel and GE/Safran's own shops. Three buckets:
  1. HPT durability-kit hardware fitted at retrofit: stage-1 blade, stage-1 nozzle, forward inner nozzle support and reverse-bleed hardware.
  2. Other new hot-section parts: combustor liners and domes, TAPS fuel nozzles, HPT stage-2 airfoils, shrouds (including CMC), LPT airfoils and seals.
  3. Life-limited parts (LLPs) as full or partial stacks: fan disk, booster spool, HPC/HPT/LPT disks and shafts.
- **Out:**
  - Shop-visit labour, test cells and workscope management.
  - Piece-part repair, whether by the OEM or by independents.
  - PMA/DER parts and used serviceable material (USM).
  - Cold-section parts other than LLPs, and line-replaceable units (LRUs).
  - On-wing services, spare engines and leasing.
  - Original-equipment (OE) engines, including kit hardware fitted on new builds.
  - CFM56, GTF, V2500 and widebody engines.

**Value-chain path.** Narrowbody traffic -> A320neo / 737 MAX / C919 fleets -> CFM LEAP-1A/-1B/-1C -> engine aftermarket -> off-wing shop visits (~15% done by third parties today, heading for ~30% [G]) -> OEM new-make material -> **hot-section parts + durability-kit hardware + LLP stacks**.

Upstream suppliers:
- Single-crystal casters: PCC, Howmet, CPP and Doncasters.
- Disk and ring forgers: Wyman-Gordon, Howmet, ATI, Safran, and Guizhou Aviation Tech for LEAP-1C.
- Module assembly: AIDC.

**Drill-down decision.** Two narrower cuts were tested and rejected. The combined level is kept.
- **Durability-kit hardware alone: rejected.**
  - It is a one-off retrofit wave. The LEAP-1A kit is on ~40% of the 1A fleet [G]. The 1B kit was certified on 18 Jul 2026, with cutover in early 2027 [G].
  - Some of the hardware may be supplied under warranty (unverified).
  - The kit doubles hot-and-harsh time on wing [G], so it cuts its own future demand.
- **LLP stacks alone: rejected, kept as a watch sub-niche.**
  - About $0.2-0.6B in 2026 rising to $1.2-3B in 2030, or ~45-70% CAGR [E]. That is a small-base bet on timing.
  - GE puts LLP-heavy visits at ~2028-29 [G].
  - LEAP LLP lives and prices are unverified. The only figures come from a non-OEM blog: a $4-10M stack and a 25k-cycle HPT disk limit.
- **Why the combined level:** the same sole-source sellers capture all three buckets in the same shop visits, and the visit-volume drivers are verified by 2026 primary sources.

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $1.7-3.9B [E] | $3.5-12B [E] | 19.8-32.4% (paired) |
| Base | $2.5B | $6.8B | 28.4% |
| Bear case (~25% probability) | $2.7-3.0B (bear's own base) | $4.5-5.5B | ~11-20% (central ~14-17%) |

**CAGR math (own estimates)**

| Case | Calculation | CAGR |
|---|---|---|
| Low | (3.5/1.7)^(1/4) − 1 = 2.06^0.25 − 1 | 19.8% |
| Base | (6.8/2.5)^(1/4) − 1 = 2.72^0.25 − 1 | 28.4% |
| High | (12/3.9)^(1/4) − 1 = 3.08^0.25 − 1 | 32.4% |
| Cross-paired (base 2026 with the low or high 2030) | | 8.8% to 48.0% |

The cross-paired spread is very wide because the 2030 figure is highly sensitive to timing.

- **Volume vs price.** In the base case, ln(2.72) = 1.00, split as follows [E]:

  | Growth leg | Base-case change | Log | Share |
  |---|---|---|---|
  | Shop visits | 1,400 -> 2,700 (1.93x) | 0.66 | ~65% |
  | Catalog/contract price | 1.22x (~5%/yr) | 0.20 | ~20% |
  | Content mix | 1.16x | 0.14 | ~15% |

  - The mix leg is almost entirely the LLP wave. Non-LLP hot-section content per visit is roughly flat after repairs (x0.97).
  - Part of the price leg is scarcity pricing: delinquencies rose 20% q/q in Q2 2026 [R].
  - "LEAP services margin parity by 2028" [G] comes mostly from RPFH repricing and cost-down, not from catalog increases.
  - The bear case splits growth ~90% volume, with a negative mix leg.

- **Top-down** (visits x all-in visit cost x OEM new-make share x hot-section+LLP share) [E]:

  | Case | 2026 | 2030 |
  |---|---|---|
  | Low | 1,150 x $3.0M x 0.60 x 0.65 = **$1.35B** | 2,100 x $4.0M x 0.60 x 0.68 = **$3.4B** |
  | Base | 1,400 x $4.0M x 0.65 x 0.72 = **$2.6B** | 2,700 x $5.3M x 0.65 x 0.75 = **$7.0B** |
  | High | 1,700 x $5.0M x 0.70 x 0.80 = **$4.8B** | 3,400 x $7.0M x 0.70 x 0.82 = **$13.7B** |

  - 2026 visit anchor:
    - The 2025 LEAP visit base is ~800-1,150. Willis Lease estimated ~1,100 [3P] [STALE 2025-05]; IATA/Emerton estimated ~600-800 [3P].
    - Applied 2026 growth is +30-45%. GE-internal LEAP visits grew more than 50% in H1 [R], against a +25% full-year guide [G].
  - Visit-cost benchmark: $2.0-4.5M+ for a performance restoration [3P, non-OEM, unverified].
  - 2030 visits:
    - GE guides a ~25% LEAP visit CAGR off a 2024 base [G]. The base is unpublished. At 700-900 it implies 2,670-3,430 visits (1.25^6 = 3.81x).
    - The low case of 2,100 follows the bear case's eligible-pool argument.
- **Bottom-up** (cohort content build) [E]:
  - **2026:** hot-section content excluding LLPs is $1.25-2.0M per visit (base $1.6M), net of repairs and concession hardware. LLP content adds $0.2-0.3M (base $0.2M).
    - Low: 1,150 x $1.45M = $1.67B.
    - Base: 1,400 x $1.80M = $2.52B.
    - High: 1,700 x $2.30M = $3.91B.
  - **2030 hot-section, excluding LLPs:** visits x 2026 content x price (1.17-1.26) x net workscope. Net workscope is 0.97-1.06; the bear case uses 0.85-1.0.
    - Low: 2,100 x 1.25 x 1.17 x 0.97 = $2.98B.
    - Base: 2,700 x 1.6 x 1.22 x 0.97 = $5.11B.
    - High: 3,400 x 2.0 x 1.26 x 1.06 = $9.08B.
  - **2030 LLP wave:**
    - The 2016-18 delivery cohort is 1,654 engines and 2019 adds 1,736 [R] [STALE 2025-01 series].
    - At an assumed ~20k-cycle limit (unverified), roughly 300-500 stacks fall due in 2030 at $3-6M each.
    - Low $0.5B, base $1.5B, high $3.0B.
  - **2030 totals:** low $3.48B, base $6.61B, high $12.08B.
  - **Supply cap check:**
    - GE is spending $500M to double its internal capacity [G].
    - Safran's in-house shops handle ~1,200 visits a year [G] [STALE 2024-12].
    - Third parties reach ~30% of visits [G].
    - Together these support ~3,000-3,600 visits in 2030 [E], so the 3,400 high case sits just inside the cap.
- **Reconciliation**
  - **2026:** top-down $2.6B and bottom-up $2.52B give a base of **$2.5B**. The range ($1.7-3.9B) uses the bottom-up figures, because the top-down extremes stack every tail.
  - **2030:** top-down $7.0B and bottom-up $6.6B give a base of **$6.8B**. The low end is $3.5B. The high end is $12B, because the top-down $13.7B needs more content than the supply cap allows.
  - **GE profit-parity cross-check:**
    - GE says LEAP profit dollars will equal CFM56's by 2030 [G].
    - CFM56 would contribute ~1,800-2,200 visits x ~$3-4M of OEM revenue each [E].
    - Matching that requires ~$8-13B of LEAP OEM aftermarket revenue. At a 55-70% niche share, the niche would be ~$5-9B [E], which brackets the base.
  - **Visit-rate check:** 2,700 visits divided by the ~13k engines delivered by YE2026 is ~21% a year. The bear case uses 17-20%; GE's guidance implies 21-27%.
  - **Rejected from the draft:**
    - The $9.0B 2030 base. It needed a 2024 visit base of at least 900 (unpublished) and +6%/yr growth in non-LLP content, which contradicts GE's repair push.
    - The circular 2030 capacity math.
    - The Howmet-based check. Howmet's Q2 2026 figures are unverified (IBKR shows a ~$2.31B quarter), and Howmet's "spares" also include IGT, defense and fasteners.

#### Demand drivers and catalysts
**Demand drivers**
- **Fleet growth.**
  - LEAP deliveries were 1,802 in 2025, up 28% [R].
  - 2026 is guided up ~15% to high-teens, about 2,050-2,150 engines [G]; the high-teens figure is unverified.
  - Safran guides ~2,600 deliveries in 2028 [G].
  - GE says the installed base will more than double from 2025 to 2030 [G].
  - GE also says most newly delivered engines will not need a shop visit before 2030 [G]. So the 2030 visit pool is mostly the ~13k engines delivered by YE2026.
- **Short time on wing.** Visits are planned at 2,000-6,000 cycles, with ~4,000 as the planning base [3P]. Hot-and-harsh operators in India and the Middle East drive HPT-heavy visits.

**Catalysts**

| Catalyst | Timing | Status |
|---|---|---|
| Durability-kit retrofits | 1A through ~2029; 1B from early 2027 into the early 2030s | 1A: kit on ~40% of the fleet and reverse bleed on ~70% [G]; more than 1,200 1A kits shipped by late 2025 [G]. 1B: certified 18 Jul 2026, hardware being industrialized [G] |
| LLP-driven heavy shop visits | ~2028-29 [G] | LEAP LLP lives unverified |
| External channel growth: ~10% of visits (2024) -> ~15% (now) -> ~30% by decade-end [G] | MTU Fort Worth opened 8 Jul 2026; Iberia first inductions Q1 2027; SSAMC Chengdu [G] | StandardAero: 60 LEAP inductions in 2025 and first LEAP-1A performance restoration in Feb 2026 [R] |
| LEAP services margin parity with the rest of CES | By 2028 [G] | Guidance |
| GE acquisition of CPP for $11.75B [R]; GE expects its airfoil demand to rise more than 30% from 2026 to 2030 [G] | Announced 8 Sep 2026; close expected 2027 | Close timing unverified; not re-checked |
| Safran 30,000-t forging press (~€150M) | Operational 2029 | Under construction [R] |
| GE Q3 2026 results and Safran Q3 2026 revenue | ~20-31 Oct 2026 | Upcoming |

#### Supply side
- **Suppliers and shares.**
  - CFM supplies ~97-100% of new-make LEAP hot-section and LLP parts; PMA is ~0% and used material negligible [E].
  - GE holds ~50-60% of niche value: the core (HPC, combustor, HPT), all kit hardware, and the HPC/HPT LLPs [E].
  - Safran holds ~40-50%: fan, booster and LPT parts and their LLPs [E].
  - Tier-2 casting shares (all [E], unverified): Howmet ~35-50%, PCC ~25-40%, CPP ~10-20%.
- **Capacity and lead times.**
  - Current strain: spare-parts delinquencies rose 20% q/q [R]; GE's LEAP turnaround is ~100 days [R].
  - The draft quoted Leeham saying that engines off-wing plus planned removals exceed GE's full-year guide by more than 40%. The fact-check could not confirm this; it is unverified.
  - GE spending:
    - $500M of MRO investment [G].
    - ~$200M for durability-upgrade capacity [G].
    - A $1B US manufacturing plan (9 Mar 2026), with more than $100M going to suppliers [G].
  - CFM network: GE more than $1B and Safran more than €1B over five years [G].
  - Howmet capex is above $500M, including a new plant in Japan [G].
  - Lead times:
    - Premier MRO licence to first induction: ~9-12 months [R].
    - New forging press: ~3 years [E].
    - Qualifying a single-crystal casting source: ~12-24+ months [E, unverified].
- **Qualification barriers.**
  - CFM controls the type design, parts release and repair data.
  - Lessors resist PMA parts on young LEAP assets.
  - There is no LEAP used-material pool until teardowns start in the 2030s.
  - Result: effectively sole-source pricing through 2030.
- **Geographic concentration.**
  - Airfoil casting and LLP forging: over 60% in the US [E], then France and the UK.
  - Secondary nodes: Mexico, Poland, Belgium, India (HAL's scope unverified), Taiwan (AIDC), Japan (Howmet) and China (Guizhou Aviation Tech rings for LEAP-1C; SSAMC).
  - Chokepoints: rhenium, superalloy master-melt and single-crystal casting know-how.

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| GE Aerospace | GE / NYSE | CFM 50% partner; LEAP core, HPT, kits, HPC/HPT LLPs; largest LEAP shop network; acquiring CPP | ~2-5%, base ~3% [E] |
| Safran | SAF / Euronext Paris | CFM 50% partner; fan, booster and LPT parts and their LLPs; RPFH services; CRT repairs | ~2-5%, base ~3% [E] |
| Howmet Aerospace | HWM / NYSE | Single-crystal HPT/LPT airfoils and rings (tier-2) | ~2-4% [E] |
| Precision Castparts | BRK.B / NYSE (parent) | Airfoils; Wyman-Gordon disks | <1% of Berkshire [E] |
| Consolidated Precision Products | Private (to GE) | LEAP castings | Unverified (~10-25% of ~$2B) |
| AIDC (漢翔) | 2634 / TWSE | LEAP core-module parts, mostly OE | Aftermarket <3% [E] |
| Guizhou Aviation Tech (航宇科技) | 688239 / SSE STAR | LEAP-1C ring forgings | <2% aftermarket-relevant [E] |
| StandardAero | SARO / NYSE | Premier MRO; buys parts at catalog price (buyer, not seller) | n/a |
| MTU Aero Engines | MTX / XETRA | Premier MRO (Fort Worth); buyer | n/a |
| HEICO | HEI / NYSE | PMA substitution risk after ~2028-30 | ~0% |

#### Bear case and key risks
- **Technology substitution.** The substitutes are repair and durability, not a new engine.
  - **Repairs.**
    - GE will double the number of LEAP repairs it develops in 2026, and a repaired part can cost more than 50% less than a new one [G].
    - About 85% of visits are done in GE/Safran shops under RPFH contracts, where the OEM pays for the parts. The seller is therefore motivated to shrink this niche.
    - Safran bought CRT for €148M to expand LEAP repairs [R].
    - StandardAero's component repair business made $709M in 2025 (+19.6%) and guides $775-800M for 2026 [R/G].
    - Bear estimate: repairs displace 15-25% of hot-section new-make value by 2030 [E].
  - **PMA.** Jet Parts Engineering won FAA approval for 13 PMA parts and 3 DER repairs, including LEAP inserts and seals, on 27 May 2026 [R]. HEICO launches ~500 PMA parts a year, ~25% of them engine parts [R]. PMA share reaches 1-3% of niche value by 2030 [E].
  - **Durability kits** lower 2030 visits by ~10-20% versus the pre-kit trajectory [E].
  - **CJ-1000A** targets CAAC certification for the C919 in 2027 [3P]. Impact on the niche is under 1-2% [E].
  - **Net bear effect:** new-make content per visit grows only ~0-2% a year nominal.
- **Capex cuts.** For this niche, the risk is airline maintenance opex rather than aircraft capex.
  - Jet fuel rose from $99.40/bbl (27 Feb) to $209/bbl (week to 3 Apr 2026) [R; underlying data unverified].
  - Cirium: May 2026 global capacity growth was cut ~3 points to +3.4%, and Qatar's schedule fell 33% [3P].
  - United cut Q2-Q3 capacity by ~5% and warned of cuts into 2027 [R].
  - GE says Middle East airlines are under 5% of its collections [G].
  - If airlines cut spending in 2028, they would swap in green-time engines, choose lighter workscopes and run LLPs to their limits. Bear estimate: niche revenue −15-25% in 2028 and −5-10% in 2030 [E].
- **Chinese capacity.** A low-weight factor.
  - Guizhou Aviation Tech has a backlog of RMB 6.43B [G].
  - The US lifted its LEAP-1C export restrictions in Jul 2025 [R] [STALE 2025-07].
  - If decoupling resumes, CAAC could push domestic PMA and repairs on Chinese LEAP-1A/-1B fleets, about 8-12% of LEAP engines [E, unverified].
  - Impact: worst case 3-6% of niche value; base case 1-2% [E].
- **Double-ordering / pull-forward.**
  - GE's Q2 spare-parts growth of more than 25% "followed improved material availability" [R], meaning catch-up shipments.
  - Howmet's spares grew 37%, against GE's internal shop-visit revenue at +25%. The Howmet figure is unverified.
  - New Premier MROs place one-off initial provisioning orders.
  - The kit retrofit wave is front-loaded.
  - Airworthiness directives create lumpy replacement demand, e.g. EASA AD 2024-0026 [STALE 2024-01].
  - Safran's H1 spare-parts growth (+27.9%) was led by CFM56, not LEAP [R].
  - Bear estimate: 5-10% of 2026-27 shipments is inventory build, which would take 5-10% off 2028-29 revenue [E].
- **Already priced in?** Largely, yes.
  - GE guides the ~25% visit CAGR publicly [G].
  - GE traded at ~40x P/E in Mar 2026 [3P].
  - The stock fell ~5% after its Q2 beat-and-raise [R] and sits ~18% below its 6 Aug 2026 record, at ~$318 [3P, date unverified].
  - There is no pure play: the niche is ~3% of GE or Safran revenue.
- **Bear-case numbers** (bear analyst, [E]):
  - 2030 size: $4.5-5.5B, central $5.0B. That is 2,100-2,500 visits x $1.9-2.3M.
  - CAGR: ~13.6% from a $3.0B 2026 base, or ~16.7% from $2.7B; range ~11-20%. Re-based on the final $2.5B 2026 figure, it is ~19% (15.8-21.8%).
  - Probability: ~25%. A severe tail of ≤$4.0B (~7.5-10%; 12.5% from $2.5B) has ~10% probability.
  - **First warning sign:** in GE's Q3 2026 call (~20-21 Oct 2026) or its FY2027 guide (Jan 2027), all three of these together:
    - the gap between off-wing engines and the shop-visit guide narrows to under ~15% while capacity is still being added;
    - 2027 LEAP internal visit growth is guided below ~15-20%;
    - spare-parts growth falls below internal visit growth while delinquencies fall.

#### Leading indicators to watch (next 2-4 quarters)
1. **GE Q3 2026 (late Oct) and FY2027 guide (Jan 2027):**
   - LEAP internal visit growth (versus +>50% in H1);
   - spare-parts growth against delinquencies;
   - any absolute LEAP visit count (a 2024 base of at least 900 lifts the 2030 base toward $8-9B);
   - the number of LEAP repairs developed.
2. **Safran Q3 revenue (late Oct) and FY2026 results (Feb 2027):** LEAP visit growth, RPFH services growth, and spare parts split between CFM56 and LEAP.
3. **Durability kits:** LEAP-1A penetration (~40% today) and whether the LEAP-1B cutover holds for early 2027.
4. **Casting supply:** CPP regulatory clearance and close; Howmet's Q3 spares growth.
5. **External channel:** StandardAero, MTU Fort Worth and Iberia LEAP inductions; Willis Lease Q3 (early Nov) LEAP lease rates and utilisation.

#### Confidence and biggest unknown
**Confidence: medium.** Volume is well evidenced: deliveries, GE visit guidance and the capacity programmes are all on record. Content per visit is not.

The biggest unknown is new-make content per visit and how it changes by 2030. That depends on four things:
- LEAP LLP lives and stack prices; no OEM source gives them.
- How many new parts GE's repair push displaces.
- Whether kit hardware is billed or supplied under warranty.
- How much catalog value RPFH accounting actually recognises as revenue.

A second unknown is the absolute 2025 LEAP visit base, which estimates put anywhere from 600 to 1,150.

#### Sources
- GE Aerospace, "GE Aerospace announces second quarter 2026 results", 2026-07-16. https://www.geaerospace.com/news/press-releases/ge-aerospace-announces-second-quarter-2026-results
- The Motley Fool, "GE Q2 2026 earnings call transcript", 2026-07-23. https://www.fool.com/earnings/call-transcripts/2026/07/23/ge-ge-q2-2026-earnings-call-transcript/
- Leeham News, "Q2 2026 earnings: GE Aerospace keeps the beat despite a few missed notes", 2026-07-16. https://leehamnews.com/2026/07/16/q2-2026-earnings-ge-aerospace-keeps-the-beat-despite-a-few-missed-notes/
- GE Aerospace IR, "Recent events: your questions answered", 2026 (date unverified). https://www.geaerospace.com/news/investor-relations/ir-updates/recent-events-your-questions-answered
- GE Aerospace IR, "2Q26 recent events recap", 2026-07. https://www.geaerospace.com/news/investor-relations/ir-updates/2q26-recent-events-recap
- GE Aerospace, Q4 2025 webcast transcript, 2026-01-22. https://www.geaerospace.com/sites/default/files/geaerospace_webcast_transcript_01222026.pdf
- Forecast International, "Safran revenue up 15% in 2025, LEAP deliveries surge 28%", 2026-02-13. https://flightplan.forecastinternational.com/2026/02/13/safran-revenue-up-15-in-2025-leap-deliveries-surge-28/
- Safran, "Safran reports its first-half 2026 results", 2026-07-28. https://www.safran-group.com/pressroom/safran-reports-its-first-half-2026-results-2026-07-28
- Safran, "Safran reports excellent financial performance 2025 and raises its 2028 ambitions", 2026-02-13. https://www.safran-group.com/pressroom/safran-reports-excellent-financial-performance-2025-and-raises-its-2028-ambitions-2026-02-13
- CFM International, "CFM secures certification for LEAP-1B durability upgrades", 2026-07-18. https://www.cfmaeroengines.com/press-articles/cfm-secures-certification-for-leap-1b-durability-upgrades
- CFM International, "CFM expands, strengthens open MRO ecosystem", 2026-07. https://www.cfmaeroengines.com/press-articles/cfm-expands-strengthens-open-mro-ecosystem
- AIN Online, "CFM modifications ease LEAP engine maintenance burden", 2025-11-14. https://backend.ainonline.com/aviation-news/aerospace/2025-11-14/cfm-modifications-ease-leap-engine-maintenance-burden
- BNN Bloomberg (Reuters), "GE Aerospace to buy castings maker CPP for nearly US$12 billion", 2026-09-08. https://www.bnnbloomberg.ca/business/2026/09/08/ge-aerospace-to-buy-castings-maker-cpp-for-nearly-us12-billion/
- Howmet Aerospace, "Howmet Aerospace reports second quarter 2026 results", 2026-08-06 (figures unverified). https://www.howmet.com/press-release/2026-08-06/howmet-aerospace-reports-second-quarter-2026-results/
- Willis Lease Finance, "Q1 2025 investor presentation", 2025-05 [STALE 2025-05]. https://www.sec.gov/Archives/edgar/data/0001018164/000101816425000055/wlfc1q25presentationfina.htm
- AFM, "Engine MRO bottlenecks... shop visits set to rise sevenfold by 2040, IATA study finds", date unverified. https://afm.aero/engine-mro-bottlenecks-disrupting-airline-operations-with-shop-visits-set-to-rise-sevenfold-by-2040-iata-study-finds
- AviTrader, "StandardAero completes first LEAP engine performance restoration shop visit", 2026-02-06. https://avitrader.com/2026/02/06/standardaero-completes-first-leap-engine-performance-restoration-shop-visit/
- Visual Approach, "Wave of early LEAP-1A/1B shop visits frustrating operators", date unverified. https://visualapproach.io/wave-of-early-leap-1a-1b-shop-visits-frustrating-operators/
- SafeFly Aviation, "Engine shop visit costs 2026", 2026 (non-OEM). https://safefly.aero/engine-shop-visit-costs-2026/
- Jet Parts Engineering, "JPE announces FAA approval of 13 new PMA parts and 3 new DER repairs", 2026-05-27. https://www.jetpartsengineering.com/press-releases/jpe-announces-faa-approval-of-13-new-pma-parts-and-3-new-der-repairs
- Cirium, "Ascend Consultancy: how higher jet fuel prices are reshaping airline capacity plans", 2026-04/05. https://www.cirium.com/thoughtcloud/ascend-consultancy-how-higher-jet-fuel-prices-are-reshaping-airline-capacity-plans/
- Airways Magazine, "United to reduce Q2-Q3 capacity on jet fuel price surge", 2026. https://www.airwaysmag.com/new-post/united-reduce-q2-q3-capacity-jet-fuel-price-surge
- AVM Magazine, "How fuel prices are affecting aviation in 2026", 2026-04. https://avm-mag.com/how-fuel-prices-are-affecting-aviation-in-2026-what-it-means-for-airlines-and-mros
- Sina News, CJ-1000A certification outlook, 2026-02-06. https://news.sina.cn/bignews/insight/2026-02-06/detail-inhkvrer5254848.d.html?vt=4
- IDN Financials, "US lifts jet engine export ban; China to accelerate COMAC C919", 2025-07 [STALE 2025-07]. https://www.idnfinancials.com/news/55702/us-lifts-jet-engine-export-ban-china-to-accelerate-comac-c919
- TIKR, "GE Aerospace stock is 17% below its high...", 2026 (date unverified). https://www.tikr.com/blog/ge-aerospace-stock-is-17-below-its-high-heres-what-its-cfm56-retirement-data-means-for-2027
- Yahoo Finance, "Wall Street split on GE Aerospace", 2026 H2. https://finance.yahoo.com/markets/stocks/articles/wall-street-split-ge-aerospace-143628303.html
- MarketBeat, "GE Aerospace stock price down 3.7%", 2026-03-05. https://www.marketbeat.com/instant-alerts/ge-aerospace-nysege-stock-price-down-37-heres-why-2026-03-05/
- Taipei Times, AIDC investor conference, 2026-04-21. https://www.taipeitimes.com/News/biz/archives/2026/04/21/2003855936
- Tencent News, Guizhou Aviation Tech IR notes, 2026-05-20. https://news.qq.com/rain/a/20260520A031ZZ00
- EASA, "AD 2024-0026", 2024-01 [STALE 2024-01]. https://www.caat.or.th/wp-content/uploads/2023/01/EASA_AD_2024_0026.pdf
- Interactive Brokers, company-connections data for GE, SAF, HWM, SARO and HEI, 2026 (MCP data; no public URL).


---

### A.2 · OSAT-outsourced CoWoS-class 2.5D packaging for AI/HPC (ASE/SPIL, Amkor, other non-China OSATs; ex-test)
*Megatrend: AI compute build-out hitting the advanced-packaging bottleneck | 2026 -> 2030 revenue: $2.1-3.5B -> $5-13B | CAGR: 24-39% (central ~30%) | Growth mix: ~100% volume / ~0% net price (band -10% to +15%) | Confidence: low (2026 base medium; 2030 path low)*

**Definition.** In: revenue booked by non-foundry OSATs (ASE incl. 100%-owned SPIL, Amkor, Powertech, other non-China OSATs) for interposer-class 2.5D packaging of GPUs, custom AI ASICs, chiplet DC CPUs and switch/CPO ASICs. This covers (a) on-substrate (oS/WoS) assembly of TSMC CoW modules, including turnkey substrate/lid/underfill billed by the OSAT; (b) full-flow 2.5D (CoWoS-S/R/L-like, ASE FOCoS/FOCoS-Bridge/CoWoP, Amkor S-SWIFT/S-Connect/HDFO); (c) OSAT assembly of EMIB/EMIB-T packages; and (d) OSAT panel 2.5D from 2027. Out: TSMC CoW and in-house CoWoS/CoPoS/SoIC; Intel captive EMIB/Foveros; Samsung I-Cube; all test (~25% of ASE LEAP); HBM stacking (L15); substrates (L21); foundry interposers (UMC); FCBGA and InFO/fan-out; and the China domestic pool (SJ Semiconductor, JCET, Tongfu; ~$0.5-0.7B in 2026 [E, unverified]). Admitting DC-CPU HDFO, EMIB and switch packages inflates the base ~10-20% vs a pure AI-accelerator scope, with little CAGR effect [E].

**Value-chain path.** AI accelerators / ASICs / DC CPUs / switch-CPO -> advanced packaging -> 2.5D integration (Si, RDL, RDL+bridge, bridge-in-substrate) -> foundry/OSAT step split (TSMC: interposer plus most CoW; OSAT: oS, increasingly CoW) -> **OSAT 2.5D packaging revenue (this niche)** -> test (excluded) -> rack.

**Drill-down decision.** Kept at L19. OSAT full-process 2.5D was rejected as the headline: ASE's ~$0.3B in 2026 [G; exact figure unverified] is ~10% of LEAP only as a year-end exit rate (~7-9% full-year [E]), so its 45-90% CAGR (~$0.35-0.6B -> $2.5-6B [E]) is a small-base effect and mostly reclassification of the same lines from oS to full flow: not additive, not trackable, and the most reversible slice. oS-only (commoditising; ~59% of ASE LEAP per Nomura [3P]) and the China pool (SJ Semiconductor chiplet revenue +2.6% YoY in 1H26 [R, not re-verified]) are slower.

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $2.1-3.5B [E] | $5-13B [E] | 24-39% [E] |
| Central | ~$2.8B | ~$8B | ~30% |
| Bear case (~25% probability) | ~$2.8B | $2.4-4.8B | -4% to +14% |

CAGR math (like-for-like pairs): (5/2.1)^0.25-1 = 24.2%; (13/3.5)^0.25-1 = 38.8%; (8/2.8)^0.25-1 = 30.0%. The cross-paired envelope, 9.3% [(5/3.5)^0.25-1] to 57.7% [(13/2.1)^0.25-1], is a stress band, not the range; the draft's 16-55% was such a cross-pair. Growth is front-loaded: 2027 runs ~+80-95% (ASE LEAP to "double" [G], target reportedly raised from $5.5B to >=$7.5B [3P]) to ~$5.0-5.5B, leaving ~+13-17%/yr for 2028-30 at the central case ((8.0/5.2)^(1/3)-1 = 15.4%) [E].

- **Volume vs price:** Central revenue rises 2.86x. OSAT wafer-equivalents (WE) rise ~3.0x, from ~0.33M (1.3M x 25%) to ~1.0M (3.6M x 28%): industry WE ~2.75x times OSAT share ~1.1x [E]. Revenue/WE dips from ~$8.2-8.5k to ~$7.5-8.0k. Mix adds +15-25% (full process from ~8% to 25-40% of OSAT WE at $11-14k; CPO). Price subtracts 10-20%: 2026 contains ASE back-end hikes of 5-20% (Morgan Stanley [3P, Jan 2026]) that should reverse as TrendForce sees tightness easing from 2027 [3P], and turnkey substrates can shift to consignment. Net: ~100% volume / ~0% (about -5%) price in log terms. The draft's 80-90/10-20 split is withdrawn because its own 3.5x WE vs 3.17x revenue implied revenue/WE of -9%. The share-gain piece (~10% of volume growth) depends on TSMC policy and is the least durable.
- **Top-down (output x OSAT share x revenue/WE):** 2026 uses output, not demand. TSMC goes from ~70k wpm (end-2025) to 130-140k (end-2026) [3P], averaging ~100-110k wpm = 1.20-1.32M WE; adding ~0.02-0.04M OSAT full flow gives 1.2-1.35M. Morgan Stanley's 1.394M is demand [3P, Jul 8 2026], consistent with TrendForce's ~10% gap [3P]. OSAT share is 20-30% [E] and revenue/WE $7-9k [E]. Calibration: oS-only value is likely ~$2-4k/WE (40-50% of CoWoS-S oS outsourcing was worth $150-200M [3P, STALE 2024-11]); a fully processed wafer is ~$10-12k [3P, STALE 2025-04]; ASE disclosure over capacity implies $7-9k including pass-through and price hikes. Low 1.2M x 20% x $7k = $1.7B; central 1.3M x 25% x $8.2k = $2.7B; high 1.35M x 30% x $9k = $3.6B. For 2030, 2027 is supply-limited at ~2.0-2.4M WE (TSMC 170-220k wpm end-2027; demand 2.31-2.69M per GS/UBS/MS [3P]), then +10-25%/yr to 2.8-4.7M WE, x share 22-35% x $6-9k. Low 2.8M x 22% x $6k = $3.7B; central 3.6M x 28% x $7.5k = $7.6B; high 4.7M x 35% x $9k = $14.8B.
- **Bottom-up:** For 2026, ASE is LEAP $3.6-3.8B [G] x packaging 65-75% (2026 guide 75% [G]; 2025 actual 60-65% [R]) x 2.5D share 70-90% [E] = $1.64-2.57B, central 3.7 x 0.72 x 0.80 = $2.13B. Cross-check: Nomura's oS at 59% of LEAP [3P] (~$2.1-2.2B) plus ~$0.3B full process [G] gives ~$2.4-2.5B, the upper half. Amkor computing was Q1 21% x $1,685M = $354M and Q2 22% x $1,898M = $418M [R]; Q3 is +30% QoQ to ~$543M [G] and Q4 ~$520-620M [E]. That makes 2026 ~$1.83-1.94B vs ~$1.4-1.5B in 2025 [E], an increment of $0.35-0.5B. If 2.5D+HDFO "nearly triples" [G] and supplies most of it, the base was ~$0.17-0.3B and 2026 ~$0.45-0.85B [E] (the draft's $0.6-1.1B is corrected down). Others add $0.03-0.15B [E]. Sum $2.1-3.6B, central ~$2.9B; capacity check 0.30-0.42M WE x $7-9k = $2.1-3.8B. For 2030, ASE is 2027 LEAP >=$7.5B x 65-75% x 70-90% = $3.0-5.1B, then +5-20%/yr to $3.5-8.8B. Amkor is $0.7-1.4B in 2027 (UBS flat 20k wpm vs KGI 15k->25k, unverified) and $1.0-3.0B in 2030 with Arizona ~2028 (unverified). Others add $0.1-0.5B. Sum $4.6-12.3B, central ~$8B. Capacity method: 90-150k wpm [E] x 12 x 70-85% = 0.76-1.53M WE x $6-9k = $4.5-13.8B; central 120k x 12 x 0.8 x $7.5k = $8.6B.
- **Reconciliation:** 2026 top-down $1.7-3.6B and bottom-up $2.1-3.6B; adopt $2.1-3.5B (central $2.8B), not the draft's $2.4-3.6B, since Amkor was overstated by $0.15-0.3B and LEAP packaging share is a range. The Nomura cross-check makes the low end less likely (a $3.0B central gives a 27.8% CAGR). The methods are partly circular, as revenue/WE was calibrated to disclosures. For 2030 the three methods overlap at $5-13B, central ~$8B. The $5B low end is about a 25th percentile; the bear case sits below it.

#### Demand drivers and catalysts
- **Accelerator volume:** CoWoS demand is 1.394M wafers in 2026 and 2.694M in 2027 (+93%, Morgan Stanley [3P]); UBS 2.63M and GS ~2.31M [3P, attribution approximate]. AMD is the swing OSAT customer, but MS's 130k -> 530k is contested (240k elsewhere; JPMorgan 90k/120k) [3P].
- **TSMC short and front-end-focused:** call coverage calls CoWoS the primary bottleneck, with Wei reportedly welcoming more back-end providers [R via media; wording unverified]. Nvidia reserved ~800-850k TSMC wafers (~60%) for 2026 [3P].
- **Outsourcing widening:** TSMC reportedly extended CoW, not only WoS, outsourcing to OSATs (ETNews via TrendForce, Aug 2026; no ratio) [3P]. AMD reportedly moved ~half its orders to ASE/SPIL/Amkor, and Nvidia named Amkor and SPIL as partners [3P].
- **Bigger packages** (Rubin +30-35% area, Rubin Ultra, Feynman) and **US onshoring** (TSMC-Amkor 10-year Arizona deal, Jun 16 2026, unsized [R]).
- **Catalysts:** TSMC Q3-26 call, Oct 15-16 (pending); ASE/Amkor Q3-26, late Oct (pending); ASE Kaohsiung CoWoS-L-like line, validation end-2026 and volume 2027 (in progress [3P]); ASE 310mm panel line, Q1 2027 (announced [G]); ASE Feb-2027 guide; Rubin and MI400/450 ramps, 2H26-27 (in progress). Counter-catalysts: EMIB-T HVM 2027; CoPoS MP 2028 to 1H29 [3P]; TSMC Arizona AP ~2029.

#### Supply side
- **Suppliers and shares:** ASE incl. SPIL ~65-80% (central ~75%), Amkor ~15-30%, others 1-5% [E]. No third non-China OSAT is volume-qualified.
- **Capacity and lead times:** OSAT capacity is ~35-45k wpm at end-2026 (Commercial Times 40k; UBS ASE 20k + Amkor 20k [3P]) vs TSMC 120-140k. End-2027 OSAT is ~65-90k (UBS ASE 70k, a second UBS note 50k) vs TSMC 170-220k (KGI 170k, UBS 180k, Commercial Times 220k) [3P]. End-2028 TSMC is ~260k [3P, EDN] and OSAT ~110k (unverified). UBS's 270k total double counts oS on TSMC CoW wafers, and KGI's ASEH +125% / Amkor +66% are unverifiable. Tools take 7-9 months [3P] and new AP buildings ~18-24 months [E]. 2026 capex is ~$10.5B at ASE ($4B facilities / $6.5B equipment) [G] and $2.5-3.0B at Amkor, 30-35% to 2.5D/HDFO/test [G].
- **Qualification barriers:** TSMC licences and on-site support; ~6-12 months per program [E]; yield liability on HBM-laden CoW wafers worth tens of thousands of dollars; customer prepayments.
- **Geographic concentration:** ~70-80% Taiwan, ~15-25% Korea [E]; US ~0 until Amkor Arizona (~2028, unverified) and TSMC Arizona AP (~2029). Upstream TSMC, ABF (Ibiden/Unimicron) and tools are concentrated too, with Taiwan-contingency and Section 232 exposure.

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| ASE Technology Holding | 3711 TWSE / ASX NYSE | #1: SPIL oS for Nvidia; FOCoS/FOCoS-Bridge, CoWoS-L-like, CoWoP; EMIB assembly; 310mm panel | ~7-11% of group, ~11-18% of ATM [E] |
| SPIL | private (100% ASE) | Main Nvidia oS partner; CoW with TSMC support | ~20-35% [E, unverified] |
| Amkor Technology | AMKR NASDAQ | #2: 2.5D/HDFO; TSMC Arizona partner | ~6-11% [E: $0.45-0.85B of ~$7.6B] |
| Powertech Technology | 6239 TWSE | Fringe (FOPLP/2.5D development) | <2% [E] |
| SJ Semiconductor | 688820 SSE STAR | China 2.5D leader (outside core) | ~54% chiplet integration, 1H26 [R, not re-verified] |
| JCET / Tongfu | 600584 SSE / 002156 SZSE | China 2.5D; Tongfu is AMD's back-end partner | <3% / <5% [E] |
| TSMC | 2330 TWSE / TSM NYSE | Licensor, CoW supplier, dominant competitor | n/a |
| Intel | INTC NASDAQ | EMIB-T rival format; may outsource assembly | n/a |
| UMC | 2303 TWSE / UMC NYSE | Interposers for OSAT full flow | n/a (adjacent) |
| BESI / ASMPT / K&S / Hanmi / Disco / Advantest | BESI Euronext / 0522 HKEX / KLIC NASDAQ / 042700 KRX / 6146 TSE / 6857 TSE | Tools gating capacity | n/a (enablers) |

#### Bear case and key risks
- **Technology substitution:** Nomura puts oS at 59% of ASE LEAP in 2026 and 51% in 2027 [3P], so ~80% of LEAP packaging is the most commoditised, most exposed step. (1) **CoPoS:** MP targeted 2028 (brokers via DigiTimes); Nvidia reportedly chose it post-Rubin (TVBS), and MS has Feynman Ultra fully on CoPoS in 2029 [3P]. CoPoS takes 20-35% of leading-edge 2.5D WE by 2030, and OSATs lose 30-50% of Nvidia flagship oS if TSMC keeps oS in-house [E]; ASE's panel line is only a partial hedge. (2) **EMIB-T:** HVM 2027, with Google TPU v8e (2H27) and a Meta CPU (2H28) per Jeff Pu, Google/Amazon named via WIRED, and Intel's CFO "close to deals worth billions per year" [3P]. It takes ~4-8% of 2.5D WE by 2030, mostly captive [E]; the brake is yield (~98% CoWoS vs ~90% EMIB [3P]). (3) **CoWoP** removes the substrate and oS step. It is not expected in Rubin Ultra MP [3P; TrendForce STALE 2025-07] and needs PCB L/S below 10/10um, so 2028-29 at the earliest and 0-10% by 2030 [E]. (4) **Substrate consignment** could cut revenue/WE 20-40% with no value change [E]. Net: OSAT share falls to ~18-23% by 2030 rather than 22-35% [E].
- **Capex cuts:** GS sees hyperscaler capex growth slowing from ~100% (2026) to 54% (2027) and 12% (2028, $1.4T), with capex above operating cash flow; Moody's flags power limits and overbuild fears [3P]. Bear: 2028 capex -20-30% cuts 2.5D demand 10-25% to 1.6-2.0M WE, which TSMC's ~260k wpm (~3.1M/yr) absorbs in-house. OSATs idle first, and OSAT revenue falls ~35-50% in 2028 (demand 0.75-0.9x x share 0.7-0.8x x price 0.8-0.9x; ~-58% at all lows) [E]. A 40% AMD shortfall alone removes ~$0.7-0.8B, 15-20% of 2027 revenue [E]. Leverage worsens it: Amkor capex is up to ~40% of revenue against an "absence of backlog" (TheNextWeb), with Arizona underutilisation flagged for 2027-28 [G], and BofA flags a possible ASE bond/equity raise [3P].
- **Chinese capacity:** Direct risk is low; price risk is moderate. SJ Semiconductor (~85% of China 2.5D, ~8% global [3P]) broke ground on a ~RMB 10B Lingang 2.5D/3D line on Jun 29 2026 [R]. JCET has STATS ChipPAC Korea/Singapore sites [E, unverified route], and Tongfu owns TF-AMD Penang. No Chinese OSAT is qualified for Nvidia/AMD 2.5D on TSMC CoW (BIS rule [STALE 2025-01]). Idle capacity could undercut non-US HPC/networking/FPGA work: -2 to -5% on 2030 price/share [E].
- **Double-ordering / pull-forward:** Lead times of 52-78 weeks (TechTimes; unverified) drive parallel bookings, and overflow bookings are cancelled first. End-2027 capacity of 245-310k wpm annualises to ~2.9-3.7M wafers vs 2.31-2.69M 2027 demand. Net of double counting, TSMC alone (2.16-2.64M) nearly covers it, making OSAT full-flow lines the marginal capacity. DigiTimes reports TSMC delayed 2027 AP tool orders, read by the supply chain as CoWoS/CoPoS rebalancing [3P]. A tool-price-squeeze rumour is unverified. No cancellations were found.
- **Already priced in?** Largely, for ASE: the ADR was $42.09 on Oct 14 2026, +164% YTD, ~+260% over 12 months [R, IBKR]. Brokers are unanimously Buy at NT$730-835 [3P], and it trades at ~37x 2026E / ~25x 2027E Nomura EPS [E, FX unverified]. Amkor ($43.95, -55% from its $96.68 June peak, -23% in the Q2 week on a soft guide [R]) has partly priced the bear case; two 2x single-stock ETFs signal speculation [R]. The 2027 doubling is consensus; 2028-30 share and price are not.
- **Bear-case numbers:** 2030 at $2.4-4.8B, central ~$3.4-3.5B = demand 2.4-3.0M WE x share 18-23% x $5.5-7k: 2.4 x 18% x $5.5k = $2.4B; 2.7 x 20.5% x $6.2k = $3.4B; 3.0 x 23% x $7k = $4.8B [E]. Path: 2027 $4.5-5.5B, a 2028 trough of $2.5-3.5B, partial recovery. CAGR on $2.8B: (2.4/2.8)^0.25-1 = -3.8% / (3.5/2.8)^0.25-1 = +5.7% / (4.8/2.8)^0.25-1 = +14.4% (bear analyst's on $3.0B: -5.4% / +3.9% / +12.5%). Volume ~+7-12%/yr, price ~-2 to -5%/yr. Probability: ~25% that 2030 is <= ~$5B (<= ~16% CAGR), including a 5-8% tail below $2.4B [E]. First warning sign: TSMC's 2027 CoWoS tool allocation or OSAT tool push-outs (Q4-26 to Q1-27), an end-2027 TSMC target below ~180k wpm, or 2027 demand cut below ~2.3M.

#### Leading indicators to watch (next 2-4 quarters)
1. TSMC Q3-26 (Oct 15-16) and Q4-26 calls: end-2027 CoWoS target, CoW/oS outsourcing language, CoPoS timing; Taiwan press on tool allocation.
2. ASE monthly ATM revenue (MOPS) and LEAP: 2026 >= ~$3.7B; a Feb-2027 guide >= $7B (bull) or < ~$6B / a capex cut (bear).
3. Amkor computing vs the ~+30% QoQ Q3 guide; backlog language; 2027 capex.
4. Sell-side 2027 demand (MS 2.69M, UBS 2.63M, GS ~2.31M): a cut below ~2.3M is the earliest digestion signal.
5. BESI/ASMPT/K&S/Disco order intake tied to OSAT 2.5D lines.
6. EMIB-T design wins, CoWoP or substrate-consignment moves.

#### Confidence and biggest unknown
Low overall: medium for the 2026 base (ASE LEAP guidance, Amkor segment data), low for the 2030 path. No OSAT discloses pure 2.5D revenue, revenue/WE rests on stale data, key broker figures are unverifiable (KGI) or contested (AMD 530k), and the bear case carries ~25% probability. Biggest unknown: whether the OSAT share of 2.5D wafer-equivalents keeps rising after the 2027 capacity wave or reverses as TSMC AP7/AP8, CoPoS and Arizona AP arrive amid AI-capex digestion.

#### Sources
- Taipei Times, "ASE LEAP revenue to double in 2026", 2026-02-06. https://www.taipeitimes.com/News/biz/archives/2026/02/06/2003851840
- Fugle, "ASE (3711) Q4-2025 earnings call notes", 2026-02-05. https://blog.fugle.tw/post/earnings-call-3711-2026-02-05
- StatementDog, "ASE Q3-2025 earnings call transcript", 2025-10. https://statementdog.com/analysis/ASX/earnings_calls/301671
- Economic Daily News (udn), "ASE Q1-2026 call: LEAP target >$3.5B", 2026-04-30. https://money.udn.com/money/story/5612/9472104
- BusinessNext, "ASE LEAP revenue, 2027 outlook and capex", 2026-07-30. https://www.bnext.com.tw/article/91677/ase_leap_revenue_2027_capex
- finmoconf, "ASE Q2-2026 call summary", 2026-07-30. https://finmoconf.diveinvest.net/en/ase/2026-q2
- TrendForce, "ASE again raises 2026 capex to record US$10.5B, eyes 2x LEAP revenue by 2027", 2026-07-31. https://www.trendforce.com/news/2026/07/31/news-ase-again-raises-2026-capex-to-record-us10-5b-eyes-2x-leading-edge-advanced-packaging-revenue-by-2027/
- MoneyDJ, "ASE CoWoS-L-like line in Kaohsiung", 2026-02. https://www.moneydj.com/kmdj/news/newsviewer.aspx?a=73a9bb96-969a-4a3a-8757-726af1e984e5
- TechNews, "ASE to raise prices by 5-20% in 2026 (Morgan Stanley)", 2026-01-08. https://finance.technews.tw/2026/01/08/ase-technology-holding-co-ltd-will-raise-prices-by-5-to-20-in-2026/
- TechNews, "Four factors drive ASE momentum (Nomura)", 2026-06-30. https://finance.technews.tw/2026/06/30/four-factors-drive-the-momentum-of-ase-technology-holdings-operations/
- TechNews, "UBS rates ASE Buy, target NT$835", 2026-07-02. https://finance.technews.tw/2026/07/02/ubs-gives-ase-technology-holding-a-buy-rating-with-a-target-price-of-nt835/
- TechNews, "BofA target NT$750 for ASE", 2026-07-09. https://finance.technews.tw/2026/07/09/bank-of-america-gives-ase-technology-holding-a-target-price-of-nt750/
- Amkor, "Form 10-K FY2025", 2026-02. https://www.sec.gov/Archives/edgar/data/1047127/000104712726000014/amkr-20251231.htm
- Amkor, "Q2-2026 earnings release (8-K)", 2026-07-27. https://www.sec.gov/Archives/edgar/data/0001047127/000104712726000043/amkr6302026erex-991.htm
- Amkor IR, "Q2-2026 financial tables", 2026-07-27. https://ir.amkor.com/node/24571/html
- DigiTimes, "Amkor packaging revenue 2026, Arizona", 2026-04-28. https://www.digitimes.com/news/a20260428VL214/amkor-packaging-revenue-2026-arizona.html
- Barchart, "Amkor just crushed earnings: why Wall Street still punished AMKR", 2026-07-28. https://www.barchart.com/story/news/3506149/amkor-just-crushed-earnings-heres-why-wall-street-still-punished-amkr-stock
- TheNextWeb, "Amkor Q2 2026 record revenue, capex and advanced packaging", 2026-07. https://thenextweb.com/news/amkor-q2-2026-record-revenue-capex-advanced-packaging
- Business Wire, "TSMC and Amkor announce long-term partnership to accelerate advanced packaging in the United States", 2026-06-16. https://www.businesswire.com/news/home/20260616574153/en/TSMC-and-Amkor-Technology-Announce-Long-Term-Partnership-to-Accelerate-Advanced-Packaging-in-the-United-States
- Motley Fool, "TSMC Q2 2026 earnings call transcript" (quoted wording unverified), 2026-07-16. https://www.fool.com/earnings/call-transcripts/2026/07/16/tsm-tsm-q2-2026-earnings-call-transcript/
- BigGo Finance, "TSMC Q2-2026 call summary", 2026-07-16. https://finance.biggo.com/news/5784aaf1-fcbc-4f76-8856-491b9e7175f6
- TechTimes, "TSMC posts record quarter; full-year growth outlook past 40%", 2026-07-16. https://www.techtimes.com/articles/320696/20260716/tsmc-posts-record-quarter-ai-chip-demand-pushes-full-year-growth-outlook-past-40.html
- TrendForce (citing ETNews), "TSMC reportedly expands outsourcing of key CoWoS front-end step to OSATs", 2026-08-05. https://www.trendforce.com/news/2026/08/05/news-tsmc-reportedly-expands-outsourcing-of-key-cowos-front-end-step-to-osats-amid-rising-nvidia-asic-demand/
- TrendForce, "TSMC CoWoS supply-demand gap seen narrowing from 20% to 10% by end-2026", 2026-06-15. https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/
- KuCoin (summarising Morgan Stanley), "Morgan Stanley forecasts 2.694M CoWoS demand in 2027", 2026-07-08. https://www.kucoin.com/news/flash/morgan-stanley-forecasts-2-694-million-cowos-demand-in-2027-amd-cpu-joins-advanced-packaging
- Economic Daily News (udn), "UBS: global CoWoS capacity 270k wpm by end-2027", 2026 (~Sep). https://money.udn.com/money/story/5607/9773857
- KGI, "TSMC (2330 TT) report", 2026-09-03. https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/tsmc_2330-tt_09032026e.pdf
- Commercial Times / Wantrich, "CoWoS capacity: TSMC and OSATs", 2026-10-08. https://wantrich.chinatimes.com/news/20261008900006-420101
- TechNews, "TSMC CoWoS capacity; AMD shifts orders to OSATs", 2026-09-12. https://technews.tw/2026/09/12/tsmc-cowos-capacity
- TechNews, "CoWoS home court in Taiwan" [STALE 2024-11], 2024-11-04. https://technews.tw/2024/11/04/cowos-home-court-taiwan/
- Silicon Analysts (JPMorgan), "CoWoS packaging cost" [STALE 2025-04], 2025-04. https://siliconanalysts.com/analysis/cowos-packaging-cost-chiplet-vs-monolithic-2026
- DigiTimes Taiwan, "TSMC CoPoS mass production delayed", 2026. https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=0000729902_XBLLCENFLJ1FFU3FJD9OK
- DigiTimes Taiwan, "TSMC delays release of 2027 advanced-packaging equipment orders", 2026 (~Q3). https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=766912
- TVBS News, "Nvidia reportedly selects CoPoS beyond Rubin", 2026. https://news.tvbs.com.tw/english/3123474
- TrendForce (citing Jeff Pu / Seeking Alpha), "Google TPU v8e and Meta CPU to adopt Intel EMIB", 2026. https://www.trendforce.com/news/?p=57840
- Wccftech (citing WIRED), "Intel EMIB challenges TSMC CoWoS", 2026. https://wccftech.com/intel-emib-challenges-tsmcs-cowos-as-america-answer-to-the-ai-packaging-bottleneck/amp/
- TrendForce, "CoWoP: a game changer beyond CoWoS or just hype?" [STALE 2025-07], 2025-07-30. https://www.trendforce.com/news/2025/07/30/news-cowop-a-game-changer-beyond-cowos-or-just-hype-pcb-makers-stay-skeptical/
- PYMNTS (summarising Goldman Sachs), "Hyperscaler capex growth to slow", 2026. https://www.pymnts.com/?p=4233514
- DatacenterDynamics, "US hyperscaler capex to top $700bn in 2026; investors fear overbuild (Moody's)", 2026. https://www.datacenterdynamics.com/en/news/us-hyperscaler-capex-to-top-700bn-in-2026-investors-fear-overbuild-and-weak-returns-moodys/
- 21st Century Business Herald, "SJ Semiconductor Lingang 2.5D/3D project breaks ground", 2026-07-13. https://www.sfccn.com/2026/7-13/1NMDE1MjBfMjE4MTE1Ng.html
- Shanghai Securities News, "SJ Semiconductor 2.5D share", 2026-04-21. https://paper.cnstock.com/html/2026-04/21/content_2202550.htm
- Stockstar, "SJ Semiconductor 1H26 results", 2026-08-20. https://wap.stockstar.com/detail/IG2026082000045199
- IBKR, company and price data (ASE/ASX, AMKR), 2026-10-14. n/a (terminal data)


---

### A.3 · Hit-to-kill interceptor solid propulsion: PAC-3 MSE two-pulse SRM + attitude-control motors and THAAD solid rocket boost motor
*Megatrend: Defense rearmament / integrated air and missile defense replenishment | 2026 -> 2030 revenue: $0.40-0.75B -> $0.9-2.0B | CAGR: 22-28% (central ~23%) | Growth mix: ~88% volume / ~12% price | Confidence: low (medium on the 2026 base and on direction)*

**Definition.** In: PAC-3 MSE solid two-pulse rocket motor (incl. igniters/ISDs) and solid attitude-control motor (ACM) set; THAAD solid rocket boost motor (SRBM); motor-supplier revenue for all customers, from L3Harris Missile Solutions (ex-Aerojet Rocketdyne) and qualified second sources (Northrop ABL). Out: THAAD liquid DACS and PAC-3 Lethality Enhancer (bundled in the same UCAs); structures and seekers; PAC-3 ACE's single-pulse motor (substitution); SM-x, ESSM, GEM-T, Aster, IRIS-T, CAMM, Asian interceptor motors (parent only); tactical, strategic, hypersonic, space motors; raw energetics.

**Value-chain path.** Defense rearmament -> integrated air and missile defense (Patriot lower tier, THAAD upper tier) -> hit-to-kill interceptors (prime Lockheed Martin, Camden AR / Troy AL) -> propulsion subsystem -> **solid rocket motors: PAC-3 MSE SRM + ACMs, THAAD SRBM** (L3Harris Camden AR / Orange VA / Huntsville AL; Northrop ABL, WV) -> sub-tier: ammonium perchlorate (AMPAC, single US source), HTPB, aluminum, nozzles, ISDs.

**Drill-down decision.** Parent (all NATO + allied interceptor-class SRMs): $1.2-2.0B -> $2.4-4.5B [E, low confidence; European/Asian parts not re-verified], CAGR 19-23% ((2.4/1.2)^(1/4)-1 = 18.9%; (4.5/2.0)^(1/4)-1 = 22.5%), central ~20% ($1.6B -> $3.3B). The 2030 low is cut from the draft's $3.0B because 434 of 540 FY27 SM-6 and 114 of 136 SM-3 IIA are reconciliation-funded [R]. I keep the PAC-3/THAAD slice because only its ramp is contracted at the motor tier (L3Harris $4.7B PAC-3 and >$6B THAAD propulsion UCAs, Sep 2026 [R]); after challenge its lead over the parent shrank from ~8 to ~3-4 points, on two programs and one supplier through ~2028 (use the parent if diversification matters). Rejected: Northrop second-source alone (share shift), ACMs alone (undisclosed), THAAD SRBM alone (borderline size, bundled with DACS).

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) [E] | $0.40-0.75B | $0.9-2.0B | 22-28% |
| Central [E] | $0.56B | $1.30B | 23.4% |
| of which PAC-3 MSE SRM + ACMs [E] | $0.30-0.53B (c. $0.41B) | $0.61-1.26B (c. $0.83B) | 19.5% (central) |
| of which THAAD SRBM [E] | $0.10-0.24B (c. $0.16B) | $0.28-0.74B (c. $0.47B) | 31.4% (central) |

CAGR math: low-low (0.9/0.40)^(1/4)-1 = 22.5%; high-high (2.0/0.75)^(1/4)-1 = 27.8%; central (1.30/0.56)^(1/4)-1 = 23.4%. Cross pairings (4.7-49.5%) are not coherent joint outcomes; dispersion is in the scenario table.

- **Volume vs price:** value multiple 1.30/0.56 = 2.30x; unit multiples 1,600/850 = 1.88x (PAC-3) and 310/120 = 2.58x (THAAD), 2026-value-weighted (72/28) = 2.08x; price/mix 1.11x, so ln(1.11)/ln(2.30) = ~12% price, ~88% volume [E]. Per-set price +2%/yr PAC-3 ($0.48M -> $0.52M), +3.6%/yr THAAD ($1.3M -> $1.5M): escalation, capex recovery, mix; not shortage pricing. Bear: definitization leaves price flat to -10%, growth ~100% volume.
- **Top-down** [E unless labelled]:
  - 2026: PAC-3 750-950 motor sets (620 missiles delivered 2025 [R]; ~700-800 missiles 2026; motors lead missiles 6-12 months) x $0.40-0.56M = $0.30-0.53B; THAAD 100-140 SRBMs (baseline ~96/yr [R]) x $0.95-1.7M = $0.10-0.24B. Total $0.40-0.77B.
  - 2030: PAC-3 1,350-2,000 sets x $0.45-0.63M = $0.61-1.26B (2,000/yr is an end-2030 exit rate [G], so on-schedule calendar 2030 is ~1,500-1,900; the low end adds slip and ACE displacing 10-20% of rounds); THAAD 250-400 x $1.1-1.85M = $0.28-0.74B. Total $0.88-2.00B.
  - Content: L3Harris PAC-3 UCA $4.7B [R] x ~93% ex-Lethality Enhancer = $4.37B / ~10,650-11,950 missiles = $0.37-0.41M/set; adding half to all of Northrop's $2B ceiling gives $0.45-0.60M. THAAD: >$6B [R] / 2,000-2,300 rounds [3P, unverified] = $2.6-3.0M SRBM+DACS, 21-32% of MDA FY24 flyaway $9.5-12.3M [STALE 2023-03], implying facilitization content; at 40-60% SRBM share, ~$1.0-1.8M.
- **Bottom-up:**
  - PAC-3 flyaway share: FY27 unit cost $4.36M Army ($12.2B/2,798), $4.20M Navy [R] (TWZ cites ~$5.3M, basis unverified) x propulsion 8-12% [E] (L3Harris-only $4.37B/$58.62B = 7.5%; full Northrop 10.9%). 2026: 750-950 x $4.3M x 8-12% = $0.26-0.49B. 2030: 1,350-2,000 x $4.65M x 8-12% = $0.50-1.12B (central $0.74B).
  - THAAD contract lot: 2026 = Feb-2026 ~$400M SRBM+LDACS lot [R] x 40-60% over 12-24 months = $0.10-0.20B. 2030 = $6B x 1.10 escalation x 40-60% x 15-19% of 7-year units = $0.40-0.75B (central $0.56B).
  - Totals: 2026 $0.36-0.69B; 2030 $0.90-1.87B (central $1.30B). Contract pool: L3Harris PAC-3 ~$0.62B/yr and THAAD SRBM ~$0.34-0.52B/yr on 7-year averages; the prime UCA runs through 2033 [R], so a back-loaded 2030 fits.
  - Supplier check (circular): MSL FY26 guide ~$4.1B [G], high-teens growth [G] -> $7.2-8.2B in 2030 (4.1 x 1.15^4 to 1.19^4); sub-niche = 10-18% of MSL (2026), ~11-25% (2030). "More than double by 2030" applies to the Aerojet segment ($2,845M in 2025 [R]), not MSL.
- **Reconciliation:** 2026 converges on $0.40-0.75B, central $0.56B. The draft ($0.45-0.70B) under-counted 2026 motor sets 10-20% (motor lead applied only to 2030) and mis-added its low end (700 x $0.45M = $0.315B). 2030: top-down $0.88-2.00B, bottom-up $0.90-1.87B -> $0.9-2.0B. The fact-check central ($1.50B, 27.9%) assumes reconciliation passes; bear weights pull lower, so the central is probability-weighted:

| Scenario | Prob. [E] | 2030 | CAGR from $0.56B |
|---|---|---|---|
| On track (reconciliation largely enacted) | ~40% | $1.4-2.1B (c. $1.6B) | 25.7-39.2% (c. 30.0%) |
| Soft bear (ramp slips to 2031-32, ~$60B partial reconciliation) | ~35% | $1.1-1.4B (c. $1.25B) | 18.4-25.7% |
| Hard bear (funding shortfall + ACE + price) | ~25% | $0.65-1.0B (c. $0.80B) | 3.8-15.6% (c. 9.3%) |
| Weighted: 0.4x1.6 + 0.35x1.25 + 0.25x0.8 | | ~$1.28B | 22.9% |

With the draft's uncorrected $1.8B on-track central, the bear case's own weighted figure is $1.36B (24.3% on $0.57B).

#### Demand drivers and catalysts
- **Replenishment:** Ukraine, Israel (June 2025) and the 2026 Iran conflict drew down stocks; the THAAD buy restocks Iran use [R]. FY27 request 3,203 PAC-3 MSE (Army 2,798 + Navy 405, first shipboard buy) [R]; 857 THAAD unverified (~$10.5B THAAD in reconciliation implies ~700-850 rounds [E]).
- **Funding, not only capacity, sets the pace (corrects the draft):** ~92% of FY27 PAC-3 quantities (2,936) and ~86% of all interceptor quantities sit in the $350B reconciliation request [R]; base funds 267 PAC-3 vs 310 in FY26 [R]. Lead times of 31 (PAC-3) and 34 months (THAAD) [R, attribution approximate] mean FY27-28 money sets 2029-30 output.
- **7-year contracting:** PAC-3 prime UCA up to $53.86B ($58.62B incl. April action) [R]; THAAD up to ~$35.3B, 96 -> 400/yr [R]; Northrop $2B PAC-3 + $1B THAAD frameworks are ceilings [R].
- **Allied floor:** 16+ PAC-3 customers; April 2026 action reportedly ~94% FMS [3P, unverified]; NATO 3.5% + 1.5% [STALE 2025-06].
- **Catalysts:** (1) FY27 appropriations/reconciliation, Dec 2026-Jan 2027: CR into at least December [3P]; House resolution ~$60B defense reconciliation vs $350B [R]; pending. (2) L3Harris UCA definitization, Q4-26/Q1-27 [G]; awarded Sep 8/29. (3) Lockheed UCA definitization, late 2026-27; awarded Jul 29/Jun 24. (4) Two Camden SRM plants online 2027 [G], building since June 2026; THAAD boost-motor plant 2027-28 [E]. (5) Northrop ABL PAC-3 qualification 2027-28 [E]. (6) PAC-3 ACE production "as early as 2028" [G], negative; Army FY28 budget Feb 2027. (7) MSL S-1, mid-2027 [R], first motor-level disclosure.

#### Supply side
- **Suppliers and shares:** L3Harris ~95-100% in 2026 (sole source), ~75-85% by 2030 [E]; Northrop <5% in 2026, 15-25% by 2030 if qualified (~$0.1-0.35B) [E]. ACE's motor supplier is unnamed [R].
- **Capacity and lead times:** L3Harris targets ~3x PAC-3 and 4x THAAD propulsion [G]; $1B DoW convertible preferred closed Apr 23, 2026 [R]; ~$3B SRM capex retained after the August CEO ouster [R]. Northrop ABL "nearly tripled" vs "plans to triple by 2027" (sources conflict). Greenfield explosive-sited plants take ~1.5-3 years [E].
- **Qualification barriers:** 2-4 years per new source [E]. Avio's $26M Mk 104 work [STALE 2025-09], production not before 2028-29; Ursa Major $10M Mk 104 to CDR/static fire (Jul 2026) [R]; no meaningful Northrop PAC-3 volume before ~2028 [E].
- **Geographic concentration:** ~100% US, overwhelmingly Camden AR (Highland Industrial Park, also Lockheed's assembly site); ABL WV from ~2028. German PAC-3 MSE work runs via a Lockheed-Diehl/MBDA MoU with US motors; the draft's COMLOG reference was wrong (COMLOG is the GEM-T JV). AP single-sourced (AMPAC).

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| L3Harris (Missile Solutions / Aerojet Rocketdyne) | LHX / NYSE | Incumbent, near-sole source | ~2-3% of LHX; ~10-18% of MSL (2026) [E] |
| Northrop Grumman | NOC / NYSE | PAC-3 SRM second source, ISDs | <0.2% (2026) -> ~0.6-1.0% (2030) [E] |
| Lockheed Martin | LMT / NYSE | Prime/customer; ACE developer | 0% as motor maker; propulsion ~8-12% of PAC-3 value, pass-through [E] |
| NewMarket (AMPAC) | NEU / NYSE | Sub-tier AP | Indirect, low single digit (unverified) |
| RTX; Avio; Hanwha Aerospace; IHI | RTX / NYSE; AVIO / BIT; 012450 / KRX; 7013 / TSE | Parent only | 0% |
| Nammo; Roxel; Anduril; Ursa Major; X-Bow | Private | Parent; potential ACE/second sources | 0% |

#### Bear case and key risks
- **Technology substitution:** PAC-3 ACE (unveiled Jul 20, 2026) targets under half MSE unit cost and still engages SRBMs [G]; single-pulse motor, cheaper casings, blast-frag warhead [R], so likely no ACM set; motor content ~25-40% of MSE [E]. Production "as early as 2028" [G]; no motor supplier named. FY27 prices MSE at ~$5.3M vs ~$4M historically [R], pushing budgets toward ACE. ACE plus cheap interceptors take 15-30% of new Patriot-family rounds by 2030, cutting 2030 PAC-3 propulsion value 10-20% [E]. The sub-$1M supplemental interceptor (30 finalists reported, unverified) is <5% of rounds by 2030 [E]. THAAD: no direct substitute by 2030; Golden Dome space/glide-phase layers compete for budget (unverified). "Low substitution risk" holds for physics, not unit mix.
- **Capex cuts:** ~90% of FY27 PAC-3 and ~84% of THAAD funding is in reconciliation [R]; the House sized it at ~$60B vs $350B [R]; a CR cannot raise rates without anomalies [3P]. UCAs are ceilings. Stress tests [E]: a 20-30% FY28 cut removes 15-20% of 2030 value; reconciliation failing or at ~$60B cuts 2029-30 deliveries 30-45% (2030 ~$1.0-1.25B); cancelling shipboard PAC-3 or capping THAAD removes another 10-15%. At 1,000-1,200 PAC-3/yr new plants run ~50-60% utilized, and the DoW (customer and 6.5% PIK preferred holder) gains price leverage.
- **Chinese capacity:** direct share 0% (ITAR, US qualification), the weakest leg. Indirect: Korean M-SAM wins in the UAE ($3.5B), Saudi Arabia ($3.2B) and Iraq (reported; not re-verified in this run), plus HQ-9B offers (unverified), divert ~5-10% of allied lower-tier demand [E]. Sept 2026 MOFCOM precursor licensing looks counter-narcotics; no energetics controls found [R].
- **Double-ordering / pull-forward:** the FY27 PAC-3 request is ~4-5x 2025 output, risking a 2030-31 air pocket. PAC-3 motor ceilings ($4.7B L3Harris, sized to "nearly triple" alone, + ~$2B Northrop) exceed the ~$4.8-5.3B a 10,650-missile ramp needs by ~30-40% [E]. Bear THAAD SRBM share 40-55% [E]. Some FMS slots are queue insurance (SAFE European preference, not re-verified). Pull-forward shows as prime backlog outrunning deliveries, not motor inventory.
- **Already priced in?** Narrative saturated, equities de-rated [R, IBKR 2026-10-14]: LHX $237.50 vs $232.61 52-week low and ~$366 March peak (-35%); NOC $494 vs $770 high; LMT ~$522 vs ~$692; Avio EUR26-34 vs EUR44.85 high. LHX forward P/E ~28x (Feb 2026) [3P] -> $237.50/$11.78 = ~20x [E; consensus unverified]. No pure play; the market leans bear on funding conversion, so headline awards carry little signal.
- **Other:** execution (Aerojet behind on SRMs [STALE 2024-07]; CEO ousted Aug 2026); single-site Camden.
- **Bear-case numbers:** hard bear 2030 $0.65-1.0B (central $0.80B) = PAC-3 1,000-1,200 x $0.45-0.55M ($0.45-0.66B) + THAAD 150-220 x $1.1-1.5M ($0.17-0.33B) [E]; CAGR ~3-15%, central (0.80/0.57)^(1/4)-1 = 8.8% (9.3% on the $0.56B base); probability ~25% (soft bear $1.1-1.4B, ~18-25%, ~35%). Parent hard bear $2.2-2.9B, ~7-18%. First warning sign: enacted FY27 quantities (Dec 2026-Jan 2027): a full-year CR without PAC-3/THAAD anomalies, or funding for fewer than ~1,000 PAC-3 MSE and ~150 THAAD.

#### Leading indicators to watch (next 2-4 quarters)
1. Enacted FY27 base + reconciliation + supplemental quantities vs 3,203 PAC-3 requested (base 267) and THAAD (Dec 2026-Jan 2027).
2. Definitized L3Harris PAC-3 UCA (bear trigger below ~$4.0B) and annual quantity schedule; any THAAD SRBM/DACS split (Q4-26/Q1-27).
3. Lockheed Jan-2027 call: 2027 PAC-3 guide ~1,000 = on track, below ~850-900 = slip; THAAD above ~150.
4. L3Harris Q3/Q4-26 MSL growth vs high-teens guide and ~$4.1B FY26; Camden plant milestones.
5. Army FY28 budget (Feb 2027): ACE procurement line, ACE motor source, MSE quantity trend.
6. Northrop ABL PAC-3 static fire/qualification lot; AMPAC AP capacity.

#### Confidence and biggest unknown
Low on 2030 magnitude; medium on the 2026 base and direction. Award values are reported facts but are ceilings. Biggest unknown: funded FY27-28 quantities, which set 2029-30 motor output given 31-34-month lead times; ~90% of FY27 PAC-3 money rides on an unenacted reconciliation bill. Next: definitized per-set price and the THAAD SRBM/DACS split (each ~+/-15% on 2030). No 2026 call transcripts were checked (Alpha Vantage rate-limited); MSL Q2-26 revenue ($1,054M) is unverified.

#### Sources
- L3Harris, "L3Harris Closes $1B Investment from Department of War in Missile Solutions", 2026-04-23. https://l3harris.com/newsroom/press-release/2026/04/l3harris-closes-1b-investment-department-war-missile-solutions
- L3Harris, "L3Harris 2Q26 Earnings Results", 2026-07-29. https://s205.q4cdn.com/565046976/files/doc_financials/2026/q2/L3Harris-2Q26-Earnings-Results.pdf
- L3Harris, "L3Harris Receives PAC-3 MSE Propulsion Contract (Arsenal of Freedom)", 2026-09-08. https://www.l3harris.com/newsroom/press-release/2026/09/l3harris-receives-pac-3-mse-propulsion-arsenal-of-freedom
- L3Harris, "L3Harris Receives Landmark PAC-3 MSE Propulsion Contract" (PDF), 2026-09-08. https://s205.q4cdn.com/565046976/files/doc_news/L3Harris-Receives-Landmark-PAC3-MSE-Propulsion-Contract-to-Power-Americas-Arsenal-of-Freedom-2026.pdf
- L3Harris, "L3Harris Receives THAAD Propulsion Contract Valued at More Than $6 Billion", 2026-09-29. https://www.l3harris.com/newsroom/press-release/2026/09/l3harris-receives-thaad-propulsion-contract-valued-6-billion
- Lockheed Martin, "Lockheed Martin and U.S. Government Reach Historic Deal to Turbo-Charge PAC-3 MSE Production", 2026-01. https://www.lockheedmartin.com/en-us/news/features/2026/Lockheed-Martin-and-U-S-Government-Reach-Historic-Deal-to-Turbo-Charge-PAC-3-Missile-Segment-Enhancement-MSE-Production-for-U-S-and-Allies.html
- Lockheed Martin, "Department of War Awards Lockheed Martin $58.62B for Multiyear PAC-3 MSE Production", 2026-07-29. https://www.lockheedmartin.com/en-sa/news/department-of-war-awards-lockheed-martin-58-62b-for-multiyear-pac-3-mse-production-to-strengthen-the-arsenal-of-freedom.html
- The Defense Post, "US to Boost THAAD Production", 2026-06-25. https://thedefensepost.com/2026/06/25/us-boost-thaad-production/
- The Defense Post, "PAC-3 MSE Production to Triple", 2026-01-07. https://thedefensepost.com/2026/01/07/pac-3-mse-triple-production/amp/
- Army Technology, "Lockheed Martin PAC-3 Missile Contract", 2026-07-29. https://www.army-technology.com/news/lockheed-martin-pac3-missile-contract/
- Defence Blog, "U.S. Defense Giant Lockheed Martin Posts Big Second-Quarter Gains", 2026-07-23. https://defence-blog.com/u-s-defense-giant-lockheed-martin-posts-big-second-quarter-gains/
- Breaking Defense, "Pentagon Inks Deal with L3Harris to Ramp Rocket Motor Production", 2026-07. https://breakingdefense.com/2026/07/pentagon-inks-deal-with-l3harris-to-ramp-rocket-motor-production/
- Breaking Defense, "L3Harris Postpones Missile Unit IPO Until Mid-2027", 2026-07. https://breakingdefense.com/2026/07/l3harris-postpones-missile-unit-ipo-until-mid-2027/
- Washington Technology, "L3Harris Presses Pause on Missile Solutions IPO Plan", 2026-07. https://washingtontechnology.com/companies/2026/07/l3harris-presses-pause-missile-solutions-ipo-plan/415121/
- Breaking Defense, "Kubasik Ousted as L3Harris CEO Following Conduct Violation, Company Says", 2026-08. https://breakingdefense.com/2026/08/kubasik-ousted-as-l3harris-ceo-following-conduct-violation-company-says/
- MarketBeat, "L3Harris Technologies Q2 Earnings Call Highlights", 2026-07-30. https://www.marketbeat.com/instant-alerts/l3harris-technologies-q2-earnings-call-highlights-2026-07-30/
- DefenseScoop, "Pentagon Inks $3B Framework Agreement for Patriot, THAAD Components", 2026-08-03. https://defensescoop.com/2026/08/03/pentagon-inks-3b-framework-agreement-for-patriot-thaad-components/
- Military & Aerospace Electronics, "DoD Signs Framework Agreements to Expand PAC-3, THAAD Interceptor Production Capacity", 2026-08-03. https://www.militaryaerospace.com/home/article/55395696/dod-signs-framework-agreements-to-expand-pac-3-thaad-interceptor-production-capacity
- The War Zone, "Here Is What Trump's Gargantuan $1.5T Defense Budget Has in It", 2026-04. https://www.twz.com/air/here-is-what-trumps-gargantuan-1-5t-defense-budget-has-in-it
- Defence-industry.eu, "U.S. Navy Requests 405 PAC-3 MSE Interceptors for Destroyers", 2026 (date unverified). https://defence-industry.eu/u-s-navy-requests-405-pac-3-mse-interceptors-for-destroyers/
- USNI News, "New Navy Budget Wants $3B for New Tomahawks, $4.3B for SM-6s", 2026-04-06. https://news.usni.org/2026/04/06/new-navy-budget-wants-3b-for-new-tomahawks-4-3b-for-sm-6s
- Forecast International, "How Congress Is Reshaping the Pentagon's FY27 Spending Plans", 2026-08-10. https://dsm.forecastinternational.com/2026/08/10/how-congress-is-reshaping-the-pentagons-fy27-spending-plans/
- NOTUS, "Trump Munitions Production and Congress Funding", 2026-08. https://www.notus.org/defense/trump-munitions-production-congress-funding
- CSIS, "Tracking FY2027 Defense Appropriations, Reconciliation, and the Supplemental Request", 2026-08/09 (exact date unverified). https://www.csis.org/analysis/tracking-fy-2027-defense-appropriations-reconciliation-and-supplemental-request
- Breaking Defense, "The Fight Over the FY27 Defense Budget Is On: 13 Key Issues for Congress to Resolve", 2026-08. https://breakingdefense.com/2026/08/the-fight-over-the-fy27-defense-budget-is-on-heres-13-key-issues-for-congress-to-resolve/
- Defense One, "We Can Buy More Weapons. We Can't Buy More Time", 2026-08. https://defenseone.com/ideas/2026/08/we-can-buy-more-weapons-we-cant-buy-more-time/415740
- Washington Times, "FY27 Topic Tracker", 2026-08. https://m.washingtontimes.com/topics/fy27/
- The War Zone, "PAC-3 Adapted Capability Effector Is Lockheed's New Low-Cost Patriot Interceptor", 2026-07. https://www.twz.com/land/pac-3-adapted-capability-effector-is-lockheeds-new-low-cost-patriot-interceptor
- Janes, "Farnborough 2026: PAC-3 ACE Low-Cost Interceptor Has Blast-Fragmentation Warhead", 2026-07. https://www.janes.com/defence-intelligence-insights/defence-news/weapons/farnborough-2026-pac-3-ace-low-cost-interceptor-has-blast-fragmentation-warhead
- Calibre Defence, PAC-3 ACE production timing (Reuters-sourced), 2026-07. https://www.calibredefence.co.uk/?p=7560
- Calibre Defence, "PAC-3 MSE: Lockheed and Diehl Sign MoU to Expand Production", undated. https://www.calibredefence.co.uk/pac-3-mse-lockheed-and-diehl-sign-mou-to-expand-production/
- The War Zone, "Cheap Patriot Interceptor Costing Under $1 Million Now Being Sought by Army", 2026 (month unverified). https://www.twz.com/land/cheap-patriot-interceptor-costing-under-1-million-now-being-sought-by-army
- Ground News (aggregator), "Cheaper Patriot Partners: US Army Names 30 Finalists", 2026 (unverified). https://ground.news/article/cheaper-patriot-partners-us-army-names-30-finalists
- RTX, "RTX's Raytheon Partners with Department of War on Five Landmark Agreements", 2026-02-04. https://www.rtx.com/news/news-center/2026/02/04/rtxs-raytheon-partners-with-department-of-war-on-five-landmark-agreements-to-exp
- Defense News, "MBDA to Double Aster Air Defense Missile Output in 2026", 2026-03-26. https://www.defensenews.com/global/europe/2026/03/26/mbda-to-double-aster-air-defense-missile-output-in-2026/
- Defense News, "Missile Maker MBDA Buys Safran's Stake in Rocket Engine Supplier Roxel", 2025-01 [STALE 2025-01]. https://www.defensenews.com/global/europe/2025/01/07/missile-maker-mbda-buys-safrans-stake-in-rocket-engine-supplier-roxel/
- Defense News, "Italy's Avio Is on Track to Make Standard Missile Motors for Raytheon", 2025-09 [STALE 2025-09]. https://www.defensenews.com/global/europe/2025/09/25/italys-avio-is-on-track-to-make-standard-missile-motors-for-raytheon/
- Il Sole 24 Ore, Avio H1-2026 results (revenue ~EUR276M, +17.5%), 2026-09. https://en.ilsole24ore.com/art/avio-reports-a-profit-of-92-million-175-per-cent-of-revenue-amounts-to-276-million-AJnfrT9
- Nammo, "Nammo Breaks Ground on New Rocket Motor Factory", 2025-10. https://www.nammo.com/nammo-breaks-ground-on-new-rocket-motor-factory/
- Militarnyi, IRIS-T manufacturer new production facility and 2026 plans, 2026. https://militarnyi.com/en/news/iris-t-manufacturer-launches-new-production-facility-and-plans-to-produce-10-air-defense-systems-in-2026/
- Sidae, Hanwha Aerospace L-SAM production contract, 2025-11. https://www.sidae.com/article/2025112810013269479
- The Defense Post, Ursa Major Mk 104 award, 2026-07-16. https://thedefensepost.com/2026/07/16/us-ursa-major-mk104/
- The Defense Post, X-Bow solid rocket motor contracts, 2024-06 [STALE 2024-06]. https://www.thedefensepost.com/2024/06/19/us-solid-rocket-motors-xbow/
- Breaking Defense, "Solid Rocket Motors Still a Challenge for L3Harris Subsidiary Aerojet: Lockheed, RTX Officials", 2024-07 [STALE 2024-07]. https://breakingdefense.com/2024/07/solid-rocket-motors-still-a-challenge-for-l3harris-subsidiary-aerojet-lockheed-and-rtx-officials
- Forecast International, FY2024 MDA THAAD procurement line item (MD07), 2023-03 [STALE 2023-03]. https://www.forecastinternational.com/budget_site/pdf/FY2024/0300D%5FLineItem%5FMD07%5FLI%2D31%2DTHAAD%5FFY2024.pdf
- ChemRadar, MOFCOM precursor-chemical export licensing catalog, 2026-09. https://www.chemradar.com/en/lawinfo/detail/fz095r93hips
- TIKR, "The Pentagon Invested $1 Billion in L3Harris: Here's What Analysts Say", 2026-03. https://www.tikr.com/blog/the-pentagon-invested-1-billion-in-l3harris-heres-what-analysts-say
- ClearanceJobs, "This Defense Giant's Upcoming IPO Could Be a Massive Windfall for Investors", 2026-02-12. https://news.clearancejobs.com/2026/02/12/this-defense-giants-upcoming-ipo-could-be-a-massive-windfall-for-investors/
- Interactive Brokers (IBKR MCP), company connections and price data for LHX, NOC, LMT, AVIO, 2026-10-14. No public URL (tool data).


---

### A.4 · Low-CTE (T-glass-class) glass yarn and thin cloth for IC-substrate cores and prepregs
*Megatrend: AI accelerators and advanced packaging (larger, thicker FC-BGA substrates) | 2026 -> 2030 revenue: $0.13-0.32B -> $0.30-0.95B | CAGR: 14-31% (central ~22%) | Growth mix: ~120% volume / ~-20% price | Confidence: low on size, medium on direction*

**Definition.** In: glass fibre with CTE ~2.5-3.0 ppm/K (E-glass is ~5.5) and high modulus, i.e. Nittobo T-glass and comparable compositions. It is sold either as yarn to third-party weavers or as thin cloth (~10-200 um, 1017-2116-class styles) to core-laminate and prepreg makers. End uses are ABF FC-BGA cores (AI GPUs/ASICs, switch ASICs, server CPUs) and BT/FC-CSP thin cores (mobile/PC APs, some memory). Value is counted once, at the cloth sale. Out: low-Dk NE/NER cloth (L17); quartz cloth; E-glass, including filled low-CTE E-glass cores; separable 3-4 ppm "special-spec" grades; ABF film; laminate value-add; TGV glass-core panels; interposers; aerospace uses.

**Value-chain path.** AI accelerators, switch ASICs, server CPUs, mobile APs -> CoWoS-class / FC-BGA / FC-CSP packaging -> IC substrates (Ibiden, Unimicron, SEMCO, Kinsus) -> core laminates and prepregs (MGC, Resonac, Panasonic, Doosan) -> **low-CTE glass yarn and cloth** -> Pt-Rh bushings and high-purity oxide batch.

**Drill-down decision.** I kept the combined niche. The faster slice is cloth for 75-150 mm AI GPU/ASIC cores, about 55-60% of value [E]: roughly $0.11-0.13B in 2026 and $0.30-0.35B in 2030 (volume ~3.2x x ASP 0.85) [E]. That fails the size floor, has no path to $1B, and cannot be observed separately, because Nittobo shares furnaces and looms across AI, mobile and memory styles. Next-gen T-glass (as early as 2028 [3P]) has no revenue to size yet. Widening to low-Dk would merge in L17.

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $0.13-0.32B [E] | $0.30-0.95B [E] | 14-31% [E] |
| Central | ~$0.21B | ~$0.46B | (0.46/0.21)^(1/4)-1 = 21.7% |
| Severe bear (~25%) | $0.21B ($0.25B in the bear reviewer's base) | $0.19-0.30B ($0.22-0.36B on $0.25B) | -3% to +10% |

The base depends on Nittobo's undisclosed T-glass share; the 2026-30 multiple depends on capacity and price. So the CAGR range is taken from the multiple:
- 1.7x gives 1.7^(1/4)-1 = 14.2%.
- 3.0x gives 31.6%.
- The central 2.21x gives 21.9%.

The same range is reached from inside the stated size ranges: $0.18B -> $0.30B is 13.6%, and $0.32B -> $0.95B is 31.3%. The low corner, $0.13B x 1.7 = $0.22B, falls in the bear band. Fully crossing the range ends (-2% to +64%) has no meaning.

- **Volume vs price.**
  - *2025-26 was price-led.* Nittobo raised electronic glass-fibre prices ~20% in 2025 and T-glass prices ~30% in 2026 [3P, Commercial Times via TrendForce]. MGC raised all CCL and prepreg prices 30% from Apr-2026 [R]. Nittobo's Electronic Materials (EM) segment is guided +27% for FY3/27 [G], with almost no new capacity before Jan-Mar 2027.
  - That makes the +27% about 18-27 pts price/mix and 0-8 pts volume [E]. The 2026 T-glass ASP is about 1.2 x 1.3 = ~1.5x 2024 [E]. Nittobo says the hikes are "largely complete" [G].
  - *2026-30 is volume-led.* Volume 2.6x (range 2.2-3.2x) x like-for-like ASP 0.85 (0.75-1.0) = 2.21x. In logs, ln 2.6 = 0.96 and ln 0.85 = -0.16, so volume is ~120% of growth and price ~-20% [E].
- **Top-down** (fact-check model; all inputs [E]; no public T-glass $/m2 exists, so price is unverified).
  - 2026 area: AI ABF cores 16M packages x 0.008 m2 x 10 plies ÷ (0.72 utilisation x 0.65 yield) x 1.15 trim = 3.1M m2. HPC FC-BGA adds 1.3M m2 and BT/FC-CSP 0.9M m2, for 5.3M m2 (range 1.8-13.4).
  - 2026 revenue: 5.3M m2 x $21/m2 ($12-32) = **$0.11B** ($0.02-0.43B).
  - 2030 multiples: AI x3.6 (units 2.3 x body area 1.6 x plies 1.15 ÷ yield gain 1.1 x glass-core retention 0.93); HPC x1.75; BT x1.4. Weighted by the 59/24/17 mix, that is 2.78x.
  - Less ~6% more substitution from the bear evidence, volume is ~2.6x: 13.8M m2 x $17.9/m2 = ~$0.25B.
- **Bottom-up.**
  - 2026: EM FY3/27 guide ¥77.8B [G] x T-glass share 23-50% (central 36%) [E] = ¥17.9-38.9B.
    - x 0.96 to move from fiscal to calendar year [E], ÷ ¥145-150/$ = $115-257M (central ¥26.9B / 147 = $183M).
    - ÷ Nittobo value share 80-88% (central 86%) = **$0.13-0.32B (central $0.21B)**.
    - The implied non-Nittobo revenue ($16-64M) matches a supplier build-up [E, unverified]: Grace Fabric $10-35M, Taiwan Glass $3-15M, and Guangyuan, Unitika, AGY and Taishan together $4-20M.
  - 2030: Nittobo ¥26.9B x volume 2.1-2.6x x Nittobo ASP 0.80-0.95 = ¥45-66B, or $0.31-0.46B at ¥145.
    - The volume range assumes capacity of ~2.7x FY3/26 at 85-90% utilisation, against FY3/27 output of ~1.05x FY3/26.
    - ÷ a 72-85% value share gives $0.37-0.64B on the central base. Central case: ¥26.9B x 2.3 x 0.88 = ¥54B = $0.37B, ÷ 0.78 = **$0.48B**.
- **Reconciliation.**
  - The 2026 bottom-up central is about 2x the top-down. Closing the gap needs ~10M m2 at $21/m2, or ~$40/m2 at 5.3M m2.
  - $40/m2 is above the quartz/Low-Dk3 price ladder (~$20-24/m2 [3P] [STALE 2025-09]). So either the true area is about 2x the model, or T-glass is at the low end of its share of EM. I anchor on the bottom-up and let the top-down set the low end.
  - Two further risks sit inside the low end:
    - The segment base may be inflated by up to ~20% through inter-segment sales or re-segmentation. FY3/26 EM revenue of ¥61.4B [R] is +50% on ¥40.9B, while consolidated revenue grew 8.4%. The quoted 44.2% share implies a ~¥139B total against ¥118.2B reported. OP is the same ¥19.4B as in the older ¥49.3B version.
    - 5-15% of 2026 shipments may be channel inventory (bear inference).
  - For 2030 the methods agree: $0.46B from demand and $0.48B from capacity.
  - Generic research ($0.53B for 2026, pmarketresearch) uses a broader definition and is not used.

#### Demand drivers and catalysts
- **AI substrate area (main driver; in progress).** Body sizes reach 120x150 mm with more than 20 layers by 2027 [3P, Goldman Jul-2026, not re-verified]. Ibiden Electronics sales were ¥243.3B in FY3/26 [R] and are forecast at ¥330B for FY3/27 (+36%) [G]. Ibiden has ¥500B of capex (Gama ¥220B, Ono ¥280B) and guides to 2.5x AI-server substrate load by CY2028 [G, IBKR].
- **Shortage forecasts.**
  - DigiTimes: 10-20% T-glass gap in 2026 [3P].
  - Counterpoint: ABF gap ~10% in 2H26 and ~20% in 2027 [3P].
  - KGI: T-glass gaps of 22% in 2027 and 29% in 2028 [3P].
  - Unimicron: the new Japanese plant ships meaningfully only in 2028 [G, secondary press].
- **Mobile/PC APs on thin BT cores.** Apple and Qualcomm sought alternatives (Grace Fabric, Unitika) [3P, Nikkei via Mezha]. I assume 0.9-1.4x volume.
- **Nittobo H1 FY3/27 (early Nov-2026; pending).** Q1 revenue was ¥34.03B (+20.6%) and OP ¥7.94B (+84.8%) [R]. Full-year guidance was raised to ¥141B revenue and ¥30B OP [G]. Q1 x4 = ¥136B, which implies only modest 2H growth.
- **Fukushima ¥15B building.** It triples leading-edge-logic T-glass cloth output. Completion is due Dec-2026 and production Jan-Mar 2027 [G] [STALE 2025-08], with visible contribution around 3Q27 [3P, UDN]. No slip has been reported.
- **Company-wide 3x by FY3/29; Taiwan 2x by Mar-2028** [G via Nikkei/TrendForce, single source].
  - This is probably the same expansion as Fukushima, not an addition to it.
  - The ¥80B is total company capex under the FY3/25-FY3/28 plan, not extra T-glass spending.
  - The president says 3x "will not be enough". No further step is announced (possibly ~May-2027 [E]); a ¥120B figure is an unverified rumour.
- **Next-gen T-glass** as early as 2028, with Nvidia and Apple as possible customers [3P, Nikkei].
- **Offset: glass core** [3P]. Absolics reliability results are possible by end-2026; the SEMCO/Dongwoo JV starts 2H27; LG Innotek targets 2028; BOE entered in Sep-2026; Intel's own use is around 2030.

#### Supply side
- **Suppliers and shares (2026 value, [E]).** Nittobo holds ~80-88%. The ~90% cited by Nikkei/TrendForce [3P] is likely a volume share. Frost & Sullivan's 5.0% share for Grace Fabric (#3 in 2025) [3P] caps Nittobo at no more than 85-88%. Taiwan Glass has 2-5%, Guangyuan 1-5% (unverified), and Unitika, AGY and Taishan under 2% each. By 2030 Nittobo is at 72-85%.
- **Capacity and lead times.**
  - Nittobo: ~2.7x FY3/26 by FY3/29 [E from G]. Nan Ya is to make ~20% of Nittobo's glass fibre by 2027 [3P].
  - Guangyuan: targets 1M m/month from a ~US$1B Henan plant [G]. The RMB amount and unit basis are unverified. At 1.27 m width that is ~15M m2/yr, or 0.75-2.9x 2026 global area depending on $/m2.
  - Taiwan Glass: NT$2.25B to go from 4 to 12 high-end lines [G], mostly low-Dk.
  - Grace Fabric: dropped the 72M m Cangxi project and put RMB680M into Huangshi [R].
  - TechNews counts more than five T-glass suppliers [3P].
  - Lead times: a new furnace takes ~18-30 months [E]; looms are booked to ~2028 [3P] [STALE 2025-07]; cloth lead times went from 8 to 30+ weeks [3P] [STALE 2025-08].
  - Potential 2029 supply is 3.1-3.9x 2026 volume, against base demand of ~2.6x [E].
- **Qualification barriers.**
  - The path runs laminate maker -> substrate maker -> chip OEM and takes 12-24 months [E]. The barriers are composition, filament uniformity and defect density.
  - The barrier is already breached in places:
    - AMD's PCN XCN25005 moved some FPGA/SoC cores to an alternate T-glass [R].
    - Guangyuan ships to Panasonic and Resonac [R, Nikkei via TrendForce Jul-2026].
    - Taiwan Glass reportedly passed Ibiden and Resonac (media-reported, not company-confirmed).
  - The largest AI GPU cores are reportedly still Nittobo-only (unverified).
- **Geographic concentration.** About 85% of qualified melting is at one Japanese site, Fukushima. Entrants are in China and Taiwan. The niche carries single-site, energy and FX risk: ¥147 -> ¥160/$ cuts the USD size ~8%.

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| Nitto Boseki (Nittobo) | 3110 / TSE Prime | Dominant T-glass melter and weaver; price setter | ~13-28% [E] (¥17.9-38.9B of ¥141B guide); EM ~55% [G] |
| Grace Fabric Technology | 603256 / SSE (HK filing May-2026) | #3 in low-CTE cloth; batch shipments since mid-2026 | ≤10-12% [E] |
| Guangyuan New Material | Unlisted (ChiNext re-filed Jul-2026) | Chinese entrant shipping to Panasonic and Resonac | Unverified |
| Taiwan Glass Industrial | 1802 / TWSE | Taiwanese second source | <2% [E] |
| Unitika | 3103 / TSE | Small low-CTE source (Qualcomm) | <2% [E] |
| Sinoma Science & Technology (Taishan) | 002080 / SZSE | Mostly low-Dk; low-CTE status unverified | <1% [E] |
| Nan Ya Plastics | 1303 / TWSE | Contract glass fibre for Nittobo; laminates | <1% [E] |
| AGY | Private (US) | S-2-class yarn, mostly aerospace | Unverified, low |
| MGC / Resonac / Panasonic | 4182 / 4004 / 6752, TSE | Core-laminate and prepreg buyers | 0% (customers) |
| Ibiden | 4062 / TSE | Largest AI ABF substrate maker | 0% (end customer) |

#### Bear case and key risks
- **Technology substitution.** Together these take 15-30% of 2030 demand in the bear case, against 0-15% in the draft [E]. None bites before 2028.
  - *Glass core:* 10-20% of 2030 AI core area, or 12-25% of AI-ABF T-glass value, since it hits the bodies with the most plies.
  - *Filled E-glass/NE cores and 3-4 ppm cloth:* 5-10% of volume. AMD's PCN shows requalification happens; Zhen Ding's COO said "alternatives already exist" [STALE 2025-08].
  - *CoWoP and system-on-wafer:* 0-5% [STALE 2025-08, unverified].
  - *Quartz:* takes the top end if CTE targets approach ~2.0 ppm.
  - Net effect: AI-ABF volume is 15-25% below the no-substitution path.
- **Capex cuts.**
  - Scenario: AI capex plateaus in 2027 and is cut 20-30% in 2028 (25-35% probability [E]). That means 22-28M AI units in 2030 instead of 30-45M, and AI-ABF area of 1.6-2.0x.
  - Bullwhip: three inventory tiers turn a 20-30% end cut into a 30-45% cloth-order cut for 2-3 quarters. The 2021-22 "ABF shortage through 2026" became oversupply in 2023.
  - Nittobo at 3x would then run at ~50-60% utilisation, and 2028 revenue would trough at $0.18-0.24B.
- **Chinese capacity.**
  - Guangyuan already supplies Resonac and Panasonic, so the moat is breached at the laminate tier. Its target alone is about 0.75-1.1x 2026 global volume on the bear reviewer's area estimate.
  - Grace Fabric already has a 5% share, and Nan Ya's contract work weakens Nittobo's discipline.
  - Entrants price 20-40% below Nittobo (unverified). A two-tier market drags blended ASP even if Western AI programs exclude Chinese cloth.
- **Double-ordering / pull-forward.**
  - There is no direct evidence, but conditions are textbook: allocation, 30+ week lead times, serial hikes, and gap forecasts widening to 29%.
  - Bear estimate: 5-15% of 2026 shipments is inventory. Destocking would hit in 2H27-1H28, as Fukushima and entrant volume arrive.
  - Second sources qualified under duress (AMD, Apple, Qualcomm) will stay.
- **Already priced in?** Yes.
  - Nittobo (split-adjusted) went from ~¥1,500 in Oct-2025 to a ¥6,580 peak on 7-May-2026, and was ~¥3,050 on 15-Oct-2026. That is -54% from the peak and ~2x year on year [R, IBKR], at a forward P/E of ~28x [R, Monex]. It fell ~21% in the week of the +27% guide and did not recover on the August beat.
  - Grace Fabric fell from RMB304 to ~RMB107 [R, IBKR].
  - Both Chinese suppliers are raising capital at the top: Grace Fabric filed in Hong Kong and Guangyuan re-filed for ChiNext.
  - The 2026-27 shortage is consensus. The open debate is the 2028-30 price path.
- **Bear-case numbers.**
  - *Size and CAGR:* 2030 at $0.22-0.36B (central $0.30B) on a $0.25B base, a multiple of 0.9-1.45x (volume 1.4-1.8x x net ASP -20% to -35%). On this section's $0.21B base, the same multiple gives $0.19-0.30B. The CAGR is -3% to +10%, central 1.2^(1/4)-1 = 4.7%.
  - *Probability:* ~25% (20-30%). It needs two of three: a 2027-28 capex cut, Chinese or Taiwanese qualification at scale, and glass core or CoWoP at the top end.
  - *Reviewer's distribution:* the reviewer puts ~50% on a CAGR below 16% and a probability-weighted ~16-17% (bear 25% at 5%, price erosion 40% at 12-16%, bull 35% at 24-30%). Taken literally, 12-16% needs a 1.57-1.81x multiple, i.e. ASP -25% to -40% at 2.4-2.6x volume.
  - *My weighting:* 25% bear at 1.2x plus 75% central at 2.21x gives E[2030] ≈ $0.41B, a CAGR of ~18%.
  - *First warning sign:* Apr-2027 contract prices and lead times, visible Dec-2026 to Mar-2027. Watch for flat Nittobo prices or volume discounts; MGC's +30% not extended, or rolled back; laminate lead times falling toward 12 weeks or less; or entrants quoting 20% or more below Nittobo. Hard confirmation would be a QoQ fall in Nittobo EM revenue in Q4 FY3/27 (May-2027) despite new capacity.

#### Leading indicators to watch (next 2-4 quarters)
1. Nittobo H1 FY3/27 (early Nov-2026): EM run-rate against the ¥77.8B guide; segment margin against ~36%; any wording on customer inventory, easing allocation, or a T-glass mix shift toward BT.
2. Grace Fabric Q3-26 (late Oct-2026) gross margin. Guangyuan's ChiNext prospectus, which would be the first disclosure of its T-glass revenue and capacity.
3. Apr-2027 contract cycle: Nittobo T-glass prices, MGC/Resonac/Nan Ya laminate notices, and lead times.
4. Fukushima start-up (Jan-Mar 2027), Nittobo Q4 FY3/27 EM revenue QoQ, and any new furnace with the May-2027 results.
5. Unimicron, Kinsus and Nan Ya PCB monthly sales and ABF price commentary; new chip-OEM PCNs naming alternate T-glass.
6. Absolics reliability results (by end-2026) and any Nvidia, AMD or Broadcom glass-core design win.

#### Confidence and biggest unknown
Confidence is low on size and medium on direction.

The biggest unknown is the 2026 base, and how much of it is shortage price and channel inventory. Nittobo does not disclose T-glass revenue. Its share of an EM segment whose own denominator is inconsistent (23-50%) swings the base from $0.13B to $0.32B, and no public $/m2 price exists to cross-check it.

The second swing factor is the 2029-30 price path:
- If Nittobo's ~3x plus Guangyuan, Grace Fabric and Taiwan Glass outrun ~2.6x demand, ASP falls 25% or more and the CAGR is 14% or less.
- If demand absorbs the new supply, ASP holds and the CAGR is ~31%.

The niche clears the $200M floor only marginally.

#### Sources
- TrendForce, "Nittobo raises FY2027 net profit forecast by JPY 3B, no further T-glass price hikes planned", 2026-08-06. https://www.trendforce.com/news/2026/08/06/news-nittobo-raises-fy2027-net-profit-forecast-by-jpy-3b-no-further-t-glass-price-hikes-planned/
- Nittobo via JPX/TDnet, "Q1 FY3/27 kessan tanshin", 2026-08-05. https://www2.jpx.co.jp/disc/31100/081220260805509788_tse-qcedjpsm-31100-20260805331100-ixbrl.htm
- kabuyoho.jp, "Nitto Boseki (3110) segment table", 2026-05/06. https://kabuyoho.jp/reportTop?bcode=3110
- EDINET DB, "Nitto Boseki FY2026 earnings", 2026-05-12. https://edinetdb.jp/company/E00542/earnings/FY2026
- Nikkan Kogyo Newswitch, "Nittobo Fukushima T-glass cloth expansion", 2025-08-29 [STALE 2025-08]. https://newswitch.jp/p/47097
- TrendForce (citing Nikkei), "Nittobo capacity to triple by FY3/29", 2026-08. https://www.trendforce.com/news/?p=62198
- TrendForce (citing Nikkei), "Nittobo reportedly plans 2028 next-gen T-glass; customers may include Nvidia, Apple", 2026-02-04. https://www.trendforce.com/news/2026/02/04/news-nittobo-reportedly-plans-2028-next-gen-t-glass-customers-may-include-nvidia-apple-and-others/
- TrendForce (citing Commercial Times), "Raw material inflation deepens as Fulltech hikes glass fiber cloth prices up to 30%", 2026-06-30. https://www.trendforce.com/news/2026/06/30/news-raw-material-inflation-deepens-as-fulltech-hikes-glass-fiber-cloth-prices-up-to-30-vpec-adjusts-epi-wafers/
- TrendForce (citing Nikkei), "China's chip material suppliers challenge Japanese dominance; Guangyuan invests US$1B in T-glass", 2026-07-03. https://www.trendforce.com/news/2026/07/03/news-chinas-chip-material-suppliers-challenge-japanese-dominance-guangyuan-invests-us1b-in-t-glass/
- TrendForce, "Nittobo expands glass fiber output with Nan Ya; Nan Ya to handle 20% by 2027", 2025-11-28. https://trendforce.com/news/2025/11/28/news-nittobo-expands-glass-fiber-output-with-nan-ya-nan-ya-to-handle-20-by-2027-amid-ai-surge
- TrendForce, "BOE joins glass substrate race", 2026-09-23. https://www.trendforce.com/news/2026/09/23/news-boe-joins-glass-substrate-race/
- Commercial Times (wantrich), "MGC raises CCL/prepreg/CRS prices 30%", 2026-03-03. https://wantrich.chinatimes.com/news/20260303900441-420201
- Commercial Times (wantrich), "Electronic glass cloth price ladder", 2025-09-09 [STALE 2025-09]. https://wantrich.chinatimes.com/news/20250909900249-420101
- Commercial Times (wantrich), "Glass cloth gap and lead times", 2025-08-18 [STALE 2025-08]. https://wantrich.chinatimes.com/news/20250818900003-420101
- Commercial Times (ctee), "Unimicron on T-glass and ABF tightness", 2026-04-03. https://www.ctee.com.tw/news/20260403700162-430502
- UDN, "Taiwan Glass investor conference", 2025-11. https://udn.com/news/story/7252/9152772
- UDN Money, "Kinsus rating upgrade; Nittobo capacity visible ~3Q27", 2026. https://money.udn.com/money/story/5607/9459664
- UDN, "Zhen Ding investor conference", 2025-08 [STALE 2025-08]. https://udn.com/news/story/7253/8934404
- DigiTimes, "Taiwan substrate makers expect 10-20% T-glass gap in 2026", 2025-11-20. https://www.digitimes.com/news/a20251120PD212.html
- Tiger Brokers (Goldman Sachs note), "ABF supply/demand and pricing", 2026-07. https://www.itiger.com/news/1119540282
- Counterpoint Research, "From T-Glass Crisis to Capacity Erosion: The Multi-Year Substrate Shortage", 2026-03. https://counterpointresearch.com/en/reports/From-T-Glass-Crisis-Capacity-Erosion-The-Multi-Year-Substrate-Shortage
- KGI, "PCB sector report", 2026-07-20. https://www.kgi.com.hk/zh-cn/-/media/files/kgishk/research-reports/tw-reports/pcb-sector_20260720e.pdf
- AMD, "PCN XCN25005: alternate T-glass cloth for package substrates", 2025-12. https://docs.amd.com/v/u/en-US/XCN25005
- Xinhua Finance (cnfin), "Grace Fabric 2026 interim report", 2026-08-13. https://www.cnfin.com/gs-lb/detail/20260813/4454931_1.html
- Huaan Securities via 10jqka, "Grace Fabric initiation", 2026-07-02. https://stock.10jqka.com.cn/20260702/c677896123.shtml
- Sina Finance / Zhitong Caijing, "Grace Fabric HK listing filing (Frost & Sullivan data)", 2026-05. https://cj.sina.com.cn/articles/view/5835524730/15bd30a7a020025up8
- Lanjinger, "Grace Fabric terminates Cangxi project, injects RMB680M into Huangshi Honghe", 2026-08. https://www.lanjinger.com/d/1786714372128728094
- cnyes, "Guangyuan chairman on T-glass", 2026-07. https://hao.cnyes.com/post/260309
- TechNews, "T-glass supply now more than five suppliers", 2026-08-28. https://finance.technews.tw/2026/08/28/cowososat/
- Tom's Hardware, "Glass substrate roadmap examined", 2026. https://tomshardware.com/tech-industry/manufacturing/glass-substrate-roadmap-examined
- Mezha (citing Nikkei Asia), "Apple, Qualcomm chip components shortage due to AI", 2026-01. https://mezha.ua/en/news/apple-qualcomm-chip-components-shortage-due-to-ai-307738/
- Semiconsam, "Urgent check on glass fiber", 2026. https://semiconsam.substack.com/p/urgent-check-on-glass-fiber
- Monex Scouter, "Nitto Boseki (3110) chart and valuation", 2026-09-28. https://scouter.monex.co.jp/report/chart/3110
- IBKR, "Company connections and price history: Ibiden (4062), Nitto Boseki (3110), Grace Fabric (603256)", accessed 2026-10-15. No public URL.
- pmarketresearch, "Low-CTE glass cloth market" (low quality; not used for sizing), 2025-2026. https://pmarketresearch.com/?p=2309286


---

### A.5 · AC-to-800 VDC / ±400 VDC conversion equipment for AI data halls (power racks/sidecars, centralised LV rectifiers, DC-use MV SSTs)
*Megatrend: AI data-centre power moving to 800 VDC / ±400 VDC distribution | 2026 -> 2030 revenue: $0.04-0.18B -> $1.0-6.0B | CAGR: 124-140% (scenario-consistent; central ~136%; 2027-30 only ~49-71%) | Growth mix: ~125% volume / ~-25% price | Confidence: Low*

**Definition.** In: equipment that converts facility AC (415/480 VAC, or 10-35 kV MV) into an 800 VDC or ±400 VDC bus that feeds AI racks. Four parts:
1. Row-level power racks/sidecars: rectifier shelves, controls and DC busway/protection. This covers Nvidia-ecosystem 800 VDC racks and OCP Diablo-400 ±400 VDC racks.
2. Centralised hall or pod LV rectifier skids.
3. MV solid-state transformers (SSTs) sold for 800 VDC data-centre use, counted at full value.
4. DC protection bundled with any of the above.

Revenue is counted at the system vendor, with SiC embedded.

Out:
- BBU and supercapacitors in sidecars (L09).
- AC-fed 54 V shelves and PSUs, including the Vera Rubin 110 kW power rack.
- In-rack 800 V-to-12/48 V DC-DC converters.
- UPS, switchgear and conventional transformers.
- China's 240/336 V HVDC.
- SSTs for EV charging or the grid.
- Native-DC on-site generation, which is a substitute.

Caveat: part of this revenue migrates from in-rack PSUs. Full-value SSTs also absorb transformer and UPS value that is excluded elsewhere, so check for overlap with any grid-SST or transformer niche.

**Value-chain path.** AI data centres -> facility power distribution -> 800 VDC / ±400 VDC DC architecture -> **AC-to-DC conversion step**. The step moves from sidecars (2026-28) to centralised LV rectifiers (2027-28+) to SST-native halls (2029+). Inputs: SiC devices, magnetics, power ICs and DC protection.

**Drill-down decision.** I kept the conversion-step level because the same function migrates across three architectures; measuring the step avoids betting on one. Three narrower cuts were tested:
- **(a) DC-use MV SSTs: fastest on paper, rejected as a separate niche.** 2026 is pilots only: Eaton ~10 pilots [G], Sungrow samples [G], Heron pilot production in early 2027 [R]. Both published anchors fail checks:
  - Huaan's RMB2.8B (2026) -> RMB101B (2030) [3P] must be all-application: RMB2.8B ≈ $0.39B, more than all 2026 data-centre conversion revenue.
  - Citi's 37,152 MVA for 2030 [3P, date unverified] exceeds Citi's own "25+ GW" of 800 VDC additions.
  - Own estimate: ~20% of 2030 DC-fed MW (2-7 GW) x $0.15-0.30M/MW = ~$0.3-2B [E]. KGI's view that SSTs need "5+ years" [3P, STALE 2025-09] and Hitachi Energy/SPOC's comment that SSTs are not mature [3P] support keeping the share small.
  - Revisit if Sungrow or Eaton firm orders exceed 1 GW by mid-2027.
- **(b) ±400 VDC Diablo racks:** they ship first, but they converge on the same vendors and technology, so they do not grow faster.
- **(c) Solid-state DC breakers:** sub-scale and not separable from the rectifier bill of materials.

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $0.04-0.18B [E] | $1.0-6.0B [E] | 124-140% (scenario-consistent) |
| Central | ~$0.08B | ~$2.5B | ~136% |
| Cross-corner envelope | | | 54-250% |
| Memo: from 2027 base $0.3-1.2B [E] | | | 3-yr 49-71% (central ~57%) |
| Bear (~20-25% prob.) | $0.08-0.15B | $0.25-0.9B | ~24-72% (central ~50%) |

CAGR math:
- Scenario-consistent: (1.0/0.04)^0.25-1 = 124%; (6.0/0.18)^0.25-1 = 140%; central (2.5/0.08)^0.25-1 = 136%.
- Corners: (1.0/0.18)^0.25-1 = 54%; (6.0/0.04)^0.25-1 = 250%.
- 2027-30: (1.0/0.3)^(1/3)-1 = 49%; (6/1.2)^(1/3)-1 = 71%; central (2.5/0.65)^(1/3)-1 = 57%.

- **Volume vs price:** All of the growth is adoption volume; price is a headwind. All figures [E]:
  - Volume: shipped conversion capacity rises from ~0.25 GW (0.07-0.45) in 2026 to ~18 GW (10-35) in 2030. That is 72x, or 2.91x per year.
  - Price: blended conversion-only $/MW falls from ~$0.32M (0.22-0.40) to ~$0.14M (0.10-0.18). That is 0.44x, or 0.81x per year (~-19%/yr).
  - Combined: 2.91 x 0.81 = 2.37, i.e. ~137% (central check: 18 x 0.14 = $2.52B). In log terms volume contributes ~124% of growth and price ~-24%.
  - Price direction is contested. An SST-heavy mix could slow the decline to -8 to -12%/yr, since SSTs still cost "several times" conventional gear [3P, Jiemian]; that would be value pulled in from excluded categories. The bear case has -25-30%/yr after 2027.
  - No shortage pricing: the binding constraints are qualification, power ICs and standards, not capacity.
- **Top-down:**
  - **2026:**
    - Optional Vera Rubin 800 V racks (<500 units in 2H26 [3P]; MW per unit ambiguous): 0.03-0.2 GW.
    - Diablo-class ±400 VDC racks: 0.03-0.2 GW.
    - Pilots: 0.01-0.05 GW.
    - Total 0.07-0.45 GW x $0.22-0.40M/MW = $0.015-0.18B; central 0.25 x 0.32 = $0.08B [E].
    - The price is capped at $0.40M/MW because SemiAnalysis' ~$0.5M/MW sidecar price includes BBU/supercaps [3P]. GB200 in-rack power at ~$0.3M/MW [3P, STALE 2025-07] is only a loose check (different scope).
  - **2030:** new AI IT capacity x 800/±400 VDC share x conversion-only $/MW [E].
    - New AI IT capacity: 22-55 GW, central 35. Anchors: JLL 103 -> 200 GW by 2030, ≈19 GW/yr average and ~25-30 GW in 2030 [3P]; Citi-implied ~32 GW [3P]. High-side: Industrial Securities 69.9 GW and Structure Research ~150 GW of AI capacity by 2030 [3P].
    - 800/±400 VDC share: 30-65%, central 50%, net of 0-10% native-DC supply.
    - Price: $0.10-0.18M/MW.
    - Result: low 22 x 0.30 x 0.10 = $0.66B; high 55 x 0.65 x 0.18 = $6.4B; central 35 x 0.50 x 0.14 = $2.45B.
- **Bottom-up:**
  - **2026 supplier sum:**
    - Delta: power cabinets are <1% of 2026 revenue (<~NT$7B, ~$0.23B) [3P, TechNews], and that includes BBU. Q4 volumes are "limited" [G], so NT$1-5B, less 25-40% for BBU = NT$0.7-3.5B = $0.02-0.11B [E].
    - Lite-On: <$0.02B [E].
    - Vertiv, Eaton, Schneider, Siemens and ABB combined: <$0.03B [E].
    - China 800 V and SST: <$0.02B. Even 30 MW from Sungrow at RMB1.5-3/W is only $6-13M [E].
    - Total: $0.03-0.18B.
  - **2030 platform build [E]:**
    - Nvidia rack-scale: 15-30 GW x 50-85% DC = 7.5-25 GW.
    - Hyperscaler ASIC racks: 8-18 GW x 30-60% = 2.4-11 GW.
    - China AIDC: 5-12 GW x 5-25% = 0.25-3 GW.
    - Total ~10-40 GW (central 22) x $0.11-0.19M = $1.1-7.6B; central 22 x 0.15 = $3.3B.
  - **2030 vendor sum [E]** (anchored to the above, not independent): Delta $0.35-2.0B, Vertiv $0.15-1.2B, Eaton $0.1-0.8B, Lite-On $0.1-0.5B, Schneider $0.05-0.5B, Siemens/ABB/Hitachi/Flex $0.05-0.4B, China $0.1-0.8B, start-ups $0.02-0.3B. Sum: $0.9-6.5B.
- **Reconciliation:**
  - **2026:** both methods centre on $0.06-0.08B. Published $0.04-0.18B. This is below the $200M floor, so the niche qualifies only on the path-to-$1B test.
  - **2030 central ~$2.5B:** this leans to the top-down ($2.45B) over the platform build ($3.3B). The build's 50-85% Nvidia DC share predates three pieces of bear evidence: the Kyber slip, HVDC being optional on Vera Rubin, and UBS's capex decay.
  - **2030 low end $1.0B:** cut from the fact-check's $1.5B because the fact-check (P(<$1B) 10-15%) and the bear case (20-35%) disagree without decisive evidence. $1.0-6.0B is roughly P20-P90.
  - **Versus the draft ($2-7B):** the fact-check's JLL denominator overrides the draft's 35-60 GW, which excluded its own Citi bracket.
  - **Ranking caveat:** a one-quarter shift in when Delta books Q4-26 revenue moves the 2026-30 CAGR by 20-40 points. Rank on the 2027-30 CAGR.

#### Demand drivers and catalysts
- **Rack density (structural, 2027-29):** GB300 ~140 kW, Vera Rubin ~190-300 kW, Kyber/Rubin Ultra 600 kW-1 MW per rack [3P]. 54 V busbars hit copper and space limits above ~200-300 kW [E]. Nvidia: 800 VDC carries >150% more power through the same copper [G].
- **OCP Diablo-400 (Microsoft/Meta/Google):** v0.7 published 2026-03-01 [R]. v1.0 and production-hall news are possible at OCP Global Summit, 12-15 Oct 2026; the summit is in progress and nothing has been found yet.
- **Delta:** ±400 VDC mass production began Q3-26, with small shipments in Q4-26; 2027 is the main 800 VDC year [G, CTEE/SinoPac]. Some Q3-26 shipments were deferred by a power-IC/component shortage [3P]. Status: in progress.
- **Nvidia 800 V HVDC Power Rack:** optional for Vera Rubin, stock from 3Q26 [3P, TrendForce]. ~10% of Vera Rubin (~6,000 racks) expected in 2027 [3P, Want Rich]. Status: small and optional.
- **Kyber NVL144 (first 800 VDC-native platform):** reportedly slipped more than 12 months to 2028 [3P, SemiAnalysis]. Nvidia says its "roadmap is intact", which does not address Kyber specifically. Confirmation point: GTC, March 2027.
- **Vertiv MV-AC-to-800 VDC:** the investor-day plan was validation 2026 and deployment 2027 [G]. A Q2-26 call note says validation 2027 and deployment 2028 [3P, Call Sheet Daily]. Status: contested; I assume meaningful revenue from 2028.
- **Eaton:** ~10 SST pilots including hyperscalers; already quoting 800 VDC projects; orders expected 2H26; shipments late 2027-early 2028 [G]. Infineon will supply SiC for MVSST 2.0 (Sept 2026) [R].
- **Sungrow EnerNeo SST:** launched 2026-07-09. Framework agreements of >130 MW [G]: ≈30 MW for Dongyangguang (2026-27) and ≈100 MW for Zhonglian (2027-28). Batch orders expected 2027.
- **Lite-On and Heron:** Lite-On launches its 800 VDC rack in Q4-26 [3P]; Heron's pilot SST production starts early 2027 [R].
- **Capex envelope:** Dell'Oro sees >$3T of data-centre capex by 2030 [3P, month unverified]. UBS sees hyperscaler capex +76% in 2026 ($673B), then +25% in 2027 and +6% in 2028 [3P].

#### Supply side
- **Suppliers and shares:** all own estimates, unverified.
  - 2026-27 merchant power racks: Delta ~35-50%, Lite-On ~8-15%; Vertiv ~10-20% from 2028.
  - 2030: Delta 25-35%, Vertiv 10-20%, Eaton 5-15% (SST-weighted), Schneider 5-10%, Siemens/ABB/Hitachi 2-10%, Chinese vendors 5-15% (mostly domestic), start-ups 1-5%.
  - ODMs (Foxconn, Quanta, Wiwynn, Flex) can build to the open Diablo spec.
- **Capacity and lead times:** capacity is not binding.
  - Sungrow plans 1.2 GW of SST capacity by end-2026 [G]. That is 2.7-17x the whole 2026 global estimate of 0.07-0.45 GW.
  - Heron has a 40 GW US factory plan [R]. Delta has three new Thailand plants [R].
  - Lite-On's NT$2.4B Vietnam capex is for 18.3/110 kW AC shelves, i.e. the substitute [R].
  - Eaton is building flexible lines that can make UPS units or SSTs [G].
  - Lead times are unverified. Data-centre power backlogs are long in general: Vertiv ~$15B [R]; Eaton Electrical Americas book-to-bill 1.3 [R].
- **Qualification barriers:**
  - Nvidia's 20+ MGX 800 VDC partners [R, STALE 2025-10] are a list, not contracts.
  - Diablo is still v0.7.
  - Treatment of >600 VDC in white space under UL/IEC/NEC, DC arc-fault protection and insurer acceptance are all immature.
  - Sample to volume takes ~12-24 months [E]; Vertiv's own cadence is ~1 year from validation to deployment [G].
  - Eaton's MVSST 2.0 is among the first MV SSTs with IEC certification [R].
  - These barriers favour Nvidia and hyperscaler reference vendors in the US and are lower for Chinese vendors inside China.
- **Geographic concentration:**
  - Taiwan-headquartered Delta and Lite-On ship >50% of 2026-27 merchant volume [E], assembled in Thailand, Vietnam, China and Mexico, which carries tariff exposure.
  - Demand is ~65-80% US hyperscalers and neoclouds in 2027-30 [E].
  - China runs mostly on out-of-scope 240/336 V HVDC.
  - SiC comes from Infineon, onsemi, Wolfspeed, ST and Chinese fabs.

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| Delta Electronics | 2308 / TWSE | Lead 800/±400 VDC power-rack vendor; SST targeted for 2028 | 2026: <1% including BBU [3P]. 2027: ~0.5-2% conversion-only [E], vs the street's 5-10% "power-rack-related" [3P], which includes BBU and AC-fed racks. 2030: ~1-5% [E] |
| Lite-On Technology | 2301 / TWSE | No. 2 Taiwan rack-power vendor; 800 VDC rack and BBU | 2026: <1% [E]. 2027: ~0.5-3% conversion-only [E], vs "mid-single-digit" HVDC including BBU [3P] |
| Vertiv | VRT / NYSE | MV-AC-to-800 VDC pod and hall systems; MGX reference | 2026: <0.5%. 2030: ~1-5% [E] |
| Eaton | ETN / NYSE | MV SST (Resilient Power) and DC breakers | 2026: ~0%. 2030: ~0.5-2% [E] |
| Schneider Electric | SU / Euronext Paris | 800 VDC sidecar for racks up to 1.2 MW, with Nvidia [G, STALE 2025-10] | <0.5% through 2027; ~0.5-1.5% in 2030 [E] |
| Siemens / ABB / Hitachi | SIE XETRA / ABBN SIX / 6501 TSE | Sidecars; SST with Reinhausen; ABB 800 VDC product unverified | ~0-0.5% [E] |
| Sungrow Power Supply | 300274 / SZSE | 10 kV-to-800 VDC SST | 2026: <0.5%. 2030: ~1-4% [E] |
| Megmeet / Kstar / Zhongheng | 002851 / 002518 / 002364, SZSE | China 800 V entrants. Kstar: no orders yet [G]. Zhongheng: mostly 240/336 V | ~0-5% [E] |
| Flex | FLEX / Nasdaq | Possible ODM builder of Diablo racks | <0.5% [E, unverified] |
| Infineon | IFX / XETRA | SiC supplier for Eaton MVSST 2.0 (device layer) | <1% [E] |
| Heron Power | Private | SST maker; 40 GW US factory plan | Data centres ~1/3 of business [R]; pre-volume |
| Enphase | ENPH / Nasdaq | Distributed SST | 0% until its 2028 volume target [G] |

#### Bear case and key risks
- **Technology substitution:**
  - **The status quo is shipping now.** AC racks with 54 V 110 kW shelves are in volume: Lite-On has shipped them since June 2026 [R].
    - Vera Rubin is built around a 110 kW power cabinet; analysts call 800 V "not a necessary configuration" [3P].
    - Two or three shelves cover ~200-350 kW racks [E].
    - If Kyber slips again or Rubin Ultra ships AC-fed, AC keeps ~75-85% of 2030 new AI capacity [E].
  - **Native-DC generation.** Bloom's fuel cells output 800 VDC directly.
    - Bloom claims a $3.6B (27%) cut in non-compute capex per GW [G, unverified]. Brookfield raised its Bloom commitment from $5B to $25B [R].
    - Native DC could take 5-15% of DC-fed capacity by 2030 [E].
  - **Cannibalisation inside the niche.**
    - SSTs collapse the LV rectifier stage.
    - The open Diablo spec lets ODMs commoditise rectifier modules.
    - Together these push pricing toward $0.07-0.12M/MW by 2030 [E].
- **Capex cuts:**
  - **Consensus already slows after 2026.**
    - UBS: hyperscaler capex +76%, +25%, +6% over 2026-28 [3P].
    - Goldman and Moody's: ~$1T in 2027, about a third debt-funded. S&P: only Microsoft FCF-positive in 2027 [3P, secondary].
  - **Bear scenario** (all [E]):
    - A 20-30% capex cut in 2028 gives 15-22 GW of new AI capacity in 2028 and 20-30 GW in 2030.
    - Operators finish AC-designed halls and defer DC halls first, because 800 VDC is the discretionary layer.
  - **Concentration risk:** if one hyperscaler drops Diablo, or Rubin Ultra ships mainly AC-fed, 20-40% of 2028-30 volume disappears [E].
- **Chinese capacity:**
  - **Capacity far exceeds orders.** Sungrow is building 1.2 GW against >130 MW of non-binding framework agreements [G].
    - Zhongheng claims the No. 1 share in AIDC HVDC and says its 800 V product is Kyber-compatible. CATL is taking a ~RMB4.1B stake in Zhongheng's controlling shareholder [3P].
    - Kstar has no 800 V orders or revenue yet [G].
    - Megmeet is in the GB300 PSU chain; its 800 V qualification is unverified.
  - **No US qualification yet.** None of these is qualified for US hyperscaler 800 VDC halls.
  - **The mechanism is price, not US share.** China stays on 240/336 V, so its 800 V vendors export to Gulf, Southeast Asian and Indian campuses (unverified). Conversion-only $/MW then falls -25-30%/yr after 2027 [E]. Lite-On's >30% sidecar gross margin [3P] would not survive.
- **Double-ordering / pull-forward:** no channel data exists (unverified). Three risks:
  - **Qualification-lot inflation:** <500 optional racks spread across many buyers [3P] and ~10 Eaton pilots [G]. If each hyperscaler narrows 3-5 vendors to 1-2, a 2027 ramp is followed by a pause [E].
  - **Duplicate component bookings:** after Delta's power-IC deferral and the capacitor swaps on some Vera Rubin batches [3P], buyers may double-book power ICs, capacitors and SiC.
  - **Front-loaded power backlogs:** Vertiv ~$15B and Bloom ~$20B [R, secondary]. Vertiv still missed Q2-26 revenue ($3.27B vs ~$3.38B consensus) [R].
  - Sidecars bought to future-proof Vera Rubin halls could sit idle if Kyber slips. This is a secondary driver with low evidence.
- **Already priced in?** The narrative is priced in; revenue is not visible yet.
  - **Share prices** (IBKR, ~2026-10-14) [R]:
    - Delta NT$1,630: +69% YTD, -37% from its high; -17% in the week of 12 Oct, cause unverified.
    - Vertiv $217: -43% from ~$380; -27.9% in July 2026.
    - Lite-On NT$271: -17% from high.
    - Eaton $405: -15% from high.
    - Bloom $230.6: +165% YTD.
  - **Valuation:** multiples unverified.
  - **Concept names:** Kstar and Zhongheng trade ahead of any 800 V revenue.
- **Bear-case numbers:**
  - **2030 size: $0.25-0.9B, central ~$0.43-0.5B [E].** Build: 20-30 GW x 15-25% DC x 85-95% needing rectification = 2.6-7.1 GW, x $0.07-0.12M/MW = $0.18-0.86B. Central: 25 x 0.20 x 0.9 x 0.095 = $0.43B.
  - **Severe tail: $0.15-0.3B, ~8-10% probability.** Requires Kyber in 2029 or later and AC holding >85% of new capacity.
  - **CAGR from a 2026 base of $0.08-0.15B: central ~50%.** Likely band (0.35/0.15)^0.25-1 = 24% to (0.7/0.08)^0.25-1 = 72%; central (0.5/0.1)^0.25-1 = 50%. Full corners ~6-106%.
    - At Delta's implied 2026 ceiling ($0.2-0.25B), only ~15-30%.
    - 2027-30 on a $0.2-0.5B base: ~0-45%.
  - **Probability:** the bear author puts the chance that 2030 lands at or below ~$1B at ~25% (20-35%); the fact-check puts it at 10-15%; I use ~20-25%.
  - **Size-floor failure:** in the bear case the niche misses both size tests (<$0.2B in 2026, <$1B in 2030) and exits the ranking universe.
  - **First warning sign:** Delta's Q3-26 call (late Oct-early Nov 2026). The bear is in play if management moves the main 800 VDC year to 2028, lets Q4-26 ±400 VDC shipments slip into 2027, or will not size 2027 HVDC revenue against the street's 5-10%.

#### Leading indicators to watch (next 2-4 quarters)
1. **Delta Q3-26 call and monthly sales:** Q4-26 HVDC volume and the scope of the "5-10% of 2027" estimate. If that figure is HVDC conversion only, my 2027 range ($0.3-1.2B) is 2-3x too low.
2. **Vertiv Q3-26 (late Oct) and Eaton Q3-26:** whether 800 VDC validation sits in 2026 or 2027, first SST purchase orders (Eaton guided orders in 2H26), and named hyperscalers.
3. **OCP Global Summit (12-15 Oct 2026) and OCP EMEA (spring 2027):** Diablo-400 v1.0 and Microsoft, Meta or Google ±400 VDC production halls.
4. **Hyperscaler Q3-26 calls:** 2027 capex growth against the UBS +25% path, and any DC-architecture commentary.
5. **Nvidia GTC (Mar 2027), Sungrow and KGI/TrendForce:** the Kyber date and whether 800 VDC becomes standard; Sungrow framework agreements turning into firm orders (Q4-26 to Q1-27); revisions to KGI's 10-20% 2027 penetration.

#### Confidence and biggest unknown
**Confidence: low.** No vendor discloses 800 VDC revenue, so every size is an own estimate triangulated from broker percentages that mix in BBU and AC racks. The 2026 base is below the size floor. The bear case (~20-25%) removes the niche from the universe. I read no primary transcripts (Alpha Vantage was rate-limited), so company guidance comes from secondary summaries.

What I am confident of: if adoption proceeds, the 2026-30 CAGR exceeds 100%. That is mechanical, because the base is near zero.

**Biggest unknown:** what share of 2029-30 new AI capacity runs on 800/±400 VDC. Estimates range from the bear's 15-25% through my 50% central to Citi's 79% (an outlier). The answer depends on Kyber timing and whether ASIC hyperscalers standardise on Diablo-400. Secondary unknowns are conversion-only $/MW once SSTs scale, and whether SST value should sit in this niche or a grid-equipment niche.

#### Sources
- Commercial Times (CTEE), "Delta Q2-2026 investor conference coverage", 2026-07-31. https://www.ctee.com.tw/news/20260731700091-430502
- SinoPac, "Delta Q1-26 investor conference summary (±400V ships 2026, 800V volume 2027)", 2026-04-30. https://www.sinotrade.com.tw/richclub/calendar/%E5%8F%B0%E9%81%94%E9%9B%BB%E6%B3%95%E8%AA%AA-Q1-EPS-7-91%E5%85%83%E6%94%B9%E5%AF%AB%E5%96%AE%E5%AD%A3%E7%B4%80%E9%8C%84-%C2%B1400V%E4%BB%8A%E5%B9%B4%E5%87%BA%E8%B2%A8-800V%E8%93%84%E5%8B%A22027%E5%B9%B4%E6%94%BE%E9%87%8F-%E8%82%A1%E5%B8%82%E8%A9%B1%E9%A1%8C-69f3237ae912b0007968ba63
- TechNews Finance, "Delta HVDC Q4 shipments; institutional estimate of 2027 power-rack revenue share", 2026-09-07. https://finance.technews.tw/2026/09/07/delta-electronics-hvdc-q4-shipments-institutional-investors-estimate-power-rack-revenue-share-2027-10-percent/
- Nasdaq, "Vertiv Q2 earnings call highlights", 2026-08-01. https://www.nasdaq.com/articles/vertiv-q2-earnings-call-highlights
- Call Sheet Daily, "VRT Q2'26 conference call notes", 2026-07/08. https://callsheetdaily.substack.com/p/vrt-q226-conference-call-notes
- Earnings Whispers, "VRT EPS details (2026 guidance)", 2026. https://earningswhispers.com/epsdetails/VRT/202606
- MarketBeat, "Vertiv trading down 17.3%", 2026-07-29. https://www.marketbeat.com/instant-alerts/vertiv-nysevrt-trading-down-173-should-you-sell-2026-07-29/
- Nasdaq / Motley Fool, "Why Vertiv Holdings plunged in July", 2026-08. https://www.nasdaq.com/articles/why-vertiv-holdings-plunged-july
- Motley Fool, "Eaton (ETN) Q1 2026 earnings call transcript", 2026-05-05. https://www.fool.com/earnings/call-transcripts/2026/05/05/eaton-etn-q1-2026-earnings-call-transcript/
- MarketBeat, "Eaton Q2 earnings call highlights", 2026-07-31. https://www.marketbeat.com/instant-alerts/eaton-q2-earnings-call-highlights-2026-07-31/
- Mitrade, "Eaton Q2-26 earnings call transcript", 2026-08-08. https://www.mitrade.com/insights/news/live-news/article-8-1978297-20260808
- Semiconductor Today, "Infineon SiC for Eaton MVSST 2.0", 2026-09-29. https://www.semiconductor-today.com/news_items/2026/sep/infineon-290926.shtml
- KGI Securities, "Power supply sector report", 2026-07-07. https://www.kgi.com.hk/zh-cn/-/media/files/kgishk/research-reports/tw-reports/power-supply-sector_20260707_en.pdf
- Tom's Hardware, "Nvidia's Kyber rack for Rubin Ultra slips to 2028", 2026-07. https://www.tomshardware.com/pc-components/gpus/nvidias-kyber-rack-for-rubin-ultra-slips-to-2028
- SDxCentral, "Nvidia pushes Kyber release to 2028 following manufacturing concerns: report", 2026-07. https://www.sdxcentral.com/news/nvidia-pushes-kyber-release-to-2028-following-manufacturing-concerns-report/
- Want Rich / China Times, "Vera Rubin 110 kW cabinet; 800 V HVDC not necessary", 2026-06-13. https://wantrich.chinatimes.com/news/20260613900005-420101
- Want Rich / China Times, "Delta limit-down on margin concerns", 2026-07-28. https://wantrich.chinatimes.com/news/20260728900253-420101
- UDN (TrendForce), "Nvidia 800V HVDC Power Rack optional for Vera Rubin", 2026 (month unverified). https://udn.com/news/story/7240/9588387
- TrendForce, "800V HVDC Power Rack ready to ship 3Q26", 2026 (month unverified). https://www.trendforce.com/news/?p=59294
- The Standard (HK), "AI data center power shift to 800VDC to reach 79pc adoption by 2030: Citi", 2026 (month unverified). https://www.thestandard.com.hk/innovation/article/337678/AI-data-center-power-shift-to-800VDC-to-reach-79pc-adoption-by-2030-Citi
- Briefs.co (Bloomberg), "AI's hunger for electricity spurs $220B data center move to 800-volt DC", 2026 (month unverified). https://www.briefs.co/news/ais-hunger-for-electricity-spurs-220b-data-center-move-to-800-volt-dc/
- Yicai, "Sungrow EnerNeo SST launch; Huaan SST market forecast", 2026-07. https://www.yicai.com/news/103269778.html
- Jiemian, "Sungrow SST framework agreements and cost", 2026-07-09/10. https://m.jiemian.com/article/14744444.html
- Economic Daily News (UDN Money), "Lite-On HVDC mid-single-digit 2027 share", 2026 (month unverified). https://money.udn.com/money/story/5739/9625317
- Open Compute Project, "Diablo-400 base specification v0.7.0", 2026-03-01. https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf
- TechCrunch, "Heron Power raises $140M to ramp production of grid-altering tech", 2026-02-18. https://techcrunch.com/2026/02/18/heron-power-raises-140m-to-ramp-production-of-grid-altering-tech/
- 10jqka, "Brokerage summaries: Megmeet, Zhongheng 800V HVDC", 2026-09-22. https://stock.10jqka.com.cn/20260922/c680181794.shtml
- 10jqka, "Kstar investor Q&A on 800V HVDC/SST", 2026-07-24. https://news.10jqka.com.cn/20260724/c678397960.shtml
- Gelonghui (Guolian Minsheng), "Zhongheng Electric research", 2026 (month unverified). https://m.gelonghui.com/news/5317361
- SemiAnalysis, "Inside the 800VDC revolution, Part 1", 2026-05-26. https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part
- Commercial Times (CTEE), "AI rack power content by platform", 2025-07-10 [STALE 2025-07]. https://www.ctee.com.tw/news/20250710700069-439901
- Engineering News (Schneider), "Schneider Electric highlights innovation in 800 VDC power systems", 2025-10-16 [STALE 2025-10, borderline]. https://www.engineeringnews.co.za/print-version/schneider-electric-highlights-innovation-in-800-vdc-power-systems-in-support-of-nvidias-next-generation-gpus-2025-10-16
- JLL, "Global data center sector to nearly double to 200GW", 2026. https://www.jll.com/en-uk/newsroom/global-data-center-sector-to-nearly-double-to-200gw-amid-ai-infrastructure-boom
- Pipeline (Structure Research), "AI data center capacity surge", 2026-07. https://pipelinepub.com/news/structure-research-ai-data-center-capacity-surge-press-release
- Data Center Knowledge, "Solid-state transformers power next-gen AI data centers", 2026. https://www.datacenterknowledge.com/energy-power-supply/solid-state-transformers-power-next-gen-ai-data-centers
- IT Brief UK, "Dell'Oro lifts data centre capex forecast on AI demand", 2026. https://itbrief.co.uk/story/dell-oro-lifts-data-centre-capex-forecast-on-ai-demand
- Express Tribune (Reuters), "Some investors position for slower hyperscaler spending growth", 2026-07-17. https://tribune.com.pk/story/2618784/among-ai-crowd-some-investors-position-for-slower-hyperscaler-spending-growth
- TFTC, "AI capex: hyperscalers cash-flow negative in 2027", 2026. https://www.tftc.io/ai-capex-cash-flow-negative-2027-peak-hyperscalers
- BusinessWire (Bloom Energy), "Bloom Energy's 800V DC-native power can cut billions from AI data center costs", 2026-09-16. https://secure.businesswire.com/news/home/20260916878071/en/Bloom-Energys-800V-DC-Native-Power-Can-Cut-Billions-from-AI-Data-Center-Costs-Reduce-Power-Use-and-Eliminate-Need-for-Transformers
- Finviz, "Bloom Energy scales toward $3 billion as AI tailwinds intensify", 2026. https://finviz.com/news/303225/bloom-energy-scales-toward-3-billion-as-ai-tailwinds-intensify
- Interactive Brokers (IBKR MCP), "Company connections and price snapshots: Delta 2308, Lite-On 2301, VRT, ETN, BE", 2026-10-14. No public URL.


---

### A.6 · Vertical (backside / under-package) power-delivery modules for AI accelerator core rails
*Megatrend: AI data centres (power-limited accelerator compute) | 2026 -> 2030 revenue: $0.15-0.6B -> $1.5-7.0B | CAGR: ~50-120% (central ~78%; steady-state 2027-30 ~36%) | Growth mix: ~97% volume / ~3% price-content (pure $/A falls) | Confidence: low*

**Definition.** In: integrated multiphase modules (power stages, magnetics and usually an embedded capacitor layer in one package) that do the final core-rail conversion from 12 V, 6-8 V or 48 V down to ~0.7-0.8 V. They mount on the board back side directly under, or sandwiched beneath, a GPU/ASIC/CPU package, so 2,000-5,000+ A flows vertically through the board. Examples: MPS, Infineon TDM2454xx (280 A quad-phase) [R, STALE 2025-03], Infineon-Delta [R, STALE 2025-08] and Vicor current multipliers. Revenue is counted once, at module-vendor price, so Infineon dies inside Delta modules are not added again.
Out:
- lateral VR;
- **backside discrete VPD** (DrMOS plus TLVR or chip inductors placed under the package by the ODM), the main substitute;
- separately sold controllers;
- in-package IVR, unless sold as a module;
- IBCs, PSUs and HVDC equipment;
- PCB, substrate and MLCC value;
- IP royalties.

**Value-chain path.** AI data centres -> rack power (AC or ±400 V / 800 V HVDC -> 48/54 V) -> board DC-DC (48 -> 12/6 V, or 48 V direct) -> accelerator core-rail regulation -> integrated multiphase modules -> **vertical (backside, under-package) modules**

**Drill-down decision.** I kept the module level because it is the unit buyers qualify and procure. I rejected three narrower cuts:
- 48 V direct-to-core multipliers: faster-growing, but below the size floor in 2026 and dependent on one or two wins. Kept as a watch item.
- Embedded capacitors and magnetics: revenue is not separable.
- In-package IVR: an adjacent 2028+ niche, and a substitute rather than a sub-niche.

I did not widen the niche to "any vertical delivery". Backside-discrete revenue is DrMOS/TLVR content that belongs to the slower lateral-VR niches. The bear case shows that this boundary is the largest sizing risk.

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $0.15-0.6B [E] | $1.5-7.0B [E] | ~50-120% (2026 at central) |
| Central | ~$0.3B [E] | ~$3.0B [E] | ~78% |

CAGR math:
- Central: 3.0/0.3 = 10.0x; 10^0.25 = 1.778, so 78%.
- Low-low: 1.5/0.15 = 10x (78%). High-high: 7.0/0.6 = 11.7x (85%).
- With 2026 held at $0.3B: 1.5/0.3 = 5x (50%); 7.0/0.3 = 23.3x (120%).
- Cross-corners: 26% and 161%.

**Small-base warning:** 2026 includes only ~1-1.5 quarters of Rubin volume, because VR200 racks ramp in late 3Q26 [3P, TrendForce]. From a 2027 base of ~$0.85-1.7B (central $1.2B) [E], the 2027-30 CAGR to $3.0B is ~21-52%, central ~36% (2.5^(1/3) = 1.357). Use ~36% when ranking against mature niches.

- **Volume vs price:** all figures are own estimates [E].
  - Attached packages rise from ~1.0M to ~11.25M (ln 2.42).
  - Net content per package rises from ~$250 to ~$270 (ln 0.07). That is core amps x1.67 (2,100 -> 3,500 A), times $/A x0.71, times an IVR haircut of 0.90. The $/A path is ~$0.12 -> ~$0.086: -12% a year, partly offset x1.19 by the 48 V-direct mix.
  - So ~97% of log growth is units, and the pure price term is negative.
  - There is no shortage pricing: the tightness is in qualification slots, not wafers.
- **Top-down (packages x attach x amps x $/A):**
  - *2026:*
    - Rubin units: NVIDIA high-end packages 6.0-7.5M [E] x Rubin share 22% [3P, TrendForce Apr 2026] = 1.3-1.65M. After module timing and HBM4 slip: 0.8-1.6M [E].
    - Integrated-module attach on Rubin: 40-100%, central 70% [E]. "Rubin 100% VPD" appears only in Chinese secondary press (unverified), and 九方智投 says NVIDIA still mainly uses discrete parts [3P].
    - Non-NVIDIA packages: 0.05-0.3M.
    - Core current: 1,500-2,800 A (central 2,100), from a 1.8-2.3 kW TDP [3P] with 70-85% going to the core at 0.70-0.85 V [E].
    - $/A: $0.07-0.15 (central $0.12) [E; no ASP source exists], giving $150-400 per package.
    - Central: (1.2M x 70% + 0.15M) ≈ 1.0M x $250 = $0.25B, plus ~$0.04B of Vicor Gen-1 and other legacy vertical = **~$0.3B**.
    - Corners are $0.08-0.82B. The judgement band is $0.15-0.6B, capped by MPS saying vertical revenue "begins" in 2026 [G].
  - *2030:*
    - Packages: 18-32M, central 25M [E].
    - Vertical delivery of any kind: 45-75% (central 60%).
    - Integrated-module share of vertical: 50-100%, central 75%. This is the midpoint between the draft's implicit ~100% and the bear's 50-70%. Attached packages: 25M x 60% x 75% = 11.25M.
    - Blended core current: 2,800-4,500 A, central 3,500. Rubin Ultra/Feynman need 4-5 kA, but 1.5-3 kW ASICs only 1.7-3.6 kA.
    - $/A falls 8-18% a year, offset +10-30% by the 48 V mix, giving content of $170-480 per package (central $300).
    - IVR haircut: 0-30% (central 10%).
    - Central: 11.25M x $300 x 0.90 = **~$3.0B** [E].
    - Corners run from $0.5B (18M x 45% x 50% x $170 x 0.7) to $11.5B (32M x 75% x $480). The judgement band is $1.5-7.0B.
- **Bottom-up (supplier sum, each die counted once; [E] unless tagged):**
  - *2026:*
    - MPS $100-300M: Rubin 0.6-1.6M x 50-70% share x ~$250, plus $20-50M of other vertical. This sits inside a 2H26 Enterprise Data (ED) floor of ≥$971M that also covers lateral, CPU, memory and SSD power.
    - Infineon, including Delta-packaged silicon, $40-150M, out of >€1.6B of FY26 AI power [G].
    - Vicor product, excluding royalties, $10-60M.
    - Murata $0-20M; it needed a firmware re-spin before mass production [R, May 2026].
    - Others $10-40M.
    - Sum $0.16-0.57B, central ~$0.33B. If Rubin is mostly discrete, the sum is ~$0.11-0.40B.
  - *2030:*
    - MPS $0.9-2.6B: ED of $1.7-1.9B grows 20-30% a year to $3.5-5.4B, with vertical at 25-50%.
    - Infineon, including Delta silicon, $0.3-1.1B.
    - Delta/Cyntec value-add $0.1-0.4B.
    - Vicor $0.1-1.0B.
    - Murata $0.05-0.5B. Its ~¥50B target [G] is not shown to be core-rail VPD.
    - ADI, Renesas, TI, Flex, AOS and China-local vendors $0.15-0.8B.
    - Sum $1.6-6.4B, central ~$3.0B.
- **Reconciliation:** The two methods agree but are not independent. Both use the same $/A and attach assumptions, and the 2030 supplier split is share x market. No hard anchor isolates VPD:
  - MPS ED includes lateral power;
  - Infineon's figure covers all AI power;
  - Vicor Advanced Products includes royalties.

  Against the fact-check's ~$4.0B, the gap is the 75% integrated share. The draft's $2.5B low end contradicted its own math (low-low ≈ $1.9-2.1B), and the bear's discrete evidence is unresolved, so the low end widens to $1.5B.

#### Demand drivers and catalysts
- **Physics (structural):** lateral PDN resistance is ~90-140 µΩ vs ~10-15 µΩ for vertical [3P, 36Kr citing TSMC; no primary]. At 2,500 A that is ~720 W vs ~80 W of I²R loss [E]. Eight HBM4 stacks on R200 [3P] crowd out lateral VR.
- **VR200 ramp (2H26, peak 2027):** ramping, but Rubin was cut from 29% to 22% of 2026 NVIDIA high-end shipments [3P]. Whether R200 uses modules or discrete stages is unconfirmed.
- **MPS Q3 2026 (late Oct/early Nov; date unverified):** Q2 ED was $380.6M, +164% y/y [R]. The FY26 floor of ≥+130% [G, secondary only] needs 2H ≥$971M (701.8 x 2.3 - 262.8 - 380.6).
- **Infineon FY26 Q4 (mid-Nov):** FY26 AI power >€1.6B [G, Aug]. The FY27 figure of ~€2.5B [G, May] is to be "materially raised".
- **Rubin Ultra/Kyber, the first 4 kA+ platform:** 2H27 per NVIDIA; 2028 per SemiAnalysis [3P].
- **Vicor Gen-2:** production late Q3/Q4 2027 and 5 A/mm2 in early 2027 [G, secondary; the fact-check could not confirm].
- **USITC 337-TA-1526** (Vicor vs MPS, Infineon and ~18 others): 2027. The schedule is unverified and the source is low quality.
- **ASIC/AMD adoption, 2027-28:** unverified. Google's reported "VPD+TLVR" design [3P] may be the discrete route.
- **800 V HVDC:** Delta expects the main 800 V contribution in 2027 [G]. But KGI sees only 10-20% NVIDIA-platform penetration in 2027, and CTEE reports rumours of a slip past 2028 [3P].
- **M&A:** ADI-Empower, $1.5B, closed 2026-07-07, revenue immaterial [R]. Infineon-C2i and Navitas-Claros reported closed [3P].

#### Supply side
- **Suppliers and shares [E]:**
  - MPS: 45-65% in 2026, 35-50% in 2030. A blog claim of ~70% of Rubin sockets is unverified.
  - Infineon, including Delta-packaged modules: 15-25%.
  - Vicor: 3-15% in 2026, 5-15% in 2030.
  - Delta/Cyntec value-add: 3-10%.
  - Murata: 0-5%, rising to 3-10%.
  - Others: 3-12%.
- **Capacity and lead times:**
  - Silicon is not the binding constraint. Qualification slots, embedded-passive assembly, magnetics and Vicor's single fab are.
  - Vicor: Federal Street going from a $1B to a ≥$1.5B run-rate; a $250-300M second fab is required for its $2.5B target [G].
  - Infineon: capacity reservations worth a cumulative high-single-digit € billions, "concluded or in negotiation", covering all AI power [G].
  - MPS: the "$4B -> $6B" figure is a capacity-investment commitment, not revenue capacity [G, IBKR].
  - Delta: three Thailand plants [G].
  - TrendForce cut 2026 server growth from 20% to 13% on shortages reaching power silicon [3P].
  - Lead times are unverified; I estimate ~20-40 weeks [E].
- **Qualification barriers:** ~12-24 months of co-design per platform [E], with 2-3 suppliers each, so shares swing by generation. Vicor's IP is an overhang.
- **Geographic concentration:** design and IP sit in the US, Germany and Japan. Assembly is mostly in Asia (MPS historically in Chengdu); Vicor is US-made. NVIDIA is >50% of 2026-27 demand [E].

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| Monolithic Power Systems | MPWR / NASDAQ | Volume leader; prime NVIDIA VR supplier | ~2-7% 2026 ($100-300M on ~$4.1-4.3B) [E]; ~15-30% by 2030 |
| Infineon Technologies | IFX / XETRA | #2; TDM2454xx; silicon in Delta modules | <1% [E] |
| Vicor | VICR / NASDAQ | 48 V multiplier pioneer; US fab; IP litigant | ~2-10% 2026 ex-royalties [E]; 30-50% by 2028-30 only if Gen-2 wins |
| Delta Electronics (Cyntec) | 2308 / TWSE | Modules, magnetics; Infineon partner | <0.5% [E] |
| Murata Manufacturing | 6981 / TSE | Entrant; caps/inductors to all | ~0% 2026 [E] |
| Analog Devices (Empower) | ADI / NASDAQ | IVR: substitute and complement | <0.5% [R: immaterial] |
| Renesas Electronics | 6723 / TSE | Controllers, stages, modules | <1% [E] |
| TI / Flex / Alpha & Omega | TXN, FLEX, AOSL / NASDAQ | Challengers (VPD unverified) | <0.2% each [E] |
| Lotus Microsystems | private (Denmark) | vStrata, sampling Q3 2026 [G] | ~100%, pre-revenue |

#### Bear case and key risks
- **Technology substitution:** the vertical architecture can win while the integrated module loses.
  - (1) *Backside discrete, available now:*
    - 九方智投 says NVIDIA "currently still mainly uses discrete devices" and that the timing of a switch to VPD is unconfirmed [3P].
    - 新聿科 says its TLVR inductor is qualified for Vera Rubin at a 50-200% higher unit price [company claim, Apr 2026].
    - A count of ~6,000-7,000 chip inductors per VR200 NVL72 rack [3P] implies ~80-95 phases per GPU at ~25-30 A [E]. That fits discrete stages at least as well as 10-14 quad modules.
    - Infineon's own TDM22545T TLVR module is sold as "VPD-compatible" [STALE 2025-10].
    - 36Kr says PCB-level VPD moves fastest because it needs no package redesign.
    - Bear estimate: discrete/TLVR takes 30-50% of vertically powered packages by 2030, skewed to ASICs [E].
  - (2) *In-package IVR, 2028-29:* TSMC's CoWoS-L IVR offers ~5x the density of discrete designs [3P, STALE 2025-04]. ADI claims 10-15% power savings but gives no date [G]. IVRs take the last stage on 10-30% of flagship packages by 2030, cutting module content there by 30-60% [E].
  - (3) Lateral TLVR persists below ~1.5 kW.
  - Net: 2030 integrated attach is ~25-35%, not 45-70%.
- **Capex cuts:**
  - UBS sees hyperscaler capex growth slowing from ~76% in 2026 to ~25% in 2027, and a rising risk that 2028 falls below 2027 [3P].
  - Reuters/LSEG has capex exceeding FCF by 2027 (+$534B capex vs +$340B cash flow) [3P].
  - ~$25B of Microsoft's ~$190B CY26 capex is component inflation [G, secondary].
  - Scenario: a 2028 capex cut of 20-30% takes packages down 25-40%, with orders cut from 2H27. VPD revenue falls 10-30% in 2028, and 2030 ends at 65-80% of the uncut path [E].
  - Programme risk: a one-year Kyber slip costs ~15-25% of 2030 size, and an ASIC generation rebased to discrete costs ~5-15% [E].
- **Chinese capacity:** low risk in flagship sockets through ~2028 (qualification, security, Vicor IP). The risk is real at component level:
  - Sunlord (002138.SZ) and Platinum (300811.SZ) are claimed to be top-5 in AI chip inductors, with new capacity pressuring prices [3P].
  - Joulwatt, BPS and Silergy show no VPD qualification (unverified).
  - China's ~1-1.5M domestic packages localise at lower ASPs, and cheap parts make the discrete route cheaper.
  - Impact: -5 to -10% on 2030 size, mainly through price [E].
- **Double-ordering / pull-forward:** there is no direct proof, but there are late-cycle signals:
  - shortages [3P];
  - Infineon LTAs [G];
  - MPS 2H26 ED ≥$971M vs $643M in 1H26 and $702M in all of FY25 [R], while VR200 racks are only starting;
  - Wells Fargo cut its MPWR target from $1,860 to $1,700 [3P].

  If 20-35% of 2H26 vertical shipments are pipeline fill [E], 1H27 pauses.
- **Already priced in?** Largely. This is a consensus theme, not a contrarian setup.
  - MPWR: $1,232 (14 Oct), 28% below its high [R, IBKR]. P/E 84.5 at $1,386 vs an industry median of 54.1 [3P, AAII]. ~14-15x sales [E]. Ratings: 11 Buy / 2 Outperform / 2 Hold / 1 Underperform [3P]. Two 2x single-stock ETFs exist [R].
  - VICR: $235, ~4.6x in a year, 39% below its high, ~17x sales [E]. It is pricing Gen-2 wins that have not been announced.
  - Delta: 36% below its high [R].
- **Other:**
  - litigation may push designs to discrete or IVR;
  - NVIDIA buyer power could drive $/A down 15-20% a year;
  - value may migrate to 48 V/HVDC stages;
  - power-limited sites could cap package growth at ~1.3-1.6x;
  - back-side reliability;
  - no supplier discloses VPD revenue.
- **Bear-case numbers:**
  - 2030 size: **$0.8-1.6B, central ~$1.2B** (21M x 30% x 3,500 A x $0.06/A x 0.9 = $1.19B; corners $0.63-2.0B) [E].
  - CAGR: ~28% from the draft's $0.45B base (range 15-37%; severe tail 10-15%), or ~41% from this section's $0.3B base (4.0x).
  - Content per package falls 30-37%: all volume, negative price.
  - **Probability: ~25% (20-30%).** The bear analyst puts ~40% on $1.6-3.5B and ~35% on >$3.5B, a median of ~$2.8B.
  - **First warning:** the MPS Q3 2026 print. Watch for ED flat or down vs $380.6M or below $450M, a Q4 guide implying 2H26 <$971M, rising inventory, or Rubin content described as discrete/TLVR. Cross-check: Taiwanese TLVR/inductor monthly sales accelerating while module vendors stall.

#### Leading indicators to watch (next 2-4 quarters)
1. MPS Q3 2026: ED ≥ ~$450-500M; Q4 guide vs 2H ≥$971M; inventory days; "module" vs "discrete" language.
2. VR200 tray teardown or ODM BOM (4Q26-1Q27): integrated modules vs DrMOS + TLVR under R200, with count and suppliers. This is the most decisive data point.
3. Infineon FY26 Q4 (mid-Nov): size of the FY27 AI raise vs ~€2.5B; any VPD-module disclosure.
4. Taiwan monthly revenue: 新聿科, Chilisin/Yageo and Cyntec vs module vendors.
5. Vicor: named Gen-2 wins; product revenue excluding royalties (Q2 included a new $15M licence); second fab; ITC milestones.
6. Kyber timing (2H27 vs 2028); TrendForce's Rubin share for 4Q26-1Q27.

#### Confidence and biggest unknown
Confidence is **low** on size and medium on direction: there is no VPD revenue disclosure, the 2026 base is ±50% and ASPs are unsourced.

The biggest unknown is whether Rubin and the big ASICs use **integrated modules or backside discrete stages**, and at what $/A. That decides whether 2030 lands near ~$1.2B (bear) or $3-7B. The bear evidence is not decisive: modules contain inductors too, and Rubin's TLVR may serve non-core rails. That is why I set a 75% integrated share and widened the low end, rather than making the bear case central.

The second unknown is IVR timing after 2028. For ranking, pair the ~78% headline with the ~36% 2027-30 rate.

#### Sources
- SEC EDGAR (MPS), "Form 8-K Ex. 99.1, Q2 2026 results", 2026-07-30. https://www.sec.gov/Archives/edgar/data/0001280452/000162828026051029/mpwr-20260630xexx991.htm
- SEC EDGAR (MPS), "Q4 2025 earnings commentary, Ex. 99.2", 2026-02. https://www.sec.gov/Archives/edgar/data/1280452/000143774926003191/ex_886152.htm
- MarketBeat, "Monolithic Power Systems Q2 earnings call highlights", 2026-07-30. https://www.marketbeat.com/instant-alerts/monolithic-power-systems-q2-earnings-call-highlights-2026-07-30/
- TrendForce, "Rubin share of 2026 NVIDIA high-end GPU shipments cut to 22%", 2026-04-08. https://www.trendforce.com/presscenter/news/20260408-13003.html
- The Register (citing TrendForce), "AI now gobbling up power (server growth cut on component shortages)", 2026-04-23. https://www.theregister.com/2026/04/23/ai_now_gobbling_up_power/
- Infineon, "Q3 FY26 analyst-call intro statement", 2026-08-05. https://www.infineon.com/row/public/documents/corporate/investors/presentations/2026/2026-08-05-q3-fy26-intro-statement-analyst-call-v01-00-en.pdf
- Evertiq, "Infineon raises full-year guidance as AI demand drives Q2 growth", 2026-05-07. https://evertiq.com/design/2026-05-07-infineon-raises-full-year-guidance-as-ai-demand-drives-q2-growth
- Industrial Production, "Q3 2026: AI business propels Infineon toward record results", 2026-08. https://www.industrial-production.de/ki---data-analysis/q3-2026--ai-business-propels-infineon-toward-record-results.htm
- Infineon, "We Power AI - VRM" (TDM2454xx), page 2026; launch [STALE 2025-03]. https://www.infineon.com/technology/ai/we-power-ai/vrm
- Infineon, "Infineon and Delta vertical power delivery modules", 2025-08 [STALE 2025-08]. https://www.infineon.com/market-news/2025/INFPSS202508-138
- COMPOTECH Asia, "Infineon TDM22545T dual-phase TLVR module", 2025-10-29 [STALE 2025-10]. https://compotechasia.com/a/new_product/2025/1029/62077.html
- SEC EDGAR (Vicor), "Form 8-K Ex. 99.1, Q2 2026 results", 2026-07-21. https://www.sec.gov/Archives/edgar/data/0000751978/000119312526309538/d115827dex991.htm
- MarketBeat, "Vicor Q2 earnings call highlights", 2026-07-21. https://www.marketbeat.com/instant-alerts/vicor-q2-earnings-call-highlights-2026-07-21/
- SEC EDGAR (Analog Devices), "Form 10-Q, quarter ended Aug 1, 2026", 2026-08. https://www.sec.gov/Archives/edgar/data/0000006281/000000628126000073/adi-20260801.htm
- Yahoo Finance, "Analog Devices Q2 2026 earnings call summary", 2026-05. https://finance.yahoo.com/markets/stocks/articles/analog-devices-inc-q2-2026-164606619.html
- EE Times Japan, "Murata president interview (AI data-centre power module)", 2026-02-27. https://eetimes.itmedia.co.jp/ee/articles/2602/27/news048_2.html
- EE Times Japan, "Murata FY results briefing", 2026-05-01. https://eetimes.itmedia.co.jp/ee/spv/2605/01/news074.html
- 36Kr, "APEC 2026 / TSMC PDN resistance data", 2026-08. https://eu.36kr.com/zh/p/3957053971299463
- 36Kr, "PCB-VPD, SIVR and in-package IVR", 2026. https://www.36kr.com/p/3866419162371330
- TMTPost (钛媒体), "AI 芯片的电力革命", 2026. https://www.tmtpost.com/8001434.html
- Tencent News, "Rubin VPD report", 2026-05-25. https://news.qq.com/rain/a/20260525A09VMA00?media_id=&suid=
- BigGo Finance, "VPD M&A closings and Rubin VPD", 2026. https://finance.biggo.com/news/5086e6f9-71ae-42cf-b54e-b83f623df911
- Tech-Insider, "NVIDIA GTC 2026 Rubin GPU analysis", 2026-04. https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/
- Tom's Hardware, "NVIDIA's Kyber rack for Rubin Ultra slips to 2028", 2026. https://www.tomshardware.com/pc-components/gpus/nvidias-kyber-rack-for-rubin-ultra-slips-to-2028
- AIReport.NET, "Vicor USITC 337-TA-1526", 2026-10-12. https://www.aireport.net/Gn_6f3c6a7b589c
- note.com (iqoys), "MPWR bottleneck-stock post", 2026. https://note.com/iqoys/n/n47ccf0e42121?hl=en
- SinoPac (sinotrade), "Delta Q1 2026 investor conference: ±400 V ships this year, 800 V ramps 2027", 2026-04-30. https://www.sinotrade.com.tw/richclub/hotstock/%E5%8F%B0%E9%81%94%E9%9B%BB%E6%B3%95%E8%AA%AA%E6%9C%83-Q1-EPS-7-91%E5%85%83%E6%94%B9%E5%AF%AB%E5%96%AE%E5%AD%A3%E7%B4%80%E9%8C%84-%C2%B1400V%E4%BB%8A%E5%B9%B4%E5%87%BA%E8%B2%A8-800V%E8%93%84%E5%8B%A22027%E5%B9%B4%E6%94%BE%E9%87%8F-%E8%82%A1%E5%B8%82%E8%A9%B1%E9%A1%8C-69f3237ae912b0007968ba63
- KGI, "Power supply sector", 2026-07-07. https://www.kgi.com.hk/zh-cn/-/media/files/kgishk/research-reports/tw-reports/power-supply-sector_20260707_en.pdf
- Commercial Times (CTEE), "800 V timing", 2026-06-14. https://www.ctee.com.tw/news/20260614700508-430201
- Power Electronics News, "Lotus Microsystems unveils vStrata vertical power delivery platform", 2026. https://www.powerelectronicsnews.com/lotus-microsystems-unveils-vstrata-vertical-power-delivery-platform/
- 九方智投, "三次电源 VPD 电感与模块", 2026 (date unverified). https://www.9fzt.com/common/93df6a6ab638738b09f0c2349b37164b.html
- Sina, "AI供电架构升级，电感量价齐升", 2026 (date unverified). https://www.sina.cn/news/detail/5328272516972563.html
- TechNews (科技新報), "新聿科 TLVR inductor qualified for Vera Rubin", 2026-04-15. https://finance.technews.tw/2026/04/15/tlvr/
- Chinese broker report (Eastmoney repository), "AI chip inductors", 2026-09-21. https://pdf.dfcfw.com/pdf/H3_AP202609211829677396_1.pdf
- eeNews Europe, "TSMC CoWoS-L IVR", 2025-04 [STALE 2025-04]. https://www.eenewseurope.com/en/wp-json/wp/v2/posts/478541
- UBS CIO, "Tech earnings point to a broader AI trade", 2026-07-30. https://www.ubs.com/global/en/wealthmanagement/insights/chief-investment-office/house-view/daily/2026/latest-30072026.html
- Khaleej Times (Reuters analysis), "AI investment boom puts Big Tech's free cash flow under pressure", 2026-07/08 (date unverified). https://www.khaleejtimes.com/business/tech/ai-investment-boom-puts-big-techs-free-cash-flow-under-pressure?amp=1
- Favish (secondary summary), "Magnificent 7 earnings rush reveals AI spending surge", 2026-07/08. https://wa.dev.favish.com/article/magnificent-7-earnings-rush-reveals-ai-spending-surge-hyperscaler-capex-set-reach-725
- AAII, "Why Monolithic Power Systems' (MPWR) stock is up 6.53%", 2026-10-11. https://www.aaii.com/investingideas/article/545378-why-monolithic-power-systems-inc8217s-mpwr-stock-is-up-653
- TIKR, "Monolithic Power has fallen 22% from its high and Wells Fargo just cut its target", 2026-07. https://www.tikr.com/blog/monolithic-power-has-fallen-22-from-its-high-and-wells-fargo-just-cut-its-target-heres-where-the-stock-could-go
- Interactive Brokers, "Company connections and price snapshots (MPWR, VICR, 2308)", 2026-10-14. IBKR company data (no public URL)


---

### A.7 · New-build North American & European sintered NdFeB magnets (non-China, DFARS-traceable)
*Megatrend: Reshoring & critical minerals (rare-earth magnet decoupling from China) | 2026 -> 2030 revenue: $0.09-0.26B -> $0.5-2.4B | CAGR: 33-97% (central ~62%) | Growth mix: ~107% volume / ~-7% price | Confidence: low*

**Definition.**

In: magnet-maker revenue from sintered NdFeB blocks and finished magnets (machined, coated, magnetized), including GBD Dy/Tb grades. The plants must be new-entrant plants of this cycle (commissioned or ramping 2021-30) in the US, Canada, EU/EEA or UK, using documentable non-China feed aimed at 10 USC 4872 / DFARS 252.225-7052. Plants in scope:
- MP Independence and 10X
- e-VAC Sumter
- USAR Stillwater and Blacksburg
- Vulcan Durham and Benson
- Noveon San Marcos. Its whole base is included even though it predates 2024; counting only its expansion would raise the CAGR by a few points.
- Neo Narva 1A/1B
- HyProMag, GKN PM lines, and later POSCO/ReElement magnet phases

Out:
- Incumbents: VAC Hanau; Shin-Etsu, Proterial and TDK; Korean makers.
- Chinese and Chinese-owned plants.
- Lynas/JS Link Malaysia, Vietnam and India.
- Bonded NdFeB, SmCo and ferrite.
- Oxide, metal and alloy (L46/L47). This includes MP's current Magnetics segment revenue, which is mostly precursors.
- Motors and rotors.
- Recycling that does not produce sintered magnets.

About 40-55% of in-scope revenue is embedded NdPr and Dy/Tb [E]. These are the same dollars as L46/L47, so do not add the niches together.

**Value-chain path.** Reshoring & critical minerals -> mining (Mountain Pass, Mt Weld, Serra Verde) -> separation (MP, Lynas, Solvay, Neo Silmet) -> metal/alloy and strip casting (MP, LCM, Korean Metals Plant) -> HD/jet milling, pressing, sintering, GBD, machining, coating -> **this niche** -> motor/actuator makers -> OEMs, defense primes, DLA stockpile.

**Drill-down decision.** I kept the NA+EU new-build level.
- **US-only, offtake-backed core:** about 80% of the 2030 niche, and it grows only slightly faster [E]. Removing the EU barely moves the CAGR, because Narva also starts near zero.
- **GBD Dy/Tb grades (rejected as a faster sub-niche):** they cannot be separated in any disclosure. MP says its GBD process uses ~60% less heavy rare earth than planned [G], so HRE value per kg probably falls.
- **The split that matters runs inside the niche:**
  - Contracted volume: MP 10X (DoD offtake), Apple/GM, eVAC GM/DLA, and Narva's Tier-1 customer.
  - Merchant volume: USAR, Vulcan, eVAC above 2 kt, and Narva Phase 1B.

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $0.09-0.26B (central $0.16B) [E] | $0.5-2.4B (central $1.1B) [E] | ~62% central; 33-97% on central 2026 base |
| Volume | 0.85-1.9 kt (central 1.4) [E] | 6.5-19 kt (central 11) [E] | ~+67%/yr |
| Blended ASP | $105-135/kg (central $115) [E] | $77-125/kg (central $100) [E] | ~-3.4%/yr |

**Revenue math.**

| Case | 2026 | 2030 |
|---|---|---|
| Central | 1.4 kt x $115 = $0.161B | 11 kt x $100 = $1.10B |
| Low | 0.85 x $105 = $0.089B | 6.5 x $77 = $0.50B |
| High | 1.9 x $135 = $0.257B | 19 x $125 = $2.38B |

**CAGR math.**
- Central: (1.10/0.16)^(1/4) - 1 = 61.9%.
- The 2026 base is mostly observed (9.5 months have elapsed), so the header range holds 2026 at its central value: (0.5/0.16)^0.25 - 1 = 33% and (2.4/0.16)^0.25 - 1 = 97%.
- Matched pairings: (0.5/0.09)^0.25 - 1 = 53.5% and (2.4/0.26)^0.25 - 1 = 74%.
- Mixed corners: 18% to 127%.

**Small-base warning.** 2027 is the first full year of MP, USAR and Narva commercial output and of DFARS: ~4.5 kt x $110 = ~$0.50B [E]. From there, (1.1/0.495)^(1/3) - 1 = ~30%. About half of the 2026-30 headline CAGR is first-year ramp.

- **Volume vs price:** ln(11/1.4) = +2.06 and ln(100/115) = -0.14, so growth is ~107% volume and ~-7% price. ASP has two drivers:
  - The ex-China premium compresses as scale arrives, and HRE use is thrifted: -1 to -3%/yr [E].
  - NdPr pass-through moves ASP by about +/-20-30% [E].

  The draft's "1.5-3x policy premium over ~$30/kg Chinese magnets" rested on a Mysteel N35M blank of RMB215/kg [STALE ~2024, fact-check inference]. Current prices are far higher: China PrNd oxide was RMB752.5k/t on 23-Jul-2026 [3P] (~$105/kg at RMB7.15) and PrNd alloy ~RMB917.5k/t [3P]. An N35 magnet therefore carries ~RMB265-275/kg of rare earth alone. Chinese EV-grade GBD magnets are ~$65-95/kg [E], so the Western premium is only ~1.2-1.8x [E]. Durable-growth exposure therefore sits in two places: merchant volume (the premium) and the NdPr cycle.
- **Top-down, 2026:**
  - US direct consumption is 9-12 kt [E]. It is built from China customs data on magnet exports to the US: ~504 t/month in 2026 YTD vs 621 in 2024 [3P compilation].
  - US: 9-12 kt x 5-12% = 0.45-1.4 kt.
  - EU: 18-25 kt [E] x 0.3-1.2% = 0.05-0.3 kt.
  - Total 0.5-1.7 kt x $95-140/kg = $0.05-0.24B (central $0.15B).
- **Top-down, 2030 [E]:**

| Segment | Base: units x content x new-build share | Base kt | Bear kt |
|---|---|---|---|
| NA xEV traction | 4-6.5M x 1.0-1.6 kg x 30-55% | 1.2-5.7 | 0.3-0.85 (2.5-3.5M x 1.0-1.2 kg x 0.8 RE-free haircut x 15-25%) |
| NA auxiliary motors | 15.5M x 0.3-0.5 kg x 5-15% | 0.2-1.2 | 0.1-0.3 |
| Defense, drones, DLA | — | 1.1-3.0 | 0.6-1.2 |
| Industrial/HVAC/data-center/robots | 6-10 kt x 15-30% | 0.9-3.0 | 0.5-1.5 |
| Consumer (Apple) | — | 0.3-1.0 | 0.2-0.5 |
| EU auto + industrial | — | 1.5-4.5 | 1.0-2.0 |
| Exports (Japan/Korea) | — | 0-1.5 | 0-0.3 |
| **Total** | | **5.2-19.9** | **2.7-6.6** |

  **Consumption cross-check:**
  - US 2030 demand is 13-22 kt [E]. Adamas's 20-25 kt, via a secondary source and unverified, is the high end.
  - US: 13-22 kt x 35-60% = 4.6-13 kt.
  - Stockpile and exports: +0.5-1.5 kt.
  - EU: 23-33 kt x 6-12% = 1.4-4 kt.
  - Total 6.5-18.5 kt x $80-130/kg = $0.52-2.4B.

  US-located nameplate (~38-40 kt [G, summed]) is about 2x total 2030 US direct demand.

- **Bottom-up, 2026:**

| Supplier | Basis | kt [E] | Rev @ $105-135/kg [E] |
|---|---|---|---|
| eVAC Sumter | 2 kt/yr block [G]; first shipments 12-Dec-2025 [R]; 130 staff Jul-26 vs 300 planned [R] | 0.4-1.0 | $42-135M |
| Noveon | Output undisclosed; Series C to expand "beyond 2,000 t/yr" [G] | 0.2-0.7 | $21-95M |
| Neo Narva | Commercial production 14-Sep-2026 [G]; millionth magnet Feb-2026 (~20-100 t cumulative [E]) | 0.05-0.3 | $5-40M |
| MP Independence | Commercial deliveries from Q4-26 [G] | 0.02-0.15 | $2-20M |
| USAR Stillwater | Q2-26 revenue $5.8M, all LCM, no magnet sales [R]; first sales by year-end [G] | 0-0.1 | $0-10M |
| Vulcan pilot + others | — | 0.03-0.18 | $3-25M |
| **Total** | Sum 0.7-2.4 kt, narrowed because lows and highs will not coincide | **0.85-1.9** | **$0.09-0.26B** |

  eVAC price check:
  - VAC's ~$65-75M EBITDA at 2 kt [G] equals $32.5-37.5 per kg of block.
  - At a 20-30% EBITDA margin that implies $108-188/kg [E].
  - The Permanent Magnets gross margin was ~10.4% in FY2025 [R, start-up].
  - So the check supports ASP of at least ~$105/kg but does not pin it.

- **Bottom-up, 2030:**

| Supplier | Nameplate kt [G] | Base kt [E] | Bear kt [E] |
|---|---|---|---|
| MP (Independence + 10X from 2028; DoD buys 100% of 10X) | ~10 | 3-7.5 | 2-3 |
| eVAC Sumter (block t) | 2 -> 4 (12 only with offtake) | 1.5-3.5 | 1.2-2 |
| USAR (Stillwater 3.6 + Blacksburg 6.4; full capacity guided by end-2029) | 10 | 1-4.5 | 0.3-1 |
| Vulcan Benson | 10 | 1-4 | 0.3-1 |
| Noveon | 2+ | 1-3 | 0.6-1.2 |
| Neo Narva | 2 -> 5 | 1.2-3.5 | 1-1.5 |
| GKN/HyProMag/POSCO-ReElement | ~5 (unverified) | 0.2-1.5 | 0.2-0.5 |
| **Total** | **~46-55 (mixed units)** | **8.9-27.5 (central ~17)** | **5.6-10** |

- **Reconciliation:**
  - **2026** is supply-limited, and both methods agree at ~$0.15-0.16B. The draft's $0.20B central was ~20% too high, mainly on USAR and eVAC; the higher ASP partly offsets that.
  - **2030** supply potential (~17 kt) exceeds base demand (~12 kt) and far exceeds bear demand (2.7-6.6 kt).
  - The **central** is set at 11 kt x $100 = $1.1B. Probability-weighting the base (50%, $0.8-1.6B), bull (20%, $1.6-2.3B) and bear (30%, $0.3-0.7B) cases gives ~$1.13B [E].
  - The **low end** is widened to $0.5B (6.5 kt x $77). The draft and fact-check (low $0.8B / $0.6B) and the bear case disagree on GM call-offs and merchant financing, and neither has decisive evidence.
  - The **high end** of $2.4B (19 kt x $125) needs China re-escalation, or DFARS-style sourcing spreading to commercial buyers and exports.
  - **Feed does not cap MP.** It is scaling NdPr toward 500 t/month of oxide [G], ~6 kt/yr, enough for ~15-17 kt of magnets [E]. Execution and demand cap it.
  - **Contracted volume** is nominally 6-9 kt (~55-80% of central) [E]. Only MP 10X is hard DoD take-or-pay.

#### Demand drivers and catalysts
- **DFARS 252.225-7052 / 10 USC 4872, effective 1-Jan-2027** [R]. It bars covered magnets with any upstream stage in China, Russia, Iran or North Korea, and drops the COTS exception for items that are 50% or more covered material. Status:
  - Still in law.
  - Primes are lobbying for a second delay (FT via Adamas, May-2026).
  - The rule touches 78% of weapons programs [3P].
  - No waiver had been found as of Oct-2026.
  - Pre-buying is expected in Q4-26 to H1-27.
- **China MOFCOM No.70.** The suspension of the Oct-2025 measures, including the No.61 0.1% de-minimis magnet rule, expires 10-Nov-2026 [R]. The April-2025 licensing on 7 medium/heavy rare earths remains [R], and no extension has been announced. An extension is bearish for the merchant premium; re-escalation is the bull case. A Jun-2026 blacklisting of MP and USAR has been reported by a single secondary source (unverified).
- **Government finance:**
  - MP: $110/kg NdPr floor, 10-year 100% offtake of 10X output, $400M preferred equity [R].
  - Vulcan: $620M OSC loan, $50M CHIPS incentive, $50M equity [G, Nov-2025].
  - USAR: Commerce LOI of ~$1.6B, not yet converted [R].
  - VAC: DLA contract for NdFeB blocks, production from 2026 [R].
- **OEM demand:**
  - Apple $200M and GM $150M prepayments to MP [R].
  - Apple recycled-feed magnets from ~mid-2027 [G, STALE 2025-07].
  - Narva supplies a Tier-1 EV traction customer [G].
  - Noveon's GM/ABB agreements are unverified (not in Noveon's own release).
  - Teledyne says >$1B of its annual revenue depends on supplies such as germanium and rare-earth magnets [R, Q2-26 call].
- **Catalyst timeline:**
  - **Q4-2026:** MP's first commercial deliveries to GM [G, reiterated Aug-2026]. That is about one year later than its 2025 messaging. Q3 call ~29-Oct-2026.
  - **End-Q4-26:** USAR at 600 t/yr run-rate; **Q1-27:** 1,200 t/yr [G].
  - **2027:** Vulcan Benson. "Significant" capacity was guided for 2027 [G, Nov-2025], but no 2026 source confirms construction has started.
  - **Within ~12 months:** close of Energy Fuels-VAC (~$1.9B equity value [R]; amended 13-Oct-2026 [R]).
  - **Early 2027:** Niron's Sartell iron-nitride plant (a substitute) [G].
  - **2028:** MP 10X and USAR Blacksburg commissioning [G].
  - **~2028-29:** Narva Phase 1B [E].

#### Supply side
- **Suppliers and shares [E]:**
  - 2026: eVAC ~40-55%, Noveon ~20-35%, Narva ~5-15%, MP ~2-8%, Vulcan ~2-6%, USAR ~0-5%.
  - 2030 (base): MP 30-40%, eVAC 12-20%, Narva 10-18%, USAR 8-18%, Vulcan 8-18%, Noveon 8-14%.
- **Capacity and lead times:**
  - Announced nameplate is ~46-55 kt [G, summed], in mixed units: eVAC counts block tonnes, and USAR's 5 kt of metal/alloy per site is excluded.
  - Actual 2026 output is only 0.85-1.9 kt [E]. US capacity actually installed is ~5-6 kt [E], against CSPY's nameplate-style count of 10 kt [3P].
  - Build to commercial output takes 2-4 years, and every program has slipped. MP Independence: construction 2022, commercial Q4-2026. USAR Phase 1 cut to a 600 t run-rate at end-2026. Vulcan Benson not started as of Feb-2026.
- **Qualification barriers:**
  - Auto takes ~12-24 months from first magnets to commercial supply [E] (MP-GM: 2025 to Q4-26).
  - Defense needs documented mine-to-magnet traceability. Today only MP, Lynas, Neo/Solvay/Silmet-type and recycled feed can provide it.
- **Bottlenecks:**
  - Ex-China NdPr, which MP calls binding for at least 5 years [G]. Nd oxide traded at ~$147/kg FOB China vs ~$232/kg CIF Rotterdam on 2-Sep-2026 [3P, an aggregator citing SMM; indicative only].
  - Ex-China Dy/Tb. MP's HREE circuit makes >200 t/yr [G]; Silmet's line was commissioned Apr-2026, with purity still stabilizing.
  - Equipment and know-how, given China's Dec-2023 ban on exporting magnet technology.
  - Labor: ~1,000-1,500 jobs per 10 kt plant.
- **Geographic concentration:**
  - The US holds ~75-85% of 2030 new-build capacity (TX, SC, OK, NC) [E]; the EU ~15-25%, mostly Narva. Canada is upstream only.
  - China makes ~90% of global sintered output. Per SMM, June-2026 blank output was 32,985 t at 74% utilization [3P], which implies ~530 kt/yr of capacity, ~135 kt/yr of it idle [E].
  - Shin-Etsu's new refinery plan is Japan-based, and no Japanese incumbent has announced a US/EU magnet plant [R].

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| MP Materials | MP / NYSE | Mine-to-magnet; Independence + 10X; DoD, GM, Apple | Finished magnets ~0-5% of 2026 revenue. Q2-26 Magnetics revenue of $16.5M [R] is mostly precursors. ~50-70% by 2030 [E]. |
| Energy Fuels (acquiring VAC/e-VAC) | UUUU / NYSE American; EFR / TSX | Owner-to-be of Sumter, the largest 2026 producer | 0% before close; ~10-25% after [E] |
| USA Rare Earth | USAR / Nasdaq | Stillwater, Blacksburg; LCM metals; mine assets | ~0-30% of 2026 revenue [E]; ~60-80% by 2030 [E] |
| Neo Performance Materials | NEO / TSX | Narva, the only scaled EU new build; Silmet separation | ~1-5% of 2026 (Q2-26 revenue $205.7M [R]); ~10-20% by 2030 [E] |
| Vulcan Elements | private (US government equity) | Benson 10 kt; defense focus | ~100% |
| Noveon Magnetics | private | San Marcos TX; recycled and virgin feed | ~100% |
| VAC / e-VAC | private (Ara; sale pending) | Sumter operator | Sumter ~15-35% of VAC [E]. VAC H1-26 revenue EUR211M (single secondary source). |
| POSCO International | 047050 / KRX | ReElement US separation JV; magnets in a later phase | ~0% |
| American Axle (GKN PM; ownership not re-verified) | AXL / NYSE | Planned ~4 kt US+EU (unverified) | <1% |
| Lynas | LYC / ASX | Ex-China NdPr and Dy/Tb feed | 0% in scope |

#### Bear case and key risks
- **Technology substitution:**
  - **Rare-earth-free traction motors (EESM).** BMW already ships them. Renault/Valeo plan a 200 kW unit for 2027 [STALE 2022], and ZF claims parity with PM motors [STALE 2024]. The bear expects the rare-earth-free share of NA+EU traction to rise from 10-15% to 20-30% by 2030 [E], removing 0.3-1.5 kt.
  - **Iron nitride (Niron).** Sartell is 1,500 t/yr from early 2027 [G], funded by a $150M SMSC loan (Aug-2026) plus an OSC conditional loan of up to $150M. A 10 kt second plant is targeted for groundbreaking in 2028 [G]. It goes after exactly the merchant fans/HVAC/industrial pool, with the same "domestic, China-free" label, displacing 0.5-2 kt [E].
  - **Thrifting.** Blended ASP falls to $65-85/kg.
  - **Net:** -15-25% of 2030 revenue before any China effect [E].
- **Capex cuts:**
  - **GM is the shared anchor of MP, eVAC and Noveon, and it is retreating from EVs:**
    - $1.6B EV restructuring charge in Oct-2025 [R].
    - Factory Zero cut to one shift; 1,300 workers temporarily laid off from 16-Mar to 13-Apr-2026 [R].
    - Ultium cell pauses and ~3,300 US job cuts after the $7,500 credit expired [R].
  - **Volume mismatch:** GM's 2026 NA EV traction need is ~0.2-0.4 kt, against >2-3 kt/yr of contracted Western supply [E; contracts STALE 2021-12/2022-12].
  - **Scenario effects:**
    - A 20-30% auto capex cut in 2028: -1-3 kt.
    - A 12-18 month 10X slip: 1-2 kt instead of 3-7.5 kt (-$0.2-0.5B).
  - **Supplier equity:** prices are down 57-75% since Oct-2025 [R, IBKR], which makes merchant expansion dilutive. In the bear case Blacksburg slips past 2030, eVAC stays at 2 kt, and Narva 1B and Benson stall. Overall, a 20-30% capex cut removes 40-60% of the draft's central 2030 volume [E].
- **Chinese capacity:**
  - China's ~135 kt/yr of idle capacity is ~2.5-3x the entire NA+EU nameplate [E].
  - Ningbo Yunsheng has 26 kt/yr of blank capacity and filed for an HKEX listing in Jun-2026 [R].
  - Chinese makers are already qualified at essentially every Western buyer.
  - Overbuild warnings: ~40 kt of announced US capacity vs ~17 kt of credible demand (AJOT) [3P]; ~50 kt across seven projects, mostly lower-grade industrial magnets (Skillings) [3P].
  - Out-of-scope compliant rivals (Japan, Korea, Lynas/JS Link) can take DFARS demand.
  - The bear prices merchant volume at $60-75/kg. **Editor's note:** its landed-cost anchor used the stale RMB215/kg blank. At 2026 NdPr prices, Chinese EV-grade magnets land at ~$81-119/kg with the 25% Section 301 tariff [tariff STALE 2024-05; 2026 status unverified]. So the price leg needs NdPr to revert toward 2024-25 levels, or the tariff to be traded away. Both are plausible, so the leg stands, through the commodity channel.
- **Double-ordering / pull-forward:**
  - An e-VAC customer-supply arbitration is cited in an Energy Fuels 8-K summary as the reason for the 13-Oct-2026 amendment. The fact-check could not confirm this in the 424B5, and the counterparty is undisclosed.
  - DFARS pre-buys and DLA block buys are one-time.
  - SMM says China's June-2026 output rise was stockpiling [3P].
  - Prepayments are financing, not call-offs.
  - The bear calculates that a pull-forward-inflated base ($0.25B vs $0.20B) alone removes ~5 points of CAGR. Because 2026 is supply-limited, the larger effect is a 2027 spike that normalizes in 2028.
- **Already priced in?**
  - Share prices (~14-Oct-2026 [R]): MP $39.90 (-58% y/y), USAR $10.28 (-75%), UUUU $8.29 (new 52-week low).
  - 2x single-stock ETFs exist on all three [R].
  - MP: forward P/E ~47, 11 straight quarters of operating losses, consensus 2026 EPS $0.22 [3P].
  - Sell-side targets are still ~2x spot (MS $73, JPM $60, Fintel average $78) [3P], so estimate cuts are still ahead.
  - The tiny-base CAGR is a known mechanical artifact, not an edge.
  - The UUUU fall roughly halves the value of the share consideration in the VAC deal [E].
- **Bear-case numbers:**
  - 2030 revenue $0.3-0.7B (central ~$0.47B, about 6 kt x $78/kg).
  - CAGR on the bear's own $0.20B base: 24% central, band 5-47%. Recomputed on the final $0.16B base: 31% central, 17-45% across $0.3-0.7B. On the bear's $0.25B base: 17%.
  - Severe tail (~10%): $0.2-0.3B, i.e. 6-17% on $0.16B.
  - Probability ~30% (retained); base 50%, bull 20%.
  - Contracted floor ~$0.25-0.4B if 10X commissions near 2028.
  - **First warning sign:** GM call-off behavior, seen through two disclosures: the outcome and counterparty of the e-VAC arbitration, and whether MP's Q3-26 call (~29-Oct) confirms Q4 commercial deliveries to GM, and at what tonnage. Concurrent signal: MOFCOM's decision by 10-Nov-2026.

#### Leading indicators to watch (next 2-4 quarters)
1. MOFCOM's No.70 decision by 10-Nov-2026 (No.72 by 27-Nov), then Nov-Dec China HS 8505.11 exports to the US against ~504 t/month.
2. Any DFARS 252.225-7052 class deviation or waiver before 1-Jan-2027; new DLA or DoD magnet awards.
3. MP Q3/Q4-26: tonnes delivered to GM, 10X vertical construction, Project Swarm offtakes.
4. Energy Fuels/VAC: closing, the arbitration outcome, Sumter tonnes and staffing, the 4 kt go/no-go.
5. USAR: first magnet revenue in Q4-26, 1,200 t/yr in Q1-27, conversion of the Commerce LOI.
6. China PrNd oxide price (RMB752.5k/t on 23-Jul-2026), which passes straight through to Western ASP.
7. Vulcan Benson construction start; Narva Q3 volumes and Phase 1B FID; Niron start-up; GM Factory Zero shift pattern.

#### Confidence and biggest unknown
**Confidence is low.**
- We are fairly confident the CAGR is double-digit: the base is tiny and supply-limited, and the DoD 10X offtake sets a floor.
- We are not confident in the level:
  - No plant discloses tonnes or ASP, and Western magnet price series are paywalled.
  - Every size here is an own estimate.
  - About half the headline CAGR is first-year ramp; 2027-30 is ~30%.

**The biggest unknown** is whether non-defense buyers, above all GM, call off contracted volumes and keep paying an ex-China premium once 10X, Blacksburg and Benson arrive in 2028-30. That decides whether ~46-55 kt of nameplate runs at ~15% or ~40% utilization (6.5 vs 19 kt), which is the whole gap between $0.5B and $2.4B. NdPr price is the second swing, at about +/-20-30% on ASP.

#### Sources
- MP Materials, "MP Materials Reports Second Quarter 2026 Results", 2026-08-06. https://investors.mpmaterials.com/investor-news/news-details/2026/MP-Materials-Reports-Second-Quarter-2026-Results/default.aspx
- MP Materials, Q2-2026 earnings release (8-K exhibit), 2026-08-06. https://www.sec.gov/Archives/edgar/data/0001801368/000180136826000047/mpmcq22026er.htm
- MP Materials, "MP Materials selects Northlake, Texas as the site of 10X", 2026. https://mpmaterials.com/news/mp-materials-selects-northlake-texas-as-the-site-of-10x-a-new-us-rare-earth-magnet-manufacturing-campus/
- MarketBeat, "MP Materials Q4 earnings call highlights", 2026-02-28. https://www.marketbeat.com/instant-alerts/mp-materials-q4-earnings-call-highlights-2026-02-28/?.tsrc=rss
- USA Rare Earth (GlobeNewswire), "Commissioning of Phase 1a magnet production at Stillwater", 2026-03-26. https://www.globenewswire.com/news-release/2026/03/26/3262865/0/en/usa-rare-earth-achieves-major-operational-and-strategic-milestone-with-commissioning-of-phase-1a-magnet-production-at-stillwater-facility.html
- USA Rare Earth, Q2-2026 earnings release (8-K Ex.99.1), 2026-08-10. https://www.sec.gov/Archives/edgar/data/0001970622/000197062226000056/exhibit991-earningsrelease.htm
- USA Rare Earth, Q1-2026 results release, 2026-05. https://seekingalpha.com/pr/20514403
- The Wire China, "The magnet makers: Vulcan Elements", 2026-03-15. https://www.thewirechina.com/2026/03/15/the-magnet-makers-vulcan-elements-rare-earths/
- Mining Weekly, "Vulcan Elements to build $1bn North Carolina plant", 2025-11-19. https://www.miningweekly.com/article/rare-earth-magnet-startup-vulcan-elements-to-build-1bn-north-carolina-plant-2025-11-19
- Energy Fuels, "Definitive Agreement to Acquire VAC for $1.9 Billion Equity Value", 2026-06-23. https://investors.energyfuels.com/2026-06-23-Energy-Fuels-Announces-Definitive-Agreement-to-Acquire-VAC-for-1-9-Billion-Equity-Value
- StockTitan, "Energy Fuels 8-K material event", 2026-10. https://stocktitan.net/sec-filings/UUUU/8-k-energy-fuels-inc-reports-material-event-a236cc88543b.html
- Energy Fuels, Form 424B5 prospectus supplement, 2026-10. https://www.sec.gov/Archives/edgar/data/0001385849/000106299326005309/form424b5.htm
- Energy Fuels, Q2-2026 10-Q, 2026-08. https://www.sec.gov/Archives/edgar/data/0001385849/000138584926000029/efr-20260630.htm
- Crux Investor, "Energy Fuels adds magnet manufacturing through VAC acquisition", 2026-06-23. https://www.cruxinvestor.com/posts/energy-fuels-adds-magnet-manufacturing-through-vac-acquisition
- Pulse 2.0, "Energy Fuels to acquire VAC for $1.9 billion", 2026-06-23. https://pulse2.com/energy-fuels-to-acquire-vac-for-1-9-billion/amp/
- Neo Performance Materials, "Second Quarter 2026 Results", 2026-08. https://www.neomaterials.com/neo-performance-materials-reports-second-quarter-2026-results/
- Neo Performance Materials, "Advances to commercial production at its European magnet facility", 2026-09-14. https://www.neomaterials.com/neo-performance-materials-advances-to-commercial-production-at-its-european-magnet-facility/
- Metal Powder Tech, "Neo Magnequench marks one million sintered magnets from Estonia", 2026-02. https://www.metal-powder.tech/neo-magnequench-marks-one-million-sintered-magnets-from-estonia/
- Noveon Magnetics, "Noveon completes Series C", 2026-01-19. https://noveon.co/noveon-completes-series-c
- Rare Earth Directory, "China export controls timeline", 2026-09/10. https://rareearthdirectory.com/policy/china-export-controls-timeline/
- Mining Technology, "China rare earth export pause nears expiry", 2026-09/10. https://www.mining-technology.com/news/china-rare-earth-export-pause-nears-expiry-amid-persistent-supply-concentration/
- Adamas Intelligence, "U.S. defense contractors seek second DFARS delay", 2026-05. https://www.adamasintel.com/u-s-defense-contractors-seek-second-dfars-delay-as-pentagons-200b-deal-team-six-mobilizes-for-rare-earth-independence/
- Skillings, "US defense supply chains face scrutiny as 2027 rare earths decoupling deadline nears", 2026-10. https://www.skillings.net/critical-minerals-supply-chain-2026-us-defense-supply-chains-face-scrutiny-as-2027-rare-earths-decoupling-deadline-nears/
- 10jqka (生意社), daily rare-earth price report, 2026-07-23. https://news.10jqka.com.cn/20260723/c678380357.shtml
- Mysteel, 2026 rare-earth permanent magnet market page, 2026 (price content stale). https://list1.m.mysteel.com/zhishi/xtyc2026nscxq.html
- NextMSC (citing SMM), "Rare-earth price shocks and magnet cost", 2026-09 (low quality). https://www.nextmsc.com/industry-deep-dive/rare-earth-price-shocks-magnet-cost
- Rare Earth Mining, "Rare earth market pricing analysis March 2026", 2026-03. https://rare-earth-mining.com/rare-earth-market-pricing-analysis-march-2026/
- The Oregon Group, "China's rare earth magnet exports to US fall 21%", 2026-09. https://theoregongroup.com/commodities/rare-earths/chinas-rare-earth-magnet-exports-to-us-fall-21-before-trump-xi-summit/
- Rare Earth Exchanges (Adamas data), "Will America be rare earth magnet independent anytime soon?", 2026. https://rareearthexchanges.com/news/will-america-be-rare-earth-magnet-independent-anytime-soon-no-rare-earth-magnet-demand-vs-supply-u-s-and-china-through-2030-and-beyond/
- CSPY (中证鹏元), rare-earth permanent magnet research report, 2026. https://www.cspengyuan.com/api/files/6960d45d42b27b2bdc799f06
- SMM, "NdFeB output rises in June on stockpiling", 2026-07. https://news.metal.com/newscontent/103980250-produção-de-ndfeb-sobe-em-junho-com-estocagem-julho-deve-cairsmm-analysis
- 10jqka, Ningbo Yunsheng HKEX filing, 2026-06-16. https://stock.10jqka.com.cn/20260616/c677489215.shtml
- Cailian Press, NdFeB exports to US, 2024-05 [STALE 2024-05]. https://www.cls.cn/detail/1679988
- Fastmarkets, "US to impose 25% tariffs on Chinese rare earth magnets", 2024-05 [STALE 2024-05]. https://fastmarkets.com/insights/us-to-impose-25-import-tariffs-on-chinese-rare-earth-magnets
- AJOT, "USA vs China rare earth magnet race risks global oversupply", 2026. https://www.ajot.com/news/usa-vs-china-rare-earth-magnet-race-risks-global-oversupply
- Skillings, "Rare earth magnets: breaking the monopoly in the 2026 race", 2026. https://skillings.net/rare-earth-magnets-breaking-the-monopoly-in-the-2026-race
- Skillings, China blacklisting report (unverified), 2026. https://www.skillings.net/?p=99800
- Argus Media, "Niron secures $150mn loan for RE-free magnet plant", 2026-08. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2867304-niron-secures-150mn-loan-for-re-free-magnet-plant
- Mining.com (Reuters), "Automakers' drive to avoid China's EV rare earth dominance gathers speed", 2024 [STALE 2024]. https://www.mining.com/web/automakers-drive-to-avoid-chinas-ev-rare-earth-dominance-gathers-speed/
- Automotive Powertrain Technology International, "Renault teams up with Valeo and Siemens on rare-earth-free EV motor", 2022 [STALE 2022]. https://www.automotivepowertraintechnologyinternational.com/news/electric-powertrain-technologies/renault-teams-up-with-valeo-and-siemens-on-rare-earth-free-ev-motor.html
- The EV Report, "GM Factory Zero EV production pause", 2026-03-31. https://theevreport.com/gm-factory-zero-ev-production-pause
- Battery-Tech, "GM to cut 3,300 U.S. jobs across three plants", 2025-10 to 2026. https://battery-tech.net/battery-markets-news/gm-to-cut-3300-u-s-jobs-across-three-plants-amid-ev-policy/
- Seoul Economic Daily, "POSCO International launches first US rare earth magnet venture", 2026-05-22. https://en.sedaily.com/business/2026/05/22/posco-international-launches-first-us-rare-earth-magnet
- The Japan Times, "Shin-Etsu Chemical rare earth refinery", 2026-06-11. https://www.japantimes.co.jp/business/2026/06/11/companies/shin-etsu-chemical-rare-earth-refinery/
- Defense News, "Vulcan Elements wins Pentagon deals", 2025-08-25 [STALE 2025-08]. https://www.defensenews.com/industry/2025/08/25/vulcan-elements-wins-pentagon-deals-as-65m-round-fuels-expansion/
- Fintel, MP Materials analyst targets, 2026-07 to 2026-09. https://fintel.io/s/us/MP
- Nasdaq/Zacks, "MP stock: buy now or too pricey", 2026. https://www.nasdaq.com/articles/mp-stock-buy-now-or-too-pricey-its-execution-risks
- Interactive Brokers, company connections and price snapshots for MP, USAR and UUUU, 2026-10-14 (no public URL).
- Teledyne, Q2-2026 earnings call transcript via Alpha Vantage, 2026-07 (no public URL).


---

### A.8 · Low-cost expendable small turbojets (~50-400 lbf) for affordable-mass missiles, jet missile-drones, interceptors and targets
*Megatrend: Defense rearmament and drone warfare ("affordable mass" long-range strike) | 2026 -> 2030 revenue: $0.22-0.55B -> $0.6-2.0B | CAGR: 28-38% (central ~31%) | Growth mix: ~90% volume / ~10% price (all mix; like-for-like price falling) | Confidence: Low*

**Definition.**
- **In:** complete expendable or short-life turbojets of ~50-400 lbf (~0.2-1.8 kN), sold with ECU, fuel pump and starter/generator by Western, allied or Ukrainian makers. Four uses:
  - (a) affordable-mass cruise missiles: USAF FAMM (Anduril Barracuda-500, CoAspire RAACM, Zone 5/Kongsberg AGM-188 Rusty Dagger), ERAM, MALD-class decoys, Ruta B1/B2, Taiwan Barracuda-500M;
  - (b) Ukrainian jet missile-drones (Palianytsia, Peklo, Bars);
  - (c) turbine interceptors (Coyote-class, White Spike);
  - (d) small jet targets (Firejet, Mighty Hornet).
  - Captive engines (Destinus T150, Kratos engines in Firejet) count at imputed value.
  - Typical engines: Kratos Spartan (≤250 lbf), PBS TJ40/TJ80/TJ100/TJ150, Beehive Frenzy 6/8, Destinus T150 (thrust rating unverified), CSG, ZofiTech, JetCat, P&W TJ150.
- **Out:**
  - engines above 400 lbf: Safran TR40/TRI 40/60, Williams F107/FJ33, Teledyne J402, Kawasaki KJ100, Destinus T220, PBS TJ200 (~517 lbf), GEK800/1500 and CCA turbofans;
  - PBS TP100/TS100 and APUs; hobby turbines under 50 lbf;
  - piston, rocket, EDF and ramjet propulsion;
  - Chinese, Russian and Iranian engines;
  - airframes, warheads and guidance.

**Value-chain path.** Defense rearmament and drone warfare -> affordable-mass cruise missiles, jet one-way-attack missile-drones, interceptors and targets -> air-breathing propulsion -> small gas turbines -> **expendable 50-400 lbf turbojets (engine + ECU)**.
- Upstream inputs: superalloy castings or additively made hot sections, hybrid-ceramic bearings, ECUs and fuel pumps.
- Downstream buyers: Anduril, CoAspire, Zone 5 (Kongsberg), Kratos, the Rheinmetall-Destinus JV, MBDA, Ukrainian drone OEMs and NCSIST.

**Drill-down decision.** I kept the ≤400 lbf level.
- **Narrower slice rejected.** US-built engines for FAMM/ERAM-class missiles grow fastest: ~$60-150M in 2026 to ~$0.5-1.0B in 2030, a 50-90% CAGR [E]. But the slice:
  - fails the 2026 size floor and has no credible path to $1B;
  - grows that fast only because the base is small: FAMM production starts in fall 2026 [R, DefenseScoop];
  - is not a distinct product, since the same PBS TJ40/TJ80 engines power Rusty Dagger, White Spike and Palianytsia [R].
- **Wider ≤1,000 lbf level rejected.** The FAMM engine core sits inside the cap: Spartan is "250 lbf and lower" [G], TJ80 is in the ~200 lbf class [G] and Frenzy 8 is 200 lbf [R]. TR40, KJ100, T220 and GEK800 belong to a slower, higher-ASP segment.
- **Boundary risk:** Extended Range FAMM could pull value above 400 lbf (see the bear case).

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $0.22-0.55B (central ~$0.32B) [E] | $0.6-2.0B (central ~$0.95B) [E] | 28-38% (central ~31%) [E] |
| Engines | ~7-15k (central ~10k) [E] | ~12-48k (central ~27k) [E] | ~28%/yr (central) |
| Blended ASP | ~$32k [E] | ~$35k [E] | ~+2.4%/yr (mix only) |

**CAGR math:**
- Central: $0.95B / $0.32B = 2.97x; 2.97^(1/4) = 1.313, so **~31%**.
- Matched pairs: $0.22B -> $0.6B = 2.73x = 28.5%; $0.55B -> $2.0B = 3.64x = 38.1%.
- Cross-pair scenario extremes: $0.55B -> $0.6B = ~2%; $0.22B -> $2.0B = ~74%.

- **Volume vs price:**
  - Engines rise from ~10k to ~27k: 2.7x, or 1.282 per year.
  - Blended ASP rises from ~$32k to ~$35k: 1.10x, or 1.024 per year. Check: 1.282 x 1.024 = 1.313.
  - Log share: ln 2.7 / ln 2.97 = 0.99/1.09, so **~90% volume / ~10% price** [E].
  - The ASP gain is pure mix: US FAMM-class engines at $40-50k gain share from Ukraine-bound engines at $15-30k.
  - Like-for-like price likely falls ~3-6%/yr from 2027-28 as capacity arrives [E]. The bear case has blended ASP falling ~5-6%/yr [E].
  - Shortage pricing exists only in the 2026 Ukraine channel. CSG's 4% starting turbojet EBIT margin [G, via IBKR; not re-verified] shows thin economics, not windfall pricing.
- **Top-down (units x engine ASP, all [E]):**
  - **2026:**
    - Ukraine (supply-constrained): 4,500-9,300 x $15-35k = $70-325M (central 6,500 x $24k = $156M).
    - US (~200-800 FAMM engines plus MALD, Coyote-class, ERAM and targets): 1,000-2,800 x $40-65k = $40-180M (central 1,800 x $50k = $90M).
    - Europe ex-Ukraine plus Asia: 700-2,000 x $30-55k = $21-110M (central 1,200 x $40k = $48M).
    - **Total: $0.13-0.62B; central ~9.5k engines, ~$0.29B.**
  - **2030:**
    - US FAMM: 3,000-7,000 x $38-50k = $114-350M (central 5,000 x $44k = $220M).
    - US other (LCCM, ERAM-class FMS, MALD, interceptors, targets): 1,500-4,500 x $35-60k = $53-270M (central 3,000 x $45k = $135M).
    - Ukraine (ceasefire to continued war): 4,000-22,000 x $15-30k = $60-660M (central 11,000 x $23k = $253M).
    - Europe ex-Ukraine: 2,500-10,000 x $28-45k = $70-450M (central 5,500 x $35k = $193M).
    - Asia and other allies: 1,000-4,000 x $35-50k = $35-200M (central 2,000 x $42k = $84M).
    - **Total: $0.33-1.93B; central ~26.5k engines, ~$0.89B.**
  - **Spend-pool check:**
    - The FY28 FAMM request is 5,300 rounds for $1.85B, or ~$349k per round [budget request]. A $44k engine is ~13% of round cost.
    - 5,000 rounds x $350-450k x 11-15% = $0.19-0.34B, against $0.22B in the build.
    - 2026 Ukraine: 5-9k missile-drones x $100-300k x 12-20% = $0.06-0.54B [E].
- **Bottom-up (demand-allocated supplier units x ASP; only Kratos's ASP is guided):**
  - **2026:**
    - PBS (in-scope types only): 2,400-3,600 x $25-45k = $60-160M (central ~$100M).
    - US incumbents (P&W TJ150, Williams, interceptor and target engines): 600-1,800 x $40-80k = $24-144M (central ~$55M).
    - ZofiTech: 2,000-2,600 x $12-25k = $24-65M (central ~$40M).
    - CSG: 700-1,000 x $25-45k = $18-45M (central ~$28M).
    - Destinus T150: 500-1,300 x $20-40k = $10-52M (central ~$25M).
    - Kratos: 200-800 x $30-50k = $6-40M (central ~$22M).
    - Ukrainian domestic makers: 300-2,000 x $10-30k = $3-60M (central ~$20M).
    - JetCat: 300-1,200 x $15-35k = $5-42M (central ~$15M).
    - Others: $3-40M (central ~$10M).
    - **Sum: $0.15-0.65B; central ~10.3k engines, ~$0.32B.**
  - **2030:**
    - PBS (Czech plus US): 6,000-14,000 x $25-45k = $150-630M (central 9,000 x $33k = $300M).
    - Kratos: 3,000-8,000 x $35-50k = $105-400M (central 5,000 x $45k = $225M).
    - CSG including the Firecrest US JV: 2,000-8,000 x $28-45k = $56-360M (central 4,000 x $35k = $140M).
    - Destinus/Rheinmetall: 1,500-6,000 x $22-38k = $33-230M (central 3,000 x $30k = $90M).
    - Beehive: 300-4,000 x $30-55k = $9-220M (central 1,500 x $40k = $60M).
    - Others: 4,000-15,000 x $15-40k = $60-600M (central 7,000 x $25k = $175M).
    - **Sum: $0.41-2.44B; central ~29.5k engines, ~$0.99B.**
- **Reconciliation:**
  - **2026.** Top-down ($0.29B) and bottom-up ($0.32B) agree within 10%. I adopt a ~$0.32B central and a $0.22-0.55B range. That is narrower than the mechanical $0.13-0.65B because every bucket landing low, or every bucket landing high, at once is unlikely.
  - **Why the draft's 2026 was too high.** The draft's $0.3-0.6B (central $0.40B) was ~20-25% high, and the fact-check wins on evidence:
    - PBS's ~1,700 "aviation engines" in 2025 [R, not re-confirmed] include TP100/TS100/APUs and the out-of-scope TJ200.
    - The draft's $35-50k PBS ASP is unsupported. The multi-year Zone 5 subcontract worth "several tens of $M" for TJ40/TJ80 [R] fits ~$20-40k [E].
    - Destinus was double counted, and its 2026 units were overstated: 1,000 cumulative by June 2026 [G] implies ~500-1,300 in 2026 [E].
  - **2030.** Top-down is $0.89B and bottom-up $0.99B; I adopt ~$0.95B. That is slightly below the fact-check's $1.0B, reflecting bear evidence that points down but is not decisive (FY27 CR, ER-FAMM thrust creep, Chinese price anchor).
  - **Why the draft's 2030 was rejected.** The draft's $1.3B was a simple average of its demand view ($1.13B) and a capacity view ($1.5B). The capacity view adds competing suppliers' capacity for the same programs, so it double counts.
  - **Kratos cross-check.**
    - Kratos's 2028 plan of 5,000 engines x $30-50k = $150-250M [G units; ASP range from earlier calls, STALE 2025].
    - On a smooth 31% path, the 2028 market is ~$0.55B, so Kratos alone would be ~27-45% of it [E].
    - Every FAMM prime multi-sources its engines, which makes that share hard to believe. Either 2028 steps up faster than the smooth path, or Kratos builds inventory.

#### Demand drivers and catalysts
- **US FAMM (largest 2030 driver).**
  - Plan: ~28k rounds over FY27-31 for ~$12.6B. Year profile: FY27 ~1,000, FY28 5,300 ($1.85B), FY31 peak 7,990 [budget request]. "Up to 8,000/yr" is the FY31 peak, not the average.
  - Framework agreements signed 15-Jul-2026 with Anduril, CoAspire and Zone 5 cover testing and qualification, not funded production [R].
  - FY27 money:
    - The request had $55M of discretionary money (for ER-FAMM) plus $300M of reconciliation funding for up to 1,000 rounds.
    - House appropriators raised FAMM to $355M with multiyear authority [R].
    - DoD is now on a CR at ~FY26 levels; whether it carries a FAMM anomaly is unverified [R].
  - *Catalyst:* full-year FY27 appropriation and FAMM Lot 1 awards, late Nov-2026 to Mar-2027. Status: pending.
- **Ukraine missile-drones.**
  - Reuters reports [R]:
    - the mini-jet-engine shortage is "probably the main factor limiting" output;
    - PBS output is ~5x the 2023 level and heading to ~8x by end-2026;
    - ZofiTech makes ~200 engines/month, mostly for Ukraine;
    - CSG aims for ~1,000 engines in 2026. The ~35% Ukraine share is cited by the draft and the bear case, but the fact-check could not re-locate it.
  - "Thousands" per month is ZofiTech's own expectation, not official Ukrainian demand.
  - A Ukrainian minister projects ~10,000/month for one engine type in 2027 [3P]. ~2,000 Bars/month is an unverified claim [3P].
  - *Status:* supply-constrained through 2026. Forecasters' median date for a lasting ceasefire is ~Nov-2027 [3P].
- **ERAM FMS:** up to 3,350 rounds (~$825M) [R, STALE 2025-08]. The first delivery was reportedly a ~10-missile evaluation batch [R, STALE 2025-10], and there are no 2026 delivery counts. I treat ERAM as an option, not as base demand.
- **Europe:**
  - Rheinmetall-Destinus Ruta deliveries before end-2026 [G].
  - CSG-PGZ engine cooperation [G, unverified].
  - MBDA One Way Effector aspiration of 1,000/month [G, STALE 2025-06]. Its engine is undisclosed, so it gets only a small allowance.
- **Interceptors and Indo-Pacific:**
  - Russia reportedly makes ~3,000 jet Geran-4/5 drones a month [3P, unverified]. Faster targets raise demand for turbine interceptors.
  - Kratos-NCSIST Mighty Hornet targets "hundreds to thousands" of systems [G].
- **Supply-side catalysts, 2026-27:**
  - Kratos: 3,000 engines in 2027, 5,000 in 2028 [G].
  - PBS: ~5,000 Roswell engines expected in 2027 [G, AJC via fact-check].
  - CSG: Firecrest US JV at full scale in 2027 [G].
  - Fire Point: in-house turbojet in serial production once tests end, ~end-2026 [R].
  - Beehive: Frenzy 8 qualification under a $29.7M USAF contract [R].

#### Supply side
- **Suppliers and shares:**
  - 2026 central [E]: PBS ~30%, US incumbents ~17%, ZofiTech ~13%, CSG ~9%, Destinus ~8% (captive), Kratos ~7%, Ukrainian domestic ~6%, JetCat ~5%, others ~3%.
  - 2030 central [E]: PBS ~30%, Kratos ~23%, CSG including Firecrest ~14%, Destinus ~9%, Beehive ~6%, others ~18%.
- **Capacity and lead times:**
  - Kratos has ordered components for 3,000 engines (2027) and plans 5,000 for 2028; 2029 "could be 8,000, 10,000" [G]. The Michigan plant is sized for ~40k/yr, and Kratos has cited a 15k-engine customer request [G, STALE 2025].
  - PBS Roswell has space for 5,000/yr annualized (Sep-2026) and targets 10,000/yr by 2028 [G]. A phase 2 of up to 20k/yr is aspirational [G, STALE 2025].
  - Beehive targets up to 8,000/yr [G].
  - Destinus built its 1,000th T150 in June 2026 [G].
  - Announced capacity totals ~45-65k/yr by 2029 [E], against ~27k central 2030 demand, or 1.5-2.5x. **Capacity caps price, not volume.**
  - Kratos orders components 12-18 months ahead [G]. Reuters reports materials as a parallel bottleneck [R]: castings, bearings, ECUs.
- **Qualification barriers:**
  - Integration plus flight qualification takes ~12-36 months [E].
  - Supplier lock-in is weak:
    - Anduril integrated four turbojets on Barracuda-500 [G].
    - The USAF funds PBS ($3M OTA [R]) and Beehive as extra FAMM sources.
    - At least six firms are working on 200-3,000 lbf engines [3P].
  - NDAA/ITAR and US-content rules shield Western makers from China, not from each other.
- **Geographic concentration:**
  - Supply: the Czech Republic (PBS, CSG, ZofiTech) makes ~45-60% of 2026 Western/allied units [E]. The US rises to ~45-55% of 2030 value [E].
  - Demand: Ukraine takes ~55-65% of 2026 units [E].
  - Asia is a buyer, not a supplier:
    - Hanwha targets 4,500-5,500 lbf CCA turbofans [R].
    - Kawasaki's KJ100 is above the cap.
    - NCSIST's engine is licensed to 豐兆航太 but is not in mass production [R].

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| Kratos Defense & Security Solutions | KTOS / Nasdaq | Spartan ≤250 lbf engine maker (~$50k ASP [G]); captive user in Firejet and Mighty Hornet | ~1-3% of 2026 revenue (guidance midpoint ~$1.73B [G]); ~6-9% in 2027 if 3,000 engines ship [E] |
| CSG N.V. | CSG / Euronext Amsterdam (IBKR: CSG1) | Turbojet maker; Firecrest US JV; PGZ cooperation | <1% [E] (H1-2026 group revenue €3.25B [R]) |
| Rheinmetall | RHM / Xetra | Owns 51% of the Ruta JV; buys T150 engines from Destinus | <0.5% [E] |
| Kongsberg Gruppen | KOG / Oslo Børs | Owns 90% of Zone 5 (Rusty Dagger, White Spike); buys PBS engines | 0% (buyer) |
| RTX | RTX / NYSE | P&W TJ150 engine (MALD); integrator for Coyote | <0.1% [E] |
| Safran | SAF / Euronext Paris | Adjacent >400 lbf TR40; doubling Grand Prairie capacity by 2028 [G] | ~0% in scope |
| PBS Group / PBS Aerospace | Private (CZ / US) | Largest merchant engine supplier | ~50-70% of group revenue [E, unverified] |
| Destinus | Private (NL) | Makes T150 engines for its own missiles | Captive |
| Beehive Industries | Private (US) | New entrant with Frenzy 6/8 | ~100% (pre-scale) |
| ZofiTech / JetCat | Private (CZ / DE) | Engine makers supplying Ukraine | ~100% / majority [E] |
| Anduril / CoAspire | Private (US) | FAMM integrators and engine buyers | 0% (buyers) |

#### Bear case and key risks
- **Technology substitution:**
  - **Thrust creep.** The USAF requested $55M in FY27 for an Extended Range FAMM of more than 1,000 nmi [R]. Longer range pulls toward GEK800, T220, TR40 or small turbofans, moving ~10-25% of US affordable-mass engine value above 400 lbf by 2030 [E]. Ruta B3 on the T220 is the European analogue.
  - **Non-turbine propulsion keeps the volume.**
    - Piston one-way-attack drones (FP-1/Liutyi class) stay the volume workhorse.
    - Electric or rocket interceptors at ~$2-6k take most counter-drone kills [E, unverified], keeping turbine interceptors under 10% of units [E].
    - Counter-argument: faster jet Geran-4/5 targets need faster interceptors.
  - **Cheaper turbojets inside the niche.** Sources of cheaper engines:
    - MBDA's automotive line with Renault;
    - Beehive's additively manufactured engines;
    - ~21 Ukrainian developers including Fire Point [R], plus Ukrainian Armor-AviaNera [R].
    - Effect: by 2030, 30-50% of Ukrainian and European units could be $10-20k engines, cutting blended ASP ~15-25% [E].
  - **Net effect:** -$0.15-0.35B of 2030 value against the draft central [E].
- **Capex cuts:**
  - FY27 FAMM production is ≤~1,000 rounds, funded partly by one-off reconciliation money, under a CR [R].
  - FY28-31 would then have to average ~6,500-7,000/yr, a 6-7x step-up [E].
  - Budget-document quantities historically shrink. FAMM also competes with Golden Dome, interceptor replenishment after the Iran conflict, shipbuilding and CCA.
  - Sensitivities against the draft's $1.13B demand view [E]:
    - FAMM cut 30% in 2028: -$0.05-0.10B.
    - FAMM held at ~1,000/yr: -~$0.2B.
    - Ukraine ceasefire: -$0.23-0.25B.
    - Europe cut 25%: -~$0.06B.
    - Combined: 2030 ~$0.55-0.70B.
  - A 20-30% demand cut against ~45-65k/yr of capacity leaves ~25-40% utilization. Expect a price war, write-downs and exits among private Czech and US entrants [E].
- **Chinese capacity:**
  - Evidence of cheap Chinese engines:
    - A Chinese Telefly JT80, described as a copy of the PBS TJ80-90, was listed at ~$18k [R, STALE 2025].
    - A Geran-4 teardown found a ~$20-25k Chinese engine [3P].
    - A Shenzhen trader offers a 100 kgf TWP100E, said to be developed by the Chinese Academy of Sciences [3P, unverified].
  - HUR's ~3,000 Geran-4/5 a month [3P, unverified] implies a Chinese 80-200 lbf supply chain of ~20-40k engines/yr at ~40-60% of Western ASP [E]. That is comparable to the entire Western 2030 market.
  - Chinese engines are barred from US, EU and Ukrainian programs. The risk is price anchoring and lost exports to non-NDAA buyers; most of the Asia and other-allies bucket is contestable.
  - Probabilities [E]: below 10% that Chinese engines take more than 10% of the niche directly by 2030; ~50% that they hold Western blended ASP growth at or below 0%/yr.
- **Double-ordering / pull-forward:**
  - Kratos has ordered components for ≥3,000 engines for 2027 [G]. FY27 funds ≤~1,000 FAMM rounds, spread across three primes that all multi-source engines.
  - Kratos has built at-risk "whitetail" Valkyrie inventory before [R].
  - Ukraine's stated demand (10,000/month for one engine type in 2027 [3P]) is 10-20x actual shipments, with supply in the "low hundreds per month" [R]. That gap is the classic setting for duplicate orders.
  - FAMM is explicitly framed as a stockpile fill [3P]. Replenishment after the fill runs far lower.
  - Tell to watch: shortening lead times and engine makers quoting stock availability in 2027.
- **Already priced in?** No. The market is skeptical.
  - KTOS closed at $38.95 on 14-Oct-2026, against a $134 52-week high (-71%). Its post-Q2-call rally from ~$46.6 to $67.1 has fully reversed [R].
  - CSG1 trades at €14.16, against a €35.5 high (-60%) [R].
  - There is no listed pure play: turbojets are ~1-3% of Kratos revenue and under 1% of CSG's [E]. The hype sits in trade press and private valuations, so a bear outcome hurts private entrants and capacity investors most.
- **Bear-case numbers:**
  - **2030 size: $0.35-0.65B** (central ~$0.48B, on ~15-16k engines at ~$30k) [E]:
    - US: 3,500-6,500 x $36-44k = $0.13-0.29B.
    - Ukraine: 4,000-8,000 x $15-25k = $0.06-0.20B.
    - Europe: 2,000-5,000 x $28-35k = $0.06-0.18B.
    - Asia and other allies: 1,000-2,500 x $30-40k = $0.03-0.10B.
    - Drivers: units grow ~10%/yr while ASP falls ~5-6%/yr.
  - **CAGR:**
    - As written: ~-6% to +17%, central ~+5% on the draft's $0.40B base (1.2^(1/4) = 1.047).
    - Rebased to the corrected $0.32B: central ~+11% (1.5^(1/4) = 1.107).
  - **Probability: ~25% (range 20-30%).**
    - A moderate bear ($0.65-0.9B) is another ~25% [E].
    - About a quarter of the probability therefore lies at or below the base range's $0.6B floor.
  - **First warning sign** (window late Nov-2026 to Mar-2027), any of:
    - FY27 ends on a full-year CR with no FAMM anomaly;
    - the $300M reconciliation tranche fails;
    - Lot 1 awards total fewer than ~1,000 rounds, or multiyear authority slips to FY28.
  - An earlier soft signal comes from the Kratos Q3 call in early Nov-2026.

#### Leading indicators to watch (next 2-4 quarters)
1. **Kratos Q3-2026 call (early Nov-2026):** the share of the 3,000-engine 2027 build backed by named, funded orders (bearish if under ~50%); Turbine Technologies inventory; any softening of the 5,000-engine 2028 plan.
2. **FY27 appropriations:** FAMM quantity and dollars, multiyear authority, and Lot 1 award sizes for Anduril, CoAspire and Zone 5/Kongsberg.
3. **Ukraine-channel engine pricing and lead times (PBS, CSG, ZofiTech):** shorter lead times or lower prices would show a glut before demand data do.
4. **CSG reports:** turbojet units against the ~1,000 target, margin against 4%, and Firecrest US JV timing.
5. **PBS Roswell:** output against ~5,000 in 2027, and any PBS revenue or ASP disclosure.
6. **Thrust, entrants and the war:** the thrust class chosen for the ER-FAMM engine, Beehive Frenzy 8 qualification, Fire Point turbojet serial production, and Ukraine ceasefire talks.

#### Confidence and biggest unknown
Confidence is **low**.
- **Direction is well supported:** signed framework agreements, Kratos and PBS capacity guidance, and the Ukraine engine shortage documented by Reuters.
- **Magnitude is not:**
  - only Kratos discloses an ASP;
  - PBS's 2025 unit count and CSG's turbojet guidance could not be re-verified;
  - ~25% of the probability sits below the base range.

**Biggest unknown:** how many FAMM-class rounds are actually appropriated and delivered in 2028-30. The plan is ~28k over FY27-31, but FY27 is only ~1,000 under a CR. This interacts with how long Ukraine's war-driven demand lasts; together they swing 2030 by ~$1B or more. A secondary unknown is like-for-like engine price once 1.5-2.5x capacity arrives.

#### Sources
- Defence Industry Europe, "Kratos prepares to produce 3,000 Spartan turbojet engines in 2027 and 5,000 in 2028 for low-cost cruise missile programs", 2026-08. https://defence-industry.eu/kratos-prepares-to-produce-3000-spartan-turbojet-engines-in-2027-and-5000-in-2028-for-low-cost-cruise-missile-programs/
- Breaking Defense, "One big FAMMily: Air Force eyes huge boost for low-cost cruise missile", 2026-04. https://breakingdefense.com/2026/04/one-big-fammily-air-force-eyes-huge-boost-for-low-cost-cruise-missile/
- DefenseScoop, "Wilsbach: FAMM low-cost cruise missile to begin production this fall", 2026-06-10. https://defensescoop.com/2026/06/10/wilsbach-famm-low-cost-cruise-missile-to-begin-production-this-fall/
- Air & Space Forces Magazine, "Pentagon announces multiyear deals to buy thousands of affordable cruise missiles", 2026-07-15. https://www.airandspaceforces.com/pentagon-announces-multiyear-deals-to-buy-thousands-of-affordable-cruise-missiles/
- The Defense Post, "CoAspire US FAMM program", 2026-07-17. https://thedefensepost.com/2026/07/17/coaspire-us-famm-program/
- The Defense Post, "US Anduril Barracuda-500", 2026-07-16. https://thedefensepost.com/2026/07/16/us-anduril-barracuda-500/
- Defense Daily, "$300 million for FAMM pulled forward by House appropriators", 2026-06. https://www.defensedaily.com/300-million-for-famm-pulled-forward-by-house-appropriators/budget/
- SpacePolicyOnline, "House Clears FY2027 CR, Now to the President", 2026-09. https://spacepolicyonline.com/news/house-clears-fy2027-cr-now-to-the-president/
- Breaking Defense, "House appropriators release $1 trillion defense bill for FY27", 2026-06. https://breakingdefense.com/2026/06/house-appropriators-release-1-trillion-defense-bill-for-fy27/
- Reuters (via KFGO), "Ukraine's attack drone fleet faces a mini jet engine supply crunch", 2026-04-07. https://kfgo.com/2026/04/07/ukraines-attack-drone-fleet-faces-a-mini-jet-engine-supply-crunch/
- Euromaidan Press, ZofiTech / Ukraine engine suppliers, 2026-04. https://euromaidanpress.com/?p=400430
- Euromaidan Press, HUR on Geran-4/5 production, 2026. https://euromaidanpress.com/?p=420149
- MM Spektrum, "Motory, které obletěly svět", 2026 (undated). https://www.mmspektrum.com/clanek/motory-ktere-obletely-svet
- ČTK / České noviny, PBS jet-engine output, 2026. https://www.ceskenoviny.cz/zpravy/2656690
- Defence Industry Europe, "PBS Aerospace says Georgia plant expansion ... supports 10,000-engine annual output target by 2028", 2026-09. https://defence-industry.eu/pbs-aerospace-says-georgia-plant-expansion-doubles-test-capacity-supports-10000-engine-annual-output-target-by-2028-amid-rising-u-s-defence-demand/
- PBS Aerospace, "PBS Aerospace awarded U.S. Air Force prime contract to support FAMM", 2026-03-18. https://www.pbsaerospace.com/news/pbs-aerospace-awarded-u-s-air-force-prime-contract-to-support-family-of-affordable-mass-munitions-famm
- Defense Express, "Czech PBS Group to supply jet engines for US White Spike interceptor", 2026. https://en.defence-ua.com/industries/czech_pbs_group_to_supply_jet_engines_for_us_white_spike_interceptor_same_company_already_powers_rusty_dagger_cruise_missiles_tied_to_ukraine-19215.html
- Kongsberg, "Kongsberg completes acquisition of Zone 5", 2026-06-10. https://www.kongsberg.com/news/news-archive/2026/kongsberg-completes-acquisition-of-zone-5/
- Destinus (ANP), "Engine No. 1000: Destinus reaches industrial-scale turbojet production in Europe", 2026-06-18. https://persportaal.anp.nl/artikel/CSN-180626048/engine-no-1000-destinus-reaches-industrial-scale-turbojet-production-in-europe
- Taiwan News (CSG release), "CSG H1-2026 results", 2026. https://www.taiwannews.com.tw/en/news/6417144
- Business Wire, "Beehive Industries awarded $29.7 million contract by U.S. Air Force for Frenzy engine family development", 2026-04-09. https://secure.businesswire.com/news/home/20260409529770/en/Beehive-Industries-Awarded-%2429.7-Million-Contract-by-U.S.-Air-Force-for-Frenzy-Engine-Family-Development
- Air & Space Forces Magazine, "Air Force contract: Beehive small disposable jet engines", 2026-04. https://www.airandspaceforces.com/air-force-contract-beehive-small-disposable-jet-engines/
- NetEase (citing Aviation Week), Beehive up to 8,000 engines/yr, 2026-06/07. https://www.163.com/dy/article/L0Q4BBLV05119LR8.html
- Safran, "Safran accelerates US growth: strategic expansion of turbojet engine production for missiles and drones", 2026-09-30. https://www.safran-group.com/pressroom/safran-accelerates-us-growth-strategic-expansion-turbojet-engine-production-missiles-and-drones-2026-09-30
- CEO Score Daily, Hanwha unmanned-aircraft engines, 2026-05-26. https://ceoscoredaily.com/page/view/2026052616574980133
- ETtoday / Commercial Times, NCSIST small turbojet, 2026-05-14. https://www.ettoday.net/news/20260514/3166101.htm
- DroneXL, "Europe 500 km kamikaze drone" (MBDA OWE), 2026-02 [STALE 2025-06]. https://dronexl.co/2026/02/20/europe-500-km-kamikaze-drone
- The War Zone, "Ukraine will receive first of thousands of new U.S.-made standoff missiles", 2025-08 to 2025-10 [STALE 2025-10]. https://twz.com/air/ukraine-will-receive-first-of-thousands-of-new-u-s-made-standoff-missiles-in-the-coming-weeks
- UNN, "How many Bars cruise missiles Ukraine produces", 2026. https://unn.ua/en/amp/it-has-become-known-how-many-bars-cruise-missiles-ukraine-produces-the-figure-is-impressive
- UNN, "From dependence to domestic production: why Ukraine needs its own jet engines", 2026. https://unn.ua/en/news/from-dependence-to-domestic-production-why-ukraine-needs-its-own-jet-engines-for-missiles-and-drones
- United24 Media, "Ukraine eyes 10,000 jet engines a month", 2026. https://united24media.com/war-in-ukraine/ukraine-eyes-10000-jet-engines-a-month-as-it-races-to-outpace-russias-drone-threat-23333
- Nordot, Ukrainian Armor-AviaNera engine partnership, 2026. https://nordot.app/1439638711548986039
- heise online, Telefly JT80 in Geran-3, 2025 [STALE 2025]. https://heise.de/-10669801
- Migflug (RFE/RL teardown), Geran-4 engine, 2026. https://migflug.com/afterburner/?p=25446174
- Novyny.live, Geran-3 engine price, 2025 [STALE 2025]. https://novyny.live/ru/industriyi/v-chomu-geran-3-obiishla-geran-2-tsina-ta-osoblivosti-281530.html/amp
- B2Brazil (Shenzhen trader), TWP100E 100 kg thrust turbojet, undated. https://cn-bp.b2brazil.com/hotsite/shenzhennuobashi/100kg-thrust-turbojet-engine-twp100e-low
- Ukranews, "Not this year: international analysts assess chances of ending war in Ukraine", 2026. https://ukranews.com/en/amp/news/1165616-not-this-year-international-analysts-assess-chances-of-ending-war-in-ukraine
- Jamaica Gleaner (wire), "Russia, Ukraine trade blame as ceasefire nears end", 2026-05-12. https://jamaica-gleaner.com/article/world-news/20260512/russia-ukraine-trade-blame-continued-fighting-ceasefire-nears-end
- Interactive Brokers, company connections and price data for KTOS and CSG1, 2026-10-14 (IBKR data; no public URL).

