# Numbers audit: nvda_verdict.md and nvda_verdict.json

*Auditor: audit_nvda. Run at about 04:35–05:10 UTC on Oct 15, 2026.*

**What I audited**
- The verdict was **revised while I worked**. The md changed at 04:31 UTC and the JSON first appeared at 04:32 UTC. I audited the current versions: md 25,409 bytes, 358 lines; JSON 20,179 bytes.
- The revision updated [SV] to the audited 26/37/37. It also changed the earnings-date wording to "Nov 17, 18 or 25" and added "36 sessions; Nov 27 half day".

**How I checked**
- Every number was recomputed with my own code in `scratchpad/audit_nvda/a1.py` through `a8.py`.
- Data: `data/*.csv` (Yahoo, through the Oct 14 close) and `dl_nvdabull/*.csv` (long history). The long NVDA file matches `data/NVDA.csv` exactly over the 1,254 shared sessions (maximum difference 0.0).
- I read `nv_scripts/v2.py` only to learn the signal definitions, then wrote independent implementations. My implementations use exact bucket edges: 210/239.24 − 1 = −12.222% and 190.01/239.24 − 1 = −20.578%. The verdict's scripts round these to −12.2% and −20.6%.

---

## A. Re-run of the load-bearing base rates (independent code)

| # | Computation (verdict §3 and §5) | Stated | My result | Reproduces? |
|---|---|---|---|---|
| 1 | Record-close episodes reaching −7.5%, 3 years | n=11, 45/36/18 | n=11, median −13.41%, 45/36/18 | **Yes** |
| 1a | Same, conditioned on −8.7% | n=9, 33/44/22 | n=9, 33/44/22 | **Yes** |
| 1b | 5 years including 2022, from −7.5% | n=14, median −16.15%, 36/43/21, 36% shallower than −10%, median 13.5 extra sessions | n=14, median −16.13%, 36/43/21, 36%, 13.5 | **Yes** (DB rounding) |
| 1c | 5 years excluding 2022 | n=13, median −14.0%, 8 of 13 at −13.4% or worse | n=13, median −13.98%, 8 of 13 | **Yes** |
| 1d | 5 years from −8.7% | n=12, 25% shallower than −10% | n=12, 25% (25/50/25) | **Yes** |
| 1e | Since 2016, from −7.5% | n=31, 26/55/19 | n=31, 26/55/19 | **Yes** |
| 1f | Bull: 5 of 11 ended at −7.6% to −9.7%, bottoming 2/0/0/0/3 sessions after the first −7.5% close | — | −9.73 (2), −8.70 (0), −7.62 (0), −8.81 (0), −9.28 (3) | **Yes** |
| 2 | 36-session set: record drawdown in (−10%, −7.5%], above a rising 200-day, de-clustered at 10 sessions, 2016– | n=75, 33/49/17 | n=75, 33/49/17 | **Yes** |
| 2a | Same, 2021– | n=44, 30/48/23 | n=44, 30/48/23 | **Yes** |
| 2b | Same + below the 50-day | n=27, 37/48/15 | n=27, 37/48/15 | **Yes** |
| 3 | Holdout: SOXX ≥15% off its 1-year high, NVDA 5–10% off its record | n=12, 42/33/25, median −13.9% | n=12, 42/33/25, −13.9% | **Yes** |
| 3a | Holdout using NVDA's 1-year high, 2010– | n=17, 47/29/24 | n=17, 47/29/24 | **Yes** |
| 3b | SOXX ≥10% off its 60-day high, NVDA 6–10% off its record | n=14, 36/50/14 | n=14, 36/50/14 | **Yes** |
| 4 | Driftless t(4) Monte Carlo, 33% vol, ±5.8% earnings jump, 36 sessions | 37/41/22; from 218.25: 30/44/26 | 37/40/22; 30/44/26 (normal innovations: 35/41/24; 28/44/29) | **Yes** |
| 5 | Betas and ratios, 1 year | 1.30/0.68; 0.48/0.59; 1.89/0.64; ratio 0.57 (n=54); through origin 0.54; OLS 0.38; down/up 0.56/0.30; QQQ down-day 1.41; QQQ < −1% ratio 1.41; SOXX < −3%: 1-year median 0.60 (n=34), 5-year 1.01 (n=113); 5-year beta about 1.0 | identical (5-year beta 1.02) | **Yes** |

