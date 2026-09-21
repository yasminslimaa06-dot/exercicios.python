while True:
    try:
        numero = int(input("Digite um número: "))
        break
    except ValueError:
        print("Digite apenas números.")

print(f"O dobro é {numero * 2}")