let historico = [];

function visitar(pagina) {
    historico.push(pagina);
}

function voltar() {
    if (historico.length > 1) {
        historico.pop();
        return historico[historico.length - 1];
    }
    return 'Não há página anterior';
}

visitar('google.com');
visitar('youtube.com');
visitar('github.com');

console.log(voltar());
