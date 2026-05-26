def exercicio_02():
    try:
        letra = input("Digite uma letra: ")

        if len(letra) == 1 and letra.isalpha():
            letra = letra.lower()

            match letra:
                case "a" | "e" | "i" | "o" | "u":
                    print(f"A letra '{letra}' é uma VOGAL.")
                case _:
                    print(f"A letra '{letra}' é uma CONSOANTE.")
        else:
            print("Entrada inválida! Digite apenas uma letra do alfabeto.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

    print("-" * 30)