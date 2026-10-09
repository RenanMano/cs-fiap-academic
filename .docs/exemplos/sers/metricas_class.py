# Matriz de confusão e métricas de classificação, calculadas à mão
real    = ["unstable", "stable", "unstable", "unstable", "stable", "stable", "unstable", "stable", "unstable", "unstable"]
previsto = ["unstable", "stable", "stable",   "unstable", "unstable", "stable", "unstable", "stable", "unstable", "unstable"]

pares = list(zip(real, previsto))
vp = pares.count(("unstable", "unstable"))   # verdadeiro positivo (instável previsto instável)
vn = pares.count(("stable", "stable"))
fp = pares.count(("stable", "unstable"))     # falso alarme
fn = pares.count(("unstable", "stable"))     # instabilidade não detectada

print("             previsto stable  previsto unstable")
print(f"real stable        {vn:>5}            {fp:>5}")
print(f"real unstable      {fn:>5}            {vp:>5}")
print(f"acurácia = {(vp + vn) / len(pares):.2f}")
print(f"precisão (unstable) = {vp / (vp + fp):.2f}")
print(f"recall (unstable) = {vp / (vp + fn):.2f}")
