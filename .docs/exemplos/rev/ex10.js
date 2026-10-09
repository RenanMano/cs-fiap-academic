let v = [10, 20, 30, 40, 50];
let ordenado = true;

for (let i = 0; i < v.length - 1; i++) {
    if (v[i] > v[i + 1]) {
        ordenado = false;
        break;
    }
}

console.log('Ordenado?', ordenado);
