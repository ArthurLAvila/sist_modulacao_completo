def exercicio_04():
    """
    Este exercício pede ao usuário para informar um número inteiro e verifica
    se ele está presente em um conjunto pré-definido.
    Em seguida, exibe uma mensagem indicando se o número foi encontrado ou não
    e mostra o tamanho total do conjunto.

    Autor: Arthur Land Avila  
    Data: 03/11/2025
    """

    # Peça ao usuário para informar um número inteiro e verifique se ele está presente em um 
    # conjunto pré-definido.
    # Exiba uma mensagem indicando se o número foi encontrado ou não.
    # Mostre também o tamanho do conjunto usando.

    # Conjunto pré-definido
    conjunto = {3, 7, 10, 14, 21, 28}

    print("Conjunto atual:", conjunto)

    # Solicita um número inteiro do usuário com validação
    numero = input("\nDigite um número inteiro para verificar se ele está no conjunto: ")

    while not numero.isdigit():
        print("Por favor, digite apenas números inteiros!")
        numero = input("Digite novamente: ")

    numero = int(numero)

    # Verifica se o número está no conjunto
    if numero in conjunto:
        print(f"\nO número {numero} foi encontrado no conjunto! ")
    else:
        print(f"\nO número {numero} NÃO está presente no conjunto. ")

    # Mostra o tamanho do conjunto
    print(f"\nO conjunto possui {len(conjunto)} elementos.")
