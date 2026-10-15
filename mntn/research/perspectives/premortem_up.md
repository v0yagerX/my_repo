# Pre-mortem #2: it is December 2030 and MNTN trades at about $31, three times the $10.25 of Oct 2026

All 2027-2030 figures are scenario estimates. I ran the repo model (mntn/model/mntn_model.py) on a 50/50 blend of its base and bull driver inputs, with the $100M buyback carried out at about $10.5-13 a share. The script is premortem/triple.py.

## The causal story (looking back from Dec 2030)

**1. The stock re-rated because the company delivered, not because of AI hype (Nov 2026 to 2027).**
- In Oct 2026 the price assumed almost no growth: about 4.3x FY27E EV/EBITDA [estimate; K]. It implied FY27-30 revenue growth of about 0.6% a year at a 30% margin [estimate; model reverse DCF].
- Management had promised growth would pick up in 2H26 [B; Q2'26 call], and it did:
  - Q3'26 came in at the top of the $86-89M guide [guidance; B].
  - Q4'26 revenue passed about $108M.
  - The FY27 guide beat the $417.3M consensus [consensus; K].
- Customers active in the quarter had slowed to +24% y/y [reported; C, Q2'26 10-Q]. Growth picked up again as the rebuilt sales team, the agency channel and Express matured. Spend per active customer stayed within about −3% [estimate; C].
- Management spent the full $100M buyback, about 13% of shares [estimate; L], at $10.5-13. That retired about 8M shares before most investors believed the story.

**2. The AI creative funnel turned into paying customers.**
- The bear case treated QuickFrame AI as a free toy. It had 73K+ signups in 1H26 [reported; I] but implied conversion to paying customers of at most about 1-3% [estimate; I]. Express had only "hundreds" of paying customers [reported; B].
- In this story, near-free AI creative and Express's removal of minimums kept bringing in first-time TV advertisers, who are 95-97% of customers [reported; C].
- Small-business customers (trailing twelve months, TTM) rose from about 2,450 in FY25 to about 8,200 in 2030 [estimate].
- Revenue per TTM customer stopped falling at about $66-67K [estimate], against $74.2K in Q2'26 [estimate; C], because growing small businesses moved up to the Pro tier.
- QuickFrame subscriptions became a small revenue line of about $13M [estimate], inside dossier N's $5-20M bull range.

**3. MNTN became the neutral TV channel for small advertisers.**
- Every close rival was absorbed:
  - tvScientific by Pinterest, $465.1M, Feb 2026 [reported; G].
  - Vibe by Walmart, about $1.2B, Aug 2026 [third-party; G, WSJ].
  - Roku by Fox, closing in 1H27 [reported; E].
- Walmart never committed to keeping Vibe neutral [third-party; G]. In this story it pointed Vibe at Walmart Connect sellers. Direct-to-consumer brands outside Walmart, and their agencies, moved to MNTN.
- The networks were consolidating too (Paramount-WBD closed Oct 6, 2026 [reported; D]). They preferred a non-retailer small-business channel to handing that demand to Amazon or Google [E].
- "Guaranteed access" to live sports (World Cup, March Madness, "soon the NFL") [reported; D] built the Premium tier. Upper mid-market revenue grew from about $28M to $74M [estimate].
- Streaming CPMs fell ($25.90 vs $27.75 at the upfronts [third-party; D]). MNTN passed the savings to customers as better returns on ad spend rather than cutting price.
- The undisclosed take rate of about 35-50% [estimate; A] lost only 1-2 points, not the 5-10 points in dossier H's bear case.

**4. AI buying agents became a sales channel instead of going around MNTN.**
- MNTN's read-write MCP server, which lets AI agents create and manage campaigns, left beta [reported; F]. Agents comparing cost per acquisition across channels chose MNTN for brands that don't sell on Amazon, based on its Verified Visits results.
- Sales and marketing excluding stock pay (SBC) fell from about 29.6% of revenue in Q2'26 [estimate; F] to about 22.5% by 2030.
- Headcount grew far slower than revenue from 451 at mid-2026 [reported; M].
- Adjusted EBITDA margin reached management's 35-40% target [reported; K], with gross margin held near 80%.

**The resulting P&L [estimate]:**

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| Revenue ($M), y/y | 430 (+22%) | 520 (+21%) | 619 (+19%) | 726 (+17%) |
| Adj. EBITDA ($M), margin | 130 (30%) | 170 (33%) | 216 (35%) | 267 (37%) |
| GAAP EPS / adj. EPS | $0.90 / $1.23 | $1.27 / $1.66 | $1.71 / $2.15 | $2.22 / $2.70 |
| FCF ($M) | 95 | 115 | 143 | 176 |
| Diluted shares (M) | 75.6 | 72.9 | 71.8 | 70.6 |

**5. Earnings growth did most of the work; the multiple rose only modestly.**
- At $31, end-2030 enterprise value (EV) is about $1.69B [estimate]. That is about:
  - 5.8x 2031E EBITDA of about $290M;
  - 14x 2030 GAAP EPS;
  - an 8% FCF yield.
- That multiple is still below today's peer median of about 7.75x [estimate; O].
- How the price got there:
  - EBITDA grew about 2.9x.
  - About $317M of buybacks retired about 17.7M shares, taking diluted shares from 78.6M to 70.6M.
  - Net cash built to about $500M.
  - The multiple on next-twelve-month EBITDA rose from about 4.3x to 5.8x.
- The model's plain base case ($620M revenue and $208M EBITDA in 2030) also reaches $31, at about 7.4x [estimate]. So tripling only needs the base case delivered and believed, not the bull case.

**6. What did not happen.**
- Meta never scaled a TV offering.
- Amazon's AI ad tools (DVA+ and Ads Agent) stayed most useful for Amazon sellers.
- ChatGPT ads took mainly from search budgets.
- The 20-30% chance of a 2027 ad recession [estimate; J] either did not happen or the recession was shallow.

**The acquisition branch.** The same path leaves MNTN as the last large independent in this category, and an obvious target.
- The CEO has said he would have to hear out a legitimate approach [third-party; G, AdExchanger 2026-08-07].
- Class B shares control about 66% of votes: Greycroft 27.7%, Douglas 25.0%, MGD 15.5% [reported; L]. Those three holders decide any deal.
- Pre-IPO holders own about 44% of shares [estimate; L] and want to cash out.
- The CEO's 7.09M performance options only vest at share prices from $25.40 up [reported; L], so a bid below about $25 would be hard for him to accept.
- Likely buyers:
  - AppLovin, which calls TV advertising its "step three" [reported; O];
  - a merged network group that wants small-business demand;
  - Adobe, through its GenStudio creative product;
  - a private-equity buyer at the DV/IAS precedent of about 8-9x EBITDA [estimate; O].
- On this path, a bid at about 9x 2029E EBITDA at end-2028 gives about $31. A 2027 bid at 10-11x 2028E EBITDA would give only about $26-28 [estimate].

## Early confirming signs (2026-2028)

| # | Signal | Confirms the 3x path | Breaks it | Starting point |
|---|---|---|---|---|
| 1 | Revenue delivery | Q3'26 ≥ $88.5M; FY26 ≥ $353M; FY27 initial guide midpoint ≥ $425M | Q3 ≤ $87.5M, or FY27 guide < $410M | Guide $86-89M; FY27 consensus $417.3M [K] |
| 2 | Customer growth | Customers active in the quarter ≥ +28% y/y in some 2027 quarter, with spend per active customer no worse than −3%; TTM net adds ≥ 450 a quarter | Active-customer growth < +20%, or net adds < 250 | +24% (Q2'26); net adds 242 / 351 [C, N] |
| 3 | Funnel conversion | ≥ 1,000 paying Express customers by Q4'27 (≥ 2,500 by Q4'28), or disclosed QuickFrame AI to paid conversion ≥ 3% | Still "hundreds" at end-2027 | "Hundreds"; ≤ 1-3% implied [B, I] |
| 4 | Pricing / take rate | Gross margin ≥ 78% every quarter; receivables / quarterly revenue ≤ 0.80; customer concessions < 1% of revenue; disclosed expansion rate or true retention ≥ 110% | Gross margin < 77%, or a new rebate or pricing disclosure | Gross margin 80.3%; receivables ratio 0.73; concessions $2.65M [H] |
| 5 | Cheaper customer acquisition | S&M ex-SBC ≤ 27% of revenue in FY27 and ≤ 25% in FY28, with growth ≥ 20%; new revenue per S&M dollar ≥ 0.9x; any disclosure of customers sourced through AI agents | S&M ex-SBC > 30% while growth < 18% | 29.6%; 0.72x [F, C] |
| 6 | Operating leverage | Adj. EBITDA margin ≥ 30% in FY27 and ≥ 33% in FY28; headcount ≤ about 520 at end-2027 | FY27 margin ≤ 27% | FY26 guide about 28%; 451 staff [K, M] |
| 7 | Buybacks and dilution | Q3'26 10-Q shows ≥ $20M repurchased; ≥ $90M done by Aug 2027 and the program renewed; diluted shares ≤ 75M by Q4'27; SBC ≤ 7% of revenue | Buyback largely unused; diluted shares > 79M | 78.6M diluted; SBC 7.2% TTM [L] |
| 8 | Neutral-channel tells | Walmart narrows Vibe to its own ecosystem or raises its $50/day minimum; MNTN confirms NFL, Netflix or Prime Video inventory; Adobe or Google names MNTN as a launch partner; third-party data (Northbeam) shows MNTN spend ≥ +40% y/y; web traffic rank (Tranco) back below about 2,700 | Meta launches self-serve TV ads for small businesses; Amazon discloses small-business streaming-TV adoption at scale | Northbeam: MNTN +29% vs Vibe +1,900% (H1'26); Tranco average 3,169 [G, M] |

## Probabilities [estimate]

**Chance the stock is at or above about $31 in Dec 2030, including takeover proceeds: about 20% (range 15-25%).**

| Path | Chance of the path | Chance of reaching $31 on that path | Contribution |
|---|---|---|---|
| Bull-like: 2030 revenue ≥ about $720M at ≥ 36% margin (needs only about 5.8x) | ~20% | ~75% | ~15 pts |
| Base-like: $580-720M (needs about 7.4x, versus about 4.3x today) | ~35% | ~20% | ~7 pts |
| Weaker paths | ~45% | ~1% | ~0.5 pt |

- The 20% bull-like weight is the model's own bull weight; dossier E gives about 40% to its "threat contained" path, which reaches about $705M in 2030.
- The total is about 22%, which I round to 20%. About 5 points of it come through a takeover.
- For reference, the model's own base case valued at 7x gives $29.77 at end-2030 (2.9x).

**Chance of a takeover announced before end-2030, at any price: about 25% (range 15-35%).**
- For: rivals and Roku were absorbed in 2025-26; the EV is small at about $0.5B; precedents exist; the CEO is open to a legitimate approach; pre-IPO holders are selling.
- Against: the Class B block and the CEO's $25.40 option hurdle; the natural buyers have already bought rivals; Amazon and Google face antitrust limits.
- Chance of a takeover at $31 or more: about 5%. The most likely bid range is $15-25, against precedent-based values of about $12-17 today [estimate; O].