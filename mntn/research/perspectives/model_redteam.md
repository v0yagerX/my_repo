# MNTN model v1 red-team audit (model code mntn_model.py, output 00-model-output-v1.md)

## Bottom line

The model's mechanics and its FY26 and FY27 base calibration hold up. Five things push the valuation too high or misstate the risk:

1. **The bear case is a tail outcome carrying a central weight.** Revenue falls three years in a row to $290M by 2030, and it gets 30% probability.
2. **The base case is too high for 2028–30.** It runs at the threat-contained end on both growth and margin.
3. **Cash taxes are too low in FY26–28.**
4. **The bull case is generous.** It sits above the top of the FY27 consensus range, uses an 11x multiple and leaves out dilution from the performance options.
5. **The DCF mechanics are inconsistent** between the scenario DCF and the reverse DCF.

I re-ran the model with all the changes below; the scripts are in redteam/ (recal.py, isolate.py, rdcf.py, mult.py). The probability-weighted value falls from **$15.83 / $19.62 / $14.58** (end-2027 multiple present value / 2030-exit present value / DCF) to **about $13.1 / $14.5 / $14.1** [estimate]. That is still about 30–40% above $10.25. The verdict is directionally unchanged, but the upside is roughly halved on the 2030-exit method.

---

## Prioritized defects and the changes I recommend

### 1. The bear case is more severe than any threat dossier's severe case, yet carries 30% weight (high priority)

- **What the model has:** bear 2030 revenue is $290M (−18% from FY26), falling −6% / −8% / −6% in 2028–30, with a 2030 adj. EBITDA margin of 18.8%.
- **What the research says:**
  - E's severe scenario C: $410M in 2030, adj. EBITDA margin in the low 20s, 15% probability [E; estimate].
  - F's victim case: −25% to −40% against the no-agent path, 20% probability [F].
  - H's bear: revenue −10% to −20%, 20–25% probability [H].
  - G's bear still grows high-single-digit to low-teens by 2028 [G].
  - J's 2027 recession is a trough year followed by recovery, not a multi-year decline [J].
  - None of these has absolute revenue declining from 2028 to 2030.
- **The judges do not support 30% either.** Their average placement is Victim 13%, At Risk 45%, Neutral 32%, Beneficiary 9%, Winner 1% [P-judge files].
- **Change (preferred):** turn the bear into "At Risk realized plus a mild 2027 SMB recession":
  - Revenue: FY26 $347.5M, FY27 +3%, FY28 +1%, FY29 +3%, FY30 +4%, giving **$387M in 2030**.
  - Adj. EBITDA margin: 27.7%, 23.5%, 21.5%, 21%, 21%.
  - Gross margin: 80.3% falling to 77%.
  - Keep the 4x multiple and 30% probability.
- **Alternative:** keep the current bear as a "severe/Criteo" tail at 10% probability and **2.5x** (Criteo trades at about 1.5x [O]), and add the milder bear at 20%.
  - Both versions give nearly the same weighted value: $13.4 / $15.1 / $14.6 for the four-scenario version.
- **No scenario has a sharp 2020-style trough.** J puts a 2027 SMB shock at −21% to −2% [J]. Add it as a sensitivity: for example FY27 −8%, then FY28 +12%.

### 2. The base case is too optimistic for 2028–30 on growth and margin (high priority)

- **Revenue:** base 2030 revenue is $620M, 44% of the way from E's share-shift scenario B ($553M, corrected) toward the threat-contained path A ($705M).
  - E's modal scenario is B (45% probability), with growth of 8–17% and margins plateauing at 28–32% [E].
  - H's base already implies 2–6% lower revenue by 2030 [H]. The model has no explicit take-rate drag; mid-market revenue per customer rises 3% a year.
- **Margin:** cash S&M falls from 27.5% to 23.5% (GAAP 25.8%) by 2030. That is below the floor of management's 25–30% long-term range.
  - G says S&M stays around 30–35% [G]. M says S&M stays around 33–35% near term [M]. F says the acquisition-cost offset from AI agents is unproven [F].