**Robustness of set #2**
- Without de-clustering, 2016–: n=266, 36/52/12.
- Without de-clustering, 2021–: n=149, 31/50/19.
- With "200-day rising" measured against 1 day ago instead of 20: 34/49/17.
- The deeper mode holds in every variant.

**Caveat the verdict understates: the holdout sets rest on very few episodes**
- Holdout set #3 has 12 signals but only about 5 episodes: 2020 (2 signals), Oct 2024 – Feb 2025 (6), May 2025 (1) and Jul–Aug 2026 (3).
- All 3 of its trend-break signals (2024-12-20 −21.6%, 2025-01-08 −23.7%, 2025-02-13 −36.9%) come from **one** episode, the Jan–Apr 2025 decline.
- Set #3a adds only 2016-01-06 (−25.3%).
- So "holdout widens both tails" rests on one or two episodes. The verdict's "effective n ≈ 6–10" is generous for these rows.

**Other items that reproduce**
- 200-day projections on flat paths:
  - Flat at 218: 204.24 (Oct 28) and 205.09 (Nov 4).
  - Flat at 200: 203.34 and 203.74.
- Volume at the last three lows: 1.01× (Mar 30), 0.96× (Jul 29), 1.05× (Sep 14) the prior 50-day average. Oct 14 was 1.01×.
- Post-print drift: 7 of 9 prints were lower five sessions later, using the CAT report dates.
- Window length: Oct 15 – Dec 4 is **36 sessions** (Thanksgiving closed). The verdict is right. Note that the semis audit addendum's "35 sessions, not 36" is itself wrong.
- No records between 2007 and 2016: confirmed. The first record after 2007 was on 2016-05-13.

---

## B. ERRORS

