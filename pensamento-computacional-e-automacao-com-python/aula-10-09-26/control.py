from pathlib import Path
import json, csv

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

# Função que recebe o texto da busca e retorna uma lista com os resultados
def read_leads_search(query):
    leads = read_leads() # lista de dicionarios/ lista de leads/ array of dicts
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead['name']} {lead['email']}".lower()
        #print(txt_lead)

        if query.lower() in txt_lead:
            results.append((i, lead))

    return results

# exportar leads como csv
def export_csv():
    """Exporta leads para csv e retorna o caminho do arquivo"""
    path_csv = DATA_DIR / "leads.csv"

    leads = read_leads()
    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, lead[0].keys())
            writer.writeheader()
            for row_dict in leads:
                writer.writerow(row_dict)
        return path_csv
    except PermissionError:
        return None