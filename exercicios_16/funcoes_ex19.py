"""
Lambda que converte Celsius para Fahrenheit e aplica em uma lista.
    
Autor: Arthur Land Avila
Data: 17/11/2025
"""
# Exercício 19:
# Crie uma função lambda para converter Celsius para Fahrenheit
# e teste com uma lista de temperaturas.

def exercicio_19():

    celsius = [0, 10, 20, 30, 40]

    converter = lambda c: (c * 9/5) + 32
    fahrenheit = list(map(converter, celsius))

    print("Celsius:", celsius)
    print("Fahrenheit:", fahrenheit)


exercicio_19()

















