"""
Incrementa a variável global 'contador' em 1 e exibe seu valor.

Autor: Arthur Land Avila
Data: 17/11/2025

"""

# Exercício 6:
# Crie uma variável global contador = 0.
# Crie uma função que incremente contador em 1 e mostre seu valor dentro da função.
# Após chamar a função, imprima o valor de contador fora da função.

contador = 0  # variável global

def incrementar():

    global contador
    contador += 1
    print("Valor dentro da função:", contador)

# Demonstração
if __name__ == "__main__":
    incrementar()
    print("Valor fora da função:", contador)