| # | Sev. | Claim (location) | Correct value | Evidence |
|---|---|---|---|---|
| 1 | **MED** | "Every independent lens puts the mode in the deeper bucket" (md §5). JSON `verdict_confidence` repeats it: "all independent lenses (episode conditionals, 36-session signal sets, …) put the mode in the deeper bucket". | **False.** 3 of the 15 rows in the verdict's own §5 table have a shallow mode: the 3-year record-episode set **45/36/18**, holdout **42/33/25** and holdout-from-1-year-high **47/29/24**. The deeper mode holds in the mean and median of the rows, not in every lens. | Verdict table; a3.py, a4.py, a8.py |
| 2 | **MED** | "A market trend break (S&P 500 below 7,314) implies QQQ at about 660 or lower, which maps to NVDA at about 192 or lower" (md §2; JSON `upper_layer_conditioning`) | At DB's QQQ/SPY betas (1.43 / 1.50 / 1.62), S&P 7,314 corresponds to QQQ **674 / 672 / 667**. That maps to NVDA about **198 / 197 / 195** at the 1.41 ratio, which is *inside NVDA's deeper bucket*. The "660" comes from MV's deeper-bucket prose (QQQ 660–685). The same verdict uses TV's mapping in §3 (7,505 ≈ 696–700, an implied beta of about 1.45), which gives about 672 at 7,314. The two mappings are internally inconsistent, and this one overstates how directly a market trend break forces an NVDA trend break. | a8.py; market_verdict.md l.186; tech_verdict.md l.73–75 |
| 3 | LOW-MED | "The base rates and mappings average about **35 / 46 / 19**" (md §5), which then feeds Final 33/47/20 | The **mean** of the 15 rows is **35.8 / 44.3 / 19.9**. The mean excluding the top-down rows is 36.0 / 43.3 / 20.5. The **median** is 36 / 46 / 20. The 46 for deeper matches the median, not the mean. Applying the stated −2 / +1 / +1 to the mean gives about **34 / 45 / 21**. | a8.py |
| 4 | LOW | "NVDA/SOXX … bottomed at **0.3185 on Jun 22, 2026**. The +33.7% 'holdout' rally since then" (md §2) | 0.3185 is the Jun 22 value, the day of the SOXX record. The 1-year low was **0.3123 on Jun 30** (0.3131 on Jun 25). The rally from the low is **+36.4%**. The +33.7% is DB's "since Jun 22" figure. | a2.py |
| 5 | LOW | "NVDA lagged the **first half** of 2026: YTD +18.7% vs SOXX +72.5%" (md §2; JSON `internals_summary`) | +18.7% / +72.5% is YTD **through Oct 14**. For the first half (to Jun 30) it is NVDA **+7.3%** vs SOXX **+112.8%**. The label was inherited from semis_leadership.md l.42. | a1.py |
| 6 | LOW | "Every base rate and the implied-volatility walk put **at least 55%** below 210" (md §6; JSON `strongest_bear_points`) | The holdout-from-1-year-high row has **53%** below 210 (47% shallow). The 3-year −7.5% set has 6/11 = 54.5%. | a8.py |
| 7 | LOW | "Shallow is 33% rather than the **25–30%** that the overnight-conditioned sets imply" (md §6) | The 3-year overnight-conditioned set is itself **33%** shallow (n=9; 33/44/22). The range is 25–33%. | a3.py |
| 8 | LOW | Key-level percentage rounding (md §8; JSON hinge `reasoning`) | 211.02: **−4.6%** from 221.30 (stated −4.7). 178.2: **−19.5 / −18.4** (stated −19.4 / −18.3; the JSON correctly says −19.5). 222.60 vs 218.35: **+1.9** (stated +2.0). 214.63: −3.0 / −1.7 (the row shows only −3.1 / −1.8). | a8.py |
| 9 | LOW | "Rising 200-day: about 203.3–204.2 by Oct 28, about **204.4–205.6** by Nov 18" (md §7) | The ranges use different paths. The Oct 28 range is flat-200 to flat-218. The Nov 18 range is flat-200 (204.38) to flat-**210** (205.63). On the flat-218 path, Nov 18 is **206.63**. | a6.py |
| 10 | LOW | "'Overnight' means the 218.35 midpoint of the 218.2–218.5 band" (md header). §5 simulation row: "from 218.25". | No 218.2–218.5 band appears among the stated prints (218.96 at 04:24; earlier 217.94–218.50). Two different overnight anchors are used: 218.35 and 218.25. Results are not materially affected (218.35 gives 30/43/26). | a5.py |
| 11 | LOW | "The 52-week low is 164.08" (md §7) | That is IBKR's field (live_snapshots). DB's Yahoo series, the stated source of truth, has a **164.27** intraday low and a 165.17 closing low on Mar 30, 2026. | a1.py |
| 12 | LOW | "**At the 1-year beta**, SOXX must break 465 before NVDA reaches 208"; "semis deeper core (474–492) maps to about **209–214**" (md §6) | The 208.1 uses the 0.57 down-day *ratio*. The 1-year beta (0.48) gives **210.2**. At 0.57 the deeper core maps to **210.3–214.6**; 209.1–213.9 is the figure at 0.63. | a8.py |
| 13 | LOW | Semis-only mapping "**42 / 46 / 12**" kept after [SV] was switched to the audited 26/37/37 (md header and §2 updated, mapping not) | It cannot be recomputed because the conditional table is judgment. With SV trend break up 2 points and deeper down 2, the semis-only mapping should move slightly toward trend break. It is stale. | semis_verdict.md addendum |
| 14 | LOW | JSON vs md consistency | The JSON gives "Jul-low AVWAP / 220 pin" as `support`; the md calls it a "Pivot". The JSON trend-line `level_low` is 189.66; the md uses 190.01. The md "UNVERIFIED" list calls the hike odds "single-source", but facts.md compiles 4 venues: Polymarket, Kalshi, Investing.com and Reuters/LSEG. All cosmetic. | file comparison |

