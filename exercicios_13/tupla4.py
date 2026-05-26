def exercicio_04():
    """
    Lista de Exercícios – Tuplas
    Autor: Arthur Land Avila
    Data: 28/10/2025

    """

    # Crie uma tupla de nomes pré-definidos.
    # Peça ao usuário para digitar um nome e verifique se ele está presente na tupla.
    # Exiba uma mensagem indicando se o nome foi encontrado e, se sim, a posição do primeiro elemento.

    nomes_fixos = ("Arthur", "Lívia", "Mariana", "Joana", "Gabriel")
    nome_busca = input("\nDigite um nome para procurar na tupla: ").strip().capitalize()

    if nome_busca in nomes_fixos:
        posicao = nomes_fixos.index(nome_busca)
        print(f"{nome_busca} foi encontrado na posição {posicao}.")
    else:
        print(f"{nome_busca} não foi encontrado na tupla.")