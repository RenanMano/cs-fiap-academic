let pilha = [];

function push(x) {
    pilha.push(x);
}

function pop() {
    if (pilha.length === 0) {
        return 'Pilha vazia';
    }
    return pilha.pop();
}

function peek() {
    if (pilha.length === 0) {
        return 'Pilha vazia';
    }
    return pilha[pilha.length - 1];
}

push('A');
push('B');
push('C');

console.log(peek());
console.log(pop());
console.log(pilha);
