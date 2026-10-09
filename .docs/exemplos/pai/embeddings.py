# Embeddings de brinquedo: cada palavra vira um vetor; direções codificam significado
import numpy as np

# dimensões (escolhidas à mão para ilustrar): [realeza, masculino, pessoa, fruta]
vetores = {
    "rei":    np.array([0.9,  0.9, 1.0, 0.0]),
    "rainha": np.array([0.9, -0.9, 1.0, 0.0]),
    "homem":  np.array([0.0,  0.9, 1.0, 0.0]),
    "mulher": np.array([0.0, -0.9, 1.0, 0.0]),
    "maçã":   np.array([0.0,  0.0, 0.0, 1.0]),
}

def cosseno(u, v):
    return u @ v / (np.linalg.norm(u) * np.linalg.norm(v))

alvo = vetores["rei"] - vetores["rainha"] + vetores["mulher"]   # rei − rainha + mulher
ranking = sorted(vetores, key=lambda p: cosseno(alvo, vetores[p]), reverse=True)
print("rei - rainha + mulher ≈", ranking[0])
for p in ranking:
    print(f"  {p:<7} similaridade = {cosseno(alvo, vetores[p]):+.3f}")
