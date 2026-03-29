from rich.table import Table
from rich.console import Console
from rich import box
import csv

console = Console()

def print_contracts(contracts: list, export_path: str | None = None):
    if not contracts:
        console.print("[yellow]No contracts found.[/yellow]")
        return

    if export_path:
        with open(export_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=contracts[0].keys())
            writer.writeheader()
            writer.writerows(contracts)
        console.print(f"[green]Exported {len(contracts)} rows to {export_path}[/green]")
        return

    table = Table(box=box.SIMPLE_HEAD, show_footer=False)
    table.add_column("Agency", style="cyan", max_width=30)
    table.add_column("Recipient", max_width=28)
    table.add_column("Amount", justify="right", style="green")
    table.add_column("NAICS", max_width=20)
    table.add_column("Date")

    for c in contracts:
        amt = c.get("award_amount") or 0
        table.add_row(
            (c.get("awarding_agency") or "")[:30],
            (c.get("recipient_name") or "")[:28],
            f"${amt:,.0f}",
            (c.get("naics_description") or "")[:20],
            c.get("award_date", "")
        )

    console.print(table)
    console.print(f"[dim]{len(contracts)} contract(s) shown[/dim]")

def print_contract(c: dict):
    for key, val in c.items():
        if val is not None:
            console.print(f"  [bold]{key}:[/bold] {val}")
