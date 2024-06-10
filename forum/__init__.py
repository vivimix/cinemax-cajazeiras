import gerenciamento

def deixar_feedback():
    print("\n== Deixar Feedback ==")
    
    while True:
        
        print("\nFilmes disponíveis:")
        for filme in gerenciamento.filmes:
            print(f"- {filme['titulo']} ({filme['genero']}) - Ingresso: R${filme['preço']:.2f}")

        
        titulo_filme = input("\nDigite o título do filme que você deseja avaliar: ").lower()
        
        
        for filme in gerenciamento.filmes:
            if filme["titulo"].lower() == titulo_filme:
                print(f"\nVocê selecionou o filme '{filme['titulo']}' ({filme['genero']})")
                
                
                comentario = input("Deixe um comentário sobre o filme: ")
                
                
                while True:
                    try:
                        avaliacao = float(input("Digite uma avaliação de 0 a 5 estrelas para este filme: "))
                        if 0 <= avaliacao <= 5:
                            break
                        else:
                            print("Avaliação inválida. Por favor, insira uma avaliação de 0 a 5 estrelas.")
                    except ValueError:
                        print("Por favor, insira um número válido.")

                print(f"\nSeu comentário sobre o filme '{titulo_filme}': {comentario}")
                print(f"Sua avaliação: {avaliacao:.1f} estrelas")
                print("Obrigado pelo seu feedback!")
                return
        
        print("Filme não encontrado. Por favor, tente novamente.")