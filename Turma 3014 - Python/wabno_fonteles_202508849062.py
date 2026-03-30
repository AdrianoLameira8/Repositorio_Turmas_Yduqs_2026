import pandas as pd
#Ler o arquivo do excel
df = pd.read_excel("trabalho_python.xlsx")
print(df)
#criar coluna média
df["Média"] = (df["Nota 1"] + df["Nota 2"])/2
print(df)
# classificação
df["Situação"] = df["Média"].apply(lambda x: "Aprovado" if x >= 6 else "Reprovado")

print(df)
