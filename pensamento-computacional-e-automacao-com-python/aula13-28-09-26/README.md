<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Orienta%C3%A7%C3%A3o%20a%20Objetos&amp;fontSize=34&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=PENSAMENTO%20COMPUTACIONAL%20E%20AUTOMA%C3%87%C3%83O%20COM%20PYTHON%20%E2%80%94%20AULA%2013%20%E2%80%94%2028%2F09%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Orientação a Objetos: Aluno e Disciplina" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=Classe%3A%20molde%2C%20objeto%3A%20inst%C3%A2ncia;self.notas_por_disciplina%20%3D%20%7B%7D;Aluno%20TEM%20Disciplinas%20%28composi%C3%A7%C3%A3o%29;aluno1.exibir_boletim%28%29" alt="Classe: molde; objeto: instância. self.notas_por_disciplina = {}. Aluno TEM Disciplinas (composição). aluno1.exibir_boletim()." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-PCP-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: PCP" />
  <img src="https://img.shields.io/badge/Aula-13-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 13" />
  <img src="https://img.shields.io/badge/Data-28--09--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 28-09-2026" />
  <img src="https://img.shields.io/badge/Linguagem-Python-FF781F?style=for-the-badge&amp;labelColor=0D1117&amp;logo=python&amp;logoColor=white" alt="Linguagem: Python" />
  <img src="https://img.shields.io/badge/Paradigma-Orienta%C3%A7%C3%A3o%20a%20objetos-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Paradigma: Orientação a objetos" />
  <img src="https://img.shields.io/badge/Conceito-Composi%C3%A7%C3%A3o-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Conceito: Composição" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Pensamento Computacional e Automação com Python](../README.md) |
| Aula | 13 — 28/09/2026 |
| Título | Orientação a Objetos: Aluno e Disciplina |
| Tema central | Introdução à orientação a objetos com o exemplo Aluno e Disciplina: classe, objeto, atributo, método e composição; matrícula, registro de notas por disciplina, médias por disciplina e geral e boletim; código desenvolvido em aula em três módulos. |
| Tecnologias e ferramentas | Python 3 |
| Docente (conforme material) | Prof. Alexandre Russi Junior |
| Natureza do conteúdo | Aula prática com código |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`PCP - Aula 10 - Orientação a Objetos.pdf`](PCP%20-%20Aula%2010%20-%20Orienta%C3%A7%C3%A3o%20a%20Objetos.pdf) | Slides (15 páginas): problema do mundo real, conceitos-chave, classes Disciplina e Aluno, métodos de matrícula e notas, cálculo de médias, composição, app de demonstração com boletim e mapa mental. |
| [`aluno.py`](aluno.py) | Classe Aluno (versão de aula): nome, RM, curso, lista de disciplinas, dicionário de notas por disciplina, matricular, adicionar_nota e calcular_media_d. |
| [`app.py`](app.py) | Demonstração: cria um aluno e duas disciplinas, matricula, adiciona notas e imprime a média em Modelagem Linear. |
| [`disciplina.py`](disciplina.py) | Classe Disciplina (nome, professor, exibir_info) com um trecho de teste no nível do módulo marcado como “temporário”. |

> [!NOTE]
> **Limitações da documentação.** Os slides mostram o código como imagem, lido visualmente. Os arquivos da pasta são a versão desenvolvida em aula, mais simples que a dos slides; ambos foram analisados, e os arquivos foram executados numa cópia temporária (o repositório não foi alterado). As diferenças e dois comportamentos inesperados estão documentados. A pasta __pycache__ (bytecode) não é documentada.

<br />

<h2 id="visao-geral">Visão geral</h2>

A **orientação a objetos** (OO) organiza o programa em torno de **objetos** que reúnem **dados** (atributos) e **comportamentos** (métodos). O problema motivador é representar:

- **alunos**, com nome, matrícula e curso;
- **disciplinas**, com nome e professor;
- **notas**, que pertencem ao aluno em cada disciplina.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
classDiagram
    class Aluno {
        nome
        matricula
        curso
        disciplinas : list~Disciplina~
        notas_por_disciplina : dict
        matricular(d)
        adicionar_nota(d, nota)
        media_em(d)
        media_geral()
        exibir_boletim()
    }
    class Disciplina {
        nome
        professor
        exibir_informacoes()
    }
    Aluno o-- Disciplina : composição
