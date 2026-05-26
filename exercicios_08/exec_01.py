def exercicio_01():
    """
        Exercicios da lista de for do dia 07/10/2025 feita em aula. 

        Autor: Arthur Land Avila. 
        Data: 07/10/2025
        
    """


    # ==============================================
    # Exercícios com FOR — Menu com match case
    # ==============================================


    print("\n===== MENU DE EXERCÍCIOS =====")
    print("1 - Números de 0 a 4")
    print("2 - Digitar e mostrar 3 números")
    print("3 - Comparar 5 números com 10")
    print("4 - Verificar se pode dirigir")
    print("5 - Verificar se é vogal ou consoante")
    print("6 - Contar letras maiúsculas")
    print("7 - Verificar se número é par ou ímpar")
    print("8 - Contar vogais de uma frase")
    print("9 - Substituir letra em texto")
    print("10 - Opções com match case (a, b, c)")
    print("11 - Verificar se número é positivo, negativo ou zero")
    print("12 - Mostrar números pares até N")
    print("0 - Sair")
    print("===============================")

    opcao = input("Escolha o número do exercício que deseja executar: ")

    match opcao:
        # Exercício 1
        case "1":
            print("\n=== Exercício 1 ===")
            for i in range(5):
                print(i)

        # Exercício 2
        case "2":
            print("\n=== Exercício 2 ===")
            for i in range(3):
                numero = input(f"Digite o {i+1}º número: ")
                print("Você digitou:", numero)

        # Exercício 3
        case "3":
            print("\n=== Exercício 3 ===")
            for i in range(5):
                numero = float(input(f"Digite o {i+1}º número: "))
                if numero > 10:
                    print("Maior que 10")
                elif numero < 10:
                    print("Menor que 10")
                else:
                    print("Igual a 10")

        # Exercício 4
        case "4":
            print("\n=== Exercício 4 ===")
            for i in range(4):
                idade = int(input(f"Digite a idade da pessoa {i+1}: "))
                if idade >= 18:
                    print("Pode dirigir ")
                else:
                    print("Não pode dirigir ")

        # Exercício 5
        case "5":
            print("\n=== Exercício 5 ===")
            for i in range(3):
                caractere = input(f"Digite o {i+1}º caractere: ").lower()
                if caractere.isalpha():
                    if caractere in "aeiou":
                        print("É uma vogal.")
                    else:
                        print("É uma consoante.")
                else:
                    print("Isso não é uma letra.")

        # Exercício 6
        case "6":
            print("\n=== Exercício 6 ===")
            palavra = input("Digite uma palavra: ")
            contagem = 0

            for letra in palavra:
                if letra.isupper():
                    contagem += 1

            print("Quantidade de letras maiúsculas:", contagem)

        # Exercício 7
        case "7":
            print("\n=== Exercício 7 ===")
            for i in range(4):
                numero = int(input(f"Digite o {i+1}º número: "))
                if numero % 2 == 0:
                    print("Par")
                else:
                    print("Ímpar")

        # Exercício 8
        case "8":
            print("\n=== Exercício 8 ===")
            frase = input("Digite uma frase: ").lower()
            vogais = "aeiou"
            contador = 0

            for letra in frase:
                if letra in vogais:
                    contador += 1

            print("Quantidade de vogais na frase:", contador)

        # Exercício 9
        case "9":
            print("\n=== Exercício 9 ===")
            texto = input("Digite um texto: ")
            letra1 = input("Digite a letra a ser substituída: ")
            letra2 = input("Digite a letra substituta: ")

            novo_texto = ""
            for caractere in texto:
                if caractere == letra1:
                    novo_texto += letra2
                else:
                    novo_texto += caractere

            print("Texto resultante:", novo_texto)

        # Exercício 10
        case "10":
            print("\n=== Exercício 10 ===")
            for i in range(3):
                opc = input("Digite uma opção (a, b, c ou outra): ").lower()

                match opc:
                    case "a":
                        print("Você escolheu a opção A")
                    case "b":
                        print("Você escolheu a opção B")
                    case "c":
                        print("Você escolheu a opção C")
                    case _:
                        print("Opção inválida")

        # Exercício 11
        case "11":
            print("\n=== Exercício 11 ===")
            for i in range(3):
                numero = int(input(f"Digite o {i+1}º número: "))

                match numero:
                    case 0:
                        print("Número zero")
                    case _ if numero > 0:
                        print("Número positivo")
                    case _ if numero < 0:
                        print("Número negativo")

        # Exercício 12
        case "12":
            print("\n=== Exercício 12 ===")
            n = int(input("Digite um número n: "))
            for i in range(n + 1):
                if i % 2 == 0:
                    print(i)
                    
        # Opção inválida
        case _:
            print("\nOpção inválida! Tente novamente.")
