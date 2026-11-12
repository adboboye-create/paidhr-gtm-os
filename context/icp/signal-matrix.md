# PaidHR: Signal Matrix

Who to target (segments x personas, with the angle per cell), which buying signals find them, and which signals to build first. Read before planning a campaign, building a list or speccing a workflow (`/campaign-strategy` and `/build-workflow-spec` read this file).
v1, 2026-11-12. Work in progress: validate with PaidHR sales and leadership before building. Method: [signal-matrix-framework.md](../../knowledge-base/playbooks/signal-matrix-framework.md), [workflow-anatomy.md](../../knowledge-base/playbooks/workflow-anatomy.md).
Related: [icp.md](icp.md), [personas.md](personas.md), [messaging.md](../messaging/messaging.md), [facts.md](../messaging/facts.md).

**INFERRED** = not supported by the research files; a reasoned hypothesis to test. Anything not marked INFERRED carries a source tag (key at the bottom). Unknown figures are written "unknown".

## How the matrix is built

- **Market**: Nigeria (proven), plus Kenya and Ghana as expansion markets from 2026-11-12 (scope decision, [icp.md](icp.md) v3; matrix cells and signals below were built and tested for Nigeria only). Medium digital footprint: LinkedIn covers office-based companies well; frontline firms (retail, logistics, manufacturing) are thinner online (INFERRED, partly confirmed by noisy LinkedIn job counts, ss:T1).
- **Product framing**: single product (HRMS with statutory remittance at the core), so no lead / upsell product columns. Modules (cross-border payroll, PaidLife / EWA, time and attendance, performance) change the angle per cell. Source: co:S1, S2.
- **Segment axis**: workforce type x company size. Chosen because it is observable (LinkedIn industry, headcount, Google Maps locations), each company fits one row, and it changes the buyer and the pain: founders own payroll under 50 staff (sp:V1, V7); HR leads own it above (sp:V3 to V6); frontline firms add shifts and sites (sp:V5, co:S1).
- **Persona axis**: the three buying roles in [personas.md](personas.md), plus Operations lead / COO (INFERRED: one data point, Sygnite COO, sp:V10).
- **Not segments**: switching from a failing provider, staff abroad and growth spurts are timing events, so they live in Matrix 2 as signals, not rows.

## Matrix 1: ICP segments x personas

### Segment definitions

- **S1. Frontline operators, 50 to 500 staff**: Nigerian HQ; most staff work shifts or on sites (retail chains, logistics, manufacturing, cinemas and hospitality, field engineering); 2+ physical locations. Filters: LinkedIn industry in Retail, Transportation / Logistics, Manufacturing, Food and Beverage, Entertainment, Renewable Energy; Google Maps locations 2+; employee count 50 to 500 from Clay / Apollo (LinkedIn headcount will undercount frontline staff, INFERRED). Evidence: PaidHR names logistics, retail, manufacturing as main sectors (cu:C3, C4); Filmhouse multi-site cinema (sp:V5); Sygnite field engineering (sp:V10).
- **S2. Office-based growth companies, 50 to 500 staff**: Nigerian HQ; tech, fintech, insurtech, digital and professional services; LinkedIn headcount 50 to 500. Evidence: Go54 (50 to 70 staff), Mono, MyCoverGenius (sp:V6, V4, V3).
- **S3. Founder-run teams, 20 to 49 staff**: Nigerian HQ; mostly startups; LinkedIn headcount 20 to 49; no HR title on LinkedIn (INFERRED filter). Evidence: Cleva "almost 20", FAMASI (sp:V7, V1); Standard plan floor 20 (co:S6).
- **S4. Large employers, 500 to 2,000 staff**: Nigerian HQ, any industry. Evidence is one customer: TSL, 2,000 staff, first customer (cu:C1). SeamlessHR leads here with ERP integrations (cp:K1, K2). Mostly INFERRED.

- **Kenya and Ghana**: S1 to S4 apply with "Nigerian HQ" read as "HQ in Nigeria, Kenya or Ghana" (icp.md v3). Evidence and examples above are all Nigerian; whether the segments behave the same in Kenya and Ghana is INFERRED.

### Company examples

