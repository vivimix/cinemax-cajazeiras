import cadastro
import loguin

def menu_principal():

    while True:
        print("\n==Cine Max de Cajazeiras==")
        print("\n ==Menu principal==")
        print("\n Bem vindo ao Cine Max de Cajazeiras \n  \n Para acessar o sistema faça login \n Se cadastre ao digitar - 1 \n Realize login ao digitar - 2\n Para sair do sistema digite - 0")

        resposta = input("\nDigite sua resposta: ")
        if (resposta == "1"):
            cadastro.cadastrar_usuario()
        
        elif (resposta == "2"):
            loguin.fazer_login()

        elif (resposta == "0"):
            print("\nDesligando o sistema...")
            print("Fim da seção.")
            
        else:
            print("\n Opção inválida, tente novamente.")
            

menu_principal()
