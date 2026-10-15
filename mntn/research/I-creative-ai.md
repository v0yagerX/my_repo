# I. Creative AI: Threat 5 (creative commoditization) and Upside 1 (TV-ad production-cost collapse leading to market expansion)

**Company:** MNTN, Inc. (NYSE: MNTN; CIK 0001891027). **As of:** 2026-10-15.
**Labels:** [reported] = company/SEC/primary disclosure; [guidance] = company outlook; [third-party] = industry, press or vendor data; [estimate] = my own derivation (math shown); [consensus] = sell-side consensus.

---

## 0. Bottom line

1. **AI has already driven the cost of a usable 30-second CTV spot close to zero.** The compute cost of one 30s, 1080p take with audio is about **$2.40–$12** at Google's list prices [estimate; from $0.08–$0.40/s, Google Gemini API pricing page, accessed 2026-10-15]. A finished spot that takes 10–50 takes costs roughly **$24–$600** [estimate]. A third-party source puts traditional production at **$10k–$500k** [third-party, AdWorldNews, 2026-05-05, flagged as low-quality]. That is a 95–99.9% cost reduction [estimate]. The upside thesis (creative no longer blocks SMBs from TV) is real.
2. **MNTN is acting on this, but the benefit is not exclusive to MNTN.** QuickFrame AI (public beta 2025-10-29; GA as "3.0" on 2026-05-05) had **>73,000 signups in 1H26, ~37,000 of them in Q2** [reported, Q2'26 call, 2026-08-04]. Management calls it gross-margin-neutral [reported]. It runs on third-party models only: Veo, Gemini Omni Flash, Seedance, Kling, Sora (now retired), ElevenLabs and WellSaid. There is no proprietary video model. Google (Veo in Google Ads, 2026-03), Meta (9M+ small businesses using AI creative tools, Q2'26) and Amazon (free Video Generator) all bundle free AI video. Roku's CEO says "AI is opening the entire new market of SMBs" for Roku Ads Manager (Marketing Dive, 2026-02-13).
3. **QuickFrame AI works as a customer funnel and a feature, not a moat.** Management does **not disclose** how many QuickFrame AI users convert to paying Performance TV (PTV) customers. The arithmetic implies a low single-digit % conversion at most (see section 4).
4. **The market-expansion evidence is mixed.** Customer counts are growing fast: TTM active PTV customers were 4,225, up 40% y/y [reported]. But quarterly active PTV customers grew only **24%** in Q2'26 [reported, 10-Q]. Revenue per TTM customer fell from about **$101k (FY24) to $80k (FY25) to $74k (TTM 2Q26)** [estimate]. Management attributes the falling average spend to its SMB mix shift [reported, 10-Q]. AI creative is bringing in more but smaller advertisers.
5. **Creative commoditization does little direct financial damage.** The human QuickFrame marketplace is reported net and is not disclosed separately. The deferred-revenue balance, which is mostly customer creative credits, shrank from **$9.0M (Dec-24) to $5.5M (Dec-25) to $2.7M (Jun-26)** [reported]. The indirect risk is larger. MNTN's pitch that "we solve the TV-creative barrier" stops being unique once every self-serve CTV seller offers free AI creative.
6. **Net verdict for this topic: a slight AI winner** (about +1 on a −3 to +3 scale). AI expands the addressable SMB pool and MNTN is early and focused. MNTN does not own the advantage, the new customers are smaller, and conversion is unproven.

