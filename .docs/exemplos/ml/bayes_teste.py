def posterior(priori, sensibilidade, especificidade):
    """P(doente | positivo) pelo Teorema de Bayes."""
    p_pos_doente = sensibilidade                 # P(+ | D)
    p_pos_sadio = 1 - especificidade             # P(+ | não D): falso positivo
    p_pos = p_pos_doente * priori + p_pos_sadio * (1 - priori)   # probabilidade total
    return p_pos_doente * priori / p_pos

# valores ILUSTRATIVOS (não constam do material): sensibilidade 99%, especificidade 95%
prob = 0.01                                      # priori: prevalência de 1%
for teste in (1, 2, 3):
    prob = posterior(prob, 0.99, 0.95)
    print(f"após {teste}º resultado positivo: P(doente) = {prob:.4f}")
