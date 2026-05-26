def exercicio_05():
    """
        Este algoritmo define se duas palavras estão na ordem alfabetica, primeiro ele verifica se a palavra1 vem primeiro que a palavra2 
        se não então a palavra2 vem primeiro que a palavra1, e se não for nenhum dos odis casos acima ele diz que elas são iguais. 
        
        Autor: Arthur Land Avila Data: 18/09/2025
    """

    # Crie um programa que peça ao usuário para digitar duas palavras (strings) e compare-as 
    # em ordem alfabética. Exiba qual palavra vem primeiro na ordem alfabética.


    #Entrada
    palavra1 = input("Digite a primeira palavra: ")
    palavra2 = input("Digite a segunda palavra: ")

    print("\n--- Comparação em ordem alfabética ---")
    #Menor que 
    if palavra1 < palavra2:
        print(f'A palavra "{palavra1}" vem primeiro que "{palavra2}" na ordem alfabética.')
    #Maior que 
    elif palavra1 > palavra2:
        print(f'A palavra "{palavra2}" vem primeiro que "{palavra1}" na ordem alfabética.')
    #São Iguais
    else:
        print(f'As palavras "{palavra1}" e "{palavra2}" são IGUAIS.')
