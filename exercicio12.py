numeros = []

for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print(f"\nMaior: {maior}")
print(f"Menor: {menor}")
print(f"Média: {media}")