**Q3 2026 status:** MNTN will report Q3 2026 after the close on **2026-11-04** [reported; company announcement 2026-10-14, relayed by StockTitan: https://www.stocktitan.net/news/MNTN/mntn-to-announce-third-quarter-2026-financial-results-on-november-4-0pv9why9jhfk.html]. Nothing in this dossier reflects Q3 results. Q3 guidance is revenue $86–89M and adj. EBITDA $22–25M [guidance, Q2'26 8-K, 2026-08-04].

---

## 1. Gen-video landscape (October 2026)

### 1a. Model and tool pricing

| Model / tool | Status (Oct 2026) | Price | Source / label |
|---|---|---|---|
| **Google Veo 3.1 (Standard)** | GA via Gemini API / Vertex | **$0.40/s** at 720p or 1080p, **$0.60/s** at 4K, video with audio; no free tier | Google Gemini API pricing page, accessed 2026-10-15, https://ai.google.dev/gemini-api/docs/pricing [third-party: vendor list price] |
| **Veo 3.1 Fast** | GA | $0.10/s (720p), $0.12/s (1080p), $0.30/s (4K) | same [third-party] |
| **Veo 3.1 Lite** | GA | $0.05/s (720p), $0.08/s (1080p) | same [third-party] |
| **Gemini Omni Flash / Omni 1.1 Flash** | Model card first published May 2026, updated 2026-08-27. Text/image/audio/video in, video with audio out, conversational editing, SynthID watermark | ~$0.10/s of 720p ($17.50 per 1M video-output tokens at 5,792 tokens/s) | Google pricing page (above); DeepMind model card, https://deepmind.google/models/model-cards/gemini-omni-flash/ (2026-08-27) [third-party] |
| **OpenAI Sora 2 / Sora 2 Pro** | **Discontinued.** Sora app shutdown announced 2026-03-24. Videos API, sora-2 and sora-2-pro **removed from the API 2026-09-24** | n/a (previously $0.10/s for sora-2 at 720p, per third-party trackers) | OpenAI deprecations page, https://developers.openai.com/api/docs/deprecations; TechCrunch 2026-03-24, https://techcrunch.com/2026/03/24/openais-sora-was-the-creepiest-app-on-your-phone-now-its-shutting-down/ [third-party] |
| **Runway (Gen-4.5, Aleph 2.0)** | GA | Standard $15/mo (625 credits), Pro $35/mo (2,250), Max $95/mo (9,500). Gen-4.5 costs 12 credits/s and Aleph 2.0 costs 28 credits/s | runway.com/pricing, accessed 2026-10-15 [third-party]. Pro works out to 187.5s of Gen-4.5 a month, or **~$0.19/s** [estimate: 2,250/12 = 187.5s; $35/187.5] |
| **ByteDance Seedance 2.0** | Launched in China 2026-02-12. Disney sent a cease-and-desist and the MPA demanded it stop "massive scale" infringement. ByteDance pledged safeguards | Volcengine ~$0.14/s per third-party reports (unverified) | Variety, 2026-02-16, https://au.variety.com/2026/film/global/bytedance-safeguards-seedance-disney-legal-threat-ip-violations-33139/ [third-party] |
| **Creatify** (ad-focused aggregator) | GA | Standard $15/mo list (55 credits), Pro $55, Max $95, Business $195. Pro and above include Seedance 2.5, Veo 3.1 and Kling 3.0 Pro | creatify.ai/pricing, accessed 2026-10-15 [third-party] |
| **HeyGen** (avatars) | GA | Free (3 videos/mo, 1080p), Creator $29/mo, Pro $49/mo (4K), Business $149/mo + $20/seat | heygen.com/pricing, accessed 2026-10-15 [third-party] |
| **Synthesia** (avatars) | GA | Free, Starter $29/mo (~12 min/mo), Pro $89/mo (~60 min/mo); Full HD MP4 | synthesia.io/pricing, accessed 2026-10-15 [third-party; page internally inconsistent on annual pricing] |
| **Adobe Firefly Video / GenStudio for Performance Marketing** | GA. Firefly is positioned as "commercially safe" (trained on licensed data) and also offers partner models | Credit-based plans; exact prices conflict across third-party sources (not verified on Adobe's page) | Adobe GenStudio product page, https://business.adobe.com/products/genstudio-for-performance-marketing [third-party; pricing unverified] |
| **QuickFrame AI (MNTN)** | GA since 2026-05-05 | Free tier (50 one-time credits), Starter $39/mo, Pro $99/mo, Max $250/mo, with first-month discounts. Lists Seedance 2.5 and Gemini Omni Flash | quickframe.com, accessed 2026-10-15 [reported, company site]. See the pricing conflict in section 2 |
| Kling 3.0, Luma, Pika, Midjourney video, Arcads, Canva, CapCut | Active. Kling 3.0 is resold inside Creatify | **Not verified this session** | Data gap |

**Cost of one 30-second spot** [estimate]: one 30s take costs **$12.00** on Veo 3.1 Standard (30 × $0.40), **$3.60** on Veo 3.1 Fast at 1080p, **$2.40** on Veo 3.1 Lite at 1080p, and **~$3.00** on Omni Flash at 720p. Assuming 10–50 takes per finished spot (multi-shot stitching, retries, voice and music), compute runs **~$24–$600 per finished 30s spot**. Self-serve subscriptions cost **$29–$250/month** (HeyGen, Synthesia, Runway, Creatify, QuickFrame). The only cost benchmark found for traditional production is "**$10,000 to $500,000** depending on complexity" with 4–8 week timelines [third-party; AdWorldNews, 2026-05-05, https://www.adworldnews.com/news/ai-video-ads-small-business-tv-advertising-ctv-broadcast-quality, an aggregator-quality source, flagged]. MNTN itself says only that a commercial "used to require weeks, large teams, and big budgets" (CEO blog, https://mountain.com/blog/introducing-quickframe-ai/, Oct 2025), with no dollar figure. **Implied reduction: about 95% to over 99.9%** [estimate].

**What this means:** the underlying video models are commoditizing quickly. Google's own Lite tier is 5x cheaper than Standard. Model churn is also severe. Sora went from launch in September 2025 to removal from the API in September 2026, a period in which MNTN had already integrated it (Q1'26 call). A wrapper like QuickFrame AI benefits from falling input costs but can rarely make a model its moat.

### 1b. Output quality against CTV/broadcast requirements

- **Length and format.** CTV slots are typically 15 or 30 seconds at 1080p or higher with mixed audio. Roku Ads Manager accepts 6–92s .mov/.mp4 files up to 1 GB and applies **2–3 days of manual content review** [third-party, Roku, 2026-02-25, https://advertising.roku.com/learn/resources/how-much-does-it-cost-to-advertise-on-roku]. Single-model clips remain short: Veo in Google Ads produces clips of **up to 10s** from still images (Google, 2026-03, https://business.google.com/en-all/accelerate/announcements/veo-google-ads/). A 30s spot therefore needs multi-shot orchestration, voiceover and music. QuickFrame AI 3.0 is built around exactly that: storyboard editor, multi-shot scenes, multi-character dialogue, saved characters, products and locations, and 16:9/vertical/square output (MNTN PR, 2026-05-05, https://mountain.com/press/mntn-releases-quickframe-ai-3-0-with-a-major-feature-expansion-delivering-tv-ready-commercials-in-minutes/).
- **Publisher QA and clearance.** MNTN's software "automatically screen[s] creative for TV network formats and standards… guaranteeing the correct format, resolution, sound" so ads are not rejected, which it calls "one of the common barriers for smaller brands" [reported, 10-K FY25, filed 2026-02-19, https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm]. This spec compliance plus one-click publishing to PTV is real workflow value. It is not proprietary science.
- **Model limits.** Google's own model card says "maintaining consistency through edits, generating scenes with complex motion, and rendering accurate text remain challenges" (DeepMind, 2026-08-27). Accurate on-screen text (prices, phone numbers, legal supers) matters for direct-response TV.
- **Legal and brand safety.**
  - MNTN's filings warn that gen-AI output "could… be infringing" and that "the United States Copyright Office has previously denied copyright protection for content generated by AI." They also cite state AI laws in Utah, Texas and California [reported, 10-K FY25; 10-Q 2Q26, https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm].
  - QuickFrame AI 3.0 added **Seedance 2.0** [reported, Q1'26 8-K], the model the MPA called a vehicle for infringement "on a massive scale" (Variety, 2026-02-16). That is a tail brand-safety and IP-indemnity risk for MNTN's SMB customers.
  - Consumer reception: only **45%** of Gen Z/Millennial consumers feel positive about AI-generated ads, against **82%** of ad executives who think consumers do. **71%** of consumers believe they have seen an AI ad, up from 54% in 2024 [third-party, IAB "The AI Ad Gap Widens," 2026-01-15, https://www.iab.com/insights/the-ai-ad-gap-widens/].
  - **86%** of buyers use or plan to use gen-AI for video creative [third-party, IAB 2025 Digital Video report, as cited on the same IAB page].

### 1c. Ad platforms that bundle free AI video creation

| Platform | Free AI video for advertisers? | TV/CTV relevance | Source |
|---|---|---|---|
| **Google / YouTube** | **Yes.** Veo in Google Ads Asset Studio (launched 2026-03) turns up to 3 images into ≤10s videos for "all campaigns" and auto-generated Demand Gen; no separate fee per secondary sources | YouTube inventory includes TV screens, but Google's announcement does not mention CTV | Google, 2026-03, URL above [third-party] |
| **Meta** | **Yes.** **8M+** advertisers used at least one AI creative tool at Q1'26, up from 4M at end-2024. Video-generation tests showed a **+3% conversion** gain. **9M+** small businesses used AI creative tools at Q2'26. Advantage+ reached a **$75B** run rate | Not a CTV seller, but competes for the same SMB video budgets | PPC Land 2026-04-30, https://ppc.land/meta-q1-2026-56-3b-revenue-as-ai-tools-double-advertiser-adoption/ ; MediaPost 2026-07-31, https://www.mediapost.com/publications/article/416925/meta-boosts-advertising-in-q2-tries-to-reassure-i.html [third-party reporting of Meta calls] |
| **Amazon** | **Yes, for Sponsored Brands.** "A free tool for sellers and vendors," multi-scene product video in under 5 minutes. Separately, **Dynamic TV Creative** (May 2026) generates impression-time variants of one base asset for select Prime Video advertisers who sell on Amazon. Sponsored TV / Streaming TV is self-serve (reported as no minimum) | Prime Video is a direct premium-CTV channel | Amazon Ads, https://advertising.amazon.com/resources/whats-new/create-high-quality-ai-generated-videos-in-minutes [third-party]; MediaPost 2026-05-12, https://www.mediapost.com/publications/article/415018/amazon-ads-unveils-personalized-ai-driven-video-f.html [third-party; Sponsored TV minimum not verified on Amazon's own page] |
| **Roku** | **No native gen-AI commercial builder** as of 2026-02-25. Offers an AI upscaler for social video and a Spaceback partnership that converts social video into CTV ads; suggests starting at $500 | Direct SMB CTV competitor (Ads Manager) | Roku, 2026-02-25 (URL above) [third-party] |
| **MNTN** | **Yes.** QuickFrame AI: free first video, three free AI-generated TV ads for new PTV advertisers, export to Meta/TikTok/YouTube/Google | Native PTV publishing | Section 2 |

---

## 2. QuickFrame AI: facts and timeline

| Date | Event | Label / source |
|---|---|---|
| 2021-12-30 | MNTN acquires QuickFrame Inc., "a marketplace platform that uses a video-as-a-service solution." Goodwill **$38.4M** | [reported] 10-K FY25 |
| 2025-10-29/30 | **QuickFrame AI public beta.** Builds an ad from a URL with no assets needed. Free creation through year-end for use on PTV. Exports to Meta, TikTok, YouTube and Google Ads Manager. Average **~12 minutes** from idea to finished ad. Initial stack: Google Veo and Imagen, ElevenLabs, WellSaid Labs, Stability AI. CEO: "97% of advertisers on our platform had never run a TV ad before, and the biggest barrier was creative." | [reported] MNTN PR, https://mountain.com/news/mntn-unveils-quickframe-ai-new-ai-platform-in-beta-allows-brands-of-any-size-to-create-studio-quality-ads-in-minutes ; PPC Land 2025-11-03, https://ppc.land/mntn-launches-quickframe-ai-to-create-studio-quality-ads-in-12-minutes/ |
| ~Dec 2025 | PTV integration: **new advertisers automatically get three free AI-generated TV ads** from a scan of their website, plus free custom commercials. Stack: Veo 3.1, ElevenLabs, Stable Audio 2.5 | [reported] https://mountain.com/product-news/mntn-quickframe-ai-creative-integration/ (page undated; Dec 2025 inferred) |
| 2026-01-28 | Consistent characters, products and locations; director controls. CEO calls it "one of the fastest-growing tools in the MNTN suite" | [reported] BusinessWire, https://www.businesswire.com/news/home/20260128625370/en/ |
| 2026-02-10 | Q4'25 call: "within the first month… **5,000 people on product**." Models orchestrated per scene (Gemini, Sora 2, Nano Banana). MNTN publishes "at least one AI video a week" for its own marketing | [reported] Q4'25 call, https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/ |
| 2026-05-05 | **QuickFrame AI 3.0, out of beta.** Storyboard editor, multi-shot, dialogue, AI plus live-footage mixing, UGC templates, collaboration, "new subscription tiers." Models: Seedance 2.0, fal, Kling, Pixverse, WellSaid, ElevenLabs, Shutterstock, Brandfetch. On the call: "most of our younger customers… small businesses, are in some way using QuickFrame AI." Integrated with "Sora, Kling, and Google's Veo." Go-live rates up, but "we haven't quantified it yet" | [reported] PR (URL above); Q1'26 8-K, https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000038/mntnearningsrelease2026-q1.htm ; Q1'26 call, https://www.investing.com/news/transcripts/earnings-call-transcript-mntn-q1-2026-tops-forecasts-stock-rises-93CH-4661246 |
| 2026-06-03 | Help center: "your first video is free… additional AI generation may require a subscription." Existing customers who have launched campaigns get one more commercial free | [reported] https://help.mountain.com/en/articles/14188510-create-videos-with-quickframe-ai |
| 2026-08-04 | Q2'26: "**over 37,000 QuickFrame AI signups in Q2**, bringing us to **over 73,000 signups year-to-date**." 8-K: "**Adobe integrating QuickFrame AI into GenStudio for Performance Marketing**" and "**Google recognizing QuickFrame AI as an early adopter of its latest Gemini Omni Flash models**." CEO: "at this moment, we're making it available at no charge… stay tuned" on monetization. Impact "essentially gross margin neutral," offset by hosting efficiencies. "A lot of the QuickFrame users are creators. They're not necessarily the marketers." The team ships "every single week, if not multiple times a week" | [reported] Q2'26 8-K, https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm ; Q2'26 call, https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/ |
| Q2'26 deck | 235 AI voices (158 unique voiceover voices) | [reported via third-party summary] Investing.com, https://ca.investing.com/news/company-news/mntn-q2-2026-slides-21-revenue-growth-48-ebitda-gain-amid-earnings-miss-93CH-4775731 |
| Oct 2026 | quickframe.com shows Free/Starter $39/Pro $99/Max $250 tiers and lists Seedance 2.5 and Gemini Omni Flash. Claims an Adweek 2026 Tech Stack "Best Generative AI Platform" award | [reported, company site; award unverified] https://quickframe.com/ |

**Derived and missing metrics**
- Q1'26 signups ≈ 73,000 − 37,000 = **~36,000** [estimate]. Signups were flat quarter over quarter, not accelerating.
- **Pricing conflict.** The Q2 call says the product is offered "at no charge." The help center (June 2026) and quickframe.com (October 2026) show paid tiers after the first free video. My reading is that creation tied to PTV campaigns is free, while standalone or heavy usage needs a subscription. **Subscription revenue has not been disclosed and is presumably immaterial** [estimate].
- **Conversion of QuickFrame AI users to paying PTV customers: NOT DISCLOSED** by management in any release, call or filing reviewed.
- **Adobe GenStudio integration:** only MNTN's 8-K describes it. I found no Adobe-side announcement, and terms and economics are undisclosed.
- **Gemini Omni Flash "early adopter":** this is MNTN's claim. Google's model card names no partners. quickframe.com does list Omni Flash as an available model, which is consistent.
- **Underlying models:** all third-party (Google Veo/Imagen/Gemini Omni Flash/Nano Banana, ByteDance Seedance 2.0/2.5, Kling, Pixverse, formerly OpenAI Sora 2, ElevenLabs, WellSaid, Stability/Stable Audio, Shutterstock licensed assets, fal inference). MNTN calls only the **orchestration layer** proprietary (Q1'26 call).

**The human QuickFrame marketplace**
- 10-K: "our marketplace of **thousands** of independent creators." Launch materials: **5,000+ vetted video professionals**, **50,000+ ads** produced, **2,750 brands** over 10 years [reported via PPC Land, 2025-11-03].
- Revenue: "we generate revenue through QuickFrame's ad production services," reported **net** because MNTN acts as agent [reported, 10-K/10-Q]. Not separately disclosed. MNTN reports a single segment with no revenue-disaggregation table.
- **Creative credits are shrinking.** Deferred revenue, which "primarily relates to customer creative credits… and creative production services in progress," fell from **$9.0M (2024-12-31) to $5.5M (2025-12-31) to $2.7M (2026-06-30)** [reported; 10-K FY25 note; 10-Q 2Q26 note 8]. Part of the 2025 decline came from $2.6M sold with Maximum Effort.
- **Breakage boosted 1H26 revenue.** 1H26 revenue included **$1.7M** "related to the expiration of unused creative credits associated with amended contracts" [reported, 10-Q 2Q26]. That is **~1.3 pts** of the 17.5% 1H26 growth, so growth ex-breakage was **~16.2%** [estimate: 1.7/132.97; (156.21 − 1.7)/132.97 − 1]. The Q2 MD&A does not mention it, so it most likely fell in Q1'26 [estimate].
- 1H26 creative revenue fell $4.2M and production revenue fell $2.0M y/y, "primarily due to the divestiture of Maximum Effort" [reported].
- AdExchanger noted many QuickFrame "maker" links now lead to broken pages (2025-11-05). The human marketplace is being de-emphasized in favor of AI.

---

## 3. Moat, funnel or copyable feature?

| Attribute | MNTN QuickFrame AI | Google/YouTube (Veo in Ads) | Meta | Amazon | Roku |
|---|---|---|---|---|---|
| Price to advertiser | Free first video, three free PTV ads; tiers $39–$250/mo | No added fee (secondary sources) | Free inside Ads Manager | Free (Sponsored Brands) | No native gen-AI; $500 suggested start |
| Output | Full multi-scene 15/30s TV spots with VO, dialogue, consistent characters | ≤10s clips from images | Image-to-video, multi-scene from images; video-from-static GA (Oct 2026, per secondary sources) | Multi-scene product video; Dynamic TV Creative variants | Upscaled social video |
| Underlying model | Third-party mix | Own (Veo) | Own | Own/undisclosed | Partner |
| Distribution scale | 4,225 TTM PTV customers; 73k QF AI signups 1H26 | Millions of advertisers | 9M+ SMBs using AI creative | Millions of sellers | Ads Manager SMBs (count undisclosed) |
| Premium CTV inventory | Yes (PTV) | YouTube on TV | No | Prime Video | Roku |

**Assessment**
- **Not a moat.** All inputs are rented. The hyperscalers own the best models, Google at marginal cost. Platforms with 100–1,000x MNTN's advertiser base give away similar tools [estimate, from the scale figures above]. Model churn (Sora gone, Seedance under legal cloud) shows the dependency risk, which the 10-K flags directly: if providers "unfavorably change the terms… our solutions may become less appealing" [reported].
- **A real funnel.** 73k signups in 1H26 against 4,225 TTM customers is a top-of-funnel about 17x the paying base [estimate: 73,000/4,225]. QuickFrame AI also exports to Meta, TikTok and YouTube, so it reaches creators and marketers who are not yet buying TV. Management positions it as a "standalone opportunity in terms of usage" and a cross-sell path. Inbound leads were ~75% of the pipeline, against ~2% three years earlier (AdExchanger, 2025-11-05) [third-party reporting of management].
- **Partly defensible feature.** The integration is where MNTN has an edge today: one-click publishing to PTV, automatic spec QA, measurement feedback, and full 30s spots where Google's in-Ads tool makes ≤10s clips. The window is probably 12–24 months [estimate]. Google already has Veo plus YouTube on CTV, Amazon has Prime Video plus an agentic Creative Agent, and Roku can add a gen-AI partner. Analysts already asked about Roku, Amazon, AppLovin and The Trade Desk moving down-market. Douglas replied that MNTN is "purpose-built for the SMB market" and that big entrants would be "a big validator" (Q1'26 call).
- **Peer signal on SMB CTV.** Roku's CEO said "AI is opening the entire new market of small and medium-sized businesses, which we're addressing with Ads Manager" (Marketing Dive, 2026-02-13, https://www.marketingdive.com/news/roku-says-its-growing-video-advertising-faster-than-broader-ott-market/812191/) [third-party]. Roku estimates local CTV advertising at about **$2.8B in 2025, ~8% of local video** [third-party, Roku 2026 predictions, https://advertising.roku.com/2026-predictions]. On the Q1'26 call Douglas said Pinterest's tvScientific deal is "not competitive to MNTN" in sales cycles [reported, management view].

---

## 4. Market expansion: does AI creative bring first-time TV advertisers?

**Company-level evidence**

| Metric | Value | Label / source |
|---|---|---|
| Customers who had never run a TV ad | ~95% (10-K FY25; Q1'26 call; Q2'26 deck for 2025 cohorts); "97%" (Oct–Nov 2025 PR/call) | [reported] |
| Share of PTV advertisers using no agency | >90% | [reported] Q1'26 call |
| Small businesses' share of MNTN revenue | **6% (Q4'24) to 15% (Q3'25)** | [third-party reporting of management] AdExchanger 2025-11-05, https://www.adexchanger.com/tv/mntns-smb-ctv-ad-business-is-growing-like-gangbusters/ |
| TTM active PTV customers | 2,225 (FY24), 3,632 (FY25, +63%), 3,874 (Q1'26, +46%), 4,225 (Q2'26, +40%) | [reported] 10-K; Q1/Q2'26 8-Ks |
| Quarterly active PTV customers, y/y | **+24% (Q2'26)**, +27% (1H26) | [reported] 10-Q 2Q26 MD&A |
| Average spend per customer | "decrease… as we continued to expand our overall SMB footprint, including small businesses" | [reported] 10-K FY25 and 10-Q 2Q26 |
| Revenue per TTM customer | ~$101k (FY24: $225.6M/2,225), ~$80k (FY25: $290.1M/3,632), ~$74k (TTM 2Q26: $313.3M/4,225, where TTM revenue = 290.1 − 133.0 + 156.2) | [estimate]. FY24 includes Maximum Effort revenue, which overstates the drop somewhat |
| MNTN Express (small-business tier, launched 2026-04-01) | >7,000 signups in 120 days; "hundreds" became paying customers; "small contributor," possibly "meaningful in 2027" | [reported] Q2'26 call (AOL transcript, https://www.aol.com/articles/mntn-mntn-q2-2026-earnings-234636000.html) |
| QuickFrame AI signups | ~5,000 users in first month; ~36k in Q1'26; 37k in Q2'26; 73k 1H26 | [reported] / [estimate] for Q1 |
| QF AI to PTV conversion | **Not disclosed** | Data gap |

**Funnel arithmetic** [estimate]
- **Express:** "hundreds" of 7,000 signups, read as 200–700 paying, is a **~3–10%** conversion.
- **QuickFrame AI:** TTM customers rose by only **593** in 1H26 (3,632 to 4,225) against 73,000 signups. Suppose gross new PTV customers in 1H26 were 1,000–2,000 and every one came from QF AI. The implied conversion is still only **~1.4–2.7%**. True attribution is surely lower, because many signups are "creators… not necessarily the marketers."
- **Bottom line:** AI creative widens the top of the funnel a great deal, but the new customers convert at low rates and spend less.

**Industry-level evidence**
- 86% of buyers use or plan to use gen-AI for video creative [third-party, IAB, cited 2026-01-15].
- Meta reports 9M+ SMBs using AI creative tools [third-party reporting, 2026-07-31].
- Roku names AI as the opener of the SMB market [third-party, 2026-02-13].
- Amazon has opened self-serve Streaming TV to Brand-Registry sellers [third-party].
- **No independent dataset found** (eMarketer, IAB or Nielsen) quantifying SMB CTV advertiser counts or the share of new CTV advertisers using AI-made creative. eMarketer pages returned 403.

**Interpretation:** the 95–97% "never advertised on TV" figure **pre-dates** QuickFrame AI. It reflects MNTN's search/social-style SMB targeting, not proof that AI caused the inflow. Since the AI launch (Q4'25 onward), TTM customer growth has *decelerated* (63% to 46% to 40%), and quarterly-active growth is 24%. Revenue growth has also slowed, from 36% ex-Maximum-Effort in FY25 to about 21% in Q2'26 and a 22–26% guide for FY26. So far AI creative has **not visibly re-accelerated** the business. Management points to 2H26 and 2027 for Express and QuickFrame AI contribution, so the test is Q3'26 (Nov 4) and Q4'26.

**Cost of giving creative away** [estimate, upper-bound sensitivity]
- Scenario: each 1H26 signup generates one 30s spot with 5–10 takes at $0.10–$0.40/s. That is 73,000 × 30s × (5 × $0.10 to 10 × $0.40), or **~$1.1M–$8.8M** of inference in 1H26.
- Management says the impact is GM-neutral, and Q2 cost of revenue rose only $0.3M y/y to $16.2M [reported]. Actual usage is therefore probably near the low end, or the cost sits in T&D/S&M.
- Where inference cost is booked is **not disclosed**. If usage scales 10x it would matter against an 80% gross margin.

---

## 5. Likelihood, timing and impact

| Scenario | Likelihood | Timing | Impact on MNTN | Key evidence |
|---|---|---|---|---|
| **Threat 5: creative commoditization.** Free AI video everywhere removes MNTN's "we solve creative" edge; QuickFrame's human marketplace and creative-credit bundles lose value | **High (~80%)** that creative stops being a differentiator by end-2027 | Already under way (2026), mostly complete by 2027–28 | **Direct: low.** Production revenue is net and small; creative credits are already down to $2.7M. **Indirect: moderate.** It lowers SMB switching costs to Amazon Sponsored TV, Roku Ads Manager, YouTube and other self-serve CTV sellers, which adds pressure on CAC and take-rate. Rough sensitivity for the model: −1 to −3 pts of annual revenue growth from 2027 in a bear case, through slower customer adds [estimate] | Google Veo in Ads (2026-03); Meta 9M SMBs; Amazon free generator; Roku SMB push; Sora retirement shows model churn |
| **Upside 1: production-cost collapse brings SMBs into TV**, and MNTN captures a share | **Medium-high (~65%)** that CTV advertiser counts expand materially. **Medium (~45%)** that MNTN captures enough to re-accelerate revenue growth above 25% | Customer-count effect visible 2026–27; revenue effect 2027–30, with Express flagged as "meaningful in 2027" | **Positive for customer count**, which could keep growing 25–40%/yr [estimate, extrapolating the current trend]. **Diluted on revenue**: spend per customer is falling roughly 5–20%/yr [estimate, from $101k to $80k to $74k]. Net revenue lift is perhaps +2 to +5 pts of growth in a bull case [estimate] | 73k QF AI signups; Express 7k signups and "hundreds" paying; TTM customers +40%; SMB revenue share 6% to 15% |

**Net for this topic: slight AI winner (+1 on −3 to +3).** AI turns MNTN's founding wedge (TV for SMBs that lack a commercial) from a costly human service into a near-free, instant one. That fits the self-serve model and is roughly gross-margin neutral. It does not create a moat, and the same economics help larger competitors. For the model: grow customers fast, assume continued decline in revenue per customer, attribute no material revenue to QuickFrame AI subscriptions before 2027, and do not count 1H26 creative-credit breakage ($1.7M) as recurring.

---

## 6. Data gaps

- QuickFrame AI to PTV paid conversion, cohort spend, and the share of new PTV customers whose first ad was AI-made: **not disclosed**.
- QuickFrame AI subscription revenue, paid-subscriber count, and the conflict between "no charge" (Aug 2026 call) and paid tiers on quickframe.com / the help center.
- QuickFrame human-marketplace revenue (reported net, not disaggregated) and current creator count.
- Adobe GenStudio integration terms and economics, with no Adobe-side confirmation found. Google Omni Flash "early adopter" status is MNTN's claim only.
- Where AI inference cost is booked (COGS, T&D or S&M) and its dollar amount.
- Independent industry data on SMB CTV advertiser counts and AI-creative usage (eMarketer was blocked). The IAB "40% of ads gen-AI by 2026" projection is cited only by a low-quality secondary source.
- Verified pricing and specs for Kling, Luma, Pika, Midjourney video, Arcads, Canva, CapCut and Adobe Firefly video; Amazon Creative Agent's video scope; Amazon Sponsored TV minimums on Amazon's own page; Vibe's free AI creative claims.
- Traditional TV-spot production cost: only one low-quality source ($10k–$500k). No ANA/4A's benchmark was retrieved.
- Q3 2026 results (due 2026-11-04).
- The session's web-search budget ran out before the platform-tool and vendor-pricing sweep was complete. Those rows rest on fewer sources.

---

## Sources

1. MNTN, "MNTN Unveils QuickFrame AI…" press release, 2025-10-29: https://mountain.com/news/mntn-unveils-quickframe-ai-new-ai-platform-in-beta-allows-brands-of-any-size-to-create-studio-quality-ads-in-minutes ; BusinessWire 2025-10-30: https://www.businesswire.com/news/home/20251030951016/en/
2. MNTN blog, "MNTN CEO Mark Douglas Introduces QuickFrame AI," Oct 2025: https://mountain.com/blog/introducing-quickframe-ai/
3. PPC Land, "MNTN launches QuickFrame AI…," 2025-11-03: https://ppc.land/mntn-launches-quickframe-ai-to-create-studio-quality-ads-in-12-minutes/
4. MNTN, "MNTN Announces Creative Integration With QuickFrame AI…," ~Dec 2025: https://mountain.com/product-news/mntn-quickframe-ai-creative-integration/
5. MNTN/BusinessWire, "QuickFrame AI Scales Rapidly…," 2026-01-28: https://www.businesswire.com/news/home/20260128625370/en/
6. MNTN, "MNTN Releases QuickFrame AI 3.0…," 2026-05-05: https://mountain.com/press/mntn-releases-quickframe-ai-3-0-with-a-major-feature-expansion-delivering-tv-ready-commercials-in-minutes/
7. MNTN Help Center, "Create Videos with QuickFrame AI," 2026-06-03: https://help.mountain.com/en/articles/14188510-create-videos-with-quickframe-ai
8. QuickFrame AI pricing page, accessed 2026-10-15: https://quickframe.com/
9. MNTN 8-K Q3'25 earnings release, 2025-11-04: https://www.sec.gov/Archives/edgar/data/1891027/000189102725000019/mntnearningsrelease2025-q3.htm
10. MNTN Q4/FY25 earnings release PDF, 2026-02-10: https://s205.q4cdn.com/886349678/files/doc_financials/2025/q4/MNTN-Reports-Record-Fourth-Quarter-and-Full-Year-2025-Results-2026.pdf
11. Motley Fool, MNTN Q4 2025 earnings call transcript, 2026-02-10: https://www.fool.com/earnings/call-transcripts/2026/02/10/mntn-mntn-q4-2025-earnings-call-transcript/
12. MNTN Form 10-K FY2025, filed 2026-02-19: https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm
13. MNTN 8-K Q1'26 earnings release, 2026-05-05: https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000038/mntnearningsrelease2026-q1.htm
14. Investing.com, MNTN Q1 2026 earnings call transcript, 2026-05-05: https://www.investing.com/news/transcripts/earnings-call-transcript-mntn-q1-2026-tops-forecasts-stock-rises-93CH-4661246
15. MNTN 8-K Q2'26 earnings release, 2026-08-04: https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm
16. Motley Fool, MNTN Q2 2026 earnings call transcript (published 2026-08-11): https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/ ; AOL copy: https://www.aol.com/articles/mntn-mntn-q2-2026-earnings-234636000.html ; Investing.com: https://www.investing.com/news/transcripts/earnings-call-transcript-mntn-q2-2026-profit-miss-sparks-afterhours-drop-93CH-4835959
17. MNTN Form 10-Q for Q2 2026, filed 2026-08-10: https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm
18. Investing.com, "MNTN Q2 2026 slides…" (secondary deck summary), Aug 2026: https://ca.investing.com/news/company-news/mntn-q2-2026-slides-21-revenue-growth-48-ebitda-gain-amid-earnings-miss-93CH-4775731
19. StockTitan (relaying MNTN PR), "MNTN to Announce Third Quarter 2026 Financial Results on November 4, 2026," 2026-10-14: https://www.stocktitan.net/news/MNTN/mntn-to-announce-third-quarter-2026-financial-results-on-november-4-0pv9why9jhfk.html
20. AdExchanger (V. McNally), "MNTN's SMB CTV Ad Business Is Growing Like Gangbusters," 2025-11-05: https://www.adexchanger.com/tv/mntns-smb-ctv-ad-business-is-growing-like-gangbusters/
21. Google, Gemini API pricing, accessed 2026-10-15: https://ai.google.dev/gemini-api/docs/pricing
22. Google DeepMind, Gemini Omni Flash model card, 2026-08-27: https://deepmind.google/models/model-cards/gemini-omni-flash/
23. OpenAI, API deprecations (Sora 2 / Videos API removal 2026-09-24; notice 2026-03-24): https://developers.openai.com/api/docs/deprecations
24. TechCrunch, "OpenAI's Sora… is shutting down," 2026-03-24: https://techcrunch.com/2026/03/24/openais-sora-was-the-creepiest-app-on-your-phone-now-its-shutting-down/
25. Variety (Australia), "ByteDance Pledges Safeguards for Seedance 2.0 After Disney Legal Threat," 2026-02-16: https://au.variety.com/2026/film/global/bytedance-safeguards-seedance-disney-legal-threat-ip-violations-33139/
26. Runway pricing, accessed 2026-10-15: https://runway.com/pricing
27. Creatify pricing, accessed 2026-10-15: https://creatify.ai/pricing
28. HeyGen pricing, accessed 2026-10-15: https://www.heygen.com/pricing
29. Synthesia pricing, accessed 2026-10-15: https://www.synthesia.io/pricing
30. Adobe, GenStudio for Performance Marketing product page: https://business.adobe.com/products/genstudio-for-performance-marketing
31. Google, "Resonate with the YouTube audiences that matter most with Veo in Google Ads," March 2026: https://business.google.com/en-all/accelerate/announcements/veo-google-ads/
32. Amazon Ads, "Create high-quality AI-generated videos in minutes": https://advertising.amazon.com/resources/whats-new/create-high-quality-ai-generated-videos-in-minutes
33. MediaPost, "Amazon Ads Unveils Personalized, AI-Driven Video Format," 2026-05-12: https://www.mediapost.com/publications/article/415018/amazon-ads-unveils-personalized-ai-driven-video-f.html
34. PPC Land, "Meta Q1 2026: $56.3B revenue as AI tools double advertiser adoption," 2026-04-30: https://ppc.land/meta-q1-2026-56-3b-revenue-as-ai-tools-double-advertiser-adoption/
35. MediaPost, "Meta Boosts Advertising In Q2…," 2026-07-31: https://www.mediapost.com/publications/article/416925/meta-boosts-advertising-in-q2-tries-to-reassure-i.html
36. Marketing Dive, "Roku says it's growing video advertising faster than broader OTT market," 2026-02-13: https://www.marketingdive.com/news/roku-says-its-growing-video-advertising-faster-than-broader-ott-market/812191/
37. Roku Advertising, "How much does it cost to advertise on Roku?," 2026-02-25: https://advertising.roku.com/learn/resources/how-much-does-it-cost-to-advertise-on-roku
38. Roku Advertising, "Streaming in 2026: Roku's 5 predictions": https://advertising.roku.com/2026-predictions
39. IAB, "The AI Ad Gap Widens," 2026-01-15: https://www.iab.com/insights/the-ai-ad-gap-widens/
40. AdWorldNews, "Every Small Business Can Run a TV Ad Now…," 2026-05-05 (low-quality/aggregator; used only for the traditional production-cost range, flagged): https://www.adworldnews.com/news/ai-video-ads-small-business-tv-advertising-ctv-broadcast-quality

## Verification (adversarial check)

Checked 2026-10-15 against primary filings (SEC EDGAR), the Q1'26/Q2'26 call transcripts, company pages and the cited third-party pages. WebSearch budget ran out partway through, so the checks below rely on direct fetches of cited or primary URLs. Overall reliability: **high**. The numbers hold up. The corrections are about framing and labels.

| # | Finding | Verdict | Correct value / note | Evidence |
|---|---|---|---|---|
| 1 | QF AI signups >37k Q2'26, >73k YTD; ~36k Q1 (derived) | **Confirmed** | CEO, verbatim: "over 37,000 QuickFrame AI signups in Q2, bringing us to over 73,000 signups year-to-date." Q1'26 call gave no number ("I don't think we're ready to... provide those numbers"), so ~36k for Q1 is derived only. | https://www.fool.com/earnings/call-transcripts/2026/08/11/mntn-mntn-q2-2026-earnings-call-transcript/ ; https://www.investing.com/news/transcripts/earnings-call-transcript-mntn-q1-2026-tops-forecasts-stock-rises-93CH-4661246 |
| 2 | QF AI to PTV conversion not disclosed; ≤~1.4–2.7% implied | **Confirmed (estimate)** | No conversion figure was disclosed. TTM customers 3,632 to 4,225 (+593) is confirmed in the Q2 8-K table. Caveat: on the Q2 call the CEO said "a lot of the QuickFrame users are creators. They're not necessarily the marketers," so signups are a poor denominator. The bound is illustrative only. | https://www.sec.gov/Archives/edgar/data/1891027/000189102726000070/mntnearningsrelease2026-q2.htm ; Fool Q2 transcript (above) |
| 3 | QF AI free with PTV; "at no charge"; "essentially gross margin neutral"; $39/$99/$250 tiers | **Confirmed, with nuance** | All quotes and tiers match (first-month prices $32/$65/$125; Free = 50 one-time credits). "Free to PTV customers" overstates it. The help center (2026-06-03) says the first video is free, "additional AI generation actions may require an active subscription," and existing customers get one extra free commercial. The product page says new advertisers get three free AI TV ads. | https://quickframe.com/ ; https://help.mountain.com/en/articles/14188510-create-videos-with-quickframe-ai ; https://mountain.com/product-news/mntn-quickframe-ai-creative-integration/ |
| 4 | Veo 3.1 $0.40/$0.12/$0.08 per s; Omni Flash ~$0.10/s 720p; $24–$600 per finished spot | **Confirmed. Label fix** | List prices match: Std $0.40 (720p/1080p), Fast $0.12 (1080p), Lite $0.08 (1080p), Omni Flash ~$0.10/s at 720p. The $2.40–$12 per take and $24–$600 per spot are **[estimate]** (10–50 takes is an assumption), not third-party figures. The pricing page lists Veo 3.1 model IDs as "-preview". | https://ai.google.dev/gemini-api/docs/pricing |
| 5 | Traditional production $10k–$500k, 4–8 weeks | **Confirmed (as stated by a weak source)** | AdWorldNews (2026-05-05) gives both figures without any source. The arithmetic floor is ~94% reduction ($600 vs $10k), not 95%. Still needs an ANA/4A's-grade benchmark. | https://www.adworldnews.com/news/ai-video-ads-small-business-tv-advertising-ctv-broadcast-quality |
| 6 | QF AI runs on third-party models only; only orchestration called proprietary | **Confirmed. Label fix** | Q1'26 call, CEO on the orchestration layer: "we consider that part of a technology to be proprietary"; models named include Sora, Kling, Gemini, Veo. The cited 3.0 PR names Seedance 2.0, Kling, Pixverse, WellSaid, ElevenLabs, fal, Shutterstock and Brandfetch. It does **not** name Veo, Gemini or Sora, which come from the Q1 call, the Q2 8-K (Omni Flash) and the product page (Veo 3.1, Stable Audio 2.5). "0 proprietary video models" is an inference [estimate], not a reported figure. The 10-Q risk factors refer generically to "our proprietary AI Technologies". | https://mountain.com/press/mntn-releases-quickframe-ai-3-0-with-a-major-feature-expansion-delivering-tv-ready-commercials-in-minutes/ ; Investing.com Q1'26 transcript (above); https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm |
| 7 | Google Veo in Asset Studio; Meta 9M+ SMBs and +3%; Amazon free video generator + Dynamic TV Creative | **Confirmed, with caveats** | Google (Mar 2026): Asset Studio, ≤10s, up to 3 images, "all campaigns". The Google page does **not** say it is free. Meta: 8M+ advertisers at Q1 (from 4M at end-2024), +3% conversion, 9M+ SMBs at Q2 (MediaPost 2026-07-30/31). Amazon's free Sponsored Brands video generator dates to **unBoxed 2024**, not 2026. Dynamic TV Creative (MediaPost 2026-05-12) personalizes interactive ads for US advertisers who sell on Amazon in select categories. Its pricing is not stated, so it should not be called free. | https://business.google.com/en-all/accelerate/announcements/veo-google-ads/ ; https://ppc.land/meta-q1-2026-56-3b-revenue-as-ai-tools-double-advertiser-adoption/ ; https://www.mediapost.com/publications/article/416925/meta-boosts-advertising-in-q2-tries-to-reassure-i.html ; https://advertising.amazon.com/resources/whats-new/create-high-quality-ai-generated-videos-in-minutes ; https://www.mediapost.com/publications/article/415018/amazon-ads-unveils-personalized-ai-driven-video-f.html |
| 8 | Roku: no native gen-AI builder; $500 start; 2–3 day review; CEO "AI is opening the entire new market of SMBs" | **Confirmed** | The quote matches (Marketing Dive, 2026-02-13). The Roku page (2026-02-25) says "$500–$1,000 is enough" for most first-time advertisers, with no stated minimum. It lists manual review of 2–3 days and only an AI upscaler plus Spaceback. Note: Marketing Dive says Roku cited "generative artificial intelligence tools" as an Ads Manager accelerant, without naming a native builder. | https://www.marketingdive.com/news/roku-says-its-growing-video-advertising-faster-than-broader-ott-market/812191/ ; https://advertising.roku.com/learn/resources/how-much-does-it-cost-to-advertise-on-roku |
| 9 | ~95% (10-K) / 97% (Oct 2025) never ran a TV ad; pre-dates QF AI | **Confirmed. Date fix** | The 10-K FY25 says "approximately 95%". The 97% figure is from the **Q3'25 call (2025-11-04)**, not October 2025 (AdExchanger 2025-11-05). The pre-dating point is stronger than stated: the IPO 424B4 (2025-05-22) says "approximately 96%... as of March 31, 2025," months before the QF AI beta (late Oct 2025). | https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm ; https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm ; https://www.adexchanger.com/tv/mntns-smb-ctv-ad-business-is-growing-like-gangbusters/ |
| 10 | Small business 6% of revenue (Q4'24) to 15% (Q3'25); inbound ~75% vs ~2% | **Confirmed (third-party)** | AdExchanger (V. McNally, 2025-11-05): "In Q4 of last year, small businesses represented 6%... as of last quarter, it's up to 15%"; inbound "roughly 2%... three years ago... Now... 75%". Not re-checked in a primary transcript. | https://www.adexchanger.com/tv/mntns-smb-ctv-ad-business-is-growing-like-gangbusters/ |
| 11 | TTM customers +63%/+46%/+40%; quarterly active +24% Q2, +27% 1H; lower spend per customer | **Confirmed** | 3,632/2,225 = +63.2% (the 10-K says 63.2%). 3,874/2,647 = +46.4%. 4,225/3,020 = +39.9%. The 10-Q says active PTV customers +24% (Q2) and +27% (1H), "offset by a decrease in average spend per customer." Q1'26 quarterly was +26% (Q1 10-Q). | https://www.sec.gov/Archives/edgar/data/1891027/000189102726000073/mntn-20260630.htm ; Q2 8-K (above) |
| 12 | Revenue per TTM customer $101k to $80k to $74k | **Confirmed (estimate)** | $225.571M/2,225 = $101.4k. $290.093M/3,632 = $79.9k. TTM 2Q26 revenue $313.3M (290.1 − 64.5 − 68.5 + 73.7 + 82.5)/4,225 = $74.2k. Caveat: the numerator is total revenue, including non-PTV creative/production revenue and $5.4M of Maximum Effort in Q1'25. | 10-K FY25; Q2'26 8-K (above) |
| 13 | MNTN Express: >7,000 signups in 120 days; "hundreds" paying; meaningful in 2027 | **Confirmed** | Verbatim: "over 7,000 signups for Express in the first 120 days... hundreds of those signups have become paying customers... small today... will be a meaningful contributor to growth as we enter 2027." Launched April 1. The ~3–10% conversion is an estimate. | Fool Q2 transcript (above) |
| 14 | Creative-credit deferred revenue $9.0M to $5.5M to $2.7M; $1.7M breakage (~1.3 pts; ~16.2% ex-breakage) | **Corrected (framing)** | The numbers are right, but the line is **total** deferred revenue ("primarily... creative credits... and creative production services in progress"). **$2.6M of the Dec-24 $9.0M was sold with the Maximum Effort divestiture**, so the like-for-like decline is ~$6.4M to $5.5M to $2.7M. The $1.7M expired-credit revenue was recognized in **Q1'26** ("associated with amended contracts"). The 10-Q does not call it "one-time". Growth math is right: 1.7/133.0 = 1.3 pts; ex-breakage +16.2%. | https://www.sec.gov/Archives/edgar/data/1891027/000189102726000019/mntn-20251231.htm (deferred revenue note) ; Q2 10-Q (above) ; Q1 10-Q https://www.sec.gov/Archives/edgar/data/1891027/000189102726000040/mntn-20260331.htm |

**Label flags:** #4 cost per finished spot and #6 "0 proprietary video models" are estimates or inferences, not reported or third-party figures. In #7, "free" is not supported for Google's Veo-in-Ads page or for Amazon Dynamic TV Creative. In #14, "creative-credit deferred revenue" is total deferred revenue, and the decline includes divestiture effects.
