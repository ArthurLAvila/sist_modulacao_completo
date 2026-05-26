"""
Usa map e filter em uma lista de nomes fornecida pelo usuário.

Autor: Arthur Land Avila
Data: 17/11/2025

"""
# Exercício 17:
# Use map para colocar todos os nomes em maiúsculas e
# filter para selecionar apenas nomes com mais de 4 letras.

def exercicio_17():

    nomes = input("Digite nomes separados por espaço: ").split()

    maiusculos = list(map(lambda n: n.upper(), nomes))
    filtrados = list(filter(lambda n: len(n) > 4, maiusculos))

    print("Maiúsculos:", maiusculos)
    print("Mais de 4 letras:", filtrados)


exercicio_17()
