# VERIFICATION CORRECTIONS (independent fact check + numbers audit, ~04:00 UTC Oct 15) — these override conflicting text in other files

Full reports: analysis/verify/facts.md and analysis/verify/audit_market.md.

## External facts
1. Oct 28 FOMC hike odds: late-night Oct 14 pricing **~24–32%** (Polymarket 23.5%, Kalshi 23–24, Investing.com fed-funds monitor 27.6% at 11:25pm ET, Reuters/LSEG 31.6%). The "35%" was a 3:50pm snapshot; "~54%" was an intraday peak (and one 54.2% article is dated Sep 23). At least one more hike by Dec 9: **~82–91%** (not >95%). Fed hiked Sep 16 to 3.75–4.00% (CONFIRMED, federalreserve.gov); Warsh is Chair (CONFIRMED).
2. Sep CPI (CONFIRMED, BLS): headline +0.6% m/m was **in line**; the beats were headline y/y (3.7 vs 3.6) and core (0.3 vs 0.2 m/m; 2.6 vs 2.5 y/y).
3. Oracle's BBB− downgrade was **S&P on Jul 9, 2026** — NOT an Oct 14 catalyst. ORCL's Oct 14 drop was attributed to Project Jupiter spending/financing worries and CPI/yields.
4. SpotGamma: 7,700 is its "risk pivot"; its Oct 14 forward map shows negative gamma **below ~7,600** (and above ~7,900). "7,400 comes into view" not found. The CTA pivots (7,704/7,493/7,012) come only from a Tickmill post whose body does not name Goldman — single-source.
5. NVDA Q3 FY27 earnings date is **not announced**; third-party calendars say Nov 17, 18 or 25; realistic window **Nov 18–25**; notice expected ~late Oct. Do not anchor on Nov 17/18.
6. NVDA exposure (CONFIRMED, SEC 8-K Aug 17 + CFO commentary Aug 26): guarantees capped at $105bn for ~4.25 GW (OpenAI affiliate tenant; OpenAI reimburses NVIDIA for amounts paid; first phase FY29/ready-for-service 2028) plus $3.5bn existing = **$108.5bn** max gross; optional credit support for ~3.8 GW more at NVIDIA's discretion; supply/capacity commitments $279bn (primarily memory); total commitments $366bn plus $56bn AI-cloud/third-party leases. Q3 guide $108bn ±2%, GM 74% ±50bp; Q4 GM trough 71–72%; FY28 ~+70% "supply-constrained" (CONFIRMED, transcript).
7. OpenAI $70bn vs $50bn: two competing published explanations — (a) partner gross-up / Anthropic-comparable basis (Reuters, CNBC "$68bn included gross revenue from partners"), (b) investors extrapolating a ~$40bn August figure by OpenAI's stated +70% growth (Yahoo citing FT). Do not present gross-vs-net as settled. Bloomberg Oct 9: OpenAI expects ≥$70bn run rate by end-2026 on its own basis.
8. ASML −3.9% on Oct 14 is the **US ADR** move. Results CONFIRMED (6-K).
9. Maia 300 (Oct 12): "multi-gigawatt deployments beginning in 2027" is Microsoft's; "potentially >1M chips next year" is Reuters; "40% more tokens/MW" is a Microsoft projection.
10. CoreWeave: −15.46% Oct 14 (CONFIRMED); 2032 notes ~14.8% YTM intraday; overnight Reuters: 2032s **below 78c**.
11. Brent closes Oct 8–14: 104.28–106.65; Oct 14 settle 106.06; ~104.3–104.7 overnight on reports of US easing sanctions on oil vessels.
12. Earnings dates CONFIRMED: META Oct 21 AMC; LRCX Oct 21; MSFT Oct 28; GOOGL Oct 28 (call 4:30pm ET); KLAC Oct 28; AMD Nov 3 AMC (Election Day). AMZN not announced (~Oct 29 est.).

## NEW overnight news (after Oct 14 close)
- **Asia chip rout Thu Oct 15:** KOSPI −7.7%, Nikkei −4.8%, Taiex −3%; SK Hynix −11.4%, Samsung −9.5%, Kioxia −11.2%, Tokyo Electron −7.3%, SoftBank −9.4% (OpenAI exposure), TSMC (2330.TW) −2.0 to −2.2% ahead of results. Memory-led de-grossing is accelerating, not exhausting.
- IBKR ~03:55 UTC: NVDA 217.94 (−1.52%), SOXX 509.71 (−1.87%), TSM ADR 422.95 (−1.64%), ES Dec 7,730.5 (−0.51% vs 7,770.25 settle) ≈ SPX cash ~7,680 (fair-value estimate, UNVERIFIED) — i.e., the open is set up to test 7,700/7,704.
- TSMC Q3 results: not yet out as of ~04:00 UTC (due ~05:30–06:00 UTC).

## Market-layer numbers audit (see addendum in analysis/market_verdict.md)
- Corrected market probabilities ≈ **46% shallow (low ≥7,505) / 34% deeper (7,314–7,505) / 20% trend break (<7,314)**; median low ≈ 7,505. A tech-only break of 7,505 is possible (QQQ ≤ ~680 with RSP flat). Key level 7,505 close (+RSP 207.16); key event Oct 28.
- base_rates.json conditional statistics for thresholds BELOW 3% are selection-biased (episodes list starts at −3%); thresholds ≥3% are unaffected.
