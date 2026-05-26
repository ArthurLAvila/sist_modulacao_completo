def exercicio_04():
    """ 
        Este algoritmo verifica se dois numeros são diferentes ou iguais usando match case.
        
        Autor: Arthur Land Avila Data: 03/10/2025
    """

    # Peça dois números ao usuário. Use match case para: Informar se são diferentes ou se são 
    # iguais

    # pede dois números
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # usa match case para verificar
    match num1 != num2:
        case True:
            print("Os valores são diferentes.")
        case False:
            print("Os valores são iguais.")
