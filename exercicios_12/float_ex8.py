def exercicio_08():
    """
    Exercício 8
    Peça para o usuário digitar preços e um valor de desconto.
    Gere uma nova lista com os preços descontados.
    """

    # Peça para o usuário digitar preços de vários produtos e armazene em uma lista.
    # Depois, peça para digitar um valor float de desconto.
    # Gere uma nova lista com os preços já descontados, sem modificar a original.
    # Exiba ambas as listas, usando laços para percorrê-las.

    precos = []
    try:
        qtd = int(input("Quantos produtos deseja registrar? "))
        for i in range(qtd):
            while True:
                try:
                    p = float(input(f"Digite o preço do {i+1}º produto: "))
                    precos.append(p)
                    break
                except ValueError:
                    print("Digite um valor numérico válido.")
        desconto = float(input("Digite o percentual de desconto (%): "))
        nova_lista = []
        for p in precos:
            novo_preco = p - (p * desconto / 100)
            nova_lista.append(round(novo_preco, 2))
        print("\nPreços originais:", precos)
        print("Preços com desconto:", nova_lista)
    except ValueError:
        print("Entrada inválida.")