def exercicio_02():
    """ 
        Este algoritmo verifica qual dos dois numeros digitados é maior ou igual usando match case.

        Autor: Arthur Land Avila Data: 2/10/2025
    """

    # Peça dois números. Use match case para verificar: Se o primeiro número é menor ou igual
    # ao segundo caso contrário, exiba que o primeiro número não é menor ou igual

    # pede dois números
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # usa match case para verificar
    match num1 <= num2:
        case True:
            print("O primeiro número é menor ou igual ao segundo.")
        case False:
            print("O primeiro número não é menor ou igual ao segundo.")
