def exercicio_08():
    """
    Lista de Exercícios – Tuplas
    Autor: Arthur Land Avila
    Data: 28/10/2025

    """

    # Crie uma tupla com vários preços de produtos digitados pelo usuário.
    # Depois, peça um percentual de desconto.
    # Gere uma nova tupla com os preços já descontados, sem modificar a original.
    # Exiba as duas tuplas.

    try:
        quantidade = int(input("\nQuantos preços deseja cadastrar? "))
        precos = []
        for i in range(quantidade):
            while True:
                preco = input(f"Digite o preço {i + 1}: ").replace(",", ".")
                try:
                    preco_float = float(preco)
                    precos.append(preco_float)
                    break
                except ValueError:
                    print("Erro: insira um valor numérico válido.")
        precos_tupla = tuple(precos)
        desconto = float(input("Digite o percentual de desconto: "))
        nova_tupla = tuple(round(p * (1 - desconto / 100), 2) for p in precos_tupla)
        print(f"\nPreços originais: {precos_tupla}")
        print(f"Preços com desconto de {desconto}%: {nova_tupla}")
    except ValueError:
        print("Erro: entrada inválida!")