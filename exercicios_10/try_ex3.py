def exercicio_03():
    """
        Este algoritmo solicita um número inteiro ao usuário e mostra o dobro dele,
        garantindo que a entrada seja realmente um número inteiro.

        Autor: Arthur Land Avila
        Data: 16/10/2025
    """

    # Solicite um número inteiro ao usuário e mostre o dobro dele. Garanta que a entrada seja 
    # um inteiro.


    try:
        num = int(input("Digite um nùmero inteiro: "))
        dobro = num * 2
        print(f"\nO dobro de {num} é {dobro}.")
    except ValueError:
        print("/nErro: Por favor digite um número inteiro valido ! ") 
    