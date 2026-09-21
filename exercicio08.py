n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif op == "-":
    print(f"{n1} - {n2} = {n1 - n2}")
elif op == "*":
    print(f"{n1} * {n2} = {n1 * n2}")
elif op == "/":
    if n2 == 0:
        print("Erro: não é possível dividir por zero.")
    else:
        print(f"{n1} / {n2} = {n1 / n2}")
else:
    print("Operação inválida.")       