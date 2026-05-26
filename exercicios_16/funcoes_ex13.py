"""
Função recursiva que retorna o n-ésimo termo da sequência de Fibonacci.

Autor: Arthur Land Avila
Data: 17/11/2025

"""
# Exercício 13:
# Crie uma função recursiva Fibonacci que retorne o n-ésimo termo.

def fibonacci(n):
    

    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


valor = int(input("Digite n para Fibonacci: "))
print("Fibonacci:", fibonacci(valor))
