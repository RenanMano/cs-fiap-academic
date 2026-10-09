let dados = [2, 5, 2, 7, 2, 9];
let alvo = 2;
let contador = 0;

for (let i = 0; i < dados.length; i++) {
    if (dados[i] === alvo) {
        contador++;
    }
}

console.log('Quantidade =', contador);
