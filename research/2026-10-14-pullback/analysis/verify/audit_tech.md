# audit_tech: adversarial numbers audit of analysis/tech_verdict.md

*Auditor, about 04:20 UTC Oct 15, 2026. Data runs through the Oct 14 close.*

**Scope**
- Audited: `analysis/tech_verdict.md`.
- **`analysis/tech_verdict.json` does not exist**, so it was not audited.

**Method**
- Every number was checked against DATA_BRIEF and the raw CSVs, using my own code in `scratchpad/audit_tech_code/`:
  - `br_indep.py`, `br_state.py`, `br_rates_full.py`, `br_postrec.py`, `episodes_audit.py`: base rates, written independently with a per-record loop rather than the verdict's per-day loop.
  - `claims.py`, `it_breadth_audit.py`: everything else.
- I also ran the verdict's own `tv_scripts/` to find out *why* some results differ.
- One read-only IBKR snapshot at 04:15 UTC: QQQ 720.95, IV 17.0%, 52-week IV percentile 8.4%; XLK last 188.11 (traded 03:23 UTC). These match the verdict's live figures.

---

## A. Errors

| # | Sev. | Claim in verdict | Correct value | Evidence |
|---|---|---|---|---|
| 1 | **HIGH** | §5 / §6: "+10-year up ≥40 bp in 3 months: n=13, **23/77/0**". "The regime-matched rate analog gives **0% trend break**." Twice used as *the* reason to keep trend break below the 28% top-down figure ("grind rather than collapse") | **The 0% is a data-window artefact.**<br>• The verdict used `dl_fred/DGS10_full.csv`, which starts 1999-01-04, so the filter can only fire from April 1999. 8 of its 13 signals are from 1999–2000.<br>• With the full 1962– series already in the scratchpad (`dl_bear_fred/DGS10.csv`; identical on the overlap, max difference 0.0), the set is **n=16, 31/44/25** (first-close rule) or **n=20, 30/50/20** (the verdict's own filter timing).<br>• It adds 1987-09-08 (−39.2%), 1987-10-08 (−39.9%), 1994-03-25 (−15.1%) and 1996-06-18 (−14.4%).<br>• **Rate shocks do produce trend breaks**, at about 20–25%. | `br_rates_full.py`; verdict's run of `base_rates_tech.py` |
| 2 | **HIGH** (method; direction of impact unclear) | §5 bold "today's state" row: "+ SOX ≥10% below its 20-day high: **n=14, 43/29/29**". The same flaw sits under "+SOX+VIX<20 n=10 40/20/40", "+SOX 2003– n=5 20/40/40" and "post-recovery + SOX n=10 60/40/0". §6 cites "two of five since 2003 broke" and "4 of 10 in the low-VIX set broke" | **Does not reproduce under the stated definition** ("NDX *first* close −3.5% to −6% below a record").<br>• The scripts apply the filter *before* marking the record as used. So the signal becomes the first in-band day on which SOX happens to be broken, up to 10 sessions after the record.<br>• **9 of the 14 signals came after NDX had already closed below −6%**, outside the stated band. Examples: 2025-02-28 after −7.33%; 1999-10-20 after −8.41%; 2019-05-17 after −6.65%; 2019-08-07 after −7.50%.<br>• Strict first close in band: **n=4, 50/25/25**. First close below −3.5%: **n=2, 0/50/50**.<br>• Best state match (in band, lowest close so far, never below −6%): **n=5, 20/40/40**, median −11.8%.<br>• +VIX<20 on the same matched definition: n=3, 0/33/67. 2003+ only: n=1–2. Post-recovery + SOX on the first band day: n=3, 67/33/0.<br>• **The n=14 precision is illusory:** depending on how signals are de-clustered, the row ranges from 50/25/25 to 0/50/50. | `br_state.py`, `br_indep.py` |
| 3 | MED | §2 / §5: uses [MV] **40/38/22** with a median of **~7,480**. Combined top-down **34/38/28**. "Trend break is below [MV]'s implied 28%" | **Stale.**<br>• The audit addendum inside `market_verdict.md` ("lower layers must use these corrections") gives **46/34/20**, with the median at or just above 7,505.<br>• Put through the verdict's own conditional matrix, that gives **38.1 / 36.7 / 25.2**. The implied trend-break figure falls from 28 to **25**, and **top-down now favours shallow by about 1 point**.<br>• Addendum item 3 also matters: under MV's regression, QQQ at 697 with RSP flat ≈ S&P 7,579 (shallow), and breaking 7,505 needs QQQ ≈ 680. "The layers line up almost exactly" holds only under the beta mapping. | `market_verdict.md` addendum; arithmetic |
| 4 | MED | §5 row "Same, 2003–: **n=43, 63/30/7**". It feeds the "unconditional ≈ 58/29/13" | **Truncation artefact.**<br>• The script slices NDX from 2003, so the running maximum restarts in 2003. **20 of the 43 "records" are not all-time highs**: NDX did not regain its 2000 high until 2015-11-03.<br>• Signals from true all-time highs in 2003+: **n=23, 52/39/9**.<br>• The unconditional average becomes about **54/33/13**. | `br_indep.py` truncated-series check |
| 5 | LOW | §5 table nesting: "+ SOX ≥10%… (n=14)" sits directly under "NDX from a −5% state, n=45", which implies it is a subset of that set | It is a subset of the n=83 set (−3.5% to −6%). The actual −5% state + SOX subset is n=6, 33/33/33 (band-first) | `br_indep.py` H |
| 6 | LOW | §4: "Oct 28 hike odds were about **35%** (single source)" | Superseded by `research/zz_verification_corrections.md`: late-night pricing was **about 24–32%** (Polymarket 23.5, Kalshi 23–24, Investing.com 27.6, LSEG 31.6). The 35% was a 3:50 pm snapshot | corrections file #1 |
| 7 | LOW | §1: "**Both** the 10-day and 20-day averages have rolled over" | Only the 10-day turned down (749.34 → 748.26). The 20-day is **still rising** (741.34 → 742.55 on Oct 14) | `claims.py` §2 |
| 8 | LOW | §3: QQQ 200-day "**694.7** by Dec 4" | **694.1.** 694.7 treats Thanksgiving (Nov 26) as a trading day. 683.2 (Nov 6) and 688.6 (Nov 20) are correct | `claims.py` §13 |
| 9 | LOW | §2 mapping: trend break "≈ **605–662**" at beta 1.43–1.62 | At the stated beta range it is **≈596–666**. 605–662 uses beta 1.5 only. The other rows use the full range correctly | arithmetic |
| 10 | LOW | §6: "about eight more **points** of SMH downside alone" | It should say **~8%**. Eight SMH points ≈ 1.4% of SMH ≈ 0.55% of QQQ. At 8%: 0.387 × 8 = 3.1% against the 3.3% needed, so the claim holds | regression b = 0.387 |
| 11 | LOW | §2: "In Dec 2024 the S&P 500 fell −4.3% and QQQ **only** −6.1%", offered as tech holding up in a broad selloff | The numbers are right, but each is measured over its own window, and QQQ fell *more* than the S&P (about beta 1.42), so the example does not show tech decoupling. Over the S&P's own window (Dec 6 → Jan 10), QQQ fell −3.66%, which *would* support the point | `claims.py` §5 |
| 12 | LOW | §4 mega-cap table: "Now: SMH −10.9%" | That is measured from SMH's Oct 5 high, while the other rows run from QQQ's peak date. From Oct 6 it is −10.7%. The Oct 2025 – Mar 2026 SMH cell is shown as "—" but is computable (−1.6%), and that value strengthens the mega-cap argument | `claims.py` §15 |
| 13 | LOW | §4: "real yield **2.88%**, the highest since 2008" | 2.88% is the Oct 13 level. The 18-year high was **2.95% on Oct 5** | macro_rates.md L30/L140 |
| 14 | LOW | Deeper-correction timing: the summary table says "Oct 27 – Nov 13"; §7's path says the low comes "Oct 28 – Nov 10" | The verdict gives two different windows | internal |
| 15 | LOW | "My median low is about 688–690" | With 35% of mass at or above 697 and the deeper core at 680–690, the implied median is about **684–686**. 688–690 holds only if 37.5% of the deeper bucket's mass sits in its top 9 points | arithmetic |
| 16 | LOW | §4 rotation gainers and losers lists | The gainers omit XLRE +0.95%, which is larger than XLF +0.94%. The losers omit XLY −0.20% and XLB −0.12%. Cosmetic | `claims.py` §14 |
| 17 | LOW | Caveats: NVDA results "Nov 17 or 18" | Corrections file #5: the date is **not announced**; the realistic window is Nov 18–25 | corrections file |
| 18 | LOW | "Discretionary US long/short net leverage" (2nd percentile) | The source says "US *fundamental* L/S net leverage" (Goldman prime book via Tickmill). The SINGLE-SOURCE tag is preserved | sentiment_positioning.md L70 |
| 19 | LOW | QQQ Oct 13 flows "conflict between vendors" | The ETF.com print (data as of 6 am ET Oct 13) probably covers the prior session, so the two figures may be consecutive days rather than a conflict. The UNVERIFIED tag is kept | sentiment_positioning.md L330–337 |

---

## B. Base-rate re-runs: do they reproduce?

All of these are my own code (`br_indep.py`). Buckets use the exact −8.248% / −12.891% thresholds. Rounded thresholds give identical buckets.

| Verdict row | Verdict | Auditor (band-first) | Auditor (first close below −3.5% must be in band) | Verdict |
|---|---|---|---|---|
| NDX, above a rising 200-day, 1985– | 83: 59/28/13 | **83: 59/28/13** | 75: 59/28/13 | **Reproduces; robust** |
| Same, 2003– | 43: 63/30/7 | 23: 52/39/9 (true all-time highs) | 22: 55/36/9 | **Fails** (#4) |
| QQQ 1999– | 25: 52/32/16 | **25: 52/32/16** | 23: 57/30/13 | Reproduces |
| −5% state | 45: 47/31/22 | **45: 47/31/22** | 32: 41/34/25 | Reproduces; sensitive to the rule |
| + SOX filter ("today's state") | 14: 43/29/29 | 4: 50/25/25; state-matched 5: 20/40/40 | 2: 0/50/50 | **Fails** (#2) |
| + SOX + VIX<20 | 10: 40/20/40 | 3: 67/0/33; state-matched 3: 0/33/67 | 1 | **Fails** (#2) |
| + SOX, 2003– | 5: 20/40/40 | 1 | 1 | **Fails** (#2) |
| + 10-year +40 bp | 13: 23/77/0 | 10: 30/70/0 (1999– data); **16: 31/44/25 (full 1962– data)** | 9: 33/67/0 | **Reproduces only on truncated data** (#1) |
| Post-recovery | 55: 67/27/5 | **55: 67/27/5**; 41 of 55 before 2001 | — | Reproduces |
| Post-recovery + SOX | 10: 60/40/0 | 3: 67/33/0 | — | **Fails** (#2) |
| XLK −5% to −8%, rising 200-day | 19: 37/47/16 | **19: 37/47/16** | 16: 38/44/19 | Reproduces |

**Episode statistics also reproduce** (`episodes_audit.py`):
- NDX given −4.04%: n=80, median −7.7%.
- NDX given −5%: n=60, median −10.7%.
- XLK given −5.73%: n=25, median −11.7%.
- NDX given −4.04% with SOX broken on the day it was first hit: n=8, median −11.2%.

---

## C. Claims I could not verify

- **The exact IBKR QQQ print of 721.00 at about 03:59 UTC.** It is consistent with 720.95 at 04:15 UTC.
- **QQQ option put/call of 0.84 against a 1.10 average.** These are IBKR fields reported in sentiment_positioning.md; I did not re-pull them.
- **The conditional matrix in §2** (0.72 / 0.25 / 0.03 and so on). It is author judgment, and it is labelled as such.
- **"Conditioning on today's state moves it to roughly 42/39/19."** No stated combination of table rows gives this. The nearest averages of the state rows land around 38–43 / 40–46 / 13–19.
- **"Net 35/40/25."** This is judgment.
- **External facts.** These are attributed correctly to their research files, with tags preserved, but I did not re-check them myself:
  - BofA FMS 37% (CONFIRMED in SP);
  - Goldman L/S at the 2nd percentile and Nomura at the 86th (SINGLE-SOURCE);
  - CoreWeave at about 15% (corrections: about 14.8% YTM intraday);
  - TSMC +50.9% y/y (CAT, 6-K);
  - ASML sold out for 2027–28;
  - NVDA 7 of 9 lower five sessions after results (CAT);
  - midterm NDX seasonality of +5.1% and 90% (SP);
  - the 2018 NDX decline of −23%;
  - the AMZN date (estimate);
  - the GDP/PCE date;
  - TSMC results not out at 04:00 UTC.

---

## D. Claims verified OK: about 160

Grouped by section; each value or row was checked.

- **Bottom line (20)**
  - Every drawdown range: −5.7/−7.9, −8.9/−11.5, −13.8/−18.4, tail −20%.
  - Every zone lies inside its own boundary; probabilities sum to 100.
  - The XLK equivalents are consistent with the 1.31 beta.
  - The most-likely zone %s for QQQ (−7.9/−10.5 and −4.0/−6.7) and XLK (−10.4/−13.9 and −5.0/−8.6).
  - Overnight −5.1%.
  - XLK 6-month beta to QQQ 1.313, correlation 0.956.
  - XLK 180.51, 166.57 (Jul 29 close) and 167.1.
  - Fri Dec 4 is 36 sessions from Oct 15.
- **§1 (18)**
  - QQQ: −4.04 / −4.45; session 6; 50-day, 50-day EMA, 100-day and 200-day levels and %s; slopes; RSI.
  - The overnight print sits below 721.12, through the Sep 21 gap and inside the 716.6–722 band.
  - XLK: −5.73; RSI 43.1; +0.3% vs its 50-day; +14.0% vs its 200-day.
  - QQQ 10-day 748.26 and 20-day 742.55.
  - Distribution days 7 of 25 and 4 of the last 5.
  - Volume ratios 1.46 / 1.58 / 1.75 / 0.77 / 0.89.
- **§2 (14)**
  - Betas.
  - The shallow, hinge and deeper beta mappings.
  - Jun 2 – Jul 29: QQQ −11.32, XLK −15.96, RSP +2.71, worst S&P close −4.5% on Jun 10.
  - Dec 2024 numbers.
  - The combined-table arithmetic at 40/38/22.
  - Oct 2025 – Mar 2026: −9.1 / −12.2.
  - SOXX and NVDA betas.
- **§3 (33)**
  - Regression 0.387 / 0.324, R² 0.947; SMH term −4.14; MEGA6 −0.13.
  - AAPL at its 52-week high; MSFT −1.8% and +5.9%; META +13.5%; GOOGL −13.7% (May 13); AMZN −10.5% (Aug 3).
  - IT excluding semis: 52.7 / 69.1 / −20.9 / 50.9 / 21.8.
  - All IT: −23.8; 76.0 → 44.0; 29.3% and 17.3% up; semis 0% and 5% up.
  - Post-recovery n=55, 41 of them before 2001.
  - July: 661.73, +3.3%, +9.36%; MSFT +18.14, AMZN +17.64; MSFT +15.51.
  - Episode statistics (n=80 / 60 / 8 / 25).
  - Rotation rows (−4.67 / +2.71, −7.03 / −1.67, −3.79 / −1.24, −4.04 / −0.11).
  - Ratios at the record: −1.69, −0.64, −7.25.
  - MSFT and META vs Jul 30 (+18.3 / +36.8) and vs Jul 31 (+14.8 / +32.5).
  - 200-day on Nov 6 and Nov 20.
- **§4 (30)**
  - Ratio levels and distances: 0.9472, 0.9454, +1.9%, −4.50% from Jun 18; 0.2474, −5.18% from Jun 2; 0.1626, −6.86%. QQQE −3.63%.
  - Ten sector-ETF moves; the Oct 8 / Oct 14 table; adv/dec.
  - IT sector breadth: third-highest 200-day reading, −5.52 median weekly return.
  - Mega-cap table: −13.6 / −24.8 / −15.9, −12.2 / −17.6, −11.3 / −20.2 / −9.1. The ≥9% rule also holds for Feb–Apr 2025 (MEGA6 −26%).
  - The deeper-bucket regression arithmetic.
  - VIX 16.87; ratio 0.898; Jul 29 VIX 20.66 and ratio 0.961.
  - QQQ IV 17.0% at the 8th percentile.
  - TNX −12.1 bp while QQQ fell −3.6%; HY 3.16%; CCC at a 3-year high; Fed hike Sep 16.
- **§5–6 (17)**
  - The n=83, QQQ n=25, −5% n=45 and XLK n=19 rows.
  - +63 bp.
  - ORCL −58.3%.
  - 721 inside the cluster; 697 is −3.33% away.
  - 10-day and 40-day analogs.
  - GOOGL −7.13, META −7.95.
  - The HY, VIX and ratio conditions.
- **§7–9 (28)**
  - QQQ Mar 30 low of 555.60, which gives the Mar–Oct Fibonacci levels 713.95 / 683.69 / 659.23 / 634.77. XLK low of 126.68 gives 174.0.
  - Sep 17 gap; Fibonacci levels; volume nodes; −10% / −15% / −20% levels; 685.82; 660.34; Apr 17 gap.
  - The 200-day at 680–695 for Oct 30 – Dec 4.
  - Dates and weekdays: Oct 16 options expiration (Fri), Oct 21 (Wed), Oct 28 (Wed).
  - SMH 503.6; QQQ/SPY 200-day 0.929.
  - All 11 QQQ and all 6 XLK key-level rows' %s and components, including the Sep 16 close of 704.72. XLK row 173–178.8 has a cosmetic gap: the 178.8 edge is the Aug 24 low, which is not named.

---

## E. Does any error change the verdict's scenario probabilities, zones or key level?

**Yes, the probabilities move modestly. The zones and key level do not.**

1. **The stated derivation of the probabilities is broken in two places.**
   - It uses stale market inputs (#3). With the corrected 46/34/20, the top-down mapping gives **38/37/25**, not 34/38/28.
   - Its main reason for holding trend break below the top-down figure, the "0% trend-break rate analog" (#1), is an artefact. With full yield history, the rate analog gives about **30/47/23**.
2. **The "today's state" SOX row (#2) is not robust.** Its state-matched version, n=5 at 20/40/40, is more bearish. The corrected "2003–" row (#4) is less shallow.
3. **Re-deriving with corrected inputs lands at about 35–38 / 37–40 / 25.**
   - Trend break at 25% survives, but for a different reason: rate-shock analogs show about 20–25% breaks, not 0%.
   - Shallow should rise by about 2–3 points.
   - **Calling deeper the leading bucket is no longer supported.** Shallow and deeper are a coin flip, about 37/38, and the corrected top-down mapping slightly favours shallow.
4. **Unaffected:**
   - Every zone (700–716 / 672–692 / 620–655, and the XLK equivalents).
   - The boundaries (697 / 661.73).
   - The single key level (QQQ **697–700 on a closing basis**, XLK 180.5).
   - The key event (Oct 28).
   - All the price-level, moving-average, AVWAP, Fibonacci and % arithmetic was correct.
