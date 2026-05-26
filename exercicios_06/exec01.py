def exercicio_01():
    """
        Este algoritmo define se dois valores são iguais, diferentes, valor 1 maior ou igual ou nenhum dos dois, e  que valor 2 ou valor 1 é 
        menor ou igual que valor 2 ou nehum dos dois. usando <, >, <=, >=, == e !=. 

        Autor: Arthur Land Avila Data: 18/09/2025
    """


    # Crie um programa que peça ao usuário para digitar dois números e compare-os utilizando 
    # os operadores >, <, >=, <=, ==, !=. Imprima o resultado de cada comparação de forma clara 
    # e explicativa.

    #entrada dos valores
    valor1 = input("Digite um valor: ")
    valor2 = input("Digite um outro valor: ")
    #valor 1 maior que valor 2 
    if valor1>valor2:
        print(f"O primeiro número {valor1} é maior que o segundo {valor2}.")
    elif valor1<valor2:
        print(f"O primeiro número {valor1} é menor que o segundo {valor2}.")
    else:
        print(f"Os dois números são iguais.")

    #verificando igualdade 
    if valor1==valor2:
        print("Os números são iguais.")
    else:
        print("Os números são diferentes.")
        if valor1>=valor2:
            print(f"{valor1} é maior ou igual a {valor2}.")
        else:
            print(f"{valor1} não é maior ou igual a {valor2}.")

    #menor ou igual
        if valor1<=valor2:
            print(f"{valor1} é menor ou igual a {valor2}.")
        else:
            print(f"{valor1} não é menor ou igual a {valor2}.")
