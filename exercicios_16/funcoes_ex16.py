"""
Usa map, filter e reduce em uma lista fornecida pelo usuário.

Autor: Arthur Land Avila
Data: 17/11/2025

"""
# Exercício 16:
# Crie uma lista de números com valores fornecidos pelo usuário,
# use map para dobrar os valores,
# use filter para selecionar números maiores que 3,
# e reduce para calcular o produto de todos.

from functools import reduce

def exercicio_16():

    lista = input("Digite números separados por espaço: ").split()
    lista = [int(x) for x in lista]

    dobrados = list(map(lambda x: x * 2, lista))
    filtrados = list(filter(lambda x: x > 3, dobrados))
    produto = reduce(lambda a, b: a * b, filtrados) if filtrados else 0

    print("Dobrado:", dobrados)
    print("Filtrado (>3):", filtrados)
    print("Produto:", produto)


exercicio_16()
