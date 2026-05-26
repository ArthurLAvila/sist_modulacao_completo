def exercicio_15():
    """
        Este algoritmo testa se uma palavra e um numero são iguais convertendo o numero em uma string.
        
        Autor: Arthur Land Avila Data: 18/09/2025
    """

    # Crie um programa que peça ao usuário para digitar uma palavra e um número. O programa 
    # deve comparar o número com a string digitada, convertendo o número para string, e 
    # verificar se são iguais ou diferentes.

    #entrada de uma palavra e um inteiro 
    palavra = input ("Digite uma palavra: ")
    valor =int(input("Digite um valor de -100 a 100: "))

    #converte um valor para uma string 
    valor_str = str(valor)

    #testa se a palavra é igual ao valor em formato de string 
    if palavra==valor_str:
        print("Eles são iguai! ")
    else:
        print("Eles são diferentes! ")