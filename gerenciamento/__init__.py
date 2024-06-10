import menu_do_adm

usuarios_dicionario_adm = {}  
emails = []    
senhas = []    
usuarios = []
idade = []


usuarios_dicionario_clientes = {}
emails2 = []
senhas2 = []
usuarios2 = []
idade2 = []



filmes = [
    {"titulo": "Jumanji", "sala_cinema": "Sala 1", "idade indicada": 12, "genero": "Ficção Científica e Aventura", "ingressos": 42, "Acentos": 42, "ingressos_vendidos": 0 , "preço": 40.00},
    {"titulo": "Homem-Aranha", "sala_cinema": "Sala 2", "ano": 2002, "genero": "Ficção Cientifica e Aventura", "ingressos": 42, "Acentos": 42, "ingressos_vendidos": 0 , "preço": 45.90},
    {"titulo": "O Poderoso Chefão", "sala_cinema": "Sala 3", "ano": 1972, "genero": "Crime/Drama", "ingressos": 42, "Acentos": 42, "ingressos_vendidos": 0 , "preço": 30.50}
]

def buscar_filme():
    titulo = input("\nDigite o título do filme que deseja buscar: ")
    for filme in filmes:
        if filme["titulo"].lower() == titulo.lower():
            print("\nTítulo:", filme["titulo"])
            print("Sala de cinema:", filme["sala_cinema"])
            print("Idade indicada:", filme.get("idade indicada", "Não informada"))
            print("Ano:", filme.get("ano", "Não informado"))
            print("Gênero:", filme["genero"])
            print("Ingressos disponíveis:", filme["ingressos"])
            menu_do_adm.menu()
            return
    print("\nFilme não encontrado.")

def adicionar_filme():
    titulo = input("\nDigite o título do filme: ")
    sala_cinema = input("\nDigite a sala de cinema: ")
    idade_indicada = input("\nDigite a idade indicada (opcional - deixe em branco se não aplicável): ")
    ano = int(input("\nDigite o ano de lançamento (opcional - deixe em branco se não aplicável): ") or 0)
    genero = input("\nDigite o gênero do filme: ")
    ingressos = int(input("\nDigite o número de ingressos disponíveis: "))
    filmes.append({"titulo": titulo, "sala_cinema": sala_cinema, "idade indicada": idade_indicada, "ano": ano, "genero": genero, "ingressos": ingressos, "Acentos": 42, "ingressos_vendidos": 0})
    print("Filme adicionado com sucesso!")
    menu_do_adm.menu()

def atualizar_filme():
    while True:
        titulo = input("\nDigite o título do filme que deseja atualizar (ou digite 'voltar' para retornar ao menu): ").lower()

        if titulo == 'voltar':
            print("Voltando ao menu anterior.")
            return

        for filme in filmes:
            if filme["titulo"].lower() == titulo:
                print("\n== Atualização do Filme ==")
                sala_cinema = input("\nDigite a nova sala de cinema: ")
                idade_indicada = input("\nDigite a nova idade indicada (opcional - deixe em branco se não aplicável): ")
                ano = int(input("\nDigite o novo ano de lançamento (opcional - deixe em branco se não aplicável): ") or 0)
                genero = input("\nDigite o novo gênero do filme: ")
                ingressos = int(input("\nDigite o novo número de ingressos disponíveis: "))

                filme.update({
                    "sala_cinema": sala_cinema,
                    "idade indicada": idade_indicada,
                    "ano": ano,
                    "genero": genero,
                    "ingressos": ingressos
                })

                print("\nDados do filme atualizados com sucesso.")
                menu_do_adm.menu()
                return

        print("Filme não encontrado.")

def remover_filme():
    titulo = input("\nDigite o título do filme que deseja remover: ")
    for filme in filmes:
        if filme["titulo"].lower() == titulo.lower():
            filmes.remove(filme)
            print("Filme removido com sucesso.")
            menu_do_adm.menu()
            return
    print("\nFilme não encontrado.")

def ver_ingressos():
    print("\nLista de filmes e seus ingressos disponíveis:")
    for filme in filmes:
        print(f"\nTítulo: {filme['titulo']} - Ingressos disponíveis: {filme['ingressos']}")
    menu_do_adm.menu()    

def remover_ingressos():
    titulo = input("\nDigite o título do filme para remover ingressos: ")
    for filme in filmes:
        if filme["titulo"].lower() == titulo.lower():
            quantidade = int(input("\nQuantos ingressos deseja remover? "))
            if quantidade <= filme["ingressos"]:
                filme["ingressos"] -= quantidade
                print(f"\n{quantidade} ingressos removidos com sucesso para o filme {filme['titulo']}.")
                menu_do_adm.menu()
            else:
                print("\nQuantidade de ingressos solicitada maior do que a disponível.")
            return
    print("\nFilme não encontrado.")

