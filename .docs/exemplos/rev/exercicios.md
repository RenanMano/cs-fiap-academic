### Bloco 1 — Vetores

#### Exercício 1 — Leitura e exibição

**Enunciado:** Crie um vetor com 5 números e exiba todos os elementos.  
**Conhecimento avaliado:** Percurso completo com índice.  
**Complexidade:** O(n)

```javascript
{{include:rev/ex01.js}}
```

Saída esperada:

```text
{{include:rev/ex01.out}}
```

**Erro comum:** Usar `i <= dados.length` acessa uma posição inexistente e imprime `undefined`.

#### Exercício 2 — Soma dos elementos

**Enunciado:** Some todos os valores de um vetor numérico.  
**Conhecimento avaliado:** Acumulador inicializado fora do laço.  
**Complexidade:** O(n)

```javascript
{{include:rev/ex02.js}}
```

Saída esperada:

```text
{{include:rev/ex02.out}}
```

**Erro comum:** Declarar `soma = 0` **dentro** do laço zera o acumulador a cada iteração.

#### Exercício 3 — Maior valor

**Enunciado:** Encontre o maior valor do vetor sem usar funções prontas.  
**Conhecimento avaliado:** Algoritmo de máximo: começar com o primeiro elemento e comparar com os demais.  
**Complexidade:** O(n)

```javascript
{{include:rev/ex03.js}}
```

Saída esperada:

```text
{{include:rev/ex03.out}}
```

**Erro comum:** Iniciar `maior = 0` falha para vetores só com negativos. Por isso o material inicia com `dados[0]` e o laço com `i = 1`.

#### Exercício 4 — Busca linear

**Enunciado:** Retorne a posição de um valor no vetor. Se não existir, exiba -1.  
**Conhecimento avaliado:** Busca sequencial com sentinela de "não encontrado" (-1) e parada antecipada (`break`).  
**Complexidade:** O(n) no pior caso; O(1) no melhor caso

```javascript
{{include:rev/ex04.js}}
```

Saída esperada:

```text
{{include:rev/ex04.out}}
```

**Erro comum:** Usar `==` em vez de `===` permite coerções inesperadas (`'30' == 30` é `true`).

#### Exercício 5 — Contagem de ocorrências

**Enunciado:** Conte quantas vezes um número aparece no vetor.  
**Conhecimento avaliado:** Contador condicional. Diferente da busca, **não** pode usar `break`: precisa ver todos os elementos.  
**Complexidade:** O(n)

```javascript
{{include:rev/ex05.js}}
```

Saída esperada:

```text
{{include:rev/ex05.out}}
```

**Erro comum:** Interromper o laço na primeira ocorrência conta no máximo 1.

### Bloco 2 — Listas e manipulação

#### Exercício 6 — Inserção no final

**Enunciado:** Insira um novo elemento no final da lista.  
**Conhecimento avaliado:** A operação *append* do ADT Lista. O comentário didático do material associa a operação de lista com *append* no final.  
**Complexidade:** O(1) amortizado

```javascript
{{include:rev/ex06.js}}
```

Saída esperada:

```text
{{include:rev/ex06.out}}
```

**Erro comum:** Confundir `push` (no final) com `unshift` (no início, O(n)).

#### Exercício 7 — Remoção do último elemento

**Enunciado:** Remova o último elemento da lista.  
**Conhecimento avaliado:** `pop()` remove **e devolve** o elemento.  
**Complexidade:** O(1)

```javascript
{{include:rev/ex07.js}}
```

Saída esperada:

```text
{{include:rev/ex07.out}}
```

**Erro comum:** Ignorar o retorno quando o valor removido é necessário; `pop()` em lista vazia devolve `undefined`.

#### Exercício 8 — Inserção manual em posição específica

**Enunciado:** Insira o valor 25 na posição 2, deslocando os demais elementos.  
**Conhecimento avaliado:** Deslocamento à direita, do fim para a posição, abrindo espaço. Mostra **por que** a inserção em array é O(n).  
**Complexidade:** O(n)

```javascript
{{include:rev/ex08.js}}
```

Saída esperada:

```text
{{include:rev/ex08.out}}
```

**Erro comum:** Deslocar da esquerda para a direita sobrescreve os valores antes de copiá-los. O laço precisa ir **de trás para frente** (`i--`).