- **S1**: customers Filmhouse Group, Sygnite Power (sp:V5, V10), TSL (above band, cu:C1). Prospects seen in a Google Maps test, size unverified: Prince Ebeano Supermarket, SPAR Market Ikoyi, Grand Square Supermarket and Stores (ss:T3). Full list: requires Clay research with the S1 filters above.
- **S2**: customers Go54, Mono, MyCoverGenius (sp:V6, V4, V3). Prospect list: requires Clay research with the S2 filters above.
- **S3**: customers Cleva, FAMASI (sp:V7, V1). Prospect list: requires Clay research with the S3 filters above.
- **S4**: customer TSL (cu:C1). Prospect list: requires Clay research.
- **Do not use customer names in copy** until cleared in [facts.md](../messaging/facts.md).

### Angle per cell

| Segment | HR lead (champion) | CEO / founder (economic buyer) | Finance lead / CFO (influencer) | Ops lead / COO (INFERRED influencer) |
|---|---|---|---|---|
| **S1. Frontline 50 to 500** | Approval workflows that catch last-minute errors before salaries go out, and staff get payslips without coming to HR (sp:V5, V6). Shifts and clock-ins flow into payroll (co:S1). | Every state's PAYE and pension filed on time with a receipt for each (sp:V7, V2; co:S1). Multi-state remittance for multi-site firms: INFERRED. | One payroll check instead of two, self-generated payment receipts, fast disbursement (sp:V6, V5). | Geo-referenced clock-ins, shifts and overtime flow straight into payroll; staff self-onboard (co:S1; sp:V10). |
| **S2. Office-based 50 to 500** | Run payroll on the day, not weeks ahead; compliance and statutory filing off your plate; staff self-serve payslips (sp:V3, V4, V6). | What worked for a smaller team stops working as you grow; EWA as a benefit staff use (sp:V3, V7, V6). | Remittances that land at the statutory bodies, with proof; ISO 27001; no customer deposits held (sp:V6; co:S1, S8). | n/a (no ops role in office-based payroll evidence) |
| **S3. Founder-run 20 to 49** | n/a: usually no HR lead yet; founder owns payroll (sp:V1, V7). | Get your payroll hour back; tax and pension automated as you add people; finally offer pension; start the same day with no onboarding fee (sp:V1, V7; co:S7). | n/a: rarely a finance lead at this size (INFERRED) | n/a |
| **S4. Large 500 to 2,000** | Built for your size with dedicated support (Enterprise plan, co:S6); named account manager (sp:V4). Rest INFERRED. | INFERRED: same remittance proof as S1 at higher volume. | ERP and finance-system pushes and payroll API (co:S1). Fit against SeamlessHR's SAP / Oracle integrations unknown (cp:K1). | INFERRED: as S1 Ops. |

- **Cross-border angle (any cell, only when signal S08 fires)**: pay staff and contractors abroad in 45+ currencies from the same payroll (co:S1, S8; cp:K6).
- **New tax law layer (any cell)**: the Nigeria Tax Act 2025 changed PAYE bands, reliefs and what counts as taxable pay from 1 Jan 2026 (ss:E1). Use as context in copy; PaidHR supports the changes per a third-party listing (co:S13).

### Segment priority

| Segment | Signal density | Product fit | Reachable with Nigerian data | Priority | Why |
|---|---|---|---|---|---|
| **S2. Office-based 50 to 500** | High | High | High | **1** | Most on-camera proof (Go54, Mono, MyCoverGenius); LinkedIn headcount and hiring data work for these firms. |
| **S3. Founder-run 20 to 49** | Medium | Medium | High | **2** | Clear founder pain (sp:V1, V7) and fast decisions; free tools compete (cp:K11); lower deal size (INFERRED, pricing unknown). |
| **S1. Frontline 50 to 500** | Low to medium | Claimed high, proven medium | Low to medium | **3, run as a test** | PaidHR calls it core (cu:C3) but only Filmhouse and Sygnite prove it on camera (icp open question 1). Google Maps gives a physical signal LinkedIn cannot. |
| **S4. Large 500 to 2,000** | Low | Low (one customer) | Medium | **4, park** | SeamlessHR's home ground; no evidence beyond TSL. |

## Matrix 2: Buying signals

**Scores**: each test 1 (weak) to 3 (strong). **Reason** = clear buying reason now. **Volume** = enough companies per month. **Data** = data you can actually get. **Story** = a natural opener in copy. Total out of 12.

