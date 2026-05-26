def exercicio_03():    
    try:
        num = input("Digite um número: ")

        # Verifica se a entrada é um número válido (positivo ou negativo)
        if num.lstrip("-").isdigit():
            num = int(num)

            if num != 0:   # se NÃO for igual a zero
                print("O número não é zero.")
            else:
                print("O número é zero.")
        else:
            print("Você não digitou um número inteiro válido.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")