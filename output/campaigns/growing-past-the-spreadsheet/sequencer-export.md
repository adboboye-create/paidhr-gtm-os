# W1: Growing past the spreadsheet, sequencer export

The tool-neutral sequencer setup for W1: settings, steps, bodies and the value of every custom variable per cell. Read before loading W1 into the email sequencer or building the columns that fill its variables.
Generated 2026-11-12 from the approved copy in [workflow-spec.md](workflow-spec.md) (status COPY-APPROVED 2026-11-12). Regenerate whenever the copy there changes; the spec wins if the two disagree.

**Not launch-ready.** Before loading: quote consent (Cleva, MyCoverGenius, Filmhouse), sender name, exclusion lists, and cells B and D held until PaidHR confirms the 2026 PAYE bands. See the spec's Open items.

## Campaign

- **Campaign name**: W1 Growing past the spreadsheet
- **Tag**: `w1-growth`
- **Sequencer**: unknown (not yet decided). Syntax below is the kit syntax: `{{variable}}` and `{a|b}` spintax. Convert at import (e.g. Instantly: `{{variable}}` and `{{RANDOM|a|b}}`).

## Recommended settings

- Plain text ON, open tracking OFF, ignore out-of-office replies ON.
- Leave the campaign daily cap high; throttle per mailbox.
- **Schedule**: Monday to Friday, 08:00 to 17:00, Africa/Lagos (WAT). Confirm with PaidHR.
- **Cell B and D leads**: load only between 1 December and 25 January, and only after open item 1 clears. Outside that window every lead is A or C.

## Custom variables

One column per variable in the lead upload. Built-ins excluded: `first_name`, `last_name`, `company_name`, `email`, sender signature.