```

*Figura 1 — Diagrama de classes da versão dos slides. A disciplina não guarda notas: quem sabe o desempenho é o aluno.*

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Diferenciar classe e objeto, atributo e método.
- Escrever classes com `__init__` e métodos que usam `self`.
- Aplicar **composição**: um objeto que contém outros.
- Organizar classes em módulos e importá-las.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 09](../aula09-10-08-26/README.md) (dicionários) e [aula 11](../aula11-09-09-26/README.md) (módulos e `import`).

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Conceitos-chave

| Conceito | Significado | No exemplo |
| :--- | :--- | :--- |
| **Classe** | Molde | `Aluno`, `Disciplina` |
| **Objeto** | Instância concreta | `aluno1`, `mat` |
| **Atributo** | Estado (dados) do objeto | `nome`, `notas_por_disciplina` |
| **Método** | Comportamento (ação) | `adicionar_nota`, `media_em` |
| **Composição** | Objeto que contém outros | O aluno tem uma lista de `Disciplina` |

### 2. As duas estruturas do Aluno

- `disciplinas`: lista de **objetos** `Disciplina` (em quais está matriculado);
- `notas_por_disciplina`: **dicionário** do nome da disciplina para a lista de notas, por exemplo `{"Matemática": [8.0, 6.5], "Física": [9.0]}`.

`setdefault(nome, [])` cria a lista vazia **só se** a chave ainda não existir.

### 3. Versão dos slides × versão da pasta

| Recurso | Slides | Arquivos da pasta (aula) |
| :--- | :--- | :--- |
| Atributo de matrícula | `matricula` | `rm` |
| `adicionar_nota` em disciplina não matriculada | **Matricula automaticamente** | Gera `KeyError` |
| Médias | `media_em` e `media_geral` | Só `calcular_media_d` |
| Boletim | `exibir_boletim` | Não implementado |
| Método da disciplina | `exibir_informacoes` | `exibir_info` |

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — executando os arquivos da pasta

`python3 app.py`, executado numa cópia dos arquivos, produziu:

<!-- norun -->
```text
Disciplina: Modelagem matemática | Professor: Igor
4.0
```

- **4.0** é a média de Modelagem Linear, $(5 + 3)/2$, o resultado esperado de `app.py`.
- A **primeira linha** não vem de `app.py`: `disciplina.py` tem, no nível do módulo, um trecho marcado como `# temporário` (`model_mat = Disciplina(...)` e `model_mat.exibir_info()`). Esse código executa sempre que o módulo é **importado**.

> [!NOTE]
> Na versão da pasta, `adicionar_nota` numa disciplina em que o aluno **não** foi matriculado gera `KeyError` (testado: `KeyError: 'Física'`). Isso acontece porque a lista de notas só é criada em `matricular`. A versão dos slides trata o caso matriculando antes. Os arquivos originais não foram alterados.

### Exemplo aplicado — a versão completa dos slides

Transcrição própria das classes mostradas nos slides, num único arquivo, com o app de demonstração:

```python
class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_informacoes(self):
        print(f"Disciplina: {self.nome} | Professor: {self.professor}")


class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = []                 # composição: o aluno "tem" disciplinas
        self.notas_por_disciplina = {}        # nome da disciplina -> [notas]

    def matricular(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina, nota):
        if disciplina.nome not in self.notas_por_disciplina:
            self.matricular(disciplina)       # versão dos slides: matricula se preciso
        self.notas_por_disciplina[disciplina.nome].append(nota)

    def media_em(self, disciplina):
        notas = self.notas_por_disciplina.get(disciplina.nome, [])
        return sum(notas) / len(notas) if notas else 0.0

    def media_geral(self):
        medias = [self.media_em(d) for d in self.disciplinas if self.notas_por_disciplina.get(d.nome)]
        return sum(medias) / len(medias) if medias else 0.0

    def exibir_boletim(self):
        print(f"Aluno: {self.nome} | Matrícula: {self.matricula} | Curso: {self.curso}")
        for d in self.disciplinas:
            d.exibir_informacoes()
            print(f"  Notas: {self.notas_por_disciplina[d.nome]} | Média: {self.media_em(d):.1f}")
        print(f"MÉDIA GERAL: {self.media_geral():.1f}")


aluno1 = Aluno("João Silva", "2025001", "Ciência da Computação")
mat = Disciplina("Matemática", "Prof. Carlos")
fis = Disciplina("Física", "Prof. Ana")
aluno1.matricular(mat)
aluno1.adicionar_nota(mat, 8.0)
aluno1.adicionar_nota(mat, 7.0)
aluno1.adicionar_nota(fis, 9.0)              # Física é matriculada automaticamente
aluno1.adicionar_nota(fis, 8.0)
aluno1.exibir_boletim()
```

