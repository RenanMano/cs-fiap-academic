from itertools import product

V = lambda b: "V" if b else "F"

print("P Q | P and not Q | (P or Q) and (P and Q)")
for P, Q in product([True, False], repeat=2):
    print(V(P), V(Q), "|", V(P and not Q), "            |", V((P or Q) and (P and Q)))

print("\nP Q R | (P or R) or (not Q and R) | exercício 7")
for P, Q, R in product([True, False], repeat=3):
    e6 = (P or R) or (not Q and R)
    e7 = ((P or not Q) and (P and Q)) or e6
    print(V(P), V(Q), V(R), "|", V(e6), "                        |", V(e7))
