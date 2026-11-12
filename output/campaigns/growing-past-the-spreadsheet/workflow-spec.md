# W1: Growing past the spreadsheet

**Status:** COPY-APPROVED 2026-11-12 · cells B and D GATED on PaidHR confirming 2026 PAYE bands (open item 1) · not launch-ready: quote consent, sender and exclusion lists open (see Open items)

The structure of the outbound workflow that reaches Nigerian companies with 20 to 500 staff whose LinkedIn headcount grew 20% or more in 12 months. Read before writing copy for it (`/campaign-copy` reads this file) or building its table in Clay.
Built with `/build-workflow-spec` from campaign idea 4 in [campaign-strategy.md](../campaign-strategy.md) and signal S04 / tracker row W1 in [signal-matrix.md](../../../context/icp/signal-matrix.md).

**INFERRED** = not supported by the research files; a hypothesis to test. Source tags are keyed at the bottom.

## What the source test changed

- **Apollo detects the trigger**: 9,159 Nigerian HQ companies with 20 to 500 staff; 99 of 100 tested carry 6, 12 and 24-month growth fields. Source: ss:T6.
- **Threshold moved from 6 to 12 months**: "20%+ in 6 months" matched 0 of 100; "20%+ in 12 months" matched 6. Rough extrapolation about 550 companies, but page 1 may be ordered by relevance, so treat the volume as unknown until the full pull. Source: ss:T6.
- **Growth counts LinkedIn profiles, not payroll staff**: one source counted 116 profiles for Cleva, whose CEO said "almost 20" staff. Copy uses growth bands only, never a staff number. Source: ss:T5, sp:V7.

## 1. Mother Intent (Trigger) [ENGINE]

- **Mother intent**: a Nigerian company with 20 to 500 staff whose LinkedIn headcount grew 20% or more in the last 12 months and is still growing.
- **Catalog match**: Companies in hypergrowth (headcount) ([workflow-anatomy.md](../../../knowledge-base/playbooks/workflow-anatomy.md)).
- **Why it is a buying moment**: the buying reason with the most research support. Cleva: "As we grew it just didn't scale" (sp:V7). MyCoverGenius: "What used to work for a smaller team, it can no longer work for us" (sp:V3).

## 2. Inclusion / Exclusion [ICP]

### Include

- **Company**: Nigerian HQ, 20 to 500 staff, office-based (segments S2 and S3, [icp.md](../../../context/icp/icp.md)). Kenya and Ghana are out of this workflow: approved as Nigeria only, and every angle below relies on Nigerian remittances.
- **Trigger definition**: `twelve_month_growth` >= 0.20 AND `six_month_growth` >= 0.
- **Recipient**: one person per company. 20 to 49 staff: CEO or founder. 50 to 500 staff: the most senior HR or People lead; if Apollo finds none, the CEO or founder ([personas.md](../../../context/icp/personas.md)).

### Exclude

- **Shrinking now**: `six_month_growth` < 0 (grew over the year, cutting now).
- **Frontline sectors**: NAICS starting 11, 21, 23, 31 to 33, 44 to 45, 48 to 49 or 72. LinkedIn undercounts their staff (signal-matrix.md), and ideas 13 and 14 cover them.
- **Not real employers for this pitch**: membership organisations, communities and NGOs (NAICS 813), public administration (92), staffing and HR consultancies (5613, 541612), Apollo records with no `primary_domain`.
- **Competitors**: SeamlessHR, Workpay, Deel, Cadana, NotchHR, Salario, roPay, BizEdge, Motherboard, Xceed365HR, SystemSpecs, Sage, PaySpace (cp:K1 to K11; same list as W3).
- **Existing relationships**: PaidHR customers (`{{paidhr_customer_domains}}`, list needed from PaidHR) and active pipeline (`{{crm_open_deals}}`, CRM unknown).
- **Overlap**: anyone already contacted by W1 or W3. A company whose HR lead started in the last 100 days goes to W3, not W1.
- **No verified email**: Apollo `email_status` not `verified`.

