"""
Função que calcula e retorna a média de três números.

Autor: Arthur Land Avila
Data: 17/11/2025

"""

# Exercício 5:
# Crie uma função media que retorna a média de três números.

def media(n1, n2, n3):

    return (n1 + n2 + n3) / 3


print("\n--- Exercício 5 ---")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
print("Média:", media(a, b, c))
