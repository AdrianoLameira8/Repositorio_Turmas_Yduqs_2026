alunos = []

while True:
    nome = str(input("Digite seu nome (ou 'sair'): "))

    if nome == "sair":
        print("Encerrando o programa...")
        break

    nota = float(input("Digite a sua primeira nota: "))
    nota1 = float(input("Digite a sua segunda nota: "))
    
    media = (nota + nota1) / 2

    if media >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    aluno = {
        "nome": nome,
        "nota1": nota,
        "nota2": nota1,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)

print("\nLista de alunos:")

for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Média: {aluno['media']}")
    print(f"Situação: {aluno['situacao']}\n")
   