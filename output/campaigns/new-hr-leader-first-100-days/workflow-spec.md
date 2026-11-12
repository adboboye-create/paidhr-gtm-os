# W3: New HR leader, first 100 days

**Status:** STRUCTURE-APPROVED 2026-11-12 (decisions delegated: user asked Claude to choose the best fit) · amended 2026-11-12: window 90 to 100 days, geography Nigeria to Nigeria, Kenya and Ghana · Kenya and Ghana sending GATED (open item 5) · copy pending

The structure of the outbound workflow that reaches a People or HR leader in their first 100 days at a company with 50 to 500 staff in Nigeria, Kenya or Ghana. Read before writing copy for it (`/campaign-copy` reads this file) or building its table in Clay.
Built with `/build-workflow-spec` from signal S03 and tracker row W3 in [signal-matrix.md](../../../context/icp/signal-matrix.md). No copy in this file yet.

**INFERRED** = not supported by the research files; a hypothesis to test. Source tags are keyed at the bottom.

## 1. Mother Intent (Trigger) [ENGINE]

- **Mother intent**: a People or HR leader joined a company with 50 to 500 staff in Nigeria, Kenya or Ghana in the last 100 days.
- **Catalog match**: New leadership (past 90/180 days), people enrichment filtered by title and start date ([workflow-anatomy.md](../../../knowledge-base/playbooks/workflow-anatomy.md)). 100 days sits inside this catalog window.
- **Why it is a buying moment**: the HR lead is the champion and the demo is where deals are decided (sp:V5, V6). That a new leader reviews tools in the first 100 days is INFERRED.
- **Granularity limit**: Apollo stores start dates by month only (ss:T4), so "100 days" is read as "current role started in the run month or one of the 4 calendar months before it". Example: a run on 1 December looks back to 23 August; the rule keeps every start from August onward, so no start inside 100 days is missed, but August starts can be up to about 122 days old. Accepted trade-off: a missed lead costs more than a slightly older one.

## 2. Inclusion / Exclusion [ICP]

### Include

- **Geo**: company HQ in Nigeria, Kenya or Ghana, and person located in the same country as the company HQ. Nigeria source: [icp.md](../../../context/icp/icp.md). Kenya and Ghana added by user decision 2026-11-12 (icp.md v3 now covers all three as proven vs expansion markets); PaidHR evidence outside Nigeria is thin (icp Not a fit: "no evidence of non-Nigerian entities"; Kenya named as a market in funding coverage, Ghana not named, co:S4, S5). See open item 5.
- **Country field**: `country` = NG / KE / GH, from the organization HQ country. Used for the send gate and the country rules in section 5; not a routing axis.
- **Size**: Apollo estimated employees 50 to 500 (segments S1 frontline and S2 office-based). 20 to 49 is left to W4 (a first HR hire at a founder-run company, sp:V1, V7). Over 500 is S4, parked.
- **Industry**: any. Frontline vs office-based is a router (section 4), not a filter.
- **Government, NGO and foreign-parent subsidiaries**: kept in and labelled, because the research does not support excluding them (icp open question 7). Label field: `org_type_flag`.
- **Trigger titles**: Head of HR, Head of Human Resources, Head of People, Head of People and Culture, HR Manager, Human Resources Manager, Chief People Officer, HR Operations Lead. Titles taken from Nigerian customers on camera (sp:V3 to V6, V9); whether the same titles cover Kenya and Ghana is INFERRED.
- **Trigger event**: current role `start_date` on or after the first day of the month 4 months before the run month (section 1) AND the previous role was at a different company (joined, not promoted).
- **Recipient**: the new HR leader (champion, [personas.md](../../../context/icp/personas.md)). One contact per company. CEO and CFO are not contacted in this workflow.

### Exclude