def relatorio_vendas():
    total_ingressos_vendidos = 0
    lucro_total = 0

    print("\n== Relatório de Vendas ==")
    if not filmes:
        print("Não há filmes cadastrados.")
    else:
        print("Filmes:\n")
        for filme in filmes:
            ingressos_vendidos = filme.get('ingressos_vendidos', 0)
            lucro_filme = ingressos_vendidos * filme['preço']
            total_ingressos_vendidos += ingressos_vendidos
            lucro_total += lucro_filme

            print(f"Título: {filme['titulo']}, Ingressos Vendidos: {ingressos_vendidos}, Lucro: R${lucro_filme:.2f}")

        print("\nTotal de Ingressos Vendidos:", total_ingressos_vendidos)
        print("Lucro Total: R$", lucro_total)


def gerenciar_horarios_exibicao():
    print("\n== Gerenciamento de Horários de Exibição ==")
    titulo_filme = input("Digite o título do filme para o qual deseja gerenciar os horários de exibição: ").lower()

    
    filme_encontrado = False
    for filme in filmes:
        if filme["titulo"].lower() == titulo_filme:
            filme_encontrado = True
            print(f"\nHorários de Exibição para o filme '{titulo_filme}':")
            if filme.get("horarios"):
                for horario in filme["horarios"]:
                    print(f"- {horario}")
            else:
                print("Nenhum horário de exibição cadastrado para este filme ainda.")

            opcao = input("\nEscolha uma opção:\n1 - Adicionar novo horário\n2 - Atualizar horário existente\n3 - Remover horário\n0 - Voltar\nDigite sua opção: ")

            if opcao == "1":
                novo_horario = input("Digite o novo horário de exibição (formato HH:MM): ")
                filme.setdefault("horarios", []).append(novo_horario)
                print(f"Novo horário '{novo_horario}' adicionado com sucesso para o filme '{titulo_filme}'.")
            elif opcao == "2":
                if not filme.get("horarios"):
                    print("Nenhum horário de exibição cadastrado para este filme ainda.")
                    continue
                horario_antigo = input("Digite o horário de exibição que deseja atualizar: ")
                novo_horario = input("Digite o novo horário de exibição (formato HH:MM): ")
                if horario_antigo in filme["horarios"]:
                    filme["horarios"][filme["horarios"].index(horario_antigo)] = novo_horario
                    print(f"Horário '{horario_antigo}' atualizado para '{novo_horario}' com sucesso.")
                else:
                    print("Horário não encontrado.")
            elif opcao == "3":
                if not filme.get("horarios"):
                    print("Nenhum horário de exibição cadastrado para este filme ainda.")
                    continue
                horario_remover = input("Digite o horário de exibição que deseja remover: ")
                if horario_remover in filme["horarios"]:
                    filme["horarios"].remove(horario_remover)
                    print(f"Horário '{horario_remover}' removido com sucesso.")
                else:
                    print("Horário não encontrado.")
            elif opcao == "0":
                print("Voltando ao menu principal.")
                break
            else:
                print("Opção inválida. Tente novamente.")
            break

    if not filme_encontrado:
        print("Filme não encontrado.")

def gerenciar_reservas_assentos():
    while True:
        print("\n== Gerenciamento de Reservas de Assentos ==")
        titulo_filme = input("Digite o título do filme para o qual deseja gerenciar as reservas de assentos: ").lower()

        filme_encontrado = False
        for filme in filmes:
            if filme["titulo"].lower() == titulo_filme:
                filme_encontrado = True
                print(f"\nReservas de Assentos para o filme '{titulo_filme}':")
                if filme.get("reservas"):
                    for reserva in filme["reservas"]:
                        print(f"- Assento: {reserva['assento']}, Cliente: {reserva['cliente']}")
                else:
                    print("Nenhuma reserva de assento cadastrada para este filme ainda.")

                while True:
                    opcao = input("\nEscolha uma opção:\n1 - Adicionar reserva\n2 - Remover reserva\n0 - Voltar\nDigite sua opção: ")

                    if opcao == "1":
                        assento = input("Digite o número do assento que deseja reservar: ")
                        cliente = input("Digite o nome do cliente para quem deseja reservar o assento: ")
                        filme.setdefault("reservas", []).append({"assento": assento, "cliente": cliente})
                        print(f"Reserva de assento '{assento}' para o cliente '{cliente}' adicionada com sucesso.")
                    elif opcao == "2":
                        if not filme.get("reservas"):
                            print("Nenhuma reserva de assento cadastrada para este filme ainda.")
                            continue
                        assento_remover = input("Digite o número do assento que deseja remover a reserva: ")
                        for reserva in filme["reservas"]:
                            if reserva["assento"] == assento_remover:
                                filme["reservas"].remove(reserva)
                                print(f"Reserva de assento '{assento_remover}' removida com sucesso.")
                                break
                        else:
                            print("Assento não encontrado.")
                    elif opcao == "0":
                        print("Voltando ao menu principal.")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
                break

        if not filme_encontrado:
            print("Filme não encontrado.")
