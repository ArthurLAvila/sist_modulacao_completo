def exercicio_05():
    """
        Este algoritmo pede um número inteiro para fazer aq sua raiz quadrada, e trata qualquer erro possível exibindo uma mensagem de erro. 
        E permite ao usuário continuar no programa.  

        Autor: Arthur Land Avila
        Data: 16/10/2025
    """

    # Solicite um número inteiro para calcular a raiz quadrada. Trate qualquer erro e exibir a 
    # mensagem do erro.

    import math

    try:
        numero = int(input("Digite um número inteiro: "))
        raiz = math.sqrt(numero)
        print(f"\nA raiz quadrada de {numero} é {raiz:.2f}.")
    except ValueError as erro:
        print(f"\nErro: {erro}")
