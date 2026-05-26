"""
Função que recebe um nome e um sobrenome e exibe o nome completo. 

Autor: Arthur Land Avila
Data: 17/11/2025
    
"""


def imprimir_nome_completo(nome, sobrenome):
    
    # Exercício 1:
    # Crie uma função imprimir_nome_completo(nome, sobrenome)
    # que exibe o nome completo da pessoa.

    nome_completo = nome + " " + sobrenome
    print("Nome completo:", nome_completo)


print("\n--- Exercício 1 ---")
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
imprimir_nome_completo(nome, sobrenome)

