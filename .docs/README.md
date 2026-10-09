# Ferramentas de documentação

Geram e validam os `README.md` das aulas, dos índices das disciplinas e da raiz. As regras de conteúdo estão no [`CLAUDE.md`](../CLAUDE.md) da raiz.

| Caminho | Função |
| :--- | :--- |
| `build.py` | Gera os READMEs das aulas e o índice de uma disciplina a partir de `specs/` |
| `build_root.py` | Gera o `README.md` da raiz (tabela de disciplinas e totais) |
| `check.py` | Valida links, âncoras, exemplos Python, JS e NASM com saída esperada, e diagramas Mermaid |
| `specs/<disciplina>/<aula>.md` | Especificação de cada aula (META em JSON e corpo em Markdown) |
| `specs/<disciplina>/_index.md` | Especificação do índice da disciplina |
| `exemplos/<grupo>/` | Scripts e saídas (`.py` e `.out`) incluídos com `{{include:<grupo>/arquivo}}` |
| `figuras/` | Scripts que geram os SVGs de `assets/` (helpers em `stat_svg.py`) |
| `package.json` | Dependência opcional (mermaid-cli) para validar os diagramas |

## Uso

Comandos a partir da raiz do repositório:

```bash
# gerar uma disciplina inteira (aulas e índice; atualiza a navegação entre aulas)
python3 .docs/build.py pensamento-computacional-e-automacao-com-python

# gerar só uma aula
python3 .docs/build.py pensamento-computacional-e-automacao-com-python/aula13-28-09-26

# atualizar o README da raiz
python3 .docs/build_root.py

# validar (com Mermaid: rode antes `npm install` dentro de .docs/)
python3 .docs/check.py README.md */README.md */aula*/README.md
python3 .docs/check.py <arquivos> --no-mermaid   # sem validar Mermaid
```

## Figuras

Os scripts `figuras/gen_*.py` escrevem direto nas pastas `assets/` e rodam sem argumentos. Os demais recebem o destino:

```bash
python3 .docs/figuras/gates_svg.py computer-science/aula04-30-03-26/assets/portas-basicas.svg AND,OR,NOT
python3 .docs/figuras/gates_svg.py computer-science/aula09-31-08-26/assets/portas-nand-nor.svg NAND,NOR
python3 .docs/figuras/kmap_svg.py computer-science/aula10-28-09-26/assets/mapa-k-exemplo.svg
python3 .docs/figuras/gen_matrix_svg.py computer-organization-and-architecture/aula13-02-10-26/assets/letra-a-matriz-8x8.svg
```

`computer-organization-and-architecture/aula05-17-04-26/assets/cpu-simples.svg` foi escrito à mão e não tem script.

Requisitos: Python 3.12+, NumPy e pandas. Node.js é necessário para os exemplos JS e para o mermaid-cli, e `nasm`/`ld` para os exemplos em Assembly.
