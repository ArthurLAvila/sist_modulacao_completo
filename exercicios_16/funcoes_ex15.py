"""
Função recursiva que mostra números de n até 0.

Autor: Arthur Land Avila
Data: 17/11/2025

"""
# Exercício 15:
# Crie uma função contagem_regressiva que mostre números de n até 0 recursivamente.

def contagem_regressiva(n):
    

    if n < 0:
        return
    print(n)
    contagem_regressiva(n - 1)


valor = int(input("Digite n para contagem regressiva: "))
contagem_regressiva(valor)
