def calcular_media(a, b, c):
    return (a + b + c) / 3
    
def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


for i in range(4):
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))


    media = calcular_media(nota1, nota2, nota3)
    resultado = situacao(media)

    print(f"{nome}: Média {media:.1f} - {resultado}\n")