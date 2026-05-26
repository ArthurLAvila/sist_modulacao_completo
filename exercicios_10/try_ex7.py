def exercicio_07(): 
    """
        Este algoritmo pede uma idade e se for negativa ele mostra um erro de idade invalida. caso contrario mostra a idade.
        Data: 16/10/2025
    """

    # Peça a idade do usuário. Se a idade for negativa, levante um erro manualmente com a 
    # mensagem Idade inválida. Caso contrário, mostre a idade.

    try:
        idade = int(input("Digite sua idade: "))

        if idade < 0:
            raise ValueError("Idade inválida")

        print(f"\nSua idade é {idade} anos.")

    except ValueError as erro:
        print(f"\nErro: {erro}")
