"""
Retorna True se for par e False se for ímpar.

Autor: Arthur Land Avila
Data: 17/11/2025

"""
# Exercício 4:
# Crie uma função eh_par que retorna True se o número for par
# e False se for ímpar.

def eh_par(numero):
    

    return numero % 2 == 0


print("\n--- Exercício 4 ---")
num = int(input("Digite um número inteiro: "))
print("É par?", eh_par(num))