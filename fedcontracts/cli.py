import click
from .client import search, contracts_by_date, get_contract, health
from .config import save
from .formatters import print_contracts, print_contract, console

@click.group()
def main():
    """Search US federal contracts from your terminal.

    Get a free API key at: https://rapidapi.com/d0nldduck22-crypto/api/govspend-us-federal-contracts
    """
    pass

@main.command()
@click.option("--api-key", required=True, help="Your RapidAPI key")
def config(api_key):
    """Store your RapidAPI key locally."""
    save({"api_key": api_key})
    console.print("[green]API key saved to ~/.fedcontracts/config.json[/green]")

@main.command()
@click.option("--agency", default=None, help="Filter by agency code")
@click.option("--naics", default=None, help="Filter by NAICS code")
@click.option("--date-from", default=None, help="Start date YYYY-MM-DD")
@click.option("--date-to", default=None, help="End date YYYY-MM-DD")
@click.option("--min-amount", default=None, type=float, help="Minimum award amount")
@click.option("--limit", default=20, show_default=True, help="Max results")
@click.option("--export", default=None, help="Export to CSV file path")
def search_cmd(agency, naics, date_from, date_to, min_amount, limit, export):
    """Search federal contracts."""
    try:
        result = search(agency=agency, naics=naics, date_from=date_from,
                        date_to=date_to, min_amount=min_amount, limit=limit)
        contracts = result.get("data", [])
        print_contracts(contracts, export_path=export)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise SystemExit(1)

main.add_command(search_cmd, name="search")

@main.command()
@click.argument("date")
@click.option("--limit", default=20, show_default=True)
@click.option("--export", default=None, help="Export to CSV")
def by_date(date, limit, export):
    """Get contracts awarded on a specific date (YYYY-MM-DD)."""
    try:
        result = contracts_by_date(date, limit=limit)
        contracts = result.get("data", [])
        print_contracts(contracts, export_path=export)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise SystemExit(1)

@main.command()
@click.argument("award_id")
def get(award_id):
    """Get details for a single contract by award ID."""
    try:
        print_contract(get_contract(award_id))
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise SystemExit(1)

@main.command()
def status():
    """Check API availability."""
    try:
        result = health()
        console.print(f"[green]API status: {result}[/green]")
    except Exception as e:
        console.print(f"[red]API unreachable: {e}[/red]")
        raise SystemExit(1)
