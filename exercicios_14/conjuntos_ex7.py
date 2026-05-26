def exercicio_07():
    """
    Exercício 6 – Conversão de conjunto em lista e vice-versa
    Autor: Arthur Land Avila
    Data: 10/11/2025

    Objetivo:
    Criar um conjunto com números digitados pelo usuário.
    Converter o conjunto em lista, ordenar os valores e mostrar a lista ordenada.
    Depois, converter novamente a lista em conjunto e mostrar o resultado.
    """

    # Cria um conjunto vazio
    numeros = set()

    # Coleta os números do usuário
    while True:
        entrada = input("Digite um número (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
            numeros.add(int(entrada))
        else:
            print("Entrada inválida! Digite apenas números inteiros. ")

    # Mostra o conjunto original
    print(f"\nConjunto original: {numeros}")

    # Converte o conjunto em lista e ordena
    lista = list(numeros)
    lista.sort()
    print(f"Lista ordenada: {lista}")

    # Converte novamente em conjunto
    novo_conjunto = set(lista)
    print(f"Conjunto reconvertido: {novo_conjunto}")