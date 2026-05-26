"""
Lambda que verifica se o primeiro valor é maior que o segundo.

Autor: Arthur Land Avila
Data: 17/11/2025

"""
# Exercício 12:
# Crie um lambda maior que com dois valores fornecidos pelo usuário.

def exercicio_12():


    maior_que = lambda a, b: a > b

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Resultado:", maior_que(n1, n2))


exercicio_12()