- **PaidHR customers**: `{{paidhr_customer_domains}}`, list to be supplied by PaidHR; at minimum the named customers in [facts.md](../../../context/messaging/facts.md).
- **Active pipeline**: `{{crm_open_deals}}`, CRM unknown.
- **Competitors and HR-tech, payroll or EOR vendors**: SeamlessHR, Workpay, Deel, Cadana, NotchHR, Salario, roPay, BizEdge, Motherboard, Xceed365HR, SystemSpecs, Sage, PaySpace, Oze, and any company Apollo classifies as HR or payroll software (cp:K1 to K11; icp Not a fit). Kenyan and Ghanaian HR-tech vendors beyond these are not yet researched (unknown).
- **Recruitment, staffing and HR outsourcing firms**: their HR managers are usually recruiters and their headcount includes placed contractors (INFERRED).
- **Non-leadership titles**: HR officer, HR assistant, HR intern, recruiter, talent acquisition, HR business partner (INFERRED: not the payroll owner).
- **Internal promotions**: previous role at the same company.
- **Unverified email**: Apollo `email_status` not `verified` (email is the main channel, section 7).
- **Already contacted**: any Apollo person ID contacted by this workflow before (the monthly pull sees the same person up to 5 times).

## 3. Sources [ENGINE]

- **Trigger pool (free)**: treg `apollo.people.search`: one call per trigger title per country, `organization_locations[]` = Nigeria, Kenya, Ghana (one country per call so `country` is known), `organization_num_employees_ranges[]=50,200` and `201,500`, paged. Returns Apollo person IDs, no contact data. Nigeria pool seen 2026-11-12 for 20 to 500 staff: about 2,260 "HR manager", 700 "Head of HR", 620 "Head of People" (overlapping; deduplicated size unknown). Source: ss:T4. Kenya and Ghana pool sizes: unknown, not yet pulled.
- **New-ID diff (free)**: compare this month's person IDs with last month's stored IDs; only new IDs go to enrichment.
- **Trigger confirmation and contact data**: treg `apollo.people.enrich` by `id`, $0.026 per match. Returns current title, `employment_history` with `start_date`, verified email, LinkedIn URL, organization name, domain, industry, estimated employees. Tested on one Nigerian Head of People: all fields returned. Source: ss:T4. Not yet tested on a Kenyan or Ghanaian record (unknown).
- **HR team count (free)**: treg `apollo.people.search` with `q_organization_domains_list[]=<domain>` and HR titles (HR, human resources, people, payroll, talent).
- **Open roles**: treg `scrapecreators.x.v1-linkedin-company` ($0.00188) on the organization's LinkedIn URL for the company ID, then treg `harvestapi.linkedin.search.jobs` with `companyId` ($0.001). Source: `tools/treg/README.md`.
- **First run cost**: the first month has no previous list to diff, so every pool member must be enriched once. Estimated at the deduplicated pool size x $0.026 (pool size unknown; at 2,500 people that is $65 for Nigeria alone; Kenya and Ghana add an unknown amount). Kenya and Ghana pulls start only after open item 5 clears, so no enrichment money goes on leads that cannot be sent. Ask before running (CLAUDE.md treg rule: batches over $1).
- **Monthly cost after that**: unknown until the first diff; new IDs x $0.026, plus about $0.003 per qualified lead for open roles.

## 4. Signals table [ENGINE]

| # | Signal | Role | How it's read (boolean / count / regex) | Output |
|---|---|---|---|---|
| 1 | New HR leader joined in the last 100 days | trigger | Boolean: current role title matches the trigger title list (regex, case-insensitive) AND `start_date` >= first day of the month 4 months before the run month AND previous `employment_history` organization differs from the current one | `is_new_hr_leader` = true / false |
| 2 | Workforce type | router | Regex on Apollo `organization.industry` against the frontline list: transportation, trucking, logistics, supply chain, warehousing, retail, supermarkets, wholesale, manufacturing, food and beverages, food production, consumer goods, hospitality, restaurants, entertainment, renewables, oil and energy, construction, mining, security, facilities services, apparel, textiles. Match = frontline; no match or empty = office | `workforce_type` = frontline / office |
| 3 | HR team around the new leader | router | Count of Apollo people at the company domain with HR titles, minus the new leader. Clusters: 0 = solo (the only HR person on record); 1+ = team (an existing HR team) | `hr_team_cluster` = solo / team |
| 4 | Hiring now | context-clause | Count of open LinkedIn jobs for the company ID. Cluster: 3+ = hiring wave; 0 to 2 = none | `hiring_wave` = true / false |
| 5 | Tax-year window (Nigeria only) | context-clause | Boolean: `country` = NG AND send date between 1 December and 31 January (Nigerian annual PAYE returns due 31 January, ss:E1). Always false for KE and GH: their filing dates are not researched (unknown) | `tax_window` = true / false |
| 6 | Organization type label | context-clause (label only, never in copy) | Regex on organization name and industry for government, ministry, agency, NGO, foundation, international organization; plus Apollo parent organization outside the company's `country` | `org_type_flag` = standard / public / ngo / foreign_parent |
| 7 | Country | gate | Organization HQ country from the Apollo search call that returned the ID. NG = send; KE, GH = hold until open item 5 clears | `country` = NG / KE / GH |

