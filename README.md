# fedcontracts-cli

Search US federal contracts from your terminal.

## Install

```bash
pip install fedcontracts-cli
```

## Setup

Get a free API key at [RapidAPI](https://rapidapi.com/d0nldduck22-crypto/api/govspend-us-federal-contracts) (50 requests/day free).

```bash
fedcontracts config --api-key YOUR_RAPIDAPI_KEY
```

## Usage

```bash
fedcontracts search                                    # keyword search
fedcontracts search --naics 541511 --min-amount 1000000
fedcontracts search --date-from 2026-03-01 --date-to 2026-03-28
fedcontracts search --agency 097 --export dod.csv
fedcontracts by-date 2026-03-24                        # all contracts on a date
fedcontracts get AWARD_ID                              # single contract detail
fedcontracts status                                    # API health check
```

## Data source

US federal contract awards via [USASpending.gov](https://usaspending.gov).
Updated nightly. Powered by the GovSpend API on [govspendapi.com](https://govspendapi.com).
