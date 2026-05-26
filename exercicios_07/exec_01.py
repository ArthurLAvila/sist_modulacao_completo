def exercicio_01(): 
    """ 
        Este algoritmo verifica qual dos dois numeros digitados é maior ou igual usando match case.

        Autor: Arthur Land Avila Data: 2/10/2025
    """


    # Peça dois números. Use match case para verificar:
    # Se o primeiro número é maior ou igual ao segundo, exiba O primeiro número é maior ou 
    # igual ao segundo. Caso contrário, exiba que o primeiro número não é maior ou igual

    # Pede dois números
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # Usa match case para verificar
    match num1 >= num2:
        case True:
            print("O primeiro número é maior ou igual ao segundo.")
        case False:
            print("O primeiro número não é maior ou igual ao segundo.")
