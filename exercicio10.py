def calcular_media(a, b, c):
    return (a + b + c) / 3

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

media = calcular_media(n1, n2, n3)

print(f"A média é {media}")