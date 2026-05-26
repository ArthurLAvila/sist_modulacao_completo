def exercicio_01():

    try:
        valor1 = int(input("Digite um número: "))
        valor2 = int(input("Digite outro número: "))

        # Usa 'and' para verificar se ambos são pares
        if valor1 % 2 == 0 and valor2 % 2 == 0:
            print("Os dois números são pares.")
        else:
            print("Pelo menos um dos números não é par.")

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
