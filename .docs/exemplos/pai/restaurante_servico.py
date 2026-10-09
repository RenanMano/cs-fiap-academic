# Lógica das function tools do notebook como funções de serviço puras (sem LLM, sem arquivos)
import pandas as pd

cardapio = pd.DataFrame([
    {"item_id": "BURGER01", "nome": "Classic Burger", "preco": 29.90, "disponivel": True},
    {"item_id": "VEGGIE01", "nome": "Veggie Burger", "preco": 31.90, "disponivel": True},
    {"item_id": "FRIES01", "nome": "Batata Frita", "preco": 14.90, "disponivel": True},
    {"item_id": "SODA01", "nome": "Refrigerante Lata", "preco": 7.50, "disponivel": True},
])
pedidos = []   # lista de dicionários (no notebook: pedidos.csv)

def fazer_pedido(user_id, item_id, quantidade, pedido_id):
    if quantidade <= 0:
        return {"ok": False, "message": "A quantidade deve ser positiva."}
    item = cardapio[(cardapio["item_id"] == item_id) & cardapio["disponivel"]]
    if item.empty:
        return {"ok": False, "message": "Item inexistente ou indisponível."}
    row = item.iloc[0]
    pedidos.append({"pedido_id": pedido_id, "user_id": user_id, "item_id": item_id,
                    "quantidade": quantidade, "preco_unitario": float(row["preco"]),
                    "status": "ABERTO"})
    return {"ok": True, "pedido_id": pedido_id, "item": row["nome"], "quantidade": quantidade}

def calcular_total(user_id, pedido_id):
    linhas = [p for p in pedidos if p["pedido_id"] == pedido_id and p["user_id"] == user_id]
    if not linhas:
        return {"ok": False, "message": "Pedido não encontrado."}
    total = sum(p["quantidade"] * p["preco_unitario"] for p in linhas)
    return {"ok": True, "pedido_id": pedido_id, "total": round(total, 2)}

print(fazer_pedido("cliente_001", "VEGGIE01", 2, "PED-0001"))
print(fazer_pedido("cliente_001", "PIZZA99", 1, "PED-0002"))
print(fazer_pedido("cliente_001", "SODA01", 0, "PED-0003"))
print(calcular_total("cliente_001", "PED-0001"))
print(calcular_total("cliente_002", "PED-0001"))   # outro usuário não vê o pedido
