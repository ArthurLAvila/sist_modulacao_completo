def exercicio_08():
    """
    Exercício 8 - Desconto em preços
    """
    # Enunciado:
    # Peça para o usuário digitar preços de vários produtos e armazene em uma lista.
    # Depois, peça para digitar um valor float de desconto.
    # Gere uma nova lista com os preços já descontados, sem modificar a original.
    # Exiba ambas as listas, usando laços para percorrê-las.

    try:
        n = int(input("Quantos produtos deseja registrar? "))
        precos = []
        for i in range(n):
            while True:
                try:
                    preco = float(input(f"Digite o preço do produto {i+1}: R$"))
                    precos.append(preco)
                    break
                except ValueError:
                    print("Entrada inválida.")
        desconto = float(input("Digite o valor de desconto (%): "))
        nova_lista = [p - (p * desconto / 100) for p in precos]

        print("\n--- Lista original ---")
        for p in precos:
            print(f"R${p:.2f}")
        print("\n--- Lista com desconto ---")
        for p in nova_lista:
            print(f"R${p:.2f}")
    except ValueError:
        print("Erro: digite números válidos.")