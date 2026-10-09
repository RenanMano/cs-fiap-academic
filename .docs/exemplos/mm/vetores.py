import numpy as np

u, v = np.array([1, 3]), np.array([3, 2])
print("u + v =", u + v, "| 2·<3, 3> =", 2 * np.array([3, 3]))

a, b = np.array([1, -2, 0]), np.array([-2, 4, -3])
print("a · b =", a @ b)                                  # produto escalar: um número

precos, quantidades = np.array([4, 2, 5]), np.array([5, 10, 6])
print("receita = preços · quantidades =", precos @ quantidades)

print("<2, 0> · <0, 3> =", np.array([2, 0]) @ np.array([0, 3]), "→ vetores perpendiculares")

c, d = np.array([1, -1, 2]), np.array([2, -1, 3])
cxd = np.cross(c, d)                                     # produto vetorial: um vetor
print("c × d =", cxd, "| perpendicular a c e d?", cxd @ c == 0 and cxd @ d == 0)
