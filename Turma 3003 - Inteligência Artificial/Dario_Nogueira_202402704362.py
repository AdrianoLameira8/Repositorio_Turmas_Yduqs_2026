import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

#==================================
#ETAPA 1 - LEITURA DOS DADOS
#==================================
df = pd.read_excel('base_dados_ia.xlsx')

print("===DataFrame===")
print(df.head())
print("===Informações do DataFrame===")
print(df.info())

#==================================
#ETAPA 2 - PREPARAÇÃO DOS DADOS
#==================================
x = df[["nota1", "nota2", "frequencia", "horas_estudo"]]
y = df["resultado"]

#==================================
#ETAPA 3 - CRIAÇÃO DO MODELO
#==================================
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

model = LogisticRegression(solver="liblinear")
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
y_pred_proba = model.predict_proba(x_test)[:, 1]

#==================================
#ETAPA 4 - AVALIAÇÃO DO MODELO
#==================================
acuracia = accuracy_score(y_test, y_pred)
relatorio_classificacao = classification_report(y_test, y_pred, target_names=["Reprovado", "Aprovado"])

print(f"Acurácia: {acuracia:.2f}")
print("Relatório de Classificação")
print(relatorio_classificacao)

#==================================
#ETAPA 5 - PROBABILIDADES
#==================================
def interpretar_probabilidade(probabilidade):
    if probabilidade >= 0.85:
        return "Alta Chance de Aprovação"
    elif probabilidade <= 0.40:
        return "Reprovado"
    else:
        return "Risco de Reprovação"

amostras = x_test
amostras["probabilidade_aprovacao"] = model.predict_proba(amostras)[:,1]
amostras["interpretação"] = amostras["probabilidade_aprovacao"].apply(interpretar_probabilidade)
print("\n=== Probabilidades de aprovação ===")
print(amostras[["nota1", "nota2", "frequencia", "horas_estudo", "probabilidade_aprovacao", "interpretação"]])

#==================================
#PERGUNTAS OBRIGATÓRIAS
#==================================

#O modelo teve boa acurácia?
#Sim pois o modelo teve uma acurácia de 0.88.

#Como interpretar a probabilidade gerada pelo modelo?
#Ela indica a probabilidade de aprovação ou reprovação do aluno
# 0.85 - alta probabilidade de aprovação
# 0.40 - probabilidade de reprovação

#O modelo pode ser usado na vida real? Por quê ?
#Sim, porque pode ser usado pra indentificar alunos que podem ter alguma dificuldade na matéria

#Existe risco de erro ou injustiça?
#Sim, pois o modelo apesar de ter tido uma boa acurácia ela não foi 100% mas somente 88% tendo uma chance de 12% de ocorrer um erro

#O que poderia melhorar no modelo?
#Coletar mais dados relevantes, não ignorar o contexto pessoal e não só se basear pelas horas de estudo e frequencia