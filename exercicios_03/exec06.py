def exercicio_06():
    try:
        num1 = input("Digite o 1º número: ")
        num2 = input("Digite o 2º número: ")
        num3 = input("Digite o 3º número: ")

        if num1.replace(".", "", 1).lstrip("-").isdigit() and \
           num2.replace(".", "", 1).lstrip("-").isdigit() and \
           num3.replace(".", "", 1).lstrip("-").isdigit():

            n1 = float(num1)
            n2 = float(num2)
            n3 = float(num3)

            maior = max(n1, n2, n3)
            print(f"O maior número é: {maior}")

            if n1 <= n2 and n1 <= n3:
                if n2 <= n3:
                    print("Ordem crescente:", n1, n2, n3)
                else:
                    print("Ordem crescente:", n1, n3, n2)
            elif n2 <= n1 and n2 <= n3:
                if n1 <= n3:
                    print("Ordem crescente:", n2, n1, n3)
                else:
                    print("Ordem crescente:", n2, n3, n1)
            else:
                if n1 <= n2:
                    print("Ordem crescente:", n3, n1, n2)
                else:
                    print("Ordem crescente:", n3, n2, n1)
        else:
            print("Entrada inválida! Digite apenas números (use ponto para decimais).")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

    print("-" * 30)