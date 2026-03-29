import os, json
from pathlib import Path

CONFIG_PATH = Path.home() / ".fedcontracts" / "config.json"

def load() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text())
    return {}

def save(data: dict):
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(data, indent=2))

def get_api_key() -> str | None:
    return load().get("api_key") or os.environ.get("RAPIDAPI_KEY")
