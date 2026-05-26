def exercicio_07():
    """
        Este algoritmo trasforma nuemros string em digitos e consegue usar negativos tambem, e realiza uma das 4 operações basicas da calculadora,
        soma, sub, div e mult, e confere se não esta dividindo por 0 se não da erro, isso tudo usando match case.  *sensitivel a acento*
        
        Autor: Arthur Land Avila Data: 03/10/2025
    """

    # Peça ao usuário para digitar uma operação: somar, subtrair, multiplicar ou dividir.
    # Peça dois números. Use match case para realizar a operação.

    # Pede ao usuário qual operação ele quer realizar
    operacao = input("Escolha uma operação (soma/subtracão/multiplicacão/divisão [sensitivel a acento] ): ").lower()

    # Pede os dois números (string)
    entrada1 = input("Digite um número inteiro qualquer: ")
    entrada2 = input("Digite um segundo número inteiro qualquer: ")

    # Verifica se as duas entradas são números inteiros válidos (aceita negativo tambem)
    if entrada1.lstrip("-").isdigit() and entrada2.lstrip("-").isdigit():
        # Converte as entradas de string para inteiro
        num1 = int(entrada1)
        num2 = int(entrada2)

        # Usa match case para saber qual operação realizar
        match operacao:
            case "soma":
                print(f"Resultado: {num1 + num2}")
            case "subtracão":
                print(f"Resultado: {num1 - num2}")
            case "multiplicação":
                print(f"Resultado: {num1 * num2}")
            case "divisão":
                # Verifica se não ta dividindo por zero antes da operação
                if num2 != 0:
                    print(f"Resultado: {num1 / num2}")
                else:
                    print("Erro: divisão por zero não é permitida.")
            case _: 
                print("Operação inválida.")
    else:
        print("Você não digitou números inteiros válidos.")
