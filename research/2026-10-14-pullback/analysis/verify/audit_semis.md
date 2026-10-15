# Numbers audit: semis_verdict.md and semis_verdict.json

*Auditor: audit_semis. Run about 04:15–04:35 UTC Oct 15. Data runs through the Oct 14 close.*

**What was audited**
- `analysis/semis_verdict.md`. It was re-saved at 04:16:33 UTC while this audit ran. The only change was the TSMC "checked again at about 04:17 UTC" wording, which adds 45 bytes; everything below refers to that saved version.
- `analysis/semis_verdict.json`. It did not exist when the audit started and appeared at 04:16:33 UTC. It is audited in full.

**Method**
- Every number was checked against DATA_BRIEF and the raw CSVs, recomputed with my own code in `scratchpad/audit_semis_code/`:
  - `a1_levels.py`: ranges, breakout dates, AVWAPs, Fibonacci levels, 200-day paths, RSI, volume ratios, SMH/SOX ratios.
  - `a2_vp_misc.py`: volume profile, ratios, S&P drawdowns, ARM, NVDA, ^TNX.
  - `a3_baserates.py`, `a4_bins.py`, `a6_robust.py`: an independent re-implementation of the ^SOX base rates, the incremental slope and the NDX-conditional bins, plus sensitivity tests.
  - `a5_betas.py`: betas, down-day beta, residual vol.
- Research attributions were checked against the cited files.
- One read-only IBKR snapshot was taken (SOXX at 04:24 UTC).

---

## A. Re-run of the load-bearing computations (independent code)

| # | Computation | Verdict's figure | My re-run | Reproduces? |
|---|---|---|---|---|
| 1 | §6 ^SOX base rates: first close ≤ −11.6% vs the 60-day closing high, re-armed on a new 60-day high, above a rising 200-day, lowest close within 36 sessions, S ≥ −15.6% / D ≥ −21.1% | n=31 42/29/29, med −16.6%; 2003– n=21 43/33/24; 2009– n=20 45/30/25; +NDX within 6%: n=10 30/50/20, med −17.1%; overnight state ≤ −13.5%: n=20 20/40/40, med −18.0%; overnight 2003– n=13 23/46/31, med −17.5% | Identical on every row (n, S/D/T and median). Median days to low 6–11; low on the signal day 20–31% | **YES**, exactly |
| 2 | §4 incremental SOX-vs-NDX slope and NDX-conditional bins | slope 1.1–1.2×, corr 0.84–0.91, n=54; ≤4.5 pp bin: 68–81% shallow; 4.5–9 pp bin: 0–8 / 54–56 / 38–44 (n=9–13) | Slope 1.17 (all, n=54) / 1.08 (above 200d) / 1.24 (2003+); intercepts −1.36 / −1.92 / −0.70; corr 0.84 / 0.85 / 0.91. Bins: ≤4.5 pp gives 73 / 68 / 81% shallow; 4.5–9 pp gives **all n=18: 17/39/44**; above 200d n=9: 0/56/44; 2003+ n=13: 8/54/38 | Numbers **YES**. Reporting is **selective** (see E1) |
| 3 | Levels: range, breakout, AVWAPs, Fibonacci levels, 200-day path | 497.40 / 559.12 / 485.71 / 566.02 / 528.26; Sep 21 559.34; 15 closes above; AVWAPs 555.84 / 548.99 / 544.50 / 530.19 / 525.39 / 476.52 / 539.98 / 559.71; Fib 541.95 / 527.26 / 512.56 / 491.65; 482.40 / 441.66; 200-day (flat 495) 470.3 / 474.5 / 478.5 / 485.7 / 493.7 | Identical to the cent | **YES** |
| 4 | Betas (1y / 6m / 3m) | SOXX/QQQ 2.04 / 2.26 / 2.04; down-day 2.25 / 2.46; resid vol 22–24%; NVDA/SOXX 0.48 / 0.39 / 0.52; NVDA/QQQ 1.30 / 1.16 / 1.28 | Identical. Resid vol 22.2 / 24.2 / 23.0% (6.3–6.8% over 20 days) | **YES** |
| 5 | §4 top-down arithmetic | 24/34/42 (TV 35/40/25); 26/34/41 (38/37/25) | 24.1 / 34.1 / 41.9 and 25.6 / 33.7 / 40.7. Matrix rows sum to 1.00 | **YES** |
| 6 | 3-month volume profile | 7.7% at 465–495, 12.4% at 495–505, 19.3% at 505–520 | Fine-grained, range-distributed, 63–65 sessions: **8.1–8.4% / 12.3–12.8% / 16.9–17.6%**. The verdict's figures come from 40-bin midpoint assignment. Typical-price assignment gives the bear's 14.6% for 496–504 exactly | Approximately. The air-pocket conclusion holds |

