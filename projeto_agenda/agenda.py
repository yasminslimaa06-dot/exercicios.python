ARQUIVO = "agenda.txt"


def carregar():
    agenda = {}
    try:
        with open(ARQUIVO, "r", encoding = "utf-8") as arquivo:
            for linha in arquivo:
                try:
                    nome, telefone = linha.strip().split(";") 
                    agenda[nome] = telefone
                except ValueError:
                    print(f"Linha ignorada (formato inválido): {linha.strip()}")
    except FileNotFoundError:
        pass
    return agenda


def salvar(agenda):
    with open(ARQUIVO, "w", encoding = "utf-8") as arquivo:
        for nome, telefone in agenda.items():
            arquivo.write(f"{nome};{telefone}\n")


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            print("Não pode ficar vazio.")
        elif ";" in texto:
            print("Não use o caractere ';'.")
        else:
            return texto


def adicionar(agenda):
    nome = ler_texto("Digite o nome: ")
    if nome in agenda:
        print("Esse contato ja existe. Use a opção de editar.") 
        return
    telefone = ler_texto("Telefone: ")
    agenda[nome] = telefone
    salvar(agenda)
    print("Contato salvo!")


def buscar(agenda):
    nome = ler_texto("Nome: ")
    if nome in agenda:
        print(f"{nome}: {agenda[nome]}")
    else:
        print("Contato não encontrado.")


def listar(agenda):
    if agenda:
        for nome, telefone in sorted(agenda.items()):
            print(f"{nome}: {telefone}")
    else:
        print("Nenhum contato cadastrado.")


def remover(agenda):
    nome = ler_texto("Nome: ")
    if nome in agenda:
        del agenda[nome]
        salvar(agenda)
        print("Contato removido.")
    else:
        print("Contato não encontrado.")


def editar(agenda):
    nome = ler_texto("Nome: ")
    if nome in agenda:
        telefone = ler_texto("Novo telefone: ")
        agenda[nome] = telefone 
        salvar(agenda)
        print("Telefone atualizado!")
    else:
        print("Contato não encontrado.")


agenda = carregar()

while True:
    print("\n1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Listar contatos")
    print("4 - Remover contato")
    print("5 - Editar telefone")
    print("0 - Sair")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        adicionar(agenda)
    elif opcao == "2":
        buscar(agenda)
    elif opcao == "3":
        listar(agenda)
    elif opcao == "4":
        remover(agenda)
    elif opcao == "5":
        editar(agenda)
    elif opcao == "0":
        salvar(agenda)
        print("Até logo!")
        break
    else:
        print("Opção inválida.") 
   