## 3. Sources [ENGINE]

- **Trigger**: treg `apollo.companies.search`, three runs by size band (20 to 49, 50 to 200, 201 to 500) so the band is known without enrichment. Returns growth fields, NAICS codes, domain. About $2.39 for all 92 pages, monthly. Source: ss:T6.
- **Recipient (free)**: treg `apollo.people.search` by domain (up to 1,000 per call) with the W3 HR titles or founder and CEO titles.
- **Email and contact data**: treg `apollo.people.enrich`, $0.026 per contact; about $14 for a first backlog of about 550 companies (volume estimate from one page, see above).
- **Spend gate**: first full run about $17 against a treg balance last seen at $0.76. Ask before any batch over $1 (CLAUDE.md).

## 4. Signals table [ENGINE]

| # | Signal | Role | How it's read (boolean / count / regex) | Output |
|---|---|---|---|---|
| 1 | 12-month headcount growth | trigger | `twelve_month_growth` >= 0.20 | boolean |
| 2 | Still growing | trigger (guard) | `six_month_growth` >= 0 | boolean |
| 3 | Recipient persona | router | Size band 20 to 49 = `founder`. Band 50 to 500 with an HR title found = `hr_lead`. Band 50 to 500 with no HR title found = `founder` | `recipient_persona` = founder / hr_lead |
| 4 | Send window | router | Send date between 1 December and 25 January = `yearend`, else `standard` | `send_window` = yearend / standard |
| 5 | Growth band | context-clause (never routes) | 12-month growth 0.20 to 0.33 / 0.33 to 0.50 / 0.50 to 1.00 / 1.00 or more | `grew_by` = "grew by more than a fifth" / "grew by more than a third" / "grew by more than half" / "at least doubled" |
| 6 | Size band | context-clause (never routes) | Which Apollo band call returned the company | `size_band` = 20 to 49 / 50 to 200 / 201 to 500 |

- **Clusters declared**: growth (signal 5) is banded and never routes. No raw count reaches copy.
- **Not used to route**: growth size (a company up a fifth and one that doubled have the same problem; only one clause changes), industry, funding (W7 / idea 10 booster).

## 5. Routing matrix WITH angles [ENGINE]

Axis 1, recipient persona: 2 values (founder, hr_lead). Axis 2, send window: 2 values (standard, yearend). 2 x 2 = 4 cells.

Data every cell has: `company_name`, recipient `first_name` and `title`, `grew_by`, `size_band`. No cell has a staff count, open roles, office locations, current payroll tool or any company-specific tax data, so no angle depends on them.

