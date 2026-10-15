# Verification: TSMC Q3 2026 readout

*Verified 06:54–07:03 UTC Thu Oct 15, 2026 (2:54–3:03 am ET). Target: /tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/analysis/tsmc_q3_readout.md (written 06:52 UTC). Nothing below is filled in from memory. IBKR was used read-only (snapshots and history only); no orders, alerts or watchlists were created. Alpha Vantage was not used.*

## 0. Verdict

- **Every hard Q3 number is CONFIRMED.** I checked each one against my own fetch of TSMC's documents:
  - the 3Q26 Management Report, whose SHA-256 `27b5b92d…` matches the readout's copy byte for byte;
  - the **with-guidance** 3Q26 Earnings Release and Presentation, now posted on TSMC IR.
- **The Q4 guide is now CONFIRMED from TSMC's own documents**, not only from UDN:
  - **Revenue:** US$52.3–54.3bn.
  - **Gross margin:** 65–67%.
  - **Operating margin:** 56.5–58.5%.
  - **FX assumption:** 31.8 NT$/US$.
  - **Corroboration:** Reuters and CNA match the release.
  - **Outdated caveat:** the readout says "not yet from a TSMC document". That is now out of date: the with-guidance release was on investor.tsmc.com by about 06:56 UTC.
- **The 6-K is still not on EDGAR.** At 07:00:55 UTC the latest 6-K was dated Oct 8.
- **The call items are CONFIRMED by at least two outlets each:**
  - full-year growth of about 44%;
  - capex held at US$60–64bn;
  - capex for 2026–28 "significantly higher";
  - "prudent" on 2027.
- **The numbers need no material correction.** There are 6 framing or omission fixes (§4). The biggest are:
  - **NT$ revenue is not a "beat".** It was already known from the monthly sales reports.
  - **Gross margin was in line with consensus.** At 66.4% it matches the ~66.5% consensus; it is not "below the sell side".
  - **A positive early-2027 remark was left out.** Management said Q1 2027 demand for advanced nodes will "strongly support" the business.
  - **The rules table drops one criterion.** It omits the pre-registered "hedged 2027 AI commentary" trigger.
- **The implications follow the pre-registered rules and mostly do not overclaim.**
  - The readout correctly holds semis at 25/37/38 and NVDA at 35/45/20 until the US closes on Oct 15 and Oct 16.
  - **Fix needed:** the bottom line says SOXX is "below the semis verdict's line that invalidates the shallow path". That line is a **closing** condition, so an overnight print cannot trigger it.
  - **Premature:** "the only route left is a faded beat" should wait for the full Q&A transcript.
- **The tape is unchanged since the readout** (§5).
  - At about 07:01 UTC: TSM 420.85 (−2.13%), SOXX 509.49 (−1.91%), NVDA 217.86 (−1.55%), QQQ 719.55 (−1.29%).
  - All of these are overnight prints. None is a close, so no tape rule has resolved.

## 1. Primary documents I fetched myself

