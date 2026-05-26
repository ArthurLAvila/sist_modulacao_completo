def exercicio_07():
    try:
        entrada = input("Digite um número inteiro: ")

        if entrada.lstrip("-").isdigit():
            numero = int(entrada)

            if numero % 3 == 0 and numero % 5 == 0:
                print(f"{numero} é múltiplo de 3 e 5")
            elif numero % 3 == 0:
                print(f"{numero} é múltiplo de 3")
            elif numero % 5 == 0:
                print(f"{numero} é múltiplo de 5")
            else:
                print(f"{numero} não é múltiplo nem de 3 nem de 5")
        else:
            print("Entrada inválida! Digite apenas números inteiros.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

    print("-" * 30)