| Cell | Deterministic read | What it tells us (inferred situation) | The angle it earns |
|---|---|---|---|
| **A. Founder, standard** | `recipient_persona` = founder AND `send_window` = standard | The company added people this year and has no HR lead on record, so payroll is most likely still run by the founder or finance, as it was at Cleva and FAMASI before PaidHR (sp:V7, V1). Every person added this year added a payslip and a line in four monthly remittances: PAYE, pension, NHF and NSITF. That they still run it by hand rather than on another tool is INFERRED. | **Payroll is still set up for last year's team.** The team grew `{{grew_by}}`; the way payroll and remittance are run did not. Move it to a system that adds each new hire's PAYE, pension, NHF and NSITF automatically, which can start the same day with no onboarding fee (co:S7). Proof: Cleva, a founder-run payroll that "didn't scale" as the company grew, and that could then offer pension (sp:V7). |
| **B. Founder, yearend** | `recipient_persona` = founder AND `send_window` = yearend | The company ends 2026, the first year under the Nigeria Tax Act 2025, with more people than it started with. Annual PAYE returns for everyone paid in 2026 are due 31 January (ss:E1). The founder is pulling a year of payroll records together, including mid-year joiners (INFERRED). | **Start 2027's payroll on a system, not the 2026 spreadsheet.** Year-end is when a growing team's manual payroll is most visible; switching now means every monthly filing in the next hiring year runs automatically. Proof: ₦934M PAYE remitted in 2025 with zero defaults and delays (co:S1, S2). **Limits**: never claim PaidHR files the annual return (unknown). Gated on PaidHR confirming the platform applies the 2026 PAYE bands (campaign-strategy idea 2; only source is a third-party listing, co:S13). |
| **C. HR lead, standard** | `recipient_persona` = hr_lead AND `send_window` = standard | An HR lead exists and the company grew `{{grew_by}}`. The extra payslips, onboarding records and remittances land on HR's monthly payroll run. That the HR team did not grow at the same pace is INFERRED. | **Growth lands on HR's payroll week.** Payroll is the HR job that grows with every hire; take the per-head work out of it: staff onboard themselves and get payslips without coming to HR, approvals catch errors before salaries go out, and each remittance comes with a receipt. Proof: MyCoverGenius runs payroll on the day (sp:V3); Filmhouse approvals "catch the last-minute details" (sp:V5). |
| **D. HR lead, yearend** | `recipient_persona` = hr_lead AND `send_window` = yearend | The HR lead is closing the first Tax Act year with a bigger team and preparing for January joiners (sp:V10 describes the same January moment; Sygnite is "Confirm first" in facts.md, so paraphrase only, never name). | **Go into 2027's hiring on a system before January's joiners arrive.** New hires self-onboard (co:S1; sp:V10), and every monthly remittance has a receipt to show the year was filed. Same limits and gate as cell B. |

- **Context clauses on every cell**: `grew_by` (one clause, banded, never a number); `size_band` only to choose wording such as "team" vs "company", never printed as a number.
- **Branch coverage**: all four cells use only fields every qualified lead has. Gap: a 50 to 500 company where Apollo found no HR title routes to the founder (A or B), but Apollo may simply be missing the HR lead. Cells A and B must not assert "you run payroll yourself"; they assert that payroll did not change while the team did, which holds either way.
- **Niche-native test**: each angle combines this company's own growth band with Nigeria's four monthly remittances (A, C) or the first Tax Act year-end (B, D). A generic HR tool could not send them unchanged. SeamlessHR could send something close (cp:K1), so proof stays on PaidHR's own customers and remittance record, never feature exclusivity (facts.md Banned).
- **Proof allowed in copy**: only claims in [facts.md](../../../context/messaging/facts.md). Cleva, MyCoverGenius and Filmhouse after the standard check (still a customer, consent to quotes). FAMASI and Sygnite are "Confirm first": situation only, no names or quotes.
- **Launch timing**: today is 2026-11-12, so if W1 launches in December the first sends are cells B and D, and both depend on the Tax Act confirmation. If that confirmation is not in by 1 December, run A and C through the window instead.

## 6. Variables contract [ENGINE]

| Variable | Source field | Exists in branches |
|---|---|---|
| `{{first_name}}` | `apollo.people.enrich` person.first_name | A, B, C, D |
| `{{company_name}}` | `apollo.companies.search` organization.name (cleaned: drop Ltd, Limited, PLC) | A, B, C, D |
| `{{recipient_title}}` | person.title (current role) | A, B, C, D |
| `{{grew_by}}` | signal 5 output, from `twelve_month_growth`: "grew by more than a fifth" / "grew by more than a third" / "grew by more than half" / "at least doubled" (verb phrases, amended 2026-11-12 so the copy reads cleanly; meaning unchanged) | A, B, C, D |
| `{{size_band}}` | signal 6 output; picks wording only, never printed as a number | A, B, C, D |
| `{{recipient_persona}}` | signal 3 output; routing only, not printed | A, B, C, D |
| `{{send_window}}` | signal 4 output, from send date; routing only, not printed | A, B, C, D |
| `{{email}}` | person.email, `email_status` = verified | A, B, C, D |
| `{{linkedin_url}}` | person.linkedin_url; stored for reference, not used (email-only channel) | A, B, C, D |
| `{{sender_name}}`, `{{sender_title}}` | Unknown: sender not yet decided ([facts.md](../../../context/messaging/facts.md) Sender identity) | A, B, C, D |

