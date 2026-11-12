# treg

One gateway to 4,100+ paid data and generation tools (enrichment, LinkedIn, SEO, web scraping, YouTube, job boards). One login, prepaid balance, pay per call. Docs: https://treg.to/docs

## Setup in this project

| Piece | Where | Notes |
|---|---|---|
| CLI binary | `~/.local/bin/treg` (v1.0.0-beta.1) | Machine-wide install; signed out everywhere except this project |
| Login | `.treg/config.json` | Gitignored. Team `ad-s-team` |
| Claude Code scoping | `.claude/settings.local.json` sets `TREG_CONFIG` + telemetry off | Gitignored. Restart Claude Code after changes |
| Skill | `.claude/skills/treg/` (Claude), `.agents/skills/treg/` (Codex etc.) | Project-only |
| Wrapper | [treg.sh](treg.sh) | Use this from any terminal |

**Install on a new machine:** `curl -fsSL https://treg.to/install.sh | sh` (read it first), then sign in for this project only:
`TREG_CONFIG="$PWD/.treg/config.json" ~/.local/bin/treg login`

## Everyday use

```sh
tools/treg/treg.sh balance                          # credit left + recent spend
tools/treg/treg.sh catalog search "<job to do>"     # find an endpoint, shows prices
tools/treg/treg.sh catalog get <id>                 # params + exact price (always before calling)
tools/treg/treg.sh call <id> --query key=value      # run it
```

Quote any URL that contains `?` (zsh treats it as a wildcard): `--query "url=https://www.youtube.com/watch?v=ID"`.

## Spend rules (from CLAUDE.md)

- Check price with `catalog get` before every call.
- State the price before any call over $0.10. Ask before any batch over $1.
- Log spend in the week's work log.
- Prefer free web search and fetch first. Use treg where they fail (blocked pages, LinkedIn, YouTube, structured company data).

## Proven endpoints (used in this project)

Prices from the treg catalog on 2026-11-11.

| Job | Endpoint | Price | Example |
|---|---|---|---|
| LinkedIn company profile (headcount, About, recent posts) | `scrapecreators.x.v1-linkedin-company` | $0.00188/call | `--query url=https://www.linkedin.com/company/getpaidhr` |
| LinkedIn company posts (paginated) | `scrapecreators.x.v1-linkedin-company-posts` | $0.00188/call | `--query url=... --query page=2` |
| LinkedIn job search by company | `harvestapi.linkedin.search.jobs` | ~$0.0005 to $0.001/call | `--query companyId=75031619` (ID from company profile) |
| Render a JS / Cloudflare page | `litescrape.web.fetch.post` | $0.00015/success | `--method POST --data '{"url":"...","respond_with":"html","engine":"browser"}'` |
| YouTube channel video list | `scrapecreators.x.v1-youtube-channel-videos` | $0.00188/page | `--query handle=GetPaidHR` |
| YouTube transcript | `scrapecreators.x.v1-youtube-video-transcript` | $0.00188/call ($0 if cached) | `--query "url=https://www.youtube.com/watch?v=ID"` |

Gotchas found:
- PaidHR's LinkedIn slug is `getpaidhr`, not `paidhr` (404, not charged).
- `mobiusengine-jobs.jobs.company` needs our own provider key; use the harvestapi job search instead.
- LinkedIn post dates from scrapecreators are approximate (converted from "X months ago").

Worth trying next (not yet used): `getleadsio.companies.funding.feed` (free funding feed), `predictleads.financing.discover` ($0.04/result), `treg.companies.enrich` (routed enrichment, variable price).

## Scripts

### [youtube_transcripts.py](youtube_transcripts.py)

```sh
python3 tools/treg/youtube_transcripts.py --channel GetPaidHR --list          # list all channel videos
python3 tools/treg/youtube_transcripts.py ID1 ID2 --out <folder>               # one .md per video
```

Default output: `context/docs/research/customer-videos/transcripts/`. Reuses cached transcripts up to 30 days old at $0 (`--cache-days`, one of 1d, 3d, 7d, 14d, 30d).
