# October 2026 pullback: where does it bottom?

Top-down assessment, as of the Oct 14, 2026 close plus overnight Oct 15, covering the S&P 500 → QQQ/XLK → SOXX/SMH → NVDA.

**Start with [FINAL_REPORT.md](FINAL_REPORT.md).** It has the verdict, the scenarios for each layer, the key levels, the catalysts, the verification notes and the sources.

| Folder | Contents |
|---|---|
| `data/` | `DATA_BRIEF.md` (the single source of truth for computed numbers); technicals, levels, breadth, base rates, betas and analogs (JSON/TXT); raw daily prices in `data/prices/` (Yahoo Finance; cross-checked against IBKR) and FRED series |
| `research/` | Research reports: the Oct 8 OpenAI story (narrative and skeptic), macro and rates, the catalyst calendar, semis leadership, sentiment and positioning, and the verification corrections |
| `analysis/` | For each layer: the bull brief, the bear brief and the judge's verdict (`*_verdict.md` and `.json`; the audit addenda at the end of each `.md` hold the corrected probabilities). Also the TSMC Q3 readout |
| `analysis/verify/` | Independent numbers audits for each layer, the external-fact re-verification, the cross-layer coherence and bias review, the completeness review, and the TSMC verification |
| `scripts/` | Python used to fetch data and compute the statistics |

Note: the `*_verdict.json` files were saved before the audits and carry the pre-audit probabilities. Use the audit addenda in the `.md` files, or FINAL_REPORT.md, for the corrected figures.

Not investment advice. The S&P 500 breadth data uses current constituents only (survivorship bias). The S&P 500 member price files are not committed because of their size; `scripts/fetch_yahoo.py` regenerates them.
