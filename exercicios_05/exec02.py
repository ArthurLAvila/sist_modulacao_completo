def exercicio_02():
    # Peça para o usuário digitar três números inteiros.
    # Informe qual é o maior número e se ele é positivo ou se ele é múltiplo de 5, mas não 
    # múltiplo de 3.

    n1 = input("Digite o primeiro número inteiro: ")
    n2 = input("Digite o segundo número inteiro: ")
    n3 = input("Digite o terceiro número inteiro: ")

    if n1.lstrip("-").isdigit() and n2.lstrip("-").isdigit() and n3.lstrip("-").isdigit():
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)

        # descobrir o maior
        maior = n1
        if n2 > maior:
            maior = n2
        if n3 > maior:
            maior = n3

        print(f"O maior número é {maior}.")

        # verificar condições
        if (maior > 0) or (maior % 5 == 0 and not (maior % 3 == 0)):
            print("Ele é positivo OU é múltiplo de 5 mas não múltiplo de 3.")
        else:
            print("Ele não atende às condições.")
    else:
        print("Entrada inválida. Digite apenas números inteiros.")
