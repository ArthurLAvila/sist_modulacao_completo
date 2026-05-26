def exercicio_09():
    """
    Exercício 9 – Adicionar ou remover frutas de um conjunto
    Autor: Arthur Land Avila
    Data: 10/11/2025
    """

    # Objetivo:
    # Criar um conjunto com nomes de frutas.
    # Pedir ao usuário para digitar uma fruta e verificar se ela está no conjunto.
    # Se estiver, removê-la. Caso contrário, adicioná-la.
    # Mostrar o conjunto atualizado após a operação.


    # Conjunto inicial de frutas
    frutas = {"maçã", "banana", "laranja", "uva", "pera"}

    print(f"Conjunto inicial de frutas: {frutas}")

    # Solicita uma fruta ao usuário
    fruta = input("Digite o nome de uma fruta: ").strip().lower()

    # Verifica se a fruta está no conjunto
    if fruta in frutas:
        frutas.remove(fruta)
        print(f"'{fruta}' removida do conjunto!")
    else:
        frutas.add(fruta)
        print(f"'{fruta}' adicionada ao conjunto!")

    # Mostra o conjunto atualizado
    print(f"Conjunto atualizado: {frutas}")
