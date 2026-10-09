const readline = require('node:readline');
const { relatorio } = require('./recarga.js');

const rl = readline.createInterface({ input: process.stdin });
const linhas = rl[Symbol.asyncIterator]();

async function perguntar(texto) {
  process.stdout.write(texto);
  const { value, done } = await linhas.next();
  if (done) throw new Error('Entrada encerrada');
  return value.trim();
}

async function lerNumero(texto, valido) {
  while (true) {                                   // repete até a entrada ser válida
    const n = Number((await perguntar(texto)).replace(',', '.'));
    if (valido(n)) return n;
    console.log('Valor inválido, tente novamente.');
  }
}

async function main() {
  const potenciaKw = await lerNumero('Potência do carregador (kW): ', (n) => n > 0 && n <= 150);
  const minutos = await lerNumero('Duração da recarga (min): ', (n) => Number.isInteger(n) && n > 0);
  const hora = await lerNumero('Hora de início (0-23): ', (n) => Number.isInteger(n) && n >= 0 && n <= 23);
  let tipoUsuario;
  do {
    tipoUsuario = (await perguntar('Tipo de usuário (comum/assinante): ')).toLowerCase();
  } while (tipoUsuario !== 'comum' && tipoUsuario !== 'assinante');
  rl.close();
  console.log(relatorio({ potenciaKw, minutos, hora, tipoUsuario }));
}

main();