---

## C. Claims verified OK (≈250 distinct numbers, dates and statistics; md and JSON duplicates counted once)

**Bottom-line table**
- Boundaries 210.00 / 190.01.
- Probabilities 33 + 47 + 20 = 100.
- Each zone (211–218.9, 198–209, 175–189) and core lies inside its own boundary.
- All 12 drawdown figures from 239.24 and 243.37.
- All six "171 is x% below" figures.
- The most-likely zone at −5.6% to −9.2% / −4.3% to −7.9%.
- 67% below 210.
- The JSON core, tail and from-221.30 strings.

**Levels [DB]**
- 221.30: −7.50% / −9.07%.
- 50-day 223.21 (20-day slope +4.51%). First close below it since Sep 15: correct, since the prior closes below the 50-day were Sep 14–15.
- 100-day 214.45 (+3.19%, rising +1.35% per 20 sessions); 200-day 202.69 (+9.18%).
- RSI 43.9; ATR 5.83 (2.63%).
- 235.74 failed breakout (Oct 5–7, then Oct 8 at 230.48); 36.4% retracement; SOXX 56.3%.
- POC 218.85; 6-month POC 211.02.
- Gaps: 216.76–217.15, 228.86–229.11, 189.66–190.77, 184.08–184.30, 178.23–180.30.
- AVWAPs: 221.01, 210.21, 200.85, 230.98, 178.37.
- Fibonacci levels: 222.99, 216.69, 210.39, 201.43; on closes 214.63 and 200.55.
- Sep 14 low 208.93 / close 210.96; Aug 24 low 207.25; Aug–Sep closing low 206.64 (Aug 3).
- Jul 29 close = low = 190.01; Jul 30 close 195.04; Jun 29 low 189.80.
- −25% at 179.4; 2024 analog −27.05% at 174.6.
- Analog MAE 203.4 / 199.6.

**Upper-layer mappings**
- All 16 numbers in the §2 table reproduce (216.0 / 211.9 / 208.1 / 198.1 / 200.8–205.7 / 185–194 / 208.9–215.7 / 207.6 / 203.3 / 196.9–205.5 / 192.5 / 183.3 / 174.7–189.7).
- Current-leg ratios 0.63 and 1.86.
- MV 46/34/20, TV 37/38/25 and SV 26/37/37 match the audit addenda; 63% = 38 + 25.
- May 14 → Jul 29: NVDA −19.40% while the S&P 500's worst close was −4.50% (Jun 10).
- Jun 22 → Jul 29: NVDA −8.9% vs SOXX −29.0%.
- NVDA/SOXX 0.4261: +5.0% since Oct 6, +2.6% vs its 50-day, −5.5% vs its 200-day; 1-year high 0.6738 on Nov 20, 2025.
- NVDA/QQQ −3.6% since Oct 6 and below its 50-day.

**Advocate checks (§3)**
- All the statuses reproduce, including the bear's 0.63 (n=40) against my 0.60 (n=34).
- The Oct 23 straddle (5.925 + 4.20) gives 211.2–231.4.
- The bull's "[MV] 7,480 → QQQ 660–685 → NVDA 192–203" is correctly called overstated.

