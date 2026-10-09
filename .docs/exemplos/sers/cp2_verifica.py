import sys
import numpy as np, pandas as pd
df = pd.read_csv(sys.argv[1])
print(df.shape, df.isna().sum().sum())
print("p1 + p2 + p3 + p4 max abs:", np.abs(df[['p1','p2','p3','p4']].sum(axis=1)).max())
# divisão como ShuffleSplit/train_test_split(test_size=0.2, random_state=42)
perm = np.random.RandomState(42).permutation(len(df))
te, tr = perm[:2000], perm[2000:]
X = df.drop(columns=['stab','stabf']).to_numpy(); y = (df['stabf'] == 'unstable').astype(float).to_numpy()
Xtr, Xte, ytr, yte = X[tr], X[te], y[tr], y[te]
# logística L2 (C=1, intercepto sem penalidade) por Newton
A = np.column_stack([np.ones(len(Xtr)), Xtr]); w = np.zeros(A.shape[1]); R = np.eye(A.shape[1]); R[0,0] = 0
for _ in range(50):
    p = 1/(1+np.exp(-A@w)); g = A.T@(p-ytr) + R@w; H = A.T@(A*(p*(1-p))[:,None]) + R
    w -= np.linalg.solve(H, g)
pt = 1/(1+np.exp(-np.column_stack([np.ones(len(Xte)), Xte])@w))
print("primeiras probs unstable:", np.round(pt[:5], 8))
print("acurácia:", 100*np.mean((pt>=0.5)==yte))
