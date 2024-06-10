import gerenciamento


def menu():
    print("\n==Cine Max de Cajazeiras==")
    print("\n ==Menu do ADM== \n ==Gerenciamento de filmes==")
    print("\nSelecione a opção:")
    print("1 - Para buscar filmes")
    print("2 - Para adicionar filmes")
    print("3 - Para atualizar dados do filme")
    print("4 - Para deletar filme")
    print("5 - Para ver ingressos")
    print("6 - Para remover ingressos")
    print("7 - Para ver o relatorio de vendas")
    print("8 - Para gerenciamento de horarios")
    print("0 - Para voltar")

    while True:
        opcao = input("\nDigite sua opção: ")

        if opcao == "1":
            gerenciamento.buscar_filme()
        elif opcao == "2":
            gerenciamento.adicionar_filme()
        elif opcao == "3":
            gerenciamento.atualizar_filme()
        elif opcao == "4":
            gerenciamento.remover_filme()
        elif opcao == "5":
            gerenciamento.ver_ingressos()
        elif opcao == "6":
            gerenciamento.remover_ingressos()
        elif opcao == "7":
            gerenciamento.relatorio_vendas()
        elif opcao == "8":
            gerenciamento.gerenciar_horarios_exibicao()
        elif opcao == "9":
            gerenciamento.gerenciar_horarios_exibicao()
        elif opcao == "0":
            print("\nVoltando ao menu principal.")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

