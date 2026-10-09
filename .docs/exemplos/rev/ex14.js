let expressao = '(a+b) * (c-d)';
let pilha = [];
let ok = true;

for (let i = 0; i < expressao.length; i++) {
    if (expressao[i] === '(') {
        pilha.push('(');
    }

    if (expressao[i] === ')') {
        if (pilha.length === 0) {
            ok = false;
            break;
        }
        pilha.pop();
    }
}

if (pilha.length > 0) {
    ok = false;
}

console.log('Balanceado?', ok);
