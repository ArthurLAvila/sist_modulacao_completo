def exercicio_02():
    """
    Exercício 02 – 13/10/2025

    Este algoritmo recebe temperaturas em graus Celsius (de -50 a 50) 
    e classifica como Frias (<10), Moderadas (entre 10 e 25) ou Quentes (>25).
    O usuário pode continuar ou encerrar digitando '!encerrar'.
    Ao final, mostra todas as temperaturas informadas, as contagens por categoria, 
    a maior, a menor e a média. Caso a média seja menor que 0, alerta "Muito frio!".

    Autor: Arthur Land Avila – Data: 13/10/2025
    """

    # Faça um programa que receba temperaturas em graus Celsius, uma por vez.
    # Aceite somente números válidos entre -50 e 50.
    # Para cada temperatura, classifique-a como Fria < 10, moderada entre 10 e 25 ou Quente > 
    # 25.
    # Conte quantas temperaturas de cada categoria foram inseridas.
    # Permita que o usuário escolha continuar ou parar a qualquer momento.
    # Ao final, exiba um resumo com as contagens de cada categoria, a maior e a menor 
    # temperatura informadas, e a média.
    # Se a média for abaixo de zero, mostre uma mensagem extra alertando muito frio no 
    # conjunto de dados.

    print("=== Leitura de Temperaturas ===")

    # variáveis de contagem
    fria = 0
    moderada = 0
    quente = 0
    soma = 0
    quantidade = 0

    # variáveis de controle
    maior = -51
    menor = 51
    todas_temp = ""  # variável auxiliar pra guardar o histórico das temperaturas

    while True:
        entrada = input("Digite uma temperatura entre -50 e 50 (ou 'sair' para sair): ")

        if entrada == "sair":
            break

        if entrada.lstrip("-").isdigit():  # permite número negativo
            temp = int(entrada)

            if temp < -50 or temp > 50:
                print("Temperatura fora do intervalo permitido! Tente novamente.")
                continue

            # atualiza histórico
            todas_temp += str(temp) + ", "

    # classificação
            if temp < 10:
                fria += 1
            elif temp <= 25:
                moderada += 1
            else:
                quente += 1

            # atualiza soma, quantidade, maior e menor
            soma += temp
            quantidade += 1

            if temp > maior:
                maior = temp
            if temp < menor:
                menor = temp

        else:
            print("Entrada inválida! Digite apenas números inteiros ou '!encerrar'.")

    # saída final
    if quantidade > 0:
        media = soma / quantidade

        print("\n=== RESULTADO FINAL ===")
        print(f"Temperaturas digitadas: {todas_temp}")
        print(f"Total de temperaturas: {quantidade}")
        print(f"Frias: {fria}° | Moderadas: {moderada}° | Quentes: {quente}°")
        print(f"Maior temperatura: {maior}"+"°")
        print(f"Menor temperatura: {menor}"+"°")
        print(f"Média das temperaturas: {media:.2f}"+"°")
        print(f"Média das temperaturas: {round(media)}"+"°")
        if media < 0:
            print("Média abaixo de zero: MUITO FRIO!")
    else:
        print("\nNenhuma temperatura válida foi informada.")
