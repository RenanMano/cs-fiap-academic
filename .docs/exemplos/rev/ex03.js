let dados = [8, 15, 3, 27, 12];
let maior = dados[0];

for (let i = 1; i < dados.length; i++) {
    if (dados[i] > maior) {
        maior = dados[i];
    }
}

console.log('Maior valor =', maior);
