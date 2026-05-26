def exercicio_04():
    """
        Este algoritmo recebe números inteiros positivos e verifica se a sequência 
        está sempre crescendo. O programa encerra se o usuário digitar um número 
        menor ou igual ao anterior ou se optar por parar voluntariamente. 
        Ao final, exibe se a sequência é crescente, a soma e a quantidade de números.

        Autor: Arthur Land Avila
        
        Data: 14/10/2025
    """

    # Crie um programa que recebe números inteiros positivos um a um.
    # Valide que o número seja maior que zero.
    # Verifique se a sequência está sempre crescendo.
    # Permita que o usuário pare quando quiser.
    # Se em algum momento o número informado for menor ou igual ao anterior, interrompa a 
    # entrada e informe que a sequência não é crescente.
    # Caso o usuário pare voluntariamente, informe se a sequência é crescente ou não.
    # Exiba a soma e a quantidade de números informados.


    print("=== Verificador de Sequência Crescente ===")
    print("Digite números inteiros positivos um por um.")
    print("Digite 'parar' para encerrar voluntariamente.\n")

    anterior = 0
    soma = 0
    quantidade = 0
    sequencia_crescente = True  # variável de controle

    while True:
        entrada = input("Digite um número inteiro positivo (ou 'parar'): ")

        # Verifica se o usuário quer encerrar voluntariamente
        if entrada.lower() == "parar":
            break

        # Verifica se a entrada é um número inteiro válido
        if not entrada.isdigit():
            print("Entrada inválida! Digite apenas números inteiros positivos.\n")
            continue

        numero = int(entrada)

        # Verifica se é positivo
        if numero <= 0:
            print("O número deve ser maior que zero.\n")
            continue

        # Se for o primeiro número, apenas registra
        if quantidade == 0:
            anterior = numero
        else:
            # Se o número for menor ou igual ao anterior, encerra
            if numero <= anterior:
                sequencia_crescente = False
                print("\nA sequência não é crescente!")
                break
            anterior = numero

        soma += numero
        quantidade += 1

    # Exibe o resumo final
    if quantidade == 0:
        print("\nNenhum número foi informado.")
    else:
        print("\n===== RESULTADO FINAL =====")
        print(f"Quantidade de números: {quantidade}")
        print(f"Soma total: {soma}")

        if sequencia_crescente:
            print("A sequência é crescente! ")
        else:
            print("A sequência não é crescente. ")
            