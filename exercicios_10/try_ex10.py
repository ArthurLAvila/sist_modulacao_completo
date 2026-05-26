def exercicio_10():
    """
        Este algoritmo pede números ao usuário para fazer uma operação de soma com eles. Podendo sair do programa ao digitar "sair". 
        Mostra a soma total de todos os números inseridos. E tentativas invalidas são tratadas. 

        Autor: Arthur Land Avila
        Data: 16/10/2025
    """

    # Este algoritmo pede números ao usuário para somar.
    # O usuário pode digitar 'sair' para encerrar.
    # No final, o programa mostra a soma total.
    # Entradas inválidas são tratadas.


    soma = 0

    while True:
        entrada = input("Digite um número para somar (ou 'sair' para encerrar): ").strip().lower()

        if entrada == "sair":
            break

        try:
            numero = float(entrada)
            soma += numero
        except ValueError:
            print("Erro: digite um número válido ou 'sair' para encerrar.")

    print(f"\nA soma total dos números digitados é: {soma:.2f}")
