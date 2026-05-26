def exercicio_08():
    """
        Este algoritmo solicita um inteiro pósitivo. E se esse for o caso ele faz o dobro e exibe na tela. Ele mostra o dobro se não foi digitado um número negativo.

        Autor: Arthur Land Avila
        Data: 16/10/2025
    """

    # Solicite um número positivo. Se a entrada for válida e o número for realmente positivo, 
    # mostre o dobro. Use else para exibir o resultado apenas se não houve erro.

    try:
        num = int(input("Digite um número inteiro positivo: "))

        if num <= 0:
            print("\nErro: o número deve ser positivo.")
        else:
            dobro = num * 2

    except ValueError:
        print("\nErro: digite um número válido.")

    else:
        # Este bloco só será executado se NÃO houver erro no try
        if num > 0:
            print(f"\nO dobro de {num} é {dobro}.")
