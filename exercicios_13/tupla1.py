def exercicio_01():
    """
    Lista de Exercícios – Tuplas
    Autor: Arthur Land Avila
    Data: 28/10/2025

    Objetivo:
    Praticar o uso de tuplas, listas, conversões de tipo e estruturas condicionais (match case).
    Cada exercício contém validações e tratamento de erros.
    """

    # Peça ao usuário para informar dois números inteiros e armazene-os em uma tupla.
    # Mostre a tupla criada e exiba seus elementos separadamente: primeiro e segundo número.

    try:
        n1 = int(input("Digite o primeiro número inteiro: "))
        n2 = int(input("Digite o segundo número inteiro: "))
        numeros = (n1, n2)
        print(f"\nTupla criada: {numeros}")
        print(f"Primeiro número: {numeros[0]}")
        print(f"Segundo número: {numeros[1]}")
    except ValueError:
        print("Erro: Insira apenas números inteiros válidos!")