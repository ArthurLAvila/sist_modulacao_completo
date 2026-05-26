def exercicio_0():    
    try:
        num = input("Digite um número inteiro: ").strip()

        # Verifica se é inteiro (aceita negativos)
        if num.lstrip("-").isdigit():
            num = int(num)

            # Testes com if/elif/else
            if num == 0:
                print("Zero")
            elif num > 0 and num % 2 == 0:
                print("Positivo e par")
            elif num > 0 and num % 2 != 0:
                print("Positivo e ímpar")
            elif num < 0 and num % 2 == 0:
                print("Negativo e par")
            else:
                print("Negativo e ímpar")
        else:
            print("Entrada inválida. Digite um número inteiro.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")