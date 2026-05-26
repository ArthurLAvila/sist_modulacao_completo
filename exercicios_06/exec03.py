def exercicio_03():
    """
        Este algoritmo compara um numero em formato string com uma palavra. Transformando o numero em uma str na força.

        Autor: Arthur Land Avila Data: 18/09/2025
    """

    # Crie um programa que peça ao usuário para digitar um número e uma palavra (string). 
    # Compare o número com a string utilizando os operadores == e !=. Converta o número para 
    # uma string antes da comparação.

    #Entrada
    numero = int(input("Digite um número: "))
    palavra = input("Digite uma palavra: ")

    #Converter número para string 
    numero_str = str(numero)

    #Cabeçalho
    print("\n--- Resultados das Comparações ---")

    #Igualdade
    if numero_str == palavra:
        print(f'O número convertido "{numero_str}" é IGUAL à palavra "{palavra}".')
    #Diferença
    else:
        print(f'O número convertido "{numero_str}" NÃO é igual à palavra "{palavra}".')