---

## B. ERRORS

| # | Sev. | Claim (location) | Correct value | Evidence |
|---|---|---|---|---|
| E1 | **MED** | §4: "The analog bins agree" with the judgment matrix (tech-shallow row S .60 / D .36 / T .04; tech-deeper row .07 / .50 / .43). Quoted bins: "0–8% shallow, 54–56% deeper, 38–44% trend break (n=9–13)" | (a) The largest 4.5–9 pp bin is omitted: all signals, n=18, give **17 / 39 / 44**. (b) The tech-shallow row's D=0.36 lies outside every ≤4.5 pp bin (**D 14–21%**, S 68–81%, T 5–11%). (c) From the **overnight state** (THR 13.5%), the state the verdict weights 60%, the bins are far more bearish: ≤4.5 pp gives 31–40 / 43–54 / 7–22, and **4.5–9 pp gives 0–10 / 20–25 / 70–80** (n=5–10). (d) Applied mechanically to TV's 35/40/25, the bins give a top-down of **24–32 / 22–30 / 42–46** (close state) or **11–16 / 23–29 / 57–62** (overnight state). Trend break beats deeper in every variant; the matrix gives 24 / 34 / 42 | a4_bins.py |
| E2 | LOW-MED | §6 base rates use H=36 sessions for the "Oct 15 – Fri Dec 4" window | That window has **35** sessions (Thanksgiving Nov 26 is closed). 3 of the 31 signals bottom exactly on day 36 (1995-10-03, 2022-01-20, 2026-06-05). With H=35 the close-state trend-break rates fall: 29→**26**, 24→**19**, 25→**20**, and 20→**10** for the NDX subset. Overnight-state rows are unchanged. So the close-state trend-break bias runs opposite to E1 | a3_baserates.py |
| E3 | LOW | §6 net adjustment: blend "about 28 / 36 / 36", then "three points from shallow to deeper, one point from trend break to deeper. **Final: 26 / 39 / 35**" | The stated arithmetic gives **25 / 40 / 35**. Separately, the "semis-only ... about 31 / 38 / 31" blend method is not specified. My closest reconstruction, which averages the close-state rows excluding the NDX subset and weights them 40/60 against the overnight rows, gives 30 / 38 / 32 | Arithmetic |
| E4 | LOW | §3 leadership table: "AI compute, **excluding the mega-caps** −14.5%" | SL's −14.5% is the median of all **7** AI-compute names, including NVDA (−7.5), AVGO (−7.9) and AMD (−12.1). Excluding NVDA and AVGO the median is **−18.8%**; excluding all three it is about **−20.1%** | semis_leadership.md lines 225–231, 270 |
| E5 | LOW | §4 / JSON: "SOXX −29% while the S&P 500's worst close was only −4.5%" | The −4.5% S&P close was **Jun 10** (the Jun 2→Jun 10 episode), before SOXX's Jun 22→Jul 29 leg. During that leg the S&P's worst close was **−3.9%** vs its Jun 2 peak (7316.15 on Jul 29), or −2.1% vs Jun 22. The point is stronger, not weaker | a2 output; DB line 266; MV line 98 |
| E6 | LOW | "My median lowest close is about **480–485**" | The verdict's own 26/39/35 split implies a median of about **477–480**: 477.5 if the deeper mass is uniform over 465–497.4, about 479 if it is weighted to the 474–492 core. A median of 485 needs about 62% of the deeper mass inside 485–497.4, which contradicts the stated 474–492 core | Arithmetic |
| E7 | LOW | §1: "Intraday lows since July are rising: 464.08 → 485.71 → 489.21 → 495.15" | It omits the **Aug 24 swing low 498.93** [DB], which the Sep 3 low (489.21) undercut. The swing-low sequence 464.08 → 498.93 → 489.21 → 495.15 is not monotonic. The closing-basis higher low (465.00 → 497.40) is correct | DB SOXX swing lows |
| E8 | LOW | §3: "volume 1.52× its 50-day average (2.88× on Jun 5; 1.79× on Jul 29)"; also "Oct 8 1.40×" | The conventions are mixed. 1.40× and 1.52× divide by a 50-day average that includes the day; 2.88× and 1.79× use the prior 50 days. On one basis (including the day): Jun 5 **2.77×**, Jul 29 **1.76×**, Oct 8 1.40×, Oct 14 1.52×. The conclusion is unchanged | a1 output |
| E9 | LOW | Bottom-line SMH/SOX equivalents: trend break "SMH 452–499; SOX 9,500–10,340"; shallow "SOX 11,130–11,500" | At SOXX 420: SMH **≈455–457**, SOX **≈9,435–9,450** (Jul 29 or Oct 14 ratio). At SOXX 515: SOX **≈11,525–11,585**. All other equivalents check out (541.5 / 561 / 504.22 / 515–535; 10,447 / 11,131; 10,640–11,120) | a1 ratios |
| E10 | LOW | §7 / §8 / JSON: NVDA results "Nov 18–25 (unconfirmed)" | CAT, MV and TV all say **"Nov 17 or 18"** (WSH lists Nov 17 as "confirmed"; the Wednesday pattern points to Nov 18). Nov 19–25 has no source, and Nov 17 is dropped | catalysts.md lines 44–47, 121; MV line 263; TV line 370 |
| E11 | LOW | Bottom line: "None of the semis capitulation markers are present ... **there are no sell-side downgrades**" | The verdict's own sources record downgrades: Citi downgraded **NXPI and Nova** (Oct 8), and Barclays downgraded **Dell, HPE and NetApp** (Oct 14; the rationale cites normalising memory prices). There may be no *sector-level* or leader downgrade, but the claim as worded is contradicted | semis_leadership.md lines 156, 160; oct8_narrative.md line 227 |
| E12 | LOW | Caveats: "Analogs are weighted toward the 1990s" (md); "analogs weighted to 1995–2002" (JSON) | In the main n=31 set, 10 signals are pre-2003, 1 is from 2003–08 and **20 are from 2009 on**. The overnight set has 7 of 20 pre-2003. The pre-2003 signals do carry the trend-break outcomes (40% trend break pre-2003 vs 24% for 2003+), so the caveat should say that instead | a6 output |
| E13 | LOW | §3: "real yield about 2.9% (the highest since 2008)" | The current 10-year TIPS yield is **2.88%**. The "highest since Nov 2008" reading was the **2.95% peak on Oct 5** [MR] | macro_rates.md lines 30, 123, 140 |
| E14 | LOW | Live checks: "SOXX implied vol 35.6%, at the 26th percentile of its 52-week range" | IBKR's field is an "IV high percentile" (52w 0.263), with an undocumented methodology. SP carries that caveat; the verdict drops it and calls it a range percentile. The value itself is confirmed by my 04:24 UTC snapshot | sentiment_positioning.md lines 172–177; IBKR |
| E15 | LOW | md vs JSON inconsistencies | (a) The late-Sep shelf is "551.95–579.98" in the md but "572.78–579.98" in the JSON. (b) The most-likely-zone "core" is 474–492 in the md (deeper core) but "480–492" in the JSON. (c) The "572.78 shelf was lost on Oct 8" only holds *after* the Oct 2 gap: SOXX had already closed below 572.78 on 5 of 7 sessions from Sep 23 to Oct 1 (565.72, 566.07, 560.79, 567.44, 568.64) | a1 daily table |
| E16 | LOW | §4 mapping: tech trend break (QQQ < 661.73) → "SOXX ≤ about 440" at beta 1.5–2.0 | The boundary maps to **447.6** at β 1.5 and 423.6 at β 2.0, so "≤ about 448" at the low-beta end | Arithmetic |
| E17 | LOW | Header and TSMC line: "written about 04:15–04:45 UTC"; TSMC "checked again at about 04:17 UTC" | The file carrying this sentence was saved at **04:16:33 UTC** (filesystem mtime), so the 04:17 check post-dates the save. This is cosmetic, but the timestamp claims are not self-consistent | `ls --full-time` |