- Raw growth percentages, LinkedIn headcounts and NAICS codes are for list building only and never reach copy (ss:T5: LinkedIn profiles are not payroll staff).
- There is no variable for current payroll tool, open roles, office locations or industry, so copy cannot reference them.

## 7. Cadence & channel [ENGINE]

- **Periodicity**: monthly, always-on. Run on the first working day of each month: full `apollo.companies.search` pull (about $2.39), then free people search and paid enrichment for new qualifying companies only.
- **Dedupe**: one contact per company, contacted once by this workflow (dedupe on `primary_domain`). Growth figures persist for months, so without this the same company would qualify every run.
- **Cell by send date**: the cell is set when the email is sent, not when the company is pulled. A company pulled on 28 November and sent on 2 December goes to B or D.
- **Channel**: email only, 3 emails in one thread (user decision 2026-11-12; LinkedIn steps dropped). Wait days E2 +3, E3 +7 (kit default, confirm).
- **Year-end window**: 1 December to 25 January (leaves time to act before the 31 January PAYE returns, ss:E1). Cells B and D send only after open item 1 clears; until then, A and C run all year.
- **Overlap with W3**: if a company qualifies for both, W3 wins (section 2).

## Definition of done

- [x] Mother intent: one sentence, signal-led, matched to the catalog
- [x] Inclusion: ICP box + trigger definition + recipient, tagged [ICP]
- [x] Exclusion: who's out and why
- [x] Sources: trigger + every enrichment
- [x] Signals table: every read deterministic, every role declared
- [x] Count clusters declared for any count that routes (growth is banded and never routes)
- [x] Routing matrix with the angle column complete (B and D gated on open item 1)
- [x] Branch coverage checked
- [x] Variables contract complete
- [x] Engine / ICP markers on every section
- [x] Cadence & channel declared

## Open items before launch

1. PaidHR to confirm the platform applies the 2026 PAYE bands (gates cells B and D).
2. Quote consent: Cleva, MyCoverGenius, Filmhouse still customers and OK with written quotes.
3. PaidHR customer domain list and CRM open deals for the exclusions.
4. Sender name, title and LinkedIn account (facts.md Sender identity).
5. Top up treg and approve the first-run spend (about $17: $2.39 search pull plus about $14 enrichment).
6. After the first full pull: real qualifying volume (the 550 estimate comes from one page), and spot-check that NAICS exclusions remove the noise seen in ss:T6 (NGOs, staffing firms, law firms).

## Copy

Channel: email only, 3 emails in one thread. Written with `/campaign-copy`. Every claim traces to [facts.md](../../../context/messaging/facts.md). Before sending: confirm Cleva and MyCoverGenius are still customers and consent to the written quotes (facts.md).

### Email 1 (approved 2026-11-12)

**Subject** (static, all cells): {payroll for a bigger team|payroll as the team grows|a bigger payroll}

**Skeleton**

```
{{first_name}},

{{e1l1}}

{{e1l2}}

{{e1l3}}

{{social_proof}}

{{e1cta}}

{{sender_name}}
```

**L1 `{{e1l1}}`** (dynamic by growth band; exhaustive, no fallback)

- + `grew_by` = grew by more than a fifth: On LinkedIn, {{company_name}}'s team grew by more than a fifth over the past year.
- + `grew_by` = grew by more than a third: On LinkedIn, {{company_name}}'s team grew by more than a third over the past year.
- + `grew_by` = grew by more than half: On LinkedIn, {{company_name}}'s team grew by more than half over the past year.
- + `grew_by` = at least doubled: On LinkedIn, {{company_name}}'s team at least doubled over the past year.

