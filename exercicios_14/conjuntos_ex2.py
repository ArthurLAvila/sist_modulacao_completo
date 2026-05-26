def exercicio_02():
    """ 
        Este exercicio pergunta ao usuario quantos numeros ele quer inserir em um determinado conjunto. 
        armazenando eles um a um em um set, mostra o conjunto criado e usa um laço para exibir todos os valores armazenados.

        Autor: Arthur Land Avila  
        Data: 03/11/2025
    """

    # Peça ao usuário para informar quantos números deseja inserir em um conjunto.
    # Solicite os números um por um e armazene-os em um set.
    # Mostre o conjunto criado.
    # Use um laço for para exibir todos os valores armazenados.


    numeros = input("Digite quantos números você quer inserir no conjunto: ")

    while not numeros.isdigit():
        print("Por favor, digite apenas números inteiros!")
        numeros = input("Digite quantos números você quer inserir no conjunto: ")

    numeros = int(numeros)

    numeros_conjunto = set()

    for i in range(numeros):
        numero = input(f"Digite o {i+1}º número: ")
        while not numero.isdigit():
            print("Entrada inválida! Digite apenas números inteiros.")
            numero = input(f"Digite o {i+1}º número novamente: ")
        numeros_conjunto.add(int(numero))

    print("\nConjunto criado:", numeros_conjunto)

    print("Valores armazenados:")
    for numero in numeros_conjunto:
        print(numero)
