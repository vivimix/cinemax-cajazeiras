import forum
import gerenciamento

saldos = []


ingressos_comprados = []


def menu_dos_clientes():
    while True:
        
        print("\n== Cine Max de Cajazeiras ==")
        print("\n== Menu do Cliente ==\n== Gerenciamento dos ingressos ==")
        print("\nBem vindo, caro cliente. O que você deseja fazer?")
        print("\nSe você deseja depositar dinheiro na sua conta para a compra de ingressos, digite 1.")
        print("Se você deseja comprar um ingresso, digite 2.")
        print("Se deseja cancelar sua compra e pedir reembolso, digite 3.")
        print("Se deseja dar seu feedback do filme, digite 4.")
        print("Se deseja voltar para o menu inicial, digite 0.")

        resposta = input("\nDigite aqui sua resposta: ")

        if resposta == "1":
            depositar_saldo()

        elif resposta == "2":
            comprar_ingresso()

        elif resposta == "3":
            cancelar_compra()

        elif resposta == "4":
            forum.deixar_feedback()

        elif resposta == "0":
            print("\nVoltando para o menu principal...")
            print("Ação completa.")
            break

        else:
            print("\nResposta inválida. Por favor, escolha uma opção válida.")

def depositar_saldo():
    while True:
        saldo_depositado = float(input("\nDigite o valor que deseja depositar: "))
        if saldo_depositado > 0 and saldo_depositado <= 1000:
            saldos.append(saldo_depositado)
            print(f"Depósito de R${saldo_depositado:.2f} realizado com sucesso.")
            print(f"Seu saldo atual é de R${sum(saldos):.2f}.\n")
            break
        else:
            print("O valor do depósito deve ser maior que zero e menor ou igual a 1000. Tente novamente.")


def comprar_ingresso():
    while True:
        print("\n== Compra de Ingresso ==")
        saldo_atual = sum(saldos)
        print(f"Saldo atual: R${saldo_atual:.2f}\n")

        print("Filmes disponíveis para compra:")
        for filme in gerenciamento.filmes:
            print(f"- {filme['titulo']} ({filme['genero']}) - Ingresso: R${filme['preço']:.2f}")

        titulo_filme = input("\nDigite o título do filme que deseja assistir: ").lower()
        quantidade_ingressos = int(input("Digite a quantidade de ingressos que deseja comprar: "))

        if quantidade_ingressos <= 0:
            print("Quantidade inválida de ingressos. Tente novamente.")
            continue

        for filme in gerenciamento.filmes:
            if filme["titulo"].lower() == titulo_filme:
                if quantidade_ingressos > filme["Acentos"]:
                    print("Desculpe, não há ingressos suficientes disponíveis para este filme.")
                    break

                custo_total = quantidade_ingressos * filme["preço"]

                if saldo_atual < custo_total:
                    print("Saldo insuficiente para realizar a compra.")
                    break

                assentos_vendidos = 0
                assentos_disponiveis = list(range(1, filme['Acentos'] + 1))
                while assentos_vendidos < quantidade_ingressos:
                    assento = input(f"Digite o número do assento desejado (disponíveis: {assentos_disponiveis}): ")
                    if assento.isdigit() and int(assento) in assentos_disponiveis:
                        assento = int(assento)
                        assentos_disponiveis.remove(assento)
                        assentos_vendidos += 1 
                        ingressos_comprados.append({"Filme": filme['titulo'].lower(), "assento": assento})
                        
                        print(f"Ingresso comprado para o assento {assento} do filme '{filme['titulo']}'.")

                filme["Acentos"] -= quantidade_ingressos
                saldo_atual -= custo_total
                filme["ingressos_vendidos"] += quantidade_ingressos

                print(f"{quantidade_ingressos} ingresso(s) comprado(s) com sucesso para o filme '{filme['titulo']}'.")
                print(f"Saldo restante: R${saldo_atual:.2f}")
                saldos.clear()
                saldos.append(saldo_atual)
                return

        print("Filme não encontrado.")

def cancelar_compra():
    print("\n== Cancelar Compra e Pedir Reembolso ==")

    if  len(ingressos_comprados) < 1:
        print("Você ainda não comprou ingressos.")
        return

    
    saldo_atual = sum(saldos)
    print(f"Seu saldo atual é: R${saldo_atual:.2f}")
    
   
    print("\nIngressos comprados:")
    for ingresso in ingressos_comprados:
        print(f"- Filme: {ingresso['Filme']}, assento: {ingresso['assento']}")

   
    titulo_filme = input("\nDigite o título do filme que deseja cancelar a compra: ").lower()

    if ingresso in ingressos_comprados:
        titulo_filme = ingresso["Filme"]
        assento_cancelar = int(input("Quantos ingressos deseja cancelar: "))

        
        if assento_cancelar <= 0:
            print("Número de assentos maior que a quantidade disponivel.")
            return

        if assento_cancelar > 42 :
            print("Número de assentos maior que a quantidade disponivel.")
            return

        for filme in gerenciamento.filmes:
            if filme["titulo"].lower() == titulo_filme:
                filme["Acentos"] += assento_cancelar
                saldos.append(filme["preço"])

        
        ingressos_comprados.remove(ingresso)

        print(f"{assento_cancelar} ingresso(s) cancelado(s) com sucesso para o filme '{titulo_filme}'.")
        print(f"Seu saldo atual é: R${saldo_atual:.2f}")

    else:
        print("Você não comprou ingressos para este filme.")