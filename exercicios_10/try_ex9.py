def exercicio_09():
    """
        Este algoritmo pede para o usuário chutar um número de 1 a 10. Ele armazena a quantidade de tentativas necessarias até o usuário acertar. 
        E trata erros de numeros/entradas em que não seriam possiveis realizar o teste.  

        Autor: Arthur Land Avila
        Data: 16/10/2025
    """

    # Peça para o usuário adivinhar um número secreto entre 1 e 10. Conte quantas tentativas 
    # foram necessárias até ele acertar. Trate erros de entrada.

    import random

    secreto = random.randint(1, 10)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Adivinhe o número secreto (entre 1 e 10): "))
            tentativas += 1

            if palpite < 1 or palpite > 10:
                print("Erro: o número deve estar entre 1 e 10.")
            elif palpite < secreto:
                print("Tente um número maior!")
            elif palpite > secreto:
                print("Tente um número menor!")
            else:
                print(f"\nParabéns! Você acertou o número {secreto} em {tentativas} tentativas.")
                break

        except ValueError:
            print("Erro: digite um número inteiro válido.")

