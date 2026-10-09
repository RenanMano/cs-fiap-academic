entrada = "joao.silva@fiap.com.br, maria.souza@fiap.com.br, ana.paula@fiap.com.br"

usuarios, por_dominio = [], {}
for email in entrada.split(","):
    usuario, dominio = email.strip().split("@")
    usuarios.append(usuario)
    por_dominio[dominio] = por_dominio.get(dominio, 0) + 1

usuarios = tuple(sorted(usuarios))              # o exemplo do slide mostra os nomes em ordem alfabética
print("Primeiro:", usuarios[0], "| Último:", usuarios[-1])

lista = list(usuarios)                          # tuplas são imutáveis: troca feita numa lista
lista[0], lista[-1] = lista[-1], lista[0]       # atribuição de tupla, sem variável temporária
trocada = tuple(lista)

print("Relatório:")
print("Quantidade de e-mails por domínio:")
for dominio, qtd in por_dominio.items():
    print(f"  {dominio}: {qtd}")
print("Lista de usuários:", usuarios)
print("Após troca de posições:", trocada)
