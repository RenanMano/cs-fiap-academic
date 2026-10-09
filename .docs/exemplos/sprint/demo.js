const { relatorio } = require('./recarga.js');

console.log(relatorio({ potenciaKw: 22, minutos: 50, hora: 19, tipoUsuario: 'assinante' }));
console.log(relatorio({ potenciaKw: 200, minutos: 0, hora: 25, tipoUsuario: 'vip' }));