**Robustness note (not an error, but material to how thin the edge is).** Using SOX's own hinge equivalents (11,131 and 10,447 are −15.79% and −20.96% from the SOX swing high 13,217.82) instead of the SOXX-mapped −15.6% / −21.1%:
- the close-state set becomes **45 / 26 / 29**;
- the overnight set becomes **25 / 35 / 40**.

Definitional choices (thresholds, H=35 vs 36, which subset) move the deeper and trend-break rates by ±3–10 points.

---

## C. Claims that could not be verified (or were verified only against a secondary file)

**IBKR quotes at 04:10 UTC**
- The 04:10 prints (SOXX 509.46, QQQ 720.92, NVDA 218.25) cannot be reproduced after the fact.
- My 04:24 UTC snapshot shows SOXX **512.27 (−1.38%)**, so "−13.6% / 2.4% above the hinge" is already stale: it is now −13.1% and +3.0%.
- IV 35.6% and the 52-week percentile 0.263 do match.

**Matched to facts.md / zz_corrections only (not independently re-sourced)**
- Asia moves: KOSPI −7.7% (Reuters says −7.2%; the md does not mention it), SK Hynix −11.4%, Samsung −9.5%, Kioxia −11.2%, TEL −7.3%, Taiex −3%.
- CoreWeave 2032s below 78c.
- Oct 28 hike odds of 24–32%.
- The ASML ADR −3.9% (this one is confirmed in the local ASML.csv: −3.94%).

