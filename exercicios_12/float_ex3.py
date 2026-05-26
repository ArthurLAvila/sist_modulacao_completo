def exercicio_03():
    """
    Exercício 3
    Peça ao usuário para inserir vários preços (float) em uma lista.
    Depois, solicite um valor limite e mostre todos os preços maiores que ele.
    """

    # Peça ao usuário para inserir vários preços de produtos float em uma lista.
    # Valide cada entrada.
    # Depois, solicite um valor limite.
    # Exiba todos os preços da lista que são maiores que esse limite, usando um laço.


    precos = []
    try:
        quantidade = int(input("Quantos preços deseja inserir? "))
        for i in range(quantidade):
            while True:
                try:
                    p = float(input(f"Digite o {i+1}º preço: "))
                    precos.append(p)
                    break
                except ValueError:
                    print("Digite um valor válido (ex: 19.90).")
        limite = float(input("Digite o valor limite: "))
        print(f"\nPreços maiores que {limite}:")
        for p in precos:
            if p > limite:
                print(p)
    except ValueError:
        print("Erro: entrada inválida.")