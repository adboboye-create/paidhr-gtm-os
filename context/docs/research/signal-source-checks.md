# PaidHR: Signal data source checks (raw research)

Tests of the data sources behind the signal matrix: what was called, what came back, what it cost. Read when you need to verify a data source or volume figure cited in [signal-matrix.md](../../icp/signal-matrix.md).
v1, 2026-11-12. Total treg spend for these checks: about $0.12.

## LinkedIn job search, Nigeria, posted in the last month

- **Tool**: treg `harvestapi.linkedin.search.jobs`, $0.001/call, params `search=<title>`, `location=Nigeria`, `postedLimit=month`. Source: T1.
- **"payroll"**: 49 results. Source: T1.
- **"HR manager"**: 20 results. Source: T1.
- **"Head of People"**: 11 results. Source: T1.
- **"Human Resources"**: 9 results. Source: T1.
- **"HR generalist"**: 7 results. Source: T1.
- **"Chief Financial Officer"**: 5 results. Source: T1.
- **Quality note**: many results are global or remote employers (Tether.io, MailerLite, Canonical, ReliefWeb, Celebrity Cruises), not Nigerian companies. Nigerian names seen: FAMAD PLC, Viju Industries (Nigeria) Limited, Sporty Group, Worknigeria. Volume of real Nigerian employers is lower than the counts above; exact share unknown. Source: T1.
- **Search matches job title only**, not the job description. Source: T1 (endpoint params).

## MyJobMag (Nigerian job board)

- **Exists and lists payroll and HR roles by title**, with employer name, city and salary range, e.g. Payroll Officer at PPC Limited, Lagos; Payroll Supervisor at CIG Motor Ltd. Source: E2.
- **Volume**: pages say "over 18" vacancies per payroll title, which looks like a template figure; some title pages run to 10+ pages. Real monthly volume unknown. Source: E2.
- **Access**: no treg endpoint for MyJobMag or Jobberman. Would need a scrape (crawl4ai, `tools/crawl4ai/`) or Clay HTTP. Not tested. Source: T2.

## Google Maps (physical locations)

- **Tool**: treg `crawl4ai.google.serp.maps`, $0.00023/success. Source: T3.
- **Test "supermarket Lagos Nigeria"**: returned named Lagos businesses with address and category: Renee Supermarket, Grand Square Supermarket and Stores, SPAR Market Ikoyi, Prince Ebeano Supermarket Lekki, Daytona 24/7 Supermarket, Delis Delicatessen. Source: T3.
- **Implication**: counting locations per brand, and changes over time, is possible. Employee counts are not returned. Source: T3.

## Apollo company search with headcount growth (test 2026-11-12)

- **Tool**: treg `apollo.companies.search`, $0.026 per page of up to 100 companies (charged per page, not per company). Params `organization_locations[]=Nigeria`, `organization_num_employees_ranges[]=20,500`, `per_page=100`. Source: T6.
- **Base size**: 9,159 Nigerian HQ companies with 20 to 500 staff, 92 pages, so a full pull costs about $2.39. Source: T6.
- **Fields returned per company**: `organization_headcount_six_month_growth`, `twelve_month_growth`, `twenty_four_month_growth`, `naics_codes`, `primary_domain`, `linkedin_url`, `founded_year`. Not returned: employee count, industry label. Source: T6.
- **Fill rate (page 1, 100 companies)**: 99 of 100 have all three growth fields and NAICS codes. Source: T6.
- **6-month growth spread**: below 0%: 26; 0 to 10%: 71; 10 to 20%: 2; 20%+: 0. So the signal matrix's "20%+ in 6 months" finds almost nothing. Source: T6.
- **12-month growth spread**: below 0%: 25; 0 to 10%: 53; 10 to 20%: 15; 20 to 50%: 6; 50%+: 0. Source: T6.
- **24-month growth spread**: below 0%: 23; 0 to 10%: 30; 10 to 20%: 16; 20 to 50%: 20; 50%+: 10. Source: T6.
- **Noise among top growers**: communities and NGOs (She Code Africa, Remote WorkHER, UNDP Nigeria), staffing and HR consultancies (HRLeverage), law firms, an oil producer. NAICS codes separate most of these. Page 1 may be ordered by Apollo relevance, so the shares above may not hold across all 92 pages. Source: T6.
- **Caveat**: growth is computed from LinkedIn profiles, not payroll. companyenrich counted 116 LinkedIn profiles for Cleva while its CEO said "almost 20" staff (T5, sp:V7). Treat growth as direction, not as an exact staff count. Source: T5, T6.

