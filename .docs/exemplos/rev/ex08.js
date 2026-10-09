let dados = [10, 20, 30, 40];
let valor = 25;
let posicao = 2;

dados.push(0); // abre uma posição no final

for (let i = dados.length - 1; i > posicao; i--) {
    dados[i] = dados[i - 1];
}

dados[posicao] = valor;

console.log(dados);
