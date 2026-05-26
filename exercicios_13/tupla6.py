def exercicio_06():
    """
    Lista de Exercícios – Tuplas
    Autor: Arthur Land Avila
    Data: 28/10/2025

    """

    # Crie uma tupla com nomes de frutas e mostre-a.
    # Depois, exiba uma nova tupla ordenada alfabeticamente, sem alterar a original.
    # Mostre também a tupla invertida usando slicing ([::-1]).


    frutas = ("Banana", "Abacaxi", "Uva", "Morango", "Laranja")
    print(f"\nTupla original: {frutas}")
    ordenada = tuple(sorted(frutas))
    invertida = frutas[::-1]
    print(f"Tupla ordenada: {ordenada}")
    print(f"Tupla invertida: {invertida}")
