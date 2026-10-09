// Solução proposta: inserir no início e remover da versão com vetores paralelos
let valores = [], proximo = [], inicio = -1, ultimo = -1;

function adicionarNoFim(nome) {
  const i = valores.length;
  valores.push(nome);
  proximo.push(-1);
  if (inicio === -1) inicio = i;
  else proximo[ultimo] = i;
  ultimo = i;
}

function adicionarNoInicio(nome) {
  const i = valores.length;        // o dado vai para o fim do vetor...
  valores.push(nome);
  proximo.push(inicio);            // ...mas passa a apontar para o antigo primeiro
  inicio = i;
  if (ultimo === -1) ultimo = i;
}

function remover(nome) {
  let anterior = -1, atual = inicio;
  while (atual !== -1 && valores[atual] !== nome) {
    anterior = atual;
    atual = proximo[atual];
  }
  if (atual === -1) return false;
  if (anterior === -1) inicio = proximo[atual];
  else proximo[anterior] = proximo[atual];
  if (atual === ultimo) ultimo = anterior;
  return true;                     // a posição fica "órfã" no vetor, mas fora do encadeamento
}

function mostrar() {
  let s = "";
  for (let a = inicio; a !== -1; a = proximo[a]) s += valores[a] + " → ";
  return inicio === -1 ? "Lista vazia" : s + "null";
}

adicionarNoFim("Bruno");
adicionarNoFim("Carla");
adicionarNoInicio("Ana");
console.log(mostrar());
console.log("valores:", JSON.stringify(valores), "proximo:", JSON.stringify(proximo), "inicio:", inicio);
remover("Carla");
console.log(mostrar(), "| ultimo:", valores[ultimo]);
remover("Ana");
remover("Bruno");
console.log(mostrar());
