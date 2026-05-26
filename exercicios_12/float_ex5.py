def exercicio05():
    """
    Exercício 5
    Peça ao usuário para informar quantos valores float deseja adicionar a uma lista.
    Pergunte um número float e mostre a posição dele se estiver na lista.
    """

    # Peça ao usuário para informar quantos valores float deseja adicionar a uma lista.
    # Insira os valores com validação.
    # Pergunte ao usuário um número float para verificar se ele está na lista.
    # Mostre a posição do número na lista, ou uma mensagem se não estiver presente.
    # Use laços para fazer a busca

    valores = []
    try:
        quantidade = int(input("Quantos valores deseja adicionar? "))
        for i in range(quantidade):
            while True:
                try:
                    v = float(input(f"Digite o {i+1}º valor: "))
                    valores.append(v)
                    break
                except ValueError:
                    print("Digite um número válido.")
        busca = float(input("Digite um número para verificar se está na lista: "))
        encontrado = False
        for i in range(len(valores)):
            if valores[i] == busca:
                print(f"O número {busca} está na posição {i}.")
                encontrado = True
        if not encontrado:
            print("Número não encontrado na lista.")
    except ValueError:
        print("Entrada inválida.")