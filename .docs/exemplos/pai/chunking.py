# Splitting: fatias de tamanho fixo com sobreposição (overlap), medidas em palavras
texto = ("O RAG funciona em duas etapas. Na recuperação, o sistema vasculha os dados "
         "para encontrar informações úteis. Na geração, um modelo generativo usa as "
         "informações recuperadas para criar respostas claras e precisas.")

def fatiar(texto, tamanho, sobreposicao):
    palavras = texto.split()
    passo = tamanho - sobreposicao
    chunks = []
    for inicio in range(0, len(palavras), passo):
        chunks.append(" ".join(palavras[inicio:inicio + tamanho]))
        if inicio + tamanho >= len(palavras):
            break
    return chunks

for tamanho, sobreposicao in [(12, 0), (12, 4)]:
    print(f"tamanho={tamanho}, sobreposição={sobreposicao}:")
    for i, c in enumerate(fatiar(texto, tamanho, sobreposicao), 1):
        print(f"  [{i}] {c}")
