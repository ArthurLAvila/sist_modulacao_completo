def exercicio_05():
    """
        Este algoritmo escolhe um caso de operação a resolver de acordo com o numero digitado no input usando match case.

        Autor: Arthur Land Avila Data: 03/10/2025
    """

    # Solicite ao usuário que escolha uma opção de 1 a 3.
    # Use match case para exibir uma mensagem de acordo com a opção:
    # 1 = Você escolheu a opção 1 - Verificar saldo.
    # 2 = Você escolheu a opção 2 - Realizar saque.
    # 3 =Você escolheu a opção 3 - Depositar dinheiro.
    # Outro valor = Opção inválida

    # Pede opção
    opcao = int(input("Digite um numero de 1 a 3: "))

    # Usa match case para definir a opção:

    match opcao:
        case 1:
            print("Você escolheu a opção 1 - Verificar Saldo")
        case 2:
            print("Você escolheu a opção 2 - Realizar Saque")
        case 3:
            print("Você escolheu a opção 3 - Depositar Dinheiro")     
        case _: 
            print("Opção invalida")