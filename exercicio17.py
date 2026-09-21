agenda = {}

while True:
    print("\n1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Listar contatos")
    print("0 - Sair")

    opcao = input("Escolha: ")
    
    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
        print("Contato salvo!")

    elif opcao == "2":
        nome = input("Nome: ")
        if nome in agenda:
            print(f"{nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        if agenda:
            for nome,telefone in agenda.items():
                print(f"{nome}: {telefone}")
        else:
            print("Nenhum contato cadastrado.")

    elif opcao == "0":
        print("Até logo!")
        break

    else:
        print("Opção invalida.") 