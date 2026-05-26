"""
Função que recebe dois números e retorna o produto entre eles.

Autor: Arthur Land Avila
Data: 17/11/2025

"""

def multiplicar(valor1, valor2):
    # Exercício 3:
    # Crie uma função multiplicar(valor1, valor2) que recebe dois números
    # e retorna o produto. Pergunte ao usuário dois números e mostre
    # o resultado usando a função multiplicar.

    return valor1 * valor2


print("\n--- Exercício 3 ---")
v1 = float(input("Digite o primeiro número: "))
v2 = float(input("Digite o segundo número: "))
resultado = multiplicar(v1, v2)
print("Resultado da multiplicação:", resultado)
