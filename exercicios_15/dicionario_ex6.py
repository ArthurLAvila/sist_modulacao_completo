def exercicio_06():
    """
    Exercício 6 – Conversões de dicionário
    Autor: Arthur Land Avila
    Data: 10/11/2025
    """

    # Dicionário de exemplo
    dados = {"nome": "Arthur", "idade": 24, "cidade": "São Paulo"}

    # Converte para outras estruturas
    tuplas = list(dados.items())
    chaves = list(dados.keys())
    valores = list(dados.values())

    print("Lista de tuplas:", tuplas)
    print("Lista de chaves:", chaves)
    print("Lista de valores:", valores)

    # Reconvertendo a lista de tuplas em dicionário
    novo_dict = dict(tuplas)
    print("\nNovo dicionário reconstruído:", novo_dict)