- **Clusters declared**: signal 3 (0 / 1+), signal 4 (0 to 2 / 3+). No raw count goes to copy.
- **Not used to route**: company size band, previous employer, funding, country. Size changes nothing in the story at 50 to 500; previous employer would need inference about the person; funding is covered by W7; country changes which proof is allowed (section 5 country rules), not the angle.

## 5. Routing matrix WITH angles [ENGINE]

Axis 1, workforce type: 2 values (frontline, office). Axis 2, HR team: 2 values (solo, team). 2 x 2 = 4 cells.

| Cell | Deterministic read | What it tells us (inferred situation) | The angle it earns |
|---|---|---|---|
| **A. Office, solo** | `workforce_type` = office AND `hr_team_cluster` = solo | The company hired its first or only HR leader. Payroll and remittance were probably run by a founder or finance before, as at Cleva and FAMASI (sp:V7, V1). The new leader is setting up the HR function and is about to take payroll over. | Take payroll and PAYE, pension, NHF and NSITF remittance off the setup list from the first payroll run, so the new function starts on people work instead of computation: run payroll on the day, staff get payslips without coming to HR (sp:V3, V6; co:S1). |
| **B. Office, team** | `workforce_type` = office AND `hr_team_cluster` = team | The new leader inherited an HR team and an existing payroll process (a spreadsheet or another provider, sp:V6, V5). They are reviewing how the team works. | A review of the inherited payroll process: approval levels before salaries go out, remittances that land at the statutory bodies with a receipt for each, and one check instead of HR and finance each re-checking every run (sp:V6, V5; co:S1). |
| **C. Frontline, solo** | `workforce_type` = frontline AND `hr_team_cluster` = solo | One HR leader now owns payroll for staff who work shifts or on sites. Attendance, overtime and onboarding records arrive from several places before each payroll run (INFERRED from the module set, co:S1; Sygnite, sp:V10). | Shifts, geo-referenced clock-ins and overtime flow straight into payroll, staff self-onboard and get payslips on their phone, so one HR person can run payroll for a site-based workforce (co:S1, S3; sp:V10, V6). |
| **D. Frontline, team** | `workforce_type` = frontline AND `hr_team_cluster` = team | The new leader inherited an HR team that runs payroll for a large site-based workforce, as at Filmhouse (sp:V5). Errors and delayed salaries reach many staff at once. | Approval workflows that catch last-minute errors before salaries go out, fast disbursement with failed-payment alerts and re-send, and self-generated receipts when a staff member says they were not paid (sp:V5). |

- **Context clauses on every cell**: if `hiring_wave` = true, one line on onboarding many new staff at once (sp:V10). If `tax_window` = true (Nigeria only), one line on the annual PAYE returns due 31 January under the Nigeria Tax Act 2025 (ss:E1). Neither changes the angle.
- **Country rules**: the angles above are written for Nigeria and every proof point comes from Nigerian customers. Cell A names Nigerian remittances (PAYE, pension, NHF, NSITF) and cell B promises receipts from statutory bodies; neither may be sent to KE or GH. For KE and GH, cells A and B need a country version naming that country's statutory deductions, written only after PaidHR confirms it computes and remits them there (open item 5). Cells C and D carry no Nigeria-only claim, but their niche-native defence (remittance proof) is also unproven outside Nigeria, and Workpay (Nairobi) and SeamlessHR (offices in Nairobi and Accra) are local there (cp:K1, K7). Customer names and quotes stay Nigeria-only until a Kenyan or Ghanaian customer is cleared in facts.md.
- **Branch coverage**: all four cells use only fields every qualified lead has (`first_name`, `company_name`, `hr_title`, `start_month`, plus the two routers). `hiring_wave` and `tax_window` lines appear only when true. No cell depends on industry text, previous employer or a count.
- **Niche-native test**: each angle names Nigerian statutory remittance or a module PaidHR evidences with a customer on camera, and each is tied to the new leader's situation (setting up vs inheriting, office vs site-based). A generic HR SaaS could not send them unchanged. Overlap risk: SeamlessHR also serves shift-based teams (cp:K1), so cells C and D must lean on remittance proof and support, not feature claims (facts.md Banned). For KE and GH this test is not yet passed (country rules above).
- **Proof allowed in copy**: only claims in [facts.md](../../../context/messaging/facts.md). Customer names only after the checks listed there.

