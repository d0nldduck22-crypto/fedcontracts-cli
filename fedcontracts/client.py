import requests
from .config import get_api_key

RAPIDAPI_HOST = "govspend-us-federal-contracts.p.rapidapi.com"
BASE_URL = "https://" + RAPIDAPI_HOST

def _headers():
    key = get_api_key()
    if not key:
        raise RuntimeError(
            "No API key set. Run: fedcontracts config --api-key YOUR_KEY\n"
            "Get a free key at: https://rapidapi.com/d0nldduck22-crypto/api/govspend-us-federal-contracts"
        )
    return {"X-RapidAPI-Key": key, "X-RapidAPI-Host": RAPIDAPI_HOST}

def search(agency=None, naics=None, date_from=None, date_to=None, min_amount=None, limit=20, offset=0):
    params = {"limit": limit, "offset": offset}
    if agency:      params["agency_code"] = agency
    if naics:       params["naics"] = naics
    if min_amount:  params["min_amount"] = min_amount
    if date_from:   params["date_from"] = date_from
    if date_to:     params["date_to"] = date_to
    resp = requests.get(BASE_URL + "/search", headers=_headers(), params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()

def contracts_by_date(date, limit=20, offset=0):
    params = {"date": date, "limit": limit, "offset": offset}
    resp = requests.get(BASE_URL + "/contracts", headers=_headers(), params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()

def get_contract(award_id: str):
    resp = requests.get(BASE_URL + "/contracts/" + award_id, headers=_headers(), timeout=15)
    resp.raise_for_status()
    return resp.json()

def health():
    resp = requests.get(BASE_URL + "/health", headers=_headers(), timeout=10)
    resp.raise_for_status()
    return resp.json()
