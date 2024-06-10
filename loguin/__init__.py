import gerenciamento
import compra_de_ingressos
import menu_do_adm

def fazer_login():
    while True:
        print("\nComeçando seu login:")
        print("Para voltar ao menu principal, digite 0.")
        email = input("Digite seu email de usuário aqui: ")

      
        if email == "0":
            return

        senha = input("Digite sua senha: ")

        for usuario, dados in gerenciamento.usuarios_dicionario_adm.items():
            if dados["email"] == email and dados["senha"] == senha:
                menu_do_adm.menu()
                return
        else:
            for usuario, dados in gerenciamento.usuarios_dicionario_clientes.items():
                if dados["email"] == email and dados["senha"] == senha:
                    compra_de_ingressos.menu_dos_clientes()
                    print("Login bem-sucedido! Bem-vindo(a) cliente!")
                    return

        print("Dados de login incorretos. Tente novamente.")


        



    



