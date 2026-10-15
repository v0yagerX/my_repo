# Cross-layer coherence and bias critique (market → tech → semis → NVDA)

*Written about 04:40–05:10 UTC Oct 15. Data runs through the Oct 14 close. TSMC Q3 was not out (it is due about 05:30–06:00 UTC).*

**What I read**
- All four verdicts: `market_verdict.md`/`.json`, `tech_verdict.md`/`.json`, `semis_verdict.md`/`.json`, `nvda_verdict.md`/`.json`. The NVDA JSON appeared at 04:32 UTC.
- All eight bull and bear briefs.
- `verify/audit_market.md`, `verify/audit_tech.md`, `verify/audit_semis.md`, `research/zz_verification_corrections.md`.
- `DATA_BRIEF.md`, `betas_ratios.txt`, `analog_forward_returns.txt`, `live_snapshots.md`.

**Which probabilities I test.** Each layer's latest *audited* figures:

| Layer | Shallow / Deeper / Trend break |
|---|---|
| Market | 46 / 34 / 20 |
| Tech | 37 / 38 / 25 |
| Semis | 26 / 37 / 37 |
| NVDA | 33 / 47 / 20 |

**Method.** My own scripts are in `scratchpad/coh_scripts/c1–c6.py` and use none of the team's code.
- **Benchmark:** a driftless joint bootstrap (5-day blocks, 40–60k paths, **36 sessions**) of SPX, QQQ, SOXX, NVDA, RSP and XLK daily returns. It uses three windows (1y, 6m, 2y), plus a variant scaled to implied vol (IV).
- **Historical check:** overlapping 36-session forward-minimum windows since Oct 2021, both raw and vol-normalised.
- **Joint tables:** iterative proportional fitting (IPF), seeded with the empirical joint distribution.
- **Translations:** level translations use the betas in `betas_ratios.txt`.
- **What the benchmark is:** a *no-information* reference for how the four instruments move together. It is not a forecast.

## Bottom line

1. **Market and NVDA agree with each other. Tech is the outlier.**
   - Tech's 25% trend break is more than the market's 20%, yet QQQ's trend line is the farthest away of all four layers in volatility terms (1.31σ).
   - Given the market's 46/34/20, every empirical estimate of SPX–QQQ dependence implies QQQ at about **50 / 35 / 15**.
   - Tech's numbers come entirely from a hand-made conditional table that is 10–20 points more bearish than every empirical estimate, in every row.
2. **With tech fixed, every layer sits within about ±5 points of a driftless random walk at current volatility.**
   - The "modal" calls are statistical noise: deeper vs shallow in tech, and deeper vs trend break in semis.
   - One-point precision is not justified when the effective samples are n ≈ 6–35.
3. **"Trend break" does not mean the same event in each layer.**
   - Mapped to the S&P 500, the trend lines sit at about 7,400 for SOXX, 7,314 for the S&P itself, about 7,250 for QQQ and about 7,155 for NVDA.
   - In volatility terms they run from 0.64σ (SOXX) to 1.31σ (QQQ).
   - The NVDA verdict mis-translates the market trend line: S&P 7,314 maps to NVDA about **195–199**, not "≤192".
4. **The machine-readable outputs are stale or internally broken.**
   - The market, tech and semis JSONs still carry pre-audit probabilities.
   - The market JSON's shallow definition adds an RSP condition. That leaves about **13–14%** of outcomes in no bucket.
   - The semis audit's "35-session" correction is wrong (the window has 36 sessions), and it was written into the semis verdict.
5. **Invalidation rules mix definitional lines with signals, and several contradict the Dec 4 window or the layer's own zones.**
   - Two of them would misfire about 28% and 39% of the time in scenarios they claim to rule out.

---

## Findings, ranked by importance

### 1. HIGH: the tech layer is incoherent with the market layer

**(i) The trend-break ordering is inverted**

| | S&P 500 | QQQ | NVDA |
|---|---|---|---|
| Distance to trend line | −5.39% | −9.67% | −15.24% |
| In σ (realized vol) | 1.12σ | **1.31σ** | 1.08σ |

- In beta terms, QQQ 661.73 maps to **S&P 500 about 7,221–7,280**, which is *below* the market's own 7,314 trend line.
- So P(QQQ trend break) should be ≤ P(S&P trend break) unless tech falls while equal weight rallies *in a tail*.
- Tech gives 25% against the market's 20%.
- The no-information bootstrap gives QQQ trend break 12–17% against S&P 16–27%.

**(ii) The conditional table is outside the empirical envelope.** P(QQQ bucket | S&P bucket), with each row in the order shallow / deeper / trend break:

