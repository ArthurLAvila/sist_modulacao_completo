def exercicio_03():
    """
    Este exercício cria dois conjuntos de números inteiros A e B, definidos diretamente no código.
    Em seguida, mostra:
    - A união dos conjuntos (A | B)
    - A interseção (A & B)
    - A diferença (A - B)
    - A diferença simétrica (A ^ B)

    Autor: Arthur Land Avila  
    Data: 03/11/2025
    """

    # Crie dois conjuntos de números inteiros A e B, definidos diretamente no código.
    # Mostre: a união dos conjuntos A | B, a interseção A & B, a diferença A - B e A diferença 
    # simétrica A ^ B.

    # Cria dois conjuntos pré-definidos
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    print("Conjunto A:", A)
    print("Conjunto B:", B)

    # União
    uniao = A | B
    print("\nUnião (A | B):", uniao)

    # Interseção
    intersecao = A & B
    print("Interseção (A & B):", intersecao)

    # Diferença
    diferenca = A - B
    print("Diferença (A - B):", diferenca)

    # Diferença Simétrica
    diferenca_simetrica = A ^ B
    print("Diferença Simétrica (A ^ B):", diferenca_simetrica)
