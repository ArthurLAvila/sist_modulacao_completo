def exercicio_08():
    """
        Este algoritmo define se o numero digitado é maior que 10 e se for ele informa e se não for maior que 19 ele 
        verifica se a palavra digitada é python com letrtas minusculas.
        
        Autor: Arthur Land Avila Data: 18/09/2025
    """

    # Crie um programa que peça ao usuário para digitar uma palavra e um número. O programa 
    # deve verificar se o número é maior que 10 e, caso seja, imprimir "O número é maior que 
    # 10". Caso contrário, deve verificar se a palavra digitada é "Python" e imprimir "Você 
    # digitou Python".

    #entrada de um numero flutuante(com virgula ou ponto) e uma palavra(string)
    numero = float(input("Digite um número: "))
    palavra = input("Digite uma palavra: ")

    #Conversão da palavra com qualquer letra maiuscula para todas as letras minusculas para pegar a resposta independentemente de como ela for digitada se for a resposta esperada
    palavra_lower = palavra.lower()
    #se for mior que 10 mostra que o numero > 10 na tela 
    if numero > 10:
        print("O número é maior que 10")
    #Caso contrario se a palavra for exatamente iguala python ele mostra na tela    
    elif palavra_lower == "python":
        print("Você digitou Python")