**L2, L3, social proof, CTA** (dynamic by cell; exhaustive, no fallback)

- **+ A. Founder, standard**
  - L2: Every new hire adds a payslip and four monthly remittances: PAYE, pension, NHF and NSITF. So payroll probably takes more of someone's month than it did a year ago.
  - L3: PaidHR works out all four for every new hire and remits them each cycle, and you can run your first payroll the same day you sign up.
  - Social proof: Cleva's CEO put it this way: "As you add on more people it starts to get very complicated and cumbersome."
  - CTA: Does that sound like payroll at {{company_name}} right now?
- **+ B. Founder, yearend** (GATED, open item 1)
  - L2: So 2026, the first year under the Nigeria Tax Act, probably closes with a lot more payslips than it opened with. Annual PAYE returns are due 31 January, which usually means pulling a year of payroll together.
  - L3: PaidHR works out PAYE, pension, NHF and NSITF for every hire and remits them each month, so next year's hires go onto a system from day one.
  - Social proof: Last year PaidHR remitted ₦934M in PAYE for customers with zero defaults or delays.
  - CTA: Is changing how payroll runs on the list for 2027?
- **+ C. HR lead, standard**
  - L2: For whoever runs HR, that usually means more payslips, more onboarding and more remittances in the same payroll week.
  - L3: PaidHR lets staff onboard themselves and get their own payslips, runs payroll through approvals, and remits PAYE, pension, NHF and NSITF with a receipt for each.
  - Social proof: MyCoverGenius's Head of People and Culture: "My employees can access their payslip, they don't have to come to me."
  - CTA: Has payroll week grown along with the team?
- **+ D. HR lead, yearend** (GATED, open item 1)
  - L2: With the first Tax Act year closing and January joiners probably on the way, payroll in the next few weeks is likely busier than usual.
  - L3: PaidHR lets new hires onboard themselves and remits PAYE, pension, NHF and NSITF every month with a receipt for each, so 2027 starts on one system.
  - Social proof: Last year PaidHR remitted ₦934M in PAYE for customers with zero defaults or delays.
  - CTA: Are January's joiners going onto the same payroll setup as this year?

Sources: Cleva quote sp:V7 [1:07]; MyCoverGenius quote sp:V3 [13:47]; ₦934M co:S1, S2; same-day start co:S7; remittance, approvals, self-onboarding, payslips co:S1; Tax Act and 31 January ss:E1.

### Email 2 (approved 2026-11-12)

Same thread, +3 days, subject `Re: <E1 subject>`, no PS.

```
{{first_name}},

{{e2l1}}

{{e2l2}}

{{e2l3}}

{{e2cta}}

{{sender_name}}
```

Dynamic by cell; exhaustive, no fallback.

- **+ A. Founder, standard** (new value: pension, easy start)
  - L1: A bigger team also tends to bring up pension.
  - L2: Cleva's CEO said "pension is a big one" for them, and having PaidHR handle the remittance helped them offer it to staff.
  - L3: There's no upfront onboarding fee, so next month's payroll could be the first one on it.
  - CTA: Is pension something you'd like to offer the team?
- **+ B. Founder, yearend** (GATED; new value: receipts, how money is held)
  - L1: When a year of payroll gets pulled together, the slow part is usually finding proof that each month's PAYE and pension actually landed.
  - L2: On PaidHR every remittance comes with a receipt, and the money moves through licensed financial institutions, not a PaidHR account.
  - L3: Cleva's CEO on switching: "The whole tax [and] pension remittance was automated."
  - CTA: Would a sample of those receipts be useful?
- **+ C. HR lead, standard** (new value: approvals, salary queries)
  - L1: More people on payroll also means more ways for one wrong figure to slip through.
  - L2: Filmhouse's HR team says PaidHR's approval levels "catch the last-minute details that could really affect the entire payment or salary for the month."
  - L3: And when someone says they weren't paid, HR can pull the payment receipt themselves.
  - CTA: How are salary queries handled at {{company_name}} today?
