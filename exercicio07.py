# Parte 1: par ou impar
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")

# Parte 2: maior de 3 números
a = int(input("Digite o 1º número: "))
b = int(input("Digite o 2º número: "))
c = int(input("Digite o 3º número: "))

if a >= b and a >= c:
    print(f"O maior número é: {a}")
elif b > c:
    print(f"O maior número é: {b}")
else:
    print(f"O maior número é: {c}")