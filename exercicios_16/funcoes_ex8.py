"""
Recebe um número arbitrário de argumentos numéricos e retorna a soma.

Autor: Arthur Land Avila
Data: 17/11/2025

"""

# Exercício 8:
# Crie uma função soma_numeros que receba qualquer quantidade de números
# e retorne a soma.

def soma_numeros(*numeros):
    
    return sum(numeros)

# Demonstração
if __name__ == "__main__":
    resultado = soma_numeros(2, 5, 10)
    print("Soma:", resultado)
    # exemplo com nenhum argumento
    print("Soma (nenhum argumento):", soma_numeros())
