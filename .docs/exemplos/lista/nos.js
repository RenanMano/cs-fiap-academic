// Lista encadeada com nós de verdade: cada nó guarda o valor e a referência ao próximo
class No {
  constructor(valor) {
    this.valor = valor;
    this.proximo = null;
  }
}

class ListaEncadeada {
  constructor() {
    this.inicio = null;
    this.fim = null;
    this.tamanho = 0;
  }

  inserirNoFim(valor) {            // O(1) graças à referência para o último nó
    const novo = new No(valor);
    if (this.inicio === null) this.inicio = novo;
    else this.fim.proximo = novo;
    this.fim = novo;
    this.tamanho++;
  }

  inserirNoInicio(valor) {         // O(1): nenhum elemento é deslocado
    const novo = new No(valor);
    novo.proximo = this.inicio;
    this.inicio = novo;
    if (this.fim === null) this.fim = novo;
    this.tamanho++;
  }

  remover(valor) {                 // O(n): precisa procurar o nó anterior
    let anterior = null;
    let atual = this.inicio;
    while (atual !== null && atual.valor !== valor) {
      anterior = atual;
      atual = atual.proximo;
    }
    if (atual === null) return false;
    if (anterior === null) this.inicio = atual.proximo;
    else anterior.proximo = atual.proximo;
    if (atual === this.fim) this.fim = anterior;
    this.tamanho--;
    return true;
  }

  toString() {
    const partes = [];
    for (let n = this.inicio; n !== null; n = n.proximo) partes.push(n.valor);
    return partes.concat("null").join(" → ");
  }
}

const lista = new ListaEncadeada();
lista.inserirNoFim("Bruno");
lista.inserirNoFim("Carla");
lista.inserirNoInicio("Ana");
console.log(lista.toString(), "| tamanho:", lista.tamanho);
console.log("remover Bruno:", lista.remover("Bruno"), "→", lista.toString());
console.log("remover Zé:", lista.remover("Zé"), "→", lista.toString());
lista.remover("Carla");
lista.inserirNoFim("Davi");
console.log(lista.toString(), "| fim:", lista.fim.valor);
