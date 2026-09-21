ARQUIVO = "estoque.txt"


def carregar():
    estoque = {}
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                try:
                    nome, qtd, preco = linha.strip().split(";")
                    estoque[nome] = {"qtd": int(qtd), "preco": float(preco)}
                except ValueError:
                    print(f"Linha ignorada: {linha.strip()}")
    except FileNotFoundError:
        pass
    return estoque


def salvar(estoque):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for nome, dados in estoque.items():
            arquivo.write(f"{nome};{dados['qtd']};{dados['preco']}\n")


def ler_inteiro(mensagem, minimo=0):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"Digite um número maior ou igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print("Digite apenas números inteiros.")


def ler_preco(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor <= 0:
                print("O preço deve ser maior que zero.")
            else:
                return valor
        except ValueError:
            print("Digite apenas números.")


def ler_nome():
    nome = input("Nome do produto: ").strip()
    if nome == "":
        print("O nome não pode ficar vazio.")
        return None
    if ";" in nome:
        print("Não use o caractere ';'.")
        return None
    return nome


def cadastrar(estoque):
    nome = ler_nome()
    if nome is None:
        return
    if nome in estoque:
        print("Esse produto já existe.")
        return
    qtd = ler_inteiro("Quantidade: ")
    preco = ler_preco("Preço: ")
    estoque[nome] = {"qtd": qtd, "preco": preco}
    salvar(estoque)
    print("Produto cadastrado!")


def listar(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    total = 0
    menor_nome = None
    menor_qtd = 0
    for nome, dados in sorted(estoque.items()):
        valor = dados["qtd"] * dados["preco"]
        total += valor
        print(f"{nome}: {dados['qtd']} un. x R${dados['preco']:.2f} = R${valor:.2f}")
        if menor_nome is None or dados["qtd"] < menor_qtd:
            menor_nome = nome
            menor_qtd = dados["qtd"]
    print(f"Valor total do estoque: R${total:.2f}")
    print(f"Menos unidades: {menor_nome} ({menor_qtd} un.)")


def entrada(estoque):
    nome = ler_nome()
    if nome is None:
        return
    if nome not in estoque:
        print("Produto não encontrado.")
        return
    qtd = ler_inteiro("Quantidade que entrou: ", 1)
    estoque[nome]["qtd"] += qtd
    salvar(estoque)
    print(f"Estoque atualizado: {estoque[nome]['qtd']} un.")


def saida(estoque):
    nome = ler_nome()
    if nome is None:
        return
    if nome not in estoque:
        print("Produto não encontrado.")
        return
    qtd = ler_inteiro("Quantidade que saiu: ", 1)
    if qtd > estoque[nome]["qtd"]:
        print(f"Estoque insuficiente. Disponível: {estoque[nome]['qtd']} un.")
        return
    estoque[nome]["qtd"] -= qtd
    salvar(estoque)
    print(f"Estoque atualizado: {estoque[nome]['qtd']} un.")


def remover(estoque):
    nome = ler_nome()
    if nome is None:
        return
    if nome in estoque:
        del estoque[nome]
        salvar(estoque)
        print("Produto removido!")
    else:
        print("Produto não encontrado.")


estoque = carregar()

while True:
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Dar entrada")
    print("4 - Dar saída")
    print("5 - Remover produto")
    print("0 - Sair")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        cadastrar(estoque)
    elif opcao == "2":
        listar(estoque)
    elif opcao == "3":
        entrada(estoque)
    elif opcao == "4":
        saida(estoque)
    elif opcao == "5":
        remover(estoque)
    elif opcao == "0":
        salvar(estoque)
        print("Até logo!")
        break
    else:
        print("Opção inválida.")