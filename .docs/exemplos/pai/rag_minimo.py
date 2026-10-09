# Pipeline RAG mínimo (sem LLM): fatiar → vetorizar → recuperar → montar o prompt
import math
import re
from collections import Counter

documento = (
    "Horário: segunda a sábado, das 11h às 23h. "
    "Endereço: Rua das Flores, 123, Centro. "
    "Pagamentos: dinheiro, Pix, cartão de débito e crédito. "
    "Entrega: Centro, Jardim América, Vila Nova e Santa Clara. "
    "Pedidos: alterações são aceitas enquanto o pedido estiver com status ABERTO."
)

# 1) Splitting: uma frase por chunk
chunks = [c.strip() for c in documento.split(". ") if c.strip()]

# 2) "Embedding" simplificado: contagem de palavras (saco de palavras)
def vetor(texto):
    return Counter(re.findall(r"\w+", texto.lower()))

def similaridade(a, b):
    comum = sum(a[t] * b[t] for t in a)
    return comum / (math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values())))

indice = [(c, vetor(c)) for c in chunks]          # o "vectorstore"

# 3) Retrieval: os k chunks mais parecidos com a pergunta
pergunta = "Vocês aceitam pagamento com Pix?"
q = vetor(pergunta)
top = sorted(indice, key=lambda par: similaridade(q, par[1]), reverse=True)[:2]
for c, v in top:
    print(f"{similaridade(q, v):.3f} | {c}")

# 4) Augmentation: contexto + pergunta formam o prompt enviado ao LLM
contexto = "\n".join(f"- {c}" for c, _ in top)
prompt = f"Responda usando apenas o contexto.\nContexto:\n{contexto}\nPergunta: {pergunta}"
print("\n" + prompt)
