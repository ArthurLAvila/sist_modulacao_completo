def exercicio_04():
    """
    Exercício 4 – Verificar existência de chave em dicionário
    Autor: Arthur Land Avila
    Data: 10/11/2025
    """

    # Dicionário pré-definido
    dados = {
        "nome": "Arthur",
        "idade": 24,
        "cidade": "São Paulo"
    }

    chave = input("Digite o nome de uma chave: ")

    if chave in dados:
        print(f"O valor da chave '{chave}' é: {dados[chave]}")
    else:
        print("Essa chave não existe no dicionário.")
