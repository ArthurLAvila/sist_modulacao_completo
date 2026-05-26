def exercicio_05():
    """
    Este exercício cria dois conjuntos e mostra:
    - Se o primeiro é subconjunto do segundo
    - Se o segundo é superconjunto do primeiro
    - Se eles são disjuntos (não têm elementos em comum)

    Autor: Arthur Land Avila  
    Data: 03/11/2025
    """
    # Crie dois conjuntos.
    # Mostre se o primeiro é subconjunto do segundo e se o segundo é superconjunto do 
    # primeiro. Verifique também se são disjuntos.

    # Cria dois conjuntos pré-definidos
    A = {1, 2, 3}
    B = {1, 2, 3, 4, 5}

    print("Conjunto A:", A)
    print("Conjunto B:", B)

    # Verifica se A é subconjunto de B
    if A.issubset(B):
        print("\nA é subconjunto de B ")
    else:
        print("\nA não é subconjunto de B ")

    # Verifica se B é superconjunto de A
    if B.issuperset(A):
        print("B é superconjunto de A ")
    else:
        print("B não é superconjunto de A ")

    # Verifica se são disjuntos (não compartilham elementos)
    if A.isdisjoint(B):
        print("A e B são disjuntos  (não têm elementos em comum)")
    else:
        print("A e B NÃO são disjuntos  (possuem elementos em comum)")