**Sourced from research files, tags preserved**
- BofA FMS: "most crowded" is CONFIRMED; the 45% figure is SINGLE-SOURCE.
- SOXL +$711.9M: one vendor.
- SOXX option P/C 2.59 vs 1.87: a single overnight IBKR read.
- The 2018 analog (−13.3% → −26.0%, giving −14.6% further, about 443): derived correctly from SP.

**Pending or estimated**
- TSMC Q3 status and timing: 2:00 am ET is 06:00 UTC, consistent with [CAT].
- Unannounced or estimated dates: AMZN, CoreWeave, Samsung, SK Hynix.

**Other**
- Advocate statistics the verdict says it did not re-run: the bull's 16 fast legs, the bear's n=14 lower-high subset and its 57-signal table. I did not re-run them either.
- The §6 "semis-only ≈ 31/38/31" blend: the method is unspecified, and I can only approximately reproduce it (30/38/32).
- "TV re-weighted for MV's audit ≈ 38/37/25" is a judgment input, not a computation.
- The rising-lows trend line is subjective; the arithmetic checks out (519.7 at the Oct 14 close, 520.7 for Oct 15).

---

## D. Claims verified OK

About **235 distinct numeric claims** were checked OK across the md and JSON, counting each number once. They include:

**Bottom line and scenarios**
- Boundaries, probabilities and sum (26+39+35 = 100).
- All three zones, cores and the tail lie inside their own boundaries.
- All 22 drawdown figures vs 589.51 and 655.01, plus the JSON core and tail drawdowns.
- 21 of 24 SMH/SOX equivalents.
- Most-likely-zone distances (−4.3/−8.7, −15.7/−19.6, −24.1/−27.6).
- Overnight distances (−13.6%, +2.4%, −1.92 / −1.10 / −1.38%).

**§1 structure**
- Range, dates and weekdays (Sep 14 Mon, Aug 17 Mon, Sep 21 Mon, Oct 2 Fri, Oct 5 Mon, Oct 8 Thu, Oct 12 Mon).
- 15 consecutive closes above the range top; Oct 2 open 590.91; 596.44; 655.01; Jul 1 599.70; weekly 588.9 vs 639.5.
- DB's 573 window note; the Oct 8 and Oct 12 losses; all 5 AVWAPs; volumes 6.88M / 10.36M / 10.67M.
- 7 straight down closes; 56% retrace; the Sep 17 gap; 61.8% at 512.56; higher high and higher low on closes.
- +11.5% vs the 200-day, rising 5.9%; SOXX/SPY +5.8% vs its 200-day with no relative lower low (0.6749 vs 0.6537 on Sep 14).
- POC 500.28; SMH 541.50; SOX 11,131.28; measured move 435.7.
- −29.0% over 26 sessions from Jun 22 to Jul 29.

**§2 key levels**
- All 12 rows: levels and % distances.
- The 200-day path; 482.40; 441.66; the Apr 17 gap.
- All 12 JSON distance_pct values (computed from range midpoints).

