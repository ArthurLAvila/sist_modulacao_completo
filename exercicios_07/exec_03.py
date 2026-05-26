def exercicio_03():
    """ 
        Este algoritmo verifica se dois numeros são iguais ou não usando match case.
        
        Autor: Arthur Land Avila Data: 03/10/2025
    """

    # Solicite dois valores e use match case para: Informar se são iguais ou se são diferentes

    # pede dois números
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # usa match case para verificar
    match num1 == num2:
        case True:
            print("Os valores são iguais.")
        case False:
            print("Os valores são diferentes.")
