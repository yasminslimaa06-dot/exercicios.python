produtos = []
precos = []

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    if nome == "sair":
        break

    preco = float(input("Digite o preço do produto: "))

    while preco <= 0:
        print("Preço inválido.")
        preco = float(input("Digite o preço do produto: "))

    produtos.append(nome)
    precos.append(preco)

print()

if produtos:
    for i in range(len(produtos)):
        print(f"{produtos[i]} - R${precos[i]:.2f}")

    total = sum(precos)
    maior = max(precos)
    mais_caro = produtos[precos.index(maior)]

    print(f"Total: R${total:.2f}")
    print(f"Mais caro: {mais_caro}")
else:
    print("Nenhum produto foi adicionado.")