| # | Signal | Mother intent | Segments | Data source | Tool to detect | Reason | Volume | Data | Story | Total | Type | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 | Hiring an HR, payroll or People role (payroll officer, HR manager, Head of People) | Hiring specific roles | S1, S2, S4 | LinkedIn Jobs; MyJobMag; Jobberman (not tested) | treg `harvestapi.linkedin.search.jobs` or Clay Find Jobs; crawl4ai scrape for MyJobMag | 2 | 2 | 3 | 3 | **10** | Universal | VERIFIED (data); reason INFERRED |
| S02 | First HR hire at a 20 to 49 person company | Have / don't have team + hiring | S3 | Same as S01, filtered to headcount 20 to 49 with no current HR title | Same as S01 + treg `scrapecreators.x.v1-linkedin-company` for headcount | 3 | 1 | 2 | 3 | **9** | Universal | VERIFIED (COMPOUND) |
| S03 | New HR leader in the last 100 days | New leadership | S1, S2, S4 | LinkedIn profiles (start date in role) | treg `apollo.people.search` (free) + `apollo.people.enrich` ($0.026, returns start dates, ss:T4); Clay Find People | 2 | 2 | 3 | 3 | **10** | Universal | VERIFIED (ss:T4); reason INFERRED |
| S04 | Headcount up 20%+ in 6 months | Hypergrowth (headcount) | S2, S3 | LinkedIn company employee count, monthly snapshots | treg `scrapecreators.x.v1-linkedin-company` ($0.00188/call) or Clay Enrich Company | 3 | 2 | 1 | 3 | **9** | Universal | VERIFIED (PARTIAL): no fresh history for Nigerian firms (ss:T5) |
| S05 | Raised a funding round in the last 90 days | Fundraising | S2, S3 (tech only) | TechCabal and Techpoint funding news; funding databases | treg `predictleads.companies.financing_events` ($0.04/call) or `aviato.companies.funding_rounds` ($0.01) | 2 | 1 | 2 | 2 | **7** | Universal | VERIFIED (COMPOUND): pair with S04 |
| S06 | Looks like an on-camera customer | Lookalike of customers | S2, S3, S1 | Seeds: Go54, Mono, MyCoverGenius, Cleva, FAMASI, Filmhouse (sp:V1 to V7) | Clay lookalike / company search by industry and size | 1 | 3 | 2 | 2 | **8** | Universal | VERIFIED as ICP filter, not a timing signal |
| S07 | Opened a new site or store | Niche-specific (physical world) | S1 | Google Maps location count per brand, monthly delta | treg `crawl4ai.google.serp.maps` ($0.00023/success) | 2 | 2 | 2 | 2 | **8** | Niche-specific | VERIFIED (data, ss:T3); reason INFERRED |
| S08 | Hiring or paying people outside Nigeria | Hiring offshore | S2, S3 | LinkedIn Jobs posted by Nigerian companies for remote or non-Nigeria roles | treg `harvestapi.linkedin.search.jobs` (location and workplaceType filters) | 2 | 1 | 1 | 3 | **7** | Universal | VERIFIED (PARTIAL): hard to tie role location to employer HQ |
| S09 | Engaged with PaidHR content or events (post reactions, Thrive webinars, GITEX Nigeria, Moonshot) | LinkedIn content engagement / event attendance | All | PaidHR LinkedIn posts (posts); webinar sign-ups (PaidHR's own data, INFERRED) | treg scrapecreators post endpoints (reactor lists untested, INFERRED); CRM export | 2 | 1 | 2 | 3 | **8** | Universal | VERIFIED (PARTIAL) |
| S10 | Tax calendar: annual PAYE returns due 31 Jan; new tax law year | Regulatory change | All | Nigeria Tax Act 2025 and JRB guidelines (ss:E1) | None per company: a calendar date | 3 | 3 | 1 | 3 | 10 | Universal | NARRATIVE LAYER only: not a per-company timing signal |
| S11 | Job post names a competitor tool or Excel payroll (SeamlessHR, Workpay, Sage) | Competitor customers | S1, S2 | Job descriptions on MyJobMag / LinkedIn | crawl4ai scrape of descriptions (untested); LinkedIn search is title only (ss:T1) | 2 | 1 | 1 | 2 | 6 | Universal | INFERRED, COMPOUND only |
| S12 | Former Bento Africa client | Competitor customers | S2 | News of Bento collapse; only 3 clients named (cp:K9) | None | 1 | 1 | 1 | 1 | 4 | n/a | KILLED |
| S13 | Newly incorporated company (CAC) | Recently incorporated | S3 | CAC registry | treg corpoapi registry (not connected for this org, ss:T2) | 1 | 2 | 1 | 1 | 5 | n/a | KILLED |
| S14 | New employer pension registration (PenCom) | Regulatory change | S3 | PenCom | None found | 2 | 1 | 1 | 2 | 6 | n/a | KILLED: no public per-employer feed (INFERRED) |

### Signal notes

- **S01 hiring**: LinkedIn, Nigeria, last month: "payroll" 49, "HR manager" 20, "Head of People" 11, "Human Resources" 9, "HR generalist" 7 results; many are global remote employers, so filter to Nigerian HQ (ss:T1). MyJobMag lists Nigerian payroll roles by title with employer and city (ss:E2); its monthly volume is unknown. Why it might mean buying: a company formalising HR or payroll is about to own the problem PaidHR solves (INFERRED). Research says job posts were never tested as a predictor (icp open question 6).
- **S02 first HR hire**: strongest buying reason in S3, because the founder hands payroll to someone new; founders own payroll today (sp:V1, V7). Volume is low (INFERRED).
- **S03 new HR leader**: the HR lead is the champion and decides by demo (sp:V5, V6); that new leaders review tools in their first 100 days is INFERRED (window changed from 90 to 100 days on 2026-11-12). Nigerian LinkedIn profile coverage for start dates is unknown.
- **S04 headcount growth**: best-supported reason in the research: "As we grew it just didn't scale" (sp:V7); "What used to work for a smaller team, it can no longer work for us" (sp:V3); contractors moving to full time triggered PAYE (sp:V7). LinkedIn headcount is reliable for office-based firms (INFERRED) and weak for frontline firms, so S04 is not used for S1. Monthly volume unknown until the first snapshot pair.
- **S05 funding**: only for tech startups (cu:C4 names tech startups as part of the ICP). Nigerian rounds per month unknown; use as a booster on S04, not alone.
- **S06 lookalike**: a static fit filter with no timing, so it fails the framework's "signals indicate timing" check. Use it to seed S2 and S3 lists that S01 to S04 then trigger on.
- **S07 new site**: Google Maps returns named Lagos businesses with addresses (ss:T3); counting a brand's locations month to month needs brand-name matching (INFERRED effort). Ties to the time and attendance and shift modules (co:S1) and to Filmhouse's multi-site setup (sp:V5).
- **S08 staff abroad**: cross-border payroll is a "standout feature" (cp:K6) and about 15% of revenue in Jun 2025 (co:S5). Detection is weak.
- **S09 engagement**: founder-led social has worked (Cleva found PaidHR through the CEO's posts, sp:V7); events are active (posts). Volume depends on PaidHR's own audience: unknown.
- **S10 tax calendar**: every employer must file annual PAYE returns by 31 January and remit within ten days of month end, with penalties for unremitted tax (ss:E1). Use it as a send window (December to January) and an opener for any signal, not as a list source.
- **Killed**: S12 (Bento collapsed Feb 2025, most clients have likely moved on, only 3 names public, naming Bento is an open question in [competitors.md](../positioning/competitors.md)); S13 (new companies sit below the 20-employee floor, co:S6, and the registry is not connected); S14 (no data source).
- **Compounding insight**: 9 of the 11 non-killed signals are universal (one build, keyword and filter swaps per segment). Only S07 is niche-specific, and S10 is a narrative layer.

### Signal coverage per segment

| Signal | S1 Frontline | S2 Office-based | S3 Founder-run | S4 Large |
|---|---|---|---|---|
| S01 HR / payroll hiring | Payroll officer, HR officer roles; S1 industries | Head of People, HR manager roles | n/a (see S02) | HR manager, payroll supervisor roles |
| S02 First HR hire | n/a | n/a | Primary | n/a |
| S03 New HR leader | Yes | Yes | n/a | Yes |
| S04 Headcount growth | n/a (LinkedIn undercounts) | Primary | Yes | n/a |
| S05 Funding | n/a | Booster | Booster | n/a |
| S06 Lookalike | Seeds: Filmhouse, Sygnite | Seeds: Go54, Mono, MyCoverGenius | Seeds: Cleva, FAMASI | n/a |
| S07 New site | Primary | n/a | n/a | Optional |
| S08 Staff abroad | n/a | Yes | Yes | n/a |
| S09 Engagement | Yes | Yes | Yes | Yes |
| S10 Tax calendar | Layer | Layer | Layer | Layer |

## Build first: top five signals

1. **S04 headcount growth, for S2 and S3 (score 9, downgraded 2026-11-12 from 11: tested history sources are stale or shallow for Nigerian companies and count LinkedIn profiles, not payroll staff, ss:T5; needs our own monthly snapshots, first 6-month reading May 2027)**. The buying reason with the most research support (sp:V7, V3), a proven endpoint at $0.00188 per company per month, and a natural opener ("as the team grows past 50..."). Build: monthly LinkedIn headcount snapshot of the S2 and S3 lookalike list (S06), flag 20%+ growth over 6 months.
2. **S01 HR and payroll hiring, for S2 and S1 (score 10)**. Highest volume of the timing signals and the data is verified (ss:T1, E2). Same build for every segment with title keyword swaps. Filter out global remote employers before sending.
3. **S03 new HR leader, for S2 and S1 (score 9)**. Reaches the champion directly at the moment they are choosing tools; the demo is where deals are decided (sp:V5, V6). Check Nigerian start-date coverage on 20 known companies before scaling, because leadmagic costs $0.075 per call.
4. **S02 first HR hire, for S3 (score 9)**. Same build as S01 plus a headcount filter, so nearly free once S01 exists. Gives the founder angle a clear moment (sp:V1, V7).
5. **S07 new site, for S1 (score 8, test)**. The only signal that sees frontline firms LinkedIn misses, and the cheapest way to answer icp open question 1 (are logistics, retail and manufacturing really core). Run as a small Lagos retail and hospitality test before committing.

- **Apply S10 tax calendar to all five** as the send window and opener in December and January (ss:E1).
- **Next in line**: S09 engagement (needs PaidHR's webinar and event data), S05 funding (as a booster to S04), S08 staff abroad.

## Matrix 3: Workflow tracker

| W # | Status | Workflow name | Mother intent | Segment | Persona | Channel | Clay URL | Copy URL | Total leads |
|---|---|---|---|---|---|---|---|---|---|
| W1 | COPY-APPROVED 2026-11-12, B/D gated, consent and sender open (12-month growth trigger, ss:T6; [spec](../../output/campaigns/growing-past-the-spreadsheet/workflow-spec.md)) | Growing past the spreadsheet | Hypergrowth (headcount), S04 | S2, S3 | CEO / founder, HR lead | unknown | | | |
| W2 | Planned | Hiring HR or payroll | Hiring specific roles, S01 | S2, S1 | HR lead | unknown | | | |
| W3 | Spec approved 2026-11-12, amended same day: 100 days; NG, plus KE and GH gated ([spec](../../output/campaigns/new-hr-leader-first-100-days/workflow-spec.md)) | New HR leader, first 100 days | New leadership, S03 | S2, S1 | HR lead | unknown | | | |
| W4 | Planned | First HR hire | Have / don't have team, S02 | S3 | CEO / founder | unknown | | | |
| W5 | Planned | New site opened (test) | Niche-specific, S07 | S1 | HR lead, Ops lead | unknown | | | |
| W6 | Planned | Engaged with PaidHR | LinkedIn engagement / events, S09 | All | All | unknown | | | |
| W7 | Planned | Funding booster | Fundraising, S05 | S2, S3 | CEO / founder | unknown | | | |
| W8 | Planned | Staff abroad | Hiring offshore, S08 | S2, S3 | CEO / founder, CFO | unknown | | | |

- Other tracker columns from the framework (campaigns, launch date, iterations, bounce) get added when a workflow goes live.

## Open questions

1. Does PaidHR sales agree with the segment priority (S2 first, S1 as a test)? This decides where the first build goes.
2. Which signals preceded recent closed deals? There is no CRM or win data in research (icp open question 6).
3. How much of LinkedIn's Nigerian HR job volume comes from Nigerian-HQ companies? Measure on the first S01 pull.
4. Does Clay / Apollo give usable employee counts for Nigerian frontline firms? Decides whether S1 can be sized at all.
5. Can PaidHR share webinar and event attendee lists for S09?
6. Who sends outbound, and on which channel? Sender is unknown ([facts.md](../messaging/facts.md)).
7. Kenya and Ghana: which signals and data sources work there (Apollo pool sizes, LinkedIn coverage, local tax calendars for an S10 equivalent)? Unknown; nothing tested outside Nigeria. Depends on icp.md open question 10.

## Citation key

- `co:S#`: [company.md](../docs/research/company.md)
- `cu:C#`: [customers.md](../docs/research/customers.md)
- `cp:K#`: [competitors.md](../docs/research/competitors.md)
- `sp:V#`: [social-proof-sources.md](../docs/research/customer-videos/social-proof-sources.md)
- `ss:T#`, `ss:E#`: [signal-source-checks.md](../docs/research/signal-source-checks.md)
- `posts`: [LinkedIn posts JSON](../docs/research/raw/linkedin-posts-getpaidhr-2026-11-11.json)
