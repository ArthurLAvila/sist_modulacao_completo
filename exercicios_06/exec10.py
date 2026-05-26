def exercicio_10():
    """
        Este algoritmo define se a primeira palavra é menor que a segunda ou a primeira é maior que a segunda palavra digitada.

        Autor: Arthur Land Avila Data: 18/09/2025
    """

    # Crie um programa que compare duas strings de diferentes tamanhos e imprima se a 
    # primeira string é maior ou menor que a segunda, levando em consideração a comparação 
    # lexicográfica.

    #Entrada de duas strings 
    string1 = input("Digite uma palavra: ")
    string2 = input("Digite uma segunda palavra: ")

    #Condição se a primeira string é menor que a segunda 
    if string1 < string2:
        print(f'A primeira string "{string1}" é MENOR que a segunda "{string2}"')
    #Condição se a primeira string é maior que a segunda
    elif string1 > string2:
        print(f'A primeira string "{string1}" é MAIOR que a segunda "{string2}"')
    # se não for os resultados a cima, então as palavras são iguais/identicas 
    else:
        print(f'As duas strings são IGUAIS')
