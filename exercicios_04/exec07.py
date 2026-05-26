def exercicio_07():        
    try:
        letra = input("Digite uma letra: ").strip()

        # Verifica se é apenas um caractere e se é uma letra do alfabeto
        if len(letra) == 1 and letra.isalpha():
            if letra.lower() in "aeiou":   # se for vogal
                print("É uma vogal.")
            else:
                print("É uma consoante.")  # se for consoante
        else:
            print("Entrada inválida. Digite apenas uma única letra.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")