**§3 internals**
- Breadth 14 / 93 / 17 / 0 / 76 / −30.8 / 66.
- All per-name and group moves except the E4 label.
- NVDA/SOXX +5.0%; RSI 37.3 / 33.1; VIX 16.87; VIX/VIX3M 0.898.
- SOXX/SPY −10.0% in 5 sessions; SMH/QQQ below its 50-day.
- HY 3.16% at the 91st percentile; CCC at a 3-year high.
- 10-year 5.19–5.21; −12 bp from the Oct 5 peak while SOXX fell −11.9%.

**§4 conditioning**
- MV 46/34/20 and 7,505; TV 35/40/25, 697–700, 661.73, 683.7, 731.
- All betas, correlations and residual vol; the 2.9× overshoot.
- The mapping table (5 of 6 ranges).
- Top-down arithmetic.
- NVDA −8.9% vs SOXX −29.0%.
- ~1.5× in price terms, which holds once the regression intercept is included: QQQ 680–690 maps to 467–476, QQQ 700 to about 485–488.

**§5 advocate checks**
- All recomputable items, including the DB conditionals n=1 at −41.7% and 5y n=4 at −29.15% (≈464).
- Bull 470.5 / 475; bear 474 / 478 / 483–486; the bear's 468–478 at β 2.0–2.5.

**§6 calibration**
- Every row of the table; DB SOXX episodes (median −13.4%, 16 days); the 2018 analog arithmetic.
- The 28/36/36 average.

**§7–§9 scenarios, catalysts and signals**
- NVDA 208.8 (the 61.8% Fibonacci level); "7 of last 9"; LRCX $8.10bn; ARM −45.8%; LRCX −4.71%; SOXX +8.50% on Jul 30.
- TSMC rule inputs (65% gross margin, $60–64bn capex, 512.6).
- All catalyst dates and weekdays except E10:
  - Oct 15 Thu (PPI); Oct 16 Fri (3rd-Friday opex); Oct 21 Wed (VIX expiration, 30 days before Nov 20).
  - Oct 22 WDC; Oct 27 NXPI and STX; Oct 28 Wed (FOMC, MSFT, GOOGL, KLAC).
  - Oct 29 INTC, PCE and AMZN (estimated); Nov 3 Tue (AMD, Election Day); Nov 4 ARM.
  - About Nov 10: CPI, CoreWeave and TSMC October sales; Fri Dec 4.

**JSON-only figures**
- SMH −10.9 / −15.6; SOX −11.6 / −20.2; +18.5% from Sep 14 to Oct 5.
- 39% vs 33% uniform; 65% that 465 holds.
- TSMC NT$1,494.2bn +50.9%; MU FQ1 guide $61.5bn; MU −16.7%.
- The overnight "20–25" range, which is the 2009+ overnight row (25/42/33) not shown in the md table.

---

## Does any error change the verdict's scenario probabilities, zones or key level?

**Zones and key level: no. Probabilities: yes, but only at the margin, and only through E1.**

**Zones and key level**
- Every level, AVWAP, Fibonacci level, 200-day path, boundary and drawdown that defines the zones reproduces to the cent.
- The 497.40 / 465.00 hinges are correct.
- The equivalent-price slips (E9) and the md/JSON inconsistencies (E15) are cosmetic.

**The pure arithmetic and labelling errors (E3–E17)**
- Each one moves the numbers by at most about 1 point, for example 26/39/35 becomes 25/40/35 under E3, or does not move them at all.

**E1, the analog bins**
- E1 matters because the verdict's thin deeper-over-trend-break edge (39 vs 35) rests on a judgment matrix it says "the analog bins agree" with.
- They agree only for two of the three close-state 4.5–9 pp bins.
- Against the bins:
  - the tech-shallow row over-assigns deeper (0.36 vs 0.14–0.21);
  - the omitted all-signals bin and the overnight-state bins put trend break well above deeper;
  - feeding the bins in mechanically makes the top-down trend break 42–62% and deeper 22–30%.
- Substituting the close-state bin top-down for the judgment top-down, and keeping the verdict's semis-only blend and regime adjustments, gives about **27 / 36 / 37**. That makes deeper and trend break co-modal, with trend break marginally ahead.
- Correcting E2 (H=35) pushes partly back toward deeper, to about 26 / 38 / 36.

**Net**
- The ordering "deeper ≥ trend break ≫ shallow" is not robust. Deeper and trend break are statistically indistinguishable (each about 35–39%).
- The sentence "the analog bins agree" should be withdrawn or qualified.
- Shallow at about 25–27% is robust.