| Time (UTC) | Document | Result |
|---|---|---|
| 06:55 | [3Q26 Management Report](https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-10/f53a64fd40fc0b453f94e077e5aba8cad506f27b/3Q26%20ManagementReport.pdf) (fetched with WebFetch; curl gets a Cloudflare 403) | 468,113 bytes, SHA-256 `27b5b92d1d2c5942…886b411d2`, **identical** to the readout's copy |
| 06:56 | [TSMC IR Q3 page](https://investor.tsmc.com/english/quarterly-results/2026/q3) | Now lists the full **with-guidance** set (FS.pdf, Presentation, Management Report, Earnings Release) and a Guidance table with a 4Q26 column: 52.3–54.3 / 31.8 / 65.0–67.0% / 56.5–58.5% |
| 06:56 | [3Q26 Earnings Release, with guidance](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/526b65af7305df2dde6b9ece6812b1fdf1e49f9b/3Q26%20EarningsRelease.pdf) | SHA-256 `c56119b2…a29734a`. Contains the 4Q26 outlook bullets (quoted in §3) |
| 06:56 | [3Q26 Presentation, with guidance](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/e630db74ca50871f7598b011eafb5c036e7dd831/3Q26%20Presentation%20%28E%29.pdf) | SHA-256 `ba70fc4a…cdb`. Slide 8 is "4Q26 Guidance" with the same figures. Slide 3 shows the Q3 guide used an FX assumption of 32.0 |
| 06:55:18 and 07:00:55 | SEC EDGAR 6-K atom feed, CIK 1046179 | **No Oct 15 6-K yet.** Latest is 0001046179-26-000680, dated 2026-10-08 |
| 07:00:19 | [TWSE MIS](https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_2330.tw&json=1&delay=0) | 2330: last 2,440, prior 2,490 (−2.01%), at 13:30. TAIEX: 46,969.87, prior 48,625.83 (−3.41%) |

Note: the IR page renders links with a `www.tsmc.com` prefix, and those return 404. The working host is `investor.tsmc.com`.

## 2. Q3 2026 actuals

| Item | Readout | Primary source value | Status |
|---|---|---|---|
| Revenue, US$ | 46.72bn, +16.2% q/q, +41.2% y/y | 46.72 / +16.2% / +41.2% (Management Report, Earnings Release) | **CONFIRMED** |
| Versus the US$44.6–45.8bn guide | 2.0% above the top | 46.72 / 45.8 = +2.01%. Average FX was 31.98 against the 32.0 assumption, so FX did not help | **CONFIRMED** |
| Revenue, NT$ | 1,494.24bn, +17.6% q/q, +50.9% y/y | 1,494.24 / +17.6% / +50.9% | **CONFIRMED** (but see §4, item 1: not a "beat") |
| Gross margin | 66.4% (2Q 67.7%), decline from N2 dilution | 66.4% / 67.7%. The Management Report says: "primarily due to the margin dilution from the initial ramp-up of N2 technology" | **CONFIRMED** |
| Operating margin | 58.7%, above the 56–58% guide | 58.7%. The presentation shows the guide as 56.0–58.0% | **CONFIRMED** |
| Net income | NT$763.06bn, +68.7% y/y | 763.06 / +68.7% (+8.0% q/q). Net margin 51.1% | **CONFIRMED** |
| Versus LSEG SmartEstimate | 746.3bn, +2.2% | Reuters: "easily beat a T$746.3 billion LSEG SmartEstimate compiled from 16 analysts". 763.06 / 746.3 = +2.25% | **CONFIRMED** |
| "Sixth straight record" | Yes | Reuters (via KSL): "a sixth consecutive quarter of record earnings" | **CONFIRMED** |
| EPS | NT$29.43; US$4.60 per ADR | 29.43 / 4.60. Diluted shares 25,932mn | **CONFIRMED** |
| Implied consensus EPS | about 28.78 | 746.3 / 25.932 = 28.78 | **CONFIRMED** (arithmetic) |
| Node mix | N2 8% (2Q 3%), N3 33%, N5 28%, N7 10%; advanced 79% | Identical | **CONFIRMED** |
| HPC | 68%, +22% q/q | 68%, +22% q/q | **CONFIRMED** |
| Geography | North America 79%, China 5% | 79% / 5% | **CONFIRMED** |
| Days of inventory | 87 → 82 | 87 → 82. TSMC says this is "primarily due to the increase in wafer shipments". Inventory in NT$ rose 10.9% q/q (385.53 → 427.75bn) | **CONFIRMED** (see §4, item 6) |
| Capex, Q3 / year to date | US$13.84bn / US$40.64bn | 13.84 / 40.64 | **CONFIRMED** |
| Implied Q4 capex | US$19.4–23.4bn, +40–69% q/q | 19.36–23.36, +39.9% to +68.8% | **CONFIRMED** (arithmetic) |
| Dividend | No Q3 dividend yet; last was NT$7.00 for 2Q (ex-dividend Dec 10) | The Management Report's recap lists only the 2Q NT$7.00 (ex-dividend Dec 10, record Dec 16, paid Jan 7, 2027) | **CONFIRMED** |
| CFO's "sustainable and steadily increasing" dividend | Yes | [UDN 9816694](https://money.udn.com/money/story/5612/9816694): 「維持永續且穩健增加每股現金股利」 | **CONFIRMED** (one outlet) |
| Consensus references | LSEG 740.8; FactSet ~731.8; NT$1.47tn revenue; Street GM ~66.5%; Morgan Stanley 67.5%; HSBC 66.9% | GM figures (66.5% consensus, MS 67.5%, HSBC 66.9%, plus BofA ~67%) appear in secondary previews ([Hudson Labs](https://www.hudson-labs.com/research/tsmc-q3-2026-earnings-preview-tsm-revenue-and-margins), [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262213491-tsmc-q3-earnings-preview-profits-hit-record-high-sixth-straight-quarter-tradingkey)). I did not re-check LSEG 740.8 or FactSet 731.8 | **PARTLY CONFIRMED**. LSEG 740.8 and FactSet 731.8 are **UNVERIFIABLE** here |

## 3. Q4 guide and call commentary

| Item | Readout | Source | Status |
|---|---|---|---|
| Q4 revenue | US$52.3–54.3bn | Earnings Release: "Revenue is expected to be between US$52.3 billion and US$54.3 billion". Presentation slide 8; IR Guidance table; [Reuters/KSL](https://www.ksl.com/article/51636529/tsmc-expected-to-report-sixth-straight-quarter-of-record-profit-thanks-to-ai-boom); [CNA](https://www.cna.com.tw/news/afe/202610150159.aspx) | **CONFIRMED (official)** |
| Q4 change q/q | +11.9% to +16.2%, midpoint +14.1% | 52.3 / 46.72 = +11.94%; 54.3 / 46.72 = +16.22%; 53.3 / 46.72 = +14.08%. CNA and [LTN](https://ec.ltn.com.tw/article/breakingnews/5607191) both say "季增14%" | **CONFIRMED** |
| Q4 change y/y | +58% | Reuters gives the 4Q25 base as US$33.73bn, so the midpoint is +58.0% (top +61%). CNA: "年增58%" | **CONFIRMED** |
| Q4 gross margin | 65–67% | Earnings Release: "between 65% and 67%" | **CONFIRMED (official)** |
| Q4 operating margin | 56.5–58.5% | Earnings Release: "between 56.5% and 58.5%". Note: the 57.5% midpoint is 1.2pp below Q3's actual 58.7% | **CONFIRMED (official)** |
| FX assumption | 31.8 NT$/US$ | Earnings Release: "1 US dollar to 31.8 NT dollars" | **CONFIRMED (official)** |
| Spot about 32.3 | — | Reuters: "$1 = 32.3450 Taiwan dollars" | **CONFIRMED** |
| GM midpoint 66%, −0.4pp q/q, from N2 and overseas-fab dilution | — | The −0.4pp is in [UDN 9816708](https://money.udn.com/money/story/5612/9816708) and LTN. The cause (「2奈米…稀釋」, 「海外晶圓廠的稀釋效應」) is in UDN only | **CONFIRMED** (cause from one outlet) |
| Full-year 2026 growth | About 44% in US$, up from "slightly above 40%" | CNA headline: 「再調升全年美元營收成長44%」; LTN; [UDN 9816750](https://money.udn.com/money/story/5612/9816750); [NextApple](https://news.nextapple.com/finance/20261015/692132EAD58B39ABC22A5A0765E1CF16). Call statement only; not in the written release | **CONFIRMED** |
| Versus the street | Street range 40–46% | Morgan Stanley's Charlie Chan expected "low-to-mid 40%" (secondary). I found no source for 40–46% | **PARTLY CONFIRMED** |
| Street Q4 expectation | +10–15% q/q | BofA's Haas Liu, 10–15% sequential (via TipRanks, secondary). Morgan Stanley's implied range was US$51.4–53.7bn | **CONFIRMED** (one broker, secondary) |
| 2026 capex | US$60–64bn held | Reuters: "maintained its capital spending expectation for 2026 at $60 billion to $64 billion"; UDN 9816694; NextApple | **CONFIRMED** |
| 2026–28 capex "significantly higher"; tight tool supply | — | UDN 9816694: 「2026年至2028年的資本支出金額將比過去3年顯著更高」 and 「儘管機台供應吃緊」. NextApple: 「未來3年投資規模將明顯高於過去3年」 | **CONFIRMED** |
| AI is "very strong" and "multi-year structural" | — | UDN 9816750: 「先進製程需求仍極為強勁…AI多年結構性成長趨勢維持高度信心」 | **CONFIRMED** |
| "Recent developments very positive" | — | NextApple: 「近期發展對AI成長及需求展望相當正面」 | **CONFIRMED** |
| Agentic AI, CPUs and networking; teams sent to check US data-center power; "CSPs ready" | — | UDN 9816750, verbatim match | **CONFIRMED** (one outlet) |
| "Won't leave food on the table" | Shown as a quote | NextApple: 「我們不打算把任何商機拱手讓給別人」. The meaning matches, but the English wording is a back-translation; I found no English transcript yet | **Substance CONFIRMED; exact English wording UNVERIFIABLE** |
| CoWoS / "demand exceeds supply" | None seen | None found in CNA, LTN, UDN, NextApple or Reuters for Oct 15. Reuters attributes "CoWoS remains strong" to *analysts*, not management. PTS and BigGo hits were from 2024 and April 2026 | **CONFIRMED absent** (as of about 07:00 UTC) |
| "Prudent in planning 2027" | — | UDN 9816750: 「對2027年營運規劃保持審慎」 (citing component prices, macro, consumer and price-sensitive markets). NextApple: 「對2027年業務規劃維持謹慎態度」 | **CONFIRMED** |
| **Q1 2027 demand** | **Omitted** | NextApple: 「展望2027年第一季，包括2奈米快速放量在內的先進製程需求仍將強力支撐業務表現」 | **MISSING from the readout.** This is positive early-2027 commentary (see §4, item 4) |
| N2 capacity more than doubles in 2027 | — | NextApple: 「N2家族2027年全年產能將增加逾1倍」 | **CONFIRMED** (one outlet read directly) |
| A14 in 2028 | — | NextApple: 「於2028年量產」 | **CONFIRMED** (one outlet) |
| "Three new 3nm fabs, including another in Tainan (1H28)" | — | [UDN 9816715](https://money.udn.com/money/story/5612/9816715): 「決定在台南再增建一座3奈米廠…2028年上半年」. The other sites (the existing new Tainan fab for 1H27, Arizona and Kumamoto 2) were **already announced on the April call** | **CONFIRMED, with a nuance:** the only *new* fab announced today is the extra Tainan one (1H28) |
| Arizona fab 2 in 3Q27, slightly early | — | NextApple: 「量產時程提前至2027年第三季」. The April call said 2H27 | **CONFIRMED** |
| Japan fab 2 on 3nm in 2028 | — | NextApple: 「預計2028年量產」 | **CONFIRMED** (one outlet) |
| Texas fab under evaluation | — | NextApple, related story: 「派遣團隊赴德州評估設廠機會」 | **CONFIRMED** (one outlet) |
| Talks with a customer that plans its own fab | — | Only a NextApple related headline (「客戶合作晶圓廠須台積電營運」); body not read | **UNVERIFIABLE** |
| No digestion, China, export-control or tariff remarks | — | None found in the coverage I read. The Q&A was still running at 06:52, so this is provisional until there is a transcript | **PROVISIONALLY CONFIRMED** |

## 4. Corrections and framing fixes (none changes the direction of the readout)

1. **NT$ revenue "Beat" (§2 table) is misleading.**
   - Q3 NT$ revenue of 1,494.2bn was already public from the monthly 6-Ks before results day.
   - Comparing it with LSEG's ~NT$1.47tn measures stale estimates, not a surprise on the day.
   - **Fix:** call it "pre-reported via monthly sales". The real surprise variables are margins, net income and the guide.
2. **Gross margin was in line, not "a touch light".**
   - The bottom line says the margin was "slightly below the 66.9–67.5% the sell side expected". That picks the two highest broker numbers (HSBC and MS).
   - The consensus quoted in the readout's own §2 is ~66.5%. The actual 66.4% is in line with it (−0.1pp) and 0.4pp above the guide midpoint.
   - **Fix:** "in line with ~66.5% consensus; below the MS/HSBC/BofA 66.9–67.5% bulls."
3. **The net-income beat range is incomplete.**
   - Against the three figures it lists, the beat is +2.2% (LSEG SmartEstimate 746.3), +3.0% (LSEG 740.8) and +4.3% (FactSet 731.8).
   - The readout says "2.2–3.0%", which leaves FactSet out. Either drop FactSet or say 2.2–4.3%.
4. **The early-2027 commentary is less mixed than the readout says.**
   - **Omitted positive:** management said Q1 2027 advanced-node demand, including the fast N2 ramp, will "strongly support" the business (NextApple).
   - **The hedge is narrow:** the "prudent on 2027" remark is explicitly tied to consumer and price-sensitive end markets, component costs and macro, not to AI. AI was called "multi-year structural".
   - **Box status:** the "early 2027 growth commentary" box stays ◐ (no 2027 growth number), but it leans positive.
5. **The rules table omits a pre-registered trigger.**
   - Under "toward deeper or trend break", the pre-registered rules include **"hedged 2027 AI commentary"**. §5 of the readout leaves it out.
   - On the evidence above it **did not fire**, because the prudence is about non-AI end markets. It should still be listed and scored explicitly (✘, with that rationale) rather than omitted.
6. **The inventory point needs a caveat.** "Days of inventory fell, which argues against digestion" is fair, but the decline is driven by shipments. NT$ inventory rose 10.9% q/q, so the point is weaker than stated.

## 5. Tape: refreshed IBKR quotes (read-only, REALTIME, overnight session; none is a close)

| Instrument (conid) | Prior close | 06:54 UTC snapshot | **About 07:01 UTC snapshot** | Distance to rule levels from the latest print |
|---|---|---|---|---|
| TSM (6223250) | 430.00 | 421.37 (−2.01%) at 06:54:15 | **420.85 (−2.13%)** at 07:01:30; bid/ask 420.65 / 421.30 | Needs +2.17% to close green |
| SOXX (12658194) | 519.42 | 509.10 (−1.99%) at 06:54:06 | **509.49 (−1.91%)** at 07:01:33; bid/ask 509.10 / 509.44 | Green needs +1.95%. 512.6 is +0.61% away; 510 is +0.10%. Cushion over 497.40: 2.37% |
| NVDA (4815747) | 221.30 | 217.89 (−1.54%) at 06:54:02 | **217.86 (−1.55%)** at 07:01:05; bid/ask 217.78 / 217.95 | 0.53% above 216.7; 1.57% above 214.45 |
| QQQ (320227571) | 728.95 | 719.39 (−1.31%) at 06:54:20 | **719.55 (−1.29%)** at 06:59:59 | — |

- **The readout's 06:50 prints are consistent with mine:** TSM 420.50, SOXX 509.30, NVDA 218.02, QQQ 719.25.
- **The TSM peak of 427.00 at 06:15 is UNVERIFIABLE.** IBKR's history call returns bars only up to 00:00 UTC Oct 15, so I could not check it. The full reversal to about 420–421 *is* confirmed.
- **2330.TW and the TAIEX are CONFIRMED** from TWSE MIS: 2,440 (−2.01%); TAIEX 46,969.87 (−3.41%). [Focus Taiwan](https://focustaiwan.tw/business/202610150007) also gives 46,969.87 (−3.41%).
- **The backdrop is CONFIRMED:**
  - **US inflation:** [Focus Taiwan](https://focustaiwan.tw/business/202610150005) says September US CPI was 3.7% against 3.6% expected, with renewed worries about Fed tightening.
  - **Korea:** the KOSPI triggered a circuit breaker ([Reuters via Investing.com](https://www.investing.com/news/economy-news/south-koreas-kospi-triggers-circuit-breaker-in-techled-selloff-4950522), [Korea Herald](https://www.koreaherald.com/article/10903746)). Samsung fell about −10% and SK hynix about −11%.

## 6. Implications versus the pre-registered rules

| Readout claim | Check | Status |
|---|---|---|
| Q4 guide up q/q ✔; GM guide ≥ ~65% ✔; capex held ✔ | Official guide +14.1% q/q at the midpoint; GM 65–67% (the bottom of the range meets the bar); capex US$60–64bn held | **Correct** |
| AI/CoWoS "demand exceeds supply" ◐ | No explicit language found. Strictly, the box is **not** ticked; ◐ is generous. The bottom line does count it as not ticked | **Acceptable**; the bottom line is accurate |
| Early 2027 commentary ◐ | Correct that there is no number, but the readout omits the positive Q1'27 remark (§4, item 4) | **Correct with an omission** |
| No deeper or trend-break fundamental trigger fired | True for flat/down guide, GM < 63–64%, digestion and capex cut. The "hedged 2027 AI" trigger is not scored (§4, item 5); on the evidence it did not fire. Digestion is provisional until the transcript | **Correct, but incomplete** |
| Tape rule written as "SOXX green close (above 519.42)" | The rule's text is "a green SOXX close above ~512.6". Green requires a close above 519.42, so the readout's reading is the literal and stricter one. A close between 512.6 and 519.42 is red and **does not** pass the rule | **Correct.** Suggest stating the ambiguity explicitly |
| "SOXX 509.30 … below the semis verdict's line that invalidates the shallow path ('a TSMC beat that closes SOXX red below 510')" | The verdict line is quoted accurately (semis_verdict.md line 269), but it is a **closing** condition. An overnight print below 510 does not trigger it | **Overclaim in wording.** Reword to "trading below the 510 invalidation level, which applies only on a close" |
| Semis 25/37/38 and NVDA 35/45/20 held | These match FINAL_REPORT.md. Both halves of each rule (fundamentals and tape) are required, and the tape is unresolved | **Correct; not overclaimed** |
| "Flat-guide route closed; only route left to ~42% trend break is a faded beat" | The flat-guide route is closed by the official guide. "Only route left" is premature: digestion or hedged-AI language could still surface in the unreviewed Q&A | **Minor overclaim** |
| Scenario table: holds → 35/37/28; faded → 20/38/42 | Matches the semis verdict's "to about 35%" and "to about 42%" end-states. The NVDA rows are labelled interpolations, and the 41/43/16 cap is consistent with the NVDA verdict's 223.21 condition for >45% shallow | **Correct; disclosed as interpolation** |
| Row "SOXX red but ≥ 497.40, below 510 → 20/42/38" | Not pre-registered. The verdict calls a beat that closes SOXX red below 510 an *invalidation* of shallow, so 20% shallow is generous; something like 15–18% would follow the verdict's language more closely. This is a judgement call | **Flag (low severity)** |
| "The ADR's guide pop has already fully reversed" | TSM was 420.85 at 07:01, matching the 05:40 level | **Correct** (the size of the pop is unverifiable) |

## 7. Still open

- The 6-K on EDGAR. TSMC's IR release already serves as the primary source.
- An English call transcript, to check:
  - CoWoS remarks;
  - any digestion or hedged-AI language;
  - the exact English wording of the quotes the readout gives.
- The US session tests:
  - SOXX at 497.40 / 510 / 512.6 / 519.42;
  - NVDA at 216.7 / 214.45;
  - US PPI on Oct 15;
  - 2330.TW at the Oct 16 open (01:00 UTC);
  - options expiration on Oct 16.

## Sources

- **TSMC (primary):**
  - [Management Report](https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-10/f53a64fd40fc0b453f94e077e5aba8cad506f27b/3Q26%20ManagementReport.pdf)
  - [Earnings Release (with guidance)](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/526b65af7305df2dde6b9ece6812b1fdf1e49f9b/3Q26%20EarningsRelease.pdf)
  - [Presentation (with guidance)](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/e630db74ca50871f7598b011eafb5c036e7dd831/3Q26%20Presentation%20%28E%29.pdf)
  - [IR Q3 page](https://investor.tsmc.com/english/quarterly-results/2026/q3)
  - SEC EDGAR 6-K feed, CIK 1046179
  - TWSE MIS
- **Wires:**
  - Reuters, via [KSL](https://www.ksl.com/article/51636529/tsmc-expected-to-report-sixth-straight-quarter-of-record-profit-thanks-to-ai-boom) and [Investing.com](https://www.investing.com/news/stock-market-news/tsmc-q3-profit-jumps-69-to-record-beating-expectations-4950551)
  - [CNA](https://www.cna.com.tw/news/afe/202610150159.aspx)
  - [Focus Taiwan 0007](https://focustaiwan.tw/business/202610150007) and [Focus Taiwan 0005](https://focustaiwan.tw/business/202610150005)
- **Taiwanese press:**
  - [LTN](https://ec.ltn.com.tw/article/breakingnews/5607191)
  - UDN [9816694](https://money.udn.com/money/story/5612/9816694), [9816708](https://money.udn.com/money/story/5612/9816708), [9816715](https://money.udn.com/money/story/5612/9816715) and [9816750](https://money.udn.com/money/story/5612/9816750)
  - [NextApple](https://news.nextapple.com/finance/20261015/692132EAD58B39ABC22A5A0765E1CF16)
- **Previews (secondary):**
  - [Hudson Labs](https://www.hudson-labs.com/research/tsmc-q3-2026-earnings-preview-tsm-revenue-and-margins)
  - [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262213491-tsmc-q3-earnings-preview-profits-hit-record-high-sixth-straight-quarter-tradingkey)
- **Korea:**
  - [Reuters via Investing.com](https://www.investing.com/news/economy-news/south-koreas-kospi-triggers-circuit-breaker-in-techled-selloff-4950522)
  - [Korea Herald](https://www.koreaherald.com/article/10903746)
- **Local copies of my fetches:**
  - /tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/verify_dl/mine/mr.pdf
  - /tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/verify_dl/mine/er_wg.pdf
  - /tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/verify_dl/mine/pres_wg.pdf
  - each with a matching .txt extract
