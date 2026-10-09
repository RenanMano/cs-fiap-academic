# Merge no estilo Olist com dados fictícios: price e freight_value estão no arquivo de ITENS
import pandas as pd
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

orders = pd.DataFrame({"order_id": ["o1", "o2", "o3", "o4"],
                       "order_status": ["delivered", "shipped", "delivered", "approved"]})
reviews = pd.DataFrame({"order_id": ["o1", "o2", "o3", "o4"], "review_score": [5, 3, 4, 1]})
payments = pd.DataFrame({"order_id": ["o1", "o2", "o3", "o4"],
                         "payment_type": ["credit_card", "boleto", "credit_card", "voucher"],
                         "payment_installments": [1, 1, 3, 2]})
items = pd.DataFrame({"order_id": ["o1", "o2", "o3", "o4"], "order_item_id": [1, 1, 1, 1],
                      "price": [29.90, 149.99, 520.00, 75.50], "freight_value": [8.72, 15.10, 43.30, 12.00]})

df = orders.merge(reviews, on="order_id").merge(payments, on="order_id")
try:
    df[["payment_type", "price"]]
except KeyError as erro:
    print("Sem o arquivo de itens:", erro)

df = df.merge(items, on="order_id")                    # correção: incluir order_items
cols = ["order_status", "payment_type", "review_score", "payment_installments", "price", "freight_value"]
df = df[cols].dropna()
print(df)
print(df["payment_installments"].value_counts().sort_index().to_dict())
faixas = pd.cut(df["price"], bins=[0, 50, 100, 200, 500, 5000],
                labels=["<50", "50-100", "100-200", "200-500", ">500"])
print(faixas.value_counts().sort_index().to_dict())
