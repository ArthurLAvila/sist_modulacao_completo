def exercicio_13():    
    try:
        num1 = input("Digite o primeiro número: ").strip()
        num2 = input("Digite o segundo número: ").strip()

        if num1.lstrip("-").isdigit() and num2.lstrip("-").isdigit():
            num1 = int(num1)
            num2 = int(num2)

            # pelo menos um positivo
            um_positivo = (num1 > 0) or (num2 > 0)
            # pelo menos um par
            um_par = (num1 % 2 == 0) or (num2 % 2 == 0)

            # precisa satisfazer ambas as condições
            if um_positivo and um_par:
                print("Pelo menos um é positivo e pelo menos um é par.")
            else:
                print("Condição não satisfeita.")
        else:
            print("Entrada inválida. Digite números inteiros.")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

    print("-" * 30)