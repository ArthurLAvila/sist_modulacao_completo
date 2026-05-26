def exercicio_07():
    """
        Este algoritmo define qual das duas palavras inseridas vem primeiro na ordem lexicografica. 

        Autor: Arthur Land Avila Data: 18/09/2025
    """

    # Crie um programa que compare duas palavras em relação à sua ordem lexicográfica e 
    # informe se a primeira palavra é maior ou menor que a segunda.


    # Programa para comparar duas palavras em ordem lexicográfica

    palavra1 = input("Digite a primeira palavra: ")
    palavra2 = input("Digite a segunda palavra: ")

    print("\n--- Comparação lexicográfica ---")
    # A palavra que vem antes é a primeira 
    if palavra1 < palavra2:
        print(f'A palavra "{palavra1}" vem ANTES de "{palavra2}" na ordem lexicográfica.')
    # A palavra que vem antes é a segunda 
    elif palavra1 > palavra2:
        print(f'A palavra "{palavra1}" vem DEPOIS de "{palavra2}" na ordem lexicográfica.')
    #As duas palavras são as mesmas 
    else:
        print(f'As palavras "{palavra1}" e "{palavra2}" são IGUAIS na ordem lexicográfica.')
