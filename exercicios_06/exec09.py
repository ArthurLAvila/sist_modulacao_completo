def exercicio_09():
    """
        Este algoritmo verifica se foi digitado python em minusculo, caso contrario ele verifica se o numero digitado é maior que 5 e informa.
        
        Autor: Arthur Land Avila Data: 18/09/2025
    """

    # Crie um programa que peça ao usuário para digitar um número e uma palavra. O programa 
    # deve verificar se a palavra é "Python" e, caso seja, imprimir "Você digitou Python". Caso 
    # contrário, verifique se o número digitado é maior que 5 e imprima "O número é maior que 
    # 5".

    #Entrada
    palavra = input("Digite uma palavra: ")
    numero = float(input("Digite um número: "))

    #Converter palavra maiuscula para tudo minusculo 
    palavra_lower = palavra.lower()

    # se a palavra for python mostra na tela 
    if palavra_lower == "python":
        print("Você digitou Python")
    # Se não testa se o número é maior que 5 e mostra na tela se for 
    elif numero > 5:
        print("O número é maior que 5")
    else:
        print("Você não acertou :( )")
        print("Tente novamente")    
