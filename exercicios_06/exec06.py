def exercicio_06():
    """
        Este algoritmo coloca em ordem crescente três palavras e mostra na tela o resultado usando apenas if e else. Usando maior, menor e meio.

        Autor: Arthur Land Avila Data: 18/09/2025
    """

    # Crie um programa que peça ao usuário para digitar três palavras. O programa deve exibir 
    # as palavras ordenadas em ordem alfabética crescente.

    #Entrada das três palavras 
    p1 = input("Digite a primeira palavra: ")
    p2 = input("Digite a segunda palavra: ")
    p3 = input("Digite a terceira palavra: ")

    print("\n--- Palavras em ordem alfabética crescente ---")
    # ordenação alfabetica usando menor maior e meio com if e else 
    if p1 <= p2 and p1 <= p3:
        menor = p1
        if p2 <= p3:
            meio = p2
            maior = p3
        else:
            meio = p3
            maior = p2
    elif p2 <= p1 and p2 <= p3:
        menor = p2
        if p1 <= p3:
            meio = p1
            maior = p3
        else:
            meio = p3
            maior = p1
    else:
        menor = p3
        if p1 <= p2:
            meio = p1
            maior = p2
        else:
            meio = p2
            maior = p1
    #Mostra na tela na ordem

    print(menor)
    print(meio)
    print(maior)
