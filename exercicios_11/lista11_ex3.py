def exercicio_03():
    """
    Exercício 3 - Preços e limite
    """
    # Enunciado:
    # Peça ao usuário para inserir vários preços de produtos float em uma lista.
    # Valide cada entrada.
    # Depois, solicite um valor limite.
    # Exiba todos os preços da lista que são maiores que esse limite, usando um laço.

    try:
        n = int(input("Quantos preços deseja inserir? "))
        precos = []
        for i in range(n):
            while True:
                try:
                    preco = float(input(f"Digite o preço {i+1}: R$"))
                    precos.append(preco)
                    break
                except ValueError:
                    print("Entrada inválida! Digite um valor numérico.")
        limite = float(input("\nDigite um valor limite: R$"))
        print(f"\nPreços maiores que R${limite:.2f}:")
        for p in precos:
            if p > limite:
                print(f"R${p:.2f}")
    except ValueError:
        print("Erro: entrada inválida!")
