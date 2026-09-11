from datetime import date

def model_lead(name, email, status):
    return {
        "name": name,
        "email": email,
        "status": status,
        "created": date.today().isoformat()
    }