def exercicio_03():
    """
    Exercício 3 – Atualização e remoção de chaves entre dicionários
    Autor: Arthur Land Avila
    Data: 10/11/2025
    """

    # Cria dois dicionários a partir de entradas do usuário
    dicionario1 = {}
    dicionario2 = {}

    quantidade1 = int(input("Quantos pares deseja adicionar no Dicionário 1? "))
    for i in range(quantidade1):
        chave = input(f"Chave {i+1}: ")
        valor = input(f"Valor para '{chave}': ")
        dicionario1[chave] = valor

    quantidade2 = int(input("\nQuantos pares deseja adicionar no Dicionário 2? "))
    for i in range(quantidade2):
        chave = input(f"Chave {i+1}: ")
        valor = input(f"Valor para '{chave}': ")
        dicionario2[chave] = valor

    # Atualiza dicionário1 com dicionário2
    dicionario1.update(dicionario2)

    # Remove uma chave específica
    chave_remover = input("\nDigite o nome de uma chave para remover: ")
    if chave_remover in dicionario1:
        dicionario1.pop(chave_remover)
        print(f"Chave '{chave_remover}' removida com sucesso!")
    else:
        print("Essa chave não existe.")

    print("\nDicionário final:", dicionario1)
