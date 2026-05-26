"""
Lambda que calcula o quadrado de um número informado pelo usuário.

Autor: Arthur Land Avila
Data: 17/11/2025

"""
# Exercício 11:
# Crie um lambda quadrado de um número com valores fornecidos pelo usuário.

def exercicio_11():
    

    quadrado = lambda x: x * x

    valor = int(input("Digite um número: "))
    print("Quadrado:", quadrado(valor))


exercicio_11()
