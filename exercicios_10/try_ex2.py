def exercicio_02():
    """
        Este algoritmo pede dois números ao usuário e exibe o resultado da divisão,
        tratando entradas inválidas e divisão por zero.

        Autor: Arthur Land Avila
        Data: 16/10/2025
    """

    # Faça um programa que peça dois números ao usuário e exiba o resultado da divisão. Trate
    # divisão por zero e entradas inválidas.


    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 / num2
        print(f"\nO resultado da divisão de {num1} por {num2} é: {resultado:.2f}")

    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos.")
    except ZeroDivisionError:
        print("\nErro: Não é possível dividir por zero.")