## Company registry (CAC)

- **treg `corpoapi.companies.registry.search`**: refused, no corpoapi credential in this org. Nigerian coverage not confirmed. Source: T2.

## Other treg endpoints found (not called)

- **Job change**: `leadmagic.x.job-change-detector`, $0.075/call; `lusha.x.contacts-signals`, $0.125/result. Source: T2.
- **Funding**: `aviato.companies.funding_rounds`, $0.01/success; `predictleads.companies.financing_events`, $0.04/call. Source: T2.
- **LinkedIn company headcount**: `scrapecreators.x.v1-linkedin-company`, $0.00188/call (proven, see `tools/treg/README.md`). Source: T2.

## Nigeria Tax Act 2025

- **In force 1 January 2026**, replacing PITA. New PAYE bands (0% on first ₦800,000, then 15% to 25%), CRA replaced by rent relief, old minimum tax removed, bonuses and 13th month added to PAYE base, gratuity taxed, NHF changes. Source: E1.
- **Remittance**: deduct and remit to the State IRS within ten days after month end; annual PAYE returns due 31 January. Source: E1.
- **Penalties**: unremitted tax plus penalties and interest; states get more audit control under the Personal Income Tax (Amendment) Act 2025. Source: E1.

## Apollo: HR leaders and start dates (for W3)

- **Free search**: treg `apollo.people.search`, one title per call (repeating `person_titles[]` keeps only the last value). Nigerian HQ companies, 20-49 / 50-200 / 201-500 staff: "HR manager" 887 / 913 / 459; "Head of HR" 256 / 317 / 130; "Head of People" 224 / 286 / 113; "HR business partner" 66 / 151 / 107. Titles match loosely and overlap; "people operations" matched too broadly (1,474 / 1,475 / 830). Source: T4.
- **Enrich**: treg `apollo.people.enrich` by Apollo `id`, $0.026 per match. One Head of People at a 180-staff Nigerian trucking company returned: verified email, LinkedIn URL, org size and industry, and `employment_history` with start dates by month (current role from 2024-09-01; previous HR role 2022-06 to 2024-08). Source: T4.

## Headcount history (for W1)

- **companyenrich `companies.workforce`** ($0.049): Cleva history monthly from 2023-03 to 2026-03; latest month 2026-03 (8 months old on 2026-11-12). Observed count 116 to 117 from Oct 2025, while Cleva's CEO said "almost 20" staff on camera around Nov 2025 (sp:V7); 58 profiles counted as marketing. Counts LinkedIn profiles, not payroll staff. Source: T5.
- **fiber-ai `linkedin.company.profile`** with history ($0.04): PaidHR page 58 employees; only 2 snapshots (2026-07-24, 2026-07-28), so every growth period reads 0%. Source: T5.
- **Implication**: no tested source gives fresh 6-month headcount growth for Nigerian companies today. Source: T5.

## Sources

- `E1`: KPMG flash alert https://kpmg.com/xx/en/our-insights/gms-flash-alert/flash-alert-2025-168.html ; DLA Piper Africa, FAQs on payroll taxes and employer liability (2026) https://www.dlapiperafrica.com/en/nigeria/insights/2026/FAQs-on-payroll-taxes-and-employer-liability ; Metricsuite, Nigeria PAYE tax changes 2026 https://metricsuite.tools/nigeria-paye-tax-changes-2026/ (via web search summaries, 2026-11-12)
- `E2`: MyJobMag payroll title pages, e.g. https://www.myjobmag.com/jobs-by-title/payroll and https://www.myjobmag.com/jobs-by-title/hr-payroll (via web search summaries, 2026-11-12)
- `T1`: treg calls `harvestapi.linkedin.search.jobs`, 6 calls, 2026-11-12
- `T2`: treg catalog lookups, 2026-11-12 (free)
- `T3`: treg call `crawl4ai.google.serp.maps`, 1 call, 2026-11-12
- `T4`: treg calls `apollo.people.search` (free, about 25 calls) and `apollo.people.enrich` (1 call, $0.026), 2026-11-12
- `T6`: treg call `apollo.companies.search` (1 page, $0.026), 2026-11-12
- `T5`: treg calls `companyenrich.companies.workforce` (1 call, $0.049) and `fiber-ai.linkedin.company.profile` (2 calls, about $0.04), 2026-11-12