| Given market | Tech's judgment | Bootstrap 1y | Bootstrap 6m | Bootstrap 2y | History 2021– (raw) | History (vol-normalised) |
|---|---|---|---|---|---|---|
| Shallow | **72 / 25 / 3** | 88 / 12 / 0 | 84 / 16 / 1 | 91 / 9 / 0 | 93 / 6 / 1 | 90 / 10 / 0 |
| Deeper | **13 / 64 / 23** | 28 / 65 / 7 | 20 / 67 / 14 | 32 / 64 / 4 | 33 / 62 / 5 | 19 / 78 / 3 |
| Trend break | **3 / 17 / 80** | 1 / 39 / 60 | 1 / 27 / 73 | 1 / 39 / 60 | 3 / 31 / 67 | 1 / 31 / 69 |

- Fitting the two published marginals together by IPF reproduces tech's table almost exactly (72/26/1, 11/66/23, 0/17/83). **The whole gap between the layers is the judgment table.**
- Run in reverse, tech's 37/38/25 implies **S&P 38 / 31 / 31**, against the market's 46/34/20.

**(iii) The precedent cited for decoupling does not support the market-shallow row.**
- In Jun–Jul 2026 the S&P's worst close was −4.5% from its record. That lies *past* today's 7,505 hinge (−4.0%).
- So that episode was market-deeper with tech-deeper, not market-shallow with tech-deeper.
- The tech verdict's own Oct 2025 – Mar 2026 example (S&P −9.1%, QQQ −12.2% from the record) is market trend break with tech *deeper*. That argues for a *lower* tech trend-break row, not 0.80.

**(iv) Tech also adds bear weight on top of its own state-conditioned base rate.**
- That base rate (42/39/19) already conditions on broken semis, the −5% overnight print and the rate shock.
- **Fix:** see the recommended table (about 43 / 38 / 19).

### 2. HIGH: the probabilities carry almost no information beyond a random walk, but are quoted to one point

**No-information benchmark** (driftless bootstrap, 36 sessions; shallow / deeper / trend break)

| Layer | Latest verdict | 1y realized | 6m | 2y | IV-scaled\* | History 2021– (vol-normalised) |
|---|---|---|---|---|---|---|
| S&P 500 | 46 / 34 / 20 | 50 / 29 / 21 | 56 / 28 / 16 | 47 / 26 / 27 | 47 / 29 / 24 | 63 / 20 / 17 |
| QQQ | 37 / 38 / 25 | 52 / 33 / 14 | 52 / 32 / 16 | 52 / 31 / 17 | 50 / 33 / 17 | 61 / 27 / 12 |
| SOXX | 26 / 37 / 37 | 30 / 28 / 43 | 28 / 25 / 47 | 32 / 30 / 38 | 35 / 33 / 32 | 35 / 28 / 37 |
| NVDA | 33 / 47 / 20 | 38 / 42 / 20 | 39 / 40 / 21 | 35 / 37 / 28 | 41 / 44 / 15 | 45 / 44 / 11 |

\*IV-scaled: S&P 13.5%, QQQ 21%, SOXX 35.6%, NVDA 33.2%.

**No-information median lows** (1y bootstrap, SOXX and NVDA scaled to IV)

| | No-information | Verdict |
|---|---|---|
| S&P 500 | **7,504** | audited "about 7,505" |
| QQQ | 698.8 | 688–690 |
| SOXX | 483.7 | 477–480 |
| NVDA | 206.6 | 205–207 |

- The market and NVDA medians *are* the random-walk medians. Only tech departs materially, by −1.4%.
- **Sampling error swamps the "modal" edges.**
  - The standard error for p≈0.35 is ±11 points at n=20 and ±8 points at n=35, and the effective n is smaller (overlapping windows; NVDA effective n is about 6–10).
  - Tech: 38 vs 37. Semis: 37 vs 37. Market: 46 vs 34, about one standard error. NVDA: 47 vs 33, 1–1.5 standard errors.
- **Fix:** publish 5-point-rounded ranges, show the no-information row beside each verdict, and say "co-modal" where the gap is under 10 points.

### 3. HIGH-MED: "trend break" is not commensurate across layers, and one translation is wrong

**Translating trend lines at beta** (S&P→QQQ 1.43–1.62; QQQ→SOXX 1.5–2.04; QQQ→NVDA 1.16–1.41; S&P→NVDA 1.89–1.99)

