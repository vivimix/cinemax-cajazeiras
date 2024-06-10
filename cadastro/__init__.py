import gerenciamento

def cadastrar_usuario():
    while True:
        print("\n1 - Criar conta de ADM\n2 - Criar conta de cliente\n0 - Voltar")

        cadastro = input("Digite sua resposta aqui: ")

        if cadastro == "1":
            criar_conta_adm()
        elif cadastro == "2":
            criar_conta_cliente()
        elif cadastro == "0":
            print("\nVoltando para o menu principal.")
            break
        else:
            print("\nOpção inválida, tente novamente.")

def criar_conta_adm():
    usuario = obter_dados_usuario("ADM")

    gerenciamento.usuarios_dicionario_adm[usuario["nome"]] = usuario
    print(f"Bem-vindo(a) {usuario['nome']}, sua conta de ADM foi criada.")

def criar_conta_cliente():
    usuario = obter_dados_usuario("cliente")

    
    gerenciamento.usuarios_dicionario_clientes[usuario["nome"]] = usuario
    print(f"Bem-vindo(a) {usuario['nome']}, sua conta de cliente foi criada.")

def obter_dados_usuario(tipo):
    while True:
        usuario = input("\nDigite o nome de usuário: ")
        if len(usuario) < 3:
            print("Nome de usuário deve ter pelo menos 3 caracteres.")
        elif usuario in gerenciamento.usuarios_dicionario_adm or usuario in gerenciamento.usuarios_dicionario_clientes:
            print("Nome de usuário já está em uso.")
        else:
            break

    while True:
        email = input("\nDigite o seu email de usuário: ")
        if "@gmail.com" not in email or len(email) < 10:
            print("O email deve ser do tipo @gmail.com e ter pelo menos 10 caracteres.")
        elif email in [u["email"] for u in gerenciamento.usuarios_dicionario_adm.values()] or email in [u["email"] for u in gerenciamento.usuarios_dicionario_clientes.values()]:
            print("Este email já está em uso.")
        else:
            break

    while True:
        senha = input("\nCrie sua senha: ")
        if len(senha) < 3:
            print("Senha deve ter pelo menos 3 caracteres.")
        elif senha in [u["senha"] for u in gerenciamento.usuarios_dicionario_adm.values()] or senha in [u["senha"] for u in gerenciamento.usuarios_dicionario_clientes.values()]:
            print('Esta senha já está em uso.')
        else:
            break

    return {"nome": usuario, "email": email, "senha": senha, "tipo": tipo}