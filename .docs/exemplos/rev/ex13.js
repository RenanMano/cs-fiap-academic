let palavra = 'casa';
let pilha = [];
let invertida = '';

for (let i = 0; i < palavra.length; i++) {
    pilha.push(palavra[i]);
}

while (pilha.length > 0) {
    invertida = invertida + pilha.pop();
}

console.log(invertida);
