"""
Função recursiva que retorna a soma de 1 até n.

Autor: Arthur Land Avila
Data: 17/11/2025

"""
# Exercício 14:
# Crie uma função recursiva soma_recursiva que retorne a soma de 1 até n.

def soma_recursiva(n):
    

    if n == 1:
        return 1
    return n + soma_recursiva(n - 1)


valor = int(input("Digite n para soma recursiva: "))
print("Soma:", soma_recursiva(valor))
