import pandas as pd

df = pd.read_excel("tarefa_python.xlsx")
df["Media"] = (df["Nota1"] + df["Nota2"]) / 2
df["Situacao"] = df["Media"].apply(lambda x: "Aprovado" if x >= 7 else "Reprovado")
print(df)