| Line | S&P 500 | QQQ | SOXX | NVDA | σ-distance (realized / IV) |
|---|---|---|---|---|---|
| SOXX 465.00 | ≈7,394–7,408 | 678–692 | — | 198–210 | 0.64 / 0.82 |
| S&P 7,314 | — | 667–674 | 449–452 | **198–199** | 1.12 / 0.85 |
| QQQ 661.73 | 7,221–7,280 | — | 422–448 | 193–198 | 1.31 / 1.51 |
| NVDA 190.01 | 7,141–7,171 | 640–656 | 366–446 | — | 1.08 / 1.21 |

- **A semis "trend break" is a market *deeper* outcome.** At 0.64σ it happens 32–47% of the time by chance.
- **A market "trend break" is a tech *deeper* outcome**, unless RSP holds up. With RSP at 200.5 (the market's own trend-break signature), the market regression puts QQQ at about 675 for S&P 7,314.
- **The NVDA verdict's error (§2 and JSON):** "A market trend break (S&P 500 below 7,314) implies QQQ at about 660 or lower, which maps to NVDA at about 192 or lower."
  - At beta the line maps to QQQ 667–674 and NVDA 195–199. Both are inside NVDA's *deeper* bucket.
  - The verdict mapped the market's trend-break *zone* (6,850–7,250), not its *boundary*.
- **Fix:** relabel each layer's trend break as "below Jul 29 low (layer-specific)". In the final report, state which upper-layer outcome each line corresponds to.

### 4. MED-HIGH: stale or broken machine outputs and inconsistent inputs (practical; this will contaminate the final report)

**Stale JSONs.** Each file was saved before its audit addendum.

| File | Saved (UTC) | Still says | Audited figure |
|---|---|---|---|
| `market_verdict.json` | 03:42 | 40 / 38 / 22, median 7,480 | 46 / 34 / 20 |
| `tech_verdict.json` | 04:05 | 35 / 40 / 25 | 37 / 38 / 25 |
| `semis_verdict.json` | 04:16 | 26 / 39 / 35 | 26 / 37 / 37 |

- `market_verdict.json` also has `upper_layer_conditioning` empty and the "24-year high" real-yield error.

**The market JSON's shallow definition is not exhaustive.**
- It reads "stays at or above 7,505 … *RSP holds 207.16 on a closing basis*." The deeper definition requires S&P < 7,505.
- So "S&P ≥ 7,505 but RSP < 207.16" belongs to no bucket.
- Empirically, P(RSP < 207.16 | S&P shallow) = **27–28%**. That leaves about **13–14%** of all outcomes unassigned.
- The md table defines shallow on the S&P only. The JSON must match it.

**The session count.**
- Oct 15 – Dec 4, excluding Thanksgiving, is **36 sessions**. I checked it with an explicit calendar, and audit_market agrees.
- audit_semis E2 ("35 sessions") is wrong, and the semis addendum repeats it ("pulls close-state trend-break rates down a few points").
- **Reverse that adjustment.** It is small, about +1 point to semis trend break.

**Conflicting inputs across layers**

| Input | Market / tech say | Semis / NVDA say | Correct per facts.md / zz_corrections |
|---|---|---|---|
| Oct 28 hike odds | 35% | 24–32% | 24–32% |
| NVDA results date | "Nov 17 or 18" (the market JSON definition embeds "about two weeks after NVDA's Nov 17/18 results") | Nov 18–25 | Nov 18–25 |

- The market layer's trend-break path #1 leans on an Oct 28 hike, so that verdict was never re-run on the lower odds.

**The NVDA window floats.** NVDA's definition runs "to about Dec 9 if the print is Nov 25". The other three layers use a hard Dec 4. NVDA's buckets are then not comparable with the others, and the joint tables break. **Fix:** hard-stop every layer at Dec 4 and report "low after window" as a caveat.

### 5. MED: the invalidation rules contradict the window, the zones, or the definitions

**(a) Time-truncated invalidations contradict the Dec 4 window**
- **Market deeper:** "holds 7,505 through Nov 6 and reclaims 7,790.83 → shallow". Deeper can still occur later, and the market's own trend-break timing is Nov 10 – Dec 4.
- **NVDA deeper:** "every close ≥210 through Oct 30 plus a close >230.48". This contradicts the NVDA verdict's own "second window: earnings week (Nov 18–27)".
- **Tech shallow (JSON):** "a new QQQ closing low after Oct 29". A new low after Oct 29 that stays ≥697 is still shallow by definition. On the no-information benchmark, **39%** of QQQ-shallow paths make their low after Oct 29, so this rule would misfire about 4 times in 10.

**(b) Triggers sit inside the scenario's own zone**
- **Semis shallow:** "a TSMC beat that still closes SOXX red below 510". 510 sits inside the 497.4–515 shallow zone.
- **NVDA shallow:** "TSMC beat with NVDA closing <214.45 on Oct 15–16". 214.45 sits inside the 211–218.9 shallow zone.

**(c) Non-price triggers are declared to "mean a trend break"**
- **Market deeper downside invalidation (JSON):** "HY OAS >3.46%, A/D <4,960, or VIX/VIX3M >1 for 3+ sessions, *which means a trend break*." A trend break is defined on price.
- **Market trend-break invalidation:** it lists a reversal (HY back below 3.0%, contango, RSP reclaiming 207) as invalidating, then says a V-shaped flush "still counts as a trend break". It contradicts itself.

**(d) Market shallow invalidation "RSP closes below 207.16"** fires in **27–28%** of S&P-shallow outcomes on the no-information benchmark. It is a signal, not an invalidation.

**Fix:** separate a definitional line (closing basis only) from warnings. Never invalidate on a date before Dec 4.

### 6. MED: cross-layer confirmation signatures contradict each other

**The deeper scenario has opposite RSP conditions in two layers**
- **Market deeper confirms:** "a close below 7,505 **with RSP below 207.16**".
- **Tech deeper confirms:** "the S&P 500 closes below 7,505 **while RSP holds 207 or better**".
- They give opposite reads for the same joint scenario.
- Empirically, P(RSP holds 207.16 | S&P deeper) is 36–39%. So both signatures are common, and neither confirms anything.

**Semis shallow lists "QQQ holds 697" as a confirming signal. That condition is too loose.**
- SOXX 497.40 maps to **QQQ about 708–714** at beta 1.5–2.04. The semis verdict's own incremental model maps QQQ 700 to SOXX about 485–488.
- Tech's whole shallow zone (700–716) maps to SOXX 477–506, mostly inside the semis *deeper* bucket.
- The joint of tech shallow and semis shallow needs QQQ in the upper half of tech's shallow zone.

### 7. MED: the same evidence is counted more than once

**(i) The overnight print is counted twice in three layers**
- **Semis:** it weights the overnight-state base rates 60/40, then moves "three points from shallow to deeper (overnight state and Asia)".
- **Tech:** it conditions on "a −5% overnight print", then refuses to go further toward shallow because "the 697 hinge is only −3.3% away" from the overnight print.
- **NVDA:** it uses overnight-state rows, then argues against shallow because "the 210 hinge is only 3.8–4.1% below the overnight prints".
- The quotes are thin, pre-TSMC and not closes, and the scenarios are defined on closes.

**(ii) Macro factors are re-applied at every layer**
- The same factors appear as regime adjustments in all four verdicts: a hiking Fed, real yields at 2008 highs, AI-credit stress and crowding.
- Tech, semis and NVDA also take in the upper layer's verdict, which already contains those adjustments.
- The double count is largest in tech, about 5–7 points of shallow.

**(iii) "No capitulation" is counted as bearish evidence against shallow**
- Tech ("Low VIX means no capitulation yet"), semis ("no capitulation yet") and NVDA ("no index volatility capitulation") do this.
- The market verdict's own analysis says "A shallow low needs no inversion at all". The NVDA verdict shows NVDA's last three lows came on 0.96–1.05× volume.
- Missing capitulation is evidence that a *deep* low has not happened. It is not evidence against a shallow one.
- The original market verdict made the same move: it cut shallow "from about 50% to 40%", stacking the tech-damage argument on reference sets that already conditioned on that damage.

**Bear overreach**
- The original market verdict (40/38/22, corrected by audit) and the tech verdict both lean bear.
- Semis and NVDA are roughly neutral relative to their own evidence.
- The semis judgment table leans *bullish* in one row: P(SOXX trend break | QQQ deeper) is 0.43, against 46–76% in every empirical estimate. That partly offsets the bearish overnight double count.

### 8. LOW-MED: the timing windows are partly mechanical, and the deeper windows are too early

On the no-information benchmark, the share of each bucket's lows that falls inside the stated window:

| Layer | Shallow | Deeper | Trend break | No-information median date of a deeper low |
|---|---|---|---|---|
| S&P 500 | 63% | **29%** | 88% | Nov 16 |
| QQQ | 61% | **36%** | 91% | Nov 17 |
| SOXX | 67% | **43%** | 84% | Nov 3 |
| NVDA | 71% | **40%** | 89% | Nov 12 |

- **The shallow and trend-break windows are mostly a by-product of the bucket definitions.** Shallow lows come early and trend-break lows come late in any random walk. They are not catalyst insight.
- **The deeper windows are a real view, and a fragile one.**
  - They are centred on the Oct 28 cluster, about two weeks earlier than the no-information median.
  - The NVDA bear's own analog says deeper non-bear episodes took about **32 sessions (about Nov 30)** to trough.
  - NVDA's added "second window: earnings week" partly hedges this. The other layers have no equivalent.
- **The sequencing across layers is coherent:**

  | Layer | Expected break | Line |
  |---|---|---|
  | Semis | Oct 16–22 | 497.40 |
  | NVDA | Oct 16–28 | 210 |
  | Tech | Oct 21–29 | 697 |
  | Market | Oct 28–29 | 7,505 |

  Higher beta breaks first. All four name Oct 28 as the key event and TSMC as the first test.
- **But the semis rules overlap.**
  - Its deeper path breaks 497.40 "around Oct 16–22".
  - It calls a 497.40 break on more than 2× volume *before Oct 21* a trend-break signal.
  - Yet it lists more than 2× volume on the low day as a *deeper* confirmation.
  - The same volume reading points both ways.
- **The market layer's trend-break timing does not match semis.**
  - The market says semis and NVDA lows come *after* NVDA's results in a market trend break, which would be Nov 19 – Dec 4 or later.
  - The semis trend-break window starts Nov 3.

### 9. LOW-MED: the NVDA verdict overstates its consensus

- **The claim:** "Every independent lens puts the mode in the deeper bucket" (md §5), repeated in the JSON as "all independent lenses".
- **Its own table has three rows with a shallow mode:**
  - record-close, 3 years: 45/36/18;
  - holdout: 42/33/25;
  - holdout from the 1-year high: 47/29/24.
- Its no-drift simulation from the close is nearly tied (37/41/22), and my historical raw check is 40/34/26.
- **Horizons are mixed.** The record-close rows measure final depth with no time limit. The 36-session rows measure a fixed window. The market audit flagged the same issue (#18).

### 10. LOW: zone gaps, the volatility assumption, and one odd input

**The zones do not tile the buckets**

| Layer | Where | What falls outside the stated zones |
|---|---|---|
| NVDA | Deeper zone 198–209 omits 190–198 | About 32% of no-information deeper mass |
| Market | Gap 7,460–7,540 between the shallow and deeper zones | The median itself; only about 48% of deeper mass lies in its zone |
| Tech | Gaps at 697–700, 692–697, 661.73–672 and 655–661.73 | — |

**The SOXX forward-volatility choice is never stated, and it decides deeper vs trend break**
- Realized vol is 46% (1y) and 54% (6m). Implied vol is 35.6%.
- On realized vol, SOXX trend break is 43–47%. On IV it is about 32%.
- The verdict's 37% implicitly assumes something close to IV.

**QQQ IV of 17.0% (IBKR) against VIX at 16.87 is implausible.**
- QQQ's realized vol runs 1.5× the S&P's, so its IV would normally be well above VIX.
- Tech uses the 17.0% as a complacency signal. Treat it as unverified.

---

## (a) Probability coherence: implied marginals and the joint table

**Upper-layer verdict pushed through the empirical conditionals** (1y realized | IV-scaled)

| Implied layer | From | Result | Published |
|---|---|---|---|
| QQQ | Market 46/34/20 | **50 / 35 / 14 \| 50 / 35 / 15** | 37 / 38 / 25 ✗ |
| S&P 500 (reverse) | Tech 37/38/25 | 38 / 31 / 31 | 46 / 34 / 20 ✗ |
| SOXX | Tech 37/38/25 | 22 / 24 / 54 \| 26 / 32 / 42 | 26 / 37 / 37 |
| SOXX | Market-implied tech | 29 / 27 / 44 \| 34 / 34 / 32 | 26 / 37 / 37 |
| SOXX | Corrected tech, about 42–44 / 37–38 / 19–20 | 25 / 26 / 49 \| 29–30 / 33 / 37–38 | 26 / 37 / 37 ≈ ✓ |
| NVDA | Market 46/34/20 | 37 / 43 / 20 \| 40 / 45 / 15 | 33 / 47 / 20 ✓ (slightly bearish) |
| NVDA | Tech 37/38/25 | 30 / 44 / 27 \| 33 / 47 / 21 | 33 / 47 / 20 |
| NVDA | Semis 26/39/35 | 39 / 43 / 18 \| 38 / 46 / 16 | 33 / 47 / 20 |

**The semis judgment table against the empirical estimates** (P(SOXX bucket | QQQ bucket), shallow / deeper / trend break)

| Given QQQ | Semis judgment | Empirical range |
|---|---|---|
| Shallow | 60 / 36 / 4 | 50–68 / 31–35 / 1–17 |
| Deeper | 7 / 50 / **43** | 2–10 / 21–47 / **46–76** |
| Trend break | 1 / 6 / 93 | 0–1 / 3–11 / 88–97 |

- The deeper row under-assigns trend break.
- That error roughly offsets tech's over-bearishness. So the semis marginal is coherent *by accident*.
- With the corrected tech table, IPF gives P(SOXX | QQQ) of 51/41/7, 10/45/45 and 1/11/88. The deeper and trend-break rows match the IV-scaled empirical rows (10/44/46 and 1/11/88). The shallow row is close (empirical 60/33/7).

**Can NVDA's shallow probability exceed SOXX's? Yes, and it needs no extra "decoupling" premium.**
- NVDA's 210 hinge is 0.37–0.42σ away. SOXX's 497.40 is 0.25–0.32σ away.
- The no-information gap is +6 to +8 points (38 vs 30; 41 vs 35). The verdicts show +7 (33 vs 26).
- NVDA's low beta to SOXX (0.48) is already inside the 1y covariance.
- **The joint:**
  - P(NVDA holds 210 while SOXX breaks 497.40) ≈ 0.37×0.37 + 0.37×0.16 ≈ **20%**.
  - The reverse, P(SOXX holds 497.40 while NVDA breaks 210), ≈ 8%.
- **The direction is robust. The size depends on the regime.** If NVDA's ratio to SOXX on big down days reverts to its 5-year level of about 1.0, P(NVDA shallow | SOXX deeper) falls from about 40% to about 10–15%.

**Joint table: market × NVDA** (IPF to the published marginals, seeded with the 1y empirical joint; % of all outcomes)

| | NVDA shallow (≥210) | NVDA deeper | NVDA trend break (<190.01) | Market total |
|---|---|---|---|---|
| **S&P shallow (≥7,505)** | 24.8 | 18.2 | 3.0 | 46 |
| **S&P deeper** | 6.9 | 20.2 | 6.9 | 34 |
| **S&P trend break (<7,314)** | 1.3 | 8.7 | 10.1 | 20 |
| **NVDA total** | 33 | 47 | 20 | 100 |

**The implied P(NVDA | S&P) matches the empirical estimate**

| Given S&P | Implied by the joint | Empirical, 1y |
|---|---|---|
| Shallow | 54 / 39 / 7 | 59 / 35 / 6 |
| Deeper | 20 / 59 / 20 | 24 / 56 / 21 |
| Trend break | 6 / 43 / 50 | 7 / 41 / 51 |

- So the market and NVDA layers are mutually coherent.
- **About 1 path in 5 has the market holding 7,505 while NVDA breaks 210.** That is consistent with May–Jul 2026, when NVDA fell −19.4% with the S&P's worst close at −4.5%.
- In about half of market trend breaks, NVDA still holds 190.01.

**With the recommended marginals** (market 45/35/20 × NVDA 36/45/19), the same method gives:

| | NVDA shallow | NVDA deeper | NVDA trend break |
|---|---|---|---|
| S&P shallow | 26.3 | 16.1 | 2.6 |
| S&P deeper | 8.2 | 20.1 | 6.7 |
| S&P trend break | 1.5 | 8.7 | 9.7 |

The implied P(NVDA | S&P) rows are 58/36/6, 23/57/19 and 8/44/49, which essentially equal the empirical estimates.

## (b) Zone coherence

**Hinges.** S&P 7,505 ≈ QQQ 696–700 ≈ NVDA 209–210. These three line up well. SOXX's 497.40 is a tighter test: it maps to S&P about 7,590, QQQ 708–714 and NVDA 212–217.

**Medians and most-likely zones**

| Layer's figure | Translated at beta |
|---|---|
| Tech median 689 | S&P 7,423–7,458 (the market *deeper* bucket) |
| Market median 7,505 | QQQ 696–700 |
| Market most-likely 7,420–7,600 | QQQ 683–713 |
| Tech most-likely 680–700 | S&P 7,356–7,530 |

- Tech's view is about 1% below the market's view, the same tilt as Finding 1.
- **Beta translation of SOXX and NVDA medians is misleading.**
  - For a high-idiosyncratic-vol name, the minimum falls further than beta times the index minimum.
  - For example, NVDA's no-information median of 206.6 maps at beta to S&P about 7,445, while the S&P's own no-information median is 7,504.
  - Use the joint simulation, not beta, for SOXX and NVDA. Linear beta is adequate only for QQQ (correlation 0.91).

**The remaining contradictions are Findings 3 (trend lines) and 6 (semis shallow needs QQQ about 710 or above, not 697).**
- NVDA's deeper zone (198–209) maps to QQQ 663–700 and S&P 7,289–7,503. That is coherent with tech deeper.
- The semis trend-break zone (420–460) maps to QQQ 636–688. It overlaps tech's deeper zone, which is consistent with the semis claim that its trend break can occur with tech deeper.

**RSP mapping (market).** The concordance with the S&P bucket is weak:

| S&P bucket | RSP in the matching bucket |
|---|---|
| Shallow | 72% |
| Deeper | 51% |
| Trend break | 39% |

So the RSP equivalents (207.16 and 200.5) are loose signals, not mappings.

## (c) Timing coherence

**Coherent:**
- the shallow lows (Oct 15–23/30);
- the deeper clusters around Oct 28 – Nov 10/13;
- the trend-break windows (Nov 3/10 – Dec 4);
- the beta-ordered sequence of breaks;
- the catalyst anchors: TSMC Oct 15, opex Oct 16, META/LRCX/TXN Oct 21, FOMC/MSFT/GOOGL/KLAC Oct 28, AMD Nov 3, CPI and CoreWeave about Nov 10, NVDA Nov 18–25.

**Incoherent:**
- **Inputs:** stale hike odds and NVDA date in the market and tech layers (Finding 4). NVDA's floating window end (Finding 4).
- **Window placement:** the deeper windows are too early and narrow relative to both the benchmark and the NVDA bear's analog (Finding 8).
- **Contradictory signals:** the semis volume rules contradict each other (Finding 8). The market's "high-beta trend-break low comes after NVDA's results" conflicts with the semis Nov 3 start (Finding 8).
- **Time-truncated invalidations:** three of them contradict the Dec 4 window (Finding 5a).

## (d) Bias check: summary

| Layer | Its own evidence | Published | Read |
|---|---|---|---|
| Market | Data 46–58 shallow; no-information 47–56 | Original 40/38/22 → audited 46/34/20 | Original was bear overreach (double-counted tech damage, a mis-built anchor set). Audited is fine |
| Tech | Unconditional 58/29/13; state-conditioned 42/39/19 | 37/38/25 (audited) | Bear overreach. The judgment table is outside the empirical envelope, plus a macro double count and an overnight double count |
| Semis | Close-state 42–45/29–33/24–29; overnight state 20–25/40–46/31–40; IV benchmark 35/33/32 | 26/37/37 | Roughly balanced. A bearish overnight double count offsets a bullish trend-break under-assignment in the deeper row of its table |
| NVDA | Average of its lenses 35/46/19; no-drift simulation from the close 37/41/22 | 33/47/20 | Slight bear tilt. It inherited tech's tilt, double-counted the overnight print, adopted the bear's zone (200–209, centre 205) almost verbatim, and overstated its consensus |

- **Bull side:**
  - The tech and NVDA bull briefs were written against the stale market 40/38/22, before the tech and semis verdicts existed. That is a process gap.
  - No layer shows anchoring on the bull case beyond the semis table row noted above.

## (e) Invalidation levels

**What is right**
- All four layers use closing-basis boundaries.
- Each layer's boundary is specific and sits at a real structural level (the Jul 29 lows, the Sep 14/16 lows and the Mar 30 AVWAP).

**The minor slip:** the market's 7,314 and 7,505 are intraday prints (the Jul 29 close was 7,316.15; the range floor was 7,504.78 intraday). The effect is trivial.

**What is wrong is covered in Findings 5 and 6:**
- time-truncated rules;
- triggers inside the scenario's own zone;
- non-price triggers declared to "mean" a price bucket;
- the self-contradictory market trend-break invalidation;
- RSP-based triggers with high false-positive rates;
- opposite RSP signatures for the deeper scenario in market vs tech.

**Cross-layer ladder.** The upper-layer lines quoted in lower layers are mostly consistent:
- tech uses SMH 503.6 (≈ SOXX 463);
- semis uses NVDA 208.8 (≈ SOXX 465 at 0.57);
- NVDA uses QQQ 683.7 and SOXX 465.

**One loose use:** the NVDA verdict lists "S&P below 7,505 with RSP below 207.16", which is *market deeper*, as a trend-break confirmation. Empirically P(NVDA trend break | market deeper) is only 13–28%.

## (f) Scenario definitions (MECE)

**The md definitions are mutually exclusive and exhaustive.** In each layer they are lowest daily close Oct 15 – Dec 4 against two contiguous boundaries.

**Exceptions:**
- **Market JSON:** the RSP clause in the shallow definition leaves about 13–14% of outcomes unassigned (Finding 4).
- **NVDA:** the floating window end (Finding 4).

**The zones are subsets of their buckets, but they leave large gaps (Finding 10).** The "most likely" zones straddle the hinges in market (7,420–7,600) and tech (680–700), which is acceptable if labelled.

## Recommended probability tables

Changes are made only where justified. Ranges reflect sampling error of about ±8–10 points. Each row reads shallow / deeper / trend break.

| Layer | Latest audited | **Recommended** | Justification |
|---|---|---|---|
| **Market** (S&P 7,505 / 7,314) | 46 / 34 / 20 | **No change: 46 / 34 / 20** (publish as about 45 / 35 / 20, ranges 40–55 / 28–38 / 15–25) | Matches the data (46–58 shallow) and the no-information benchmark (47–56). The reverse implication from tech (38/31/31) comes from an incoherent table, so it is no reason to move. Fix the JSON |
| **Tech** (QQQ 697 / 661.73) | 37 / 38 / 25 | **43 / 38 / 19** (ranges 38–48 / 33–42 / 15–23) | Market-implied 50/35/14–15 across all vol variants. Own state-conditioned base rate 42/39/19. Trend-break ordering: QQQ's line is the farthest (1.31σ) and maps below S&P 7,314, so it should not exceed the market's 20. Remove the macro and overnight double counts. The residual bear tilt is kept for the untested mega-cap reports (Oct 21–29). IPF check against market 45/35/20 gives P(QQQ \| S&P) of 82/18/1, 18/70/12 and 1/27/72, inside the empirical envelope |
| **Semis** (SOXX 497.40 / 465) | 26 / 37 / 37 | **No material change: 26 / 37 / 37.** Reversing the wrong 35-session tweak argues for 26/36/38, which is within noise | The tech correction lowers the top-down trend break by about 4 points. Fixing the deeper row of its table raises it by 1–13 points. The forward-vol choice (IV vs realized) swings trend break ±7. Report deeper and trend break as **co-modal** and state the vol assumption |
| **NVDA** (210 / 190.01) | 33 / 47 / 20 | **36 / 45 / 19** (ranges 30–42 / 40–50 / 14–24) | Remove the double-counted overnight conditioning. Market-implied 37–41 shallow; semis-implied 38–39; corrected-tech-implied 32–37 / 43–46 / 18–25; its own no-drift simulation from the close 37/41/22. Jointly coherent with the market (see the second joint table) |

## Single biggest weakness

**There is no shared joint model, and so no check on false precision.** Each layer turns the layer above into its own numbers through a hand-built conditional table, then re-applies the same macro and overnight evidence.

**The result has two parts:**
1. **The tech layer contradicts the market layer in a way the betas forbid.** It puts 25% on trend break against the market's 20%, although QQQ's trend line is the farthest of the four in volatility terms. Its table sits 10–20 points outside every empirical estimate.
2. **Once that error is removed, every layer lands within about ±5 points of a driftless random walk at current volatility.** That includes the median lows: S&P 7,504 against "about 7,505", and NVDA 206.6 against 205–207. The thin "modal" calls (deeper vs shallow in tech, deeper vs trend break in semis) and one-point probabilities therefore imply knowledge the analysis does not show.

**The scenario labels compound this.** "Trend break" is drawn at each instrument's own Jul 29 low, so it means a 0.64σ event for SOXX but a 1.31σ event for QQQ. The four tables look like one shared regime call, but they describe different-sized events.

**What the final report should do:**
- present one joint table with no-information benchmark rows;
- use 5-point ranges;
- align the trend-break definitions, or relabel them as layer-specific.

## Method notes and caveats

**The scripts**

| Script | What it does |
|---|---|
| `coh_scripts/c1_mc.py` | Joint bootstrap: 1y, 6m and 2y windows |
| `c2_hist.py` | Historical overlapping windows since 2021 (about 33 independent windows) |
| `c3_joint.py` | Implied marginals, IV scaling, IPF |
| `c4_zones.py` | Zone coverage and median lows |
| `c5_ipf.py` | Joint tables |
| `c6_timing.py` | Timing of lows |

**The beta translations** are in this report's §3 and §(b), computed from the Oct 14 closes.

**Caveats**
- The bootstrap is driftless and samples 5-day blocks of the last 252, 126 or 504 sessions. It keeps cross-asset dependence and some volatility clustering, but it carries no view, no catalysts, and no regime change beyond what is in the sample.
- The 1y sample includes the Jun–Jul 2026 rotation. Only the 2y sample includes the Apr 2025 shock.
- Historical windows overlap heavily, and include 2022, which inflates the trend-break share.
- The conditional tables carry ±5–10 points of uncertainty in the smaller cells.
- I took no IBKR pulls. Overnight prices are as quoted in the verdicts, and none of my conclusions depend on them.
