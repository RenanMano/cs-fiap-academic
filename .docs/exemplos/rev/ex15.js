let tarefas = [];

function adicionar(tarefa) {
    tarefas.push(tarefa);
}

function concluir() {
    if (tarefas.length === 0) {
        return 'Nenhuma tarefa para concluir';
    }
    return tarefas.pop();
}

function atual() {
    if (tarefas.length === 0) {
        return 'Sem tarefa atual';
    }
    return tarefas[tarefas.length - 1];
}

adicionar('Ler exercício 1');
adicionar('Resolver exercício 2');
adicionar('Corrigir exercício 3');

console.log(atual());
console.log(concluir());
console.log(tarefas);
