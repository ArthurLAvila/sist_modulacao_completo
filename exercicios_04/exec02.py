def exercicio_02():

    try:
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")

        # Verifica se as entradas são válidas (incluindo números negativos)
        if num1.lstrip("-").isdigit() and num2.lstrip("-").isdigit():
            num1 = int(num1)
            num2 = int(num2)

            # Verifica se pelo menos um é negativo
            if num1 < 0 or num2 < 0:
                print("Pelo menos um dos números é negativo.")
            else:
                print("Nenhum dos números é negativo.")
        else:
            print("Você não digitou números inteiros válidos.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