#### Exercício 9 — Remoção manual por posição

**Enunciado:** Remova o elemento da posição 1, deslocando os demais para a esquerda.  
**Conhecimento avaliado:** Deslocamento à esquerda e descarte da última posição duplicada com `pop()`.  
**Complexidade:** O(n)

```javascript
{{include:rev/ex09.js}}
```

Saída esperada:

```text
{{include:rev/ex09.out}}
```

**Erro comum:** Esquecer o `pop()` final deixa o último valor duplicado (`[10, 30, 40, 50, 50]`).

#### Exercício 10 — Verificar se está ordenado

**Enunciado:** Verifique se um vetor está em ordem crescente.  
**Conhecimento avaliado:** Comparação de pares vizinhos (`v[i]` com `v[i+1]`) com parada antecipada.  
**Complexidade:** O(n)

```javascript
{{include:rev/ex10.js}}
```

Saída esperada:

```text
{{include:rev/ex10.out}}
```

**Erro comum:** Laço até `v.length` (sem `- 1`) compara o último com `undefined`.

### Bloco 3 — Pilhas

#### Exercício 11 — Push, pop e peek

**Enunciado:** Implemente operações básicas de pilha.  
**Conhecimento avaliado:** Interface do ADT Pilha com proteção contra *underflow*.  
**Complexidade:** O(1) por operação

```javascript
{{include:rev/ex11.js}}
```

Saída esperada:

```text
{{include:rev/ex11.out}}
```

**Erro comum:** `peek()` não deve remover. Note que, na solução, `pop()` e `peek()` devolvem o texto `'Pilha vazia'`, que se confunde com um elemento válido: lançar um erro (`throw`) ou devolver `undefined` evita a ambiguidade.

#### Exercício 12 — Histórico de navegação

**Enunciado:** Simule um histórico de navegação usando pilha.  
**Conhecimento avaliado:** Aplicação de pilha: "voltar" remove a página atual e revela a anterior.  
**Complexidade:** O(1)

```javascript
{{include:rev/ex12.js}}
```

Saída esperada:

```text
{{include:rev/ex12.out}}
```

**Erro comum:** Permitir voltar com uma única página esvaziaria o histórico. A condição `historico.length > 1` impede isso.

#### Exercício 13 — Inverter palavra com pilha

**Enunciado:** Use uma pilha para inverter uma palavra.  
**Conhecimento avaliado:** A propriedade LIFO inverte a ordem naturalmente: o último caractere empilhado é o primeiro a sair.  
**Complexidade:** O(n)

```javascript
{{include:rev/ex13.js}}
```

Saída esperada:

```text
{{include:rev/ex13.out}}
```

**Erro comum:** Concatenar em ordem (`invertida = pilha.pop() + invertida`) desfaz a inversão.

#### Exercício 14 — Parênteses balanceados

**Enunciado:** Verifique se uma expressão possui parênteses balanceados.  
**Conhecimento avaliado:** Uso clássico de pilha: cada `(` empilha e cada `)` desempilha. Ao final, a pilha precisa estar vazia.  
**Complexidade:** O(n)

```javascript
{{include:rev/ex14.js}}
```

Saída esperada:

```text
{{include:rev/ex14.out}}
```

**Erro comum:** Só contar `(` e `)` aceita `)(` como balanceado. A pilha detecta o fechamento sem abertura (`pilha.length === 0`).

#### Exercício 15 — Mini gerenciador de tarefas

**Enunciado:** Crie um gerenciador simples em que adicionar tarefa faz push e concluir tarefa faz pop.  
**Conhecimento avaliado:** Pilha com três operações (`adicionar`, `concluir`, `atual`) e mensagens para o caso vazio.  
**Complexidade:** O(1) por operação

```javascript
{{include:rev/ex15.js}}
```

Saída esperada:

```text
{{include:rev/ex15.out}}
```

**Erro comum:** Repare na **consequência de projeto**: como é uma pilha, "concluir" finaliza sempre a tarefa **mais recente**. Se a regra do negócio fosse "concluir na ordem em que foram criadas", o correto seria uma **fila** (`shift()`), como discutido na [aula 05](../aula05-07-04-26/README.md#6-o-que-acontece-se-errarmos-a-estrutura).
