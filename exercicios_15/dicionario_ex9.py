def exercicio_09():
    """
    Exercício 9 – Frutas e cores
    Autor: Arthur Land Avila
    Data: 10/11/2025
    """

    frutas = {
        "maçã": "vermelha",
        "banana": "amarela",
        "uva": "roxa",
        "laranja": "laranja"
    }

    print("Dicionário inicial:", frutas)
    fruta = input("Digite o nome de uma fruta: ").strip().lower()

    if fruta in frutas:
        print(f"A cor da {fruta} é {frutas[fruta]}. Ela será removida do dicionário.")
        frutas.pop(fruta)
    else:
        cor = input(f"Informe a cor da fruta '{fruta}': ").strip().lower()
        frutas[fruta] = cor
        print(f"'{fruta}' adicionada ao dicionário com a cor '{cor}'.")

    print("\nDicionário atualizado:", frutas)
