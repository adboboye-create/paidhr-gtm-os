# W3: New HR leader, first 100 days, sequencer export

The tool-neutral sequencer setup for W3: settings, steps, bodies and the value of every custom variable per cell. Read before loading W3 into the email sequencer or building the columns that fill its variables.
Generated 2026-11-12 from the approved copy in [workflow-spec.md](workflow-spec.md) (status COPY-APPROVED 2026-11-12, Nigeria only). Regenerate whenever the copy there changes; the spec wins if the two disagree.

**Not launch-ready.** Before loading: sender name and mailbox, customer name checks (Cleva, MyCoverGenius, Filmhouse Group; Sygnite "confirm first"), exclusion lists (PaidHR customers, open deals), first-run enrichment spend. See "Before launch" in the spec.

**Email only.** The LinkedIn steps (empty connection request, DM 1, DM 2) are in the spec and go into the LinkedIn tool, not this export.

## Campaign

- **Campaign name**: W3 New HR leader, first 100 days (NG)
- **Tag**: `w3-new-hr-leader`
- **Sequencer**: unknown (not yet decided). Syntax below is the kit syntax: `{{variable}}` and `{a|b}` spintax. Convert at import (e.g. Instantly: `{{variable}}` and `{{RANDOM|a|b}}`).

## Recommended settings

- Plain text ON, open tracking OFF, ignore out-of-office replies ON.
- Leave the campaign daily cap high; throttle per mailbox.
- **Schedule**: Monday to Friday, 08:00 to 17:00, Africa/Lagos (WAT). Confirm with PaidHR.
- **Country**: load only leads with `country` = NG. KE and GH leads are held until the spec's open item 5 clears.
- **Pause rule**: a reply on email or LinkedIn stops both channels for that lead.

## Custom variables

One column per variable in the lead upload. Built-ins excluded: `first_name`, `last_name`, `company_name`, `email`, sender signature.

- `e1l1`, `e1l2`, `e1l3`, `e1l4`, `social_proof`, `e2l1`, `e2l2`, `e3l2`
- **`company_name`** must hold the cleaned name (no Ltd, Limited, PLC), because it appears in subjects and CTAs.
- **`e1l3` and `e2l2` are optional lines.** When they fire, the value ends with two line breaks (a blank line after the sentence). When they don't, the value is empty. The body templates below place them directly in front of the next line, so an empty value leaves no gap.
- The data tool resolves `{{company_name}}` and `{{start_month}}` inside every variable value before upload. No variable value contains spintax.

## Steps

### Step 1 | wait: 0 days | new thread

Subject: `{payroll at {{company_name}}|{{company_name}} payroll|your first payroll run}`

Body:
```
{{first_name}},

{{e1l1}}

{{e1l2}}

{{e1l3}}{{e1l4}}

{{social_proof}}

{Has payroll landed with you yet|Is payroll already on your plate}?

{Best,|Thanks,}
{{sender_signature}}
```

### Step 2 | wait: 3 days | same thread (subject "Re: <step 1 subject>")

Body:
```
{{first_name}},

{{e2l1}}

{{e2l2}}{Worth showing you how that would look for {{company_name}}?|Would a short walkthrough before {{company_name}}'s next payroll run help?}

{{sender_signature}}
```

### Step 3 | wait: 7 days | same thread (subject "Re: <step 1 subject>")

Body:
```
{{first_name}},

{Last note from me on this|I'll leave it here after this one}: PaidHR is ISO 27001 certified, holds no customer deposits and works with licensed financial institutions.

{{e3l2}}

{{sender_signature}}
```

## Variable values

### Optional lines (any cell)

**`e1l3`** (first match wins):
- `tax_window` = true: `And 2026 is the first year under the Nigeria Tax Act, with annual PAYE returns due by 31 January.` + two line breaks
- `hiring_wave` = true AND `tax_window` = false: `And with {{company_name}} hiring for several roles right now, there's probably a round of onboarding coming too.` + two line breaks
- otherwise: empty

