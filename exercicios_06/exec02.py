def exercicio_02():
    """
        Este algoritmo testa duas palavras e retorna qual vem antes de qual em ordem crescente. Primeiro ele testa se a 1 vem depois da 2 se não ele diz o contraio, 
        depois ele verifica se a palavra 1 vem antes da palavra 2 e se não é esse o caso ele também informa. Depois ele testa a igualdade das duas palavras, ou seja 
        ele retorna true se as duas palavras forem exatamente iguais sendo case sensitive e acento sensitive. Depois ele teste se as duas palavras são diferentes uma 
        da outra e retorna isso ou elas são iguais    
        
        
        [detalhe ele não mostra na tela na ordem correta ou na atual, somente informa qual vem primeiro ou depois de qual na ordem alfabetica]
        
        Autor: Arthur Land Avila Data: 18/09/2025
    """

    # Crie um programa que peça ao usuário para digitar duas palavras (strings) e compare-as 
    # utilizando os operadores >, <, ==, e !=. Exiba o resultado de cada comparação de maneira 
    # clara.

    # Programa para comparar duas palavras
    palavra1 = input("Digite a primeira palavra: ")
    palavra2 = input("Digite a segunda palavra: ")

    #cabeçalho
    print("\n--- Resultados das Comparações ---")

    #Maior que 
    if palavra1 > palavra2:
        print(f'"{palavra1}" vem depois de "{palavra2}" na ordem alfabética.')
    else:
        print(f'"{palavra1}" NÃO vem depois de "{palavra2}" na ordem alfabética.')

    #==================================================

    #Menor que 
    if palavra1 < palavra2:
        print(f'"{palavra1}" vem antes de "{palavra2}" na ordem alfabética.')
    else:
        print(f'"{palavra1}" NÃO vem antes de "{palavra2}" na ordem alfabética.')

    #==================================================

    #Igualdade 
    if palavra1 == palavra2:
        print(f'As palavras "{palavra1}" e "{palavra2}" são IGUAIS.')
    else:
        print(f'As palavras "{palavra1}" e "{palavra2}" são DIFERENTES.')

    #==================================================

    #Diferença
    if palavra1 != palavra2:
        print(f'As palavras "{palavra1}" e "{palavra2}" são DIFERENTES.')
    else:
        print(f'As palavras "{palavra1}" e "{palavra2}" são IGUAIS.')
