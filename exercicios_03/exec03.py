def exercicio_03():
    try:
        entrada = input("Digite um número inteiro: ")

        if entrada.lstrip("-").isdigit():
            numero = int(entrada)

            if numero == 0:
                print("Zero")
            elif numero > 0:
                if numero % 2 == 0:
                    print("Positivo par")
                else:
                    print("Positivo ímpar")
            else:
                if numero % 2 == 0:
                    print("Negativo par")
                else:
                    print("Negativo ímpar")
        else:
            print("Valor inválido! Digite apenas números inteiros (sem pontos ou vírgulas).")

    except Exception as erro:
        print("Ocorreu um erro inesperado:", erro)

    print("-" * 30)

