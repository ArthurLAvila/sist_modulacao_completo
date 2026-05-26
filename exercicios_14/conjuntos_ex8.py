def exercicio_08():
    """
    Exercício 7 – Análise de valores numéricos em conjunto
    Autor: Arthur Land Avila
    Data: 10/11/2025
    """

    # Pedir ao usuário para digitar uma quantidade de valores numéricos,
    # armazená-los em um conjunto e calcular:
    # - o maior valor
    # - o menor valor
    # - a soma total
    # - a quantidade de elementos


    # Cria um conjunto vazio
    valores = set()

    try:
        quantidade = int(input("Quantos valores deseja digitar? "))

        for i in range(quantidade):
            valor = float(input(f"Digite o {i+1}º valor: "))
            valores.add(valor)

        print(f"\nConjunto informado: {valores}")
        print(f"Maior valor: {max(valores)}")
        print(f"Menor valor: {min(valores)}")
        print(f"Soma total: {sum(valores)}")
        print(f"Quantidade de elementos: {len(valores)}")

    except ValueError:
        print(" Digite apenas números válidos!")