- **Change:**
  - Revenue: FY27 $417M (+18.3%, equal to consensus [K]), FY28 +14.5%, FY29 +12%, FY30 +10%, giving **$588M in 2030** (about E's weighted $592M).
  - `sm_cash` = [0.275, 0.270, 0.265, 0.260, 0.255].
  - `td_cash` = [0.180, 0.180, 0.177, 0.174, 0.171]. N says T&D leverages to 15–18% only if growth stays near 20% [N].
  - Adj. EBITDA margin: 28.2%, 29.0%, 30.0%, 31.0%, **31.5%** (instead of 33.5%), giving 2030 EBITDA of $185M rather than $208M.
  - `qf_ai` (QuickFrame AI revenue) = [0, 0.5, 1, 2, 3]. N says no standalone QuickFrame AI revenue in the base case [N]; the model has $7M by 2030.
- **What does not change:** FY27–28 growth was already consistent with M's "mid-to-high teens" and B's "high-teens to low-20s" [M, B]. The overstatement is in 2029–30 and in the margin.

### 3. Cash taxes are too low for FY26–28 (high priority, new finding)

- **What the model has:** `cash_tax_rate` = [5%, 12%, 20%, 24%, 25%]. That shelters about $35M of cash tax below book over 2026–30 in the base case.
- **What the attributes support:** federal NOLs of $33.9M are worth about $7.1M, and R&D credits $3.7M [A; 10-K FY25].
- **The 1H26 current tax provision was already 18.2% of pre-tax income** [reported; Q2'26 10-Q, A]:
  - Provision $5.29M, less $1.50M deferred, leaves $3.79M current, on pre-tax income of $20.78M.
  - Cash paid was only $0.71M because payment lagged: income taxes payable rose from $0.10M to $2.77M.
  - FY26 taxable income of roughly $60–70M likely uses up the federal NOLs in 2026.
  - This contradicts A's "5–15% through about 2027" [A; estimate].
- **Change:** `cash_tax_rate` = **[0.07, 0.22, 0.25, 0.26, 0.26]**.
  - Base FY27 FCF falls from $88.8M to about $78.7M; FCF per share falls from $1.19 to about $1.05.
  - DCF falls by about $0.45 per share.

### 4. The bull case is too generous (medium-high priority)

- **FY27 revenue:** the bull's $445.6M (+25%) is above the top of the consensus range ($427.0M) [K]. The judges' upgrade trigger is FY27 ≥ $430M [P-financial]. M's evidence of share pressure from Vibe (Northbeam H1'26: Vibe +1,900%, MNTN +29%; verified) argues against more than 22% growth [M].
  - **Change:** FY27 $436M (+22.5%), then +23%, +22%, +20%, giving **$785M in 2030** at a 38.5% margin.
- **Multiple:** 11x matches AppLovin (about 11.5x NTM at +53% growth and an 84% margin) [O].
  - Takeout precedents are lower: DoubleVerify 8.1x, IAS about 9x EBITDA [O].
  - 11x on bull FY28 EBITDA is about 3.8x revenue, against about 2.8–3.3x for revenue-multiple precedents [O].
  - **Change: 9.5x.**
- **Dilution is understated.**
  - At the bull's own prices (buybacks at $25–30; implied values of $32.65 at end-2027 and $64.58 at end-2030), the 7.27M performance options start vesting. They have a $3.79 strike and hurdles of $25.40 and up [A, L].
  - The roughly 9.9M Class A options at about $11.55 average strike also become fully in the money.
  - Potential dilution by 2030 is about 24M shares against the model's 15M (7.0M gross issuance plus 8.0M treasury add-on). Bull gross issuance (1.4M a year) is also lower than base (1.6M), which runs the wrong way.
  - **Change:** `gross_issuance_m` = 2.0; `dilution_addon_m` = [4.8, 6.5, 8.5–9, 10.5–12, 12–15].
  - Effect on bull values: end-2027 falls from $32.65 to about $30.8; end-2030 from $64.58 to about $57.0.
- **The weighted value leans heavily on the bull:** in v1, 42% of the weighted 2030-exit value comes from the bull's 20% weight.

### 5. DCF mechanics (medium-high priority)

- **(a) Terminal cliff.** The scenario DCF drops from 2030 growth (12.4% base, 22.1% bull) straight to 3% forever, while `generic_value` fades growth over 2031–35.
  - The generic engine values the base path (15.4% CAGR, 33.5% margin) at $19.51; the scenario DCF gives $16.15.
  - **Fix:** use the same 5-year fade in `dcf()`. On v1 assumptions the base goes from $16.15 to about $17.9 and the bull from $25.09 to $31.6.
- **(b) Share count and buyback double-count.** The denominator is the FY26 average diluted count (78.0M), which already reflects the $30M 2026 buyback, while cash is the pre-buyback June balance ($237.3M).
  - **Fix:** use 74.80M basic + 4.72M dilutive (Q2'26) ≈ 79.5M, plus about 1–2M for excluded shares (item 6), so **80.5–81.5M**. This is about −3% per share.
- **(c) 2H26 cash flow.** The DCF credits only 0.21 × annual FY26 FCF-after-SBC plus $1M for Q3, about $11M in total.
  - Q4 was 60% of FY25 FCF [A]. The base implies about $34M of 2H26 FCF after SBC.
  - **Fix:** credit 2H26 directly as FY26 FCF − $27.0M (1H26 actual), less 2H SBC. This adds about $0.3 per share.
  - The same issue exists in `generic_value`, which credits $12M.
- **(d) Multiple valuation share basis.** `value_on_multiple` divides by FY28 average diluted shares (net of 2028 buybacks) but adds end-2027 cash. This overstates value by 1–2.5%. **Fix:** use end-2027 diluted shares.

### 6. Dilution handling by scenario (medium priority)

- **Excluded shares** [A]:
  - About 1.97M note-restricted shares remain (2.52M at June 30, less 554,610 released in July).
  - 1.57M Maximum Effort earnout shares are contingent through March 31, 2027.
  - **Change:** add about **+1.5–2.0M** (probability-weighted) to diluted shares in every scenario. That is about −2–2.5% per share.
- **Bear case:** SBC stays at 8–9% of revenue ($27–35M) while the share price is $5–8, yet gross issuance is only 2.0M a year.
  - Expressed as RSU-equivalents, that SBC implies about 3.5–5M shares a year. The 5% + 1% evergreen caps this at about 4.4M a year [L].
  - **Change:** bear `gross_issuance_m` = 3.5–4.4. End-2027 value falls from $7.69 to $7.05–7.28.
- **Base case:** the treasury add-on is held at a flat 4.0M while the price rises from $12 to $18.
  - **Change:** `dilution_addon_m` = [4.7, 4.8, 5.2, 5.6, 6.0] and `gross_issuance_m` = 2.1 (SBC $28–37M ÷ $12–18 per share).
- **Buyback:** the $100M is assumed fully executed by YE27 ($30M + $70M), but no execution is disclosed yet [L, K]. The 50%-of-FCF buybacks in 2028–30 have no authorization behind them.
  - Label both [estimate]. Show a no-buyback case until the Q3 10-Q (around Nov 9–10).

### 7. FY26 calibration against guidance and track record (medium priority)

- **Bear FY26** ($344.2M revenue, $92.9M adj. EBITDA) is **below the low end of guidance on both** ($347M and $96M), with Q3 already closed.
  - Revenue has landed 0.0% to +1.9% above the guidance midpoint each quarter (+0.4% average excluding the breakage) [B, corrected].
  - Adj. EBITDA beat the midpoint every quarter: +14%, +10%, +21%, +4.9% [B].
  - **Change:** $347.5M / $96.3M.
- **Base FY26** ($350.2M / $98.0M) sits below the midpoint and below consensus of $352.3M [K]. It implies Q4 of about $106M (+22%) against $108.4M consensus.
  - Defensible as skeptical (B allows $345–354M), but the track record argues for **$352–353M / $99–100M**.
- **FY26 FCF conversion:**
  - The base implies 2H26 FCF of $48.3M against $32.6M in 2H25. The 2H26 ratio of operating cash flow to (adj. EBITDA + interest) is 87%.
  - History is 79–81%: FY25 79.0%, LTM 81.2%, 1H26 81.4% [estimate from reported, A].
  - **Change:** `wc_pct_of_delta_rev` (working-capital drag per dollar of revenue growth) from 0.18 to **0.22**. Together with item 3, FY26 FCF comes to about $72M, inside K's $69–79M [K].

### 8. Probabilities (medium priority)

- The panel average implies roughly Victim 13% and Beneficiary+ 10%; the model uses Bear 30% and Bull 20%.
- With the milder bear from item 1, **Bear 30 / Base 55 / Bull 15** is defensible. It gives weighted 2030 revenue of $557M.
  - That sits in the middle of a stacked research range of about $530–570M: path A $705M × E −16%, plus the non-overlapping parts of F −9% and H −5.5%, plus J's AI drag [estimate].
- Keeping 30/50/20 with the recalibrated scenarios gives $13.5 / $15.2 / $14.7, so the result is not sensitive to this choice.

### 9. Multiples and discount rate (medium priority)

- **Base 7x:** O's central range is 5–8x [O], and the modal judge verdict is "At Risk". **Recommend 6.5x**, with peer median 7.75x and no re-rating (5.0x) as sensitivities.
  - Recalibrated base end-2027 present value: 5.0x $11.53; 6.0x $13.22; 6.5x $14.06; 7.0x $14.91; 7.75x $16.17.
- **Bear 4x:** fine only with the softened bear. A revenue-declining bear needs about 2.5x.
- **Bull:** 9.5x (item 4).
- **11% cost of equity:** reasonable (K uses 10–12%) [K]. Show 10% and 12%: recalibrated base DCF is $16.93 at 10% and $13.74 at 12%.
- **Method priority:** make the end-2027 multiple and the DCF primary, and the 2030 exit secondary. The 2030 exit compounds forecast error and lets a $423–549M cash pile carry the bull.

### 10. Reverse DCF (medium-low priority)

- **Inconsistent rows:** the 33.5%, 35% and 40% margin rows pair shrinking revenue (−2.7% to −7.4% CAGR) with rising margins. Show only consistent growth/margin pairs.
  - The headline is robust: 30% margin implies about 0.6% CAGR at 11%; −2.1% at 10%; +3.2% at 12%; −2.1% at the $9.40 prior close; +1.4% on 81.5M shares.
- **Add a scenario-weight framing:** at $10.25 the market prices about **53–54% weight on the recalibrated bear** against the base, on either the end-2027 multiple or the DCF. That is roughly twice the panel's bear weight.
- This agrees with K's corrected implied perpetual FCF growth: −0.4% to −2.2% before SBC, +2.8% to +4.7% after SBC [K].

### 11. Customer-segment split (low-medium priority; the mechanics are sound)

- **The constraint is respected:** with 3,632 TTM customers and at least about 1,000 mid and upper customers, a 13–15% small-business share forces small net revenue per TTM customer to about $14–16K. So treating the CEO's "~$15K" as net works [B, C]; if it were gross, the arithmetic fails.
- **Upper segment:** 70 customers × $323K = $22.6M, about 8%, matches the roughly 9% non-SMB remainder in Q1'25 (12% small / 79% mid) [A, C].
- **But:**
  - **(a) Small share is too low.** FY25 is set at 13.0%, against 12% (Q1'25) and about 15% (Q3'25) disclosed. FY26 at 14.1% barely moves despite the Express launch. Use about **14% FY25 and 16–17% FY26**.
  - **(b) Small revenue per customer recovers too early.** Base small revenue per customer of 0% / +2% / +2% in 2028–30 contradicts C's view that each AI-sourced customer wave is structurally low-spend. Use −5% / −4% / −3% / −1% / 0%.
  - **(c) Labels conflate size and tier.** Label "upper" as non-SMB/enterprise, not "Premium" (a product tier). The top-10 customers (about 17%, roughly $5M each) sit mostly in "mid" by firm size, so mid's $200K is a skewed mean.
  - **(d) TTM customer growth runs ahead of quarterly-active growth.** FY27 has TTM customers +25% with revenue per customer −5%. Quarterly-active customers grew +24% and are still decelerating [C], so about +20–22% customers with about −3% revenue per customer gives the same revenue on a more honest split.
- The bear should load the damage on small businesses and Express, where E says platform defaults are strongest. The current bear mostly does this already.

### 12. Presentation and consistency fixes (low priority)

- **`cash_cogs_addback` = 2.5% is inconsistent with the model's own D&A.**
  - Amortization of capitalized software was 3.4% of 1H26 revenue ($6.62M amortization less $1.32M acquired intangibles) and 3.9% in Q2 [reported].
  - Actual cash gross margin is about 84.3% against the model's 83.0%. The displayed GAAP gross margin of 79% in 2030 is inconsistent with the model's own D&A, which implies about 77.8%.
  - G&A excluding SBC is understated: 9.5% in the model against 12.2% in 1H26.
  - EBITDA totals are unaffected. Set the add-back from the software amortization schedule and raise `ga_cash` by about 1.3 points.
- **Adjusted EPS is not comparable to consensus.** The model's $0.90 / $1.14 (FY26/27) is not comparable with the "normalized" consensus of $1.05 / $1.31, which appears to add back all amortization [K, inferred]. Doing the same gives about $1.00 / $1.27. Reconcile explicitly.
- **Add a normalized FY25/TTM GAAP EPS row,** excluding the $9.6M valuation-allowance release and the $23.0M IPO charges [A, K]. Also add a consensus and long-term-target comparison table: $352.3M / $417.3M revenue; $115–130M FY27 EBITDA (backed out); 35–40% long-term EBITDA margin [K].

---

## What is fine (keep)

- FY27 base revenue $414M and EBITDA $120M against consensus of $417.3M and the backed-out $115–130M range [K].
- FY26 SBC of $26.6M is inside L's $25–28M [L].
- Book tax rate of 26% with no further valuation-allowance release ($0.7M remains) [A].
- D&A of $14.8M is close to the 1H26 run-rate (about $14.5M).
- Interest income yield of about 3.5% matches the Q2'26 $2.05M [reported].
- Capitalized software at 4.3% of revenue (1H26 actual 4.5%).
- Gross margin paths sit within the 75–80% long-term target.
- T&D at 19.5–19.7% GAAP in FY26–27 matches N.
- Base net adds of about 300 a quarter match the recent 242–351 [N].
- Treating SBC as cash in the DCF is conservative and consistent with K.
- The 11% cost of equity.
- Buybacks are executed below the scenario's own value, so they are accretive rather than value-destroying.
- The directional reverse-DCF conclusion that the price implies roughly no growth.

## Recalibrated scenarios (scratch run; all [estimate])

| | Bear (30%) | Base (55%) | Bull (15%) | Weighted |
|---|---|---|---|---|
| FY26 revenue / adj. EBITDA ($M) | 347.5 / 96.3 | 352.5 / 99.4 | 356.0 / 101.5 | |
| FY27 revenue ($M) | 358.0 | 417.0 | 436.0 | |
| 2030 revenue / adj. EBITDA ($M) (margin) | 387 / 81 (21%) | 588 / 185 (31.5%) | 785 / 302 (38.5%) | 557 / 172 |
| 2030 GAAP EPS / adj. EPS / FCF per share | $0.40 / $0.81 / $0.87 | $1.40 / $1.81 / $1.71 | $2.27 / $2.69 / $2.34 | |
| Multiple | 4.0x | 6.5x | 9.5x | |
| End-2027 multiple, present value | $6.87 | $14.06 | $22.13 | **$13.11** (v1: $15.83) |
| 2030 exit, present value | $6.15 | $15.04 | $29.24 | **$14.50** (v1: $19.62) |
| DCF (fade, 80.5M shares, 2H26 FCF fixed) | $6.08 | $15.13 | $26.29 | **$14.09** (v1: $14.58) |

These runs include the item 2 operating-cost and QuickFrame AI paths (`sm_cash`, `td_cash`, `qf_ai`), the item 3 tax rates, working-capital 0.22, item 4 bull issuance 2.0 with add-on rising to 12, and bear `gross_issuance_m` = 3.5. The item 6 excluded shares enter only the DCF, through the 80.5M denominator. The item 11 small-share and spend-per-customer changes are not applied, because the runs targeted revenue totals directly.