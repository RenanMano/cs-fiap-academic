endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500],
]

def sucesso(codigo):
    return 200 <= codigo <= 299

def analisar(codigos):
    ok = sum(sucesso(c) for c in codigos)
    pct = 100 * ok / len(codigos)
    erros = len(codigos) - ok
    seguidos = any(not sucesso(a) and not sucesso(b) for a, b in zip(codigos, codigos[1:]))
    if seguidos:
        classe = "CRÍTICO"
    elif pct >= 80:
        classe = "ESTÁVEL"
    else:
        classe = "INSTÁVEL"
    return pct, erros, seguidos, classe

resultados = {ep: analisar(cod) for ep, cod in zip(endpoints, status)}
for ep, (pct, erros, seguidos, classe) in resultados.items():
    print(f"{ep:<10} sucesso {pct:5.1f}% | erros {erros} | dois seguidos: {seguidos} | {classe}")
print("mais erros:", max(resultados, key=lambda ep: resultados[ep][1]))
