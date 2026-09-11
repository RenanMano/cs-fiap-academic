from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

# CRUD
# CREATE
# READ
# UPDATE
# DELETE

# READ
def read_leads():
    if not DB_PATH.exists():
        return[]

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return[]

# CREATE
def create_lead(lead_dict):
    leads = read_leads()
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")