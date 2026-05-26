def exercicio_04():
    """
        Este algoritmo exibe na tela se duas palavras tem comprimentos diferentes, sendo a primeira maior que a segunda, depois ao contrario, 
        e dai se são exatamente iguais, case e acento sensitive. [usando len()].

        Autor: Arthur Land Avila Data: 18/09/2025
    """

    # Crie um programa que peça ao usuário para digitar duas palavras. O programa deve 
    # comparar o comprimento das duas palavras e dizer qual delas tem mais caracteres ou se 
    # elas têm o mesmo número de caracteres.


    #Entrada
    palavra1 = input("Digite a primeira palavra: ")
    palavra2 = input("Digite a segunda palavra: ")
    #Definindo tamanho das palavras usando metodo len
    tam1 = len(palavra1)
    tam2 = len(palavra2)
    #Cabeçalho
    print("\n--- Comparação de comprimentos ---")
    #Maior que 
    if tam1 > tam2:
        print(f'A palavra {palavra1} tem mais caracteres {tam1} do que {palavra2} {tam2}.')
    #Menor que 
    elif tam1 < tam2:
        print(f'A palavra {palavra2} tem mais caracteres {tam2} do que {palavra1} {tam1}.')
    #Palavras iguais
    else:
        print(f'As palavras "{palavra1}" e "{palavra2}" têm o MESMO número de caracteres {tam1}.')
