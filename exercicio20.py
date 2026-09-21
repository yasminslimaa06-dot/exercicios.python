def carregar():
    agenda = {}
    try:
        with open("agenda.txt", "r", encoding="utf-8") as arquivos:
            for linha in arquivos:
                nome, telefone = linha.strip().split(";")
                agenda[nome] = telefone
    except FileNotFoundError:
        pass
    return agenda

def salvar(agenda):
    with open("agenda.txt", "w", encoding="utf-8") as arquivos:
        for nome, telefone in agenda.items():
            arquivos.write(f"{nome};{telefone}\n")

def adicionar(agenda):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    agenda[nome] = telefone
    print("Contato salvo!")

def buscar(agenda):
    nome = input("Nome: ")
    if nome in agenda:
        print(f"{nome}: {agenda[nome]}")
    else:
        print("Contato não encontrado.")

def listar(agenda):
    if agenda:
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")
    else:
        print("Nenhum contato cadastrado.")

def remover(agenda):
    nome = input("Nome: ")
    if nome in agenda:
        del agenda[nome]
        print("Contato removido.")
    else:
        print("Contato não encontrado.")


agenda = carregar()

while True:
    print("\n1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Listar contatos")
    print("4 - Remover contato")
    print("0 - Sair")

    opcao = input("Escolha: ")
    
    if opcao == "1":
        adicionar(agenda)
        salvar(agenda)
    elif opcao == "2":
        buscar(agenda)
    elif opcao == "3":
        listar(agenda)
    elif opcao == "4":
        remover(agenda)
    elif opcao == "0":
        salvar(agenda)
        print("Até logo!")
        break
    else:
        print("Opção inválida.")

    