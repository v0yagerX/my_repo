# The fastest-growing niche industries, 2027–2030

*A supply-chain view: 16 megatrends → 122 raw candidates → 50-niche longlist → 18 deep dives → top 10.*
*Data as of 15 October 2026. Growth metric: revenue CAGR 2026→2030 (four compounding years). Not investment advice.*

**How to read this report**

- **Claim labels.** **[R]** reported fact · **[G]** company guidance · **[3P]** third-party estimate · **[E]** own estimate. **[STALE yyyy-mm]** marks a figure published before ~October 2025. "Unverified" means the figure could not be checked against a source in this research.
- **CAGR terms.** CAGR = (S2030 / S2026)^(1/4) − 1.
  - "Central" is the deep dive's central case.
  - "Prob-wtd" is the panel-median probability-weighted CAGR, including each niche's bear case.
  - "2027→30" is annual growth over 2027–2030. It strips out the 2026 base effect, which flatters niches that only start ramping in late 2026.
- **Growth mix.** Volume / price splits are shares of log revenue growth. A volume share above 100% means prices fall.
- **Evidence caveat.** This environment could not fetch web pages directly: SEC EDGAR, company IR sites and research-firm sites were blocked. Web search was also capped at 200 calls per research round. The evidence therefore comes from three channels:
  - search-result summaries of primary and Asian-press sources;
  - full earnings-call transcripts (Alpha Vantage);
  - company data (Interactive Brokers).

  Almost no supplier discloses revenue at niche level, so most sizes are triangulated **[E]** estimates with wide ranges. Phase-1 longlist evidence was partly recalled from memory and is flagged as such in Appendix B. The 18 deep dives re-verified their load-bearing numbers through an independent fact-check. Details are in [Appendix C](#appendix-c--methodology-and-limitations).

**Contents.**
1. [Executive summary](#1-executive-summary)
2. [Value-chain trees](#2-value-chain-trees)
3. [Longlist scoring](#3-longlist-scoring)
4. [Deep dives: top 10](#4-deep-dives-top-10)
5. [Too-early watchlist](#5-too-early-watchlist-niches-whose-volume-ramps-start-after-2028)
6. [Overhyped list](#6-overhyped-popular-niches-whose-2027-2030-revenue-will-disappoint)
7. [Sources](#7-sources)

Appendices:
- [A: other deep dives](appendix-a-other-deep-dives.md)
- [B: longlist evidence and audit trail](appendix-b-longlist-evidence.md)
- [C: methodology and limitations](#appendix-c--methodology-and-limitations)
- Data: [`data/`](data/)

---

## 1. Executive summary

**The ten fastest-growing narrow niches for 2026→2030, ranked by risk-adjusted revenue growth.** The ranking rule is in Section 3.3. In short: each niche needs a 2026 base of at least ~$0.1B and passes an evidence/quality gate; eligible niches are then sorted by probability-weighted CAGR.

| # | Niche (where it sits in the value chain) | Revenue 2026 → 2030, central (range) | CAGR 2026→30, central (range) | Prob-wtd | 2027→30 | Growth mix: volume / price | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | **Merchant HBM4/4E logic base dies**: AI accelerators → HBM stacks → foundry-made base (logic) die | $0.6B → $7.5B ($0.3–1.1B → $4–14B) | ~88% (61–120%) | 78% | ~33% | ~83% / ~17% | Medium |
| 2 | **Ultra-high-power CW InP lasers + external-laser-source modules for CPO/NPO**: AI networking → co-packaged optics → light source | $0.19B → $2.3B ($0.11–0.30B → $1.0–4.5B) | ~86% (35–153%) | 73% | ~28% | ~110% / ~−10% | Low |
| 3 | **Merchant scale-up switch silicon for non-NVLink accelerator racks** (PCIe AI fabric, then UALink/ESUN) | $0.9B → $8B ($0.6–1.4B → $3.5–14B) | ~73% (55–78%) | 61% | ~45% | ~60% units / ~40% content per XPU | Low |
| 4 | **Merchant optical circuit switches (OCS)** for AI cluster fabrics | $0.47B → $3.3B ($0.35–0.65B → $1.8–6.0B) | ~63% (51–74%) | 57% | ~40% | ~115% / ~−15% | Low |
| 5 | **HAMR nearline hard drives (≥30 TB)**: AI/cloud storage → nearline HDD → recording-technology transition | $4.9B → $33B ($4.3–5.6B → $20–52B) | ~61% (42–80%) | 55% | ~42% | ~110% / ~−10% ($/TB) | Medium |
| 6 | **SF6-free high-voltage (>52 kV) switchgear and circuit breakers** | $0.7B → $3.4B ($0.5–1.2B → $2.5–5.0B) | ~48% (37–63%) | 43% | ~35% | ~95–100% / ~0–5% | Medium |
| 7 | **US 765 kV-class autotransformers and shunt reactors** | $0.25B → $1.25B ($0.15–0.40B → $0.75–1.8B) | ~50% (31–67%) | 41% | ~32% | ~80% / ~20% | Low |
| 8 | **Merchant 300 mm silicon-photonics PIC foundry wafers** | $0.7B → $3.3B ($0.5–1.0B → $1.8–5.0B) | ~47% (38–50%) | 41% | ~38% | ~100% / ~0% | Low |
| 9 | **HVLP4/5 copper foil for M8–M10 ultra-low-loss laminates** (AI server and switch boards) | $0.33B → $1.3B ($0.22–0.47B → $0.7–2.1B) | ~41% (21–59%) | 35% | ~33% | ~113% / ~−13% | Medium |
| 10 | **Transcatheter tricuspid valve replacement (TTVR) systems** | $0.25B → $0.70B ($0.17–0.33B → $0.45–1.1B) | ~29% (16–45%) | 27% | ~27% | ~110% / ~−10% | Low |

**One line each:**

1. **HBM base dies.** From HBM4 onward, the stack's base die moves from a DRAM process to a foundry logic node (TSMC N12 to N3), and SK hynix and Micron buy it from TSMC. About 70% of unit growth is that one-time sourcing shift, so growth is front-loaded and exposed to a 2028 memory-cycle reversal.
2. **CPO lasers.** Every co-packaged or near-packaged optical engine needs external ~300–400 mW CW lasers from a handful of InP fabs. Purchase orders and NVIDIA capacity deals give good near-term visibility. But the 2030 size hinges on when optical scale-up arrives (bear case: $0.5–1.1B, ~30% probability).
3. **Scale-up switch silicon.** Non-NVIDIA accelerator racks need merchant scale-up switches (Astera Scorpio X, Broadcom Tomahawk Ultra, then UALink/ESUN parts). This has the highest growth inside the 2027–30 window. NVLink Fusion is the swing substitution risk. On the Q4-2026 exit run-rate the CAGR is ~50–58%.
4. **OCS.** Growth comes from TPU superpods and Google moving optical circuit switching from in-house to vendors (Lumentum, Coherent). The bear case (~25%): Google keeps a captive majority and NVIDIA skips OCS.
5. **HAMR.** HAMR is the only way to add exabytes without building new drive factories. Seagate is ~100% of volume today and Western Digital ramps from 1H 2027. It is the largest dollar gain on the list (+~$28B), but today's $/TB includes shortage pricing.
6. **SF6-free HV switchgear.** EU F-gas Regulation 2024/573 bans new SF6 gear at 52–145 kV from 1 January 2028, a legally forced technology switch. This is the best-evidenced non-AI pick. The 2026 base cannot be observed, and PFAS rules put fluoronitrile mixtures at risk.
7. **765 kV transformers and reactors.** ERCOT, PJM, SPP and later MISO are building 765 kV backbones. Korean OEM orders (Hyosung, HD Hyundai) are the primary evidence, and very few plants can build and test at 765 kV. Calendar 2030 may fall between delivery waves.
8. **300 mm silicon-photonics wafers.** Growth comes from PIC migration to 300 mm (TSMC COUPE, GlobalFoundries, Tower) plus CPO and optical I/O. TSMC, Tower, GlobalFoundries, Samsung and Chinese fabs are all adding capacity at once, which points to wafer-price pressure in 2028–29.
9. **HVLP4/5 copper foil.** This is supply-capped foil for AI boards (Mitsui Kinzoku, Co-Tech, Furukawa, Lotte Energy Materials, Circuit Foil; Chinese challengers such as Jiujiang Defu are qualifying). Growth is front-loaded to 2026–28. Processing fees reset when converted Chinese capacity qualifies in 2028–30.
10. **TTVR.** Edwards' EVOQUE holds ~95% share after the 2025 Medicare coverage decision. Growth is procedure-volume-led. EVOQUE revenue is not disclosed, and Edwards' own PASCAL repair device competes for the same patients.

**What the research says overall**

- **AI dominates the list, and that is a correlation risk.** Seven of the ten, including all of the top five, sit in AI data-center supply chains and share one demand driver: hyperscaler and AI-cloud capex. A 2028 capex digestion would hit #1–#5, #8 and #9 together. The three non-AI picks rest on different drivers: EU law (SF6), regulator-approved transmission plans (765 kV) and Medicare coverage (TTVR). They grow more slowly but are not correlated with AI.
- **Headline CAGRs are front-loaded.** The 2026→2030 metric flatters niches whose ramp starts in late 2026. CPO lasers and HBM base dies show ~86–88% headline CAGRs but only ~28–33% a year over 2027–30. Ranked on in-window growth (2027→30), the order is:
  1. scale-up switch silicon, ~45%
  2. HAMR, ~42%
  3. OCS, ~40%
  4. silicon-photonics wafers, ~38%
  5. SF6-free switchgear, ~35%
- **Growth is volume-led.** In all ten, unit volume, share shift or content per unit explains at least ~80% of log revenue growth, and in seven of them like-for-like prices fall.
  - Shortage pricing does exist today: HAMR $/TB, HVLP processing fees, InP laser ASPs and T-glass. But none of the ten ranks on it.
  - Where growth was mostly price, the niche dropped out. T-glass cloth fell to ~17% probability-weighted; ultra-high-capacitance MLCCs to ~20%.
- **The common thread is a technology transition that switches on inside the window.** Each pick rides one:

  | Pick | Transition |
  |---|---|
  | HBM base dies | DRAM-process → logic-process base dies |
  | CPO lasers, silicon-photonics wafers | electrical → optical I/O |
  | OCS | packet → circuit switching |
  | HAMR | PMR → HAMR recording |
  | SF6-free switchgear | SF6 → vacuum / clean air |
  | 765 kV transformers | 345/500 kV → 765 kV transmission |
  | HVLP copper foil | HVLP1–3 → HVLP4/5 |
  | TTVR | surgery and repair → transcatheter replacement |

  Several picks also sit behind a supply bottleneck with only a handful of qualified suppliers: TSMC for merchant base dies; Seagate, then Western Digital, for HAMR; Mitsui Kinzoku and Co-Tech for most HVLP4/5; about five OEMs (Hyosung, HD Hyundai, Hitachi Energy, Siemens Energy, GE Vernova/Prolec) able to build and test at 765 kV.
- **High growth that failed the evidence gate.** These are listed, not ranked (Section 3.3):

  | Niche | Prob-weighted CAGR | Why it is not ranked |
  |---|---|---|
  | Vertical power-delivery modules | ~70% | No vendor discloses revenue; discrete backside stages and integrated voltage regulators can substitute |
  | US/EU NdFeB magnets | ~56% | The DoD-, Apple- and GM-contracted core is real, but uncontracted nameplate capacity is exposed to Chinese pricing |
  | AC→800 VDC conversion | ~110% | Growth starts from ~$80M, so it is listed as emerging |
- **High-quality but slower: #11–#14.** These are:
  - LEAP aftermarket hot-section/LLP material, ~26%;
  - OSAT CoWoS-class packaging, ~24%;
  - PAC-3/THAAD interceptor motors, ~22%;
  - T-glass cloth, ~17%.

  LEAP and the interceptor motors have sole-source or duopoly supply and multi-year contracts. They are the best choice for visibility rather than speed.
- **Robustness.** Ranking instead by the composite 7-criteria score keeps 8 of the 10. LEAP aftermarket and PAC-3/THAAD motors replace HVLP foil, and scale-up switch silicon and TTVR tie for the last slot.
- **Largest dollar growth, 2026→2030 central:**
  - HAMR, +~$28B
  - HBM base dies, +~$7B
  - scale-up switch silicon, +~$7B
  - OSAT CoWoS-class packaging (#12), +~$5B
  - LEAP aftermarket (#11), +~$4B
- **Is it priced in?** For the AI picks, largely yes. Each deep dive's bear case reviews valuations and coverage; for example, Seagate's share price rose roughly 11x from October 2024 to its June-2026 peak [R] before falling ~38%. The least-crowded picks are #6 (SF6-free switchgear, inside large diversified OEMs) and #10 (TTVR, about 2.5–5% of Edwards' revenue).

**Emerging from near zero (listed separately; sub-$0.1B 2026 bases, so CAGRs are not meaningful):**

| ID | Niche | 2026 | 2030 | Note |
|---|---|---|---|---|
| L08 | AC→800 VDC conversion equipment for AI data halls (deep-dived; Appendix A) | ~$0.04–0.18B (central ~$0.08B) | $1.0–6.0B (central ~$2.5B) | 2027→30 ~52%; adoption tied to NVIDIA Kyber-class racks; many credible vendors |
| L05 | CPO fiber-to-chip connectivity (FAU harnesses, detachable PIC connectors) | $0.05–0.15B | $1–3B | Same CPO timing risk as #2 and #8 |
| L09 | High-voltage (±400 V / 800 V) Li-ion BBU modules for AI racks | <$0.1B | $0.75–4B | Rides the 800 VDC transition |
| L14 | Microchannel lid cold plates (MLCP) for 3.5 kW+ packages | $5–40M | $0.3–4B | Needs package-level adoption (also on the too-early list) |
| L20 | Panel-level 2.5D (CoPoS/FOPLP-for-AI) and substrate-less CoWoP | ~$0 (pilot lines) | $0.3–3B | Volume after 2028 |
| L44 | e-SAF / power-to-liquid jet fuel for EU/UK mandate markets | ~$0 (pre-FID/pilot) | $0.3–1.5B | ReFuelEU 2030 synthetic sub-mandate is the switch |

---

## 2. Value-chain trees

These 13 trees place all 50 longlist items (L01-L50) in their value chains, from megatrend down to niche. Each item is marked once, and "→" points to the tree that holds it. Unmarked nodes are context (parents, substitutes, inputs) and were not scored. The trees show structure only; sizes, scores and evidence are in Section 3, the deep dives and Appendix B.

Legend: ★#n = final top-10 rank · ◆ = other deep-dived niche · •Lxx = other longlist item · [em] emerging (sub-scale 2026 base) · [OH] overhyped · [TE] too early (volume after ~2028) · → cross-reference

#### AI data centers (a): networking, optics and copper

```
AI DATA CENTERS: CLUSTER NETWORKING (optics + copper)
├── Scale-up fabric (XPU↔XPU, in-rack and rack-to-rack)
│   ├── Switch silicon
│   │   ├── NVLink Switch (captive NVIDIA; out of scope)
│   │   └── ★#3 L07 Merchant scale-up switch ICs (PCIe-AI, UALink, ESUN/SUE)
│   │       └── TSMC N5/N3 wafers, large-body ABF, Taiwan OSAT/test
│   ├── In-rack passive copper: cartridges, cable backplanes, flyover twinax
│   └── Optical scale-up: XPU optical I/O chiplets, microLED links  [TE]
├── Scale-out back-end fabric (NIC → leaf → spine)
│   ├── Copper links
│   │   └── •L06 200G/lane DSP-retimed AECs (incl. retimer DSP content)
│   ├── Optical links: pluggable → LPO/LRO [OH] → CPO/NPO
│   │   ├── 800G/1.6T pluggable module assembly  [OH beyond 2026]
│   │   ├── SiPh PIC die
│   │   │   └── ★#8 L03 Merchant 300 mm SiPh PIC foundry wafers
│   │   ├── Light sources
│   │   │   ├── EML / 50-100 mW CW-DFB chips (pluggables; slower)
│   │   │   └── ★#2 L01 Ultra-high-power CW InP lasers + ELS/ELSFP modules
│   │   ├── •L05 CPO fiber-to-chip (FAU harnesses, detachable PIC connectors)
│   │   └── Compound-semiconductor upstream
│   │       ├── •L04 Merchant InP single-crystal substrates
│   │       └── InP epi; indium metal (China export controls)
│   └── Optical circuit switching (TPU pods now; GPU domains later)
│       └── ★#4 L02 Merchant OCS systems
│           └── MEMS mirror arrays, 2D collimator / fiber arrays
└── Scale-across / DCI (2 km to 1,000+ km)
    ├── 800G/1.6T ZR/ZR+ coherent pluggables, coherent DSPs
    └── Hollow-core fiber  [OH near term]
```

#### AI data centers (b): power delivery, storage and thermal

```
AI DATA CENTERS: POWER DELIVERY, ENERGY STORAGE & THERMAL
├── Site power, behind the meter
│   ├── Gas recips; aeroderivative and frame GTs  [capacity-capped, price-led]
│   └── •L11 SOFC systems for data-center prime/bridge power
├── Facility distribution: 415/480 VAC → ±400 VDC / 800 VDC
│   ├── ◆ L08 AC→800 VDC conversion (power sidecars, central rectifiers)
│   │   ├── 1.2 kV SiC modules; GaN as the 800 VDC winner  [OH]
│   │   └── MV solid-state transformers (later SST phase of L08)  [TE]
│   └── DC protection: solid-state breakers, DC busway
├── Rack power & storage
│   ├── Power shelves / PSUs (5.5 → 12 kW+ per PSU)
│   └── Rack energy storage
│       ├── 48 V Li-ion BBU shelves
│       └── •L09 High-voltage (±400 V / 800 V) Li-ion BBU modules  [em]
├── Board & package power (48 V → ~0.7 V core)
│   ├── Core-rail regulation
│   │   ├── Lateral VR: controllers, DrMOS, TLVR inductors
│   │   ├── ◆ L10 Vertical (backside) power-delivery modules
│   │   └── In-package IVR / embedded-inductor regulators  [TE]
│   └── Decoupling passives
│       ├── •L12 Ultra-high-capacitance (≥47 µF) low-voltage MLCCs
│       └── •L13 Deep-trench silicon capacitors (discrete + embedded)
└── Thermal (direct-to-chip liquid)
    ├── Cold-plate loops; quick disconnects; ≥1 MW row/hall L2L CDUs
    ├── •L14 Microchannel lid cold plates (MLCP)  [em]
    └── Immersion  [OH]; two-phase direct-to-chip  [TE]
```

#### AI data centers (c): compute silicon, memory, packaging, substrates and storage

```
AI DATA CENTERS: COMPUTE SILICON, MEMORY, PACKAGING, SUBSTRATES, STORAGE
├── Accelerator / switch dies (N3 → N2/A16)  [→ front-end fabs tree]
├── Memory
│   ├── HBM stacks (HBM3E → HBM4 → HBM4E → HBM5)
│   │   ├── DRAM core dies (1b/1c nm)
│   │   ├── ★#1 L15 HBM4-gen logic base dies on foundry nodes (incl. custom cHBM)
│   │   └── TCB stacking, probe cards, ATE; hybrid bonding for 16-20-high  [TE]
│   └── LPDDR moving into servers
│       └── •L22 SOCAMM2 LPDDR5X/LPDDR6 modules
├── 2.5D / 3D integration
│   ├── CoWoS-L class (TSMC in-house)
│   │   └── ◆ L19 OSAT-outsourced CoWoS-class (ASE/SPIL, Amkor)
│   ├── •L20 Panel-level CoPoS / FOPLP and substrate-less CoWoP  [em]
│   └── SoIC 3D stacking → D2W hybrid bonders
├── Package substrate (FC-BGA)
│   ├── •L21 Large-body (≥120 mm, ≥24-layer) ABF substrates
│   │   ├── ABF build-up film; low-alpha spherical silica
│   │   └── Core laminate / prepreg
│   │       └── ◆ L18 Low-CTE (T-glass-class) glass cloth & yarn
│   └── Glass-core (TGV) substrates  [TE]
├── Board level (compute/switch trays, midplanes)
│   └── M8U/M9 ultra-low-loss CCL → high-layer-count PCBs
│       ├── ★#9 L16 HVLP4/HVLP5 copper foil
│       ├── •L17 Quartz (Q-glass) fiber cloth & yarn
│       └── AI-grade carbide micro-drills (consumable)
└── Storage
    ├── Nearline HDD: PMR/ePMR/MAMR → HAMR
    │   └── ★#5 L23 HAMR nearline HDDs (3.5-inch, ≥30 TB)
    │       └── Laser-on-slider heads; FePt media on glass substrates
    └── QLC eSSD ≥61 TB; High Bandwidth Flash  [TE]
```

#### Leading-edge front-end chip manufacturing

```
LEADING-EDGE FRONT-END (2nm / A16 / 18A / 14A; GAA nanosheets; backside power)
├── Lithography
│   ├── EUV scanners
│   │   ├── Low-NA NXE:3800E / 4000F
│   │   └── •L24 High-NA (0.55 NA) EUV scanners (EXE:5200B)
│   │       └── Zeiss SMT optics; Trumpf drive laser
│   ├── EUV materials: CAR resists; metal-oxide resists (spin-on, dry)
│   └── Mask chain: blanks, multi-beam writers, actinic inspection; CNT pellicles  [TE]
├── Deposition / metallization
│   ├── Si/SiGe superlattice epi; ALD high-k and work-function metals + precursors
│   └── W → Mo fill (Mo oxychloride precursors); Ru interconnect  [TE]
├── Etch / clean: GAA selective etch; CVD-SiC and quartz chamber parts
├── Backside power + wafer-level 3D
│   ├── W2W fusion / hybrid bonding; edge trim, thinning
│   └── nTSV / backside contact etch + fill
├── Process control: multibeam e-beam inspection, CD-SEM
└── Foundry output that feeds other trees
    ├── Leading-edge logic wafers (accelerators, switch ASICs)
    ├── HBM base dies, N12 → N3P custom  [→ L15, AI tree (c)]
    └── 300 mm SiPh PIC wafers  [→ L03, AI tree (a)]
```

#### Power generation, grid and electrification

```
POWER GENERATION, GRID & ELECTRIFICATION
├── Generation
│   ├── Gas: frame GTs → SX/DS hot-gas-path castings  [→ aerospace tree]
│   ├── On-site SOFC  [→ L11, AI tree (b)]
│   └── Nuclear  [→ nuclear tree]
├── Grid-scale storage (BESS)
│   ├── DC block: LFP ESS cells
│   │   ├── •L28 FEOC-compliant (non-PFE) North American LFP ESS cells
│   │   └── Chinese commodity LFP ESS cells  [OH: ASP deflation]
│   └── Power conversion
│       └── •L25 Grid-forming PCS + controls for utility BESS
├── Transmission: AC substations
│   ├── Power transformers & reactors
│   │   ├── ★#7 L26 765 kV-class autotransformers & shunt reactors (US backbones)
│   │   ├── ≤500 kV LPT / GSU  [price-led; OH beyond 2028]
│   │   └── Inputs: GOES, bushings, on-load tap changers, pressboard
│   ├── HV switchgear & breakers (≥52 kV)
│   │   ├── Conventional SF6 GIS / AIS (EU F-gas phase-out)
│   │   └── ★#6 L27 SF6-free HV switchgear & circuit breakers
│   │       ├── HV vacuum interrupters + clean air
│   │       └── C4-FN / C5-FK fluoronitrile-mixture GIS
│   └── FACTS: STATCOM, synchronous condensers
├── Transmission: HVDC (VSC converter stations, 525 kV cable)
└── Distribution & end use: distribution transformers, MV gear; MV SST  [TE]
```

#### Nuclear

```
NUCLEAR (uprates, restarts, new build, SMRs, fuel cycle)
├── Front-end fuel cycle
│   ├── Mining → conversion (UF6)
│   ├── Enrichment: Western LEU SWU; LEU+ (5-10%) for longer cycles
│   ├── HALEU enrichment + deconversion  [TE]
│   └── Fuel fabrication: LWR assemblies, Zr cladding; TRISO / metallic  [TE]
├── Operating fleet
│   ├── Power uprates: turbine-generator retrofits, NSSS re-analysis
│   ├── 80-year licence renewal: digital I&C, steam-generator replacement
│   └── Restarts (one-offs); outage services; pump/valve aftermarket
├── Western LWR new build
│   ├── Nuclear island
│   │   ├── •L29 Heavy components + ultra-large forgings
│   │   │   ├── AP1000 long-lead items: RPV shells/heads, SG tubesheets
│   │   │   └── Light-water SMR RPVs / modules (BWRX-300, NuScale, AP300)
│   │   ├── Canned-motor reactor coolant pumps (sole source)
│   │   └── ASME III pumps & valves; CRDMs
│   └── Turbine island (Arabelle, GE Vernova, Siemens Energy, MHI)
├── Advanced reactors
│   ├── SMR developer / licensor revenue before 2030  [OH]
│   └── Gen-IV components, nuclear graphite, microreactors  [TE]
└── Back end: dry casks; recycling  [TE]; decommissioning
```

#### Defense, rearmament and drones

```
DEFENSE, REARMAMENT & DRONES (NATO pledges, US munitions rebuild, Golden Dome)
├── Missiles & interceptors
│   ├── Air & missile defense (PAC-3 MSE, THAAD, SM-x, ESSM, IRIS-T SL, Aster, CAMM)
│   │   ├── Propulsion
│   │   │   ├── ◆ L30 Interceptor-class solid rocket motors
│   │   │   │   └── Ammonium perchlorate, HTPB, Al powder, cases, nozzles
│   │   │   └── Large boosters (hypersonic, Sentinel)  [TE]
│   │   └── Seekers (Ka-band RF, IR), IMUs, thermal batteries
│   └── Affordable-mass cruise missiles, jet OWA drones, jet interceptors, targets
│       └── ◆ L31 Low-cost expendable small turbojets (~50-400 lbf)
├── Munitions: artillery shell bodies  [OH]; energetics; propellant charges
├── Sensors: AESA radars → GaN-on-SiC T/R modules; EO/IR
├── Drones (FPV / OWA / ISR / Group 2-3)
│   ├── Airframe assembly  [OH]
│   ├── Propulsion & power
│   │   ├── BLDC motors → NdFeB magnets  [→ L45, minerals tree]
│   │   └── •L33 NDAA-compliant silicon-anode Li-ion cells
│   ├── Thermal cores, MANET mesh radios, GNSS-denied navigation
│   └── Fiber-optic FPV payout spools  [OH]
└── Counter-UAS
    ├── Detection: RF, radar, EO/IR, C2 fusion
    ├── Kinetic defeat
    │   ├── •L32 Low-cost electric interceptor drones (~$1k-50k/unit)
    │   ├── Jet interceptors (Coyote-class) ← L31 engines
    │   └── Guns + airburst ammunition; APKWS-class rockets
    └── Directed energy (HEL, HPM)  [TE]
```

#### Space and satellites

```
SPACE & SATELLITES
├── Launch: reusable medium/heavy (Falcon 9, Starship, New Glenn); small launch  [OH]
├── Space segment (satellite manufacturing)
│   ├── Bus: III-V multijunction solar cells ← Ge substrates; EP; star trackers
│   ├── Comms payloads
│   │   ├── Phased-array Ku/Ka; large-aperture D2D arrays
│   │   └── Optical inter-satellite link terminals
│   └── Sensing payloads
│       ├── Small-sat X-band SAR (GaN T/R modules, deployable antennas)
│       └── Missile warning/tracking IR payloads → HgCdTe / SLS FPAs
├── Ground segment: gateways; phased-array user terminals  [merchant ICs OH]
├── Services
│   ├── LEO broadband (consumer, aviation, maritime, government)
│   ├── Mobile satellite → direct-to-device
│   │   ├── •L34 Broadband D2D voice/data (MNO wholesale + OEM-funded)
│   │   └── Emergency SOS / messaging D2D (slower)
│   ├── Earth observation
│   │   └── •L35 Small-sat X-band SAR: sovereign sales + defense tasking/data
│   └── Orbital data centers  [OH]; in-space servicing  [TE]
└── Defense space (Golden Dome / SDA PWSA)
    ├── Transport + tracking layers → optical terminals, IR FPAs
    └── Space-based interceptors  [TE]
```

#### Robotics and humanoids

```
ROBOTICS & HUMANOIDS (+ industrial automation)
├── Humanoid robots  (every humanoid node rides one correlated unit-volume bet)
│   ├── Actuation (largest BOM block)
│   │   └── •L37 Merchant joint-actuator assemblies  [OH]
│   │       ├── Rotary: frameless motors, harmonic / planetary reducers  [OH]
│   │       ├── Linear: inverted planetary roller screws (IPRS)  [OH]
│   │       │   └── Thread-grinding / hard-turning machine tools
│   │       └── Encoders, TMR sensor ICs, joint servo drives (GaN / Si)
│   ├── End effectors
│   │   ├── •L36 High-DoF (≥15 active DoF) dexterous hands
│   │   │   └── Coreless / micro-BLDC motors, micro gearheads, tendons
│   │   └── Fingertip / palm tactile e-skin  [TE]
│   ├── Sensing: 6-axis force/torque sensors, 3D lidar, stereo/ToF cameras
│   ├── Compute: ≥100 TOPS on-robot modules (Jetson Thor class)
│   └── Power: 2-3 kWh high-rate packs; structure (Mg/Al castings, PEEK)
├── Industrial robots & cobots: RV / harmonic reducers (mature), servos, vision
├── Mobile robots: AMRs, ASRS, lawn robots, quadrupeds → 3D lidar, edge compute
└── Services: embodied-AI data collection (teleop, mocap); EOL test benches
```

#### Healthcare: obesity drugs, biomanufacturing and medtech

```
HEALTHCARE: OBESITY DRUGS, BIOMANUFACTURING & MEDTECH
├── Obesity / incretin drugs (GLP-1, GIP, glucagon, amylin)
│   ├── Drug substance (API)
│   │   ├── Injectable peptides: SPPS / hybrid; recombinant + acylation (Novo)
│   │   │   ├── Lilly/Novo overflow CDMO (slows as both insource)
│   │   │   ├── •L38 Outsourced peptide API for next-wave sponsors
│   │   │   └── Inputs: Fmoc amino acids  [OH]; resins; prep-HPLC silica
│   │   └── Oral small-molecule GLP-1 (orforglipron) API + intermediates
│   ├── Drug product: fill-finish  [overbuild risk 2028+]; cartridges; pens
│   └── Generic semaglutide in 2026 loss-of-exclusivity markets
├── Other therapeutics
│   ├── ADCs → •L42 Topo-I (exatecan/DXd) payload-linker HPAPI, outsourced
│   ├── siRNA / ASO for cardiometabolic targets (LDL-C, Lp(a), ATTR-CM)
│   │   ├── •L40 Outsourced GalNAc-siRNA/ASO drug substance
│   │   └── •L41 2'-modified phosphoramidites + GalNAc building blocks
│   ├── Radioligand therapy: n.c.a. Lu-177; Ac-225 / Pb-212  [TE]
│   └── IV → SC conversion: recombinant hyaluronidase co-formulation
└── Medical devices
    ├── Structural heart
    │   ├── TAVR (mature); TEER repair clips
    │   └── Transcatheter valve replacement (mitral / tricuspid)
    │       ├── ★#10 L39 TTVR systems (EVOQUE, LuX-Valve)
    │       └── TMVR (SAPIEN M3, Tendyne, Intrepid)
    ├── Electrophysiology: pulsed-field ablation catheters + generators
    └── Imaging: photon-counting CT detectors (CdTe / CZT)
```

#### Reshoring and critical minerals

```
RESHORING & CRITICAL MINERALS (non-China / non-FEOC supply)
├── Rare earths → permanent magnets
│   ├── Mining & concentration (bastnaesite, monazite); ionic-clay HREE  [TE]
│   ├── Separation
│   │   ├── NdPr oxide ex-China
│   │   └── •L47 Dy/Tb oxide, metal & GBD alloys ex-China
│   ├── Metallization & alloying
│   │   └── •L46 Ex-China NdPr metal + NdFeB master-alloy conversion
│   ├── Magnet making
│   │   ├── Sintered NdFeB, Japan incumbents (slow growth)
│   │   ├── ◆ L45 New-build NA/EU sintered NdFeB (DFARS, incl. GBD grades)
│   │   ├── Bonded NdFeB; SmCo (defense, small)
│   │   └── RE-free magnets (iron nitride, MnBi)  [TE]
│   └── Recycling: magnet-to-magnet  [TE]
├── Battery minerals (FEOC / AD-CVD driven)
│   ├── Graphite anode material; North American synthetic new-build
│   ├── Substitutes: Si-C, hard carbon  [→ L48/L49, other-drivers tree]
│   └── Lithium conversion, cobalt  [OH]
├── Export-controlled minor metals
│   ├── Germanium: GeCl4 (fiber), IR optics, space-cell substrates
│   ├── Gallium  [OH: tiny market]; antimony, tungsten  [OH: price-led]
│   └── Scandium (SOFC electrolyte, Al-Sc)  [TE]
└── Enablers: DoD price floor & offtakes, DFARS 2027 provenance rule, stockpile
```

#### Commercial aerospace, shipbuilding and heavy industrial

```
COMMERCIAL AEROSPACE, SHIPBUILDING & HEAVY INDUSTRIAL
├── Aero engines, original equipment
│   ├── Hot section: SX/DS turbine airfoils ← ceramic cores (bottleneck); TBCs
│   ├── SiC/SiC CMC shrouds, nozzles, combustor liners
│   └── Rotating parts: Ni-superalloy billet / PM powder; Ti forgings; bearings
├── Engine aftermarket
│   ├── New-generation narrowbody shop visits
│   │   ├── LEAP-1A/-1B shop-visit MRO (labor + OEM material)
│   │   │   └── ◆ L43 LEAP HPT durability kits, hot-section spares, LLP stacks
│   │   └── PW1100G GTF MRO (inspection peak passing; slower)
│   └── Mature engines: CFM56 / V2500 shop visits, used serviceable material
├── Airframe & cabin: CFRP prepreg, fasteners, premium seats; LEO IFC terminals
├── Aviation fuel
│   ├── HEFA-SPK SAF (waste-lipid feedstock is the bottleneck)
│   └── •L44 e-SAF / power-to-liquid for EU and UK mandate markets  [em]
├── Industrial gas turbines (share casting capacity with aero)
│   └── H/J-class hot-gas-path SX/DS blades & vanes, OE + spares
└── Shipbuilding & naval
    ├── LNG carriers; dual-fuel two-stroke engines  [orders peaking]
    └── Submarine industrial base: reactor components, castings, forgings
```

#### Other drivers: autonomy, battery chemistry and consumer AI devices

```
OTHER STRUCTURAL DRIVERS
├── Autonomy: L4 passenger robotaxi
│   ├── Service layer (fares + platform take)
│   │   ├── •L50 Driverless ride-hail revenue (US/West, China, Gulf)
│   │   └── Outsourced fleet operations (depot, charging, cleaning)  [em]
│   ├── Vehicle layer: purpose-built bodies (mostly captive), by-wire redundancy
│   └── Merchant L4 sensor + compute kits (Thor-class compute; lidar  [OH])
├── Battery chemistry transitions
│   ├── Anode materials
│   │   ├── Silicon anodes
│   │   │   ├── SiOx composites (EV blends; slower)
│   │   │   ├── •L49 CVD Si-C composite (silane into porous carbon)
│   │   │   └── 100% Si anodes  [→ L33 drone cells, defense tree]
│   │   └── Sodium-ion anodes
│   │       └── •L48 Hard carbon (biomass, resin or pitch precursor)
│   ├── Na-ion cells (ESS, truck start-stop, 2W / A00 EVs)
│   └── Sulfide solid electrolytes + Li2S  [TE]
├── Consumer AI devices: display-equipped AI/AR smart glasses
│   └── Per-eye optical engine (not longlisted: borderline size floor [E])
│       ├── Glass waveguide combiners (reflective array, diffractive SRG)
│       ├── SiC waveguides  [TE]
│       └── Microdisplays: microLED-on-silicon, LCoS, micro-OLED
└── Smaller wildcards: quantum dilution refrigerators, PFAS ion-exchange media
```

---

## 3. Longlist scoring

### 3.1 How the longlist was built and scored

- **Mapping.** Sixteen megatrend researchers mapped supply chains 3–5 levels down. The megatrends were:
  - AI data-center optics; AI data-center power and thermal; advanced packaging and memory; leading-edge front-end fabs
  - grid; nuclear; defense; drones; space; robotics
  - obesity drugs and biomanufacturing; critical minerals; other medtech
  - an Asia-first press sweep; aerospace, shipbuilding and heavy industry; and wildcards
- **Gap-filling.** A completeness critic added six gap topics: AECs and scale-up copper, direct-to-chip cooling, robotaxis, HAMR storage, GaN/SiC for 800 VDC, and AR-glasses optics.
- **Consolidation.** This produced 122 raw candidates. Merging duplicates, splitting broad segments into their faster sub-niches, and dropping sub-floor or too-broad items left 50. Appendix B lists the 80 raw candidates that were merged or dropped, with reasons.
- **Scoring.** Three independent scorers scored every longlist item, each through a different lens: demand, supply and skeptic. The table shows panel medians.

**Rubric (1–5; higher is better on every criterion):**

| Criterion | 5 | 3 | 1 |
|---|---|---|---|
| **G** — demand growth, 2026–30 CAGR | ≥40% (4 = 25–40%) | 15–25% (2 = 8–15%) | <8% |
| **V** — visibility | committed capex, LTAs or design wins | roadmaps plus some orders | speculative |
| **S** — supply tightness / pricing power | ≤3 qualified suppliers and multi-year lead times | moderately concentrated | commoditized |
| **T** — timing | ramp underway 2026–28 | inflection 2028–29 | after 2030 |
| **Sub** — substitution risk | no alternative in window | credible but slow alternative | actively displaced |
| **Cyc** — cyclicality / overbuild risk | secular, low double-ordering / China-flood risk | some capex-cycle exposure | overbuild-prone |
| **Ev** — evidence quality | multiple primary sources triangulated | mixed | press-release only |

**Composite** = 2×G + V + S + T + Sub + Cyc + Ev (maximum 40). Growth is double-weighted because it is the question being asked.

### 3.2 Phase-3 scoring table (all 50 longlist niches)

Sorted by Phase-3 composite. Sizes and CAGRs are the Phase-1/2 researcher and panel views; Phase-4 deep dives superseded them for the 18 niches in the last column. [em] marks a niche emerging from near zero.

| P3 # | ID | Niche | Megatrend | 2026 | 2030 | CAGR (panel) | G | V | S | T | Sub | Cyc | Ev | Score /40 | Phase-4 outcome |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L23 | HAMR nearline HDDs, 3.5-inch, >=30 TB | AI DC storage | $2.5-5.5B | $15-40B | 35-60% | 5 | 4 | 5 | 5 | 4 | 3 | 4 | 35 | **★ Top 10 #5** (prob-wtd 55%) |
| 2 | L15 | HBM4 logic base dies on foundry nodes (incl. cHBM) | AI packaging/memory | $0.3-1.0B | $5-16B | 50-90% | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 33 | **★ Top 10 #1** (prob-wtd 78%) |
| 3 | L18 | Low-CTE T-glass cloth/yarn for IC-substrate cores | AI packaging/memory | $0.22-0.33B | $0.6-1.1B | 20-35% | 4 | 4 | 5 | 5 | 4 | 3 | 4 | 33 | ◆ deep-dived, prob-wtd 17% |
| 4 | L30 | Interceptor-class solid rocket motors, NATO+allies | Defense rearmament | $1.2-2.0B | $2.4-4.5B | 22-35% | 4 | 4 | 5 | 5 | 5 | 4 | 2 | 33 | ◆ deep-dived, prob-wtd 22% |
| 5 | L01 | UHP CW InP lasers and ELS modules for CPO/NPO | AI DC optics | $0.08-0.3B | $2-6B | 50-90% | 5 | 4 | 5 | 4 | 3 | 2 | 4 | 32 | **★ Top 10 #2** (prob-wtd 73%) |
| 6 | L02 | Merchant optical circuit switches (OCS), AI fabrics | AI DC optics | $0.35-0.65B | $3-6B | 40-75% | 5 | 4 | 4 | 5 | 3 | 2 | 4 | 32 | **★ Top 10 #4** (prob-wtd 57%) |
| 7 | L39 | Transcatheter tricuspid valve replacement (TTVR) | Healthcare & medtech | $0.25-0.5B | $1.0-1.7B | 28-42% | 4 | 4 | 4 | 5 | 3 | 5 | 3 | 32 | **★ Top 10 #10** (prob-wtd 27%) |
| 8 | L43 | LEAP-1A/-1B OEM hot-section, HPT kit and LLP parts | Commercial aerospace | $1.5-3B | $6-11B | 25-40% | 4 | 4 | 5 | 5 | 4 | 4 | 2 | 32 | ◆ deep-dived, prob-wtd 26% |
| 9 | L03 | Merchant 300 mm SiPh PIC foundry wafers (CPO-grade) | AI DC optics | $0.5-1.0B | $1.8-5.0B | 40-70% | 5 | 4 | 3 | 5 | 4 | 2 | 3 | 31 | **★ Top 10 #8** (prob-wtd 41%) |
| 10 | L45 | NA/EU sintered NdFeB magnets (non-China, DFARS) | Critical minerals | $0.15-0.45B | $0.8-2.8B | 40-70% | 5 | 4 | 4 | 5 | 3 | 2 | 3 | 31 | ◆ deep-dived, prob-wtd 56% (below gate) |
| 11 | L12 | Ultra-high-cap low-voltage MLCCs (>=47 uF) for AI | AI DC power/thermal | $1.0-2.5B | $3-7B | 20-35% | 4 | 4 | 4 | 5 | 4 | 2 | 4 | 31 | — |
| 12 | L27 | SF6-free HV (>=52 kV) switchgear and breakers | Grid & electrification | $0.7-1.6B | $3.5-6B | 25-45% | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 31 | **★ Top 10 #6** (prob-wtd 43%) |
| 13 | L21 | Next-gen ABF FC-BGA substrates (>=120 mm, >=24L) | AI packaging/memory | $0.2-0.6B | $4-10B | 60-110% | 5 | 4 | 5 | 4 | 3 | 2 | 2 | 30 | — |
| 14 | L46 | Ex-China NdPr metal and NdFeB master-alloy | Critical minerals | $0.1-0.3B | $0.6-1.5B | 35-60% | 5 | 3 | 5 | 4 | 4 | 2 | 2 | 30 | — |
| 15 | L50 | Driverless robotaxi ride-hail revenue (US/China/Gulf) | L4 robotaxi autonomy | $0.5-1.2B | $4-18B | 50-90% | 5 | 3 | 3 | 5 | 4 | 3 | 2 | 30 | — |
| 16 | L07 | Merchant scale-up switch silicon (PCIe/UALink/ESUN) | AI DC copper/scale-up | $0.6-1.8B | $3.5-9B | 30-55% | 4 | 4 | 4 | 5 | 3 | 3 | 3 | 30 | **★ Top 10 #3** (prob-wtd 61%) |
| 17 | L10 | Vertical (backside) power modules for AI accelerators | AI DC power/thermal | $0.3-0.8B | $3-8B | 40-75% | 5 | 3 | 4 | 4 | 3 | 2 | 3 | 29 | ◆ deep-dived, prob-wtd 70% (below gate) |
| 18 | L34 | Broadband D2D satellite-to-phone wholesale service | Space & satellites | $0.15-0.4B | $1.5-5B | 50-100% | 5 | 3 | 4 | 4 | 3 | 3 | 2 | 29 | — |
| 19 | L47 | Ex-China separated Dy/Tb oxide, metal and alloys | Critical minerals | $0.04-0.2B | $0.3-1.4B | 35-65% | 5 | 3 | 5 | 4 | 3 | 2 | 2 | 29 | — |
| 20 | L16 | HVLP4/5 copper foil for M8U/M9 ultra-low-loss CCL | AI packaging/memory | $0.17-0.31B | $1.0-1.8B | 28-50% | 4 | 3 | 5 | 5 | 3 | 2 | 3 | 29 | **★ Top 10 #9** (prob-wtd 35%) |
| 21 | L26 | 765 kV EHV autotransformers and shunt reactors (US) | Grid & electrification | $0.15-0.35B | $1.0-2.0B | 28-50% | 4 | 4 | 5 | 3 | 4 | 3 | 2 | 29 | **★ Top 10 #7** (prob-wtd 41%) |
| 22 | L31 | Low-cost expendable small turbojets (50-400 lbf) | Military drones/C-UAS | $0.2-0.5B | $0.9-3.0B | 30-55% | 4 | 3 | 4 | 5 | 3 | 3 | 3 | 29 | ◆ deep-dived, prob-wtd 27% (below gate) |
| 23 | L22 | SOCAMM2 LPDDR modules for DC CPUs and inference | AI packaging/memory | $1-4B | $8-30B | 40-70% | 5 | 3 | 4 | 5 | 3 | 1 | 2 | 28 | — |
| 24 | L11 | SOFC systems for data-center behind-the-meter power | AI DC power/thermal | $2.5-3.5B | $7-15B | 25-40% | 4 | 4 | 3 | 5 | 2 | 2 | 4 | 28 | — |
| 25 | L29 | LWR nuclear-island heavy components and big forgings | Nuclear new build | $0.3-0.7B | $1.2-3.0B | 20-55% | 4 | 3 | 4 | 3 | 4 | 2 | 4 | 28 | — |
| 26 | L33 | NDAA-compliant Si-anode Li-ion cells, military drones | Military drones/C-UAS | $0.35-0.8B | $1.2-3.0B | 25-45% | 4 | 3 | 3 | 5 | 3 | 3 | 3 | 28 | — |
| 27 | L04 | Merchant InP single-crystal substrates | AI DC optics | $0.4-0.65B | $1.2-2.2B | 18-35% | 3 | 4 | 4 | 5 | 3 | 2 | 4 | 28 | — |
| 28 | L05 | CPO fiber-to-chip connectivity (FAUs, PIC connectors) | AI DC optics | $0.05-0.15B | $1-3B | 50-100% | 5 | 3 | 3 | 4 | 3 | 2 | 2 | 27 | — |
| 29 | L06 | 200G/lane (1.6T) DSP-retimed active electrical cables | AI DC copper/scale-up | $0.1-0.3B | $1.5-3.5B | 45-90% | 5 | 3 | 3 | 4 | 2 | 2 | 3 | 27 | — |
| 30 | L08 | AC-to-800 VDC power-conversion gear for AI racks | AI DC power/thermal | $0.1-0.35B | $4-9B | 50-130% | 5 | 3 | 2 | 4 | 3 | 2 | 3 | 27 | ◆ deep-dived, prob-wtd 110% (below gate) |
| 31 | L28 | FEOC-compliant N. American LFP grid-storage cells | Grid & electrification | $0.8-1.6B | $3.0-5.5B | 25-45% | 4 | 4 | 2 | 5 | 3 | 2 | 3 | 27 | — |
| 32 | L35 | Commercial small-sat X-band SAR (sovereign/defense) | Space & satellites | $0.6-1.3B | $2.5-4.5B | 22-38% | 4 | 3 | 3 | 5 | 3 | 3 | 2 | 27 | — |
| 33 | L42 | Outsourced topo-I (exatecan/DXd) ADC payload-linkers | Healthcare & medtech | $0.3-0.7B | $0.8-2.0B | 25-42% | 4 | 3 | 3 | 5 | 3 | 3 | 2 | 27 | — |
| 34 | L19 | OSAT-outsourced CoWoS-class 2.5D packaging | AI packaging/memory | $1.5-3B | $5-11B | 25-45% | 4 | 3 | 3 | 5 | 3 | 2 | 2 | 26 | ◆ deep-dived, prob-wtd 24% |
| 35 | L40 | Outsourced GalNAc-siRNA/ASO API, cardiometabolic | Healthcare & medtech | $0.15-0.9B | $0.6-3.0B | 25-45% | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 26 | — |
| 36 | L20 | Panel-level CoPoS/FOPLP and CoWoP 2.5D for AI [em] | AI packaging/memory | ~$0 (pilot lines) | $0.3-3B | n.m. (>100% from ~0) | 5 | 2 | 4 | 3 | 3 | 2 | 1 | 25 | — |
| 37 | L44 | e-SAF / power-to-liquid jet fuel (EU/UK mandates) [em] | Commercial aerospace | ~$0 (pre-FID/pilot) | $0.3-1.5B | n.m. (from ~0) | 5 | 2 | 4 | 2 | 3 | 2 | 2 | 25 | — |
| 38 | L13 | Deep-trench silicon capacitors for AI package PDN | AI DC power/thermal | $0.15-0.5B | $0.6-2.0B | 25-50% | 4 | 2 | 4 | 4 | 3 | 3 | 1 | 25 | — |
| 39 | L25 | Grid-forming PCS and controls for utility BESS | Grid & electrification | $0.3-0.8B | $2.5-5.5B | 28-50% | 4 | 3 | 2 | 4 | 3 | 2 | 2 | 24 | — |
| 40 | L24 | High-NA (0.55 NA) EUV lithography scanners | Leading-edge fabs | $1.6-4.1B | $4.4-10B | 12-30% | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 24 | — |
| 41 | L09 | HV (+/-400 V/800 V) Li-ion BBU modules for AI racks [em] | AI DC power/thermal | <$0.1B | $0.75-4B | 60-130% (base effect) | 5 | 2 | 2 | 3 | 2 | 2 | 2 | 23 | — |
| 42 | L32 | Low-cost electric interceptor drones, NATO/allied | Military drones/C-UAS | $0.1-0.3B | $1.5-4B | 45-90% | 5 | 2 | 1 | 5 | 2 | 1 | 2 | 23 | — |
| 43 | L36 | High-DoF (>=15 DoF) dexterous hands for humanoids | Humanoid robotics | $0.08-0.35B | $0.6-4.0B | 40-90% | 5 | 2 | 2 | 3 | 2 | 2 | 2 | 23 | — |
| 44 | L17 | Quartz (Q-glass) fiber cloth/yarn for M9 CCL | AI packaging/memory | $0.1-0.3B | $0.35-1.5B | 20-55% | 4 | 2 | 4 | 4 | 2 | 1 | 2 | 23 | — |
| 45 | L49 | CVD silicon-carbon (Si-C) composite anode material | Battery chemistry | $0.15-0.5B | $0.7-2.0B | 25-45% | 4 | 2 | 2 | 4 | 3 | 2 | 2 | 23 | — |
| 46 | L38 | Outsourced peptide API, next-wave incretin/amylin | Obesity/incretin drugs | $0.25-0.6B | $0.5-1.5B | 12-32% | 3 | 3 | 3 | 4 | 2 | 3 | 2 | 23 | — |
| 47 | L14 | Microchannel lid cold plates (MLCP), 3.5 kW+ chips [em] | AI DC power/thermal | $5-40M | $0.3-4B | n.m. (>100% from ~0) | 5 | 1 | 3 | 3 | 2 | 2 | 1 | 22 | — |
| 48 | L37 | Merchant humanoid joint actuators incl. IPRS | Humanoid robotics | $0.04-0.25B | $0.4-3.0B | 40-80% | 5 | 2 | 2 | 3 | 2 | 1 | 2 | 22 | — |
| 49 | L41 | 2'-modified amidites and GalNAc building blocks | Healthcare & medtech | $0.1-0.3B | $0.3-0.9B | 15-35% | 3 | 2 | 4 | 4 | 3 | 2 | 1 | 22 | — |
| 50 | L48 | Hard carbon anode material for sodium-ion cells | Battery chemistry | $0.15-0.55B | $0.6-2.5B | 25-50% | 4 | 2 | 2 | 4 | 2 | 1 | 2 | 21 | — |

*Sources and claims behind every row are in [Appendix B](appendix-b-longlist-evidence.md). The table is also in [`data/longlist_phase3_scores.csv`](data/longlist_phase3_scores.csv).*

### 3.3 Phase-4 re-score of the 18 deep-dived niches, and the final ranking rule

**Which niches were deep-dived.** The 13 highest-scoring Phase-3 niches, plus five more:
- three high-growth alternates: small turbojets, scale-up switch silicon, and 800 VDC conversion;
- two challengers that a separate top-10 challenger agent surfaced: US 765 kV transformers and OSAT CoWoS-class packaging.

**How each deep dive was built.** Each went through four independent passes:
1. a deep-dive researcher;
2. a fact-checker and quant, who rebuilt the top-down and bottom-up sizing from scratch;
3. a bear-case analyst;
4. an editor, who integrated the three. Where the fact-check had evidence, it overrode the draft.

Three new scorers then re-scored all 18 on the final write-ups.

**Ranking rule.**
1. **Gate.** The 2026 central size must be at least ~$0.1B, and the six non-growth criteria must sum to at least 18/30 (an average of 3 or better).
2. **Sort.** Eligible niches are ranked by panel-median probability-weighted 2026→2030 CAGR. Ties are broken on the composite score.

Growth is the sort key because the question is which niches will grow the most. The gate stops thinly evidenced, base-effect-driven stories from topping the list.

**Sensitivity.** Ranking by the composite alone keeps 8 of the 10. LEAP aftermarket and PAC-3/THAAD motors would replace HVLP foil, and scale-up switch silicon and TTVR would tie for the last place.

| Final | ID | Niche | 2026 (central) | 2030 (central) | Central CAGR | Prob-wtd CAGR | 2027→30 | G/V/S/T/Sub/Cyc/Ev | Non-growth /30 | Composite /40 | Gate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **#1** | L15 | Merchant HBM4/4E logic base dies | $0.60B | $7.5B | 88% | 78% | 33% | 5/4/5/5/4/2/3 | 23 | 33 | pass |
| **#2** | L01 | UHP CW InP lasers + ELS modules for CPO/NPO | $0.19B | $2.3B | 86% | 73% | 28% | 5/4/4/4/3/2/3 | 20 | 30 | pass |
| **#3** | L07 | Merchant scale-up switch silicon (non-NVLink) | $0.90B | $8.0B | 73% | 61% | 45% | 5/3/3/5/2/2/3 | 18 | 28 | pass |
| **#4** | L02 | Merchant optical circuit switches (OCS) | $0.47B | $3.3B | 63% | 57% | 40% | 5/4/4/5/3/2/3 | 21 | 31 | pass |
| **#5** | L23 | HAMR nearline HDDs (>=30 TB) | $4.9B | $33.0B | 61% | 55% | 42% | 5/4/4/5/3/3/4 | 23 | 33 | pass |
| **#6** | L27 | SF6-free HV (>52 kV) switchgear and breakers | $0.70B | $3.4B | 48% | 43% | 35% | 5/4/4/5/4/4/3 | 24 | 34 | pass |
| **#7** | L26 | US 765 kV autotransformers + shunt reactors | $0.27B | $1.2B | 45% | 41% | 32% | 5/4/4/4/4/3/3 | 22 | 32 | pass |
| **#8** | L03 | Merchant 300 mm SiPh PIC foundry wafers | $0.70B | $3.3B | 47% | 41% | 38% | 5/4/3/5/3/2/3 | 20 | 30 | pass |
| **#9** | L16 | HVLP4/5 copper foil for M8-M10 CCL | $0.33B | $1.3B | 41% | 35% | 33% | 4/3/3/5/3/2/3 | 19 | 27 | pass |
| **#10** | L39 | Transcatheter tricuspid valve replacement | $0.25B | $0.70B | 29% | 27% | 27% | 4/3/4/4/2/4/3 | 20 | 28 | pass |
| #11 | L43 | LEAP aftermarket OEM hot-section/LLP material | $2.5B | $6.8B | 28% | 26% | 28% | 4/4/5/5/3/4/4 | 25 | 33 | pass |
| #12 | L19 | OSAT-outsourced CoWoS-class 2.5D packaging | $2.8B | $7.5B | 28% | 24% | 14% | 3/3/3/5/2/2/3 | 18 | 24 | pass |
| #13 | L30 | PAC-3 MSE / THAAD interceptor rocket motors | $0.56B | $1.3B | 23% | 22% | 22% | 3/4/4/4/4/3/4 | 23 | 29 | pass |
| #14 | L18 | Low-CTE T-glass cloth/yarn for IC substrates | $0.21B | $0.46B | 22% | 17% | 19% | 3/3/4/4/3/2/3 | 19 | 25 | pass |
| — | L08 | AC-to-800 VDC conversion for AI data halls | $0.08B | $2.5B | 136% | 110% | 52% | 5/2/2/3/2/2/2 | 13 | 23 | fails: 2026 base < $0.1B |
| — | L10 | Vertical power-delivery modules for AI XPUs | $0.30B | $3.0B | 78% | 70% | 36% | 5/3/3/4/2/2/2 | 16 | 26 | fails: non-growth < 18 |
| — | L45 | New-build NA/EU sintered NdFeB magnets | $0.16B | $1.1B | 62% | 56% | 28% | 5/3/2/4/2/2/3 | 16 | 26 | fails: non-growth < 18 |
| — | L31 | Expendable small turbojets (<=400 lbf) | $0.32B | $0.95B | 31% | 27% | 24% | 4/3/2/4/3/2/3 | 17 | 25 | fails: non-growth < 18 |

*Per-scorer scores and rationales are in [`data/deep_dive_phase4_scores.csv`](data/deep_dive_phase4_scores.csv). "—" means the niche failed the gate (listed, not ranked). Deep dives for #11–#14 and the four gate-fails are in [Appendix A](appendix-a-other-deep-dives.md).*

### 3.4 Near misses and challengers tested

A separate challenger agent tried to break the top 10. It tested niches outside the deep-dive set against the weakest deep-dived niches.

**Promoted to deep dives:**
- **US 765 kV transformers and reactors.** Ranked #7 in the end.
- **OSAT CoWoS-class packaging.** Finished at #12, with a ~24% probability-weighted CAGR: growth is front-loaded into 2027, and TSMC could pull the work back in-house.

**Rejected:**

| Niche | Verdict |
|---|---|
| 200G/lane active electrical cables | Lane-rate migration inside an AEC market growing ~18–25% |
| Large-body (≥120 mm) ABF substrates | An arbitrary slice of a ~18–25% parent, with a 2027–29 capacity overhang |
| Ultra-high-capacitance MLCCs | ~20%, with a shortage-priced base |
| Broadband direct-to-device satellite service | Sub-floor in 2026; the largest pool sits inside private SpaceX |
| Ex-China NdPr metal | Thin, mostly captive value-add |
| SOFC for data centers | ~29% probability-weighted; single-vendor and substitution risk |
| FEOC-compliant LFP storage cells | ~26%, with a policy premium that compresses |
| Pulsed-field ablation | ~12–18%; the conversion was largely done by 2026 |
| Radiopharmaceutical isotopes | No $1B path by 2030 |
| Renal denervation | Watchlist; base at the floor |
| Hybrid-bonding equipment | Lumpy and slipping |
| Quartz glass cloth | Still in qualification |
| Western nuclear-island forgings | Binary on 2026–27 long-lead orders |
| Next-wave peptide API | ~22% |
| Robotaxi ride-hail | Excluded on depth: an end-consumer service, not a layer several levels down a value chain. On growth alone (~50–90%) it would rank high. |

---

## 4. Deep dives: top 10

Every deep dive follows the same template:
- definition
- value-chain path
- market size and math (top-down and bottom-up)
- demand drivers and catalysts
- supply side
- key companies with pure-play exposure
- bear case
- leading indicators
- confidence and biggest unknown
- sources

"The draft", "the fact-check" and "the bear case" refer to the independent analyst passes behind each deep dive (Section 3.3). Where they disagreed without decisive evidence, the ranges were widened.

### 4.1 — #1 · Merchant HBM logic base dies (foundry-made HBM4/4E/5 base dies, incl. custom cHBM)
*Megatrend: AI accelerators -> HBM bandwidth and custom memory | 2026 -> 2030 revenue: $0.3-1.1B -> $4-14B | CAGR: 61-120% (central ~88%; 2027-30 only ~33%) | Growth mix: ~83% volume / ~17% price | Confidence: medium*

**Definition.**

In: revenue that external foundries book at first sale for the bottom logic/interface die of HBM4, HBM4E and HBM5 stacks built on a logic process.
- Processes: TSMC N12FFC+, N5/N6, N3P/N3, later N2/A16; Intel 3/18A if it qualifies.
- Delivered as wafers or known-good dies (KGD), with the foundry doing the TSV via-middle, bumping and KGD test.
- Buyers: SK hynix (HBM4, 2026), Micron (HBM4E, 2027), and accelerator designers that consign their own die (Nvidia, reported; hyperscaler cHBM). Customer-designed dies for Samsung stacks count if TSMC makes them.
- Also in: NRE specific to the base die.

Out:
- Samsung's captive SF4/SF2 dies (sized only as the parent).
- Base dies made on a DRAM process: HBM3E and earlier, Micron's HBM4, CXMT.
- SMIC-made dies for Huawei (closed loop).
- DRAM core dies, stacking and KGSD test.
- Interposers, bridges and CoWoS.
- Host-side controller/PHY IP.
- Design-house turnkey resale of TSMC wafers (that would double count).
- The HBM stack itself.

This niche is a slice inside HBM value, so never add it to HBM-stack niches. No company discloses it; it sits inside TSMC's HPC line.

**Value-chain path.** AI accelerators (Nvidia Rubin/Rubin Ultra/Feynman, AMD MI450, Google TPU, AWS Trainium) -> CoWoS/EMIB package -> HBM4/4E/5 stack (SK hynix, Samsung, Micron) -> logic base die (2048-bit PHY, TSV landing, DFT, power delivery; from HBM4E optionally the memory controller and custom logic) -> **foundry-made base-die wafer/KGD**

**Drill-down decision.** I narrowed from all logic-process base dies (the parent, which includes Samsung's captive dies) to the merchant slice.
- It grows faster: ~88% vs ~74% central.
- It is the only slice priced at arm's length.

I rejected a custom-only cHBM slice:
- Its 2026 base (~$0.02-0.1B [E]) is below the size floor.
- Its CAGR (>150%) says little.
- Standard and custom dies are converging onto the same TSMC N3 wafers.

Parent for reference: $0.7-2.1B in 2026 (central $1.2B) -> $6-19B in 2030 (central $11B). (11/1.2)^0.25-1 = 74%, band 50-100% [E].

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $0.3-1.1B [E] | $4-14B [E] | 61-120% = (4/0.6)^0.25-1 to (14/0.6)^0.25-1; full corners 38% (4/1.1) to 161% (14/0.3) |
| Central | ~$0.6B | ~$7.5B | (7.5/0.6)^0.25-1 = 88% |
| Bear (~25%) | ~$0.6B | $1.5-3.5B (central $2.3B) | 26-55%, central 40% |
| Memo: 2027 bridge | 2027 $1.8-5.5B, central $3.2B [E] | | 2027-30: (7.5/3.2)^(1/3)-1 = 33% (plausible 25-55%) |

The band uses the central 2026 base because a die-price error would hit both years in the same direction. About 66% of the 2026-30 log growth (ln5.33/ln12.5) comes in the single 2026-27 step.

- **Volume vs price:**
  - Central dies grow 20M -> 169M (8.45x) and blended ASP $29 -> $45 (1.55x). Log split: 2.13/2.57, so ~83% volume and ~17% price [E].
  - About 70% of the unit growth (ln4.5/ln8.45) is a one-time sourcing shift. Merchant share of all HBM base dies rises from ~15% to ~67% as Micron and all of SK hynix move to foundry dies. Total HBM base dies grow only ~1.85x [E].
  - ASP: ~70-80% comes from node mix and customer-designed dies (durable); ~20-30% comes from TSMC list-price hikes of 3-10% a year [3P] (less durable).
  - TrendForce's +121% 2027 blended HBM ASP [3P] is driven by mix and does not pass through to base dies.
  - The real price risk is in the 2026 base: $29 per die is 2-3x pure wafer economics. At $15-20 per die, the 2026 base falls ~35% [E].
- **Top-down, 2026:**
  1. HBM bits: 3.75-4.5 EB. TrendForce's >30bn Gb is 3.75 EB [3P][STALE 2025-05], revised up since. The draft's "+77%" on top was a double count.
  2. Divided by 30-36 GB per stack: 105-150M stacks.
  3. Times 20-33% HBM4: 21-50M. A Rubin/MI450 demand check (16-31M+) trims this to ~21-37M [E].
  4. Times SK hynix's 45-60% of HBM4 (TrendForce >50%, Counterpoint 54% [3P]): 10-22M stacks.
  5. Times 1.2-1.6 dies per shipped stack: yield 1.1-1.2 x wafer lead 1.05-1.35, because TSMC bills 4-6 months ahead of a 2027 ramp that is ~4-5x 2026. Result: 12-35M dies, central 20M.
  6. Times $18-45 per die. Basis: Herald's 3-4x a core die [3P] at $6-10 [E], capped by Business Post's ≤20% of HBM4 cost [3P][STALE 2025]. Corners $0.22-1.6B.
  7. Central: 20M x $29 = $0.58B, plus $0.02-0.08B NRE, ≈ $0.6B.
  8. Cross-check: 10-22M stacks x $500-600 (mid-$500s [3P]) = $5-13B of SK hynix HBM4 revenue. At ~$39 per stack (~7%), the base die is worth $0.35-0.9B.
- **Top-down, 2030:**
  1. HBM bits: 10-20 EB, central 14 [E].
  2. Divided by 48-72 GB per stack: ~160-320M stacks, central 241M.
  3. Times 92-98% logic base die and 1.05-1.15 dies per stack: 155-360M dies, central 252M.
  4. Times 55-80% external (SK hynix 40-55%, Micron 15-25%, customer dies on Samsung stacks 0-10%): 85-290M dies, central 169M.
  5. Times $32-64 per die. The central $45 blends 60% N3-class at ~$55 with 40% N12/N6/N5 at ~$30. Corners $2.7-18.6B.
  6. Central: $7.6B, plus $0.2-0.5B NRE [E].
- **Bottom-up, 2026:**
  - 12-20M SK hynix HBM4 stacks x 1.35, divided by ~450 good dies per N12 wafer (110-125 mm² die; area unverified), gives 36-60k wafers (3-5k wpm on average).
  - At $9-16k per wafer including TSV, bumps and KGD: $0.32-0.96B. Central: 45k x ~$12.75k = $0.57B, plus NRE, ≈ $0.6B [E].
  - Commodity wafer economics ($6.5-10k) would give only ~$0.25-0.5B. That is why the low end stays at $0.3B.
- **Bottom-up, 2030:**
  - 169M dies ÷ ~440 per wafer = 384k wafers, ≈ 32k wpm.
  - N3: 19k wpm x 12 x $24k = $5.5B. Basis: N3 ~$19.5k in Jun-2026 [3P], plus 2026-29 hikes [3P], plus TSV/KGD [E].
  - Mature nodes: 13k wpm x 12 x $13k = $2.0B.
  - Plus $0.3B NRE ≈ $7.8B. A 16-55k wpm range gives $3-17B.
  - Capacity check: 10-40k wpm of N3 is ≈ 4-17% of an assumed 220-250k wpm N3 family by 2028. KGI expects N3 capacity +40-45% by end-2028 [3P]; the starting level is my assumption [E].
- **Reconciliation:**
  - 2026: both methods give ~$0.6B, but they share the same unverified die price.
  - 2030: both methods give $7.6-7.8B including NRE. I use $7.5B, rounded down for the bear skew.
  - The fact-check, which has evidence, overrides the draft's $9B. The draft assumed 65-80% N3 (reporting says 12nm for mainstream, 3nm for premium), 380-420 dies per wafer (vs 440-470), and a custom premium on top of NRE (a double count).
  - The bear analyst's probability-weighted CAGR of ~75-85% (≈$5.6-7.0B on $0.6B [E]) is below the base-case central. I flag that skew rather than netting it.

#### Demand drivers and catalysts
- **Architecture lock-in (permanent from HBM4).** HBM4 I/O above 10 Gbps needs a logic-node base die. TSMC N12 cuts voltage from 1.1 V to 0.8 V [R].
- **SK hynix HBM4 ramp on TSMC N12FFC+ into Rubin (2H26, in progress).**
  - SK hynix says mass-production shipments began in Q2-26 [G].
  - TrendForce says it slipped to 3Q26 and full-year volume was cut [3P]. Volume is reportedly 20-30% below plan [3P].
- **Micron HBM4E on TSMC base dies (2027 ramp) [G].** This covers both standard and custom "NVHBM" with Nvidia. About 75% of FY27 is committed [G]. The "26 agreements / ~35% through 2030" figure is unverified.
- **SK hynix HBM4E node split (1H27 to 2028; reported, unconfirmed).** Standard dies for Nvidia on 12nm in 1H27; 3nm for premium Nvidia/TPU parts in 2H27-28 [3P].
- **Custom dies on N3 (2025 to ~2028).**
  - TSMC disclosed C-HBM4E on N3P with an integrated controller in Dec-2025 [R].
  - Nvidia's own 3nm base die: trial production 2H27 [3P, undated].
  - Feynman cHBM ~2028, on the GTC 2026 roadmap [R].
- **TSMC N3 capacity and pricing (2027-29).** TSMC names HBM base dies among its N3 adds; the Tainan 3nm fab reaches volume in 1H27 [G, via KGI/VectorShift]. Price hikes run 2026-29 [3P].
- **Intel as second source (decision 2027; volume 2028+ at the earliest).** Reported; SK hynix disputes parts of the report.

#### Supply side
- **Suppliers and shares:**
  - TSMC: ~100% of merchant in 2026, 85-100% in 2030. Intel: 0-15% [E].
  - Parent: Samsung's captive dies are ~50% of 2026 value ($0.6B of $1.2B) and 20-45% of 2030 dies [E]. The fact-check uses 20-35%, the bear case 40-45%.
  - Q2-26 HBM revenue shares: SK hynix 50%, Samsung 33%, Micron 18% (Counterpoint [3P]). The draft's 38% for Samsung was its DRAM share.
- **Capacity and lead times:**
  - TSMC base-die load: ~3-5k wpm of N12 in 2026, rising to 16-55k wpm by 2030 (central 32k: 19k N3 + 13k mature) [E].
  - Samsung reportedly put >50% of ~30k wpm of Pyeongtaek 4nm on base dies, >15k wafers in Aug-26 (Hankyung; DigiTimes via Guru3D [3P, secondary]). That implies ~80M dies a year against ~11-16M HBM4 stacks, so it is not used for sizing.
  - Cycle time is ~2 months on N12 and ~3-3.5 on N3, plus 1-2 months of stacking and test. Wafer starts therefore lead stack shipments by 4-6 months [E].
- **Qualification barriers:**
  - The base die is qualified as part of each stack at each GPU/ASIC customer (~6-12 months).
  - Changing foundry means a PHY/TSV redesign and requalification, so sourcing is locked per generation [E].
  - A custom N3 die adds tens of $M of NRE and three-way co-design [E].
- **Geographic concentration:**
  - Merchant: ~100% Taiwan in 2026 and >85% in 2030, unless Intel (US/Ireland) or TSMC Arizona N3 wins share.
  - Parent: ~50/50 Taiwan/Korea [E].
  - Every non-Samsung HBM4 supplier depends on one Taiwan foundry.

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| TSMC | 2330 TWSE / TSM NYSE | Sole merchant foundry: N12FFC+ for HBM4, N3P C-HBM4E, custom dies | ~0.2-0.6% in 2026 ($0.3-1.1B vs ~$165-175B; that revenue base is not verified); ~1-3% by 2030 [E] |
| Samsung Electronics | 005930 KRX | Captive SF4/SF2 base dies; the main threat to the merchant pool | 0% merchant; captive transfer value ~0.1-0.5% [E, unverified] |
| Intel Foundry | INTC NASDAQ | Possible SK hynix HBM4E second source (Intel 3/18A) | 0% (option value) |
| SK hynix | 000660 KRX | Largest buyer; designs the standard die, picks the node | 0% (cost item; ≤20% of HBM4 cost [3P][STALE 2025]) |
| Micron | MU NASDAQ | Buyer from HBM4E (2027): standard dies plus NVHBM | 0% |
| Nvidia | NVDA NASDAQ | Demand anchor; own 3nm base die (reported) | 0% |
| Global Unichip (GUC) | 3443 TWSE | HBM PHY IP and cHBM design (only NRE is in scope) | Unverified; low single digits [E] |
| Alchip | 3661 TWSE | Possible cHBM design partner (no win verified) | Unverified; 0-3% [E] |
| Marvell / Broadcom / MediaTek | MRVL, AVGO NASDAQ / 2454 TWSE | XPU partners that specify custom base-die logic | <1% (unverified) |
| Synopsys / Cadence | SNPS / CDNS NASDAQ | HBM4/4E IP and EDA (adjacent; host-side IP is OUT) | <1% |

#### Bear case and key risks
- **Technology substitution:** The base die does not disappear. The question is whose fab makes it and on which node.
  1. **Captive Samsung.** Samsung was first to validate and ship HBM4 and targets 2x shipments in 2027 [3P]. UBS has Samsung at 41% of 2027 HBM bits, vs SK hynix 39% and Micron 20% [3P]. Samsung pitches turnkey custom HBM4E and is studying 2nm base dies [3P]. The bear case keeps Samsung at 40-45% of dies through 2030, leaving 55-60% external.
  2. **Node substitution (most likely bear leg, 50-60% [E]).** SK hynix uses 12nm for mainstream dies and 3nm only for premium ones; Nvidia's first HBM4E is on 12nm. There is precedent: KED reported in 2024 that HBM4 would be on TSMC 3nm in 2025 [STALE 2024-12], and it shipped on N12. The bear case has N3 at 30-45% of dies and a blended ASP of $28-38. This leg alone takes the central to ~$6.5B (~82% CAGR).
  3. **Price-capping second sources.** Intel could take 0-15% from 2028. Micron could re-insource standard HBM4E (10-15% probability [E]).
  4. **Substitutes for HBM bits.** GDDR7 (Rubin CPX reports conflict), LPDDR5X/SOCAMM, SRAM-based decode, HBF and SoIC DRAM-on-logic could absorb 10-20% of incremental AI memory bits. That would leave stacks 10-15% below the base path [E].
  5. **Stack mix.** The shortage-driven move to 8-hi stacks reverses, and 16-hi stacks at 64-96 GB need fewer dies per bit.
- **Capex cuts:**
  - Goldman sees hyperscaler capex growth slowing from ~100% (2026) to 54% (2027) and 12% (2028, ~$1.4T), with ~1/3 of 2027 AI capex debt-funded [3P]. The 2027 consensus is ~$1.1-1.3T [3P].
  - The bear case [E]:
    - 2028 AI capex falls 20-30% to $0.85-0.95T, and HBM stacks are flat to -15%.
    - TSMC base-die starts fall 30-50% for 2-3 quarters, visible in 2H27-1H28, before memory revenue turns.
    - Recovery runs at 15-25% a year, for 7-9 EB of bits in 2030.
  - Program cuts: pushing Nvidia's custom HBM4E to Feynman, or cutting one hyperscaler ASIC, removes $0.3-1B of 2030 revenue [E]. Rubin Ultra HBM has already been cut from 1TB to 768GB [3P].
- **Chinese capacity:** This is the weakest leg.
  - CXMT's HBM3 is on a 16nm DRAM process, its mass production is slipping, and HBM3E is not expected before 2027 [3P].
  - Huawei's HBM is a closed loop. No Chinese base die is qualified at Nvidia, AMD or US hyperscalers, and US controls apply [STALE 2024-12].
  - Direct impact: <2% of 2030 revenue [E]. The indirect channel, commodity DRAM pushing HBM into oversupply in 2028, hits stack prices more than base-die units.
- **Double-ordering / pull-forward:**
  - Micron says purchase intentions are ~150% of committable supply [G]. Micron's HBM capacity is reportedly heading to ~100k wpm [3P], Samsung plans 2x, and Samsung's own planners flag a reversal around 2028 [3P].
  - Base dies are bought 4-6 months early and banked as KGD. TSMC bookings can therefore overshoot in 2027 and correct first in 2028.
  - Memory long-term agreements are generally not take-or-pay. This is the bear analyst's own knowledge, not re-verified.
  - Bear effect [E]: 2027 inflated 15-30%; 2028 down 10-30% YoY; the 2030 endpoint 10-20% lower.
  - The bear analyst reads Samsung's SF4 wafer starts vs its stack needs as captive inventory already building. The fact-check finds the wafer figure too large (5-7x need) to be inventory alone.
- **Already priced in?**
  - The story is consensus: Korean and Taiwanese press cover it weekly, and TSMC named base dies on its Q1-26 call.
  - There is no pure play; the niche is <1% of TSMC.
  - Prices from IBKR, 2026-10-14 [R]:
    - TSM $423: +40% YTD, 13% below its $487 high, -5% on the day before Q3 results.
    - GUC TWD 8,245: +288% YTD, 5.8x its 52-week low.
    - Alchip: +13% YTD, -30% from its 26-week high.
    - SK hynix KRW 1.30M: -56% from its ~KRW 2.99M June peak, +100% YTD.
    - Micron $891: -29% from ~$1,255, +212% YTD.
  - The market is already debating 2028. The cause of the October drawdown is unverified.
- **Bear-case numbers:**
  - 2030 merchant: $1.5-3.5B, central $2.3B [E]. Build: 7-9 EB ÷ 64-80 GB = 90-140M stacks (central 110M), x 1.05 dies per stack, x 55-60% external = 50-85M dies (central 66M), x $28-38 per die (central $33) = $2.2B, plus $0.1-0.2B NRE.
  - CAGR on the $0.6B base: 26-55%, central 40% ((2.3/0.6)^0.25-1). The bear analyst's own figure is 46% on a $0.5B base. If the 2026 base is $0.9-1.1B, the bear CAGR is ~20-26%.
  - Mix: ~85-90% volume.
  - Probability ~25%. A deep bear ($1.0-1.5B; ~14-26% CAGR) has ~10%. Parent in the bear case: ~$3.8B (33% CAGR on $1.2B).
  - **First warning sign:** SK hynix's 2027 HBM4E node split, due on the Q3-26 call (late Oct) and the Q4-26 call (late Jan 2027). If standard HBM4E stays on 12nm and N3 is limited to Nvidia/Google custom parts, the ASP leg fails.
  - Volume trigger: 2028 HBM contract talks in 2Q-3Q27.
  - Already flashing: memory equities are 29-56% off their June peaks.

#### Leading indicators to watch (next 2-4 quarters)
1. TSMC Q3-26 call (mid-Oct 2026) and Jan-2027 guidance: is the HBM base die still named among N3 adds? Also the Tainan 3nm schedule, and 2027 price hikes (sub-3nm +3-10%, 12/16nm up to +10%).
2. SK hynix Q3-26 (late Oct) and Q4-26 (late Jan 2027) calls: HBM4 share of 2H26 shipments, the 2027 HBM4E 12nm vs 3nm split, and Intel's status.
3. Micron FQ1-27 (Dec 2026): HBM4E/NVHBM qualification and ramp timing; FY28 commitments vs FY27's ~75%.
4. Wafer trackers (DigiTimes, Hankyung, The Elec, MoneyDJ): Samsung's SF4 base-die wafers vs its stack output, and TSMC N3 base-die tape-outs for SK hynix, Micron and Nvidia.
5. 2028 HBM contract pricing and hyperscaler 2027-28 capex guides (2Q-3Q27): any price decline would cut base-die wafer starts 4-6 months ahead of stack shipments.
6. Nvidia GTC (Mar 2027) and TrendForce: Rubin Ultra stack count and height, the share of custom HBM4E in 2H27-28, and 12-hi vs 8-hi.

#### Confidence and biggest unknown
Confidence is medium.
- **Direction: high.** Micron's move to TSMC and SK hynix's all-logic HBM4E are company-guided.
- **Level: low.** No company discloses a base-die price. The $29 central 2026 die is 2-3x commodity wafer economics. If pricing normalizes to $15-20, the 2026 base falls ~35% and mature-node pricing in 2030 falls with it.
- **Second-order unknowns:** the 2030 N3 share (45-80%) and Samsung's captive share (20-45%).
- **Ranking caveat:** the 88% figure overstates durability. It is a ramp-year effect; on a 2027 base the niche grows ~33% a year, and most of its unit growth is a sourcing decision that could partly reverse.

#### Sources
- TrendForce, "TSMC unveils custom C-HBM4E details: N3P logic dies reportedly target 2x efficiency gain", 2025-12-01. https://www.trendforce.com/news/2025/12/01/news-tsmc-unveils-custom-c-hbm4e-details-n3p-logic-dies-reportedly-target-2x-efficiency-gain/
- TrendForce, "Samsung reportedly targets HBM4 price parity with SK hynix", 2025-11-27. https://www.trendforce.com/news/2025/11/27/news-samsung-reportedly-targets-hbm4-price-parity-with-sk-hynix-amid-strong-nvidia-demand/
- TrendForce citing Business Post, TSMC logic dies up to 20% of HBM4 cost, 2025 [STALE 2025]. https://www.trendforce.com/news/?p=44664
- TrendForce citing Herald Business, "SK hynix reportedly weighs Intel for HBM4E base dies", 2026-08-31. https://trendforce.com/news/2026/08/31/news-sk-hynix-reportedly-weighs-intel-for-hbm4e-base-dies-amid-tsmc-cost-pressure-and-supply-diversification
- TrendForce citing Chosun/Korea Financial Times, "SK hynix reportedly weighs TSMC 3nm for HBM4E logic dies", 2026-03-20. https://www.trendforce.com/news/2026/03/20/news-sk-hynix-reportedly-weighs-tsmc-3nm-for-hbm4e-logic-dies-to-gain-edge-over-samsung/
- eDaily, SK hynix prioritizing TSMC 3nm for HBM4E base dies, 2026-06-04. https://en.edaily.co.kr/news/eda202606045605
- eDaily citing Counterpoint, Q2-26 HBM revenue shares, 2026-09-03. https://en.edaily.co.kr/news/eda202609035608/
- Fintool citing Counterpoint/UBS, Samsung HBM4 and Nvidia Vera Rubin, 2026. https://fintool.com/news/samsung-hbm4-nvidia-vera-rubin
- TrendForce, Nvidia reportedly developing its own 3nm HBM base die, 2026 (date unverified). https://www.trendforce.com/news/?p=54621
- Tiger Brokers citing TrendForce, Nvidia standard HBM4E on 12nm then custom, 2026. https://www.itiger.com/news/1139547270
- TrendForce, Micron EVP Bhatia: TSMC to make HBM4E logic dies, 2026-05. https://www.trendforce.com/news/?p=58045
- TrendForce, Micron kept DRAM process for HBM4 base die, 2026. https://www.trendforce.com/news/?p=54870
- Webull, Micron Q4 FY2026 earnings call transcript, 2026-09. https://www.webull.com/news/15672802111996928
- Guru3D citing DigiTimes, "Samsung pivots 4nm fabrication capacity to meet AI memory demand", 2026-03 to 2026-08. https://www.guru3d.com/story/samsung-pivots-4nm-fabrication-capacity-to-meet-explosive-ai-memory-demand/
- Asia Economy, SK hynix Q2-26 conference call, 2026-07-29. https://view.asiae.co.kr/en/article/2026072909405874785
- TrendForce, HBM Market Bulletin, 2026-06-23. https://www.trendforce.com/research/download/RP260623IP3
- TrendForce, 2027 HBM ASP forecast +121%, 2026-09-29. https://www.trendforce.com/presscenter/news/20260929-13255.html
- Silicon Analysts, "TrendForce lifts 2027 HBM ASP forecast to 121%; HBM4 stack seen doubling to $1,300", 2026-10-01. https://siliconanalysts.com/market/trendforce-lifts-2027-hbm-asp-forecast-to-121-hbm4-stack-seen-doubling-to-1-300-2026-10-01
- EE Times Japan, TrendForce briefing (HBM 2.2x, 8-hi substitution), 2026-09-30. https://eetimes.itmedia.co.jp/ee/spv/2609/30/news066.html
- VectorShift, TSMC Q1-26 earnings summary, 2026-04-16. https://vectorshift.ai/research/companies/taiwan-semiconductor-manufacturing-co/earnings/2026-q1-summary
- KGI, TSMC (2330 TT) 1Q26 note, 2026-04-16. https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/tsmc_2330-tt_16042026e.pdf
- MarketBeat, TSMC Q2 earnings call highlights, 2026-07-16 (figures unverified). https://www.marketbeat.com/instant-alerts/taiwan-semiconductor-manufacturing-q2-earnings-call-highlights-2026-07-16/
- Silicon Analysts, TSMC 3nm wafer cost guide, 2026-06. https://siliconanalysts.com/guide/tsmc-3nm-cost
- TrendForce, TSMC to raise sub-3nm prices 3-10% in 2026, hikes through 2029, 2025-12-29. https://www.trendforce.com/news/2025/12/29/news-tsmc-reportedly-to-raise-sub-3nm-prices-3-10-in-2026-plans-hikes-through-2029/
- SK hynix Newsroom, 2026 Market Outlook, 2026-01. https://news.skhynix.com/en/2026-market-outlook-focus-on-the-hbm-led-memory-supercycle/
- TrendForce, 2026 HBM shipments to surpass 30 billion Gb, 2025-05-22 [STALE 2025-05]. https://www.trendforce.com/presscenter/news/20250522-12589.html
- heise online, Nvidia GTC 2026 roadmap (Feynman custom HBM), 2026-03. https://heise.de/-11214678
- Herald Business, Micron FQ3-26 HBM4 >$1B, 2026-06. https://biz.heraldcorp.com/article/10787653
- AnandTech, "TSMC readies HBM4 base dies at 12nm and 5nm", 2024-05 [STALE 2024-05]. https://ns2.anandtech.com/print/21395/tsmc-readies-hbm4-base-dies-at-12nm-and-5nm
- Korea Economic Daily, SK hynix HBM4 on TSMC 3nm plan, 2024-12 [STALE 2024-12]. https://www.kedglobal.com/newsView/ked202412030008
- Money Today, Samsung considering 2nm for HBM base dies, 2026-03-11. https://www.mt.co.kr/industry/2026/03/11/2026031115332916636
- Korea Herald, UBS 2027 HBM bit-share projection, 2026. https://www.koreaherald.com/article/10828143
- WallStreetCN (UBS note), Rubin Ultra HBM reduced to 768GB, 2026-08. https://wallstreetcn.com/articles/3772171
- SemiAnalysis, Rubin CPX with GDDR7, 2025-09 [STALE 2025-09]. https://newsletter.semianalysis.com/p/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack
- HWBusters citing Ming-Chi Kuo, Rubin CPX with HBM4, 2026. https://hwbusters.com/?p=113027
- Tiger Brokers citing Goldman Sachs, hyperscaler capex path, 2026. https://www.itiger.com/news/1153929987
- PYMNTS, Goldman ~$1.2T 2027 AI infrastructure, 2026. https://www.pymnts.com/?p=4233514
- DatacenterDynamics, Moody's hyperscaler capex near $1T by 2027, 2026. https://datacenterdynamics.com/en/news/moodys-hyperscaler-capex-forecasts-marked-up-by-85bn-to-close-in-on-1trn-by-2027/
- Tiger Brokers, Micron purchase intentions ~150% of supply, 2026. https://www.itiger.com/news/1130673417
- Newsquawk citing Economic Times, Micron HBM capacity to ~100k wpm, 2026. https://www.newsquawk.com/headlines/micron-mu-plans-to-roughly-double-its-hbm-production-capacity-to-about-100000-wafers-per-month-by-year-end-et-reports
- Igor'sLAB, Samsung and SK hynix slowing DRAM expansion, 2026-03. https://www.igorslab.de/en/samsung-and-sk-hynix-are-slowing-down-their-dram-expansion-because-no-one-wants-to-voluntarily-contribute-to-the-next-round-of-overcapacity/
- Blocks & Files, "The memory supercycle", 2026-01-21. https://blocksandfiles.com/2026/01/21/the-memory-supercycle/
- MTN, CXMT HBM3 schedule slipping, 2026-04-22. https://news.mtn.co.kr/news-detail/2026042208471824398
- Financial News, CXMT HBM3E not before 2027, 2026-07-27. https://en.fnnews.com/news/202607271815265658
- DigiTimes, CXMT 16nm HBM3 samples to Huawei, 2025-10-23. https://www.digitimes.com/news/a20251023PD208.html
- TrendForce, Ascend 950PR launch, 2026-03. https://www.trendforce.com/news/?p=54956
- Interactive Brokers, price snapshots (TSM, 000660, MU, 3443, 3661), 2026-10-14. n/a (IBKR MCP data; no public URL)


---

### 4.2 — #2 · Ultra-high-power 1310 nm InP CW-DFB laser chips and external-laser-source (ELS/ELSFP) modules for CPO/NPO
*Megatrend: AI data-center optical interconnect (co-packaged and near-packaged optics) | 2026 -> 2030 revenue: $0.11-0.30B -> $1.0-4.5B | CAGR: 35-153% envelope (central ~86%) | Growth mix: ~110% volume / ~-10% price-mix | Confidence: low on 2030 magnitude (medium on 2026 base and direction)*

**Definition.** In: InP buried-heterostructure CW-DFB chips at ~1310 nm with ~200-400+ mW per emitter at >=55C, qualified as external light sources for SiPh engines (Lumentum UHP; Coherent 400 mW; Sumitomo, Furukawa, Yuanjie 300/400 mW parts); ELS modules (OIF ELSFP 8/16-channel, Nvidia ELS with 8 emitters, laser shelves/NICs); discrete UHP chips sold into NPO or XPU optical-I/O engines. Revenue counted once: modules plus merchant bare chips sold outside modules. Out: mid-power (<=~150 mW) CW in pluggables or inside NPO modules; EML/DML/VCSEL; InP substrates/epi (L04); engines, FAU, fiber (L05); WDM/comb arrays, heterogeneous or quantum-dot on-PIC lasers and Lightmatter VLSP (substitution risk, not niche revenue).

**Value-chain path.** AI data centers -> scale-out CPO switches (Nvidia Spectrum-X/Quantum-X Photonics, Broadcom TH6-Davisson), then XPU optical scale-up from ~2028 -> SiPh CPO/NPO optical engines -> external light source -> ELS module assembly -> **UHP CW-DFB chips and ELS modules** -> [upstream: InP substrates/epi, L04]

**Drill-down decision.** Kept at chips plus modules, measured at the highest packaged layer. Rejected: (a) ELSFP modules only: Cignal's >$100M -> >$1.5B [3P] = 15^0.25-1 = ~97%, no faster, and crowded assembly leaves pricing power with the chip; (b) scale-up light sources only: 2026 base ~$0-20M [E], below the floor, same chips (an application split); (c) 400 mW chips: same population. Caveat: vendor "UHP" revenue may include high-power CW sold into pluggables (out of scope).

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) [E] | $0.11-0.30B | $1.0-4.5B | 35-153% (envelope) |
| Central [E] | ~$0.19B | ~$2.3B | ~86% |
| Probability-weighted, incl. 30% bear case [E] | ~$0.19B | ~$1.8B | ~76% |
| Bear case [E] | ~$0.2B | $0.5-1.1B | 26-53% (central ~39%) |

**CAGR math:**
- Central: (2.3/0.19)^0.25-1 = 86%.
- Envelope: (1.0/0.30)^0.25-1 = 35% to (4.5/0.11)^0.25-1 = 153%.
- With 2026 at the bottom-up core ($0.15-0.22B): 46-134%.
- Probability-weighted 2030: 0.3 x 0.75 + 0.7 x 2.3 = $1.84B.

**Most of the headline is base effect.** The ramp starts in one quarter, CQ4-26.
- 2027-30, on a 2027 bridge of $0.7-1.7B (central $1.1B): (2.3/1.1)^(1/3)-1 = ~28% central, 13-38% range.
- From the CQ4-26 exit run-rate ($0.32-0.50B annualized [E]): 46-64%.

- **Volume vs price:**
  - 2026: ~3.5M emitters (including pipeline fill) x ~$54 blended (mostly chips) = $0.19B [E].
  - 2030: ~55M x ~$42 = $2.3B [E].
  - Volume rises 15.7x; revenue per emitter falls 22% (-6%/yr). Shares of log growth: ln15.7/ln12.1 = ~110% volume, ~-10% price/mix.
  - Like-for-like prices fall faster [E]: chips ~-15 to -20%/yr after 2027; ELS from $500-1,100 today (unverified: an expert call and a secondhand Citi figure) to ~$250-350.
  - Offsets: more full modules (2-2.5x chip content [G, Lumentum Feb-2026]) and 16-channel parts. Working the other way, 400G lanes on 400 mW emitters halve emitters per Tb/s.
  - Current prices are shortage prices (LTAs, prepayments). Underwrite volume, not ASP.
  - Bear case: volume ~134%, price ~-43%.
- **Top-down, 2026:**
  - Nvidia CPO switches: 10-20k 102.4T-equivalents [3P, secondhand: Foxconn via Economic Daily News >10k; GF 20k].
  - x 16-18 ELS each [R, Nvidia blog, STALE 2025] = 160-360k ELS. Add 20-60k for Broadcom, other OEMs and spares [E] = 180-420k ELS.
  - x 8 = 1.4-3.4M emitters. x pipeline fill 1.2-1.45 = 1.7-4.9M emitters.
  - x $40-65 = $0.07-0.32B. Central: 3.5M x $54 = $0.19B.
  - The quad-ASIC SN6800 uses 64 ELS, so "switch units" must be converted to 102.4T-equivalents.
- **Top-down, 2030:**
  - (A) CPO+NPO optics market $10-39B [3P: TrendForce >$39B; TechInsights ~$29.9B; low end unverified] x 8-14% light-source share [E] = $0.8-5.5B.
  - (B) Scale-out: Cignal's 30M ports [3P] x 0.8 Tb/s = 24M Tb/s. At 0.8-1.6 Tb/s per emitter that is 15-30M emitters, up to 40M [E].
  - (B) Scale-up: 2-5M optically connected XPUs x 28.8-57.6 Tb/s / 1.6 Tb/s per emitter x 50-90% discrete-UHP share = 18-162M run-rate. x a 25-50% calendar-2030 haircut = ~5-80M [E].
  - (B) Value: 23M x $45 = $1.0B; 55M x $42 = $2.3B; 120M x $35-37.5 = $4.2-4.5B.
- **Bottom-up** [E, built on guidance]:
  - **2026:** Lumentum $60-120M, Coherent $5-30M, Sumitomo $5-25M (unverified), Broadcom captive $3-15M, others $0-10M. Chips total $73-200M.
  - Plus net assembler value-add: 0.12-0.30M modules x $250-400 = $30-120M.
  - 2026 total $0.10-0.32B. Check: $73-200M / $30-60 per chip = 1.2-6.7M chips, which brackets the top-down.
  - **2027:** Lumentum $0.40-0.80B (GF's $427M [3P] sits at the low end), Coherent $0.15-0.40B, others $0.05-0.20B, module value-add $0.10-0.30B. Total $0.7-1.7B.
  - **2030** (demand-limited, net of double counting): Lumentum $0.5-1.6B, Coherent $0.25-1.2B, Japanese followers $0.1-0.5B, Chinese $0.05-0.4B, Broadcom captive and entrants $0.05-0.3B, assembler value-add $0.05-0.5B. Total $1.0-4.5B, central $2.3B.
- **Reconciliation:**
  - **2026.** Top-down ($0.07-0.32B) and bottom-up ($0.10-0.32B) overlap. Cignal's >$100M of modules [3P] and Lumentum's "meaningful revenue exiting CY2026" [G, 8-K] trim the low tail.
  - **2030: third-party bounds.**
    - Cignal >$1.5B for modules only. Cignal calls it "conservative", but it is a forecast, not a floor.
    - TrendForce >$39B x 8-12% = $3.1-4.7B. The share is my assumption; an unverified Taiwan BoM implies 11-23% today.
    - Yole $8.1B x 15-20% = $1.2-1.6B [STALE 2024].
  - **Conflicts.** LightCounting's >3M CPO ports by 2031 implies <$1B but is ~10x below Cignal and below 2026 switch counts (10-20k x 128-144 = 1.3-2.9M ports): unreconciled. Citi's 45M ELSFP in 2028 (= 360M emitters) is excluded as a likely mislabel.
  - **June-2026 delay view** (Morgan Stanley: 6-7M engines in 2027 vs 20-30M expected [3P]) is partly superseded by Nvidia's Aug-2026 full Spectrum-X CPO volume production and Foxconn's raised >50k 2026-27 outlook [3P, secondhand]; engine-yield risk keeps the low end wide.

#### Demand drivers and catalysts
- **Scale-out CPO**: each switch swaps 128-144 pluggables for 16-18 ELS [R]. Spectrum-X capacity expands 2H26 (TrendForce Jul-2026) [3P]. Status: ramping.
- **Lumentum CQ4-26** (reported ~Feb-2027): "meaningful revenue exiting CY2026" [G, 8-K]. Call summaries cite ~$50M/quarter and a first >=$100M quarter in Jan-Mar 2027, but neither figure is in the 8-K or deck: unverified.
- **Lumentum multi-hundred-million scale-out PO**: delivers 1H CY2027 [G, Feb-2026]. The first ELS module PO delivers by 2H CY2027 [G].
- **Coherent**: CPO revenue starts Oct-Dec 2026, with "absolutely no push-out" [G, Aug-12-2026]. InP capacity is to "more than double" again by end-CY2027 [G].
- **Merchant ELSFP**: USI/EugenLight mass production 1Q27 at the earliest; TFC and Lian-Jun in small volume; Furukawa 16-channel samples [R, Sep-2026].
- **OFC 2027 (Mar-2027)**: Lumentum's new long-term targets [G]; NPO light-source design wins (an AMD deal is unverified).
- **Optical scale-up, the swing factor**:
  - Citi: NPO in 2027, widespread in 2028; scale-up CPO in 2028-29 [3P].
  - Lumentum: scale-up laser ramp 2H CY2027 [G].
  - LightCounting: scale-up optics $33.9M in 2026 -> $10.6B in 2031 [3P].

#### Supply side
- **Suppliers and shares** [E]: Lumentum 45-60% in 2026-27, ~35-45% by 2030 (a secondhand ~90% figure is unverified); Coherent 15-25% and rising; Sumitomo 5-15% (unverified); Broadcom captive 5-15%; Furukawa 0-5%, rising to 5-10% by 2030; Chinese 2-10% (base) or 10-20% (bear).
- **Capacity and lead times**:
  - **Lumentum**: InP fully allocated; +40% expansion; Greensboro material early 2028; capex ~$125M/qtr [R, filings via IBKR]. Shipments >30% short of demand (Jul-2026) and orders booked to 2028 [G].
  - **Coherent**: June-quarter InP laser output +80% YoY [R]; 6-inch yields above 3-inch. Sherman 6-inch >5x [G, STALE 2025-09]. Nvidia $2B equity plus a multi-billion commitment [R].
  - **Furukawa**: >5x high-power DFB by 2028 [G, 2025-12, not re-verified]. Its ¥38B covers the whole optical-components segment.
  - **Yuanjie**: RMB4.268B park, ~late 2028 [3P].
  - **Net**: tight through 2027, then a 2028 capacity wave.
- **Qualification barriers**: high-current reliability at 55-70C, RIN <-145 dB/Hz, <200 kHz linewidth [G, STALE 2025-09], hot-swap field reliability; 12-24 months sample to volume [E], ~2 years fab to volume [3P, China Merchants]. No Chinese 300-400 mW part is verified as qualified at Nvidia or Broadcom.
- **Geographic concentration**: ~75-85% of 2026 chip output from Lumentum/Coherent fabs in Japan, the US, the UK and Sweden [E]; assembly in Southeast Asia, China and Taiwan; demand concentrated in Nvidia. Policy: FCC Covered List (Morgan Stanley, Oct-2026) [3P]; indium export controls (not re-verified).

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| Lumentum | LITE / Nasdaq | #1 merchant UHP chips; entering ELS modules | ~1-3% CY26 ($60-120M on ~$4.5B); ~6-15% CY27 [E] |
| Coherent | COHR / NYSE | #2 UHP (400 mW, 6-inch InP); integrated ELS | <1% CY26; ~3-8% CY27 [E] |
| Sumitomo Electric | 5802 / Tokyo | Nvidia CPO laser partner | <0.5% [E] |
| Furukawa Electric | 5801 / Tokyo | High-power DFB, 16-channel ELS | <0.5% [E] |
| Broadcom | AVGO / Nasdaq | CPO switches, captive lasers | ~0% |
| NVIDIA | NVDA / Nasdaq | Dominant customer; sets ELS form factor | 0% |
| Fabrinet | FN / NYSE | ELS and engine assembly | <1% [E] |
| TFC Optical | 300394 / Shenzhen | ELS, small batch | ~1-5% (unverified) |
| USI / EugenLight | 601231 / Shanghai | UHP ELSFP, mass production 1Q27 | <1% |
| Yuanjie | 688498 / Shanghai STAR | 300/400 mW in validation | ~0% |
| AAOI; OE Solutions; POET/Sivers | AAOI Nasdaq; 138080 KOSDAQ; POET Nasdaq / SIVE Stockholm | Entrants | ~0-2% (unverified) |
| Lightmatter | private | VLSP substitute | n/a |

#### Bear case and key risks
- **Technology substitution:** The bigger risk is delayed demand, not a better laser: roughly half of 2030 base-case emitters are scale-up, and Citi puts scale-up CPO at 2028-29 [3P]. Optical-I/O chiplets (Ayar Labs, Sivers, Xscape) use WDM arrays or combs [STALE 2023-24]; heterogeneous/quantum-dot lasers (Tower/Quintessent, Scintil, Innolume HiPER-CPO) are at PDK/R&D stage, ~2029-30; Lightmatter Guide claims 100 Tb/s in 1RU vs ~18 ELSFPs in 4RU [G]; NPO can use in-module 100-150 mW lasers. Bear [E]: substitutes take ~20-35% of addressable value (30-50% of scale-up, 5-10% of scale-out), and emitter-per-Tb/s deflation removes another 25-40% of units. No shipping CPO product has yet replaced the ELS.
- **Capex cuts:** The sell-side models deceleration [3P]: UBS has capex growth at 76%/25%/6% for 2026/27/28; BofA has group FCF at about -$144B (2027) and -$186B (2028). New architectures are deferred first, and the 2028 supply wave meets near-zero capex growth. Bear [E]: a 20-30% capex cut drops 2028 revenue 50-70% (from $0.6-1.2B to $0.25-0.5B) with ASP -25-40%, and 2030 recovers only to $0.5-0.9B. If scale-up stays on copper: 10-19M emitters x $22-35 = $0.2-0.7B.
- **Chinese capacity:** Yuanjie's UHP parts have no mass-production date; Everbright's chairman cannot rule out long-term price declines [G, Sep-30-2026]. China-domestic CPO (10-20% of 2030 ports) could go to Chinese vendors at 30-50% lower prices [E]. The key mechanism is indirect: as China takes pluggable CW from 2027, Western InP starts are freed for UHP, turning the 2028 wave into an ASP collapse. Bear Chinese value share: 10-20%.
- **Double-ordering / pull-forward:** LightCounting (Jul-2026) on double ordering: "this situation has never ended well" [3P]; vendor pools are widening from 2-3 to 5-7 suppliers [3P]. Bear math [E]: 2027 chip supply of $0.55-0.8B vs $0.26-0.65B of chip content in 1.3-1.8M ELS puts $0.1-0.4B into inventory; on Foxconn's figures (0.5-0.9M ELS) the gap is wider, partly a 2028 pre-build. Field-replaceable ELS lasers are not consumed by engine yield losses, so the excess accumulates. Shape risk: 2027-30 at -5% to +10% a year.
- **Already priced in?** Largely yes [R, IBKR prices]. LITE was $1,103 on Oct-9 vs $155.5 a year earlier, then $875-896 on Oct-14 (the 19-21% drop is unexplained; check it); at ~$875 it is ~25x FY28E EPS of ~$35 (derived from CMB's $1,230 target at 35x). COHR is 41% below its June high after falling ~24% in two weeks after its "no push-out" call. Yuanjie rose 7.6x with UHP parts still in validation, then hit limit-down on Oct-8. At least nine leveraged single-stock ETFs trade on LITE and COHR.
- **Bear-case numbers:**
  - 2030: $0.5-1.1B, central ~$0.75B (22M emitters x ~$30, plus ~$0.1B of NPO chips) [E]. A LightCounting-based cross-check gives $0.5-0.9B.
  - CAGR: 26-53%, central (0.75/0.2)^0.25-1 = 39%.
  - Probability: ~30% (25-35%), with a ~10% tail below $0.5B.
  - First warning sign (Nov-2026 calls): a push-out of the 1H27 PO, a CQ4 run-rate below ~$40M, Coherent's CPO start slipping, or management language moving from "supply-constrained" to "customer readiness".

#### Leading indicators to watch (next 2-4 quarters)
1. Lumentum FQ1 (Nov-2026) and FQ2 FY27 (Feb-2027): a first explicit CPO dollar figure, and timing of the 1H27 PO.
2. Coherent FQ1 FY27 (Nov-2026): CPO revenue booked in Oct-Dec, the InP doubling achieved, and the size of the Nvidia order.
3. The cause of the Oct-9 to Oct-14 drop in LITE and COHR.
4. Nvidia CPO switch tallies (in 102.4T-equivalents) against laser shipments. Lasers running at more than 2x deployments would confirm double-ordering.
5. Hyperscaler 2027 capex guidance.
6. USI/EugenLight mass production in 1Q27, and TFC and Browave volumes.
7. Second-source qualifications (Yuanjie, Furukawa), FCC Covered List action, and integrated-laser design wins at OFC 2027.

#### Confidence and biggest unknown
**Low** on the 2030 magnitude (specialist forecasts disagree >10x; no primary source discloses chip or ELS ASPs), **medium** on the 2026 base, **high** that the 2026-30 CAGR exceeds ~25% (the POs and Nvidia commitments are real). **Biggest unknown:** when optical scale-up arrives, how much is optical by 2028-30, and how many discrete UHP emitters each Tb/s needs; that swings 2030 between ~$1.0B and $4.5B. For ranking, read the ~86% headline alongside the ~28% central 2027-30 CAGR and the ~46-64% exit-run-rate CAGR.

#### Sources
- Lumentum, Q4 FY26 8-K Ex.99.1, 2026-08-11. https://www.sec.gov/Archives/edgar/data/0001633978/000162828026055726/lite_ex991xq4fy26.htm
- Yahoo Finance, "Lumentum (LITE) Q4 2026 earnings call", 2026-08-11. https://finance.yahoo.com/markets/stocks/articles/lumentum-lite-q4-2026-earnings-224414481.html
- Yahoo Finance, "Lumentum Holdings Inc Q4 2026" call summary, 2026-08. https://finance.yahoo.com/markets/stocks/articles/lumentum-holdings-inc-q4-2026-123000875.html
- Zacks, "Lumentum Q4 earnings call focuses on AI optics, OCS, NPO ramps", 2026-08-11. https://www.zacks.com/stock/news/2973530/lumentum-q4-earnings-call-focuses-on-ai-optics-ocs-npo-ramps
- AOL/Motley Fool, "Lumentum (LITE) Q2 2026 earnings call", 2026-02. https://www.aol.com/articles/lumentum-lite-q2-2026-earnings-234107096.html
- Nasdaq/Zacks, "CPO moving from hype to backlog: LITE more upside ahead", 2026. https://www.nasdaq.com/articles/cpo-moving-hype-backlog-lite-more-upside-ahead
- Eastmoney, Lumentum management remarks, 2026-05-06. https://finance.eastmoney.com/a/202605063728447146.html
- Lumentum, ELSFP reliability white paper (citing LightCounting), 2026-06. https://www.lumentum.com/sites/default/files/2026-06/elsfpreliability-wp-cl-ae.pdf
- Motley Fool, "Coherent (COHR) Q4 2026 earnings call transcript", 2026-08-12. https://www.fool.com/earnings/call-transcripts/2026/08/19/coherent-cohr-q4-2026-earnings-call-transcript/
- Futurum, "Coherent Q4 FY 2026 earnings", 2026-08. https://futurumgroup.com/insights/coherent-q4-fy-2026-earnings-1-6t-transceivers-ramp-cpo-revenue-approaches/
- Coherent, "Coherent samples low-noise 400mW CW lasers", 2025-09 [STALE 2025-09]. https://www.coherent.com/news/press-releases/coherent-samples-low-noise-400mw-cw-lasers
- Cignal AI, "ELSFP module market to exceed $1.5 billion by 2030", 2026-05. https://cignal.ai/2026/05/elsfp-module-market-to-exceed-1-5-billion-by-2030/
- TrendForce, CPO/NPO market press release, 2026-06-15. https://trendforce.com/presscenter/news/20260615-13098.html
- TrendForce, Nvidia Spectrum-X CPO shipments, 2026-07-27. https://www.trendforce.com/presscenter/news/20260727-13151.html
- TechNews, Morgan Stanley and SemiAnalysis on CPO, 2026-06-11. https://technews.tw/2026/06/11/ms-see-semianalysis-see-cpo/
- 10jqka, Nvidia CPO volume production, 2026-08-18. https://stock.10jqka.com.cn/20260818/c679027648.shtml
- 10jqka, Citi after Lightmatter meeting, 2026-09-09. https://stock.10jqka.com.cn/20260909/c679734186.shtml
- IThome, Foxconn CPO switch outlook (via Economic Daily News), 2026-05. https://www.ithome.com/0/949/743.htm
- X (@jukan05), GF Securities CPO switch estimates, 2026-02. https://x.com/jukan05/status/2021129556036645202
- MoneyWeekly, 1.6T CPO switch BoM, 2026. https://www.moneyweekly.com.tw/_Article?AID=236750
- NVIDIA developer blog, "Scaling AI factories with co-packaged optics", 2025 [STALE 2025]. https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/
- Xueqiu, Citi CPO report summary (figures excluded), 2026-03. https://xueqiu.com/5672579962/378159788
- Sina Finance, Coherent expert-call notes, 2026-08-05. https://finance.sina.com.cn/stock/stockzmt/2026-08-05/doc-inimhawf5216683.shtml
- Business Wire, "Lightmatter introduces Guide light engine", 2026-01-26. https://www.businesswire.com/news/home/20260126920594/en/Lightmatter-Introduces-Guide-Light-Engine-for-AI-Featuring-VLSP-Technology
- Optronics Media, Furukawa high-power DFB expansion, 2025-12-24. https://optronics-media.com/news/20251224/105994/
- UAnalyze, ELSFP supply chain, 2026-09. https://uanalyze.com.tw/articles/8331255940
- Gelonghui, Yuanjie broker notes, 2026-08/09. https://m.gelonghui.com/news/5303976
- Yicai, Everbright chairman on optical-chip pricing, 2026-09-30. https://www.yicai.com/news/103385708.html
- Eastmoney, Oct-8 optical sell-off on FCC Covered List report, 2026-10-08. https://finance.eastmoney.com/a/202610083889609065.html
- LightCounting, "July 2026 cloud data center optics", 2026-07. https://lightcounting.com/newsletter/en/july-2026-cloud-data-center-optics-385
- IEEE ComSoc Technology Blog, optical component shortages, 2026-08-14. https://techblog.comsoc.org/2026/08/14/impact-of-optical-component-shortages-bottlenecks-explained-hyperscalers-capex/
- TFTC, "AI capex cash-flow negative, 2027 peak", 2026-08/09. https://www.tftc.io/ai-capex-cash-flow-negative-2027-peak-hyperscalers
- CMB International, Lumentum research note, 2026-08-12. https://pdf.dfcfw.com/pdf/H3_AP202608121827906600_1.pdf
- Innolume, HiPER-CPO project, 2026-07-27. https://www.innolume.com/news/innolume-coordinates-the-hiper-cpo-project-to-develop-laser-sources-for-co-packaged-optics/
- Interactive Brokers, company-connections and price data (LITE, COHR, 5801, 688498, AAOI), 2026-10-14. IBKR company data (no public URL)


---

### 4.3 — #3 · Merchant scale-up switch silicon for non-NVLink XPU domains (PCIe AI-fabric now; UALink and ESUN/SUE Ethernet next)
*Megatrend: AI capex shifting to custom-XPU and non-NVIDIA GPU racks with switched scale-up domains | 2026 -> 2030 revenue: $0.6-1.4B -> $3.5-14B | CAGR: 55-78% (central ~73%; ~50-58% on the Q4-26 exit run rate) | Growth mix: ~60% volume / ~40% content per XPU (driven by bandwidth; like-for-like $/Tbps falls, so price contributes ≤0) | Confidence: Low (medium on direction, low on magnitude)*

**Definition.** In: switch ICs sold by third-party vendors, standard or semi-custom, whose main deployment is XPU-to-XPU scale-up. Value is counted at IC selling price.
- (a) PCIe AI-fabric switches: Astera Scorpio X; semi-custom parts in the AWS NeuronSwitch role; XConn and Switchtec parts when used as XPU fabric.
- (b) UALink 1.0/2.0 switches.
- (c) Ethernet scale-up silicon: Tomahawk Ultra; Tomahawk 5/6/7 in scale-up trays (e.g. AMD Helios); Marvell and Upscale ESUN parts.
- (d) Chinese non-Huawei merchant chips.

Out:
- NVIDIA NVLink Switch, including NVLink Fusion (the main substitute).
- Captive fabrics: Google ICI/OCS, Huawei UB, hyperscaler in-house ASICs.
- Scale-out silicon and Scorpio P (~$4B TAM [G]).
- Retimers and AECs (L06).
- Optics, CPO and photonic fabric.
- Trays and cables.

Grey zone: NeuronSwitch-v1 is counted as merchant on third-party attribution only.

**Value-chain path.** AI capex -> custom-XPU and non-NVIDIA GPU racks (Trainium, AMD Helios, MTIA, Maia, OpenAI-Broadcom, China non-Huawei) -> switched scale-up domain (64-144 XPUs now, 256-1,024 later) -> ODM switch trays (Taiwan/Mexico) -> **merchant scale-up switch IC** -> TSMC N5/N3 wafers, ABF substrates, Taiwan OSAT/test

**Drill-down decision.** I kept the niche protocol-agnostic. The same vendors serve all protocols, so the move from PCIe to UALink/Ethernet is share shift inside the niche. I tested three children:
- **PCIe AI-fabric: rejected.** It would show a false peak once sockets migrate from 2027-28. Scorpio X alone is ~$0.37-0.55B in 2026 [E].
- **UALink-native: flagged as emerging, not ranked.** ~$0 in 2026. Silicon reaches labs in H2-26, with products in late 2026 or 2027 [R]. A $0.5-2.5B path by 2030 [E] is fragile: Broadcom left UALink, and Helios runs UALink-over-Ethernet [R].
- **Ethernet scale-up: likely the fastest child, but not measurable.** ~$0.15-0.7B -> $2.5-8B [E]. Broadcom does not disclose it, and the same die also serves scale-out.

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) [E] | $0.6-1.4B | $3.5-14B | 55-78% (low-low / high-high) |
| Central [E] | ~$0.9B | ~$8B | ~73% |
| Exit-rate basis [E] | Q4-26 annualized $1.1-2.2B (central ~$1.6B) | ~$8B | ~50% (4 yr) / ~58% (3.5 yr) |
| Bear case [E] | ~$0.9-1.1B | $2-4B (central ~$3B) | ~22-45% |

Math:
- Range: (3.5/0.6)^0.25 - 1 = 55.4%; (14/1.4)^0.25 - 1 = 77.8%.
- Central: (8/0.9)^0.25 - 1 = 72.7%.
- Exit rate: (8/1.6)^0.25 - 1 = 49.5%; (8/1.6)^(1/3.5) - 1 = 58.4%.
- The cross-paired extremes (1.4->3.5 = 25.7%; 0.6->14 = 119.8%) are not coherent scenarios.

2026 is a ramp year, with Scorpio X immaterial in H1. **Rank this niche on ~50-60% durable growth, not the ~73% headline.**

- **Volume vs price:** revenue = merchant-switched XPUs x content per XPU.
  - Units go from ~1.6M to ~6M (3.75x) [E]; content per XPU from ~$560 to ~$1,330 (2.4x) [E].
  - On a log basis, ln 3.75 = 1.32 and ln 2.38 = 0.86 against ln 8.9 = 2.18, giving ~60% volume and ~40% content.
  - The content gain is bandwidth, not price. Per-XPU scale-up bandwidth rises 2-4x (400G SerDes in 2028 [G, Broadcom]), and multi-tier domains lift the tier factor from ~1.2 to ~2.0 [E]. Like-for-like $/Tbps falls ~25-35% per generation [E].
  - In Tb/s terms, volume grows ~15-25x while $/Tbps falls ~40-65%, so no base-case growth depends on shortage pricing. Dell'Oro's supply-constrained view [3P] only slows the decline.
  - I reject the draft's "flat ~$1.6-2.2k per chip" model: TH6 (~$8-15k, unverified) and PCIe switches (~$1-2k, unverified) differ 5-10x in radix and price.
- **Top-down:** all figures [E] unless marked.
  - *2026 (a), Trainium3:* 144-chip all-to-all via NeuronSwitch-v1 [R, AWS docs]. 0.6-1.2M chips (unverified) x 0.3-0.4 switches x $1.0-2.0k = $250-800 per XPU, so $0.15-0.96B (central $0.45B).
  - *2026 (b), Helios:* 12 TH6 per 72-GPU rack (6 trays x 2) [R].
    - Bandwidth check: 72 x 1.8 TB/s per direction = 1,037 Tb/s ÷ 102.4 = 10.1 chips, consistent with 12 chips using 432 of 512 ports. The draft's "260 TB/s ÷ 102.4 Tb/s" mixed bytes and bits.
    - Revenue: 0.5-2k racks x 12 x $8-15k = $0.05-0.36B (central $0.16B), or $1.3-2.5k per GPU.
  - *2026 (c), other custom XPUs:* 0.2-0.6M x $200-800 = $0.04-0.48B (central $0.16B).
  - *2026 (d), China non-Huawei:* $0.03-0.10B. This is capped by Huatai's implied 2026E of ~RMB 1.3B (~$0.18B) for the whole domestic market including Huawei [3P].
  - *2026 sum:* $0.27-1.9B; core $0.6-1.4B; central ~$0.83B (≈1.6M x $520).
  - *2030 units:* a pool of 7.5-19M non-NVIDIA, non-TPU, non-Huawei accelerators x 40-60% merchant capture = 3.0-11.4M; core 3.5-9M.
  - *2030 content:* 15-35 Tb/s per direction x $35-80/Tbps x tier factor 1.2-2.0 = $630-5,600 per XPU; core $800-2,500.
  - *2030 revenue:* 3.5M x $800 = $2.8B up to 9M x $2,500 = $22.5B; core $4-14B; central 6M x $1.4k = $8.4B.
- **Bottom-up:** Astera Scorpio X in 2026 totals $0.37-0.55B (central ~$0.47B) [E]:
  - Q1 $6-19M: Scorpio ~20% x $308.4M [R, soft], of which X is 10-30%.
  - Q2 $30-60M: Scorpio $90-130M of $392.4M [R].
  - Q3 $140-200M: on a $540-560M guide [G], +40% QoQ. The Scorpio family (P+X) becomes the largest category [G].
  - Q4 $190-270M: assumes $600-700M total revenue, which is not guided.

  Other 2026 suppliers:
  - Broadcom $0.15-0.7B (central $0.35B), from TH6 in Helios plus custom-XPU Ethernet. Tomahawk Ultra scale-up lands in FY27 [G].
  - Marvell/XConn $0.005-0.03B.
  - China $0.03-0.10B.
  - Others $0-0.02B.

  **2026 total: $0.55-1.4B, central ~$0.9B.**

  2030 build:
  - Astera $1.5-4B.
  - Broadcom $1.5-6B. The AMD socket alone is 2-3M GPUs x $1.5-3k = $3-9B if it stays on Ethernet.
  - Marvell $0.2-1.5B.
  - Start-ups $0.1-1.0B.
  - China $0.3-1.2B.

  **2030 total: $3.6-13.7B, central ~$7.6B.** For comparison, the draft built $5.4-16B and the bear case $2.3-4.7B.
- **Reconciliation:**
  - *2026.* Cut from the draft's $0.8-1.6B ($1.1B central) because the fact-check showed three upper bounds were too high. The China bound exceeded Huatai's whole domestic market. Broadcom's $0.9B ignored the FY27 timing of Tomahawk Ultra. Astera's needed a ~$700M Q4. Top-down and bottom-up are not independent: both rest on Astera's Q3 guide, which is ~45-55% of the niche.
  - *Draft 2030 top-down.* It was silently narrowed: 25-40M x 18-28% = 4.5-11.2M XPUs, not 4.5-9M, implying $3.4-33.6B.
  - *Dell'Oro.* ~$1T cumulative over 2026-30, with scale-up >50% by 2030 [3P]. My conversion to merchant silicon:
    - 2030 annual market $250-330B [E] x 50% scale-up = $125-170B;
    - x 35-50% non-NVLink = $45-85B;
    - x 20-30% silicon share = ~$9-25B.
  - *Astera TAM.* Astera's ~$20B TAM [G] is a ceiling. Its ~$10B Scorpio X portion covers PCIe+UALink; that the other half is Ethernet is unverified.
  - *Final 2030: $3.5-14B, central ~$8B.* The low end is widened below the fact-check's $4B because the bear case's substitution evidence is real but not decisive. The high end is held at $14B because the upside checks come from aggressive sources.

#### Demand drivers and catalysts
- **Torus -> switched domains.** Trainium2 used a 64-chip torus; Trainium3 switches 144 chips [R]; Helios switches 72 GPUs [R]. Status: in volume; Trn3 has been in mass production since Q2-26 [3P].
- **Domains growing to 256-1,024 XPUs (2027-29).** The UALink maximum is 1,024, which forces multi-tier switching. Counterpoint: GF Securities expects the mainstream Trainium4 to have 64 cards [3P].
- **ASIC share of AI servers:** 27.8% in 2026 -> ~40% in 2030 [3P, TrendForce].
  - Meta has a 6-GW custom MI450 programme [G].
  - Dell'Oro expects scale-up to exceed half of back-end switching by 2030, with Ethernet leading [3P].
- **Astera Q3-26 results (~10-Nov-2026):** guided at $540-560M [G]; report pending.
- **Broadcom FQ4 FY26 (Dec-2026):** Tomahawk Ultra was deployed in FQ3 [R], with scale-up applications in FY27 [G]. Tomahawk 7 (200T) has taped out for 2027 [G].
- **Helios ramp (H2-26 to 2027):** MI450 was sampling in Q2-26 [G]; HPE offers Helios in 2026 [R]. Rack counts are undisclosed.
- **UALink silicon:** Upscale SkyHammer is slated for Q4-26 [R]; Astera's portfolio arrives in 2027 [G]; the UALink 2.0 spec was released Apr-2026 [R]. No production switch is confirmed yet.
- **Trainium4 (late 2027 on N2 [3P]):** AWS has committed to NVLink Fusion [R]; Morgan Stanley says it will use both Fusion and UALink [3P]. The split should be visible in H1-27.
- **Marvell/XConn:** revenue starts FQ3 FY27, reaching ~$100M in FY28 [G, not re-verified].
- **400G SerDes copper scale-up in 2028 [G].**

#### Supply side
- **Suppliers and shares [E]:**
  - 2026: Astera ~40-60%, Broadcom ~25-50%, China 3-10%, Marvell 1-3%.
  - 2030: Astera 20-40%, Broadcom 30-45%, Marvell 5-15%, start-ups 2-8%, China 5-12%.
- **Capacity and lead times:**
  - All suppliers are fabless. Capacity means TSMC N5/N4/N3 allocation, ABF substrates (Ibiden, Unimicron, Nan Ya PCB, Kinsus) and test (KYEC/ASE).
  - 3nm is tight [3P], and XPUs get priority over switch ICs.
  - Wafer-to-ship lead time is 20-40 weeks [E, unverified].
  - Dell'Oro expects supply constraints through 2030 [3P].
- **Qualification barriers:**
  - Switches are designed in at XPU definition, 2-3 years before ramp.
  - Rack qualification takes 12-24 months and is tied to the protocol and software stack (COSMOS, NeuronLink, UALoE) [E].
  - Each generation is single- or dual-sourced; sockets become contestable at generation changes.
  - Only Broadcom, Astera, Marvell and possibly Upscale combine 200G SerDes, high-radix switch IP and the hyperscaler software stack.
- **Geographic concentration:**
  - Design: US and Israel. Wafers: ~100% TSMC Taiwan. Substrates: Japan and Taiwan. OSAT and tray ODMs (Wiwynn, Quanta, Foxconn): Taiwan.
  - Astera's Q1-26 ship-to was Taiwan $93.2M and China $89.6M (29%) [R]. These are ODM sites passing product through, not end customers.
  - China is a separate ecosystem constrained by SMIC.

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| Astera Labs | ALAB / Nasdaq | Lead PCIe/UALink scale-up switch vendor; Trainium anchor (third-party attribution) | Scorpio X ~18-30% of 2026E revenue of ~$1.85-1.95B [E] |
| Broadcom | AVGO / Nasdaq | Ethernet scale-up (TH Ultra/6/7); XPU designer able to bundle switches | <1% of revenue; ~1-4% of FY26 AI networking (~$16-20B) [E] |
| Marvell | MRVL / Nasdaq | UALink/ESUN switches (XConn); NVLink Fusion partner; photonic fabric | <0.3% in FY27; ~3-8% by FY31 [E] |
| Upscale AI | Private (~$2B valuation) | SkyHammer UALink/ESUN switch | ~100% (pre-revenue) |
| Cornelis Networks | Private | UALink/ESUN fabric (Sep-2026) | Unknown |
| Suzhou Centec | 688702 / SSE STAR | Chinese merchant switch silicon | Unverified |
| Microchip | MCHP / Nasdaq | Switchtec PCIe switches | <0.5% [E] |
| AMD / NVIDIA | AMD, NVDA / Nasdaq | Demand driver / main substitute (NVLink Fusion; stakes in Marvell and Upscale) | 0% / excluded |
| TSMC | 2330 TWSE / TSM NYSE | Sole non-China foundry | <0.5% |

#### Bear case and key risks
- **Technology substitution:** four substitutes [E unless marked].
  1. **NVLink Fusion.** AWS has committed Trainium4 to it [R]. NVIDIA's $2B stake in Marvell, AWS's Trainium partner, creates "soft lock-in" [R]. Bear case: Fusion takes 35-50% of non-Google custom-XPU domains by 2030, versus ~10-25% in the draft.
  2. **In-house switches and smaller domains.** IBKR flags AWS/Annapurna in-house parts as a threat [3P], and GF expects a 64-card Trainium4 [3P]. Together with switchless Google ICI, these take 10-20%.
  3. **ESUN/SUE commoditization.** Scale-up on Tomahawk-class Ethernet removes the PCIe/UALink price premium, and Broadcom can bundle switches with its XPUs. PCIe AI-fabric ends by 2028, and UALink stays below 15% of 2030 ports.
  4. **Photonic fabrics.** Marvell guides its Photonic Fabric to a $0.5B run rate by Q4 FY28 and $1B by Q4 FY29 [G]. 15-30% of scale-up value moves to optics.

  Net: 2.5-4M merchant-switched XPUs in 2030 at $600-1,000 content each, versus the draft's 4.5-9M at $900-1,800.
- **Capex cuts:**
  - Big-4 2026 capex is ~$725B, up 77% [3P]; 2027 is ~$1.0-1.14T [3P].
  - Hyperscaler debt issuance was ~$194B in H1-26 versus $17B in 2024 [3P, source mapping unverified]. Meta is reportedly reselling excess compute [R, secondary].
  - A 20-30% capex cut in 2028 would cut niche revenue 35-55% for 2-4 quarters [E], because custom-XPU programs are the swing capacity and ODMs buy ahead.
  - Concentration: Astera Customer A was 29% of revenue in both Q1 and Q2-26, and Customer B 25% in Q2 [R, 10-Q]. Losing the Trainium4 socket removes $0.5-1.5B of 2028 revenue [E].
- **Chinese capacity:** low risk to global pricing.
  - Centec is raising RMB 3.18B for scale-up switch chips [R]. Huatai sizes the domestic market at RMB 12.9B by 2028 [3P].
  - No Chinese part is qualified outside China, and the chance of that before 2030 is <10% [E].
  - Effect on the bear case: within ±$0.3B.
- **Double-ordering / pull-forward:** suggestive but not proven; no inventory data was retrieved.
  - A +40% QoQ guide on a single program implies 4-8 weeks of ODM pipeline fill [E], and ODM booking hides channel stock.
  - Shortage psychology and vendor financing add to the risk; Broadcom's XPV platform with Apollo and Blackstone targets >20 GW by 2028 [G].
  - 10-20% of 2026-27 revenue (~$0.15-0.4B a year) reverses [E], with a risk of a 2027 peak and a 2028 trough.
- **Already priced in?** Yes for Astera; no for Broadcom and Marvell, where the niche is under 1-3% of revenue.
  - ALAB traded at ~$292 on 14-Oct-2026, against a 52-week range of $97.89-499.48 [R]. That is ~41% below the June peak.
  - Market cap is ~$48-52B, or ~24-27x 2026E revenue [E; share count unverified].
  - The Q2 beat-and-raise sold off (Trefis), and two 2x single-stock ETFs exist [R].
  - Upscale is valued at ~$2B with no revenue, and Centec is up ~156% YTD [R].
- **Bear-case numbers:**
  - **2030 size: $2-4B, central ~$3B [E].**
    - Top-down: 20-28M accelerators x 10-14% = 2.0-3.9M XPUs (the bear rounds to 2.5-4M) x $600-1,000 = $1.2-3.9B.
    - Bottom-up: Astera $0.8-1.5B + Broadcom $1.0-2.0B + Marvell $0.2-0.5B + start-ups $0.05-0.2B + China $0.2-0.5B = $2.3-4.7B.
  - **CAGR as stated by the bear: ~11-41%, central ~28%.** $1.1B -> $3.0B = 28.5%; $1.3B -> $2.0B = 11.4%; $1.0B -> $4.0B = 41.4%.
  - **CAGR re-based on the $0.9B central: 22-45%, central 35%.** From the exit run rate it is ~0-19%.
  - **Probability:** ~30% (range 25-35%) that 2030 is ≤$4B; ~10% for a deep tail of $1.2-1.8B.
  - **First warning sign:** an Astera Q4 guide below ~$580M on ~10-Nov-2026, or no second hyperscaler named. In H1-27, the tell is Taiwan supply-chain reports showing Trainium4 switch trays using NVLink or a 64-card in-house design.

#### Leading indicators to watch (next 2-4 quarters)
1. **Astera Q3-26 (~10-Nov-2026):** a Q4 guide ≥$600M is bullish, <$580M bearish. Also watch for a Scorpio P/X split, a second hyperscaler in X volume, and customer concentration and inventory in the 10-Q.
2. **Broadcom FQ4 FY26 (Dec-2026) and FQ1 FY27:** named Tomahawk Ultra scale-up deployments and Tomahawk 7 sampling.
3. **Helios rack shipments (AMD, HPE, Celestica, Wiwynn):** racks x 12 TH6 gives a direct read on Ethernet scale-up revenue.
4. **Trainium4 switch-tray bill of materials (H1-27):** reports in DigiTimes, Commercial Times, MoneyDJ and cnyes on NVLink Fusion versus merchant trays, and 64-card versus 144-card domains.
5. **UALink/ESUN silicon:** SkyHammer availability, Astera and Marvell UALink sampling, and ESUN progress at OCP.
6. **Hyperscaler Q4-26 calls:** a 2027 capex guide below ~+30%, or talk of excess capacity.

#### Confidence and biggest unknown
**Low.** The direction is well supported by Astera's reported results and guidance, Broadcom and AMD disclosures, and Dell'Oro. The magnitude is not:
- The Scorpio X/P split, TH6 and Scorpio X ASPs, Trainium3 units and the Helios rack count are all unverified.
- Broadcom does not disclose scale-up revenue (about ±$0.3B on 2026).
- No earnings-call transcript was read directly. Alpha Vantage was rate-limited, so call content comes from secondary summaries and IBKR.

**Biggest unknown:** how much of the 2027-30 custom-XPU base stays on merchant switches instead of moving to NVLink Fusion or in-house parts. This turns mainly on Trainium4/5 and the OpenAI/Meta Broadcom racks, and it swings 2030 between ~$3B and ~$14B.

**Definitional risk:** AWS does not name the NeuronSwitch-v1 supplier; the Astera attribution rests on SemiAnalysis and sell-side notes. If the part is in-house, ~40-55% of the 2026 base leaves the niche.

#### Sources
- Astera Labs, "Astera Labs Reports Second Quarter 2026 Financial Results", 2026-08-04. https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-reports-second-quarter-2026-financial-results
- Astera Labs (SEC), Q2-2026 8-K Exhibit 99.1, 2026-08-04. https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000033/q226exhibit991.htm
- Astera Labs (SEC), Form 10-Q Q2-2026, 2026-08. https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000035/alab-20260630.htm
- Futurum Group, "Astera Labs Q2 FY 2026 Earnings Pull Scorpio Switch Leadership Forward", 2026-08-04. https://futurumgroup.com/insights/astera-labs-q2-fy-2026-earnings-pull-scorpio-switch-leadership-forward/
- MarketBeat, "Astera Labs Q2 Earnings Call Highlights", 2026-08-04. https://www.marketbeat.com/instant-alerts/astera-labs-q2-earnings-call-highlights-2026-08-04/
- Trefis, "Astera Labs Beat and Guided Higher, Then Fell Because the Rally Came First", 2026-08-06. https://www.trefis.com/stock/alab/articles/610418/astera-labs-beat-and-guided-higher-then-fell-because-the-rally-came-first/2026-08-06
- Astera Labs, "Astera Labs Broadens Scorpio X-Series Smart Fabric Switch Roadmap", 2026-01-22. https://www.asteralabs.com/news/astera-labs-broadens-scorpio-x-series-smart-fabric-switch-roadmap-to-address-expanding-scale-up-market-opportunities/
- MarketBeat, "Astera Labs Touts AI Infrastructure Tailwinds, Highlights Scorpio Switch Ramp at Morgan Stanley Conference", 2026-03-03. https://www.marketbeat.com/instant-alerts/astera-labs-touts-ai-infrastructure-tailwinds-highlights-scorpio-switch-ramp-at-morgan-stanley-conference-2026-03-03/
- Nasdaq, "Broadcom Q3 Earnings Call Highlights", 2026-09. https://www.nasdaq.com/articles/broadcom-q3-earnings-call-highlights
- Pulse2, "Broadcom Q3 Fiscal 2026 Revenue Jumps 86% to $29.6 Billion", 2026-09. https://pulse2.com/broadcom-q3-fiscal-2026-revenue-jumps-86-to-29-6-billion-as-ai-semiconductor-revenue-reaches-16-7-billion/
- ChannelWeb, "Broadcom Q3 Results: CEO Tan Forecasts Surging AI Infrastructure Buildout", 2026-09. https://www.channelweb.co.uk/news-network/2026/broadcom-q3-results-ceo-tan-forecasts-surging-ai-infrastructure-buildout
- Bullfincher, "Broadcom FY2026 Q3 Earnings Call", 2026-09. https://bullfincher.io/companies/broadcom/earnings-call/fy2026-q3
- The Register, "HPE AMD Helios racks", 2025-12-02. https://www.theregister.com/2025/12/02/hpe_amd_helios_racks/
- PC Games Hardware, "AMD Helios KI-Rack MI455X Spezifikationen", 2026-06. https://www.pcgameshardware.de/Kuenstliche-Intelligenz-Hardware-279517/Specials/AMD-Helios-KI-Rack-MI455X-Zen-6-Spezifikationen-1549243/
- ServeTheHome, "AMD Helios Architecture Deep Dive", 2026-10. https://www.servethehome.com/amd-helios-architecture-deep-dive-amd-broadcom-hardware-combined/4/
- The Register, "Amazon Nvidia Trainium", 2025-12-02. https://www.theregister.com/2025/12/02/amazon_nvidia_trainium/
- AWS, "Trainium3 Architecture" (Neuron docs), 2026. https://awsdocs-neuron.readthedocs-hosted.com/en/v2.28.1/about-neuron/arch/neuron-hardware/trn3-arch.html
- TipRanks/TheFly, Morgan Stanley and Jefferies notes on Astera/Trainium, 2025-12. https://il.tipranks.com/news/the-fly/2689327
- Zaikei, Trainium4 NVLink Fusion support, 2026-08-28. https://www.zaikei.co.jp/article/20260828/867754.html
- NVIDIA, "NVIDIA Unveils NVLink Fusion", 2025-05 [STALE 2025-05]. https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Unveils-NVLink-Fusion-for-Industry-to-Build-Semi-Custom-AI-Infrastructure-With-NVIDIA-Partner-Ecosystem/default.aspx
- Tom's Hardware, "Nvidia invests $2 billion in Marvell", 2026 (date unverified). https://tomshardware.com/tech-industry/nvidia-invests-2-billion-in-marvell-whose-biggest-clients-are-trying-to-replace-nvidia-chips
- Economic Daily News (udn), Trainium3/4 timing citing Morgan Stanley, undated (likely 2025-12). https://money.udn.com/money/amp/story/5607/9189980
- Tiger Brokers, GF Securities on Trainium4 configurations, 2026 (undated). https://www.itiger.com/news/1104706920
- Marvell, "Marvell to Acquire XConn Technologies", 2026-01-06. https://www.marvell.com/company/newsroom/marvell-to-acquire-xconn-technologies-expanding-leadership-in-ai-data-center-connectivity.html
- The Register, "Upscale SkyHammer", 2026-01-22. https://www.theregister.com/2026/01/22/upscale_skyhammer_nvidia/
- LetsDataScience, "Upscale AI raises $190M", 2026-06. https://letsdatascience.com/news/upscale-ai-raises-190m-to-expand-ai-networking-infrastructur-bd429752
- HPCwire/AIwire, "Cornelis to build scale-up interconnect using UALink and ESUN", 2026-09-14. https://www.hpcwire.com/aiwire/2026/09/14/cornelis-to-build-scale-up-interconnect-using-ualink-and-esun/
- Dell'Oro Group, "AI Back-End Switch Sales to Approach $1 Trillion Over the Next Five Years", 2026-07-28. https://www.delloro.com/news/ai-back-end-switch-sales-to-approach-1-trillion-over-the-next-five-years/
- The Register, "UALink 2.0 specs", 2026-04-07. https://www.theregister.com/2026/04/07/ualink_2_specs/
- HPCwire, UALink 1.0 silicon timing, 2026. https://www.hpcwire.com/?p=186501
- HPCwire, first UALink products late 2026/early 2027, 2026-09. https://www.hpcwire.com/?p=197496
- LightCounting, April 2025 LightTrends [STALE 2025-04; superseded, not used for sizing]. https://www.lightcounting.com/newsletter/en/april-2025-ethernet-infiniband-and-optical-switches-for-cloud-datacenters-335
- TrendForce, ASIC AI-server share, 2026-01-20. https://www.trendforce.com/presscenter/news/20260120-12887.html
- TrendForce, Trainium/ASIC update, 2026-05-20. https://www.trendforce.com/presscenter/news/20260520-13053.html
- 10jqka, supernode supply chain citing Huatai, 2026-09-20. https://news.10jqka.com.cn/20260920/c680089571.shtml
- East Money, Huatai scale-up switch-chip report, 2026-05-24. https://finance.eastmoney.com/a/202605243747425461.html
- 10jqka, Centec placement, 2026-09-02. https://stock.10jqka.com.cn/20260902/c679540905.shtml
- AI Weekly, "$725B AI capex in 2026", 2026. https://aiweekly.co/alerts/amazon-microsoft-alphabet-meta-plan-725b-ai-capex-in-2026
- DatacenterDynamics, "Moody's hyperscaler capex forecasts marked up by $85bn", 2026. https://datacenterdynamics.com/en/news/moodys-hyperscaler-capex-forecasts-marked-up-by-85bn-to-close-in-on-1trn-by-2027/
- Crypto Briefing, "AI hyperscalers' trillion-dollar spending gamble", 2026. https://cryptobriefing.com/ai-hyperscalers-trillion-dollar-spending-gamble/
- TIKR, "Astera Labs fell 12% Monday", 2026-07. https://www.tikr.com/blog/astera-labs-fell-12-monday-heres-where-alab-stock-could-head-in-2026?
- Interactive Brokers, company-connections and market data (ALAB, AVGO, MRVL, AMD), 2026-05 to 2026-10. No public URL (IBKR MCP data).


---

### 4.4 — #4 · Merchant optical circuit switches (OCS) for AI cluster fabrics
*Megatrend: AI data-center capex -> reconfigurable optical AI fabrics | 2026 -> 2030 revenue: $0.35-0.65B -> $1.8-6.0B (central ~$0.47B -> ~$3.3B) | CAGR: 51-74% matched-pair (central ~63%; 40-89% on the central 2026 base) | Growth mix: ~115% volume (~75% end-market ports + ~40% captive-to-merchant shift) / ~-15% price (shares of log growth) | Confidence: Low (direction well supported, magnitude not)*

**Definition.** In: complete OCS systems (MEMS/LC/piezo/robotic/SiPh engine, collimator and fiber arrays, chassis, control software) sold by third-party vendors for AI fabrics: TPU/XPU ICI and superpod interconnect, DCN spine, scale-across, and (from late 2028) GPU rack-to-rack scale-up. This includes merchant units bought by Google (Lumentum R300/R64, Coherent LC, Polatis in AI use, DiCon, Calient, Telescent, Chinese vendors, SiPh startups). Out: Google's in-house Palomar/Apollo OCS built by contract manufacturers (CMs), which is context only; components sold into captive builds; ROADM/WSS; lab/test switches; transceivers and circulators; electrical and CPO packet switches.

**Value-chain path.** AI data-center capex -> accelerator clusters (TPU/XPU now, GPU multi-rack later) -> cluster fabric (ICI/superpod, DCN spine, scale-up) -> optical switching layer -> optical circuit switches -> **merchant OCS systems** <- inputs: MEMS mirror arrays, 2D collimator/fiber arrays, drivers, chassis CM.

**Drill-down decision.** We kept the merchant level. It is already the faster child of total OCS (total ~33%/yr in our central [E], ">30%" per Cignal [3P]) because Google is shifting from in-house builds to vendors. Narrower children were rejected:
- (a) GPU scale-up OCS: ~zero 2026 base, undefined CAGR, contested evidence. Carried as a scenario leg.
- (b) Lumentum-to-Google: ~80-85% of the niche, so splitting adds nothing.
- (c) LC/SiPh startups: below the size floor.

Components are a separate adjacent niche.

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $0.35-0.65B [E] | $1.8-6.0B [E] | 51-74% matched (29-104% cross) |
| Central | ~$0.47B [E] | ~$3.3B [E] | ~63% |
| Bear case (~25%) | $0.55-0.65B (bear's base) | $1.1-1.8B [E] | 14-35% (central 22.5%) |
| Context: total OCS incl. captive | ~$1.9B [E]; Cignal-implied ~$2.1-2.8B | ~$6B [E]; Cignal >$8B [3P] | ~33% [E]; Cignal >30% [3P] |

Math:
- Central: (3.3/0.47)^(1/4)-1 = 7.02^0.25-1 = 62.8%.
- Matched pairs: (1.8/0.35)^0.25-1 = 50.6%; (6.0/0.65)^0.25-1 = 74.3%.
- On the $0.47B base: 1.8 gives 39.9% and 6.0 gives 89.0%.
- Cignal's implied 2026 total: $8B/1.3^4 = $2.8B; $8B/1.4^4 = $2.1B.

- **Volume vs price:** Central growth is 7.02x (ln 1.95), in three log terms [E]:
  - $/port at 0.75x (ln -0.29): **-15%** of log growth.
  - Merchant share of total value, ~25% to ~55% (2.2x, ln 0.79): **+40%**.
  - End-market ports, ~4.3x (ln 1.45): **+74%**.
  - Check: 4.26 x 2.2 x 0.75 = 7.0x.

  No shortage premium: supply is "gated" [G], but no source shows price increases. The share-shift term (draft: ~25-30%) is ~40% and rests on one discretionary choice, Google's make-vs-buy, so growth is less durable than port volume suggests.
- **Top-down:**
  - **2026:**
    - Google external: ~15,000 Google units (300-port class; Chinese data/GTR, unverified) x 17-25% external = 2,500-3,750 units x $100-150k ($330-500/port, unverified) = $0.25-0.56B.
    - Non-Google: 300-1,200 300-port-equivalent units x $50-120k = $0.02-0.14B.
    - Total $0.27-0.70B, central ~$0.45B.
    - Cross-check: 4.5M Google ports / 1.5-1.8 ports per chip = 2.5-3.0M TPUs, ~55-95% of 3.2-4.5M 2026 TPUs [3P]. Consistent.
  - **2030:**
    - (a) XPU scale-out: 6-11M OCS-connected accelerators x 1.6-1.9 ports = 10-20M ports x $260-380 = $2.6-7.6B total; x 45-70% merchant = $1.2-5.3B, central ~$2.9B.
    - (b) GPU scale-up: 0.3-2.5M GPUs x 2-4 ports x $220-330 = $0.13-3.3B, central ~$0.8B. This is a deliberate contrarian haircut to the ~$4B Cignal/Citi imply.
    - (c) DCN spine, DCI and China: $0.2-0.7B.
    - Central ~$4.1B; arithmetic span $1.5-9.3B.
- **Bottom-up:**
  - **2026 Lumentum, by calendar quarter:**
    - CQ1 $15-35M: a $10M/quarter run-rate passed early (Feb); OCS "still relatively modest" (May).
    - CQ2 $30-70M: shipments "doubled" [G].
    - CQ3 $100-140M: first quarter above $100M [G]; "meaningfully above" was not found.
    - CQ4 $150-250M: balance of the >$400M backlog [G], supply-gated.
    - Sum $295-495M, central ~$385M.
  - **2026 others:** Coherent $0.02-0.10B (not disclosed), H+S $0.01-0.04B, others $0.01-0.04B.
  - **2026 total:** $0.34-0.68B, central ~$0.47B.
  - **2030 Lumentum:** CY27 $0.8-1.3B (the ">$1B 2027 run-rate" [G] is an exit rate) x 1.25^3 to 1.45^3 = $1.56-3.96B; central 1.05 x 1.35^3 = $2.58B.
  - **2030 others:** Coherent $0.2-0.8B, H+S $0.05-0.3B, Chinese vendors $0.1-0.5B, other vendors $0.05-0.4B.
  - **2030 total:** $2.0-6.0B, central ~$3.6B.
  - **Capacity check:** $3.3B / ~$300 per port = ~11M ports (~37k 300-port units), versus ~3.5-4.5k units in 2026: a ~9x build.
- **Reconciliation:**
  - **2026:** the methods overlap; we adopt $0.35-0.65B. The fact-check overrides the draft's $0.45-0.75B: the draft's CQ1 was too high, its "meaningfully above" wording was unsourced, and its Coherent figure had no anchor. The base is H2-loaded (CQ4 annualized exit ~$0.7-1.1B).
  - **2030:** the bear and base cases disagree without decisive evidence, so the low end is widened to $1.8B (the bear's upper bound). The central is probability-weighted: 0.25 x $1.35B + 0.75 x $3.8-4.0B = $3.2-3.3B.
  - **Cignal and Citi:** our implied total (~$6B) is below Cignal's >$8B because we haircut the GPU leg. Citi's ~$11B is a bull/TAM figure. Its "$5B scale-up" bucket is likely TPU ICI, so adding it to a GPU leg would double count, and "商用" may mean commercial rather than merchant.
  - **Dropped:** ChinaBaogao's "~$600M 2026 global market" (below our own merchant range), and the IBKR "$400M = 20% of forward revenue" (really ~14-15%, and a restatement of the backlog).
  - **Small-base caveat:** 2027-30 growth is only ~36-46%/yr ($1.05-1.3B to $3.3B).

#### Demand drivers and catalysts
- **TPU volume (ramping):** 3.2-4.5M in 2026 (~4M cluster), ~5M in 2027 (GF's 8.84M is an outlier) and ~7M in 2028 [3P]. TPU v8 (3nm) mass production starts Q3-26 [3P]. Ironwood superpods (9,216 chips) are stitched by OCS at ~1.5 ICI ports per chip [R, STALE 2025-08; v4 ratio STALE 2023].
- **Google make-vs-buy (biggest swing):** Cignal says internal builds are the majority of near-term ports, with a supply-constrained share open to vendors [3P, Feb-26]. Lumentum says the customer keeps its internal source but buys "the vast majority" of incremental volume from Lumentum [G, Aug-26].
- **Non-Google demand:** Lumentum has two hyperscalers shipping and a third committed for 2026 [G, Feb-26]. Coherent has 7 shipping customers (Nov-25) and >10 engagements (Feb-26), and an OCS TAM above $4B [G].
- **Catalysts:**
  - Alphabet Q3-26 call (late Oct 2026): 2027 capex framing. Alphabet has guided only a "significant increase" [G]; the Street is at ~$265B [3P].
  - Lumentum FQ1 FY27 (early Nov 2026): first >$100M OCS quarter [G] and a backlog update.
  - Lumentum >$1B OCS run-rate during CY27 [G], under a signed multi-billion agreement with undisclosed terms.
  - Coherent LC-OCS ramp in FY27 [G]: any top-3 hyperscaler award.
  - Nvidia GTC (Mar 2027): does Kyber/Feynman scale-up specify OCS? Cignal sees "significant volume beginning in 2028" [3P]; Kyber reportedly slipped to 2028 [3P]. Speculative.
  - Lumentum R64 GA in H2-26 [G, STALE 2025-09; unconfirmed].

#### Supply side
- **Suppliers and shares [E]:** of 2026 merchant, Lumentum ~80-85%, Coherent ~5-15%, H+S Polatis ~2-6%, others ~2-6%, Chinese vendors <3% (mostly domestic). Google captive (not counted) is ~70-80% of total 2026 value.
- **Capacity and lead times:** Lumentum is adding CM capacity on top of internal output [G], and its CEO says optical component capacity is committed through early 2029 [R, ~Oct-26]. Coherent runs two parallel lines [G]. H+S H1-26 EBIT fell 8.4% to CHF41.2M on OCS capacity investment [R]. Sai's Beijing MEMS-OCS line has been in small-batch trial since Aug-2025, not mass production [R]. Tower and Salience agreed an SiPh OCS production partnership (Feb-26) [R]. The binding constraints are MEMS array yield, collimator alignment at 300+ ports, and test time. Order-to-ship is ~2-3 quarters [E, unverified].
- **Qualification barriers:** hyperscaler qualification takes ~12-24 months including field-reliability data [E]. Other barriers are proprietary MEMS design, integration with Google's control plane, and multi-year agreements.
- **Geographic concentration:** demand is Google at ~70-90% [3P]. Merchant supply is US (Lumentum, Coherent) and UK/Switzerland (Polatis). MEMS foundries are in Sweden (Silex, deconsolidated from Sai Jul-25 [R]) and China (Sai). The passive sub-tier is in Taiwan (Browave, EZconn, FOCI) and China. The main risks are export controls and the Asian sub-tier.

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| Lumentum | LITE / Nasdaq | Dominant merchant MEMS OCS | ~7-11% of CY26 [E: $0.30-0.50B on ~$4.4-4.6B]; ~15-20% if the 2027 run-rate is met [E] |
| Coherent | COHR / NYSE | No.2 merchant vendor, LC OCS | <1.5% [E; FY26 revenue $7.12B, R] |
| Huber+Suhner | HUBN / SIX | Polatis piezo OCS | ~1-5% [E, unverified; H1-26 sales CHF457.4M, R] |
| Sai Microelectronics | 300456 / SZSE ChiNext | MEMS-OCS foundry (trial) | <5% |
| Accelink | 002281 / SZSE | Chinese MEMS OCS | <1% |
| Dekeli | 688205 / SSE STAR | SiPh OCS (32x32) | <2% (unverified) |
| Tower Semiconductor | TSEM / Nasdaq, TASE | Salience SiPh OCS foundry | <1% |
| Browave / EZconn / FOCI | 3163 TPEx / 6442 TWSE / 3363 TPEx | Collimator and fiber-array sub-tier (adjacent, not counted) | unverified |
| Alphabet | GOOGL / Nasdaq | Anchor buyer, captive designer | n/a |
| DiCon, Calient, Telescent, iPronics, nEye, Salience, Oriole, 孛璞半导体 | private | Challengers | high (DiCon diversified) |

#### Bear case and key risks
- **Technology substitution:**
  - (1) Google's captive Palomar, the most potent substitute and available now. Captive keeps 50-60% of Google ports in 2030 (bull: 35-45%), and the share-shift contribution falls to ~10-15%. External TPU systems may ship with Google-designed fabrics.
  - (2) Copper/CPO packet switching wins GPU scale-up. Nvidia's CEO reaffirmed copper, and Morgan Stanley reads Kyber scale-up as copper [3P]. The NVLink 6 CPO switch does electrical packet switching, not OCS [3P Counterpoint], and MEMS OCS reconfigures in tens of milliseconds [3P Next Platform]. Result: GPU leg $0-0.1B, which alone cuts the bull central from ~$4.1B to ~$3.2B.
  - (3) 102.4T/204.8T CPO Ethernet plus merchant UALink/SUE switches from 2026 [3P LightCounting] keep non-Google DCN OCS below $0.2B.
  - (4) In-niche deflation. Coherent LC, DiCon "value-focused" 300x300, Accelink 320x320 and SiPh entrants (nEye, iPronics, Salience/Tower, 孛璞 8x8-32x32 at CIOE Sep-26) take 25-40% of merchant units. $/port falls 10-12%/yr to $250-300.
  - (5) Robotic patch panels (Telescent): <5%.
- **Capex cuts:** Alphabet guides 2026 capex of $195-205B [G], and Q2-26 FCF was -$5.9B [R, secondary]. Scenario [E]: a 20-30% cut in 2028 from a ~$300B 2027 peak cuts new superpod starts 30-50%. Google loads its captive line first, so merchant volume falls 40-60% and 2028 merchant revenue is $0.6-0.9B (bull path: $1.8-2.2B). The LTA is more likely re-phased than cancelled; optical LTAs have historically had weak take-or-pay [E].
- **Chinese capacity:** no Chinese vendor discloses OCS capacity or is verified as qualified at a US hyperscaler. Accelink's mass-production claim and the MIIT program are unverified, and Dekeli excludes silicon OCS from its 2-3-year plan [3P]. The main channel is cheaper Chinese sub-tier parts, which lower Google's captive BOM and cap merchant pricing. Bear sizing: 10-20% of merchant units but only 5-10% of revenue by 2030; a flood into US sockets before 2029 is <10% likely.
- **Double-ordering / pull-forward:** ~$10M shipped in the Dec-25 quarter became a >$400M backlog within ~4 quarters, mostly from ~3 customers [3P Guosen], at a sole merchant source, with capacity "committed through early 2029". LightCounting says double ordering disappears once capacity is added and price declines then accelerate [3P, Jul-26]; Eoptolink's H1-26 inventory rose 61% to RMB11.7B [R]. The bull needs ~9-10x merchant units, bear demand only ~2.5-3x. Bear estimate: ~$0.1-0.3B of 2026-27 revenue is pull-forward that reverses in 2028 [E]; LTA terms are undisclosed.
- **Already priced in?** Yes, for LITE: $874.50 on 2026-10-14, +137% YTD, 52-week range $152.54-$1,143 [R IBKR], after +964% in 2025; forward P/E ~41-43x, consensus target ~$1,126 (Aug-26) [3P]. COHR at $257.76 is 41% below its high [R], so its LC option is not paid for. Cignal raised its forecast three times in eight months [R]; the unpriced surprises are on the downside.
- **Bear-case numbers:**
  - **2030 size:** merchant $1.1-1.8B, central ~$1.35B [E]: scale-out $0.8-1.2B, GPU $0-0.1B, other $0.2-0.4B. Path: 2027 $1.0-1.3B, 2028 $0.7-1.1B, 2029 $0.9-1.4B.
  - **CAGR:** central (1.35/0.6)^0.25-1 = 22.5%; range 14.1% (0.65 to 1.1) to 34.5% (0.55 to 1.8); deep tail ($0.8-1.0B) ~8-14%. Price offsets ~45% of the volume gain: ports 2.9x (+1.05 log), share 35% to 45% (+0.25), $/port $450 to $280 (-0.47). Re-based on our $0.47B central, the same 2030 levels give 24-40%; the bear's 2030 dollars are what matter.
  - **Probability:** ~25% (20-30%); deep tail ~5-8%. The bear needs ≥2 of: GPU OCS below $0.3B in 2030 (~50-60%); Google keeps a captive majority (~40%); $/port erosion ≥10%/yr (~35%); a ≥20% Google capex cut in 2028 (~25-30%).
  - **First warning sign:** Lumentum FQ1 FY27 (early Nov 2026) shows OCS book-to-bill below 1 (backlog under ~$400M while shipping >$100M), stops quantifying the backlog or 2027 run-rate, or guides FQ2 OCS below ~$150M.

  At ~22-24%, L02 drops out of the top tier.

#### Leading indicators to watch (next 2-4 quarters)
1. Lumentum FQ1/FQ2 FY27 (Nov 2026, Feb 2027): OCS >$100M, then $150-250M; backlog, book-to-bill and named CMs. If FQ1 is well above $100M and FQ2 is guided at $200M+, move 2026 toward $0.55-0.65B.
2. Alphabet Q3-26 (late Oct 2026): 2027 capex versus the ~$265B Street figure; external TPU sales.
3. Cignal AI 3Q26/4Q26: merchant share, $/port, a second Google CM, or Coherent qualified at a lower $/port.
4. Coherent FQ1/FQ2 FY27: OCS customer count above 10, or any revenue disclosure.
5. Nvidia GTC (Mar 2027): OCS versus copper/CPO in Kyber/Feynman scale-up.
6. H+S FY26 (Mar 2027) OCS orders; Sai/Accelink/Dekeli mass-production disclosures; DiCon pricing.

#### Confidence and biggest unknown
**Confidence is low.** The direction (>30%/yr through 2027) is well supported by Lumentum guidance and backlog; the magnitude rests on undisclosed variables.

**Biggest unknown:** Google's make-vs-buy, ~40% of central log growth. Second is the GPU scale-up leg (~$4B per Cignal/Citi versus $0-0.1B in the bear case). Third is $/port, which has no primary disclosure (~$330-500 today, unverified).

For ranking, weight the 2027-30 rate (~36-46%/yr) over the headline ~63%, which is inflated by the 2026 intra-year ramp.

#### Sources
- Lumentum, "Q4 and Full Fiscal Year 2026 Results" (Form 8-K Ex. 99.1), 2026-08-11. https://www.sec.gov/Archives/edgar/data/0001633978/000162828026055726/lite_ex991xq4fy26.htm
- Lumentum, "Q4 FY2026 Results" press release, 2026-08-11. https://s21.q4cdn.com/377324469/files/doc_news/Lumentum-Announces-Fourth-Quarter-and-Full-Fiscal-Year-2026-Results-2026.pdf
- MarketBeat, "Lumentum Q4 Earnings Call Highlights", 2026-08-11. https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/
- MarketBeat, "Lumentum Q3 Earnings Call Highlights", 2026-05-05. https://www.marketbeat.com/instant-alerts/lumentum-q3-earnings-call-highlights-2026-05-05/
- Investing.com, "Earnings call transcript: Lumentum tops Q4 2026 forecasts", 2026-08-11. https://www.investing.com/news/transcripts/earnings-call-transcript-lumentum-tops-q4-2026-forecasts-as-ai-demand-lifts-outlook-93CH-4852933
- 404K Research, "Lumentum fiscal 2026 fourth quarter", 2026-08. https://404kresearch.substack.com/p/lumentum-fiscal-2026-fourth-quarter
- Zacks via Nasdaq, "Bull of the Day: Lumentum", 2026. https://www.nasdaq.com/articles/bull-day-lumentum-lite-0
- MoneyDJ via udn, Lumentum OCS shipments, 2026-02. https://money.udn.com/money/story/5710/9800240
- Futurum, "Coherent Q4 FY 2026 Earnings", 2026-08-19. https://futurumgroup.com/insights/coherent-q4-fy-2026-earnings-1-6t-transceivers-ramp-cpo-revenue-approaches/
- Motley Fool, "Coherent Q4 2026 Earnings Call Transcript", 2026-08-19. https://www.fool.com/earnings/call-transcripts/2026/08/19/coherent-cohr-q4-2026-earnings-call-transcript/
- Futurum, "Coherent Q1 FY 2026", 2025-11. https://futurumgroup.com/insights/coherent-q1-fy-2026-shows-strong-datacenter-comms-momentum
- Cignal AI, "OCS Market to Top $8 Billion by 2030", 2026-07-30. https://cignal.ai/2026/07/ocs-market-to-top-8-billion-by-2030/
- Cignal AI, "Google's AI Buildout Drives Higher OCS Forecast", 2026-02-02. https://cignal.ai/2026/02/googles-ai-buildout-drives-higher-optical-circuit-switching-forecast/
- cnyes (citing Citi), merchant OCS opportunity, ~2026-09. https://hao.cnyes.com/post/271223
- ChinaBaogao, OCS industry report, 2026-07. https://www.chinabaogao.com/market/202607/805608.html
- Global Technology Research, "The Ironwood", 2026 (undated). https://globaltechresearch.substack.com/p/the-ironwood-an-introduction-to-google
- Longbridge, Palomar pricing post (low quality), 2026. https://longportapp.cn/topics/39074922
- Yole Group, "DiCon announces two value-focused OCS", 2026. https://www.yolegroup.com/industry-news/dicon-announces-two-value-focused-optical-circuit-switches-ocs-for-ai-data-centers-and-celebrates-40-years-of-photonics-excellence/
- 247 Wall St, "Google TPU volume could triple to 8.8 million by 2027", 2026-08-25. https://247wallst.com/investing/2026/08/25/google-tpu-volume-could-triple-to-8-8-million-by-2027/
- Google, "Ironwood" (Hot Chips 2025), 2025-08 [STALE 2025-08]. https://hc2025.hotchips.org/assets/program/conference/day2/61_Google_Ironwood-Final.pdf
- Tom's Hardware, "Nvidia's Kyber rack for Rubin Ultra slips to 2028", 2026. https://www.tomshardware.com/pc-components/gpus/nvidias-kyber-rack-for-rubin-ultra-slips-to-2028
- Huber+Suhner, "Half-Year Report 2026", 2026-08-18. https://reports.hubersuhner.com/2026/hyr/?p=4292
- Sai Microelectronics, "2026 Half-Year Report", 2026-08-27. https://static.cninfo.com.cn/finalpage/2026-08-27/1225514709.PDF
- Dempa Shimbun, Tower-Salience OCS, 2026-02-27. https://dempa-digital.com/?p=709359
- Lumentum/BusinessWire, "Lumentum Announces R64 OCS", 2025-09-24 [STALE 2025-09]. https://www.businesswire.com/news/home/20250924536510/en/Lumentum-Announces-R64-Optical-Circuit-Switch-for-AI-Data-Centers
- PIC Magazine (citing LightCounting), "The evolving role of optics in AI clusters", date unclear [STALE]. https://picmagazine.net/article/120678/The_evolving_role_of_optics_in_AI_clusters
- Yahoo Finance, "Coherent shares rise 3.5%", 2026-10. https://finance.yahoo.com/technology/ai/articles/coherent-shares-rise-3-5-104542372.html
- Chipstrat, "Lumentum and the laser bottleneck", 2026-03/04. https://www.chipstrat.com/p/lumentum-and-the-laser-bottleneck
- 10jqka, Guosen OCS commentary, 2026-09-08. https://news.10jqka.com.cn/20260908/c679715397.shtml
- S&P Global Market Intelligence, "Alphabet post-Q: AI growth accelerates", 2026-07. https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/alphabet-postq-ai-growth-accelerates-as-spending-weighs-on-cash-flow
- Rivkin, Alphabet Q2-26 FCF, 2026-07. https://rivkin.com.au/?p=37098
- LightCounting, "July 2026 Cloud Data Center Optics", 2026-07. https://lightcounting.com/newsletter/en/july-2026-cloud-data-center-optics-385
- LightCounting, "April 2026 Ethernet, optical and scale-up switches", 2026-04. https://lightcounting.com/newsletter/en/april-2026-ethernet-optical-and-scale-up-switches-for-cloud-data-centers-378
- Crypto Briefing, "Eoptolink inventory surge", 2026-08. https://cryptobriefing.com/eoptolink-inventory-surge-ai-demand/
- Tiger Brokers, Nvidia copper remarks, 2026. https://www.itiger.com/news/1122847052
- Counterpoint Research, "From Blackwell to Feynman", 2026. https://counterpointresearch.com/cn/insights/from-blackwell-to-feynman-analyzing-nvidias-optics-roadmap
- The Next Platform, "Nvidia sees the light on silicon photonics", 2026-03-02. https://www.nextplatform.com/connect/2026/03/02/nvidia-sees-the-light-on-silicon-photonics-and-maybe-optical-switching/4093099
- KuCoin (summarizing SemiAnalysis), CPO delays, 2026. https://www.kucoin.com/news/flash/semianalysis-report-delays-nvidia-tech-sparks-market-volatility?lang=en_US
- TIKR, "Lumentum stock has more than doubled in 2026", 2026. https://www.tikr.com/blog/lumentum-stock-has-more-than-doubled-in-2026-the-ai-optics-trade-explains-why
- 247 Wall St, "Lumentum still down over 90 days", 2026-08-13. https://247wallst.com/investing/2026/08/13/lumentum-still-down-over-90-days-a-respected-analyst-sees-22-gains-ahead-following-sharp-upturn?.tsrc=rss
- Eastmoney Caifuhao, Accelink OCS, 2026-04-18. https://caifuhao.eastmoney.com/news/20260418032242866813430
- EET-China, 孛璞半导体 SiPh OCS launch, 2026-09. https://www.eet-china.com/info/75536.html
- Interactive Brokers, LITE/COHR price snapshots and company-connections digests, 2026-10-14. (MCP data; no public URL)


---

### 4.5 — #5 · HAMR nearline HDDs, >=30 TB (drive-level revenue)
*Megatrend: AI/cloud data storage (nearline capacity tier) | 2026 -> 2030 revenue: $4.3-5.6B -> $20-52B | CAGR: ~42-80% (central ~61%) | Growth mix: ~110% exabyte volume / ~-10% $/TB price (per drive ~84% units / ~16% ASP) | Confidence: medium*

**Definition.** In: finished 3.5-inch nearline HDDs using laser-heated heads on FePt media at >=30 TB, CMR or SMR. That covers Seagate Mozaic 3+/4/5, WDC HAMR (from 1H CY2027) and any Toshiba HAMR, sold to any customer at drive value. Out: PMR/ePMR/UltraSMR/MAMR drives (including WDC 40 TB ePMR), drives below 30 TB, standalone HAMR components, SSD/tape and system margin. Sub-30 TB HAMR SKUs inside Seagate EB have <3% effect [E].

**Value-chain path.** AI/cloud data growth -> object/cold storage (~80% of hyperscale data on HDD, WDC Aug 2026 [G]) -> nearline HDD tier -> recording transition (PMR/ePMR/MAMR -> HAMR) -> **HAMR nearline drives**.

**Drill-down decision.** Kept at drive level.
- (a) >=40 TB-only would show a ~110-130% CAGR [E], but it is one product generation, superseded by Mozaic 5 before 2030. Rejected as a definitional artefact.
- (b) Non-Seagate HAMR starts from ~$0 and is a company slice. Rejected.
- (c) Merchant components (Hoya glass, Resonac media, TDK heads, Sony lasers) track platters (~45-50%/yr [E]) on falling unit ASPs (Phase-1 research: glass ~33%, lasers ~27% CAGR [E]). TrendForce says WDC "relies on externally sourced components" for HAMR [3P], which contradicts the draft's "largely captive" premise. That layer may be larger than assumed: flagged, not sized.

Caveat: by 2030 this is ~70-75% of a ~$46B nearline pool, and ~3/4 of its growth is share shift cannibalizing PMR at the same vendors. It is an S-curve, not net new demand.

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $4.3-5.6B (central ~$4.9B) [E] | $20-52B (central ~$33B) [E] | ~42-80% (central ~61%) [E] |
| HAMR EB / share of nearline EB | ~296-355 EB (~17%) [E] | ~2.0-3.8 ZB (60-86%, central 2.66 ZB / 72%) [E] | ~70%/yr |
| Effective $/TB | ~$15.2 [E] | $10.1-13.7 (central $12.5) [E] | ~-5%/yr |
| HAMR drives / ASP | ~8.9-10.2M / ~$510 [E] | ~37-62M (central ~48M) / ~$700 [E] | ~49% / ~8%/yr |

CAGR = (S2030/S2026)^(1/4) - 1:
- Central: 33/4.9 gives **61.1%**.
- Headline range (2026 central vs the 2030 range): 20/4.9 gives 42.1%; 52/4.9 gives 80.5%.
- Consistent pairing: 20/4.3 gives 46.9%; 52/5.6 gives 74.6%.
- Cross-paired envelope: 37.5-86.5%. Rejected, because the 2026 error is measurement error and does not move with 2030.

- **Volume vs price:** HAMR EB grows ~70%/yr and $/TB falls ~5%/yr. In log terms EB is ~110% of revenue growth (industry growth ~36%, share shift 17% -> 72% ~75%) and price ~-10%. Per drive, units are ~84% and ASP ~16%, and the ASP gain is purely TB per drive (33.6 -> 56 TB). The share shift is durable; the price base is not. 2026 embeds ~10-17% shortage pricing [E]: Seagate DC $/TB rose +9.8% YoY to $14.9 [E from R], and TrendForce has HDD $/GB moving from $0.012-0.013 to $0.015-0.016 [3P]. That conflicts with the CFO's "flat to slightly up" [G]. Reverting to $10.5/TB cuts 2030 ~16%.
- **Top-down:**
  - 2026 industry nearline EB is ~1.82-1.95 ZB [E]: Seagate ~785-830 EB (Mar ~176 derived from the 10-K, Jun 195 [R], Sep/Dec 200-235 [E]), WDC cloud ~830-870 [E] and Toshiba ~200-230 [E].
  - Seagate HAMR share by quarter: Mar 28-33%, Jun 35-39%, Sep 41-46%, Dec 46-52% [E]. The 40% (exit FY26) and 50% (end-2026) figures are exit rates [G], not quarter averages.
  - Seagate DC $/TB: $14.1 Mar, $14.9 Jun ($2.9B / 195 EB [R]), $15.6-16.4 implied for Sep by the $4.1B guide [G]. The revenue-weighted average is ~$15.5, less ~3% for non-nearline DC revenue.
  - 2026: 323 EB x $15.5 x 0.97 = **$4.9B**. Range: 296 x $15.0 x 0.97 = $4.3B to 355 x $16.2 x 0.97 = $5.6B.
  - 2030: 3.7 ZB x 72% x $12.5 = **$33.3B**. Low: 3.3 x 60% x $10.1 = $20B. High: 4.4 x 86% x $13.7 = $52B.
  - Industry EB: guided mid-20s% [G] gives 1.87 x 1.25^4 = 4.6 ZB of demand, but flat units (~75-80M/yr) x 45-55 TB cap supply at 3.3-4.4 ZB [E]. The central is trimmed from 3.85 to 3.7 ZB for the bear's QLC substitution. HAMR share: Seagate ~43% of EB at 92-98%, WDC ~44% at 45-88%, Toshiba ~13% at 0-30% [E].
- **Bottom-up:**
  - 2026: Seagate CY26 revenue $15.0-15.6B ($3.11B [R] + $3.63B [R] + $4.1B [G] + $4.2-4.7B [E]) x DC 80-82% x nearline ~97% x revenue-weighted HAMR 38-44% = **$4.4-5.5B**. WDC and Toshiba contribute ~0.
  - 2030 Seagate: 28-31M units x 49-56 TB x 92-98% = 1.26-1.71 ZB. Units are ~6.7-7M/qtr per Wedbush [3P], not the draft's 7.5-8M; Mozaic 5 at 50 TB is in volume ~2028.
  - 2030 WDC: 32-34M x 45-58 TB x 45-88% = 0.65-1.73 ZB.
  - 2030 Toshiba: 0.45-0.65 ZB x 0-30% = 0-0.2 ZB. Its doubling is on an EB basis (記憶容量ベース, Nikkei [R]), not units.
  - Total: 1.9-3.6 ZB, central ~2.68 ZB ≈ 48M drives at ~56 TB x $12.5 = **$33.5B**.
- **Reconciliation:**
  - The 2026 estimates overlap, both anchored on reported Seagate data.
  - The 2030 centrals agree largely by construction (shared $/TB and TB/drive roadmaps); only the unit cap (~3.8 ZB) is independent.
  - Versus the draft, 2026 is ~4% lower (non-nearline deduction; exit rates not averages). 2030 drops from $40B to $33B: 56 TB rather than 62 TB per drive, no Toshiba unit double count, Toshiba HAMR at 0-30% rather than 15-50%, and 3.7 ZB rather than 4.2 ZB.
  - The low end widens from the fact-check's $22B P10 to $20B because the bear puts ~25% on ≤$21B and the evidence is not decisive; the headline is ~P20-P90.
  - Pool check: $46B total nearline in 2030 vs ~$29B in 2026 (+12%/yr [E]). HDD revenue has historically been ~flat in nominal terms (prior knowledge), so even the central is price-benign.

#### Demand drivers and catalysts
- Drivers:
  - AI data retention; mid-20s% EB growth guided [G, vendor-sourced].
  - Big-4 capex ~$725B in 2026, >$1T for 2027 [3P, not re-verified].
  - Unit-capacity discipline makes HAMR the main EB lever.
  - Allocation into CY2028 at Seagate; WDC LTA talks to CY2029-31 [G].
  - eSSD contract prices +23-28% QoQ in 4Q26 [3P].
- **Seagate FQ1 FY27, late Oct 2026 (scheduled):** guide $4.1B ±$0.1B and $7.30 EPS [G]. Model: HAMR 41-46% of nearline EB, DC $/TB $15.6-16.4.
- **Seagate HAMR >=50% of nearline EB, and Mozaic 4 >=50% of HAMR EB, by end-CY2026** [G]: on track, but PMR demand is lingering. The "70%" figure has an ambiguous metric and is not used.
- **WDC qualification (two hyperscalers incl. Meta [R, IBKR]) -> 44 TB volume 1H CY2027, 50 TB 2H CY2027** [G]: "on track", completion not announced. 40 TB ePMR goes above 50% of WDC nearline bits by FQ3 FY27 [G].
- **Mozaic 5 (50 TB) qualification, late CY2027** [G, single summary].
- **Toshiba:** first shipments from the new Laguna line 2026-10-02 [R]; EB-basis doubling by FY2027, ending Mar 2028 [R]. HAMR timing is single-source, **unverified**.
- **TDK HAMR heads ~2028** [G]; hyperscaler 2027 capex guides, Jan-Feb 2027.

#### Supply side
- **Suppliers and shares:** Seagate holds ~99-100% in 2026 [E]. 2030 central: Seagate ~55% (45-70%), WDC ~42% (25-50%), Toshiba 0-7% [E]. TrendForce sees Seagate as the largest HDD supplier by 2028, with WDC's HAMR ramp "the key variable" [3P].
- **Capacity and lead times:** EB comes from areal density, not new lines, except Toshiba's ¥60B (~$380M) Philippine expansion [R]. Components:
  - Resonac media: 160M -> 230M disks/yr, from 2027 and 2029+ [G].
  - Hoya: ¥50B Vietnam plant [R]; full output ~FY2028 unverified.
  - TDK HAMR heads ~2028 [G]; Sony laser doubling [STALE 2025-06].
  - Lead times >52 weeks [STALE 2025-09]; no 2026 figure.
- **Qualification barriers:** ~12-24 months per hyperscaler platform, plus 6-12 per capacity point [E]. Laser/NFT heads and FePt-on-glass are IP-heavy; HAMR yields are still below PMR [G].
- **Geographic concentration:** assembly in Thailand, Malaysia, the Philippines and China (prior knowledge). Glass and media come from SE Asia/Singapore, lasers from Japan or in-house. No Chinese drive maker. ~89-90% of demand is DC/cloud [R].

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| Seagate Technology | STX / Nasdaq | Sole volume HAMR maker; in-house heads, media, photonics | ~28-37% of CY2026 [E]; ~85-95% by 2030 [E]; undisclosed |
| Western Digital | WDC / Nasdaq | Second entrant (44 TB 1H27, 50 TB 2H27, ~100 TB 2029 aspirational) | ~0% 2026; ~30-85% by 2030 [E] |
| Toshiba Electronic Devices & Storage | Unlisted | Third maker; MAMR now, HAMR timing unverified | 0% 2026; small by 2030 [E] |
| HOYA | 7741 / TSE | Dominant glass substrates; HDD substrates +~25% YoY 1Q26 [R] | <~8% [E, unverified] |
| Resonac | 4004 / TSE | Merchant media, incl. HAMR for Toshiba | <~5% [E] |
| TDK | 6762 / TSE | Merchant heads; HAMR ~2028 | ~0% today [E] |
| Sony Group | 6758 / TSE | Reported HAMR laser supplier | <1% [E] |
| Gebijia | 920438 / BSE | Chinese glass entrant, 1H27 target | ~0% [unverified] |

#### Bear case and key risks
- **Technology substitution:**
  - Non-HAMR stretching. WDC ships 40 TB ePMR and guides UltraSMR to ~60% of its EB by end FY27 [G]; Toshiba plans a 40 TB MAMR in 2027 [G]. The bear assumes WDC HAMR at only 30-45% of its 2030 EB and Toshiba at 5-15%, so industry HAMR share is 50-60%. A 12-month WDC slip alone removes ~0.7 ZB (~$8-9B) [E].
  - QLC. 245 TB+ drives arrive before end-2026 [G], 2Tb QLC dies are in mass production in 2026, and QLC goes from 18% to 38% of eSSD capacity in 2026-27 [3P]. QLC also uses ~30% less power [3P, STALE 2025-09]. A 2028-29 NAND glut (QLC $/TB -40-60%) would cut HDD's share of new hyperscale EB from 80-85% to 65-70% and leave nearline EB 15-20% below path [E]. The quoted $/TB gap ranges from 3x to 22x (conflicting, low quality).
- **Capex cuts:** a 20-30% cut in 2028 from >$1T in 2027 would mean nearline EB -15-25% and $/TB -10-20% as LTAs, historically not take-or-pay, are renegotiated. Seagate revenue fell ~37% in FY2023 (prior knowledge, not re-verified). 2030 nearline EB would be ~3.0-3.2 ZB, and the cut alone gives ~$28-30B (3.4 ZB x 77% x ~$11) [E].
- **Chinese capacity:** indirect only.
  - YMTC plans >100% wafer-capacity growth, with Phase 3 from ~end-2026 [3P], and ranks #3 by NAND bits [3P]. It is entity-listed (prior knowledge), but localization could shift China (~15-25% of demand, unverified) to QLC.
  - Gebijia glass (unverified) could cheapen Toshiba's supply chain.
  - STX fell -4.3% and -4.5% on 10-13/14 on China fears [R/3P].
  - Bear impact: -0.1 to -0.3 ZB and -$0.5-1.0/TB, or **-$3-5B** in 2030 [E].
- **Double-ordering / pull-forward:** the signs are sell-outs through 2028, lead times "up to two years" (low quality, unverified), contract prices ~+10% QoQ in 2Q26 (unverified), CSPs raising eSSD forecasts because HDDs were unavailable [3P], and lingering PMR demand, which suggests shortage buying. The bear assumes 5-10% of 2026-27 EB is stock-building that unwinds over 2-4 quarters in 2028 [E], just as WDC HAMR, Toshiba's doubling and Resonac's lines land. Hyperscaler inventory is undisclosed.
- **Already priced in?** Yes.
  - STX went from ~$100 (Oct 2024) to a $1,145 high in June 2026 and was ~$691-714 on 10-14 (-38%), including -10.2% on ~5x volume on the Nikkei Toshiba report [R, IBKR].
  - WDC is down ~55% from its peak [R].
  - STX trades at ~20-24x FY27 EPS against ~8-15x historically (share count unverified) [E]; consensus targets are $986-1,142 [3P].
  - The revenue math is unaffected, but the investment asymmetry is gone.
- **Other risks:**
  - Mean reversion leaves 2030 total nearline flat at ~$29B (3.1 ZB x $9.5).
  - The 2026 base may be 5-15% high if HAMR sells below the DC-average $/TB (unverified).
  - No independent HAMR field-reliability data (Seagate's 2.5M-hour MTBF claim [STALE 2024-04]).
  - Tariffs; vendor-sourced demand forecasts.
- **Bear-case numbers:**
  - 2030 size: **$13-21B, central ~$16B** (3.1 ZB x 55% x $9.5/TB ≈ 1.7 ZB ≈ 31M drives) [E].
  - CAGR: **~27-45%, central ~34%**, with (16/4.9)^(1/4)-1 = 34.4%.
  - Probability: **~25%**, including a ~10% tail at ≤~$12B (2.7 ZB x 45% x $8.5 ≈ $10B, ~20% CAGR). The bear would put the central at $28-32B.
  - First warning sign: nearline spot/channel prices and lead times rolling over in TrendForce/DigiTimes monthlies, which lead contract prices by 1-2 quarters.

#### Leading indicators to watch (next 2-4 quarters)
1. Seagate DC revenue/DC EB in FQ1-FQ2 FY27 (Oct 2026, Jan 2027): $14.9 in Jun, ~$15.6-16.4 implied for Sep. A flat or falling QoQ figure while EB grows means shortage pricing is ending.
2. Seagate HAMR share of nearline EB (model: 41-46% in Sep, ~50% exiting Dec), and whether "allocated into CY2028" survives.
3. WDC HAMR qualification completion and first revenue in 1H CY2027, against its ePMR/UltraSMR bit mix.
4. TrendForce eSSD/QLC contract prices turning negative QoQ (the substitution tell), plus nearline spot prices and lead times.
5. Toshiba's Laguna ramp and HAMR sampling; Hoya substrate growth; Resonac's 2027 lines; TDK HAMR head sampling.

#### Confidence and biggest unknown
Confidence is medium. The 2026 base is derived for a single company that does not disclose HAMR revenue (~±12%). The biggest unknown is **2030 $/TB**. It could hold at ~$13-14 under duopoly discipline, or fall to ~$9.5-10 if WDC HAMR, Toshiba's EB doubling, a 2028 digestion and cheaper QLC coincide. That alone swings 2030 from ~$20B to ~$50B. The second unknown is WDC's HAMR conversion pace versus ePMR/UltraSMR stretching.

#### Sources
- Seagate, "Form 8-K FY26 Q4 press release", 2026-07-28. https://www.sec.gov/Archives/edgar/data/0001137789/000113778926000153/stxq42026pressreleasefinan.htm
- Seagate, "Form 10-K FY2026", 2026-08. https://www.sec.gov/Archives/edgar/data/0001137789/000113778926000159/stx-20260703.htm
- Seagate IR, "Q4 FY2026 earnings call corrected transcript", 2026-07-28. https://s24.q4cdn.com/101481333/files/doc_financials/2026/q4/STX-US-CORRECTED-TRANSCRIPT-Seagate-Technology-Holdings-PlcSTXUS-Q4-2026-Earnings-Call-28-ET-PM-27-07-2026-2026-07-27-0.pdf
- Seagate IR, "Q2 FY2026 corrected transcript", 2026-01-27. https://s24.q4cdn.com/101481333/files/doc_financials/2026/q2/CORRECTED-TRANSCRIPT_-Seagate-Technology-Holdings-Plc-STX-US-Q2-2026-Earnings-Call-27-January-2026-5_00-PM-ET.pdf
- MarketBeat, "Seagate Technology Q4 earnings call highlights", 2026-07-28. https://www.marketbeat.com/instant-alerts/seagate-technology-q4-earnings-call-highlights-2026-07-28/
- Nasdaq, "Seagate Technology Q4 earnings call highlights", 2026-07-29. https://www.nasdaq.com/articles/seagate-technology-q4-earnings-call-highlights-ai-storage-demand
- Motley Fool, "Seagate Q3 2026 earnings call transcript", 2026-04-28. https://www.fool.com/earnings/call-transcripts/2026/04/28/seagate-stx-q3-2026-earnings-transcript/
- Nasdaq, "Western Digital Q4 earnings call highlights", 2026-08-05. https://www.nasdaq.com/articles/western-digital-q4-earnings-call-highlights
- MarketBeat, "Western Digital investor day HAMR roadmap", 2026-02-04. https://www.marketbeat.com/instant-alerts/western-digital-investor-day-hamr-roadmap-ai-data-center-shift-and-new-4b-buyback-plan-2026-02-04/?.tsrc=rss
- Blocks & Files (citing Nikkei), "Distant third HDD maker Toshiba spending $380 million to catch up", 2026-10-06. https://www.blocksandfiles.com/disk/2026/10/06/distant-third-hdd-maker-toshiba-spending-380-million-to-catch-up/5301322
- Xenospectrum, "Toshiba AI HDD capacity expansion FY2027", 2026-10. https://xenospectrum.com/toshiba-ai-hdd-capacity-expansion-fy2027/
- mreport.co.th, "Toshiba HAMR HDD 40TB mass production 2028", 2026-02. https://www.mreport.co.th/en/news/industry-movement/102-toshiba-hamr-hdd-40tb-mass-production-2028
- TrendForce, "Report RP261007HN (HDD supply)", 2026-10-07. https://www.trendforce.com/research/download/RP261007HN
- TrendForce, "4Q26 Memory Price Forecast (RP260924PL)", 2026-09-24. https://www.trendforce.com/research/download/RP260924PL
- TrendForce via DRAMeXchange, "Market View (QLC share, HDD $/GB)", 2025-2026 (exact date unverified). https://www.dramexchange.com/WeeklyResearch/Post/2/12492.html
- TrendForce via Economic Daily News, "HDD price item", 2026-01 (undated). https://money.udn.com/money/amp/story/5607/9070145
- TrendForce, "Nearline HDD shortage" [STALE 2025-09], 2025-09-15. https://www.trendforce.com/presscenter/news/20250915-12714.html
- Xenospectrum / Newswitch, "AI nearline HDD and Japanese components", 2026-07. https://xenospectrum.com/ai-nearline-hdd-japan-components/
- Statementdog, "HDD industry report", 2026. https://statementdog.com/industry_reports/45
- DigiTimes, "Sony to double HAMR laser capacity" [STALE 2025-06], 2025-06-17. https://www.digitimes.com/news/a20250617PD210.html
- Eastmoney Caifuhao, "Gebijia glass substrate commentary", 2026-04-29. https://caifuhao.eastmoney.com/news/20260429234925671234530
- TechRadar Pro, "Solidigm confirms 245 TB SSDs before end of 2026", 2026. https://www.techradar.com/pro/solidigm-confirms-245-tb-ssds-set-to-launch-before-end-of-2026
- C114, "YMTC capacity", 2026-06-04. https://m.c114.com.cn/w16-1311613.html
- Sina Finance, "YMTC new fab plan", 2026-04-15. https://finance.sina.com.cn/tech/roll/2026-04-15/doc-inhupvfe0971242.shtml?cref=cj
- MarketBeat, "Seagate stock falls 4.5%", 2026-10-14. https://www.marketbeat.com/instant-alerts/price-seagate-technology-nasdaq-stx-stock-falls-45-time-to-sell-2026-10-14/
- 24/7 Wall St., "Rapid growth, high volatility ... Seagate", 2026-10-13. https://247wallst.com/investing/2026/10/13/rapid-growth-high-volatility-and-near-50-upside-confound-seagate-technology-investors/
- CoreTechTips (citing TrendForce), "Enterprise SSD Q4 2026 demand, QLC", 2026-09. https://coretechtips.com/news/enterprise-ssd-q4-2026-demand-qlc-trendforce
- DatacenterDisk, "Hard drive lead time crisis 2026" (low-quality aggregator), 2026. https://datacenterdisk.com/reports/hard-drive-lead-time-crisis-2026
- TradingKey, "Market movers: STX", 2026-10-13. https://www.tradingkey.com/news/market-movers/262214112-market-movers-stx-20261013
- Seagate blog, "HAMR reliability" [STALE 2024-04]. https://www.seagate.com/blog/seagate-hamr-solutions-deliver-industry-leading-reliability/
- AI Weekly, "Q1-2026 hyperscaler capex summary", 2026-04-30. https://aiweekly.co/node/8566
- Interactive Brokers, "Company connections and price history for STX, WDC, Hoya (7741), PSTG", 2026-10-14. (MCP data; no public URL)


---

### 4.6 — #6 · SF6-free high-voltage (>52 kV) switchgear and circuit breakers
*Megatrend: Grid build-out and electrification, forced by EU F-gas regulation | 2026 -> 2030 revenue: $0.5-1.2B -> $2.5-5.0B | CAGR: ~37-63% (central ~48%) | Growth mix: ~95-100% volume / ~0-5% price | Confidence: medium on direction and timing, low on dollar size*

**Definition.**
- **In:** new-build AC switchgear rated **>52 kV** that uses no SF6 for insulation or interruption. In practice this is the 72.5 kV class and up; the Mar 2025 EU corrigendum moved 52 kV-rated gear into the MV class [R]. Japanese 66/77/84 kV classes count.
  - Products: GIS bays, GIL, dead-tank and live-tank breakers, and hybrid modules. Instrument transformers and disconnectors count only when sold inside a bay.
  - Technology families: (a) vacuum interrupter plus clean/dry air or CO2-O2 (Siemens Energy Blue, Mitsubishi Electric, Meidensha, Toshiba, Hitachi CO2 live-tank); (b) C4-FN/C5-FK mixtures (GE Vernova g3, Hitachi EconiQ GIS, Hyosung, Pinggao).
  - Measure: OEM ex-works revenue, worldwide.
- **Out:**
  - MV SF6-free gear.
  - SF6 and SF6 mixtures.
  - Retrofill or upgrade of installed GIS (e.g. CIGRE 2026 B3-10738, 420 kV C4-FN).
  - SF6 recovery services, HVDC DC-GIS, and EPC/installation.
  - Stand-alone instrument transformers and bushings.
  - Merchant vacuum interrupters and gas.

**Value-chain path.** Grid and electrification capex -> transmission and sub-transmission substations (110-420 kV; renewables, interconnectors, data-center connections) -> HV switchgear and breakers -> GIS / GIL / dead-tank and live-tank -> **SF6-free variants (vacuum + clean air; C4-FN/C5-FK mixtures)**. Critical upstream inputs:
- HV vacuum interrupters: Siemens Energy Berlin; Japanese makers in-house.
- C4-FN gas: 3M is exiting; no replacement producer verified.
- Type-test labs: KEMA, CESI, IPH, KERI.

**Drill-down decision.** I kept the parent level.
- **By voltage.** The 52-145 kV band grows at about the parent rate. The >145 kV slice is faster but small: $0.05-0.16B in 2026 [E], below the floor. Its 2030 central is ~$0.5B, so a path to $1B+ needs the 35% penetration high case.
- **By technology.** The fluorine-free subset probably grows faster. GWP>=1 gear is legal at EU 52-145 kV after 2028 only by derogation, so C4-FN (GWP well above 1) loses share there. But no OEM discloses the split, so the subset cannot be sized.
- **HV vacuum interrupters as a stand-alone niche:** <$0.1B [E].

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $0.5-1.2B, central ~$0.70B [E] | $2.5-5.0B, central ~$3.4B [E] | 37-63%, central ~48% [E] |
| Bear case | same base | $1.7-2.6B, central ~$2.1B [E] | ~20% on bear's base; ~32% on $0.70B base |

The CAGR math uses (S2030/S2026)^(1/4) - 1:
- Central: (3.4/0.70) = 4.86x, giving **48.5%**.
- Core band, central base against the 2030 range: (2.5/0.70) gives 37.5%; (5.0/0.70) gives 63.5%.
- Correlated pairs (base and 2030 errors share price/mix assumptions): low with low (2.5/0.5) gives 49.5%; high with high (5.0/1.2) gives 42.9%.
- Cross-paired envelope: (2.5/1.2) gives 20.1%; (5.0/0.5) gives 77.8%.
- Part of the CAGR is a small-base effect from starting in the pre-ban year.

**Volume vs price.** Log decomposition of the 4.86x growth (ln 1.58) [E]:

| Leg | Assumption | Multiplier | Share of log growth |
|---|---|---|---|
| SF6-free share substitution | ex-China SF6-free value share ~4.5% -> ~17% | ~4.3x | ~92% |
| HV position growth | ~3%/yr | 1.13x | ~7.5% |
| General HV price | ~2%/yr | 1.08x | +5% |
| Premium compression | 15% -> 7% | 0.93x | -4.6% |

- Net: **volume ~99.5%, price ~+0.5%**. Plausible price range is +5% (fact-check) to negative: the bear case has the premium collapsing to 0-5%, shortage pricing unwinding, and a GIS-to-AIS mix shift, together 0.85-0.92x.
- The draft's legs (3.93x) did not multiply to its own total (4.21x); this table fixes that.
- The growth is forced substitution, not shortage pricing, so it is durable. But the base-year price includes 2024-26 HV shortage pricing.

**Top-down.** Formula: positions x SF6-equivalent price per position (= value pool) x SF6-free value share x premium. All own estimates [E].

*2026:*

| Region | Positions | $/position | Pool | SF6-free share | Premium | Result |
|---|---|---|---|---|---|---|
| Europe 52-145 kV | ~7,000 | ~$0.36M | $2.5B ($2.2-2.8B) | 15% (10-22%) | 1.15 | **$0.43B** ($0.24-0.74B) |
| Europe >145 kV | ~2,400 | ~$1.0M | $2.4B | 3.5% (2-5%) | 1.15 | **$0.10B** ($0.05-0.16B) |
| North America | ~9,000 | ~$0.44M | $4.0B | 1.3% (0.8-2%) | 1.15 | **$0.06B** ($0.03-0.10B) |
| Japan | ~3,000 | ~$0.47M | $1.4B | 3.5% (2-5%) | 1.10 | **$0.05B** ($0.03-0.09B) |
| RoW ex-China | ~15,000 | ~$0.33M | $5.0B | 0.5% (0.3-1%) | 1.15 | **$0.03B** ($0.01-0.07B) |
| China | ~25,000 | n/a | ~$9.5B | ~0.1% | n/a | **$0.01B** |

- **Total: $0.68B ($0.36-1.18B).**

*2030:*

| Region | Positions | $/position | Pool | SF6-free share | Premium | Result |
|---|---|---|---|---|---|---|
| Europe 52-145 kV | ~8,000 | ~$0.39M | $3.1B ($2.6-3.8B) | **72%** (62-82%) | 1.07 (1.02-1.12) | **$2.39B** ($1.64-3.49B) |
| Europe >145 kV | ~2,800 | ~$1.07M | $3.0B | **15%** (6-35%) | 1.12 | **$0.50B** ($0.16-1.60B) |
| North America | n/a | n/a | $5.2B | 3.5% (2-6.5%) | 1.10 | **$0.20B** ($0.10-0.43B) |
| Japan | n/a | n/a | $1.6B | 8% (5-15%) | 1.10 | **$0.14B** ($0.08-0.30B) |
| RoW ex-China | n/a | n/a | $6.5B | 1.5% (0.8-3%) | 1.15 | **$0.11B** ($0.05-0.28B) |
| China | n/a | n/a | $12B | 0.6% (0.3-1.5%) | n/a | **$0.07B** ($0.03-0.21B) |

- **Total: $3.42B ($2.07-6.30B).**
- Unit check, Europe 52-145 kV: 8,000 x 72% x $0.39M x 1.07 = $2.40B.
- How the key inputs were set:
  - **72% penetration:** between the fact-check's 74% and the bear case's 62-75%. Both reflect that the UK and Switzerland are not bound, plus derogations, >50 kA ratings and the pre-Mar-2024 contract tail.
  - **15% above 145 kV:** between the fact-check's 20% and the bear case's ~9%.
  - **~8,000 positions:** between the draft's 8,500 and the bear case's flat 6,500-7,000.

**Bottom-up.**

*2026 [E] (fact-check method adopted):*

| Supplier | Basis | Result |
|---|---|---|
| Siemens Energy Blue | 1,300-2,000 units x $0.10-0.24M | $0.13-0.48B (central 1,600 x $0.17M = $0.27B) |
| Hitachi EconiQ | 650-1,100 deliveries x $0.13-0.28M | $0.08-0.31B (central $0.17B) |
| GE Vernova g3 | | $0.06-0.20B |
| Japanese makers | | $0.025-0.08B |
| Korean makers | verified volumes are tens of breakers | $0.003-0.02B |
| Chinese makers | | $0.004-0.025B |

- **Sum: $0.30-1.12B, central $0.63B.**
- The Siemens unit range builds on the >4,150 cumulative Blue units delivered (company slide via UNEP, Oct 2025; not re-verified).
- The Hitachi delivery range comes from >4,000 EconiQ units ordered cumulatively [G, Aug 2026].

*2030 (OEM conversion of HV switching revenue; the EUR denominators are own estimates and unverified):*

| Supplier | Basis | Result (central) |
|---|---|---|
| Siemens Energy | (Europe EUR1.8-2.5bn x 40-60% + non-Europe EUR2.7-3.5bn x 4-10%) x 1.15 USD/EUR | $0.95-2.13B ($1.49B) |
| Hitachi Energy | Europe $1.8-2.4B x 30-45% + RoW $4.2-5.6B x 2-6% | $0.62-1.42B ($0.98B) |
| GE Vernova | Europe $0.9-1.2B x 25-50% + $0.03-0.10B | $0.26-0.70B ($0.46B) |
| Japanese makers | | $0.10-0.30B |
| Korean makers | | $0.10-0.30B |
| China and others | | $0.05-0.30B |

- **Sum: $2.08-5.14B, central $3.41B.**
- Capacity check: conversion runs on existing GIS and breaker lines. The binding inputs are ≥145 kV vacuum interrupters, 245-420 kV type tests and C4-FN gas.

**Reconciliation.**
- **2026:** top-down $0.68B vs bottom-up $0.63B, so the central is **$0.70B**. The fact-check's price correction supersedes the draft's $0.95B. The high end is widened to $1.2B because the bear case argues that 2026 deliveries already include units for 2028+ energization, and the Siemens unit count is unverified. A low-quality all-voltage figure ($1.72B in 2025 [3P]) minus MV (~$1.0-1.4B [E]) leaves HV at ~$0.4-0.9B in 2026, consistent with the central.
- **2030:** both methods give ~$3.4B. They are not independent, because the OEM conversion rates rest on the same regulatory logic. The range trims the joint tails ($2.1B / $6.3B) to **$2.5-5.0B**.
- The probability is asymmetric: ~30% below $2.6B (bear case) and ~10% above $5.0B [E].

#### Demand drivers and catalysts
- **EU Reg. 2024/573 Art. 13(9), 52-145 kV ban.** No putting into operation of 52-145 kV, ≤50 kA gear with GWP≥1 from **1 Jan 2028** [R].
  - Derogation cascade (no GWP<1 bid, then GWP<1000; then SF6) with notification to authorities [R].
  - Contracts concluded before 11 Mar 2024 are exempt (ESB; Siemens factsheet; legal wording via secondary sources) [R].
  - Status: firm. EirGrid (Jul 2026) says neither it, ESB nor the EPA can grant a derogation for 110 kV SF6 energized from 2028 [R]. The revenue step falls on 2027-28 deliveries.
- **>145 kV or >50 kA ban from 1 Jan 2032** [R]. Orders from ~2029; 2030 deliveries above 145 kV are mostly voluntary.
- **ECHA universal PFAS restriction.** RAC final opinion 2 Mar 2026; SEAC draft 10 Mar 2026; consultation closed 25 May 2026. SEAC "could not confirm" that the proposed exemptions are justified [R]. SEAC final opinion is expected late 2026 or early 2027. It is a binary outcome for C4-FN/C5-FK.
- **420 kV qualification.**
  - TenneT ordered the EconiQ 420 kV 80 kA live-tank breaker (24 Aug 2026) [R].
  - Siemens Energy 420 kV breaker pilots at Statnett and RTE in 2026 (date unverified).
  - Elia LIFE Blue 420 kV GIS runs to Sep 2028 [R; STALE 2024-10].
- **CIGRE 2026 launches.**
  - GE F35g 170 kV (26 Aug 2026), completing the 72.5-420 kV g3 range [G].
  - EconiQ 300 kV GIS and 245 kV dead-tank breaker, ordered by Hydro One and Wesco [R].
  - Hyosung 420 kV C4-FN GIS [R].
  - HD Hyundai 420 kV is a target only; certification is aimed at H1 2027 [R].
- **Explicitly SF6-free tenders.** Energie AG 110 kV breaker framework (Jul 2026); a Berlin 110 kV GIS tender specifying GWP<1000 [R]; GE wins at Stromnetz Berlin 110 kV (Jul 2026) [R].
- **Japan.** Chubu 550 kV all-SF6-free GIS order (Mar 2026) [R]; Toshiba targets 300 kV CO2/O2 products in FY2028 [G].
- **California.** CARB GIE phase-out by voltage/kA class [STALE 2020-07]; the final class table is unverified.
- **Grid capex.** Siemens Energy Grid Technologies Q3 FY26: orders ~EUR5.4bn (+28%), revenue ~EUR3.6bn (+29%) [R]. Q2 FY26 orders were ~EUR7bn (+41%) [R, not re-verified]. These are group grid figures, not a proxy for this niche.

#### Supply side
- **Suppliers and shares (2026, [E]).** Siemens Energy 35-45%; Hitachi Energy 22-30%; GE Vernova 15-20%; Japanese makers 6-10%; Korean makers 1-2%; Chinese makers 1-3%. The bottom-up centrals give 43/27/19/8/1/2%.
- **Capacity and lead times.**
  - Siemens Berlin vacuum interrupter line: opened Jul 2024, 6,200 m2, EUR60M through 2031 [G; STALE 2024; not re-verified]. Siemens's "only F-gas-free HV switching by 2030" goal is an aspiration [G; STALE 2022].
  - Hitachi is investing >$70M to double Pennsylvania HV capacity [G; STALE 2025-04]. This is not SF6-free specific.
  - Lead times: ~12-24 months at 72.5-145 kV and 24-36+ months at 420 kV [E; unverified].
  - C4-FN gas: 3M is exiting PFAS [R; STALE 2022-12]. Hitachi was qualifying a second source [G; STALE 2023-02]. No commercial replacement producer is verified.
- **Qualification barriers.** IEC 62271 type tests take ~12-24 months per rating [E], and TSOs want 2-5 years of pilot service [E]. No Chinese SF6-free gear ≥72.5 kV is verified as qualified at any EU TSO.
- **Geographic concentration.**
  - Demand: EU/EEA plus UK is ~70-80% of 2026 [E]. North America ~5-10%, Japan ~8-10% [E].
  - Supply: Germany, Switzerland and Sweden ~65-75% [E]. Vacuum interrupters ≥145 kV are effectively single-site (Berlin) [3P].

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| Siemens Energy | ENR / XETRA | Leader in vacuum + clean air, 72.5-145/170 kV; 420 kV in pilot; in-house interrupters | ~0.25-0.95% of group (central ~0.5%); ~1-3% of Grid Technologies [E] |
| Hitachi Ltd (Hitachi Energy) | 6501 / TSE | EconiQ GIS and breakers up to 420/550 kV | ~0.1-0.5% of Hitachi Ltd; ~0.5-2% of Hitachi Energy [E; denominators unverified] |
| GE Vernova | GEV / NYSE | g3 C4-FN GIS 72.5-420 kV; C4-FN licensor | ~0.15-0.5% [E] |
| Mitsubishi Electric | 6503 / TSE | 84 kV dry-air GIS (Kansai) [R; STALE 2024-07] | <0.15% [E] |
| Meidensha | 6508 / TSE | 120 kV dry-air vacuum circuit breaker (Chugoku) [R; STALE 2025-02] | ~0.5-2% [E] |
| Toshiba ESS | private | CO2/O2 300 kV, FY2028 | <0.5% [E] |
| HD Hyundai Electric | 267260 / KRX | 145 kV breakers to Sweden and Finland; Nexel GIS (Denmark) | <1% [E] |
| Hyosung Heavy Industries | 298040 / KRX | 420 kV C4-FN GIS; ~KRW200bn Nordic orders in H1 2026 (all equipment) [R] | <0.5% [E] |
| LS Electric | 010120 / KRX | 170 kV eco GIS | <0.3% [E] |
| Henan Pinggao | 600312 / SSE | 126/145 kV C4F7N GIS pilots | <0.5% [E] |
| China XD | 601179 / SSE | Eco-GIS pilots | <0.3% [E] |

#### Bear case and key risks
- **Technology substitution.** The risk is not a replacement technology. It is legal SF6 and lower-value formats keeping more of the pool:
  - SF6 stays legal above 145 kV until 2032. The bear case uses 6-12% penetration there, not 15-35%.
  - The UK and Switzerland are not bound. AEW's Aug 2026 110 kV GIS tender does not specify the gas [R].
  - Derogations and the pre-Mar-2024 contract tail keep SF6 in service longer.
  - Retrofill of installed GIS gives TSOs Scope-1 progress without new gear.
  - A 10-point GIS-to-AIS shift cuts the blended price ~12-15% [E].
  - C4-FN is derogation-only at EU 52-145 kV, which puts GE g3 share at risk.
- **Capex cuts.** After 2028 the niche is a bet on European position counts.
  - Germany's Reiche plan ties grid expansion to "realistic demand". EWI/BET cut 2030 power demand to 600-700 TWh [STALE 2025-09]. NEP 2023 costs rose from ~EUR324bn to ~EUR440bn [3P].
  - Counter-evidence: the cabinet added 45 grid projects on 29 Apr 2026 [R].
  - A 20-30% European HV capex cut from 2028 would take ~$0.6-0.9B off the 2030 value [E].
  - Data-center exposure: HD Hyundai's Q2 2026 European orders rose 222.5% QoQ on hyperscaler investment [R].
- **Chinese capacity.**
  - Low near-term threat in EU HV: Pinggao's capacity is absorbed domestically (CNY2.09bn State Grid 1000 kV GIS contract, Jun 2026 [R]), and its only European grid foothold is 24 kV MV [R; STALE 2025-05]. Realistic EU DSO entry is 2029-31.
  - Korean entry is the nearer pressure. It could collapse the premium to 0-5% by 2029, a -$0.2-0.4B effect on 2030 [E].
- **Double-ordering / pull-forward.**
  - Revenue is booked at delivery, so the ban step lands in 2026-28, and 2029-30 becomes a plateau for 52-145 kV.
  - SF6 projects are being rushed to energize before 2028 (EirGrid), creating an air pocket after.
  - Group book-to-bill of 1.57 [R] and multi-OEM capacity reservations could unwind as capacity rises, with -5-10% HV pricing in 2028-29 [E].
- **Already priced in?** There is no pure play: every listed exposure is <1-2% of revenue.
  - Siemens Energy trades at a P/E of ~57.8x vs ~27.4x for peers [3P, low quality].
  - IBKR, 14 Oct 2026: ENR ~EUR135, -29% from its EUR191.66 52-week high (+28% YoY); GEV ~$932, -22% from $1,195.49 (+47% YoY) [R].
  - The narrative is consensus, and the stocks react to peak-order fears long before niche data appears.
- **Bear-case numbers.**
  - 2030: **$1.7-2.6B (central $2.1B)** [E].
  - Bear's own CAGR: **~20% (range 12-32%)**, computed on its higher base. (2.1/0.95) gives 21.9%; (2.1/1.1) gives 17.5%; (1.7/1.1) gives 11.5%; (2.6/0.85) gives 32.2%.
  - The same 2030 numbers on the final $0.70B base: (2.1/0.70) gives 31.6% (24.8-38.8%).
  - Probability: **~30%** that 2030 lands at ≤$2.6B. The severe tail ($1.2-1.5B, ~7% CAGR) is 7-10% and needs a deadline delay, a reliability event or a C4-FN ban.
  - The bear case also gives only ~25% odds that $4.0B is reached.
  - **First warning sign:** Siemens Energy Q4 FY26 (~mid-Nov 2026). Watch for Grid Technologies orders below ~EUR5bn a quarter, book-to-bill below ~1.2, or "digesting" language.

#### Leading indicators to watch (next 2-4 quarters)
1. **Siemens Energy Q4 FY26 and Q1 FY27:** Grid Technologies orders and book-to-bill, and any Blue unit update. A run-rate above 2,000/yr confirms the central case; one stuck at 1,000-1,500 supports the bear case.
2. **Hitachi EconiQ cumulative orders:** reaching ≥5,500-6,000 by mid/late 2027, and follow-on 420 kV and 245 kV awards.
3. **PFAS and C4-FN supply:** the ECHA SEAC final opinion and Commission draft on C4-FN/C5-FK exemptions, and any named producer replacing 3M.
4. **EU 110-150 kV tenders and derogations:** the share of tenders requiring GWP<1 vs GWP<1000; derogation notifications (EirGrid/EPA, UBA); Korean wins at German or Nordic TSOs at a discount.
5. **420 kV pilot results:** Statnett and RTE breakers, Elia Vilvoorde, Toshiba 300 kV.

#### Confidence and biggest unknown
**Medium on direction and timing; low on dollar size.**
- Supporting direction: the law is in force and treated as firm; at least five OEMs ship 72.5-145 kV gear; and the CAGR stays ≥~25-30% even in the bear case on the corrected base.
- Biggest unknown: the 2026 base. Unit counts with an undefined mix leave it at ±40-50%, which moves the CAGR ±10-15 pp.
- Second unknown: the PFAS/C4-FN outcome. It swings the 2030 >145 kV slice between $0.16B and $1.6B.
- The single most valuable datum would be a disclosed annual Blue or EconiQ delivery run-rate.

#### Sources
- EUR-Lex, "Corrigendum to Regulation (EU) 2024/573", 2025-03-24. https://eur-lex.europa.eu/eli/reg/2024/573/corrigendum/2025-03-24/oj
- ESB Networks, "F-gas regulation", 2025-26. https://www.esbnetworks.ie/services/get-connected/renewable-connection/f-gas-regulation
- Council of the EU, "ST-10202-2025-REV-1", 2025 [STALE]. https://data.consilium.europa.eu/doc/document/ST-10202-2025-REV-1/x/pdf
- EirGrid, "Technical Update July 2026 R0", 2026-07. https://cms.eirgrid.ie/sites/default/files/publications/EirGrid-Technical-Update-July-2026-R0.pdf
- Siemens Energy, "EU F-gas regulation factsheet", ~2024 [STALE]. https://assets.siemens-energy.com/dam/783a1ca6-3b06-42e0-9d2d-b0c000a09cff/EU-F-gas-regulation-factsheet_EN-pdf_Original%20file.pdf
- Hitachi Energy, "Hitachi Energy helps customers accelerate SF6-free grid modernization with new EconiQ wins", 2026-08-24. https://www.hitachienergy.com/news-and-events/press-releases/2026/08/cs-hitachi-energy-helps-customers-accelerate-sf6-free-grid-modernization-with-new-econiq-wins
- Hitachi Ltd, "Chubu Electric Power Grid 550 kV SF6-free GIS order" (Japanese), 2026-03-12. https://www.hitachi.com/ja-jp/press/articles/2026/03/0312f/
- GE Vernova, "GE Vernova marks 10 years of SF6-free innovation, launches new 170 kV gas-insulated substation", 2026-08-26. https://www.gevernova.com/news/press-releases/ge-vernova-marks-10-years-sf6-free-innovation-launch-new-170-kv-gas-insulated
- GE Vernova, "GE Vernova to deliver SF6-free grid hubs for Stromnetz Berlin", 2026-07-16. https://www.gevernova.com/news/press-releases/ge-vernova-deliver-sf6-free-grid-hubs-stromnetz-berlin
- UNEP Ozone Secretariat, "F-gases technology and regulations (Montreal Protocol)", 2025-10. https://ozone.unep.org/system/files/documents/2025_10%20F-gases%20technology%20and%20regulations%20Montreal%20Protocol%20pdf.pdf
- Siemens Energy, "Vacuum Interrupter Factory Berlin", 2024 [STALE]. https://assets.siemens-energy.com/dam/1a52c3a3-663d-4ed5-a5d0-b21e00dec8ea/Vacuum_Interrupter_Factory-Berlin_EN-pdf_Original%20file.pdf
- Industry Europe, "Siemens Energy to end potent greenhouse gas use in power transmission", 2022 [STALE]. https://industryeurope.com/sectors/energy-utilities/siemens-energy-to-end-potent-greenhouse-gas-use-in-power-transmission/
- Siemens Energy, "EU LIFE Blue 420 kV GIS", 2024-10 [STALE]. https://www.siemens-energy.com/global/en/home/products-services/product/eu-life-blue-420kV-gis.html
- T&D India, "We believe that F-gases will be completely phased out: Siemens Energy", undated [STALE]. https://www.tndindia.com/we-believe-that-f-gases-will-be-completely-phased-out-siemens-energy/
- Siemens Energy, "Earnings Release Q2 FY26", 2026-05. https://assets.siemens-energy.com/dam/fb695b3d-e910-4f47-81b5-b4480034f6a1/Earnings-Release-Q2-FY26-EN-pdf_Original%20file.pdf
- EMR, "Siemens Energy earnings release Q3 FY 2026", 2026-08. https://www.emr-online.com/siemens-energy-earnings-release-q3-fy-2026-siemens-energy-accelerates-profitable-growth-siemens-gamesa-delivers-a-positive-quarterly-result/
- Mitsubishi Electric, "84 kV dry-air-insulated GIS order from Kansai T&D", 2024-07-17 [STALE]. https://www.mitsubishielectric.com/en/pr/2024/0717-a/?cid=rss
- AFPBB (Toshiba release), "300 kV CO2/O2 GIS and GCB", 2026-04. https://www.afpbb.com/articles/-/3632553
- Meidensha, "Agreement with Chugoku Electric Power Network on SF6-free VCB", 2025-02-26 [STALE]. https://meidensha.co.jp/news/news_03/news_03_01/__icsFiles/afieldfile/2025/02/20/20250226.pdf
- CEO Score Daily, "HD Hyundai Electric Finland 145 kV SF6-free breaker order", 2025-09-16. https://ceoscoredaily.com/page/view/2025091610200131000
- Herald Corp, "HD Hyundai Electric SF6-free GIS contracts (Nexel, Finland)", 2025-11-30. https://www.heraldk.com/article/2025113023521349339
- Money Today, "Korean eco-friendly HV equipment", 2026-06-05. https://www.mt.co.kr/industry/2026/06/05/2026060414510443560
- twig24 / Metro Seoul, "Hyosung 420 kV SF6-free GIS at CIGRE", 2026-08-26. https://twig24.com/news/2026/08/26/20260826031006
- Metro Seoul, "HD Hyundai Electric and Hyosung European/Nordic orders", 2026-08-25. https://www.metroseoul.co.kr/article/20260825500546
- Greenberg Traurig, "EU PFAS restriction: final consultation on socio-economic analysis closes 25 May 2026", 2026-05. https://www.gtlaw.com/en/insights/2026/5/eu-pfas-restriction-final-consultation-on-socio-economic-analysis-closes-25-may-2026
- Chemistry World, "3M pledges to exit PFAS manufacturing", 2022-12 [STALE]. https://chemistryworld.com/news/3m-pledges-to-exit-pfas-manufacturing/4016766.article
- ToxicDocs, "Hitachi Energy C4-FN supply document", 2023-02 [STALE]. https://www.toxicdocs.org/d/vyNOQa1X9Dkk85vEKyoEbdy68
- CIGRE, "B3-10738 Extension and upgrading of 420 kV GIS with SF6-free C4FN GIS solution", 2026. https://www.e-cigre.org/publications/detail/b3-10738-2026-extension-and-upgrading-of-420-kv-gis-with-sf6-free-c4fn-gis-solution.html
- CARB, "SF6 GIS regulation workshop slides", 2020-07 [STALE]. https://ww2.arb.ca.gov/sites/default/files/2020-07/sf6-gis-reg-slides-07132020.pdf
- Switchgear Magazine (Growth Market Reports), "SF6-free switchgear market to reach $9.85B by 2034", 2025-26. https://switchgear-magazine.com/news/business/sf6-free-switchgear-market-to-reach-9-85-b-by-2034/
- FilingReader, "Henan Pinggao Electric wins CNY2.09bn State Grid contract", 2026-06-12. https://filingreader.com/news-wire/shanghai/2026-06-12/henan-pinggao-electric-wins-cny-209bn-state-grid-contract
- China Daily (Jiading), "Shanghai Pinggao MV GIS to Spain", 2025-05-27 [STALE]. https://subsites.chinadaily.com.cn/jiading/2025-05/27/c_1096420.htm
- cleanthinking.de, "Reiche bremst beim Netzausbau", 2026. https://www.cleanthinking.de/reiche-bremst-beim-netzausbau/
- Table.Media (BMWE), "Bundesbedarfsplangesetz amendment", 2026-04-30. https://table.media/assets/berlin/260430_bmwe_lfb_bundesbedarfsplangesetz.pdf
- Publications Office of the EU (TED), "Energie AG 110 kV SF6-free circuit breaker framework", 2026-07. https://op.europa.eu/en/web/public-procurement/procurement-details/-/procurement/8e173ed8-eadc-4fb1-8b67-b55ae6b32464
- Publications Office of the EU (TED), "Berlin 110 kV GIS (GWP<1000)", 2026. https://op.europa.eu/en/web/public-procurement/procurement-details/-/procurement/fc11d0ee-e1e5-4038-a3cd-a5424ec8dc4e
- Tenderlift (simap Aargau), "110-kV-GIS-Schaltanlagen dreiphasig gekapselt", 2026-08. https://tenderlift.ch/tenders/aargau/110-kv-gis-schaltanlagen-dreiphasig-gekapselt-845ece7f/
- Simply Wall St via Webull, "Siemens Energy valuation narrative", 2026. https://www.webull.com/news/15282570662192128
- Interactive Brokers, "Price snapshots ENR and GEV", 2026-10-14. IBKR MCP data (no public URL)


---

### 4.7 — #7 · US 765 kV-class (800 kV) EHV transformers and shunt reactors
*Megatrend: Grid and electrification (AI/data-center load, Permian electrification, EHV AC backbones) | 2026 -> 2030 revenue: $0.15-0.40B -> $0.75-1.8B | CAGR: 31-67% plausible (central ~50%; cross-paired extremes 17-86%) | Growth mix: ~80% volume / ~20% price | Confidence: low (high on direction, low on magnitude)*

**Definition.** In: US-delivered 800 kV-class equipment (BIL ~1,950-2,050 kV), oil-immersed, covering:
- single-phase 765/345 kV and 765/500 kV autotransformers (~500-750 MVA per phase, built as banks plus spares);
- 765 kV step-down units for very large loads such as hyperscale campuses;
- 765 kV line and switched-bus shunt reactors (~100 MVAr single-phase);
- replacements for the legacy fleet. AEP alone owns >2,100 mi of 765 kV line [G].

Revenue is measured as supplier revenue on delivery. Bushings and tap changers are counted inside transformer value. 800 kV breakers are sized separately as an adjacency.

Out:
- 345/500 kV large power transformers, even in the same package (e.g., Hyosung's KRW 166.5bn of 345 kV units, Sep-2026).
- India/China 765 kV and UHV; Hydro-Québec 735 kV.
- HVDC converter transformers, FACTS, GIS, conductors, EPC and service.

**Value-chain path.** Grid and electrification -> US EHV AC transmission (ERCOT, PJM, SPP, MISO) -> 765 kV substations -> large power transformers and reactors -> **765 kV-class autotransformers + shunt reactors**. Inputs: grain-oriented electrical steel (GOES), copper, 800 kV RIP bushings, on-load tap changers (OLTCs), vapour-phase drying (VPD) ovens, and impulse test bays rated above 2,000 kV BIL.

**Drill-down decision.** I tested four narrower niches and rejected all of them:
- **Shunt reactors alone.** Probably growing at least as fast, because reactor demand scales with line-miles (ERCOT's Blu Lacy station alone specifies 4 x 300 MVAr [R]). But they are only ~$0.03-0.08B in 2026 [E], and every disclosed contract bundles them with transformers.
- **800 kV RIP bushings.** About 2-4% of transformer value, under $50M/yr even in 2030 [E]. They are supply-critical (Hyosung signed a long-term 765 kV bushing agreement with Trench, May-2026 [R]) but below the size floor.
- **800 kV breakers.** $0.02-0.06B -> $0.07-0.35B [E], with no path to $1B, so I report them as an adjacency.
- **Direct hyperscaler purchases.** Real (Hyosung KRW 220bn, ~$155-165M, Sep-2026 [R]) but too lumpy to size, so they stay in as a demand driver.

Transformers plus reactors is the narrowest level I can observe from supplier disclosures. It clears the size floor only marginally: the 2026 range straddles $200M, and the path-to-$1B test passes in the central and high cases but fails in the low case ($0.75B).

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $0.15-0.40B (central ~$0.25B) [E] | $0.75-1.8B (central ~$1.25B) [E] | central 49.5%; plausible 31-67%; extremes 17-86% |
| Single-phase units (autos + reactors) | ~21-50 (central ~35) [E] | ~80-160 (central ~130) [E] | central ~39% |
| Blended ASP per unit | ~$6.5-7.5M [E] | ~$9-10M [E] | ~7-10%/yr |
| 800 kV breakers (not in niche) | $0.02-0.06B [E] | $0.07-0.35B [E] | n/m |

CAGR math over 4 years:

| Case | 2026 | 2030 | Ratio | CAGR |
|---|---|---|---|---|
| Central | $0.25B | $1.25B | 5.0x | 49.5% |
| Low end with low end | $0.15B | $0.75B | 5.0x | 49.5% |
| High end with high end | $0.40B | $1.8B | 4.5x | 45.6% |
| Plausible band, low | $0.32B | $0.95B | 2.97x | 31.3% |
| Plausible band, high | $0.20B | $1.55B | 7.75x | 66.9% |
| Extreme, low | $0.40B | $0.75B | 1.875x | 17.0% |
| Extreme, high | $0.15B | $1.8B | 12x | 86.1% |

Units grow (130/35)^0.25 - 1 = 38.8%/yr. ASP grows 1.30-1.45x, or 6.8-9.7%/yr.

- **Volume vs price:** ~77-84% volume and ~16-23% price [E].
  - Revenue rises ~5x in the central case.
  - Blended ASP rises 1.30-1.45x. 2026 deliveries carry 2022-24 contract prices; 2030 deliveries carry 2025-27 contract prices.
  - Price anchors: HD Hyundai's Sep-2025 Texas order works out to ~$8.3M per unit blended (KRW 277.8bn / 24 units) [R, STALE 2025-09; own division]. Wood Mackenzie reports power-transformer prices +77% since 2019 [3P, STALE 2025-08].
  - Volume = 5 / (1.30 to 1.45) = 3.45-3.85x.
  - Price share of log growth = ln(1.30)/ln(5) = 16% to ln(1.45)/ln(5) = 23%.
  - The price part is unusually durable to 2030 because it is locked into backlog contracts. The risk is on orders placed after 2028. The bear case assumes flat ASPs there, which makes growth 85-100% volume.

- **Top-down (2026):**
  - Autos: 15-28 x $6.5-9M = $0.10-0.25B.
  - Reactors: 6-14 x $3.5-5.5M = $0.02-0.08B.
  - Early program units: $0-0.05B.
  - Total $0.12-0.38B [E].
  - Cross-check: the historical market is ~15-20 autos/yr, inferred from ~230-260 installed units and Hyosung's "nearly half" claim [E].

- **Top-down (2030, by line-miles):**
  - New non-MISO 765 kV line: ~4,300-4,900 mi. That is ERCOT Permian ~1,300-1,500 [E], STEP Eastern 1,109 [R], PJM ~600-800 [E] and SPP ~1,250-1,450 [E].
  - Equipment per 1,000 mi: ~45-55 single-phase autos and ~30-40 reactors [E]. Reactors are sized from ~4.5 MVAr/mi of line charging, 60-80% compensated.
  - Program value: 195-270 autos x $10-12M plus 130-195 reactors x $5-6.5M = $2.6-4.5B.
  - 2030 revenue:
    - 20-28% of non-MISO program value delivered in 2030: $0.52-1.26B.
    - First MISO deliveries (3-10% of $1.2-3.3B): $0.04-0.33B.
    - Legacy replacement: $0.12-0.25B.
    - Direct data-center units: $0.05-0.25B.
    - Sum $0.73-2.09B.
  - A 15% schedule haircut on the high end gives **$0.73-1.78B** [E].

- **Bottom-up (2026):**
  - Hyosung $0.07-0.20B. Its US revenue is ~$0.7-1.3B: the US 'HICO entities' were 18.02% of Q1-26 sales (≈ KRW 245bn/qtr [R, via IBKR]), plus US units booked at headquarters [E]. I assume a 765 kV share of 10-20%.
  - Hitachi Energy $0.03-0.10B.
  - HD Hyundai $0-0.03B. Its disclosed US 765 kV deliveries start in 2027.
  - Siemens Energy and others $0.01-0.04B.
  - Sum $0.11-0.37B [E].

- **Bottom-up (2030):**
  - Deliverable units: Hyosung 40-60; HD Hyundai 20-40 (~42-46 units already disclosed for 2027-29); Hitachi 15-35; Siemens 5-15; others 0-10.
  - Total 80-160 units x $8.5-10.5M blended = **$0.68-1.68B** [E].
  - Capex-share cross-check:
    - 765 kV-related capex is ~$42-58B [E].
    - Transformers and reactors are 7-11% of it. ERCOT Phase I check: ~119 autos x $11M + ~88 reactors x $5.75M ≈ $1.8B on ~$23B of capex, about 8% [E].
    - Program equipment = $2.9-6.4B.
    - 18-22% falls in 2030: $0.53-1.40B.
    - Plus $0.2-0.45B of replacement and data-center units = **$0.73-1.85B**.

- **Reconciliation:**
  - The four methods overlap at ~$0.75-1.8B, central ~$1.25B: line-miles ($0.73-1.78B), capex share ($0.73-1.85B), supplier capacity ($0.68-1.68B) and order flow ($0.8-1.6B, assuming $1.3-2.0B/yr of total intake [E]).
  - The bear's probability weights (25% at ~$0.75B, 35% at ~$1.05B, 40% at ~$1.6B) give ~$1.2B.
  - Why the draft's $1.0-2.1B was cut:
    - (i) **Stock vs flow.** Korean disclosed 765 kV intake is KRW ~1,556bn ≈ $1.07-1.11B (Sep-2025 to Sep-2026) [R sum; E FX]. That is 13 months of orders delivered over 2026-31, or ~$0.25-0.35B/yr of revenue. Grossed up for a 55-70% Korean share, it is ~$0.35-0.65B/yr. So ~50-70% of the 2030 central still depends on orders that are undisclosed or not yet placed.
    - (ii) Its capex share already included breakers and GIS, and it then added breakers again.
    - (iii) It priced 'transformer-equivalents' at $11-14M against the only observed blended price of $8.3M, and its unit counts implied ~6x revenue growth, not 5x.
  - Why 2026 was widened to $0.15-0.40B: the fact-check ($0.15-0.35B) and the bear ($0.30-0.40B) disagree, and nothing settles it because no supplier discloses 765 kV revenue. The draft's upward nudge relied on a 2025 Hyosung delivery, which is 2025 revenue.
  - Sensitivity: each +$0.05B on the 2026 base cuts the central CAGR by ~5-7 points (e.g., $0.30B -> $1.25B = 42.9%).

#### Demand drivers and catalysts
- **ERCOT Permian (largest pool, deliveries 2027-29).**
  - The PUCT approved two Oncor lines on Aug-28-2026 [R]: Dinosaur-Longshore (242.6 mi, $2.243B) and Longshore-Drill Hole (181.6 mi, $1.704B). Targets are 2028 and 2029 [G].
  - Howard-Solstice (~370 mi) was reportedly approved on Sep-11-2026 on a modified route [R; year inferred, unverified].
  - The remaining CCNs are expected Q4-2026 to H1-2027 and are pending. Legal challenges and calls from the AG and legislators to pause are outstanding.
- **ERCOT STEP Eastern, the key 2030 swing program.**
  - ~$9.4B and 1,109 mi of single-circuit 765 kV [R]. The ERCOT board endorsed it around Dec-2025/Jan-2026 [R; exact date unconfirmed].
  - Stations are due in service 2030-32 [R].
  - Risk catalyst: the Texas legislative session, Jan-May 2027.
- **PJM data-center load.**
  - The $4.6B Valley Link backbone (2024 Window 1 [R, STALE 2025-02]) targets 2029.
  - 2025 Window 1 ($11.8B, including 500/765 kV lines) was approved Feb-12-2026 [R].
  - 2026 Window 1 closed Oct-12-2026; board approval is expected ~Q1-2027 [R].
- **SPP.**
  - The 2025 ITP is $8.6B across 50 projects (Nov-5-2025) [R], with 949 mi of 765 kV [3P: Utility Dive's figure, not in SPP's own text]. It followed $7.7B in 2024 [R].
  - The overlay value reassessment and the 2026 ITP vote are due ~Q4-2026 [G]. This catalyst can move either way.
- **MISO Tranche 2.1.**
  - $21.8B, with the 765 kV backbone in service 2032-34 [R]. The 3,631 mi figure may be total portfolio line-miles rather than 765 kV only [unverified].
  - FERC complaint EL25-109 was still pending as of Apr-2026 [R]; ruling timing is unverified.
  - It adds little to 2030 revenue either way.
- **Direct large-load purchases.** Hyosung's KRW 220bn 765 kV order for big-tech AI campuses (Sep-2026) [R]. The number of campuses is unverified.
- **Legacy replacement and utility capex.** AEP guides $78B of five-year capex, including $33B for transmission, and says its EHV long-lead transformers and breakers are already secured [G; not re-verified this round].
- **Supply ramps:**
  - Hyosung-Quanta 72.5-800 kV breaker JV output from ~Oct-2026 [G].
  - HD Hyundai Alabama 765 kV capability in 2027 (Apr-2027 per one report) [G].
  - Siemens Charlotte, early 2027 [G].
  - Hyosung Memphis +50% by 2028 [G].
  - Hitachi South Boston, ~2028 [G, unverified].

#### Supply side
- **Suppliers and shares** (share of 2025-27 US 765 kV order intake; all [E]):
  - Hyosung 35-50%. The company claims ~half of the installed US 765 kV base [company claim].
  - HD Hyundai 15-25%. Disclosed orders total $386M ($199M + $67.9M + $119M) [R].
  - Hitachi Energy 10-30%, widened from the draft's 20-30%. No US 765 kV order was found; its only 765 kV order found is India's 30 x 765 kV 500 MVA [R, STALE 2025-06].
  - Siemens Energy 5-12%.
  - GE Vernova/Prolec, Toshiba and Mitsubishi 0-8% [unverified].
  - Disclosure bias: Korean firms must file contracts on DART, so their ~55-70% of *disclosed* intake overstates their true share.
  - Korean press says only ~5 firms worldwide can supply 765 kV equipment to North America [3P].
- **Capacity and lead times:**
  - 2025-26 contracts deliver through Nov-2028, Aug-2029, 2029 and Jan-2031, implying 3-5 year lead times [R].
  - Wood Mackenzie (Q2-2025): 128 weeks for power transformers, 144 weeks for GSUs, and a ~30% US supply deficit [3P, STALE 2025-08]. Its later figures (GSUs above 160 weeks in Q1-2026, a further +4-10% on price) are unverified [3P].
  - Large power transformer lead times are 36-60 months (Apr-2026) [3P].
  - Hyosung is reportedly booked through 2028 [3P].
  - Capacity additions cluster in 2027-28:
    - Memphis: +50%, announced Nov-2025 [G].
    - Alabama: +50% [G].
    - South Boston: $457M, ground broken Jun-2026 [R].
    - Charlotte: 24 -> 57 units/yr; 765 kV capability unconfirmed [G].
- **Qualification barriers:**
  - A 765 kV unit needs an impulse bay above 2,000 kV BIL, large VPD ovens, and heavy-haul logistics for main tanks of ~300-450 t.
  - Utility design review and approved-vendor qualification take 12-24 months.
  - Reference installations favour Hyosung and Hitachi [E].
  - Upstream bottlenecks: 800 kV RIP bushings (Hitachi, Trench), EHV OLTCs, and GOES (Cleveland-Cliffs is the sole US producer).
- **Geographic concentration:**
  - Memphis is the only US plant that can build 765 kV units today [company claim], so most 2026-27 units are imported from Korea and Europe.
  - The US-built share should reach ~35-50% by 2030 [E].
  - Texas takes ~35-50% of 2028-30 deliveries [E]. AEP is a developer in all four RTOs.

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| Hyosung Heavy Industries | 298040 / KRX | #1 US 765 kV transformer and reactor supplier; Memphis; breaker JV | ~2-5% (2026) -> ~5-12% (2030) [E] |
| HD Hyundai Electric | 267260 / KRX | #2-3 supplier; Ulsan, plus Alabama from 2027 | ~0-1% -> ~4-10% [E] |
| Hitachi Ltd (Hitachi Energy) | 6501 / TSE | 765 kV transformers, reactors, 800 kV breakers and bushings; South Boston | <0.5% of Hitachi Ltd [E] |
| Hitachi Energy India | POWERINDIA / NSE | 765 kV capacity reserve for the group | ~0% US [E] |
| Siemens Energy | ENR / XETRA | EU-built 765 kV units; 800 kV breakers | <0.5% [E] |
| GE Vernova | GEV / NYSE | 800 kV breakers; US 765 kV transformers unverified | <0.3% [E] |
| Mitsubishi Electric | 6503 / TSE | EHV breakers; US 765 kV role unverified | <0.1% [E] |
| Quanta Services | PWR / NYSE | Hyosung breaker JV partner; 765 kV EPC | <1% of equipment revenue [E] |
| Trench Group | private | 800 kV bushings (Hyosung agreement) | unverified |
| Cleveland-Cliffs | CLF / NYSE | Sole US GOES producer (input) | <0.5% [E] |
| AEP; Oncor (Sempra) | AEP / NASDAQ; SRE / NYSE | Lead customers and developers | n/a (customers) |

#### Bear case and key risks
- **Technology substitution:**
  - **345 kV double-circuit AC (500 kV in PJM) is the main threat.**
    - In ERCOT's study, 765 kV cost only ~7% more than 345 kV: $32.99B vs $30.75B statewide, and $13.77B vs $12.95B for the Permian [3P, STALE 2025-01].
    - That margin is fragile. SPS's estimate for one SPP 765 kV project more than doubled, from $1.69B to $3.62B [R, STALE 2025; date unverified].
    - SPP is reassessing the "comprehensive value of the entire 765 kV overlay" by Q4-2026 [G].
    - Bear view: 0-10% of 2030 deliveries at risk, but 20-40% of the 2031-34 pipeline [E].
  - Reconductoring and grid-enhancing technologies: 0-5% of 2030 [E].
  - HVDC: ~0% before 2030 because converter slots are booked to ~2030; 5-15% of post-2030 long-haul additions [E].
  - Hyperscaler self-supply (on-site generation, co-location) cuts data-center 765 kV units by 30-60% [E].
  - Design substitution inside the niche (shared spares, fewer banks per station, switching-only stations, and whether ERCOT counts banks or single units) swings content per station by 10-30% or more [E].
  - Net effect: 5-15% off 2030 revenue, plus a lower run-rate after 2030 [E].
- **Capex cuts:**
  - Approved lines slip rather than get cancelled.
  - A 20-30% cut in hyperscaler and utility capex in 2028 would leave 2030 revenue 20-35% below the draft, at ~$1.0-1.2B instead of $1.5B [E].
  - Program cuts stack on top [E]:
    - If EL25-109 is upheld, MISO's $0.1-0.3B of early deliveries goes to ~0.
    - An SPP re-scope removes $0.1-0.2B.
    - A 12-24 month STEP Eastern slip moves $0.15-0.35B into 2031-32.
  - Already visible:
    - Korea Investment & Securities cites installation delays on some of Hyosung's North American projects and Middle East war delivery delays (Oct-2026) [3P].
    - About half of ~12 GW of 2026 US data-center capacity is reportedly at risk [3P, unverified].
    - SPP sent the 345 kV Redbud-Mathewson project back to staff for breaching its cost cap (Jul-2026) [R].
  - Timing compounds these risks:
    - Calendar 2030 can be a trough between the Permian wave (2027-29) and the Eastern/MISO wave (2029-32).
    - Test-bay and oven rationing: a 765 kV unit takes ~2-3x the test and VPD time of a 345 kV unit [E].
    - First-article type-test failures at newly 765 kV-capable plants cost 6-12 months each [E].
    - Tariffs on imported units have unclear pass-through.
- **Chinese capacity:**
  - TBEA, China XD, Baobian, SDEE, Jiangsu Huapeng and Changzhou XD all have 750/1,000 kV references.
  - TBEA's Q1-26 international orders were ~$621M (+30%) [R]. It won a $2.4B Saudi EHV award [R, STALE 2025-08] and quotes 3-6 month production cycles.
  - Chinese exports of transformers above 10 MVA rose 61% y/y in Jan-Feb 2026, and exports to the US rose 182% [3P, unverified]. China holds ~4% of the US transformer market [3P].
  - Direct Chinese share of US 765 kV by 2030 is 0-3%, with under 10% probability of meaningful entry [E].
  - The indirect effect is the real risk. Chinese oversupply in other markets pushes Korean and European capacity toward the US, which could cut US pricing on 2028+ orders by 10-20% [E]. India is the plausible swing supplier.
- **Double-ordering / pull-forward:**
  - There is no channel inventory; the risk sits in slot reservations and framework contracts.
  - HD Hyundai's 24-unit Texas order came ~11-12 months before the CCN approvals [R].
  - Hyosung's KRW 787bn order runs ~5 years, to Jan-2031 [R].
  - The ~$1.09B of Korean intake is only ~$0.2-0.3B/yr of revenue, or ~$0.35-0.5B/yr grossed up for share [E].
  - 2027-28 intake could fall 30-50% from the 2025-26 pace [E].
  - Hyperscaler direct buys are a scramble signal and may duplicate the station math.
  - Filling spare-equipment pools is one-time demand.
  - Bear quantification: 2030 revenue $0.3-0.6B below the bull case [E].
- **Already priced in?** Yes, and the market is now de-rating the story.
  - Hyosung: KRW ~400k (Oct-2024) -> 4,742,000 (May-2026 peak) -> 1,844,000 (Oct-15-2026), -61% from peak [R].
  - HD Hyundai Electric: 328k -> 1,430,000 -> 488,000, -66% from peak and below its Oct-2025 level [R].
  - GE Vernova: ~$920 vs a ~$1,195 high, -23% [R].
  - HD Hyundai fell up to 13% intraday on in-line Q2 results (Jul-29-2026) [R]. Its 2026E P/E is ~36x [3P].
  - In Oct-2026 brokers cut target prices but kept Buy ratings. KB Securities blamed a "supply-demand vacuum and fear" [3P].
  - Caveat: 765 kV is a small share of each company's revenue, so the stocks are a noisy read on this niche.
- **Bear-case numbers:**
  - **2030: $0.6-0.9B (central $0.75B)** [E].
    - Transformers: 45-75 x $9-11M = $0.40-0.80B.
    - Reactors: 15-30 x $3.5-5M = $0.05-0.15B.
    - Total $0.45-0.95B, rounded to $0.6-0.9B.
    - Breakers add $0.07-0.15B.
  - On the bear's own 2026 base of $0.30-0.40B:
    - Central: (0.75/0.35)^0.25 - 1 = **21.0%**.
    - Range: 10.7% (0.40 -> 0.60) to 31.6% (0.30 -> 0.90).
  - On this section's $0.25B central base, the bear's 2030 range implies 24.5-37.7%.
  - Probability **~25%** (20-30%). The bear's full distribution: 35% on a $0.9-1.2B middle case, 40% on $1.2-2.1B.
  - **First warning sign:** DART correction filings (정정공시) that extend end-dates or cut the value of Hyosung's KRW 787bn and 220bn contracts or HD Hyundai's KRW 277.8bn, ~98bn and 173bn contracts. Others: no new US 765 kV award of KRW 100bn or more for two quarters, or an SPP overlay re-scope.

#### Leading indicators to watch (next 2-4 quarters)
1. DART filings by 298040 and 267260: new 765 kV contracts (baseline KRW ~1,556bn over 13 months) and correction filings.
2. Hyosung's Q3-2026 results and call (late Oct-2026): do the North American installation delays involve 765 kV projects?
3. The SPP overlay value review and 2026 ITP vote (Q4-2026); the PUCT's remaining CCNs; 765 kV bills in the Jan-May 2027 Texas session.
4. A FERC ruling on EL25-109; PJM 2026 Window 1 approval (Q1-2027).
5. Any disclosed US 765 kV order from Hitachi Energy or Siemens Energy. The central case needs ~30-45% non-Korean supply. Also the first 765 kV unit shipped from HD Hyundai Alabama.

#### Confidence and biggest unknown
**Confidence is low.** Direction is well supported: CCNs are approved, PJM and SPP lines are approved, and ~$1.1B of dated Korean contracts is verified. Magnitude is not:
- Neither endpoint is observable.
- The full CAGR range is 17-86%.
- No earnings-call transcripts were read, because Alpha Vantage was rate-limited.

**Biggest unknowns:**
- **The 2026 base ($0.15-0.40B).** Each +$0.05B on the base cuts the central CAGR by 5-7 points.
- **Whether STEP Eastern, SPP and early MISO equipment lands in calendar 2030 or slips into 2031 or later.** About 50-70% of the 2030 central is not yet in disclosed backlog.

#### Sources
- CEO Score Daily, "HD Hyundai Electric 765 kV transformer and reactor order from Texas utility (KRW 277.8bn, 24 units)", 2025-09-22 [STALE 2025-09]. https://ceoscoredaily.com/page/view/2025092213432517014
- Kukinews, "HD Hyundai Electric 765 kV transformer contract with AEP (KRW 98.6bn)", 2026-01. https://www.kukinews.com/article/view/kuk202601060029
- Hankyung Magazine, "HD Hyundai Electric KRW 173bn 765 kV order (SPP/MISO-area utility)", 2026-05-07. https://magazine.hankyung.com/business/article/202605071307b
- Money Today, "Hyosung Heavy Industries 765 kV transformer and reactor order (KRW 787bn)", 2026-02-10. https://www.mt.co.kr/industry/2026/02/10/2026021014245569793
- Korea JoongAng Daily, "Hyosung Heavy Industries secures $540 million ultra-high-voltage transformer contract in US", 2026-02-10. https://www.koreajoongangdaily.com/business/hyosung-heavy-industries-secures-540-million-ultra-high-voltage-transformer-contract-in-us/12240917
- Hankyung Magazine, "Hyosung KRW 386.5bn big-tech AI data-center transformer orders", 2026-09-15. https://magazine.hankyung.com/business/article/202609155016b
- Asia Economy, "Hyosung data-center transformer contracts", 2026-09-15. https://view.asiae.co.kr/en/article/2026091509364051456
- Korea Times, "Hyosung Heavy Industries forms US joint venture to make high-voltage circuit breakers", 2026-09-18. https://www.koreatimes.co.kr/business/companies/20260918/hyosung-heavy-industries-forms-us-joint-venture-to-make-high-voltage-circuit-breakers
- Action News 5, "Hyosung HICO expands again, bringing 240 new jobs to Memphis", 2025-11-12. https://www.actionnews5.com/2025/11/12/hyosung-hico-expands-again-bringing-240-new-jobs-memphis
- The Guru, "Hyosung-Trench long-term 765 kV bushing supply agreement", 2026-05-31. https://theguru.co.kr/news/article.html?no=102419
- Kyunghyang Shinmun, "HD Hyundai Electric Alabama expansion and 765 kV capability", 2026-08-02. https://www.khan.co.kr/article/202608021059001
- Hitachi Energy, "Hitachi Energy breaks ground on the nation's largest facility for the production of large power transformers in South Boston, Virginia", 2026-06-29. https://www.hitachienergy.com/news-and-events/press-releases/2026/06/hitachi-energy-breaks-ground-on-the-nation-s-largest-facility-for-the-production-of-large-power-transformers-in-south-boston-virginia
- Carolina Public Press, "Transformer shortage in US drives Siemens NC jobs expansion", 2026 (date unverified). https://carolinapublicpress.org/63153/transformer-shortage-us-drives-siemens-nc-jobs-expansion/
- Dallas Express, "Texas regulators approve 424 miles of power lines despite calls to wait", 2026-08-28. https://dallasexpress.com/business-markets/texas-regulators-approve-424-miles-of-power-lines-despite-calls-to-wait/
- Texas Tribune, "Transmission lines, Texas energy", 2026-08-28. https://www.texastribune.org/2026/08/28/transmission-lines-texas-energy/
- Texas Policy Research, "PUCT approves Howard-Solstice 765 kV line", 2026-09-11 (year inferred). https://www.texaspolicyresearch.com/?p=12342
- RTO Insider, "STEP tag page", 2025-12 to 2026-01. https://www.rtoinsider.com/tag/strategic-transmission-expansion-plan-step
- ERCOT, "Texas 765-kV STEP Eastern Backbone status update (RPG)", 2025-11-10. https://www.ercot.com/files/docs/2025/11/10/EIR-Joint_AEP_CPS_Oncor_CEHE_Texas_765-kV_STEP_Eastern_Backbone-Status-Update-RPG-Nov_2025_Final.pdf
- ERCOT, "Trending Topic: 345-kV vs 765-kV Transmission", 2025-01-28 [STALE 2025-01]. https://www.ercot.com/files/docs/2025/01/28/ERCOT_Trending_Topic_345-kV_vs_765-kV_Transmission.pdf
- SPP, "SPP board advances regional transmission plan to keep pace with accelerating growth and ensure grid reliability", 2025-11-05. https://www.spp.org/news-list/spp-board-advances-regional-transmission-plan-to-keep-pace-with-accelerating-growth-and-ensure-grid-reliability/
- RTO Insider, "SPP cost-control memo", 2025-10/11 [STALE 2025-10]. https://www.rtoinsider.com/wp-content/uploads/2025/11/Cost-Control-Memo.pdf
- Zero Emission Grid, "SPP MOPC July 2026", 2026-07. https://www.zeroemissiongrid.com/iso-rto/spp-mopc-july-2026/
- PJM Inside Lines, "PJM Board approves new transmission projects to support grid reliability", 2026-02-12. https://insidelines.pjm.com/pjm-board-approves-new-transmission-projects-to-support-grid-reliability/
- Utility Dive, "Complaint against MISO transmission MVP portfolio at FERC", 2025-08 [STALE 2025-08]. https://www.utilitydive.com/news/complaint-miso-transmission-mvp-portfolio-ferc/759739/
- RTO Insider, "EL25-109 tag page", 2026-04-08. https://www.rtoinsider.com/tag/el25-109
- AEP, "First-quarter 2026 earnings release", 2026-05-05 (not re-verified). https://docs.aep.com/docs/newsroom/resources/earnings/2026-05/1stqtr26earnings.pdf
- Transformers Magazine, "US transformer market faces severe bottlenecks" (citing Wood Mackenzie), 2025-08 [STALE 2025-08]. https://transformers-magazine.com/tm-news/us-transformer-market-faces-severe-bottlenecks/
- pv magazine USA, "U.S. transformer market faces severe supply constraints as lead times extend to four years", 2026-05-11. https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/
- Etoday, "Brokers cut power-equipment target prices", 2026-10. https://www.etoday.co.kr/news/view/2635279
- Etoday, "Korea Investment & Securities on Hyosung Q3 delays", 2026-10. https://www.etoday.co.kr/news/view/2635499
- Hankyung, "HD Hyundai Electric falls after Q2 results", 2026-07-29. https://www.hankyung.com/article/202607292475i
- Sina Finance / Cailian Press, "TBEA and China XD international orders", 2026 (date unverified). https://cj.sina.com.cn/articles/view/2868676035/aafc85c302001r4be
- China Daily HK, "US transformer import reliance", 2026-08-31. https://www.chinadailyhk.com/article/638745
- Interactive Brokers, "Company connections and price history for 298040, 267260 and GEV", 2026-10-15. n/a (IBKR MCP data, no public URL)


---

### 4.8 — #8 · Merchant 300 mm silicon-photonics PIC foundry wafers (all end uses; pluggable-led, CPO and optical I/O as upside)
*Megatrend: AI data-center optical interconnect | 2026 -> 2030 revenue: $0.50-1.00B -> $1.8-5.0B | CAGR: 38-50% (central ~47%) | Growth mix: ~102% volume (~75% end demand + ~27% 200->300 mm migration) / ~-2% price | Confidence: low on size; medium that CAGR exceeds 30%*

**Definition.**

In: merchant fabrication on 300 mm wafers, sold to third parties, of SOI silicon-photonics PICs. That covers:
- Si/SiN waveguides, Mach-Zehnder and micro-ring modulators, Ge photodetectors, grating and edge couplers;
- monolithic SiPh+CMOS (GF 45SPCLO/Fotonix);
- PIC wafers made for EIC-on-PIC stacking (TSMC N65-class COUPE PIC, ST PIC100/PIC100-TSV).

Valuation is at wafer revenue, with two exceptions. ST is valued at PIC-die revenue, which slightly inflates it against the others. TSMC is imputed, because its PIC value is bundled inside COUPE. All end uses count: 800G-3.2T pluggables, LPO/LRO, NPO/CPO, optical-I/O chiplets, coherent/DCI, photonic quantum, FMCW LiDAR and sensing.

Out: 200 mm SiPh (Tower PH18, AMF 200 mm), captive output (Intel), EIC/driver/TIA wafers including SiGe BiCMOS, SoIC/COUPE packaging, fiber attach, test, InP/GaAs lasers, TFLN, pure-SiN platforms, SOI substrates and module assembly.

**Value-chain path.** AI data-center capex -> scale-out networking plus GPU/XPU scale-up fabrics -> optical interconnect (pluggables, LPO/LRO, NPO/CPO, optical I/O) -> optical engine or transceiver (Nvidia, Broadcom, InnoLight, Eoptolink, Coherent, Marvell) -> SiPh PIC die -> **merchant 300 mm SiPh PIC foundry wafer**. Inputs: 300 mm SOI, DUV immersion lithography, Ge epitaxy, SiN deposition.

**Drill-down decision.** I kept the 300 mm merchant level and rejected two narrower cuts.

- **CPO/NPO-only PIC wafers.** 2026 is only ~$0.02-0.08B [E]. The 0.3-1M CPO engines shipping need only ~0.7-2.2k wafers/yr at 648 dies/wafer [3P] and 70% yield [E]. That fails the size floor. 2030 is $0.36-1.5B [E] once the draft's unverified "4 PICs per engine" is corrected to ~1 (COUPE stacks one EIC on one PIC), and $0.15-0.45B in the bear case.
- **TSMC COUPE PIC alone.** It cannot be separated in TSMC's disclosures.

The 300 mm slice is the narrowest unit observable from GF, ST, TSMC and Tower data. It clears the floor and outgrows its 200+300 mm parent (~47% against ~33% central CAGR). Two caveats apply:
- ~27% of the growth is 200->300 mm share shift, not new demand.
- More than 85% of 2026 value (~60-70% of 2030 value) is pluggable, LPO or other, so this is not a CPO pure play.

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $0.50-1.00B; central ~$0.70B [E] | $1.8-5.0B; central ~$3.3B [E] | 38-50% paired; central ~47% [E] |
| Merchant 200+300 mm parent (context) | $1.35-1.85B; central ~$1.6B [E] | $3.5-7.5B; central ~$5.0B [E] | 27-42%; central ~33% [E] |
| Bear case (~25% probability) | same base | $1.3-2.4B; central ~$1.8B [E] | 17-36% on $0.70B (10-28% on the bear's $0.9B base) |

CAGR arithmetic (4 compounding years):

| Case | Calculation | CAGR |
|---|---|---|
| Central | (3.3/0.70)^0.25 = 4.71^0.25 = 1.473 | ~47% |
| Paired low | (1.8/0.50)^0.25 = 3.6^0.25 = 1.377 | ~38% |
| Paired high | (5.0/1.00)^0.25 = 1.495 | ~50% |
| 2026 held at $0.70B, 2030 low | 2.57^0.25 = 1.266 | ~27% |
| 2026 held at $0.70B, 2030 high | 7.14^0.25 = 1.635 | ~63% |

The cross-paired extremes, 16% (1.8/1.0) and 78% (5.0/0.5), are not meaningful because both years rest on the same wafer-ASP and PIC-area assumptions. About 6 points of CAGR are already locked in by the 2026 exit rate: Tower's CY26 SiPh is ~$0.78B against a $1B Q4 run-rate, and (1/0.78)^0.25 = 1.064 [E].

- **Volume vs price.** The central 4.71x breaks down as ~3.2x end-demand PIC area x ~1.51x share shift x ~0.97x ASP/mix (3.2 x 1.51 x 0.97 = 4.69). The share shift is the 300 mm share of the merchant parent rising from ~44% (0.70/1.6) to ~66% (3.3/5.0). In log terms that is ~75% end-demand volume, ~27% migration and ~-2% price [E].
  - Like-for-like wafer prices stay flat to firm through 2027. Evidence: Tower's $290M of reservation prepayments [G] and >70% of capacity reserved through 2028 [R per IBKR digest; unverified at source].
  - In 2028-30, prices fall 3-8%/yr [E] as TSMC, Tower Japan, Samsung, UMC and Chinese capacity lands. Mix adds +10-25% (TSV/3D-stack-ready, 400G/lane, monolithic) [E]. Central: 0.95^3 x 1.13 = 0.97.
  - The cumulative price band is ~-15% to +12% [E]; the bear case is 0.82-0.90x.
  - 2026 is a shortage-priced base. PIC area per Gbps also falls with micro-rings, CPO and 400G/lane, so wafer volume lags bandwidth shipped.
- **Top-down, 2026** (units x SiPh share x 300 mm share x content):
  - 1.6T: 14-20M shipped [3P, BofA via Longport: 30M demand, 50-60% met] x 60-70% x 20-35% = 1.7-4.9M x $35-55 = $0.06-0.27B.
  - 800G: 38-48M x 45-50% x 30-45% = 5.1-10.8M x $20-35 = $0.10-0.38B.
  - 400G and below, AOC, LPO: $0.03-0.08B.
  - CPO/optical I/O including NRE: $0.02-0.08B.
  - Coherent, quantum, LiDAR: $0.06-0.15B.
  - **Total: $0.27-0.96B [E].** Context: TrendForce sizes the 2026 AI transceiver market at $26B [3P].
- **Top-down, 2030:**
  - Pluggables: 80-140M x 50-60% SiPh x 55-75% on 300 mm x $20-40 = $0.44-2.52B. The 50-60% is pluggable-only; LightCounting's 30%->60% [3P] covers all optics including CPO, so the draft double-counted.
  - CPO/NPO: 60-100M ports (LightCounting ~100M [3P], haircut for timing) x $6-15 = $0.36-1.50B.
  - Optical I/O: $0.05-0.40B.
  - Non-datacom: $0.20-0.60B.
  - **Total: $1.05-5.0B [E].**
  - **LightCounting cross-check.** All optical chips are $4B in 2025 and $15B in 2031 [3P], ~$12.0B in 2030 interpolated (3.75^(1/6) = 1.246/yr). Then x 27-39% SiPh PIC share x 85-95% merchant x 0.6-1.0 wafer-to-chip value x 65-80% on 300 mm = $1.1-3.6B [E].
- **Bottom-up, 2026** (supplier revenue):
  - GF: total SiPh $0.42-0.52B, from >$200M in 2025 [R] x "more than double" [G] (an analyst figure from the May call was ~$400M [3P]). Less AMF 200 mm at $0.05-0.10B (unverified), 300 mm is $0.32-0.47B.
  - TSMC: 0.5-2.5k wpm effective output x 12 x $4-6k = $0.02-0.18B [E]. The 10k wpm (2Q26) and 15k (4Q26) schedule [3P] is capacity, not output. At 648 dies and 70% yield, 2.5k wpm already makes ~13.6M good PICs, 14-45x 2026 CPO demand.
  - ST PIC100: $0.08-0.22B [E]. High-volume production started Mar-26; the data-center revenue guide was raised to >$1B [G].
  - Tower 300 mm (Uozu): $0.02-0.08B [E].
  - UMC, Chinese lines, Samsung engineering lots: $0.01-0.05B.
  - **Sum: $0.45-1.00B.**
- **Bottom-up, 2030** (capacity x utilization x price):
  - TSMC: 25-35k wpm [3P; nStock attributes the schedule to a TSMC VP] x 12 x 50-85% x $3.5-6k = $0.53-2.14B, demand-capped at $0.5-1.8B.
  - GF: $1.0-1.65B total (on a >$1B end-2028 run-rate [G]) x 85-95% on 300 mm = $0.85-1.55B.
  - Tower: 16k wpm SiPh (METI-certified plan [R]) x 12 x 65-90% x $5-8.5k = $0.62-1.47B.
  - ST: $0.3-0.9B.
  - Samsung, UMC, Intel, China: $0.15-0.6B.
  - **Supply-side sum: $2.4-6.3B [E].** The top end double-counts the same customers.
  - At the central $3.3B and $5.5k/wafer, demand is ~50k wpm against ~62-103k wpm of announced 300 mm SiPh capacity, i.e. ~50-80% utilization.
- **Reconciliation, 2026.** Top-down $0.27-0.96B, bottom-up $0.45-1.00B. I adopt $0.50-1.00B, central $0.70B, weighted to bottom-up because GF discloses its SiPh line. The fact-check top was $0.95B. I widened it to $1.00B because TSMC volume in pluggable PICs is unverified, and the fact-check's own $4-6k inputs give TSMC up to $0.18B, not its stated $0.15B.
- **Reconciliation, 2030.** Top-down $1.05-5.0B; supply sum $2.4-6.3B; LightCounting-constrained $1.1-3.6B; bear $1.3-2.4B. I adopt $1.8-5.0B, central $3.3B.
  - Low end: the fact-check's $2.0B floor rests on Tower's ~$2B 2028 SiPh. Only ~30-45% of Tower SiPh will be 300 mm, so the contracts floor the parent, not this slice. I set the low end at the bear-case central of $1.8B.
  - Ceiling: $5.0B sits above LightCounting because supplier contracts suggest LightCounting is conservative. It sits below the draft's $6.5B, which relied on Tower 300 mm reaching $2.2B (beyond the METI 16k wpm) and on a TSMC arithmetic slip.
  - The central $3.3B is near the top of the LightCounting band, which is a known bull tilt.

#### Demand drivers and catalysts
- **1.6T scale-out pluggables and the EML-to-SiPh shift.** LightCounting has SiPh rising from 30% to 60% of optics over 2025-30 [3P]. InnoLight's 1.6T SiPh modules are in volume ramp [G]. Status: ramping now.
- **LPO/LRO.** Uses SiPh PICs; 2026-28.
- **Scale-out CPO.** Nvidia Spectrum-X Photonics (on COUPE) is shipping to select partners, with capacity expanding in 2H26. Broadcom's 51.2T Bailly is in volume [3P, TrendForce Jul-26]. TH6-Davisson is sampling. Status: early volume.
- **Scale-up optics.** Lumentum expects volume shipments in 2H27 and deployments in 2028 [G]. Nvidia's Feynman (mid-to-late 2028) offers copper or CPO NVLink [3P]. GF sees the CPO inflection in late 2028-29 [G; not re-verified]. LightCounting has ~100M CPO ports and ~$10B of engines in 2030 [3P]. Status: not yet committed.
- **200->300 mm migration.** Tower's Arai SiPh supply starts May-2027 and Track 1 is ready Q4-27 [G]. The Uozu new building (Track 2) ramps 2H28 or later and has no definitive agreements. GF's AMF upgrade timing is unverified.
- **Dated catalysts:**
  - TSMC Q3-26 call, 2026-10-16: first COUPE/PIC output read. Pending.
  - Tower Q3-26 results, Nov-2026: guide $520M +/-5% [G]. Q3 SiPh above ~$210M would support the $1B Q4 exit.
  - Tower 2028 prepayments due by Jan-2027. Pending.
  - ST Crolles expansion decision by end-2026 [G].
  - Samsung SiPh commercialization (2027) [3P]; UMC opens its own 12-inch platform (2027) [press].
  - GF's $300M CHIPS photonics award: at LOI stage on the Q2 call, finalization pending.

#### Supply side
- **Suppliers and shares [E].**
  - 2026: GF ~45-65%, ST ~12-25%, TSMC ~3-20%, Tower ~3-10%, others under 5%.
  - 2030: GF ~25-35%, TSMC ~20-35%, Tower ~18-30%, ST ~8-18%, others ~5-12%.
  - Tower is the majority supplier of 1.6T PICs overall, mostly from 200 mm [R, IBKR digest].
- **Capacity and lead times.**
  - Tower: SiPh capacity 5x Q4-25 levels by end-2026; $1.3B of 2027 contracts; $290M of prepayments [G].
  - ST: >4x by 2027, yet "not capacity-constrained" on the Q2 call [G].
  - TSMC: at least 25k wpm by 2028 [3P].
  - Tower Japan: 18k wpm under the METI-certified plan (16k SiPh + 2k SiGe), subsidy up to JPY159bn, project ~JPY600bn [R]. The Nikkei 45k wpm figure is contradicted.
  - CanSemi: Phase 4 adds 40k wpm of 12-inch mixed-signal capacity including SiPh by end-2029; the SiPh share is undisclosed [R via media; unverified].
  - Lead times [E]: brownfield 15-18 months; greenfield 24-36 months; pluggable qualification 6-12 months; CPO 12-24 months.
- **Qualification barriers.**
  - Process-specific PDKs: moving from PH18 to 300 mm means redesign and requalification.
  - IP ecosystems: Tower with OpenLight and Coherent, GF Fotonix, TSMC's COUPE flow.
  - Yields: Ge photodetectors and micro-ring tuning.
  - Telcordia-class reliability, and 300 mm SOI supply (Soitec).
  - TSMC's PIC output competes for SoIC capacity.
  - GF v. Tower patent suit (11 patents, filed Mar-26): unverified beyond Taiwanese press.
- **Geographic concentration [E].**
  - 2026: US/Singapore (GF) ~45-65%, France ~12-25%, Taiwan ~3-20%, Japan ~3-10%.
  - 2030: US/Singapore ~25-35%, Taiwan ~20-35%, Japan ~18-30%, France ~8-18%, Korea/Singapore (UMC)/China ~5-12%.
  - Demand sits with Nvidia, Broadcom and the Chinese module makers InnoLight and Eoptolink. Taiwan is a single point of failure for COUPE.

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| GlobalFoundries | GFS / Nasdaq | Largest 300 mm merchant SiPh foundry (45SPCLO/Fotonix); pluggables, optical I/O, PsiQuantum | 300 mm SiPh ~4-7% of ~$7.0-7.3B [E] |
| TSMC | 2330 TWSE / TSM NYSE | COUPE PIC plus SoIC; Nvidia, Broadcom and AMD CPO | <0.15% [E] |
| STMicroelectronics | STM NYSE / STMPA Euronext Paris | IDM; PIC100 for hyperscaler (AWS) programs | ~0.6-1.8% [E] |
| Tower Semiconductor | TSEM / Nasdaq, TASE | Merchant SiPh leader (mostly 200 mm); Japan 300 mm from 2027 | Total SiPh ~38-41% of ~$1.95-2.0B; 300 mm ~1-4% in 2026, ~12-35% by 2030 [E] |
| UMC | 2303 TWSE / UMC NYSE | 12-inch SiPh entrant (Singapore, SILITH) | <0.3% [E] |
| Samsung Electronics | 005930 / KRX | 300 mm SiPh from ~2027; CPO turnkey | ~0% |
| SMIC | 688981 SSE / 0981 HKEX | Possible 300 mm SiPh (unverified) | <0.5%, unverified |
| CanSemi (Yuexin) | private (IPO filed) | Chinese 12-inch SiPh line | unknown |
| Soitec | SOI / Euronext Paris | 300 mm photonics SOI (upstream indicator) | n/a |

#### Bear case and key risks
- **Technology substitution.** All shares and dollar effects are own estimates unless labeled.
  - **Copper keeps scale-up** (the largest lever).
    - At GTC-26, Jensen Huang said Nvidia will keep copper where it can.
    - Morgan Stanley reportedly sees 6-7M optical engines in 2027 against 20-30M expected [3P].
    - SemiAnalysis reportedly pushes large-scale CPO to 2028-29 [3P].
    - One analyst sees no CPO on AI ASICs before 2030: a 2% yield loss on a ~$60k ASIC is ~$1,200 of scrap per chip [3P].
    - LightCounting's base case has only 10-15% of scale-up links on NPO/CPO by 2030-31 [3P].
    - Bear assumption: copper keeps 90% or more of in-rack links, and CPO reaches only 25-40M ports.
  - **InP EMLs regain share.** Lumentum put the EML gap above 30% in May-26 [G]. Nvidia invested $2B each in Lumentum and Coherent [R]. Bear assumption: SiPh is ~45-50% of optics in 2030. Caveat: SiPh also needs InP CW lasers.
  - **TFLN at 400G/lane.** HyperLight launched 400G/lane TFLN PICs [G]. Bear assumption: TFLN takes 15-25% of sockets. Counterpoint: Tower and Coherent showed 420G on a silicon MZM in a production process [G].
  - **MicroLED/VCSEL links:** under 5% of links by 2030.
  - **Net effect:** -$1.0B to -$1.6B against the draft's $4.5B central. The fact-check corrections (one PIC per engine, the share double count) already overlap part of this.
- **Capex cuts.**
  - Scenario [E]: hyperscaler capex falls 20-30% in 2028. Module purchases then fall 30-45%, and 300 mm wafer starts fall 40-60% as module makers draw down banked die.
  - Result: 2028 revenue is $1.1-1.4B against ~$2.0B on a 50% path. Utilization drops to 35-55% and prices fall 15-25%.
  - LTAs soften but do not prevent this: prepayments cover only ~22% of 2027 contracts (290/1,300), and take-or-pay terms are undisclosed.
  - Program cuts [E]:
    - Copper-only Feynman: CPO PIC value of $0.15-0.45B.
    - A smaller AWS PIC100 program: ST at $0.1-0.25B.
    - GF missing its $1B target: GF 300 mm at $0.6-0.9B.
  - GF's Q3 guide already trailed consensus [R], and its CDC segment is only ~16% of revenue [R, secondary].
- **Chinese capacity.**
  - CanSemi's two 12-inch fabs ran 43.3k wpm at 96.4% utilization at end-2025, across all processes [R via media]. Its Phase 4 is RMB25.2B.
  - Its PICs appear qualified only in domestic programs (unverified).
  - Bear assumption [E]: Chinese lines take 10-15% of 300 mm SiPh volume by 2030, at 30-40% lower prices. That removes $0.2-0.4B and cuts commodity PIC ASPs 5-10%, in 2028-30.
- **Double-ordering and pull-forward.**
  - Capacity is being reserved: Tower holds reservations through 2028 and ST's expansion is reservation-backed.
  - InnoLight's orders cover all of 2026 [G], and the same module makers can book at Tower, GF, TSMC, ST and UMC.
  - Tower's 5x capacity can outrun InP laser supply. Estimate: 1-2 quarters of PIC die inventory by mid-2027 [E].
  - Late-Jul-26 rumors of 1.6T order and price cuts were denied [R]. Goldman raised its 1.6T+ forecasts in Sep-26 [3P].
- **Already priced in?**
  - TSEM is $203.94: +187% YoY and -36% from its $319.94 peak [R, IBKR]. Implied vol is 86%, and two 2x single-stock ETFs trade on it.
  - Tower's market cap is ~$23B (share count unverified), ~19x its $1.2B 2028 net-profit target [E].
  - GFS is $48.40: +43% YoY and -48% from its peak [R, IBKR].
  - Wedbush is Neutral [3P].
  - Conclusion: the 2026-27 tightness is priced in, CPO slippage is partly discounted, and the 2028-30 utilization and ASP risk is not in any company's guidance.
- **Bear-case numbers.**
  - 2030 size: $1.3-2.4B, central ~$1.8B.
  - CAGR: 10-28% (central ~19%) on the bear's $0.9B base, or 17-36% (central ~27%) re-based to $0.70B. If the base is $1.0B, the central is ~16%.
  - Mix: ~1.8x end-demand area x ~1.25x migration x ~0.89x ASP.
  - Probability: ~25% for a 2030 outcome of $2.4B or less. That includes ~8% for a deeper bust of $1.0-1.4B, which is 3-12% CAGR on $0.9B or 9-19% on $0.70B.
  - First warning sign: Tower's 2028 prepayments, due by Jan-2027 (visible in Q4-26 results, ~Feb-2027), arriving late, cut or renegotiated.

#### Leading indicators to watch (next 2-4 quarters)
1. Tower Q3-26 SiPh revenue (Nov-26; above ~$210M is on track), the Q4 $1B exit, the Jan-27 prepayments, any 200/300 mm revenue split, and a Track 2 agreement.
2. TSMC Q3-26 call (2026-10-16) and Taiwan press on PIC-line loading (below 50% is a warning) and the number of COUPE customers.
3. GF Q3 and Q4-26: confirmation of >2x SiPh, a 2027 guide, the AMF 300 mm timeline, and CHIPS award finalization.
4. InnoLight and Eoptolink Q3-26 inventory and contract liabilities (late Oct-26), and whether 1.6T ASPs fall more than 20% YoY.
5. CPO volumes (Spectrum-X, Bailly/Davisson), Lumentum and Coherent external-laser revenue, the Feynman NVLink choice, and LightCounting's next CPO revision.
6. Supply loosening: UMC and Samsung customer wins, the SiPh wpm in CanSemi's prospectus, the ST Crolles decision, and Soitec's photonics-SOI commentary.

#### Confidence and biggest unknown
**Confidence: low on size, medium that the CAGR exceeds 30%.** Direction is well supported: GF guides >2x, Tower has $1.3B of contracts, and the METI-certified plan is in place. Levels are not. No 300 mm wafer ASP is published, PIC area per module is unresolved, TSMC's output is unobservable inside COUPE, Tower does not split 200 from 300 mm, and no earnings-call transcripts were obtained (Alpha Vantage was rate-limited).

**Biggest unknown:** wafer ASP and PIC area per module, which move 2030 by about +/-$1B. Close behind are TSMC's real output and scale-up CPO timing. These decide whether 62-103k wpm of 2028-30 capacity is absorbed or turns into price erosion.

#### Sources
- Tower Semiconductor (SEC 6-K Ex. 99-1), "Q2 2026 results", 2026-08. https://www.sec.gov/Archives/edgar/data/0000928876/000117891326003776/exhibit_99-1.htm
- Nasdaq, "Tower Semiconductor Q2 earnings call highlights", 2026-08. https://www.nasdaq.com/articles/tower-semiconductor-q2-earnings-call-highlights
- MarketBeat, "Tower Semiconductor Q2 2026 earnings call", 2026-08-05. https://www.marketbeat.com/earnings/reports/2026-8-5-tower-semiconductor-ltd-stock/
- Tower Semiconductor IR, "Tower Semiconductor signs customer contracts ($1.3B silicon photonics)", 2026-05-13. https://ir.towerjazz.com/news-releases/news-release-details/tower-semiconductor-signs-customer-contracts-13-billion-silicon
- Tom's Hardware, "Tower Semiconductor revives shuttered Panasonic-era fab in $3 billion Japan photonics expansion", 2026-07. https://www.tomshardware.com/tech-industry/semiconductors/tower-semiconductor-revives-shuttered-panasonic-era-fab-in-3-billion-japan-photonics-expansion
- EE Times Japan, "Tower Japan SiPh plan (METI certification)", 2026-07-15. https://eetimes.itmedia.co.jp/ee/articles/2607/15/news058.html
- SBBIT, "Tower Japan METI-certified plan", 2026-07. https://www.sbbit.jp/article/st/186146
- Newswitch, "Tower Japan SiPh plan", 2026-07. https://newswitch.jp/p/49736
- DataCenterDynamics (citing Nikkei Asia), "Tower Semiconductor to establish large-scale optical chip hub", 2026-07 (45k wpm figure contradicted). https://www.datacenterdynamics.com/en/news/tower-semiconductor-to-establish-large-scale-optical-chip-hub-as-part-of-4bn-japanese-investment-pledge/
- MarketBeat, "GlobalFoundries Q2 earnings call highlights", 2026-08-05. https://www.marketbeat.com/instant-alerts/globalfoundries-q2-earnings-call-highlights-2026-08-05/
- TrendForce News, "GlobalFoundries reportedly sees silicon photonics revenue doubling in 2026, passing $1B by 2028", 2026-05-07. https://www.trendforce.com/news/2026/05/07/news-globalfoundries-reportedly-sees-silicon-photonics-revenue-doubling-in-2026-passing-1b-by-2028/
- Nasdaq, "GlobalFoundries maps path to 40% margins as silicon photonics demand builds", 2026 (month unverified). https://www.nasdaq.com/articles/globalfoundries-maps-path-40-margins-silicon-photonics-demand-builds
- TrendForce News, "TSMC PIC capacity seen surging to 25K wafers/month by 2028", 2026-07-08. https://www.trendforce.com/news/2026/07/08/news-tsmc-pic-capacity-seen-surging-to-25k-wafersmonth-by-2028-nvidia-broadcom-eyed-as-early-coupe-customers/
- nStock, "TSMC PIC capacity plan (citing TSMC VP)", 2026-08. https://www.nstock.tw/author/article?id=2263
- TechNews, "Silicon photonics hits the market: TSMC and ASE spearhead Taiwan's strategic push", 2026-03-17. https://technews.tw/2026/03/17/silicon-photonics-hits-the-market-tsmc-and-ase-spearhead-taiwans-strategic-push/
- DataCenterDynamics, "STMicroelectronics enters high-volume production of photonics chip", 2026-03. https://www.datacenterdynamics.com/en/news/stmicroelectronics-enters-high-volume-production-of-photonics-chip/
- MarketBeat, "STMicroelectronics Q2 earnings call highlights", 2026-07-23. https://www.marketbeat.com/instant-alerts/stmicroelectronics-q2-earnings-call-highlights-2026-07-23/
- LightCounting, "December 2025: AOCs, DACs, linear drive pluggable and co-packaged optics", 2025-12. https://lightcounting.com/newsletter/en/december-2025-aocs-dacs-linear-drive-pluggable-and-co-packaged-optics-320
- LightCounting, "May 2026: Silicon photonics, LPO/LRO and NPO/CPO", 2026-05. https://www.lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377
- LightCounting, "Silicon photonics, linear drive pluggable and CPO (updated Nov 2025)", 2025-11. https://www.lightcounting.com/newsletter/en/may-2025-silicon-photonics-linear-drive-pluggable-and-cpo-updated-november-2025-334
- TrendForce, "AI optical transceiver market $26B in 2026", 2026-04-20. https://www.trendforce.com/presscenter/news/20260420-13017.html
- TrendForce, "CPO switch shipments (Spectrum-X, Bailly)", 2026-07-27. https://trendforce.com/presscenter/news/20260727-13151.html
- Longport, "BofA summary: 800G/1.6T demand and SiPh penetration", 2026. https://longportapp.cn/topics/100000000796055
- The Register, "Nvidia optical scale-up", 2026-04-05. https://www.theregister.com/2026/04/05/nvidia_optical_scale_up/
- TechNews Finance, "UMC joins battle competing with Tower, GlobalFoundries", 2026-08-22. https://finance.technews.tw/2026/08/22/umc-joins-battle-competing-tower-globalfoundries/
- IThome, "UMC 12-inch SiPh mass production with SILITH", 2026-07. https://www.ithome.com/0/976/407.htm
- Daum (Korean press), "Samsung silicon photonics as early as 2027", 2026-07-15. https://v.daum.net/v/20260715161841087
- Sina Finance, "CanSemi IPO materials", 2026. https://t.cj.sina.com.cn/articles/view/1960136440/74d54ef8027085fm6
- TrendForce News, "InP shortage emerges as AI optical interconnect bottleneck", 2026-08-06. https://www.trendforce.com/news/2026/08/06/news-inp-shortage-emerges-as-ai-optical-interconnect-bottleneck/
- XenoSpectrum, "Lumentum InP AI optics shortage", 2026. https://xenospectrum.com/en/lumentum-inp-ai-optics-shortage/
- 10jqka, "1.6T order-cut rumors denied", 2026-07-31. https://stock.10jqka.com.cn/20260731/c678577708.shtml
- CNFin, "InnoLight orders, materials and 1.6T ASP", 2026-08-21. https://www.cnfin.com/gs-lb/detail/20260821/4458801_1.html
- 36Kr, "Morgan Stanley and SemiAnalysis on CPO timing", 2026. https://eu.36kr.com/en/p/3848056383542529
- TechNews, "Nvidia CPO ramp delayed; MS cuts FOCI", 2026. https://technews.tw/?p=1364145
- Passive Components EU, "February 2026 interconnect market insights", 2026-02. https://passive-components.eu/february-2026-interconnect-passives-and-electromechanical-components-market-insights/?amp=1
- Business Wire, "HyperLight introduces 400G-per-lane PICs on its TFLN chiplet platform", 2026-03-17. https://www.businesswire.com/news/home/20260317190165/en/HyperLight-Introduces-400G-per-lane-PICs-on-its-TFLN-Chiplet-Platform-for-Next-Generation-AI-Interconnects
- Converge Digest, "Tower Semiconductor and Coherent demo 400G/lane in SiPho", 2026. https://convergedigest.com/tower-semiconductor-and-coherent-demo-400g-lane-in-sipho/
- Chartmill, "GlobalFoundries dips after Q3 revenue forecast trails estimates", 2026-08. https://www.chartmill.com/news/GFS/Chartmill-52785-GlobalFoundries-NASDAQGFS-Dips-After-Q3-Revenue-Forecast-Trails-Estimates
- I amsterdam startup map (secondary), "GlobalFoundries stock swings as tiny 16% segment drives 62% growth", 2026-08. https://startupmap.iamsterdam.com/news/feed/globalfoundries-stock-swings-as-tiny-16-segment-drives-62-growth
- Xueqiu (post citing Goldman Sachs), "Goldman raises 1.6T+ shipment forecasts", 2026-09-07. https://www.xueqiu.com/9765902096/408289879
- Webull (Wedbush summary), "Wedbush on TSEM", 2025-12 / 2026-05. https://www.webull.com/news/15546552248886272
- Semiconductor Today, "Yole Silicon Photonics 2024" [STALE 2024-12], 2024-12. https://www.semiconductor-today.com/news_items/2024/dec/yole-171224.shtml
- Interactive Brokers, market data and company connections (TSEM, GFS, STMPA), accessed 2026-10-14/15. No public URL.


---

### 4.9 — #9 · HVLP4/HVLP5 electrodeposited copper foil for M8-M10 ultra-low-loss CCL (AI servers and switches)
*Megatrend: AI data-center compute and networking (224G/448G signal integrity) | 2026 -> 2030 revenue: $0.22-0.47B -> $0.7-2.1B | CAGR: 21-59% (central ~41%) | Growth mix: ~113% volume / ~-13% price | Confidence: medium*

**Definition.**
- **In:** electrodeposited (ED) copper foil sold at HVLP grade 4 or 5, mainly 12-35 um. Bonding-side roughness is roughly Rz <=0.5-1.0 um for HVLP4 and lower for HVLP5; grade cut-offs are vendor-specific. Buyers are CCL makers producing M8/M8.5, M9 and M10 laminates (EMC, Doosan, TUC, Panasonic, ITEQ, Shengyi). End uses are GPU/ASIC compute trays, NVLink switch trays, midplanes and backplanes, 51.2T/102.4T switch boards and 1.6T/3.2T optical-module boards. Revenue includes the copper pass-through; the ex-copper processing-fee pool is tracked as a secondary metric.
- **Out:** HVLP1-3, RTF/VLP, HTE, battery foil, carrier ultra-thin foil (mSAP/IC substrate), rolled-annealed and sputtered copper, the CCL itself, and glass cloth and resins.

**Value-chain path.** AI data-center capex -> GPU/ASIC racks (GB300, Vera Rubin, Rubin Ultra, TPU, Trainium) and 1.6T/3.2T switches -> high-layer-count PCBs (22-40+ layers) -> M8/M9/M10 CCL -> **HVLP4/5 ED copper foil** -> copper cathode (LME pass-through), cathode drums and surface-treater lines (the long-lead bottleneck).

**Drill-down decision.**
- **HVLP5 alone was rejected.** It is about $20-60M in 2026 [E, not re-verified], which fails the size floor, and it depends on M10/448G arriving in 2H27-2028+. Mitsui HVLP5 is in mass production [G]; Defu is sample-certified and Longyang is still in M10 validation [G].
- **HVLP4/5 for midplanes and backplanes was rejected.** Supplier data cannot separate it out. It is also now the most exposed slice: Kyber NVL144 has reportedly slipped to 2028 [3P].
- **Board mapping is disputed.** One source has Rubin compute trays on M6/M8.5 [3P]; another prices GB300/Rubin on M8 [3P, STALE 2025-09]. Some compute-tray area may therefore use HVLP2-3, which lowers HVLP4 content per rack.

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $0.22-0.47B (central ~$0.33B) [E] | $0.7-2.1B (central ~$1.3B) [E] | Central (1.31/0.328)^(1/4)-1 = **41.3%**. Low-low (0.70/0.22) 33.6%; high-high (2.1/0.47) 45.4%; central-2026 base to 2030 extremes 20.7% / 58.8%; cross extremes 10% / 76% (not meaningful) |
| Tonnage (HVLP4/5) | 6.5-10 kt (central 8.2) [E] | 27-52 kt (central ~39) [E] | ~47.7% |
| Blended ASP incl. copper | $34-47/kg (central $40) [E] | $26-40/kg (central $33.5) [E] | ~-4.3%/yr |
| Ex-copper fee pool | ~$0.13-0.34B (central $0.22B) [E] | ~$0.5-1.5B (central ~$0.86B) [E] | ~40.6% |

- **Volume vs price:**
  - In log terms, volume is ln(39/8.2) = 1.56 and price is ln(33.5/40) = -0.18, so volume is ~113% of growth and price ~-13%.
  - The price path is not monotonic. Goldman-implied HVLP3+ blended price rises from $26.5/kg (2025: $216M / 8.15 kt) to $38.4/kg (2028: $2.4B / 62.5 kt), about +13%/yr [3P].
  - The 2026 fee already includes 1H26 hikes of 5-10% [G, CTEE AGM]; a further 2H26 increase was flagged but not quantified.
  - From ~2028, fees should fall 20-40% as Chinese capacity, Co-Tech Plant 3 and Mitsui at 1,200-1,400 t/mo all land [E]. An HVLP5 premium partly offsets this.
  - Copper was about a third of the 2026 ASP. It is noise worth ~$40M of 2030 revenue per $1/kg.
  - Growth is front-loaded: ~60-75%/yr in 2026-28 (0.33 x 1.65^2 = ~$0.90B in 2028), then ~20%/yr in 2028-30 [E].

- **Top-down:**
  - **2026 board-level BOM [E]:**
    - AI high-layer board area is ~1.0-1.8M m2 (NVL72 ~9-12.6 m2/rack; switches and optics 0.15-0.3M m2).
    - With 50-75% of that on M8+, that is 0.5-1.35M m2.
    - Content: 22-30 layers x 60-80% of layers on HVLP4 x 0.11-0.16 kg/m2, divided by 0.65-0.75 for yield and utilization, gives 2.3-4.7 kg/m2.
    - Raw demand: **1.2-6.3 kt, central ~3.2 kt.**
    - Third-party demand run-rates are far higher: 1,300 t/mo in 2Q26 and 1,500-1,849 t/mo at end-2026 [3P, unverified], which annualize to 15.6-22 kt. Year-end run-rates are not annual averages.
    - Value is set from shipments: 6.5-10 kt x $34-47/kg = $0.22-0.47B.
  - **2030 [E]:**
    - Dongwu forecasts >110 kt of all-grade AI-server HVLP [3P]. At a 45-65% HVLP4+ share (the mix shifts toward M9/M10), that is 50-72 kt.
    - Own BOM: 2.6-9.7M m2 x 80-95% M8+ x 3-6 kg/m2 = 6-55 kt raw. Calibrated ~2x to 2026 shipments, that gives ~40-50 kt.
    - The bear haircut for cables, CPO and spec-down (-20-35%) gives ~30-45 kt.
  - **2030 scenarios (volume and price correlated):**

| 2030 scenario | Volume | ASP | Revenue |
|---|---|---|---|
| Low end of range | 27 kt | $26/kg | $0.70B |
| Tight supply (fees hold) | 28 kt | $38/kg | $1.06B |
| Central | 39 kt | $33.5/kg | $1.31B |
| High | 52 kt | $40/kg | $2.08B |

- **Bottom-up (2026, supplier volumes):**

| Supplier | Basis | HVLP4/5 volume |
|---|---|---|
| Mitsui | VSP 680-780 t/mo [3P, UAnalyze, haircut for the 620->840 t/mo capacity ramp] x 35-55% HVLP4/5 share [E, undisclosed] | 2.9-5.1 kt |
| Co-Tech | HVLP3+4 averaging 90-130 t/mo (>100 t/mo in June; 150 t/mo is the year-end target [G]) x 65-80% HVLP4 | 0.7-1.25 kt |
| Furukawa | Unverified | 0.5-1.4 kt |
| Lotte | | 0.1-0.5 kt |
| CFL | | 0.2-0.6 kt |
| China | Defu 70 t/mo HVLP4 in August [G], from a low base | 0.3-0.8 kt |
| Others | | 0.1-0.4 kt |
| **Total** | | **4.8-10.1 kt** |

  - Quarterly run-rate check: Q1 450-550, Q2 600-700, Q3 700-900, Q4 850-1,150 t/mo, which gives 7.8-9.9 kt [E].
  - Goldman interpolation: 679 x 7.667^(1/3) = ~1,339 t/mo of 2026 HVLP3+ demand, x 72% supplied x 45-55% HVLP4 = 5.2-6.4 kt [E].

- **Bottom-up (2030, capacity x utilization x HVLP4/5 share):**

| Supplier | Basis | HVLP4/5 volume |
|---|---|---|
| Mitsui | 1,250-1,400 t/mo calendar average (1,400 by FY2030, which ends Mar-2031 [G]) x 85-95% x 60-85% | 7.7-13.6 kt |
| Co-Tech | 700-1,000 t/mo x 80-90% | 6.7-10.8 kt |
| Furukawa | | 1.5-4.5 kt |
| Lotte | | 0.5-2 kt |
| CFL | | 0.5-2 kt |
| China | | 5-20 kt |
| Others | | 1.5-4 kt |
| **Total** | | **23-57 kt** |

  - US broker cross-check: Co-Tech is said to hold 21% of 2028 HVLP4 capacity [3P]. At ~700-750 t/mo for Co-Tech, that implies ~3,300-3,600 t/mo globally (40-43 kt/yr).

- **Reconciliation:**
  - **2026.** The base is set by supply, not by demand. The own BOM (~3.2 kt) sits *below* shipments (~8.2 kt), so either the BOM misses content (thicker layers, CPU/NIC/power boards, non-AI switching) or the channel is building inventory. The supply-constrained thesis rests on third-party gap figures, which conflict on units and scope.
  - **2030.** Demand (~30-72 kt) is at or above supply (23-57 kt). The swing factor is Chinese tonnage, which adds volume but cuts fees.
  - **Goldman cross-check.** Goldman's 2028 market of $2.4B, x 62% supplied x 60-70% HVLP4+ share, gives ~$0.9-1.05B [E]. That matches the ~$0.90B central 2028 path.
  - **Editor's widening.** The fact-check's 2030 low end ($0.8B) did not include the Kyber slip or the ASIC-on-HVLP3 evidence. Neither is decisive for 2030, so I widened the low end to $0.7B and trimmed the central from $1.35B to $1.3B rather than cutting harder.

#### Demand drivers and catalysts
- **224G-to-448G SerDes.** At 224G, foil roughness (skin effect) dominates the loss budget. M8/M9 needs HVLP4 and M10 needs HVLP5. Ongoing; 448G arrives 2028-29 (roadmap stage).
- **Vera Rubin ramp, 2H26-1H27, in progress.** HVLP4 demand reportedly went from 590 to 1,300 t/mo in 2Q26 [3P, unverified].
- **Co-Tech fees and mix.** Fees rose 5-10% in 1H26 with room for more in 2H26 [G]. Co-Tech exited HTE/standard RTF from 3Q26 [G]. September revenue was NT$1.104B, +64.6% YoY [R].
- **Co-Tech Plant 3.** Four HVLP4 lines (~600 t/mo) start 1Q27 and are fully open by 4Q27 [G].
- **Mitsui VSP capacity steps.** 840 t/mo (Sep-26), 1,000 (Sep-27), 1,200 (Sep-28) and 1,400 by FY2030 [G]. The Malaysia site (+1,200 t/mo from 2031) adds nothing before 2030 [G].
- **Kyber M9 midplanes: slipped to 2028.** SemiAnalysis says it slipped >12 months and Rubin Ultra reverts to Oberon NVL72 in 2027 [3P]. Downgraded from the draft's 2H27.
- **M10 + HVLP5.** Three CCL makers are in Nvidia testing for 2H27 mass production [3P]. Status: qualification.
- **ASIC racks moving from M7 to M8 (2026-27).** Partly offset: Co-Tech says ASIC platforms mostly use HVLP3 [G].
- **Coupling.** These drivers are shared with the quartz-cloth and M9-resin niches, so these are not independent bets.

#### Supply side
- **Suppliers and shares (2026 tonnage) [E]:**
  - Mitsui (VSP) ~50-60%
  - Co-Tech ~8-14% (US broker: 13% of capacity [3P])
  - Furukawa (FOX-WS) ~8-15% (unverified)
  - CFL ~3-7%
  - Lotte ~1-5%
  - China ~5-8%
  - Others ~2-5%
- **Capacity and lead times:**
  - New foil and treater lines take ~18-24 months from order to qualified output. Cathode drums and treaters are the bottleneck.
  - Yields: 70-80% at the leaders [3P]; Defu HVLP4 >60% [G].
  - Morgan Stanley gaps: 31% (2027) and 20% (2028) [3P]. Goldman HVLP3+ gaps: 28%/39%/38% for 2026/27/28 [3P].
- **Qualification barriers:**
  - The chain runs foil -> CCL -> PCB -> Nvidia/ODM and takes 9-18 months.
  - Each foil generation needs 6-12 months of validation; full system-level certification takes 1-3 years [3P].
  - Nvidia reportedly plans HVLP4 capacity directly with Co-Tech [R, year unverified].
- **Geographic concentration:**
  - 2026 output: Taiwan ~60-70% (most of Mitsui VSP, plus Co-Tech), Japan ~10-15%, China ~5-10%, plus Malaysia, Korea and Luxembourg [E].
  - China rises to 20-40% by 2030 (bear: 35-50%) [E].
  - Luxembourg blocked Defu's EUR174M takeover of CFL [R].

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| Mitsui Kinzoku | 5706 / TSE Prime | Leader; VSP HVLP4/5 | ~3-6% [E]; all copper foil was 17.8% of FY2025 sales (JPY135.0B / 758.5B) [R] |
| Co-Tech Development | 8358 / TPEx | No. 2 in HVLP4; highest-beta listed pure play | ~10-16% [E] (HVLP3+4 = 15-20% of revenue [G]) |
| Furukawa Electric | 5801 / TSE Prime | FOX-WS HVLP4-class supplier | <1% [E] |
| Lotte Energy Materials | 020150 / KRX | Korean HVLP entrant | ~1-5% [E] |
| Jiujiang Defu | 301511 / SZSE ChiNext | Leading Chinese HVLP4/5 challenger | ~1% in 2026 [E] |
| Anhui Tongguan | 301217 / SZSE ChiNext | Chinese HVLP1-4 supplier; ships mainly HVLP2 | <2% [E] |
| Jiangsu Longyang | 301389 / SZSE ChiNext | HVLP5 in M10 validation | <5% [E] |
| Circuit Foil Luxembourg | Private (Skylake fund) | European HVLP supplier | unverified |
| Elite Material (customer) | 2383 / TWSE | Dominant M8/M9 CCL maker; demand bellwether | 0% |

#### Bear case and key risks
- **Technology substitution.** No material replaces the conductor itself; the risk is architectural.
  - **Cabled racks:** Kyber has slipped to 2028, and Jefferies says the backplane could be cancelled in a worst case [3P]. Cabled Kyber-class designs are impractical (>20,000 cables, +30% weight [3P]), so this is mostly a deferral.
  - **CPO:** reaches 15-35% of scale-out switch ports by 2030 and removes 30-60% of the switch slice, which is ~10-15% of the niche [E].
  - **Spec-down:** ASICs use HVLP3 [G], and HVLP4 goes only on signal layers, so kg/m2 may be overstated by 30-50% [E].
  - **448G era:** PTFE hybrids and CoWoP pull demand toward out-of-scope foils.
  - **Net:** -20-35% of bull-case 2030 tonnage [E].
- **Capex cuts.** The niche is 85-95% AI data-center [E] and tied to new builds, so it swings harder than capex.
  - A 20-30% capex cut in 2028, plus four-tier destocking, could cut foil shipments 30-45% YoY.
  - 2028 HVLP3+ nameplate of ~4,000-6,000 t/mo [E] against Goldman's 5,206 t/mo of demand turns MS's 20% gap into a 5-20% surplus. Fees would reset within 2-3 quarters.
  - Result: 2028 revenue ~$0.45-0.65B; 2030 recovers to only ~$0.5-0.8B [E].
  - Jefferies sizes the Kyber slip at -5% (2027) and -11% (2028) of PCB/CCL demand, with a further -8% / -16% on CCL [3P].
- **Chinese capacity.**
  - Defu's 50 kt/yr high-end circuit-foil base starts batch output in 2Q27 [G]. That is ~4,170 t/mo of nameplate, ~2.5-3x the 2026 HVLP4 demand estimates.
  - The bear case says 20-30% of it at HVLP4+ gives 5-7.5 kt/yr. Editor's note: at nameplate that is 10-15 kt, so the bear figure implies ~50% utilization-yield.
  - Domestic AI (Ascend) can qualify Chinese foil without Nvidia's approval.
  - SMM HVLP1 fees are CNY55k/t (35 um) and CNY63k/t (18 um), about $7.7-8.9/kg [R].
  - Bear: the HVLP4 fee falls 45-60% to ~$12-16/kg, and China takes 35-50% of tonnage by 2030 [E].
- **Double-ordering / pull-forward.**
  - Nvidia's direct procurement runs alongside CCL-maker orders, so backlogs likely double-count.
  - Demand reportedly doubled within 2Q26.
  - Dongwu's 24 kt (2026) compares with ~8 kt actually shipped.
  - The own BOM (~3.2 kt) is well below shipments.
  - 10-20% of 2026-27 "demand" may be safety stock. That would cut the true 2027 gap to 10-20% and pull the supply-demand balance into 2028 [E].
  - Not yet confirmed: Co-Tech September was +4.5% MoM [R].
- **Already priced in?** Partly. The Kyber de-rating has happened, but fee compression is not priced.

| Stock | Move [R, IBKR weekly closes] |
|---|---|
| Mitsui | ~18x off the Apr-2025 low, now -55% from peak |
| Co-Tech | -32% from peak; ~54x annualized 2026 EPS (NT$5.82 x 12/8 = NT$8.73; NT$474.5 / 8.73) [E]; consensus target ~NT$735 [3P] |
| Defu | -51% from peak |
| EMC (customer) | Only -13% from peak |

- **Bear-case numbers.**
  - **2030:** $0.45-0.80B, central ~$0.60B, on 20-28 kt x $23-28/kg [E].
  - **CAGR:** 12.8% on the draft's $0.37B base, or **~16% on the corrected $0.33B base** (range ~8-25%).
  - **Decomposition:** volume ~+31%/yr, ASP ~-11%/yr.
  - **Probability:** ~25% (20-30%) that 2030 is <=$0.8B.
  - **Severe tail:** ~10% chance of <=$0.45B, a CAGR of <=~8% on the corrected base.
  - **Probability-weighted:** ~$1.15-1.3B, a CAGR of ~37-41% [E].
  - **First warning sign:** the SMM 35 um HVLP1 fee falling below ~CNY50k/t while copper is stable. Confirmation would be Defu HVLP4 shipments above 200 t/mo.

#### Leading indicators to watch (next 2-4 quarters)
1. **Co-Tech (8358) monthly revenue** (MOPS, around the 10th). Baseline: NT$1.104B. Two consecutive MoM declines while copper is flat would be a warning. Also watch the first Plant 3 line in 1Q27 and the 2027 fee talks (Dec-26 to Jan-27).
2. **SMM HVLP fee quotes.** Watch the HVLP1 fee trend and whether coverage extends to HVLP2-3.
3. **Mitsui 2Q FY3/27 results (Nov-2026).** Watch the VSP tonnage and mix disclosure, and whether the 1,000 t/mo step is pulled forward.
4. **Defu (301511) IR records.** Watch HVLP4 monthly shipments (baseline 70 t/mo) and whether the 50 kt base starts on time in 2Q27.
5. **EMC/TUC monthly revenue and inventory days against foil revenue.** A divergence would signal destocking.
6. **Nvidia GTC (Mar-2027).** Watch the Kyber rack form and M10 timing. A further M10 slip adds ~10 points to the bear probability.
7. **LME copper path.**

#### Confidence and biggest unknown
**Confidence: medium.** It is high on the direction: volume growth survives even the bear case at ~31%/yr. It is low on the absolute 2026 base.

**Biggest unknowns:**
- How far fees fall once Chinese HVLP4 qualifies in 2027-28.
- Whether 2026 shipments overstate consumption.
- Mitsui's undisclosed HVLP4/5 share of VSP, which is worth about +/-$0.1B on the 2026 base.

Rank it at ~41% central with a 30-50% band, front-loaded and exposed to the fee cycle after 2028.

#### Sources
- Reuters via Kitco, "Mitsui Kinzoku to build new Malaysia copper foil plant", 2026-08-17. https://www.kitco.com/news/off-the-wire/2026-08-17/mitsui-kinzoku-build-new-malaysia-copper-foil-plant-eyes-ai-driven
- EE Times Japan, Mitsui VSP/HVLP5 mass production, 2026-08-24. https://eetimes.itmedia.co.jp/ee/articles/2608/24/news043.html
- LOGI-TODAY, Mitsui VSP expansion plan, 2025-11. https://www.logi-today.com/877261
- UAnalyze, Mitsui 1,400 t/mo by FY2030, 2026-08. https://uanalyze.com.tw/articles/5513853560
- UAnalyze, Mitsui VSP monthly sales (undated). https://uanalyze.com.tw/articles/1455038528
- TechNews, Co-Tech September 2026 revenue, 2026-10-08. https://finance.technews.tw/2026/10/08/co-tech-8358-202609-financial-report/
- Commercial Times (CTEE), Co-Tech AGM, 2026-06-09. https://www.ctee.com.tw/news/20260609700179-430502
- Commercial Times (CTEE), Co-Tech order visibility, 2026-06-08. https://www.ctee.com.tw/news/20260608701135-430201
- Commercial Times (CTEE), HVLP3+ supply 18-20 kt, 2026-07-22. https://www.ctee.com.tw/news/20260722700191-439901
- Money Weekly, Co-Tech HVLP3/4 mix, 2026-08/09. https://www.moneyweekly.com.tw/_Article?AID=253625
- Edgen (Goldman Sachs summary), "AI server boom to create 3-year copper foil shortage", 2026. https://www.edgen.tech/fr/news/post/ai-server-boom-to-create-3-year-copper-foil-shortage-goldman-says
- Huxiu (GF Securities repost), HVLP4 demand 1,849/2,980 t/mo, 2026-08/09. https://www.huxiu.com/article/4857752.html
- Liberty Times, US broker on Co-Tech share, 2026-09. https://ec.ltn.com.tw/article/breakingnews/5576313
- 10jqka / Cailian, HVLP4 demand and certification cycle, 2026-06-16. https://news.10jqka.com.cn/20260616/c677494971.shtml
- 36Kr (Morgan Stanley), HVLP4 gaps, 2026-09. https://eu.36kr.com/en/p/3984081016470532
- Securities Daily via 10jqka (Dongwu), 2026-06-22. https://news.10jqka.com.cn/20260622/c677597332.shtml
- Defu IR record (CNINFO), 2026-09-09. https://static.cninfo.com.cn/finalpage/2026-09-09/1225555887.PDF
- Eastmoney brokerage report on Tongguan, 2026-08-27. https://pdf.dfcfw.com/pdf/H3_AP202608271828520480_1.pdf
- SMM, "SMM adds HVLP1 copper foil quote", 2026-07-31. https://news.metal.com/en/newscontent/104036510-smm-adds-hvlp1-copper-foil-quote
- Jefferies via fxbaogao, Defu/Tongguan initiation, 2026-06-15. https://www.fxbaogao.com/detail/5519144
- Jefferies via fxbaogao, PCB/CCL Kyber note, 2026-06-22. https://www.fxbaogao.com/detail/5492546
- TechTimes (SemiAnalysis), "Nvidia Kyber NVL144 slips to 2028", 2026-07-09. https://www.techtimes.com/articles/320033/20260709/nvidia-kyber-nvl144-slips-2028-physics-not-software-defeats-backup-plan.htm
- TechFlow, Kyber midplane stack, 2026. https://techflowpost.com/en-US/article/32179
- Substack, "The Board Beneath the Chip", 2026-03. https://abhayterminal.substack.com/p/the-board-beneath-the-chip
- TechNews, AI server material upgrade, 2025-09-05 [STALE 2025-09]. https://technews.tw/2025/09/05/2025-ai-server-material-upgrade/
- Mining Reporters (Cochilco), copper record, 2026-08-17. https://www.miningreporters.com/noticia/news/2026/08/copper-price-new-all-time-high-673-lb-london-cochilco
- Yicai Global, Defu ends CFL acquisition, 2026-01. https://www.yicaiglobal.com/news/chinese-copper-foil-maker-defu-slumps-after-ending-overseas-asset-acquisition-amid-local-govt-restrictions
- News Tomato, Lotte HVLP line, likely 2025 [STALE]. https://newstomato.com/ReadNews.aspx?no=1253439
- Wantrich / China Times, Co-Tech EPS and broker target, 2026-09-17. https://wantrich.chinatimes.com/news/20260917900210-420101
- IBKR company data and price history (5706, 5801, 8358, 301511, 2383), 2026-10-14 (no public URL).


---

### 4.10 — #10 · Transcatheter tricuspid valve replacement (TTVR) systems
*Megatrend: Ageing populations; structural heart disease moving to catheter therapy | 2026 -> 2030 revenue: $0.17-0.33B -> $0.45-1.10B | CAGR: 16-45% (central ~29%) | Growth mix: ~110% volume / ~-10% price | Confidence: low (high on direction, low on magnitude)*

**Definition.** In: catheter-delivered replacement valves for the native tricuspid position and their dedicated delivery systems, counted as manufacturer revenue. Products: Edwards EVOQUE (CE Oct-2023, FDA Feb-2024 [R]) and its next generation; Jenscare LuX-Valve and LuX-Valve Plus; Topaz, VDyne, Cardiovalve and Intrepid once they sell commercially; heterotopic caval valves (TricValve, Trillium). Out: tricuspid edge-to-edge repair (TriClip, PASCAL for TR), annuloplasty (K-Clip), TMVR (SAPIEN M3, Tendyne), tricuspid valve-in-valve with SAPIEN (booked in TAVR), surgical valves, imaging, pacemakers implanted after TTVR, hospital fees, and devices supplied to IDE trials (not commercial revenue).

**Value-chain path.** Ageing -> structural-heart devices -> transcatheter mitral and tricuspid therapies (Edwards' "TMTT" line) -> tricuspid -> **TTVR systems (bovine-pericardial valve on a nitinol frame plus a transfemoral steerable delivery system)**. Tissue, frame and catheter making is captive inside Edwards. The main payer is Medicare, under the 19-Mar-2025 NCD with Coverage with Evidence Development (CED) [R, STALE 2025-03].

**Drill-down decision.** I kept the product-class level. EVOQUE is about 95% of 2026 revenue [E], so narrower cuts either collapse into it or fall below the floor:
- Orthotopic-only TTVR is the same niche, because heterotopic devices are under 3% [E].
- Ex-US TTVR is about $30-85M in 2026 [E].
- China alone is under $20M [E]; no NMPA-approved TTVR exists.
- Upstream inputs are captive, so there is no merchant market to size.

The Phase-1 research ($0.25-0.5B -> $1.0-1.7B) was too high. It assumed EVOQUE was 55-70% of TMTT, but Edwards says PASCAL is the largest TMTT platform and EVOQUE the second [R].

#### Market size and math
| | 2026 | 2030 | CAGR 2026-30 |
|---|---|---|---|
| Revenue (range) | $0.17-0.33B (central ~$0.25B) [E] | $0.45-1.10B (central ~$0.70B) [E] | 16-45% (central 29.4%) [E] |
| Implants | ~4.1-7.3k (central 5.5k) [E] | ~12-24.5k (central 17.3k) [E] | central 33% [E] |
| Blended ASP | ~$41-45k (central $44k) [E] | ~$37-43k (central $40k) [E] | central -2.4%/yr [E] |

- **Volume vs price:**
  - Implants grow from 5.5k to 17.3k, a unit CAGR of (17.3/5.5)^(1/4)-1 = 33.2%. Blended ASP falls from $44.2k to $40.1k, -2.4% a year.
  - In log terms, volume contributes ln 3.15 = 1.15 against revenue growth of ln 2.86 = 1.05. That makes volume about 110% of growth and price about -10%.
  - The ASP decline is mostly geographic mix: the non-US share of units rises from about 27% to about 36%. US like-for-like price stays roughly flat until US challengers arrive around 2029-30. LuX-Valve Plus adds EU price pressure from 2027.
  - This is not shortage pricing: Edwards is adding TMTT capacity [R]. No public device price was found, so all ASPs are [E]. TriClip was more than 10% cheaper than EVOQUE [3P, STALE 2024].
- **Top-down (implants x ASP, [E] unless labelled):**
  - **2026:**
    - US: 3,000-5,040 implants (250-420 a month) x $46-50k = $138-252M. The anchor is the TVT Registry: 1,034 US cases at 82 centres between Feb-2024 and Mar-2025, about 74 a month [R; pre-NCD, STALE 2025-03]. I scale that by 3.4-5.7x after the NCD.
    - Europe: 800-1,700 x $31-37k = $25-63M.
    - China/RoW plus heterotopic devices: $5-15M.
    - Total: $0.17-0.33B. Central: 4,000 x $48k + 1,200 x $34k + $10M = about $0.24B.
  - **2030:**
    - US: 8,000-15,000 x $42-49k = $336-735M.
    - Europe: 3,000-6,000 x $28-35k = $84-210M.
    - China/APAC/RoW: 1,000-3,500 x $18-32k = $18-112M. The China benchmark is the K-Clip repair device at RMB 160-190k, about $22-26k [R, STALE 2025-03].
    - Total: $0.44-1.06B. Central: $506M + $138M + $50M = about $0.69B.
  - **Penetration:** low-single-digit share of severe TR (unverified); throughput and the repair/replacement split bind, not patients.
- **Bottom-up (Edwards residual plus entrants):**
  - **2026:**
    - TMTT guidance is $760-780M [G, raised 23-Jul-2026]. H1 actual was $173.0M + $195.9M = $368.9M [R], which implies about $196-206M a quarter in H2.
    - Start from TMTT of $760-790M. Subtract SAPIEN M3 at $25-70M [E] and PASCAL at $400-545M [E]. EVOQUE is the residual, trimmed to the range consistent with implant counts: $165-315M. Central: 775 - 45 - 485 = $245M [E].
    - Add Jenscare LuX-Valve at $3-8M [E] and others at $2-7M [E]. Jenscare's H1-26 group revenue was RMB 64.13M, +378% YoY but about 17% below H2-25, and mostly Ken-Valve [R].
    - Total: $0.17-0.33B.
  - **History check:**
    - TMTT grew from $352.1M (2024) to $550.6M (2025), +56.4% [R].
    - EVOQUE was about $42-60M in 2024 [E], which implies $125-195M in 2025, at least a doubling.
    - The only "EVOQUE >50% in 2025" datapoint is an IBKR AI summary, possibly TMTT's +56% misattributed [unverified]. If EVOQUE's 2025 growth really was ~50-60%, its 2026 revenue is $130-190M and the niche misses the floor.
    - That low path needs PASCAL growth of 43-68% in 2025 [E]. This is plausible, given Abbott cites rising competition in its US mitral business [R].
  - **2030:**
    - TMTT of $1.5-2.1B [E], a band around Edwards' $2B target [G]. Reaching $2B needs a 27.0% CAGR from $0.77B; $1.5B needs 18.1%.
    - EVOQUE share of TMTT: 30-45%, against about 21-41% in 2026. EVOQUE: $0.45-0.95B.
    - Add Jenscare at $30-135M and others at $10-60M.
    - Total: $0.49-1.14B. Central: 1.85 x 0.37 + 0.09 = $0.77B.
- **Reconciliation:**
  - **2026:** The two methods agree, but circularly: the residual is calibrated to the same registry pace. Only H1 (about 48% of guided TMTT) is reported; Q3 is due 4-Nov-2026. The 2026 range is mostly uncertainty about the EVOQUE/PASCAL split.
  - **2030 central:** Top-down $0.69B and bottom-up $0.77B give a base of about $0.73B. Weighting in the bear case (25% at $0.43B) and a bull case (15% at about $0.92B) gives about $0.70B.
  - **2030 range:** The low end is widened to $0.45B (draft $0.58B, fact-check $0.50B, top-down low $0.44B). The high end is $1.10B, following the fact-check.
  - **CAGR:**
    - Central: (0.70/0.25)^(1/4)-1 = 29.4%.
    - With 2026 held at $0.25B: $0.45B gives 15.8% and $1.10B gives 44.8%. This is the headline band, because 2026 error is attribution and does not move with 2030 adoption.
    - Correlated endpoints: 27.6% (0.17->0.45) and 35.1% (0.33->1.10).
    - Extreme crosses: 8.1% to 59.5%.
  - **Thresholds:** The $200M floor is met at the central case, with about 65-75% probability [E]. $1B+ in 2030 is reached in roughly the top 15-20% of outcomes [E].
  - The Yahoo "$250M/~40%" item is not used (probably TMTT growth).

#### Demand drivers and catalysts
- **Ageing, AF-driven TR:** registry patients averaged 77 years, 69% were women and 84% had atrial fibrillation [R]. Structural.
- **Coverage:** NCD effective since Mar-2025 [R].
  - NTAP began Oct-2024 [R, STALE 2024] and probably ended 30-Sep-2026 under the CMS 1-April anniversary rule [E].
  - The FY2027 IPPS final rule dropped 13 technologies [R]; EVOQUE's inclusion is unverified.
  - This is now a headwind, not the 2027 catalyst the draft described.
- **Evidence:** TRISCEND II 2-year data shows lower mortality and heart-failure hospitalisation [R], but TCTMD calls the mortality signal "hints" [R]. Registry 30-day mortality is 3.1% [R, STALE 2025-10].
- **Execution:** new centres, deeper use and simpler screening [R]; next-gen EVOQUE in development [G], timing unverified.
- **Edwards Q3-26 results, 4-Nov-2026 [3P]:** guidance implies about $196-206M TMTT a quarter. Pending.
- **PASCAL TR US approval and next-gen PASCAL, Q4-2026 [G]:** CLASP II TR data is due at TCT-2026 [R]. Negative for TTVR.
- **Edwards investor conference, early Dec-2026:** 2027 TMTT guidance and a possible EVOQUE breakout.
- **LuX-Valve Plus:**
  - EU MDR CE in Jul-2026 [R]; EU launch H2-26 to 2027.
  - Hong Kong approval is reported for Sep-2026 [R, Minichart], but one source attributes it to Ken-Valve, so it is conflicting.
  - NMPA previously declined a LuX-Valve filing and asked for more evidence [R, STALE 2024]. Approval timing is unverified.
- **US head-to-head pivotal trials against EVOQUE:** LuX-Valve Plus (IDE Feb-2026) and TRiCares TRICURE (IDE Apr-2026) both first enrolled in Jul-2026 [R]. Approvals around 2029-30 at the earliest [E].
- **Medtronic Intrepid:** early feasibility only (n=150, completion ~Sep-2026); no pivotal [R].

#### Supply side
- **Suppliers and shares:** Edwards has about 95-97% in 2026 and 80-90% in 2030 [E]. Jenscare has about 1-4% in 2026 [E]. Others are under 3%.
- **Capacity and lead times:** Capacity does not bind: Edwards is increasing TMTT capacity and no allocation has been reported [R]. Supply is by consignment [E, unverified]. A Feb-2026 HALMED field safety notice on the delivery system reported a 0.53% complaint rate [R].
- **Qualification barriers:** A US PMA needs a randomised trial. TRISCEND II took about 2020 to Feb-2024, which gives EVOQUE a US monopoly to about 2029. Further hurdles: CED and TVT Registry participation and centre requirements; EU MDR plus country-by-country reimbursement; NMPA.
- **Geographic concentration:**
  - Supply: the US (Edwards; site unverified), with challengers in China, France/Germany, Israel and Austria.
  - Demand: about 70-75% US, 20-25% Europe, under 5% China/APAC [E].
  - Japan is going repair-first: TriClip launched there in Q1-2026 [R], and no EVOQUE approval was found.

#### Key companies
| Company | Ticker / exchange | Role | Pure-play (% of revenue from niche) |
|---|---|---|---|
| Edwards Lifesciences | EW / NYSE | Incumbent; only US-approved TTVR; also sells substitute PASCAL TR | ~2.5-4.7% [E] (EVOQUE $165-315M vs ~$6.7B sales; FY25 $6,067.6M [R]) |
| Jenscare Scientific | 9877 / HKEX | No.2; LuX-Valve Plus CE; US pivotal trial | ~10-45% [E, unverified] (LuX-Valve $3-8M of ~$17-25M) |
| Abbott Laboratories | ABT / NYSE | Main substitute (TriClip); no TTVR | 0% |
| Medtronic | MDT / NYSE | Intrepid TTVR early feasibility study | 0% |
| TRiCares | Private | Topaz; TRICURE pivotal trial | ~100% |
| VDyne; Cardiovalve | Private | Clinical-stage (status not re-verified) | ~100% |
| P+F; Innoventric | Private | Heterotopic caval valves | ~100% |

#### Bear case and key risks
- **Technology substitution:**
  - From Q4-2026 Edwards sells repair (PASCAL TR, FDA approval guided for Oct-Dec 2026 [G]) as well as replacement, and can route TEER-suitable patients to the cheaper option.
  - New pacemakers: 14.9% at 30 days in the registry [R, STALE 2025-10] and 19.7% vs 9.0% at 2 years in TRISCEND II [R]. The mortality benefit is only "hints" [R].
  - TRILUMINATE showed no difference in mortality or HF hospitalisation [R, STALE 2024].
  - In the bear case, repair keeps 60-70% of US procedures in 2030 versus about 50-55% in the base case [E]. Each 10 points equals 2.5-4k implants, or $0.10-0.17B.
  - EVOQUE could be only 25-30% of TMTT in 2030.
- **Capex cuts:**
  - The NTAP cliff has probably already happened [E]. The FY2027 IPPS update was only 2.3% [R]. A ~$46-50k device [E] leaves a thin hospital margin under the base DRG (unverified).
  - Assume structural-heart budgets fall 20-30% in 2028 and new-centre activation halves. US growth then drops to 10-15% a year, giving 6-8k US implants in 2030, or -$0.20-0.35B versus the draft [E].
- **Chinese capacity:**
  - Only Jenscare is commercial, and it is thin: market cap ~HK$3.1B [R], H1-26 loss RMB 48.7M [R].
  - The risk is price, not volume: LuX-Valve Plus could undercut EVOQUE by 20-35% in the EU [E], and China faces VBP risk after 2028.
  - Net effect about -$0.02-0.06B [E]. Minor.
- **Double-ordering / pull-forward:** There are no LTAs and no shortage. The analogues are:
  - A prevalent-patient bolus: TMTT grew 56% in 2025 and 45% in H1-26 [R]; guidance implies H2 at 0-5% q/q and +32-39% YoY [E].
  - Medicare cases pulled into Q3-26 before NTAP lapsed.
  - Jenscare distributor stocking in newly CE-marked markets.
- **Already priced in?**
  - Edwards: $86.42 on 15-Oct-2026 [R]; consensus target about $100-101, range $85-110 [3P]; about 28-29x 2026 EPS guidance [3P]. TTVR is only 3-4.5% of EW sales [E], so the stock neither depends on nor protects the thesis.
  - Jenscare: HK$7.00, near its 52-week low and down 37% YoY [R]; challengers are already discounted. The real risk is that consensus 2030 TMTT is too high.
- **Bear-case numbers:**
  - 2030 size: $0.35-0.50B, central $0.43B [E]. US 6-8k x $44-46k = $0.26-0.37B; Europe 2.5-3.5k x $27-31k = $0.07-0.11B; China/RoW $0.01-0.03B. Cross-check: TMTT $1.3-1.5B x 25-30% + $0.03-0.06B = $0.36-0.51B.
  - CAGR: (0.43/0.25)^(1/4)-1 = 14.5%, range 8.5-22.8%.
  - Probability: about 25%, including a 5-8% severe tail of $0.25-0.32B (0-6% CAGR) from a safety action or CED tightening.
  - Probability-weighted CAGR: about 28%.
  - First warning sign: Q3-26 TMTT at or below ~$200M, or EVOQUE growth below the TMTT average. Confirmation would be 2027 TMTT guidance under $0.92B (+19%).

#### Leading indicators to watch (next 2-4 quarters)
1. Edwards Q3-26 TMTT on 4-Nov-2026: at or above ~$200M with "EVOQUE fastest-growing" commentary supports the base case.
2. Dec-2026 investor conference: 2027 TMTT guidance of $0.95-1.0B (+23-30%) supports the base case; below $0.92B supports the bear case. Watch for any EVOQUE breakout.
3. NTAP status for EVOQUE, and management commentary on hospital economics.
4. TVT Registry post-NCD volumes and 1-year outcomes. A US run-rate of 250-420 a month supports the 2026 range (corrected from the draft's 350-450).
5. Whether PASCAL TR is positioned as repair-first; CLASP II TR data; TriClip commentary.
6. Jenscare FY2026 (~Mar-2027): a LuX-Valve revenue line, EU implant counts and the NMPA decision.

#### Confidence and biggest unknown
Confidence is low on magnitude and high on direction: growth is volume-led and not shortage-driven. The biggest unknown is EVOQUE's undisclosed share of Edwards' TMTT revenue. A ±10-point error in that share moves 2030 by about ±$0.18B. Behind it sits the repair-vs-replacement split once Edwards sells PASCAL TR.

#### Sources
- Edwards Lifesciences / Business Wire, "Q2-2026 results", 2026-07-23. https://www.businesswire.com/news/home/20260723783980/en/
- SEC, "Edwards Q2-2026 8-K Exhibit 99.1", 2026-07-23. https://www.sec.gov/Archives/edgar/data/0001099800/000109980026000038/ex-991q22026.htm
- Nasdaq, "Edwards Lifesciences Q2 earnings call highlights", 2026-07-23. https://www.nasdaq.com/articles/edwards-lifesciences-q2-earnings-call-highlights
- MarketBeat, "Edwards Lifesciences Q2 earnings call highlights", 2026-07-23. https://www.marketbeat.com/instant-alerts/edwards-lifesciences-q2-earnings-call-highlights-2026-07-23/
- Edwards Lifesciences, "Q1-2026 results", 2026-04-23. https://www.edwards.com/newsroom/news/2026-04-23-edwards-lifesciences-reports-first-quarter-results-1bcd27a
- Edwards Lifesciences, "Q4-2025 results", 2026-02-10. https://www.edwards.com/newsroom/news/2026-02-10-edwards-lifesciences-reports-fourth-quarter-result-cbac793
- Yahoo Finance, "Edwards reports strong 2025", 2026-02. https://finance.yahoo.com/news/edwards-reports-strong-2025-despite-124418404.html
- Edwards Lifesciences, "2025 investor conference", 2025-12-04. https://www.edwards.com/newsroom/news/2025-12-04-edwards-lifesciences-reaffirms-strategy-for-sustai
- Business Wire, "FDA approves SAPIEN M3", 2025-12-23. https://www.businesswire.com/news/home/20251223559191/en/FDA-Approves-Edwards-Lifesciences-SAPIEN-M3-Mitral-Valve-Replacement-System-as-First-Transseptal-Transcatheter-Therapy
- ACC, "EVOQUE TVT Registry, TCT 2025", 2025-10-24. https://www.acc.org/latest-in-cardiology/articles/2025/10/24/16/56/sun-554pm-evoque-tct-2025
- TCTMD, "Real-world EVOQUE data reassure", 2025-10. https://www.tctmd.com/news/real-world-evoque-data-reassure-its-still-early-days-ttvr
- TCTMD, "Hints of mortality benefit at 2 years in TRISCEND II", date unverified. https://www.tctmd.com/news/hints-mortality-benefit-ttvr-2-years-triscend-ii
- TCTMD, "CMS agrees to reimburse TTVR", 2025-03. https://www.tctmd.com/news/cms-agrees-reimburse-transcatheter-tricuspid-valve-replacement
- MedTech Dive, "CMS proposes coverage for tricuspid replacement", 2024. https://www.medtechdive.com/news/cms-proposes-medicare-coverage-tricuspid-replacement/736190/
- Ropes & Gray, "FFY 2027 IPPS and LTCH final rule", 2026-08. https://www.ropesgray.com/en/insights/alerts/2026/08/ffy-2027-ipps-and-ltch-final-rule
- Federal Register, "FY2027 IPPS final rule", 2026-08-04. https://www.federalregister.gov/documents/2026/08/04/2026-15833/medicare-program-hospital-inpatient-prospective-payment-systems-for-acute-care-hospitals-ipps-and
- AppliedXL, "PASCAL TR FDA decision 2026", 2026. https://www.appliedxl.com/news/pascal-tricuspid-regurgitation-tr-fda-decision-2026
- MedTech Dive, "Abbott starts TriClip study amid rising competition", 2026. https://www.medtechdive.com/news/abbott-starts-triclip-study-amid-rising-competition-for-heart-valve-repair/826438/
- PMC, "TriClip FDA approval editorial", 2024. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11392211/
- GlobalData, "US transcatheter tricuspid repair market", 2024. https://www.globaldata.com/media/medical-devices/us-transcatheter-tricuspid-valve-repair-market-grows-56-qoq-since-launch-q2-2024-reveals-globaldata/
- DAIC, "TRiCares receives FDA IDE for TTVR pivotal", 2026-04-09. https://www.dicardiology.com/content/tricares-receives-fda-approval-ide-pivotal-trial-ttvr-valve-replacement-system
- ClinicalTrials.gov, "NCT04433065 Intrepid TTVR EFS", 2026 snapshot. https://clinicaltrials.gov/study/NCT04433065
- HALMED, "EVOQUE delivery system safety notice", 2026-02. https://www.halmed.hr/fdsak3jnFsk1Kfa/novosti/Sigurnosna-obavijest-obnova-uputa-za-upotrebu-i-oznacavanja-kod-sustava-za-uvodenje-trikuspidalnog-zaliska-EVOQUE.pdf
- 10jqka, "Jenscare LuX-Valve Plus CE MDR", 2026-07-08. https://stock.10jqka.com.cn/20260708/c678021455.shtml
- 10jqka, "Jenscare announcement", 2026-09-03. https://stock.10jqka.com.cn/20260903/c679574663.shtml
- 10jqka, "Jenscare announcement", 2026-09. https://stock.10jqka.com.cn/20260904/c679622011.shtml
- 10jqka, "Jenscare 2026 interim results", 2026-09-29. https://stock.10jqka.com.cn/20260929/c680379563.shtml
- Minichart, "LuX-Valve Plus gets Hong Kong DOH approval", 2026-09-05. https://www.minichart.com.sg/2026/09/05/jenscare-lux-valve-plus-gets-hong-kong-doh-approval-advances-global-tricuspid-valve-commercialization/
- STCN, "NMPA declines LuX-Valve registration", 2024. https://www.stcn.com/article/detail/1166283.html
- ITHome, "K-Clip NMPA approval", 2025-03. https://www.ithome.com/0/838/167.htm
- CIO在线, "China tricuspid device pricing", 2025-03. https://www.ciopharma.com/article/explain/1134
- Investing.com (Zhitong), "Jenscare 2024 results", 2025-03. https://cn.investing.com/news/stock-market-news/article-2729971
- Sohu, "Jenscare market report", 2026-10-09. https://www.sohu.com/a/1085647049_122123195
- Yahoo Finance, "Edwards earnings preview", 2026-10. https://finance.yahoo.com/healthcare/articles/know-ahead-edwards-lifesciences-earnings-163214721.html
- MarketBeat, "EW forecast", 2026-10. https://www.marketbeat.com/stocks/NYSE/EW/forecast/
- Yahoo Finance, "Edwards sees TAVR expansion" ($250M item, unverified), 2026. https://finance.yahoo.com/healthcare/articles/edwards-lifesciences-sees-tavr-expansion-110223267.html
- IBKR, company connections EW/ABT/MDT and price snapshots (MCP data, no URL), 2026-05 to 2026-10.


---

## 5. Too-early watchlist: niches whose volume ramps start after 2028

**How these were picked.** I started from 141 nominations. I kept five that combine a large plausible 2032 revenue pool, one nameable catalyst, and dated milestones that can be checked in 2026-28. I left out niches already on the longlist or in the deep dives (MLCP, e-SAF, dexterous hands, OCS, AC-to-800 VDC sidecars) and niches below the size floor (CNT pellicles, tactile skins). In all five, growth to 2032 is almost entirely volume, and unit prices fall [E].

| Niche | 2026 revenue | Volume inflection | What must happen first | 2032 range | Indicators to watch |
|---|---|---|---|---|---|
| Optical I/O chiplets for XPU scale-up | <$0.1B [E] | First revenue 2H27-28; broad volume 2029-30 | Scale-up domains outgrow copper's one-rack reach; XPU-level CPO proves reliable and serviceable | $2-12B (central ~$5B) [E] | Start of Marvell/Celestial revenue; Feynman NVLink-CPO supplier qualifications; Ayar Labs volume qualification by end-2027 |
| MV solid-state transformers (13.8-34.5 kV AC to 800 VDC) for AI data centres | $0.03-0.15B [E] | China small batches 2027; Western volume 2029-30 | 800 VDC racks in volume; UL/IEEE safety and utility-interconnection rules; field reliability data for 2.3-3.3 kV SiC | $1-6B (central ~$2B) [E] | Enphase demo (Nov-2026) leading to 2027 pilots; first named hyperscaler SST order; Chinese export orders |
| Glass-core (TGV) substrates for AI/HPC packages | <$0.1B [E] | 2029-31 | Pass package-level reliability; first named AI XPU or switch on glass | $1-5B (central ~$2.5B) [E] | Absolics reliability result and first purchase order; SEMCO-Sumitomo JV line decision; DNP FY2028 mass production |
| HALEU deconversion plus advanced-reactor fuel fabrication (TRISO, metallic) | $0.05-0.15B [E], mostly government | 2029-31 | HALEU supply; deconversion awards; NRC permits for the first Xe-100/Kairos/Natrium units | $0.3-1.5B fabrication value-add (~2x including material) [E] | DOE deconversion task orders; TX-1's first HALEU receipt; Long Mott construction permit |
| Sulfide solid electrolytes and Li2S | $0.03-0.15B [E] | 2029-31 | >=1,000 cycles; pilot yield >90%; electrolyte <$100/kg | $0.5-6B (central ~$2.5B) [E] | SMM LPSC/Li2S prices; Toyota/Idemitsu launch (2027-28); Samsung SDI Ulsan line (2H27) |

**1. Optical I/O chiplets for XPU scale-up.** *Scope:* optical engines co-packaged with XPUs or scale-up switches (Marvell/Celestial AI Photonic Fabric, Ayar Labs TeraPHY, Lightmatter, NVIDIA NVLink-CPO engines). *Excluded:* lasers, fibre attach and scale-out CPO, which are covered elsewhere.
- *Marvell timeline:* Marvell guides Celestial AI revenue from 2H FY28 (Aug-2027 to Jan-2028). It targets a $500M annualised run-rate in Q4 FY28 and $1B in Q4 FY29, about end-2028 [G, Dec-2025]. Celestial has one hyperscaler design win, and AWS holds a related warrant [R].
- *NVIDIA:* NVIDIA tied NVLink CPO to Feynman (2028) for 576-1,152-GPU domains, but keeps copper for the in-rack layer [R, GTC-2026 via The Register].
- *Ayar Labs:* says customers launch large-scale products in 2028-29, so its parts must be qualified by end-2027 [G].
- *My 2032 estimate:* 25-40M accelerator packages, 10-40% optically attached, $500-1,000 of content per package, plus engines on the switch side [E].
- *Cross-checks:* Marvell CEO Matt Murphy puts the scale-up optics TAM above $10B [G]. LightCounting's $10B for 2030 CPO engines (scale-up plus scale-out) [3P, Dec-2025] brackets the top of my range.

**2. MV solid-state transformers.**
- *Products are real, volume is not:*
  - Sungrow launched a 3 MW unit at a claimed 98.5% efficiency [R, Jul-2026].
  - Eaton offers a 2 MW, 15 kV-class unit [R].
  - Siemens and Reinhausen are developing a 36 kV unit (Aug-2026) [R].
  - Enphase demos in Nov-2026, runs pilots in 2027 and targets volume deliveries in 2028 [G].
- *China:* Chinese press reports 2.4 MW deliveries by China XD, 13.8 kV samples from Jinpan in US tests, and a Sifang order book above RMB3B [3P, unverified].
- *Citi:* sees SST-native builds from 2029 and 37,152 MVA of 2030 SST demand [3P, from Phase-1 research, not re-verified]. I treat that as upside.
- *Bear anchor:* MarketsandMarkets puts the US market at $154M in 2030 [3P, low quality].
- *My 2032 estimate:* 5-20 GW a year of SST-fed capacity × $120-250/kW, with the price falling [E].
- *Risks:* a conventional MV transformer plus an LV rectifier sidecar stays cheaper; operators choose ±400 VDC instead.

**3. Glass-core substrates.**
- *Absolics (SKC):* prototypes are with several US big-tech firms. Package-level reliability tests in Taiwan may report by year-end, and full-scale production has slipped to 2027 [R, Jul-2026 call]. The original target was 1H24.
- *SEMCO:* targeted 2027 [G, Nov-2025] but reportedly failed a reliability qualification at a comms-chip customer. Its line may not start construction until 2H27 [3P, The Elec, Aug-2026].
- *Others:* DNP plans to set up mass production in FY2028 [G]. Intel pushed its own use out to about 2030 [3P]. SEMI says meaningful volume is unlikely before about 2028 [3P].
- *Rejected:* claims of a ~$1B 2025 market [3P] contradict the absence of any high-volume production.
- *My 2032 estimate:* 5-15% of a $20-30B large-body AI substrate pool [E].
- *What pulls it in:* T-glass shortages, and package bodies above 120 mm where organic cores warp.

**4. HALEU fuel: deconversion and fabrication.**
- *TRISO-X:*
  - Received its NRC Part 70 licence in Feb-2026, three months early [R].
  - TX-1 is sized at 5 tU a year, about 700k pebbles or enough for up to 11 Xe-100s [G, Nov-2025].
  - First production has slipped to early 2028 [3P].
- *Long Mott (four Xe-100s at Dow Seadrift):* environmental assessment with a finding of no significant impact in May-2026; hearing in Sep-2026 [R].
- *BWXT:* its line makes "a few hundred kilograms a year" and fuelled Antares' Mark-0 to criticality. A commercial TRISO plant in Wyoming with Kairos is still under evaluation [R/G, Q2-2026 call].
- *Deconversion:* no commercial plant exists. DOE issued two task-order requests (max $80M each) in Jun-2026, not yet awarded [R, Centrus 10-Q].
- *Oklo:* A3F fuel facility 2027, Aurora INL 2028, Centrus HALEU from 2029 [G].
- *My 2032 estimate:* 10-35 tHM a year × $15-40k/kgHM of value-add [E]. Per-kg TRISO cost has no reliable source; Canary Media cites ~$30k/kg with unclear units [3P].
- *Substitute risk:* surplus plutonium, about a 20 t tranche [G, Oklo].

**5. Sulfide solid electrolytes and Li2S.**
- *Prices (SMM, Aug-2026) [3P]:*
  - Li2S fell more than 50% in six months to about RMB1,300/kg (~$180/kg).
  - LPSC is about RMB4,300/kg (~$600/kg).
- *Capacity:*
  - Idemitsu's 1,000 t/yr Li2S plant (enough for about 50-60k EVs) is due mid-2027 [G, STALE 2025-02].
  - Idemitsu took its investment decision on an electrolyte pilot plant in Jan-2026, for several hundred t/yr by end-2027 [R].
- *Launch dates:*
  - Toyota: 2027-28 [G].
  - Samsung SDI: Ulsan in 2H27 [3P].
  - CATL: small batches in 2027 [G], although its chief manufacturing officer says scale is at least five years away [3P, Sep-2026].
  - TrendForce: scaled supply in 2029-30 [3P].
- *SNE Research:* 45 GWh of sulfide all-solid-state batteries in 2030 and 275 GWh in 2035 [3P, date unverified].
- *My 2032 estimate:*
  - 25-100 GWh × 0.4-0.8 kg/kWh × $50-120/kg [E].
  - The intensity comes from Idemitsu's tonnes-per-EV figure, with Li2S at about 43% of argyrodite mass.
  - Volume grows more than 100x while price falls 80-90%.
- *Risk:* CATL and BYD make their own electrolyte instead of buying it.

**Considered, not selected:**
- Ac-225: depends on Phase 3 results, and the isotope revenue pool is probably below $1B in 2032 [E].
- REBCO tape: already has a revenue base, and fusion-plant demand arrives in the mid-2030s.
- Hollow-core fibre: one buyer dominates.
- TFLN: may inflect in 2028.
- Embedded microfluidic cooling: no product yet.

---

## 6. Overhyped: popular niches whose 2027-2030 revenue will disappoint

I picked these five because each was heavily promoted in 2026 and the gap between the story and the revenue can be checked with numbers. Being overhyped does not always mean a low CAGR. Two of these grow fast in percentage terms, but from tiny bases: they fail the size floor, or the value goes to someone else.

### 1. Humanoid actuator parts (planetary roller screws, harmonic reducers)
**Why it is popular.** This was the biggest A-share "Tesla-chain" theme of 2025-26. At least 17 listed Chinese firms have announced roller-screw (PRS) projects [3P, 2025 article, date unverified]. Leaderdrive (688017) had a market value of RMB 53.5-69.8B in Aug-Sep 2026 [3P], against 2025 revenue of RMB 571M and net profit of RMB 124M [R]. That is roughly 95-120x sales.

**The reality.**
- **Robot volumes are real but small.** Omdia counted about 13k humanoids shipped in 2025 [3P] and IDC about 25k in H1-26 [3P]. Full-year 2026 estimates run from UBS's ~30k to TrendForce's >50k [3P].
- **Tesla's output is mostly internal.** Optimus V3 output at Fremont has started. Secondary reports cite "several hundred per week" by August and a target above 1,000 per week, with most units used inside Tesla [3P, unverified].
- **Supplier revenue is still tiny.** Best (300580) booked RMB 0.22M of humanoid PRS sample sales, 0.03% of its revenue [R]. Leaderdrive's H1-26 revenue grew 38.6% to RMB 349M [R], helped by industrial-robot share gains, while gross margin fell 2.5 pp [3P].
- **The base business is industrial.** Harmonic Drive Systems' FY3/26 recovery (¥59.6B) came from industrial robots and chip equipment [R].

**The numbers [E].** 2030 pools:
- Humanoid PRS: $0.14-1.2B (central 600k robots × 8 screws × $85 = ~$0.4B).
- Humanoid harmonic reducers: $0.15-0.5B.

Together that is ~$0.7B in 2030, up from ~$0.1B in 2026, a CAGR of about 55-65%. All of that growth is unit volume, because ASPs fall 20-25% a year. Leaderdrive's reducer ASP already fell from ~RMB 1,900 to ~RMB 1,100 between 2017 and 2024 [3P]. The Unitree and AgiBot rotary-joint designs use no PRS. Even the bull case (~$2B in 2030, shared across dozens of suppliers) is well below Leaderdrive's ~$7.5-9.8B market value alone.

**What would change my mind.** Tesla or Figure selling more than 100k units a year externally by 2028, with 14 PRS per robot confirmed; or PRS prices holding above ~$150 after 2027.

### 2. Orbital / space AI data centers
**Why it is popular.**
- SpaceX, which merged with xAI in Feb-2026 [3P], filed with the FCC for up to one million compute satellites and tied its IPO story to orbital compute [3P, details conflict across outlets].
- Starcloud has raised $450M and was last valued at $2.3B, with NVIDIA as an investor [3P].
- Beijing plans more than 1 GW of compute in orbit [3P].
- A-share "太空算力" (space computing) stocks hit limit-up, including the loss-making Haoersai [3P].

**The reality.**
- **Through 2028 there are only demonstrations.** Starcloud-1 (one H100) flew in Nov-2025. Crusoe plans "limited GPU capacity" from early 2027 [3P]. Google plans two Suncatcher prototypes by early 2027 [R].
- **Launch is a hard limit.** Falcon 9 rideshare slots are unavailable after about late 2028, and the 200 kW-class Starcloud-3 needs Starship [3P].
- **The hardware is not ready.** Google found HBM to be the weakest part under radiation, and its CEO calls thermal management and on-orbit reliability open problems [R].

**The numbers [E].** I expect 2-20 MW in orbit by 2030. At ~$10-15M of revenue per MW-year (what GPU-cloud capacity earns on the ground), that is ~$20-300M. Terrestrial AI adds tens of GW a year. Cooling 1 MW in orbit also needs about 1,000 m² of radiator. This fails the size floor, and most of the money that does exist goes to launch providers.

**What would change my mind.** Starship flying routinely below ~$500/kg by 2028, plus a paying contract for at least 100 MW in orbit.

### 3. SMR developer/licensor revenue before 2030 (NuScale, Oklo)
**Why it is popular.** These are retail nuclear favourites. 2026 market-cap snapshots range from ~$10B to ~$40B for Oklo and ~$4B to ~$14B for NuScale [3P, conflicting].

**The reality.**
- **NuScale.** Q2-26 revenue was $0.1M, against $8.1M a year earlier [R]. ENTRA1's 6 GW / 72-module program with TVA is still not a definitive PPA [R]. Romanian (RoPower) revenue "could" start in 2027 if contracts are signed [G].
- **Oklo.** It has no revenue and an H1-26 net loss of $81.6M [R]. Operating cash burn guidance was raised to $120-150M, and Aurora-INL is still targeted to go live in 2028 [G].
- **Fabricators get the money.** BWXT describes itself as a "merchant supplier of large critical components for SMRs" [R]. GE Vernova added US BWRX-300 tech selects [R].

**The numbers [E].** Pure-play licensor revenue is under $20M in 2026. In 2030 it is $0.1-1.0B, and only if the TVA and RoPower deals reach final investment decision. Much of that would be module pass-through at thin margins. SMR heavy components (Doosan, BWXT) reach about $0.6-1.8B by 2030.

**What would change my mind.** A signed TVA PPA with firm module orders and deposits, a RoPower final investment decision in 2027, or Aurora-INL reaching criticality on schedule.

### 4. GaN as the 800 VDC winner (Navitas)
**Why it is popular.** NVIDIA's 800 VDC partner lists drove a rally in Navitas shares. Innoscience calls itself the only all-GaN 800 VDC supplier [G].

**The reality.**
- **Navitas is small and shrinking for now.** Q2-26 revenue was $10.5M, against $14.5M a year earlier. Full-year 2026 growth is guided only to mid-single digits [R/G].
- **It raised far more than it sells.** Navitas raised ~$373M in Q2, about 7-9x its annual revenue [R].
- **It is changing foundries at the worst time.** Navitas is moving from TSMC, which is exiting GaN, to PSMC 200 mm, with the 650 V parts moving over 12-24 months [G]. That is exactly when 800 V qualification happens.
- **Even the leaders' data-center GaN sales are small.** Innoscience's AI/DC GaN sales were RMB 63M in 2025 [R], and its H1-26 gross margin was 11.6% [R].

**The numbers.** Yole (Aug-2026) puts AI-led telecom/infrastructure GaN at $750M by 2031 (45% CAGR), inside a $3.5B market led by consumer [3P]. That implies about $0.1B in 2026 rising to about $0.5B in 2030 [E]. At a 5-10% share, Navitas would book $25-60M [E]. SiC takes the MV, sidecar and SST stages. This is real growth, but sub-$1B, and the market has picked the wrong winner.

**What would change my mind.** Navitas disclosing a Kyber or Rubin Ultra socket worth at least $50M a quarter by 2028, or Yole or TrendForce raising AI data-center GaN above $1B by 2030.

### 5. Immersion cooling for AI
**Why it is popular.** It is a KOSDAQ "액침냉각" (immersion cooling) theme (GST, K-Ensol) [3P], and generic "$X B by 2033" reports keep it in the news.

**The reality.**
- **NVIDIA chose cold plates.** Vera Rubin is fully direct-to-chip liquid cooled and fanless, using water at up to 45°C [R].
- **Analysts treat immersion as a niche.** Dell'Oro sees liquid cooling at ~$7B by 2029 with single-phase direct-to-chip dominant [3P], and calls immersion a crypto, research and government niche [3P, STALE 2025].
- **Two-phase has a fluid problem.** 3M is withdrawing Novec, and environmental groups dispute whether Chemours' replacement fluid is PFAS-safe [3P, STALE].

**The numbers [E, low confidence].** About $0.3-0.6B in 2026, mostly crypto and edge, rising to $0.4-1.0B in 2030. That is a ~5-20% CAGR, below a tenth of liquid-cooling spend.

**What would change my mind.** An NVIDIA or hyperscaler reference design that specifies immersion, or a PFAS-free two-phase fluid with OEM warranties.

### Also considered but not picked
- **HBM TCB bonders.** Cyclical, but the slip in hybrid bonding extends their runway.
- **eVTOL.** Certification keeps slipping, and Lilium and Volocopter both became insolvent [R, STALE 2024-25].
- **Hollow-core fiber.** Under $200M through 2028 [E].
- **Solid-state transformers by 2027.** Pilots only; volume comes in 2029 or later.

---

## 7. Sources

**Where the sources are.**
- **Deep dives (Section 4 and Appendix A).** Each deep dive ends with its own source list, with publisher, title, date and URL. Across the 18 deep dives they cite 720 distinct sources.
- **Longlist (Phase 1–3).** The 386 labelled claims behind the 50 longlist niches, with sources and dates, are in [Appendix B](appendix-b-longlist-evidence.md). The raw research records are in [`data/raw_candidates_phase1.json`](data/raw_candidates_phase1.json).

**Source-quality notes.**
- **Secondary write-ups.** Because primary sites could not be fetched, some citations are secondary write-ups of primary documents: earnings-call summaries on MarketBeat, Nasdaq or Motley Fool, or broker notes quoted in the press. The deep dives say so where a figure depends on one.
- **Earnings calls.** Alpha Vantage transcripts are cited as "Alpha Vantage transcript TICKER YYYYQn".
- **Company data.** Interactive Brokers data is cited as "IBKR company data". Neither has a public URL.
- **Asian sources.** Japanese, Korean, Taiwanese and Chinese outlets were used throughout, including Nikkei, Nikkan Kogyo, The Elec, Korea Economic Daily, Economic Daily News, Commercial Times, MoneyDJ, DigiTimes, TrendForce, Cailian Press, Eastmoney and company filings. Supplier commentary there often leads English-language coverage.

### 7.1 Sources for Section 5 (too-early watchlist)

- Marvell Technology (press release), "Marvell Completes Acquisition of Celestial AI", 2026-02. https://investor.marvell.com/news-events/press-releases/detail/1005/marvell-completes-acquisition-of-celestial-ai
- Insider Monkey (transcript), "Marvell Technology Q3 FY2026 Earnings Call Transcript (Celestial AI run-rate guidance, AWS warrant, >$10B scale-up optics TAM)", 2025-12. https://www.insidermonkey.com/blog/marvell-technology-inc-nasdaqmrvl-q3-2026-earnings-call-transcript-1654847/
- Lightwave, "Marvell's Celestial AI deal broadens its data center opportunity funnel", 2025-12 (approx.). https://www.lightwaveonline.com/home/article/55336796/marvells-celestial-ai-deal-broadens-its-data-center-opportunity-funnel
- The Register, "Nvidia optical scale-up (GTC 2026: Feynman NVLink CPO, copper in-rack)", 2026-04-05. https://www.theregister.com/2026/04/05/nvidia_optical_scale_up/
- remio.ai (secondary blog), "Ayar Labs funding hits $650 million as optical I/O faces its manufacturing test", 2026 (month unverified). https://www.remio.ai/post/ayar-labs-funding-hits-650-million-as-optical-i-o-faces-its-manufacturing-test
- The Register, "Nvidia-backed photonics startup Ayar Labs eyes hyperscale customers with GUC design collab", 2025-11-16. https://www.theregister.com/2025/11/16/ayar_guc_collab
- LightCounting, "LightTrends Newsletter, December 2025: AOCs, DACs, linear drive pluggable and co-packaged optics", 2025-12. https://lightcounting.com/newsletter/en/december-2025-aocs-dacs-linear-drive-pluggable-and-co-packaged-optics-320
- pv magazine, "Sungrow launches 3 MW solid state transformer", 2026-07-10. https://www.pv-magazine.com/2026/07/10/sungrow-launches-3-mw-solid-state-transformer/
- pv magazine USA, "Enphase announces distributed solid-state transformer for AI data centers, targets 2028 for volume deliveries", 2026 (Q1 earnings period). https://pv-magazine-usa.com/?p=20319
- HPCwire, "Siemens and Reinhausen develop direct current power solutions for AI data centers", 2026-08-14. https://www.hpcwire.com/off-the-wire/siemens-and-reinhausen-develop-direct-current-power-solutions-for-ai-data-centers/
- Tiger Brokers news (Chinese press repost), "从800V终极架构到千亿市场：SST固态变压器商业化前夜 (China XD, Sifang, Jinpan SST progress; unverified)", 2026. https://www.itiger.com/news/2645092828
- Sina Finance (Chinese press), "SST data-center coverage (Sifang SST1.0 2.4 MW; Jinpan 13.8 kV samples)", 2026-04-09. https://finance.sina.cn/stock/jdts/2026-04-09/detail-inhtwaii5993298.d.html?vt=4
- The Standard (HK), citing Citi Research, "AI data center power shift to 800VDC to reach 79pc adoption by 2030: Citi (via project research file; not re-verified in this run)", 2026 (month unverified). https://www.thestandard.com.hk/innovation/article/337678/AI-data-center-power-shift-to-800VDC-to-reach-79pc-adoption-by-2030-Citi
- MarketsandMarkets (low-quality market research), "Solid-state transformers for US data centers market", 2026. https://www.marketsandmarkets.com/PressReleases/us-data-centers-solid-state-transformers.asp
- Tom's Hardware, "Glass substrate roadmaps examined: Absolics in final qualification and a first product that keeps slipping", 2026 (mid-year, approx.). https://tomshardware.com/tech-industry/manufacturing/glass-substrate-roadmap-examined
- TrendForce, "SKC said to speed glass substrate mass production by year end; advances new non-embedding tech for U.S. client", 2026-05-08. https://www.trendforce.com/news/2026/05/08/news-skc-said-to-speed-glass-substrate-mass-production-by-year-end-advances-new-non-embedding-tech-for-u-s-client/
- LEDinside / TrendForce (citing The Elec), "Shinko Electric advances 22-layer glass substrates; Samsung Electro-Mechanics faces ramp-up uncertainty", 2026-08. https://ledinside.com/news/2026/09/2026_08_18_02
- Korea Herald, "Samsung, LG and SK see glass substrates as next upgrade in AI chip packaging, but mass production remains elusive", 2026 (month unverified). https://www.koreaherald.com/article/10771160
- Asia Economy (Asiae), "Samsung Electro-Mechanics targets $12 billion glass substrate market; in talks with big tech for supply", 2025-11-12. https://view.asiae.co.kr/en/article/2025111208594809544
- TrendForce, "DNP accelerates TGV glass substrate push with late-2025 pilot line, early-2026 sample shipments", 2025-12-22. https://www.trendforce.com/news/2025/12/22/news-dnp-accelerates-tgv-glass-substrate-push-with-late-2025-pilot-line-early-2026-sample-shipments/
- American Nuclear Society (Nuclear Newswire), "NRC grants license for TRISO-X fuel manufacturing using HALEU", 2026-02-17. https://www.ans.org/news/2026-02-17/article-7762/nrc-grants-license-for-trisox-fuel-manufacturing-using-haleu/
- Barchart (X-energy press release), "TRISO-X advances to next phase of construction for TX-1 fuel fabrication facility", 2026-08. https://www.barchart.com/story/news/3999417/triso-x-advances-to-next-phase-of-construction-for-tx-1-fuel-fabrication-facility
- Dow (press release), "NRC issues Environmental Assessment with Finding of No Significant Impact for Dow and X-energy's proposed advanced nuclear project in Texas", 2026-05. https://corporate.dow.com/en-us/news/press-releases/nrc-issues-environmental-assessment-with--finding-of-no-signific.html
- Centrus Energy / SEC EDGAR, "Form 10-Q for quarter ended June 30, 2026 (HALEU deconversion RFTOPs, two at a $80M ceiling each)", 2026-08. https://www.sec.gov/Archives/edgar/data/0001065059/000162828026053863/leu-20260630.htm
- BWX Technologies (earnings call via Alpha Vantage), "BWXT Q2 2026 earnings call transcript (TRISO line output, Antares Mark-0, Wyoming/Kairos TRISO evaluation)", 2026-08. https://www.alphavantage.co/query?function=EARNINGS_CALL_TRANSCRIPT&symbol=BWXT&quarter=2026Q2
- Oklo (earnings call via Alpha Vantage), "Oklo Q2 2026 earnings call transcript (A3F 2027, Aurora INL 2028, Centrus HALEU from 2029, surplus Pu)", 2026-08. https://www.alphavantage.co/query?function=EARNINGS_CALL_TRANSCRIPT&symbol=OKLO&quarter=2026Q2
- Canary Media, "Safer nuclear fuel gaining steam (TRISO cost ~$30,000/kg; units unclear)", unverified. https://www.canarymedia.com/articles/nuclear/safer-nuclear-fuel-gaining-steam
- AJOT (Reuters-based), "Japan's Idemitsu to build lithium sulphide plant to help support Toyota's EV plans [STALE 2025-02]", 2025-02. https://www.ajot.com/news/japans-idemitsu-to-build-lithium-sulphide-plant-to-help-support-toyotas-ev-plans
- battery-news.de, "Idemitsu starts construction of pilot plant for solid electrolytes", 2026-02-03. https://battery-news.de/en/2026/02/03/idemitsu-starts-construction-of-pilot-plant-for-solid-electrolytes/
- battery-news.de, "Samsung SDI plans mass production of solid-state batteries starting in 2027", 2026-08-03. https://battery-news.de/en/2026/08/03/samsung-sdi-plans-mass-production-of-solid-state-batteries-starting-in-2027/
- SMM (Shanghai Metals Market), "Sulfide prices continue to seek bottom; Zhejiang University's kilogram-scale synthesis breakthrough (Li2S ~RMB1,300/kg; LPSC RMB4,300/kg)", 2026-08. https://news.metal.com/newscontent/104068612-sulfide-prices-continue-to-seek-bottom-zhejiang-universitys-kilogram‐scale-synthesis-breakthrough
- SNE Research, "All-solid-state battery market outlook (122 GWh in 2030; sulfide 45 GWh in 2030 and 275 GWh in 2035)", unverified. https://sneresearch.com/en/business/report_view/215/page/0
- Stockstar (Chinese financial press; quote-to-article mapping not verified), "All-solid-state battery progress roundup (CATL small batch 2027 vs CMO 'at least five years' to scale; TrendForce 2029-30 scaled supply; BYD demo 2027)", 2026-10. https://wap.stockstar.com/detail/SS2026101000006993

### 7.2 Sources for Section 6 (overhyped list)

- NuScale Power (press release), "NuScale Power Reports Second Quarter 2026 Results", 2026-08-05. https://www.nuscalepower.com/press-releases/2026/nuscale-power-reports-second-quarter-2026-results
- SEC EDGAR (NuScale 8-K), "NuScale Power Corp Form 8-K, Q2 2026 results exhibit", 2026-08-05. https://www.sec.gov/Archives/edgar/data/0001822966/000182296626000086/a2026-08x05xnuscaleq2202.htm
- Pulse 2.0, "NuScale Partner Advances TVA Talks For Potentially Largest Nuclear Deployment Program In U.S. History", 2026-08-16. https://pulse2.com/nuscale-partner-advances-tva-talks-for-potentially-largest-nuclear-deployment-program-in-u-s-history/amp/
- Oklo (earnings call, via Alpha Vantage transcript), "Oklo Q2 2026 earnings call transcript", 2026-08. (Alpha Vantage earnings-call transcript; no public URL)
- BWX Technologies (earnings call, via Alpha Vantage transcript), "BWXT Q2 2026 earnings call transcript", 2026-08. (Alpha Vantage earnings-call transcript; no public URL)
- GE Vernova (earnings call, via Alpha Vantage transcript), "GE Vernova Q2 2026 earnings call transcript", 2026-07. (Alpha Vantage earnings-call transcript; no public URL)
- The Motley Fool, "2 reasons NuScale Power and Oklo investors should ...", 2026-02-27. https://www.fool.com/investing/2026/02/27/2-reasons-nuscale-power-and-oklo-investors-should/
- SEC EDGAR (Navitas 8-K), "Navitas Semiconductor Q2 2026 results, Exhibit 99.1", 2026-07-27. https://www.sec.gov/Archives/edgar/data/0001821769/000162828026049795/exhibit991-navitassemicond.htm
- Semiconductor Today, "Navitas Q2 2026 results coverage", 2026-07-29. https://semiconductor-today.com/news_items/2026/jul/navitas-290726.shtml
- Nasdaq / Zacks, "NVTS Shifts to 8-Inch GaN: Will it Help Return to Growth Trajectory?", 2025 (exact date unverified). https://www.nasdaq.com/articles/nvts-shifts-8-inch-gan-will-it-help-return-growth-trajectory
- Semiconductor Today (Yole Group Power GaN 2026), "Yole: power GaN market forecast to 2031", 2026-08-20. https://semiconductor-today.com/news_items/2026/aug/yole-200826.shtml
- Semiconductor Today (Yole Group Power GaN 2025), "Yole: power GaN market set for sixfold expansion by 2030", 2025-10-29. https://www.semiconductor-today.com/news_items/2025/oct/yole-291025.shtml
- HKEXnews (Innoscience 2577.HK), "Innoscience 2026 interim results announcement", 2026-08-28. https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0828/2026082803672.pdf
- HKEXnews (Innoscience 2577.HK), "Innoscience 2025 annual results announcement", 2026-03-27. https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0327/2026032704478.pdf
- Eastmoney PDF (Leaderdrive 688017 continuous-supervision report), "绿的谐波 2026年半年度持续督导跟踪报告", 2026-09-17. https://pdf.dfcfw.com/pdf/H2_AN202609171829519498_1.pdf
- Gelonghui (Soochow Securities note), "绿的谐波(688017)2026中报点评", 2026-08. https://m.gelonghui.com/news/5302857
- TMTPost, "绿的谐波 valuation and humanoid business article (market value, ASP history, humanoid share)", 2026 (exact date unverified). https://www.tmtpost.com/8108147.html
- 10jqka (Tonghuashun), "贝斯特:上半年公司人形机器人用行星滚柱丝杠相关样品实现营收22.30万元 业务规模较小", 2026-07-05. https://stock.10jqka.com.cn/20260705/c677955907.shtml
- Jiemian (TrendForce), "China humanoid robot output to surge 94% in 2026, TrendForce says", 2026. https://en.jiemian.com/article/14230176.html
- Webull News (IDC), "IDC: Global humanoid robot shipments in the first half of the year were close to 25,000 units, up 432.1% year-on-year", 2026. https://www.webull.com/news/15660109226968065
- AgiBot (citing Omdia), "Omdia Ranks AGIBOT No.1 Worldwide in Humanoid Robot Shipments in 2025", 2026-01. https://www.agibot.com/article/231/detail/33.html
- iTiger (UBS), "UBS Predicts Humanoid Robot Demand to Reach 30,000 Units by 2026", 2026 (exact date unverified). https://www-web.itiger.com/news/1196639791
- Shacknews, "Tesla (TSLA) Q2 2026 earnings results and conference call transcript", 2026-07-22. https://www.shacknews.com/article/150109/tesla-tsla-q2-2026-earnings-call-transcript
- Basenor blog (secondary, citing The Information), "Tesla Optimus Production Ramp: 6 Details That Matter", 2026-09. https://www.basenor.com/blogs/news/tesla-optimus-production-ramp-6-details-that-matter
- Monex Scouter (Harmonic Drive Systems 6324 disclosure), "ハーモニック・ドライブ・システムズ 決算 (FY3/2027 Q1, forecast revision)", 2026-08-07. https://scouter.monex.co.jp/news/detail/6324_20260807_act_20260807_160027_1
- Unite.AI, "Starcloud raises $250M Series A extension at $2.3B valuation", 2026-08-21. https://www.unite.ai/starcloud-raises-250m-series-a-extension-at-2-3b-valuation/
- DatacenterDynamics, "Crusoe to deploy in Starcloud satellite data center in late 2026, offer limited GPU capacity in space from 2027", 2025-2026 (exact date unverified). https://www.datacenterdynamics.com/en/news/crusoe-to-deploy-in-starcloud-satellite-data-center-in-late-2026-offer-limited-gpu-capacity-in-space-from-2027
- Google (The Keyword blog), "Project Suncatcher", 2025-11. https://blog.google/technology/research/google-project-suncatcher/
- W.Media, "SPECIAL FEATURE: SpaceX IPO puts spotlight on Musk's orbital data center plans and AI ambitions", 2026. https://w.media/?p=40806
- Gelonghui, "太空算力 concept-stock overview (A-share space computing theme)", 2026. https://m.gelonghui.com/p/4106011
- Fierce Network, "Dell'Oro has once again upped its liquid cooling forecast", 2025 [STALE 2025]. https://fierce-network.com/cloud/liquid-cooling-wave-building-faster-expected
- Webull News (Dell'Oro release, syndicated; URL-to-release mapping unverified), "Data Center Liquid Cooling Market to Approach $7 Billion by 2029, According to Dell'Oro Group", 2026-01. https://www.webull.com/news/14166934454436864
- IT Brief New Zealand, "NVIDIA's Rubin servers ditch fans for liquid cooling", 2026-01. https://itbrief.co.nz/story/nvidia-s-rubin-servers-ditch-fans-for-liquid-cooling
- Fierce Network, "Supercomputers can stay chill with hot water says Nvidia", 2026-01. https://fierce-network.com/cloud/nvidia-has-no-chill
- DatacenterDynamics, "Chemours launches two-phase immersion cooling fluid", pre-2025 [STALE]. https://datacenterdynamics.com/en/news/chemours-launches-two-phase-immersion-cooling-fluid
- Bullstory (Korean retail blog; used only as evidence of theme popularity), "액침냉각 관련주 총정리, 국내외 핵심 종목과 시장 규모 (2026)", 2026. https://bullstory.io/blog/액침냉각-관련주-총정리-국내외-핵심-종목과-시장-규모-2026

### 7.3 Sources for the top-10 challenger check (Section 3.4)

- Bloom Energy (SEC 8-K Ex.99.1), "Bloom Energy Q2 2026 financial results", 2026-07-28. https://www.sec.gov/Archives/edgar/data/0001664703/000162828026050150/ex991_q226financialresults.htm
- The Energy Mag, "Bloom Energy Reports $1.06 Billion in Q2 2026 Revenue", 2026-07. https://theenergymag.com/news/market-news/bloom-energy-reports-1-06-billion-in-q2-2026-revenue
- Jared Watkins Research, "Bloom Energy (NASDAQ: BE) behind-the-meter SOFC", 2026 (exact date unknown). https://www.jaredwatkins.com/research/datacenters/behind-meter-power/bloom-energy-sofc/
- Yahoo Finance, "Clear Street Raises Bloom Energy (BE) Estimates on Data Center Growth but Maintains Hold", 2026 (exact date unknown). https://finance.yahoo.com/news/clear-street-raises-bloom-energy-163352972.html
- Credo Technology Group, "Credo Reports First Quarter of Fiscal Year 2027 Financial Results", 2026-09. https://s205.q4cdn.com/511065572/files/doc_news/Credo-Technology-Group-Holding-Ltd-Reports-First-Quarter-of-Fiscal-Year-2027-Financial-Results-2026.pdf
- StockHub (Korea), "Credo FQ1-27 summary (AEC growth ~40%, 1.6T AEC FY28)", 2026-09. https://stockhub.kr/en/news/news_74bec30d7eee
- Zacks, "How are Active Electrical Cables Driving Credo's Growth?", 2026. https://www.zacks.com/stock/news/2947757/how-are-active-electrical-cables-driving-credos-growth
- TechNode Global (PR Newswire), "Hyosung Heavy Industries Secures Record Order as Hyun-Joon Cho's U.S. Strategy Pays Off", 2026-02. https://technode.global/?p=116960
- BizWatch (Korea), "Hyosung Heavy 765kV transformer/reactor US order (~KRW 787B)", 2026-02-10. https://news.bizwatch.co.kr/article/industry/2026/02/10/0021
- Korea JoongAng Daily, "HD Hyundai Electric secures $120 million contract for ultra-high-voltage transformers in U.S. Midwest", 2026-05. https://www.koreajoongangdaily.com/business/hd-hyundai-electric-secures-120-million-contract-for-ultra-high-voltage-transformers-in-us-midwest/12552118
- CEO Score Daily, "HD Hyundai Electric: 24 765kV transformers/reactors for largest Texas utility, delivery 2029 [STALE 2025-09]", 2025-09-22. https://ceoscoredaily.com/page/view/2025092213432517014
- Herald Corp (mbiz), "Hyosung ultra-high-voltage transformer orders from US tech companies (765kV/345kV) - as summarized, not opened", 2026-09 (approx.). https://mbiz.heraldcorp.com/article/10873576
- ERCOT, "EHV Infrastructure Initiative Update, September 2024 RPG [STALE 2024-09]", 2024-09-25. https://ercot.com/files/docs/2024/09/25/ERCOT_EHV_Infrastructure_Initiative_Update_September_2024_RPG.pdf
- Burns & McDonnell, "From bottleneck to breakthrough: how 765-kV transmission could save the grid [STALE 2025-09]", 2025-09-30. https://info.burnsmcd.com/benchmark/from-bottleneck-to-breakthrough-how-765-kv-transmission-could-save-the-grid
- Utility Dive, "MISO board approves 2024 MTEP / Tranche 2.1 with 765-kV backbone [STALE 2024-12]", 2024-12. https://www.utilitydive.com/news/miso-regional-transmission-expansion-plan-2024-mtep/735483/
- Texas Public Policy Foundation, "New 765 kV Transmission", 2026-05. https://www.texaspolicy.com/wp-content/uploads/2026/05/NEW-765-kV-Transmission_TPPF-1.pdf
- Public Utility Commission of Texas (AEP comments), "Docket 55249 filing: 765-kV vs 500-kV line cost per mile", unknown. https://interchange.puc.texas.gov/Documents/55249_7_1414447.PDF
- Energy-Storage.news, "LG ES ramps US BESS cell production, expects boost from non-China ITC eligibility rules", 2026. https://www.energy-storage.news/lg-es-ramps-us-bess-cell-production-expects-boost-from-non-China-itc-eligibility-rules/
- LG Energy Solution (via Placera), "LG Energy Solution Announces Start of Production at All-New Lansing Battery Plant", 2026-08-18. https://www.placera.se/pressmeddelanden/lg-energy-solution-announces-start-of-production-at-all-new-lansing-battery-plant-20260818
- Etica AG, "Treasury's Updated FEOC Guidance and Its Impact on Battery Energy Storage Systems (Feb 2026)", 2026-02. https://eticaag.com/treasurys-updated-feoc-and-its-impact-on-bess-feb-2026/
- ING Think, "US battery storage needs innovation for long-term growth (cites BNEF FEOC exposure)", 2026 (exact date unknown). https://think.ing.com/downloads/pdf/article/us-battery-storage-needs-innovation-for-long-term-growth
- Energy-Storage.news, "Lazard: US utility-scale energy storage LCOS has increased since restrictions on Chinese cells came into force", 2026. https://www.energy-storage.news/lazard-us-utility-scale-energy-storage-lcos-has-increased-since-restrictions-on-chinese-cells-came-into-force/
- Wccftech, "Ajinomoto to raise prices as ABF substrate supply-demand gap extends to 2027", 2026. https://wccftech.com/msg-maker-ajinomoto-to-raise-prices-as-abf-substrate-supply-demand-gap-extends-to-2027//amp/
- TrendForce, "MLCC turns from 'electronic rice' into a gold-like rally in Huaqiangbei", 2026-06-25. https://www.trendforce.com/news/2026/06/25/news-mlcc-turns-from-electronic-rice-into-a-gold-like-rally-in-huaqiangbei-with-quotes-reportedly-updating-every-30-minutes/
- 36Kr, "MLCC price hikes, Murata/SEMCO capacity and SEMCO MLCC revenue forecasts", 2026. https://eu.36kr.com/en/p/3845611027728640
- Newsquawk, "AST SpaceMobile Q2 2026: revenue $31.5mln vs exp. $34.5mln; FY revenue view $150-200mln", 2026-08-10. https://www.newsquawk.com/headlines/ast-spacemobile-asts-q2-2026-usd-eps--077-revenue-315mln-exp-345mln-fy-revenue-view-150-200mln-exp-1557mln
- Quartr, "AST SpaceMobile (ASTS) Q2 2026 earnings summary", 2026-08. https://quartr.com/events/ast-spacemobile-inc-asts-q2-2026_3YGj0Ert
- Boston Scientific, "Boston Scientific announces results for second quarter 2026", 2026-07-29. https://news.bostonscientific.com/2026-07-29-Boston-Scientific-announces-results-for-second-quarter-2026
- The Motley Fool, "Boston Scientific (BSX) Q4 2025 earnings call transcript", 2026-02-04. https://www.fool.com/earnings/call-transcripts/2026/02/04/boston-scientific-bsx-earnings-transcript/
- Medical Device Network, "Boston Scientific reports steady Q1 2026 performance yet tempers FY26 outlook", 2026-04. https://www.medicaldevice-network.com/news/boston-scientific-reports-steady-q1-2026-performance-yet-tempers-fy26-outlook/
- AuntMinnie, "Nusano launches commercial isotope operations", unknown. https://www.auntminnie.com/clinical-news/molecular-imaging/nuclear-medicine/article/15712227/nusano-launches-commercial-isotope-operations
- Applied Radiology, "Eckert & Ziegler Signs Agreement for 10 Year Supply of Lutetium-177 [STALE, ~2021]", ~2021. https://appliedradiology.com/Articles/eckert-ziegler-signs-agreement-for-10-year-supply-of-lutetium-177
- Medtronic (SEC 10-K), "Medtronic plc Form 10-K FY2026 (fiscal year ended Apr-24-2026)", 2026-06. https://www.sec.gov/Archives/edgar/data/0001613103/000162828026044354/mdt-20260424.htm
- MarketBeat, "Medtronic Q3 earnings call highlights", 2026-02-17. https://www.marketbeat.com/instant-alerts/medtronic-q3-earnings-call-highlights-2026-02-17/?.tsrc=rss
- BE Semiconductor Industries, "Besi Announces Q2-26 and H1-26 Results", 2026-07. https://www.besi.com/investor-relations/press-releases/details/be-semiconductor-industries-nv-announces-q2-26-and-h1-26-results/
- Bits&Chips, "Besi faces longer wait as SK Hynix pushes hybrid bonding to HBM5 (headline only, unverified)", 2026. https://bits-chips.com/?p=232321
- TrendForce, "ASE again raises 2026 capex to record US$10.5B, eyes 2x leading-edge advanced packaging revenue by 2027", 2026-07-31. https://www.trendforce.com/news/2026/07/31/news-ase-again-raises-2026-capex-to-record-us10-5b-eyes-2x-leading-edge-advanced-packaging-revenue-by-2027/
- The Motley Fool, "ASE (ASX) Q2 2026 earnings call transcript", 2026-08-07. https://www.fool.com/earnings/call-transcripts/2026/08/07/ase-asx-q2-2026-earnings-call-transcript/
- TVBS, "ASE share of TSMC outsourced CoWoS-S packaging (40-50% estimate)", 2026. https://news.tvbs.com.tw/english/3176845
- Axiomatic Research (Substack), "Advanced Packaging/Outsourced Assembly and Test (OSAT)", 2026. https://axiomaticresearch.substack.com/p/advanced-packagingoutsourced-assembly
- 21st Century Business Herald (sfccn), "Feilihua: quartz electronic cloth still in small-batch testing and certification", 2026-07-21. https://www.sfccn.com/2026/7-21/4NMDE0MDRfMjE4NjI4Nw.html
- Commercial Times (ctee), "Low-Dk / Q-cloth demand for M9 and Rubin (Taiwan quartz yarn maker 德宏)", 2025-12-05. https://www.ctee.com.tw/news/20251205700272-439901
- S&P Global Commodity Insights, "US DOE might finance long-lead nuclear reactor components for utility group", 2026-05-07. https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/050726-us-doe-might-finance-long-lead-nuclear-reactor-components-for-utility-group
- Financial News (fnnews), "DOE long-lead equipment financing and expected Doosan AP1000 orders", 2026-08-25. https://en.fnnews.com/news/202608250833109229
- World Nuclear News, "Poland begins ordering long-lead components for first AP1000", unknown. https://world-nuclear-news.org/articles/poland-begins-ordering-long-lead-components-for-first-ap1000

---

## Appendix C — Methodology and limitations

**Pipeline.** The research was run as a multi-agent pipeline in five rounds, using 111 analyst agents in total:
1. **Map and longlist.** 16 megatrend researchers, a completeness critic, 6 gap-fill researchers, a consolidator and a 3-lens scoring panel.
2. **Deep dives, three batches.** 13 niches.
3. **Final round.** 3 more deep dives; the overhyped and too-early analysts; a top-10 challenger; a 3-lens re-scoring panel; tree and table compilers.
4. **Challengers.** 2 challenger deep dives and an anchored re-scoring panel.

Each deep dive was built by four separate agents: researcher, fact-checker/quant, bear-case analyst and editor. Scorers worked independently, and the report uses their medians.

**Evidence channels and constraints.**
- **Direct web fetching was blocked.** Fetches to SEC EDGAR, company IR sites, TrendForce and other primary hosts failed in this environment (DNS/egress policy). Evidence therefore comes from:
  - web-search result summaries, which often quote primary documents;
  - full earnings-call transcripts via Alpha Vantage;
  - company profile data via Interactive Brokers.
- **Search was capped.** Web search was limited to 200 calls per research round, shared by all agents in that round.
  - The Phase-1 critic, gap-fill researchers and Phase-3 scorers ran largely without live search, so their numbers are often recalled and labelled unverified.
  - This is why every top-10 number was re-verified in Phase 4, and why Phase-4 figures supersede Phase-3 ones.
- **Niche revenue is rarely disclosed.** Most sizes are own estimates triangulated two ways: top-down (units × content × ASP) and bottom-up (supplier revenue or capacity). Ranges are reported as scenario-consistent pairs (low with low, high with high), with cross-paired envelopes noted where relevant.
- **Recency.** Figures published before ~October 2025 are tagged [STALE]. Several deep dives depend on the next one to two quarterly reports; those are named as leading indicators.

**What would most improve this report.**
1. Direct access to primary filings and research-firm data. Allow `sec.gov`, company IR domains and specialist research sites in the environment's network settings.
2. Supplier disclosure of niche revenue. HAMR, EVOQUE, base-die and SF6-free revenue are all undisclosed today.
3. A re-run after the Q3-2026 earnings season (late October to November 2026), which will update most of the leading indicators listed in the deep dives.
