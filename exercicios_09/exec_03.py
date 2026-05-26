def exercicio_03():
    """
        Este algoritmo cria um jogo de adivinhação onde o usuário tenta descobrir
        um número secreto entre 1 e 100. O programa informa se o palpite está 
        alto, baixo ou correto, e encerra se o jogador desistir ou errar 5 vezes.

        Autor: Arthur Land Avila
        Data: 14/10/2025
    """

    # Construa um programa onde o usuário tenta adivinhar um número secreto entre 1 e 100.
    # O programa deve aceitar palpites até o usuário acertar ou desistir.
    # Para cada palpite, informe se está muito baixo, muito alto ou acertou.
    # O usuário pode digitar desistir para encerrar o programa.
    # Conte quantos palpites foram feitos e informe ao final.
    # Se o usuário errar 5 vezes, avise que o limite de tentativas foi atingido e encerre.
    # Use validação para aceitar somente números inteiros entre 1 e 100 ou o comando desistir.


    import random

    # número secreto aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)

    tentativas = 0  # contador de chutes

    print("=== Jogo da Adivinhação ===")
    print("Tente adivinhar o número secreto entre 1 e 100!")
    print("Digite 'desistir' para encerrar o jogo.\n")

    while True:
        palpite = input("Digite seu palpite: ")

        # Verifica se o jogador quer sair
        if palpite.lower() == "desistir":
            print("\nVocê desistiu do jogo.")
            break

        # Verifica se o chute é um número inteiro
        if not palpite.isdigit():
            print("Entrada inválida! Digite um número inteiro entre 1 e 100 ou 'desistir'.")
            continue

        palpite = int(palpite)

        # Verifica se está dentro do intervalo permitido
        if palpite < 1 or palpite > 100:
            print("Por favor, digite um número entre 1 e 100.")
            continue

        tentativas += 1  # conta o palpite válido

        # Verifica o palpite
        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.\n")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.\n")
        else:
            print(f"\n Parabéns! Você acertou o número secreto ({numero_secreto})!")
            print(f"Total de tentativas: {tentativas}")
            break

        # Se o jogador errar 10 vezes, encerra o jogo
        if tentativas == 10:
            print(f"\nLimite de 10 tentativas atingido! O número secreto era {numero_secreto}.")
            break
