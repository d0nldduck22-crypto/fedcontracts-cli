from fedcontracts.formatters import print_contracts

def test_empty():
    print_contracts([])

def test_amount_none():
    print_contracts([{
        "awarding_agency": "DOD", "recipient_name": "Test Corp",
        "award_amount": None, "naics_description": "IT Services",
        "award_date": "2026-01-01"
    }])
