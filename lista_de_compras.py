alimentos = []
menu = True

while menu:
    print('Lista de Tarefa'.center(50, '='), "\n")
    print("""
    [1] Adiconar [2]Deletar [3]Exibir [0]Sair \n
          """)
    print('-'*50)

    menu = int(input("Opção: "))

    print('PARA DEIXAR DE ADICONAR OU REMOVER DIGITE: "SAIR" \n')

    if menu == 1:
        adicionar = ""
        while adicionar != "SAIR":
            adicionar = str(input("Adicionar: ")).upper()
            alimentos.append(adicionar)
            if adicionar == "SAIR":
                alimentos.remove("SAIR")
    if menu == 2:
        remover = ""
        while remover != "SAIR":
            remover = str(input('Remover: ')).upper()
            if remover == "SAIR":
                break
            alimentos.remove(remover)
    if menu == 3:
        print("Itens da sua lista:".center(50, "-"))
        for alimento in set(alimentos):
            alimentos = list(alimentos)
            print(alimento)
        if menu == 0:
            break

