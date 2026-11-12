# PaidHR GTM Context OS

## Company

PaidHR (formerly Pade) is a Lagos-based, Nigeria-first HRMS that runs HR, payroll, statutory remittance (PAYE, pension, NHF, NSITF), time and attendance, performance, cross-border payroll and employee financial wellbeing (PaidLife, earned wage access) in one platform. It serves 400+ businesses with 25,000+ employees, has processed ₦119.2bn in salaries in 2026 YTD, and raised a $1.8M seed led by Accion Venture Lab (Jun 2025). Co-founders: Seye Bandele (CEO), Lekan Omotosho (CTO). Sources: [context/docs/research/company.md](context/docs/research/company.md) S1, S2, S4, S12.

## How this folder works

- `.claude/skills/`: one folder per skill, each with a `SKILL.md`. Read when a task matches a skill.
- `context/icp/`: ideal customer profile, buyer personas and signal matrix. Read before any targeting, list building or copy.
- `context/positioning/`: positioning, value proposition and competitors. Read before writing messaging or copy.
- `context/messaging/`: core message, pillars and `facts.md` (the only claims copy may use). Read before writing any copy.
- `context/brand-kit/`: tone of voice, key phrases and visual rules. Read before producing any customer-facing asset.
- `context/docs/`: case study index and research notes with sources. Read when you need to verify or cite a company fact.
- `knowledge-base/playbooks/`: method docs the skills read (workflow anatomy, signal matrix, copy rules, Clay guides). Read before running or designing a workflow.
- `knowledge-base/learnings/`: what worked, what failed and why. Read before planning a new campaign or experiment.
- `meetings/`: call notes and decisions, one file per meeting. Read when you need context on a past decision.
- `inspiration/`: ads and examples from other companies. Read when drafting creative or copy, for style and structure only.
- `output/campaigns/`: campaign strategy, workflow specs and finished assets, one folder per workflow. Read before reusing or iterating on past work.
- `output/outbound/`: outbound sequences, cold emails and LinkedIn messages. Read before writing or iterating on outbound copy.
- `output/social/`: organic social posts and content calendars. Read before drafting social content.
- `output/paid-ads/`: ad copy, creative briefs and campaign setups. Read before writing or iterating on paid ads.
- `output/data/`: lists, enrichment outputs and data exports. Read before building or reusing a list.
- `tools/`: scripts, integrations and tool configs, each with its own README. Read before automating or connecting a system.
- `weekly-priorities/`: one file per ISO week (`YYYY-Www.md`). Read at the start of every session.
- `work-log/`: one file per ISO week, timestamped entries of every change. Read to see recent work; append after every change.

## Rules

1. Cite a source (URL or file path) for every company fact.
2. Never invent numbers. If a figure is unknown, write "unknown" and flag it.
3. No em dashes in any copy.
4. Ask before sending or publishing anything.
5. Log every change in this week's work log (`work-log/YYYY-Www.md`) with a timestamp.

## Tools

- **treg** (CLI at `~/.local/bin/treg`, skill: `.claude/skills/treg`, login: `.treg/config.json`, scoped to this folder via `TREG_CONFIG` in `.claude/settings.local.json`): one gateway to 4,100+ paid data and generation tools (enrichment, SEO, social, ads, web data). Use it for any external or live data. Find with `treg catalog search "<task>"`, check price with `treg catalog get <id>`, run with `treg call <id>`. Prepaid balance: state the price before any call over $0.10 and ask before any batch over $1. Check balance with `treg`. Guide, proven endpoints, wrapper and scripts: `tools/treg/README.md`. Docs: https://treg.to/docs
- **whisper-transcriber-suite** (local clone at `tools/whisper-transcriber-suite`, source: https://github.com/Milomilo777/whisper-transcriber-suite): free, offline transcription of audio and video files on this Mac, no treg spend. Desktop app: `~/Applications/Whisper Transcriber Suite.app`. CLI: `whisper-transcribe <file> --language en --formats txt srt` (writes outputs next to the input file; add `--diarization` for speaker labels). Update: `git -C tools/whisper-transcriber-suite pull` then rerun `bash platform/macos/install.command` from inside it.