Saída esperada:

```text
Aluno: João Silva | Matrícula: 2025001 | Curso: Ciência da Computação
Disciplina: Matemática | Professor: Prof. Carlos
  Notas: [8.0, 7.0] | Média: 7.5
Disciplina: Física | Professor: Prof. Ana
  Notas: [9.0, 8.0] | Média: 8.5
MÉDIA GERAL: 8.0
```

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

O material não traz exercícios. **Exercício proposto para estudo:** adicione à classe `Aluno` um método `situacao(disciplina)` que devolva "Aprovado" (média ≥ 6) ou "Reprovado", e use-o no boletim.

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

<!-- norun -->
```python
    def situacao(self, disciplina):
        return "Aprovado" if self.media_em(disciplina) >= 6 else "Reprovado"

    # em exibir_boletim, dentro do laço:
    print(f"  Situação: {self.situacao(d)}")
```

O método reutiliza `media_em`, sem duplicar o cálculo. A regra de aprovação fica num só lugar.

</details>

**Observação sobre `media_geral` (slides):** o código dos slides inclui na média geral apenas médias `> 0`, para considerar só disciplinas com notas. Um aluno que tirou **zero** de fato numa disciplina também seria excluído. A transcrição acima testa a existência de notas (`if self.notas_por_disciplina.get(d.nome)`), o que evita essa distorção.

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Sistemas corporativos** modelam o domínio com classes (Cliente, Pedido, Produto) e suas relações de composição.
- ***Frameworks*** como Django e SQLAlchemy mapeiam classes Python para tabelas de banco de dados (ORM).
- **Testabilidade:** objetos com responsabilidades claras são mais fáceis de testar isoladamente.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Código de teste solto no módulo (`# temporário`) | Proteger com `if __name__ == "__main__":` | Não executa ao importar |
| Acessar `dicionario[chave]` sem garantir a chave | `setdefault` ou verificar antes | Evita `KeyError` |
| Guardar notas dentro de `Disciplina` | Guardar no `Aluno` | Uma disciplina tem muitos alunos |
| Repetir cálculos em vários métodos | Reutilizar métodos (`media_em`) | Uma regra, um lugar |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- Classe = molde; objeto = instância; atributos = estado; métodos = comportamento.
- `__init__` inicializa os atributos; `self` é o próprio objeto.
- Composição: `Aluno` contém objetos `Disciplina`; as notas ficam no aluno, por disciplina.
- Código de módulo fora de `if __name__ == "__main__"` executa na importação.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Qual a diferença entre classe e objeto?
2. Por que as notas ficam no `Aluno` e não na `Disciplina`?
3. O que faz `self.notas_por_disciplina.setdefault("Física", [])`?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. A classe é o molde, que define atributos e métodos; o objeto é uma instância concreta criada a partir dele.
2. Porque a nota é um dado do desempenho de um aluno específico, e uma disciplina é compartilhada por vários alunos.
3. Cria a chave "Física" com uma lista vazia **se ela não existir**; se existir, mantém a lista atual.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [Python — classes](https://docs.python.org/pt-br/3/tutorial/classes.html)
- Materiais da pasta: [slides](PCP%20-%20Aula%2010%20-%20Orienta%C3%A7%C3%A3o%20a%20Objetos.pdf) · [aluno.py](aluno.py) · [disciplina.py](disciplina.py) · [app.py](app.py)

<br />

<p align="center"><a href="../aula12-23-09-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
