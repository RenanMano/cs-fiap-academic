import csv, json, tempfile
from pathlib import Path

# mesma lógica de control.py, apontando para uma pasta temporária
DATA_DIR = Path(tempfile.mkdtemp()) / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

def read_leads():
    if not DB_PATH.exists():
        return []
    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:                  # arquivo corrompido: recomeça com lista vazia
        return []

def create_lead(lead):
    leads = read_leads()
    leads.append(lead)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

def read_leads_search(query):
    return [(i, l) for i, l in enumerate(read_leads()) if query.lower() in f"{l['name']} {l['email']}".lower()]

def export_csv():
    leads = read_leads()
    if not leads:                                 # sem leads não há cabeçalho para escrever
        return None
    path_csv = DATA_DIR / "leads.csv"
    with path_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, leads[0].keys())   # o original usa lead[0] (NameError)
        writer.writeheader()
        writer.writerows(leads)
    return path_csv

print("vazio:", read_leads(), "| export:", export_csv())
create_lead({"name": "Ana", "email": "ana@exemplo.com", "status": "novo", "created": "2026-09-10"})
create_lead({"name": "Bruno", "email": "bruno@exemplo.com", "status": "contato", "created": "2026-09-10"})
print(f"## | {'Nome':<10} | E-mail")
for i, lead in enumerate(read_leads()):
    print(f"{i:02d} | {lead['name']:<10} | {lead['email']}")
print("busca 'bru':", read_leads_search("bru"))
print(export_csv().read_text(encoding="utf-8"), end="")
DB_PATH.write_text("{ isto não é JSON", encoding="utf-8")
print("JSON corrompido ->", read_leads())
