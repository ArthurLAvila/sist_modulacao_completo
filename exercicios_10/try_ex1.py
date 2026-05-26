def exercicio_01():
    """
        Este algoritmo consiste em converter a temperatura em Celsius digitada pelo usuário em Fahrenheit, 
        usando tratamento de erro com try/except.

        Autor: Arthur Land Avila
        Data: 16/10/2025
    """
    # Peça para o usuário digitar a temperatura em graus Celsius. Garantir que seja um número 
    # decimal válido. Converta a temperatura para Fahrenheit e exiba o resultado.

    # Conversão de Celsius para Fahrenheit: F = (C * 9/5) + 32

    try:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"\nA temperatura de {celsius:.2f}°C corresponde a {fahrenheit:.2f}°F.")
    except ValueError:
        print("\nErro: Por favor, digite um número válido para a temperatura.")
