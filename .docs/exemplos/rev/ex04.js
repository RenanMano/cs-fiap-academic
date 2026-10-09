let dados = [10, 20, 30, 40, 50];
let procurado = 30;
let posicao = -1;

for (let i = 0; i < dados.length; i++) {
    if (dados[i] === procurado) {
        posicao = i;
        break;
    }
}

console.log('Posição =', posicao);