- **+ D. HR lead, yearend** (GATED; new value: January onboarding)
  - L1: January joiners mean new records, tax and pension details before their first salary.
  - L2: On PaidHR new hires fill in their own details, and payroll picks them up from there.
  - L3: Cleva's CEO: "I feel relief when I log in, especially when I'm adding new people."
  - CTA: Roughly how many people are you expecting to onboard in January?

Sources: Cleva quotes sp:V7 [4:29, 5:36, 7:48]; Filmhouse approvals and self-generated receipts sp:V5 [0:31, 3:17]; no onboarding fee co:S7; licensed financial institutions, no customer deposits co:S8; self-onboarding co:S1, sp:V10. Filmhouse quote also needs the standard check before sending.

### Email 3 (approved 2026-11-12)

Same thread, +7 days, subject `Re: <E1 subject>`, no PS. Last email.

```
{{first_name}},

{{e3l1}}

{{e3l2}}

{{e3cta}}

{{sender_name}}
```

Dynamic by cell; exhaustive, no fallback. `{{e3l2}}` is empty for A and B.

- **+ A. Founder, standard** (referral; covers the founder-fallback gap in section 5)
  - L1: Last note from me on this.
  - CTA: If payroll and remittance sit with someone else at {{company_name}}, finance or an HR lead, who would be the right person to ask?
- **+ B. Founder, yearend** (GATED; referral)
  - L1: Last note from me before January gets busy.
  - CTA: If someone else at {{company_name}} owns payroll and the year-end PAYE work, who would be the right person to ask?
- **+ C. HR lead, standard** (new value: scale and security)
  - L1: Last note from me on this.
  - L2: PaidHR runs payroll for 400+ businesses and 25,000+ employees, and is ISO 27001 certified.
  - CTA: Is this worth a look this quarter, or better to leave until after January?
- **+ D. HR lead, yearend** (GATED; new value: scale and security)
  - L1: Last note from me before the January joiners arrive.
  - L2: PaidHR runs payroll for 400+ businesses and 25,000+ employees, and is ISO 27001 certified.
  - CTA: Worth a look before then, or better to come back once they're settled in?

Sources: 400+ businesses, 25,000+ employees, ISO 27001 co:S1, S2.

### Assembled sample (cell C, Email 1)

Example values, not a real lead: `first_name` = Adaeze, `company_name` = Northbay, `grew_by` = grew by more than a third. Sender not yet decided.

```
Subject: payroll for a bigger team

Adaeze,

On LinkedIn, Northbay's team grew by more than a third over the past year.

For whoever runs HR, that usually means more payslips, more onboarding and more remittances in the same payroll week.

PaidHR lets staff onboard themselves and get their own payslips, runs payroll through approvals, and remits PAYE, pension, NHF and NSITF with a receipt for each.

MyCoverGenius's Head of People and Culture: "My employees can access their payslip, they don't have to come to me."

Has payroll week grown along with the team?

{{sender_name}}
```

### Before launch (copy)

- Confirm Cleva, MyCoverGenius and Filmhouse are still customers and consent to the written quotes (facts.md).
- Fill `{{sender_name}}` (facts.md Sender identity).
- Cells B and D send only after open item 1 clears; until then A and C run.
- Final manual read against [copy-iron-laws.md](../../../knowledge-base/playbooks/copy-iron-laws.md).

## Citation key

- `co:S#`: [company.md](../../../context/docs/research/company.md)
- `cp:K#`: [competitors.md](../../../context/docs/research/competitors.md)
- `sp:V#`: [social-proof-sources.md](../../../context/docs/research/customer-videos/social-proof-sources.md)
- `ss:T#`, `ss:E#`: [signal-source-checks.md](../../../context/docs/research/signal-source-checks.md)
