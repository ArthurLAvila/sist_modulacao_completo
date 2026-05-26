def exercicio_11():
    """ 
        Este algoritmo solicita 5 números, validando eles a cada entrada e somando em um acumulador.
        Também conta quantas entradas foram validas. Por ultimo exibe a media de números inseridos.

        Autor: Arthur Land Avila
        Data: 16/10/2025
    """

    # Este algoritmo solicita que o usuário digite 5 números.
    # Para cada número, valida a entrada, acumula a soma
    # e conta quantas entradas foram válidas.
    # No final, exibe a média dos números digitados.


    soma = 0
    validos = 0

    for i in range(1, 6):
        try:
            numero = float(input(f"Digite o {i}º número: "))
            soma += numero
            validos += 1
        except ValueError:
            print("Erro: entrada inválida. Este número será ignorado.")

    if validos > 0:
        media = soma / validos
        print(f"\nForam digitados {validos} números válidos.")
        print(f"A soma total é {soma:.1f}.")
        print(f"A média dos números digitados é {media:.1f}.")
    else:
        print("\nNenhum número válido foi digitado.")
