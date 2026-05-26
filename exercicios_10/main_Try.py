"""
    Programa principal com menu interativo usando while e match case.
    Contém os exercícios de tratamento de erros e entrada de dados.

    Autor: Arthur Land Avila
    Data: 16/10/2025
"""

import math
import random

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Converter Celsius para Fahrenheit")
    print("2 - Divisão entre dois números")
    print("3 - Dobro de um número inteiro")
    print("4 - Divisão entre dois inteiros (com tratamento)")
    print("5 - Raiz quadrada de um número")
    print("6 - Dividir 100 por um número (sempre mostrar 'Tentativa concluída')")
    print("7 - Validar idade (não pode ser negativa)")
    print("8 - Mostrar o dobro de um número positivo (usar else)")
    print("9 - Adivinhar número secreto")
    print("10 - Somar vários números até digitar 'sair'")
    print("11 - Média de 5 números válidos")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

  
    match opcao:
        # Exercício 1
        
        # Peça para o usuário digitar a temperatura em graus Celsius. Garantir que seja um número 
        # decimal válido. Converta a temperatura para Fahrenheit e exiba o resultado.

        # Conversão de Celsius para Fahrenheit: F = (C * 9/5) + 32    

        case "1":
            try:
                celsius = float(input("Digite a temperatura em °C: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
            except ValueError:
                print("Erro: digite um número válido.")

        # Exercício 2
        
        
        case "2":
            # Peça para o usuário digitar a temperatura em graus Celsius. Garantir que seja um número 
            # decimal válido. Converta a temperatura para Fahrenheit e exiba o resultado.

            # Conversão de Celsius para Fahrenheit: F = (C * 9/5) + 32

            try:
                celsius = float(input("Digite a temperatura em graus Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"\nA temperatura de {celsius:.2f}°C corresponde a {fahrenheit:.2f}°F.")
            except ValueError:
                print("\nErro: Por favor, digite um número válido para a temperatura.")

        # Exercício 3
        # Solicite um número inteiro ao usuário e mostre o dobro dele. Garanta que a entrada seja 
        # um inteiro.

        
        case "3":

            try:
                num = int(input("Digite um nùmero inteiro: "))
                dobro = num * 2
                print(f"\nO dobro de {num} é {dobro}.")
            except ValueError:
                print("/nErro: Por favor digite um número inteiro valido ! ") 

        # Exercício 4
        # Peça dois números inteiros. Divida o primeiro pelo segundo, tratando entrada inválida e 
        #divisão por zero
        
        case "4":
            try:
                num1 = int(input("Digite um número inteiro: "))
                num2 = int(input("Digite um segundo número inteiro: "))
                
                divisao = num1/num2
                print("O resultado da divisão do primeiro num{num1}, pelo segundo número {num2} é: {divisao}!")
            except ZeroDivisionError:
                print("\nErro: Não é possível dividir por zero.")

        # Exercício 5
        
        # Solicite um número inteiro para calcular a raiz quadrada. Trate qualquer erro e exibir a 
        # mensagem do erro.

        
        case "5":
            import math

            try:
                numero = int(input("Digite um número inteiro: "))
                raiz = math.sqrt(numero)
                print(f"\nA raiz quadrada de {numero} é {raiz:.2f}.")
            except ValueError as erro:
                print(f"\nErro: {erro}")


        # Exercício 6
        
        # Faça um programa que divide 100 por um número fornecido pelo usuário. Sempre exiba a 
        # mensagem Tentativa concluída, independentemente de erro.
        
        case "6":
            try:
                numero = float(input("Digite um número: "))
                resultado = 100 / numero
                print(f"\n100 dividido por {numero} é igual a {resultado:.2f}.")
            except ValueError:
                print("\nErro: Por favor, digite um número válido.")
            except ZeroDivisionError:
                print("\nErro: Não é possível dividir por zero.")
            finally:
                print("\nTentativa concluída.")

        # Exercício 7
        
        # Peça a idade do usuário. Se a idade for negativa, levante um erro manualmente com a 
        # mensagem Idade inválida. Caso contrário, mostre a idade.
        
        case "7":
            try:
                idade = int(input("Digite sua idade: "))

                if idade < 0:
                    raise ValueError("Idade inválida")

                print(f"\nSua idade é {idade} anos.")

            except ValueError as erro:
                print(f"\nErro: {erro}")

        # Exercício 8
        
        # Solicite um número positivo. Se a entrada for válida e o número for realmente positivo, 
        # mostre o dobro. Use else para exibir o resultado apenas se não houve erro.
        
        case "8":
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

        # Exercício 9
        
        # Peça para o usuário adivinhar um número secreto entre 1 e 10. Conte quantas tentativas 
        # foram necessárias até ele acertar. Trate erros de entrada.
        
        case "9":
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

        # Exercício 10
        
        # Este algoritmo pede números ao usuário para somar.
        # O usuário pode digitar 'sair' para encerrar.
        # No final, o programa mostra a soma total.
        # Entradas inválidas são tratadas.
        
        case "10":
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

        # Exercício 11
        
        # Este algoritmo solicita que o usuário digite 5 números.
        # Para cada número, valida a entrada, acumula a soma
        # e conta quantas entradas foram válidas.
        # No final, exibe a média dos números digitados.
        
        case "11":
            soma = 0
            validos = 0

            for i in range(1, 6):
                try:
                    numero = float(input(f"Digite o {i}º número: "))
                    soma += numero
                    validos += 1
                except ValueError:
                    print("Erro: entrada inválida. Este número será ignorado.")

            if validos > 0:
                media = soma / validos
                print(f"\nForam digitados {validos} números válidos.")
                print(f"A soma total é {soma:.1f}.")
                print(f"A média dos números digitados é {media:.1f}.")
            else:
                print("\nNenhum número válido foi digitado.")

        # Sair do programa
        case "0":
            print("\nSaindo do programa. ")
            break

        # Opção inválida
        case _:
            print("Opção inválida. Tente novamente. ")