- `e1l1`, `e1l2`, `e1l3`, `social_proof`, `e1cta`
- `e2l1`, `e2l2`, `e2l3`, `e2cta`
- `e3l1`, `e3l2`, `e3cta`
- `sender_name` (unknown until the sender is decided; use the sequencer's sender signature field if it has one)

## Steps

### Step 1 | wait: 0 days | new thread

Subject: {payroll for a bigger team|payroll as the team grows|a bigger payroll}

```
{{first_name}},

{{e1l1}}

{{e1l2}}

{{e1l3}}

{{social_proof}}

{{e1cta}}

{{sender_name}}
```

### Step 2 | wait: 3 days | same thread (subject "Re: <step 1 subject>")

```
{{first_name}},

{{e2l1}}

{{e2l2}}

{{e2l3}}

{{e2cta}}

{{sender_name}}
```

### Step 3 | wait: 7 days | same thread (subject "Re: <step 1 subject>")

```
{{first_name}},

{{e3l1}}

{{e3l2}}

{{e3cta}}

{{sender_name}}
```

- Cells A and B have no third line in this step: fill `e3l2` with the CTA and leave `e3cta` empty. Check in the sequencer preview that the empty variable leaves no stray blank line; if it does, remove the `{{e3cta}}` line for an A/B-only copy of step 3.

## Variable values

Fill per lead from `grew_by` (for `e1l1`) and the cell (for everything else). `{{company_name}}` inside a value is resolved by the data tool before upload. No spintax inside any value.

### e1l1 (by `grew_by`)

- grew by more than a fifth: On LinkedIn, {{company_name}}'s team grew by more than a fifth over the past year.
- grew by more than a third: On LinkedIn, {{company_name}}'s team grew by more than a third over the past year.
- grew by more than half: On LinkedIn, {{company_name}}'s team grew by more than half over the past year.
- at least doubled: On LinkedIn, {{company_name}}'s team at least doubled over the past year.

### Cell A: `recipient_persona` = founder, `send_window` = standard

- e1l2: Every new hire adds a payslip and four monthly remittances: PAYE, pension, NHF and NSITF. So payroll probably takes more of someone's month than it did a year ago.
- e1l3: PaidHR works out all four for every new hire and remits them each cycle, and you can run your first payroll the same day you sign up.
- social_proof: Cleva's CEO put it this way: "As you add on more people it starts to get very complicated and cumbersome."
- e1cta: Does that sound like payroll at {{company_name}} right now?
- e2l1: A bigger team also tends to bring up pension.
- e2l2: Cleva's CEO said "pension is a big one" for them, and having PaidHR handle the remittance helped them offer it to staff.
- e2l3: There's no upfront onboarding fee, so next month's payroll could be the first one on it.
- e2cta: Is pension something you'd like to offer the team?
- e3l1: Last note from me on this.
- e3l2: If payroll and remittance sit with someone else at {{company_name}}, finance or an HR lead, who would be the right person to ask?
- e3cta: (empty)

### Cell B: `recipient_persona` = founder, `send_window` = yearend (GATED)

- e1l2: So 2026, the first year under the Nigeria Tax Act, probably closes with a lot more payslips than it opened with. Annual PAYE returns are due 31 January, which usually means pulling a year of payroll together.
- e1l3: PaidHR works out PAYE, pension, NHF and NSITF for every hire and remits them each month, so next year's hires go onto a system from day one.
- social_proof: Last year PaidHR remitted ₦934M in PAYE for customers with zero defaults or delays.
- e1cta: Is changing how payroll runs on the list for 2027?
- e2l1: When a year of payroll gets pulled together, the slow part is usually finding proof that each month's PAYE and pension actually landed.
- e2l2: On PaidHR every remittance comes with a receipt, and the money moves through licensed financial institutions, not a PaidHR account.
- e2l3: Cleva's CEO on switching: "The whole tax [and] pension remittance was automated."
- e2cta: Would a sample of those receipts be useful?
- e3l1: Last note from me before January gets busy.
- e3l2: If someone else at {{company_name}} owns payroll and the year-end PAYE work, who would be the right person to ask?
- e3cta: (empty)

### Cell C: `recipient_persona` = hr_lead, `send_window` = standard

- e1l2: For whoever runs HR, that usually means more payslips, more onboarding and more remittances in the same payroll week.
- e1l3: PaidHR lets staff onboard themselves and get their own payslips, runs payroll through approvals, and remits PAYE, pension, NHF and NSITF with a receipt for each.
- social_proof: MyCoverGenius's Head of People and Culture: "My employees can access their payslip, they don't have to come to me."
- e1cta: Has payroll week grown along with the team?
- e2l1: More people on payroll also means more ways for one wrong figure to slip through.
- e2l2: Filmhouse's HR team says PaidHR's approval levels "catch the last-minute details that could really affect the entire payment or salary for the month."
- e2l3: And when someone says they weren't paid, HR can pull the payment receipt themselves.
- e2cta: How are salary queries handled at {{company_name}} today?
- e3l1: Last note from me on this.
- e3l2: PaidHR runs payroll for 400+ businesses and 25,000+ employees, and is ISO 27001 certified.
- e3cta: Is this worth a look this quarter, or better to leave until after January?

### Cell D: `recipient_persona` = hr_lead, `send_window` = yearend (GATED)

- e1l2: With the first Tax Act year closing and January joiners probably on the way, payroll in the next few weeks is likely busier than usual.
- e1l3: PaidHR lets new hires onboard themselves and remits PAYE, pension, NHF and NSITF every month with a receipt for each, so 2027 starts on one system.
- social_proof: Last year PaidHR remitted ₦934M in PAYE for customers with zero defaults or delays.
- e1cta: Are January's joiners going onto the same payroll setup as this year?
- e2l1: January joiners mean new records, tax and pension details before their first salary.
- e2l2: On PaidHR new hires fill in their own details, and payroll picks them up from there.
- e2l3: Cleva's CEO: "I feel relief when I log in, especially when I'm adding new people."
- e2cta: Roughly how many people are you expecting to onboard in January?
- e3l1: Last note from me before the January joiners arrive.
- e3l2: PaidHR runs payroll for 400+ businesses and 25,000+ employees, and is ISO 27001 certified.
- e3cta: Worth a look before then, or better to come back once they're settled in?

## Cell assignment

- The cell is set by the send date of step 1, not the pull date (spec section 7). A lead whose sequence starts on or after 1 December and on or before 25 January is B or D; otherwise A or C.
- A sequence that starts in the standard window keeps its A or C copy for steps 2 and 3, even if they land after 1 December.
