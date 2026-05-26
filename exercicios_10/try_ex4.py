def exercicio_04():
    """
        Este algoritmo pede dois numeros inteiros e divide o primeiro pelo segundo. tratando entradas invalidas.

        Autor: Arthur Land Avila
        Data: 16/10/2025
    """

    # Peça dois números inteiros. Divida o primeiro pelo segundo, tratando entrada inválida e 
    #divisão por zero

    try:
        num1 = int(input("Digite um número inteiro: "))
        num2 = int(input("Digite um segundo número inteiro: "))
        
        divisao = num1/num2
        print("O resultado da divisão do primeiro num{num1}, pelo segundo número {num2} é: {divisao}!")
    except ZeroDivisionError:
        print("\nErro: Não é possível dividir por zero.")