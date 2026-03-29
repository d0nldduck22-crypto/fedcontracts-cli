# fedcontracts-cli

Search US federal contract awards from your terminal. Data sourced from [USASpending.gov](https://usaspending.gov), updated nightly.

[![PyPI version](https://img.shields.io/pypi/v/fedcontracts-cli)](https://pypi.org/project/fedcontracts-cli/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Install

```bash
pip install fedcontracts-cli
```

## Setup

Get a free API key at [RapidAPI](https://rapidapi.com/d0nldduck22-crypto/api/govspend-us-federal-contracts) (free tier: 100 requests/month).

```bash
fedcontracts config --api-key YOUR_RAPIDAPI_KEY
```

## Usage

```bash
# Keyword search
fedcontracts search --query "cybersecurity"

# Filter by NAICS code and minimum award amount
fedcontracts search --naics 541511 --min-amount 1000000

# Filter by date range
fedcontracts search --date-from 2026-03-01 --date-to 2026-03-28

# Filter by awarding agency, export to CSV
fedcontracts search --agency 097 --export dod.csv

# All contracts awarded on a specific date
fedcontracts by-date 2026-03-24

# Full detail for a single award
fedcontracts get AWARD_ID

# API health check
fedcontracts status
```

## Use Cases

- **GovCon lead generation** — Find new contract awards by agency, NAICS code, or dollar threshold
- **Competitive intelligence** — Track which vendors are winning contracts in your space
- **Journalism & research** — Query federal spending data without navigating USASpending.gov manually
- **Dashboards & integrations** — Pipe contract data into spreadsheets, databases, or BI tools

## API

This CLI is powered by the [GovSpend API](https://govspendapi.com), also available directly on [RapidAPI](https://rapidapi.com/d0nldduck22-crypto/api/govspend-us-federal-contracts).

| Endpoint | Description |
|----------|-------------|
| `GET /contracts` | List contracts with filters (agency, date, amount, NAICS) |
| `GET /contracts/{award_id}` | Full detail for a single award |
| `GET /search` | Full-text keyword search across descriptions |
| `GET /naics` | Browse NAICS industry codes |
| `GET /agencies` | List all federal awarding agencies |
| `GET /health` | API status and data freshness |

## License

MIT
