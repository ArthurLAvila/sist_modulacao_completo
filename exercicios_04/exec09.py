def exercicio_09():
    try:
        texto = "python é incrível!"
        letra = input("Digite uma letra: ").strip().lower()

        # Verifica se é uma única letra do alfabeto e se está no texto
        if len(letra) == 1 and letra.isalpha():
            if letra in texto:
                print("A letra está no texto.")
            else:
                print("A letra NÃO está no texto.")
        else:
            print("Entrada inválida. Digite apenas uma única letra do alfabeto.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")