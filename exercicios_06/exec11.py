def exercicio_11():
    """
        Este algoritmo verifica se foi digitado um numero ou uma palavra.

        Autor: Arthur Land Avila Data: 18/09/2025
    """

    # Crie um programa que peça ao usuário para digitar uma palavra e verifique se ela é um 
    # número. Se for, imprima "Você digitou um número". Caso contrário, imprima "Você digitou 
    # uma palavra".


    # entrada de uma palavra qualquer, podendo ser um número ou não 
    entrada = input("Digite algo: ")
    #Verifica com uma boleana se é um digito, retornando True se for verdadeiro ou false se for falso 
    if entrada.isdigit():
        print("Você digitou um número") #True 
    else:
        print("Você digitou uma palavra") #False
