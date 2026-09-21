estoque = {} 

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    if nome == "sair":
        break

    quantidade = int(input("Quantidade: "))
    estoque[nome] = quantidade

print()

if estoque:
    for nome, quantidade in estoque.items():
        print(f"{nome}: {quantidade}")  
   
    print(f"Total de itens: {sum(estoque.values())}")
else:
    print("Nenhum produto foi adicionado.")
