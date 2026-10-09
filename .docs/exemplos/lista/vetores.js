// Mesma lógica de listas2.html, sem a página: dois vetores paralelos simulam a lista encadeada
let valores = [];   // dado de cada "nó"
let proximo = [];   // índice do próximo nó (-1 = fim)
let inicio = -1;
let ultimo = -1;

function adicionar(nome) {
  if (nome === "") {
    console.log("Digite um nome");
    return;
  }
  const novoIndice = valores.length;
  valores.push(nome);
  proximo.push(-1);
  if (inicio === -1) {
    inicio = novoIndice;
    ultimo = novoIndice;
  } else {
    proximo[ultimo] = novoIndice;   // o antigo último passa a apontar para o novo
    ultimo = novoIndice;
  }
}

function mostrar() {
  if (inicio === -1) return "Lista vazia";
  let resultado = "";
  let atual = inicio;
  while (atual !== -1) {
    resultado += valores[atual] + " → ";
    atual = proximo[atual];
  }
  return resultado + "null";
}

console.log(mostrar());
for (const nome of ["Ana", "Bruno", "", "Carla"]) adicionar(nome);
console.log(mostrar());
console.log("valores:", JSON.stringify(valores));
console.log("proximo:", JSON.stringify(proximo));
console.log("inicio =", inicio, "| ultimo =", ultimo);
