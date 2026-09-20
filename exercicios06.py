total = 0

for i in range(5):
    numero = int(input(f"Digite o numero {i + 1}: "))
    total = total + numero 

media = total / 5
print(f"A soma total é {total}")
print(f"A media é {media}")