**Research attributions**, each matching its source with tags preserved:
- [SP]: 220 strike OI 99.2k / 64.6k; Nov max pain about 210 (partial chain); 200-strike puts 53.2k / 64.5k; event ±5.8–5.9%; straddle ±9.8% (199.7–242.9); risk-neutral 35/23/15%; IV 15th percentile; HF net 2nd percentile (SINGLE-SOURCE); crowded trade (CONFIRMED); buyback blackout (UNVERIFIED).
- [FX] and [CAT]: $105bn / $108.5bn, about 4.25 GW, 2028, OpenAI reimburses; $279bn / $366bn; "roughly a quarter"; 55% hyperscaler share; Q3 $108bn ±2%; 71–72%; +70%; Q4 guide about $120bn.
- [FX]: 24–32% hike odds; CoreWeave below 78c; SoftBank −9.4%; $50bn vs $68–70bn not settled.
- [SL]: $235bn / $150bn on Sep 28; median semi −30.8%; 76% of 29 in a bear market; 14% breadth.
- [MR]: real yield 2.95% is the highest since Nov 2008; CCC at a 3-year high.
- [O8]: no downgrades or insider sales.
- Calendar items: 15x FY28 (MS; single-source per completeness.md); OpenAI round about $1.4T.

**Calendar**
- Every weekday is correct: Wed Oct 14, Oct 21 and Oct 28; Thu Oct 29; Tue Nov 3; Fri Nov 6; Tue Nov 10; Fri Nov 20 (third Friday); Fri Dec 4; Wed Dec 9.
- Oct 16 is the third Friday. Oct 21 is the VIX expiry (30 days before Nov 20). Sep PPI is Oct 15. Nov 27 is a half day. The 2018 low was Dec 24.

**Rates, vol and credit**
- HY OAS 3.16% (versus 3.46%); VIX/VIX3M 0.898; 10-year 5.19–5.21%, 1-year high 5.31%; QQQ 683.7 = −10%.

**JSON**
- All 15 `distance_pct_from_oct14_close` values equal the midpoint distance to the cent.

---

## D. Could not be verified

- **Overnight IBKR prints** (NVDA 218.96 at 04:24, 217.94–218.50; SOXX 512.27; QQQ 722.57) are point-in-time snapshots. They agree with live_snapshots (218.50 at about 02:30 UTC) and facts.md (217.94 at 03:55 UTC), but cannot be re-pulled for those times.
- **Judgment items:** the conditional mapping tables (31/50/20, 42/46/12, 32/48/20), the regime net (−2 / +1 / +1), and the "about 33% in the 198–209 zone" confidence figure.
- **External facts:** the 8-K amounts, hike odds, CoreWeave bond price, OpenAI figures, MS "15x FY28" and the earnings-calendar entries. I checked these only for agreement with the research and facts files, not against fresh sources.
- **The 2026 report dates** used in the 7-of-9 statistic (Feb 25, May 20, Aug 26) are taken from CAT. The reaction math reproduces given those dates.
- **The bull's holdout (n=15) and swing-leg (n=21) sets.** The verdict correctly says these were not re-run, and I did not re-run them either.

---

## Does any error change the verdict's scenario probabilities, zones or key level? **No.**

**Why not**
- Every load-bearing statistic reproduces exactly with independent code: the record-episode conditionals, all three 36-session signal sets, all three holdout/SOXX-conditioned sets, the Monte Carlo, the betas and down-day ratios, the 200-day paths, and every level, gap, AVWAP and Fibonacci value that defines the zones.
- The 210.00 / 190.01 boundaries, the zones, and the 210 key level (the 210.21–211.02 cluster) are unaffected.

**What does change**
- The errors are framing, labelling and rounding.
- The two medium items (#1 the "every lens" unanimity, #2 the 7,314 → QQQ 660 → NVDA 192 mapping) and the averaging slip (#3) all lean slightly bearish.
- Corrected, they argue for roughly **34 / 45 / 21** rather than 33 / 47 / 20, a 1–2 point shift that is well inside the verdict's stated uncertainty. Deeper stays modal on both the mean (44) and the median (46) of the reference rows.

**What should be fixed in the text**
- Withdraw "every independent lens" and "at least 55%".
- Correct the NVDA/SOXX bottom (0.3123 on Jun 30) and the "first half" label.
- Recompute the market-to-NVDA mapping at the 7,314 boundary (about NVDA 195–198, not 192).
- Note that the holdout trend-break share comes from a single episode (Jan–Apr 2025).
