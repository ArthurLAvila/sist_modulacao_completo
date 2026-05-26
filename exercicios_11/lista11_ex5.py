def exercicio_05():
    """
    Exercício 5 - Verificação de número na lista
    """
    # Enunciado:
    # Peça ao usuário para informar quantos valores float deseja adicionar a uma lista.
    # Insira os valores com validação.
    # Pergunte ao usuário um número float para verificar se ele está na lista.
    # Mostre a posição do número na lista, ou uma mensagem se não estiver presente.
    # Use laços para fazer a busca.

    try:
        n = int(input("Quantos valores deseja adicionar? "))
        valores = []
        for i in range(n):
            while True:
                try:
                    val = float(input(f"Digite o {i+1}º valor: "))
                    valores.append(val)
                    break
                except ValueError:
                    print("Entrada inválida! Digite um número real.")
        busca = float(input("Digite um número para verificar: "))
        encontrado = False
        for i in range(len(valores)):
            if valores[i] == busca:
                print(f"Número encontrado na posição {i}.")
                encontrado = True
        if not encontrado:
            print("Número não encontrado na lista.")
    except ValueError:
        print("Erro: entrada inválida!")