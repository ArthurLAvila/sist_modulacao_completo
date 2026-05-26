def exercicio_09():
    """
    Lista de Exercícios – Tuplas
    Autor: Arthur Land Avila
    Data: 28/10/2025

    """

    # Crie uma tupla com números inteiros.
    # Peça ao usuário para informar um número e conte quantas vezes ele aparece na tupla.
    # Exiba também a posição da primeira ocorrência.
    # Se o número não estiver presente, mostre uma mensagem apropriada.



    tupla_numeros = (2, 5, 7, 2, 9, 2, 10)
    print(f"\nTupla de números: {tupla_numeros}")
    try:
        busca = int(input("Digite um número para procurar: "))
        if busca in tupla_numeros:
            print(f"O número {busca} aparece {tupla_numeros.count(busca)} vez(es).")
            print(f"Primeira ocorrência na posição {tupla_numeros.index(busca)}.")
        else:
            print("O número informado não está na tupla.")
    except ValueError:
        print("Erro: digite um número inteiro válido!")