**`e2l2`**:
- `hiring_wave` = true AND cell is A, B or D: `With several roles open at {{company_name}}, new joiners can fill in their own details instead of HR keying them in.` + two line breaks
- otherwise: empty

### Cell A: `workforce_type` = office, `hr_team_cluster` = solo

- `e1l1`: My guess is you're setting up HR at {{company_name}} more or less from scratch since joining in {{start_month}}.
- `e1l2`: If a founder or finance ran payroll before you arrived, it's probably landing on your desk about now.
- `e1l4`: PaidHR runs payroll and remits PAYE, pension, NHF and NSITF every cycle, and staff get their own payslips without coming to HR.
- `social_proof`: Cleva's CEO ran payroll on one big spreadsheet until it stopped scaling, and now tax and pension run automatically.
- `e2l1`: One thing that helps when you're setting HR up: you can sign up, onboard and run the first payroll in PaidHR on the same day, with no upfront onboarding fee.
- `e3l2`: If payroll still sits with finance or a founder at {{company_name}}, who would be best to speak to?

### Cell B: `workforce_type` = office, `hr_team_cluster` = team

- `e1l1`: Since you joined {{company_name}} in {{start_month}}, I imagine you've been getting to know how the team runs payroll.
- `e1l2`: Taking over a process someone else set up usually means checking each run twice until you trust it.
- `e1l4`: PaidHR puts approval levels in front of every payroll run and remits PAYE, pension, NHF and NSITF with a receipt for each payment.
- `social_proof`: At MyCoverGenius, the Head of People now runs payroll on the day it's due, with no prep in the weeks before.
- `e2l1`: On the remittance side, PaidHR remitted ₦934M in PAYE and ₦754M in pension for its customers in 2025, with zero defaults or delays.
- `e3l2`: Is someone on your team closer to payroll who I should speak to instead?

### Cell C: `workforce_type` = frontline, `hr_team_cluster` = solo

- `e1l1`: Joining {{company_name}} in {{start_month}} probably made you the person who pays everyone across shifts and sites.
- `e1l2`: That probably means gathering attendance, overtime and new-joiner details from each site before every run.
- `e1l4`: In PaidHR, shifts, clock-ins and overtime flow straight into payroll, and new staff onboard themselves.
- `social_proof`: At Sygnite, a solar engineering firm, new staff now fill in their own details instead of HR keying them in. **If the Sygnite check fails: leave `social_proof` empty and remove its line from the Step 1 body for cell C leads, or load cell C as a separate campaign.**
- `e2l1`: Staff on shifts can also pull their own payslips in PaidHR, so those requests stop coming to you.
- `e3l2`: If payroll still sits with finance or a founder at {{company_name}}, who would be best to speak to?

### Cell D: `workforce_type` = frontline, `hr_team_cluster` = team

- `e1l1`: Could be off, but since joining {{company_name}} in {{start_month}} you're likely learning how your team pays people across every shift and site.
- `e1l2`: With that many staff, one wrong figure or late payment reaches a lot of people at once.
- `e1l4`: PaidHR flags failed salary payments so you can re-send them, and lets HR pull a payment receipt the moment someone says they weren't paid.
- `social_proof`: Filmhouse Group's HR team uses the approval steps to catch last-minute details before salaries go out.
- `e2l1`: For a workforce that size, the remittance record matters too: ₦934M in PAYE and ₦754M in pension went through PaidHR in 2025, with zero defaults or delays.
- `e3l2`: Is someone on your team closer to payroll who I should speak to instead?

## Cell assignment

Each lead gets exactly one cell from two columns the data tool fills (spec section 4):

- `workforce_type`: frontline if Apollo `organization.industry` matches the frontline list in the spec, otherwise office.
- `hr_team_cluster`: solo if no other HR-titled person is on record at the company domain, otherwise team.
- office + solo = A; office + team = B; frontline + solo = C; frontline + team = D.
- `tax_window` is true only for NG leads sent between 1 December and 31 January; `hiring_wave` is true when the company has 3+ open LinkedIn jobs.
