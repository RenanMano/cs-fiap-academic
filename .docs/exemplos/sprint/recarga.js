// Simulador de sessão de recarga — solução proposta para estudo (valores de tarifa hipotéticos)
const TARIFA_KWH = { normal: 1.2, ponta: 1.8 };     // R$/kWh
const DESCONTO = { comum: 0, assinante: 0.15 };     // fração de desconto
const HORARIO_PONTA = { inicio: 18, fim: 21 };       // 18h às 20h59

function validarSessao({ potenciaKw, minutos, hora, tipoUsuario }) {
  const erros = [];
  if (!(potenciaKw > 0 && potenciaKw <= 150)) erros.push('potência deve estar entre 0 e 150 kW');
  if (!(Number.isInteger(minutos) && minutos > 0)) erros.push('duração deve ser um inteiro positivo');
  if (!(Number.isInteger(hora) && hora >= 0 && hora <= 23)) erros.push('hora deve estar entre 0 e 23');
  if (!(tipoUsuario in DESCONTO)) erros.push('tipo de usuário inválido');
  return erros;
}

function simularRecarga(potenciaKw, minutos, passoMin = 15) {
  const registros = [];
  let energiaKwh = 0;
  for (let t = 0; t < minutos; t += passoMin) {            // repetição: simula o tempo
    const intervalo = Math.min(passoMin, minutos - t);
    energiaKwh += potenciaKw * (intervalo / 60);
    registros.push({ minuto: t + intervalo, energiaKwh });
  }
  return { energiaKwh, registros };
}

function tarifar(energiaKwh, hora, tipoUsuario) {
  const ponta = hora >= HORARIO_PONTA.inicio && hora < HORARIO_PONTA.fim;   // decisão de tarifação
  const preco = ponta ? TARIFA_KWH.ponta : TARIFA_KWH.normal;
  const bruto = energiaKwh * preco;
  const desconto = bruto * DESCONTO[tipoUsuario];
  return { ponta, preco, bruto, desconto, total: bruto - desconto };
}

function relatorio(sessao) {
  const erros = validarSessao(sessao);
  if (erros.length > 0) return 'Sessão recusada: ' + erros.join('; ');
  const { energiaKwh, registros } = simularRecarga(sessao.potenciaKw, sessao.minutos);
  const c = tarifar(energiaKwh, sessao.hora, sessao.tipoUsuario);
  const brl = (v) => 'R$ ' + v.toFixed(2).replace('.', ',');
  const linhas = [
    '========== SESSÃO DE RECARGA ==========',
    `Usuário: ${sessao.tipoUsuario.padEnd(10)} Início: ${String(sessao.hora).padStart(2, '0')}h`,
    `Potência: ${sessao.potenciaKw} kW      Duração: ${sessao.minutos} min`,
    '--- Progresso ---',
    ...registros.map((r) => `  ${String(r.minuto).padStart(3)} min -> ${r.energiaKwh.toFixed(2)} kWh`),
    '--- Cobrança ---',
    `Energia: ${energiaKwh.toFixed(2)} kWh x ${brl(c.preco)}/kWh (${c.ponta ? 'horário de ponta' : 'horário normal'})`,
    `Subtotal: ${brl(c.bruto)}   Desconto: ${brl(c.desconto)}`,
    `TOTAL: ${brl(c.total)}`,
    '=======================================',
  ];
  return linhas.join('\n');
}

module.exports = { validarSessao, simularRecarga, tarifar, relatorio };