## 6. Variables contract [ENGINE]

| Variable | Source field | Exists in branches |
|---|---|---|
| `{{first_name}}` | `apollo.people.enrich` person.first_name | A, B, C, D |
| `{{company_name}}` | person.organization.name (cleaned: drop Ltd, Limited, PLC) | A, B, C, D |
| `{{hr_title}}` | person.title (current role) | A, B, C, D |
| `{{start_month}}` | current `employment_history` start_date, formatted as month name (e.g. September) | A, B, C, D |
| `{{workforce_type}}` | signal 2 output; routing only, not printed | A, B, C, D |
| `{{hr_team_cluster}}` | signal 3 output; routing only, not printed | A, B, C, D |
| `{{hiring_wave}}` | signal 4 output; switches the hiring line on | A, B, C, D (line only when true) |
| `{{tax_window}}` | signal 5 output; switches the tax-year line on (NG only) | A, B, C, D (line only when true) |
| `{{country}}` | signal 7 output; send gate and country version of the copy, not printed | A, B, C, D |
| `{{sender_name}}`, `{{sender_title}}` | Unknown: sender not yet decided ([facts.md](../../../context/messaging/facts.md) Sender identity) | A, B, C, D |
| `{{email}}` | person.email, `email_status` = verified | A, B, C, D |
| `{{linkedin_url}}` | person.linkedin_url | A, B, C, D (LinkedIn step skipped if empty) |

- `org_type_flag` is for list review only and never reaches copy.

## 7. Cadence & channel [ENGINE]

- **Periodicity**: monthly, always-on. Run on the first working day of each month; a person stays eligible for 5 monthly runs (the run month plus the 4 before it) but is contacted once (dedupe on Apollo person ID).
- **Channel**: both. Email first (Apollo verified email), then a LinkedIn connection request from the sender. Number of steps and timing are set in `/campaign-copy`.
- **Send window**: December and January runs carry the `tax_window` line for Nigeria only.
- **Country rollout**: Nigeria sends from the first run. Kenya and Ghana are pulled and sent only after open item 5 clears.

## Definition of done

- [x] Mother intent: one sentence, signal-led, matched to the catalog
- [x] Inclusion: ICP box + trigger definition + recipient, tagged [ICP]
- [x] Exclusion: who's out and why
- [x] Sources: trigger + every enrichment
- [x] Signals table: every read deterministic, every role declared
- [x] Count clusters declared for any count that routes
- [x] Routing matrix with the angle column complete (Nigeria; KE and GH versions of A and B pending open item 5)
- [x] Branch coverage checked
- [x] Variables contract complete
- [x] Engine / ICP markers on every section
- [x] Cadence & channel declared

## Open items before launch

1. PaidHR customer domain list and CRM open deals for the exclusions.
2. Sender name, title and LinkedIn account.
3. Approve the first-run enrichment spend (deduplicated pool x $0.026).
4. After the first run: check how many new leaders per month qualify, and whether Apollo's industry field sorts frontline vs office correctly on 20 known companies.
5. Kenya and Ghana gate: PaidHR to confirm (a) it can pay staff of a Kenyan or Ghanaian company through local payroll, not only cross-border, (b) which local statutory deductions it computes and remits there, and (c) any Kenyan or Ghanaian customer that can be named. Then: add the facts to facts.md, write KE and GH versions of cells A and B, run a free Apollo pool count per country, and test `apollo.people.enrich` on one record per country (icp.md open question 10).

## Citation key

- `co:S#`: [company.md](../../../context/docs/research/company.md)
- `cp:K#`: [competitors.md](../../../context/docs/research/competitors.md)
- `sp:V#`: [social-proof-sources.md](../../../context/docs/research/customer-videos/social-proof-sources.md)
- `ss:T#`, `ss:E#`: [signal-source-checks.md](../../../context/docs/research/signal-source-checks.md)
