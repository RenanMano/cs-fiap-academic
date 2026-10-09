# CLAUDE.md — CS FIAP Academic

Repositório com os materiais das aulas de Ciência da Computação (FIAP). Cada pasta de aula tem um `README.md` gerado a partir de uma especificação, no padrão visual **Knowledge Atelier**. As ferramentas ficam em [`.docs/`](.docs/README.md).

## Pedido típico

> "Documente a aula `aulaNN-DD-MM-AA` da disciplina `<pasta>`" (ou "documente as aulas novas").

Para "aulas novas", procure pastas `aula*` sem `README.md` e confira o histórico (`git log --stat`).

## Fluxo para documentar uma aula

1. **Ler todo o material da pasta**, sem exceção:
   - PDF: `pdftotext` mais renderização das páginas que têm imagens (`pdftoppm`);
   - PPTX: converter com `soffice --headless --convert-to pdf`, sem esquecer os slides ocultos;
   - notebooks: células e saídas salvas;
   - código, CSV e afins: tudo.

   Nunca documente a partir do nome da pasta ou do arquivo.
2. **Escrever a especificação** em `.docs/specs/<disciplina>/<aula>.md`. Use como modelo uma aula parecida que já existe.
3. **Exemplos executáveis** ficam em `.docs/exemplos/<grupo>/`, como `nome.py` mais `nome.out` gerado executando o script. O `.out` nunca é escrito à mão. No corpo da especificação, use `{{include:<grupo>/nome.py}}`.
4. **Figuras (opcional):** SVG original em `<aula>/assets/`, gerado por um script em `.docs/figuras/` (helpers em `stat_svg.py`).
5. **Gerar:** rode `python3 .docs/build.py <disciplina>` (todas as aulas e o índice, o que atualiza a navegação anterior/próxima) e `python3 .docs/build_root.py` (totais do README da raiz).
6. **Validar:** `python3 .docs/check.py README.md */README.md */aula*/README.md`. Tudo precisa sair `OK`.
7. **Commit:** apenas `README.md`, `assets/` e `.docs/`.

## Especificação (`.docs/specs/<disciplina>/<aula>.md`)

Começa com `<!--META {json} META-->`. Chaves:

- `title`, `header` (texto curto do cabeçalho), `tema`;
- `typing` (4 frases curtas);
- `tecnologias`, `tipo`, `professor` (só se constar do material);
- `badges` (`[rótulo, valor, cor, logo?]`; cores `FF781F`, `FF4500`, `E60000`);
- `icons` e `icons_alt` (skillicons, só tecnologias realmente trabalhadas na aula);
- `limitacoes` (o que não foi lido, executado ou verificado);
- `files`: descrição de **cada** arquivo da pasta, inclusive `assets/*.svg`; sem isso o build falha. `__pycache__` e o próprio `README.md` são ignorados.

O corpo usa títulos `<h2 id="...">` com `<br />` antes, nesta ordem:

| id | Seção |
| :--- | :--- |
| `visao-geral` | Visão geral, com um diagrama Mermaid |
| `objetivos` | Objetivos de aprendizagem |
| `pre-requisitos` | Pré-requisitos, com links para aulas anteriores |
| `fundamentacao-teorica` | Fundamentação teórica |
| `exemplos-praticos` | Exemplo básico e exemplo aplicado |
| `exercicios-resolvidos` | Exercícios e resoluções comentadas |
| `aplicacoes` | Aplicações no mercado de trabalho |
| `boas-praticas` | Boas práticas e erros comuns (tabela) |
| `resumo` | Resumo para revisão |
| `questoes` | 3 a 5 questões de fixação, com respostas em `<details>` |
| `referencias` | Referências: oficiais ou citadas no material, mais os arquivos da pasta |

O índice da disciplina vem de `.docs/specs/<disciplina>/_index.md`, com as chaves META `header`, `typing`, `badges`, `icons` e `mapa`. Disciplina nova: acrescente-a ao dicionário `DISC` em `.docs/build.py`.

## Regras de conteúdo

- **Idioma:** pt-BR formal e didático, com redação própria. Slides com aviso de direitos autorais são explicados, não copiados.
- **Nada inventado:**
  - não inventar conteúdo, links ou referências;
  - na falta de informação, registrar em `limitacoes`;
  - só afirmar que algo foi executado se foi de fato.
- **Soluções:** marque sempre como **"solução do material original"** ou **"solução proposta para estudo"**. Nunca apresente uma solução própria como gabarito oficial.
- **Código com saída:** um bloco ```` ```python ```` seguido de `Saída esperada:` e de um bloco ```` ```text ```` é executado pelo validador numa pasta vazia.
  - Use `<!-- norun -->` antes dos dois blocos quando o código depender de arquivos da pasta, rede ou API, e chame a saída de "Saída obtida" ou "Saída registrada".
  - Com pandas, use `pd.set_option("display.width", 200)` para a saída ser estável.
  - Valores em reais: `f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")`.
- **Materiais originais:** não altere nem exclua. Se houver erro num código da pasta, documente-o com a correção sugerida, sem corrigir o original.
- **README que já existe na pasta:** preserve o texto integralmente dentro da nova página, como foi feito em `solucoes-em-energia-renovaveis-e-sustentaveis/aula09-14-09-26`.
- **Segredos:** nunca reproduza chaves, *tokens*, links públicos temporários (Gradio, por exemplo), formulários ou SharePoint institucionais.
- **Notebooks que dependem de API paga:** documente a partir do código e das saídas salvas, sem executar, e diga isso em `limitacoes`.
- **Ferramentas:** não instale bibliotecas sem necessidade justificada. Prefira NumPy, pandas e a biblioteca padrão; por exemplo, `statistics.NormalDist` no lugar do scipy.
- **SVGs:** fundo `#0D1117`, faixa superior em gradiente, fonte Fira Code e `role="img"` com `<title>` e `<desc>`. Escape `<` e `>` nos textos (`&lt;`, `&gt;`). Na página, use texto alternativo descritivo.

## Padrão visual (gerado pelo build)

- **Cabeçalho e rodapé:** capsule-render com o gradiente `0:FF781F,50:FF4500,100:E60000`.
- **Animação:** readme-typing-svg.
- **Menu:** centralizado.
- **Badges:** shields com `style=for-the-badge&labelColor=0D1117`.
- **Paleta:** `FF781F`, `FF4500`, `E60000`, `0D1117`, `F8FAFC` e `CBD5E1`.
- **Proibido:** imagens de estatísticas ou de "snake".

## Pastas e git

- Pastas de aula seguem `aulaNN-DD-MM-AA`, com número sequencial na disciplina e data. Se chegar uma pasta fora do padrão, proponha a renomeação (`git mv`) antes de documentar.
- Mensagem de commit da documentação: `docs: add academic documentation for <disciplina> <aula>`.
- Não use `git push --force` e não faça merge sem pedido explícito.
