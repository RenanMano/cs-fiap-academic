import glob
import pandas as pd

for f in sorted(glob.glob("*.csv")):
    df = pd.read_csv(f, sep=";", encoding="utf-8-sig")   # utf-8-sig remove o BOM
    contagem = df["resultado_esperado"].value_counts()
    print(f"{f:<40} {len(df):>2} casos | BLOCK={contagem['BLOCK']}, ALLOW={contagem['ALLOW']}")
