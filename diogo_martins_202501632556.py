import pandas as pd
# Leia o arquivo Excel
df = pd.read_excel('tarefa.xlsx')
# Mostrar a base de dados
print("Base de dados:")
print(df)
# Criar Coluna de Média
df['Média'] = df[['Nota 1', 'Nota 2']].mean(axis=1)
# Classificar aprovados e reprovados
df['Situação'] = df['Média'].apply(lambda x: 'Aprovado' if x >= 6 else 'Reprovado')
# Mostrar a base de dados atualizada com a média e situação
print("\nBase de dados atualizada:")
print(df)