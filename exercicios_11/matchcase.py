"""
Autor: Arthur Land Avila
Data: 24/10/2025
Descrição: Programa com 8 exercícios sobre listas, laços e validações em Python.
Usa estrutura match-case e tratamento de exceções (try-except) para as entradas do usuário.
"""

while True:
    print("\n=== MENU DE EXERCÍCIOS ===")
    print("1 - Exercício 1")
    print("2 - Exercício 2")
    print("3 - Exercício 3")
    print("4 - Exercício 4")
    print("5 - Exercício 5")
    print("6 - Exercício 6")
    print("7 - Exercício 7")
    print("8 - Exercício 8")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                """
                Exercício 1 - Lista de números reais
                """
                # Enunciado:
                # Peça ao usuário para informar quantos números reais deseja inserir em uma lista.
                # Solicite os números um por um validando entrada float.
                # Mostre a lista criada.
                # Exiba os números um por um usando um laço for.

                try:
                    n = int(input("Quantos números reais deseja inserir? "))
                    numeros = []
                    for i in range(n):
                        while True:
                            try:
                                num = float(input(f"Digite o {i+1}º número: "))
                                numeros.append(num)
                                break
                            except ValueError:
                                print("Entrada inválida! Digite um número real válido.")
                    print("\nLista criada:", numeros)
                    print("Números digitados:")
                    for num in numeros:
                        print(num)
                except ValueError:
                    print("Erro: digite um número inteiro válido para a quantidade.")


            case 2:
                """
                Exercício 2 - Lista de temperaturas
                """
                # Enunciado:
                # Peça ao usuário para informar a quantidade de temperaturas que deseja registrar.
                # Armazene em uma lista as temperaturas informadas com validação.
                # Mostre a maior e a menor temperatura da lista.
                # Calcule e exiba a média das temperaturas.
                # Utilize laços para percorrer a lista.

                try:
                    n = int(input("Quantas temperaturas deseja registrar? "))
                    temperaturas = []
                    for i in range(n):
                        while True:
                            try:
                                temp = float(input(f"Digite a {i+1}ª temperatura: "))
                                temperaturas.append(temp)
                                break
                            except ValueError:
                                print("Entrada inválida! Digite uma temperatura válida.")
                    print(f"\nMaior temperatura: {max(temperaturas)}°")
                    print(f"Menor temperatura: {min(temperaturas)}°")
                    media = sum(temperaturas) / len(temperaturas)
                    print(f"Média das temperaturas: {media:.2f}°")
                except ValueError:
                    print("Erro: informe um número inteiro válido.")


            case 3:
                """
                Exercício 3 - Preços e limite
                """
                # Enunciado:
                # Peça ao usuário para inserir vários preços de produtos float em uma lista.
                # Valide cada entrada.
                # Depois, solicite um valor limite.
                # Exiba todos os preços da lista que são maiores que esse limite, usando um laço.

                try:
                    n = int(input("Quantos preços deseja inserir? "))
                    precos = []
                    for i in range(n):
                        while True:
                            try:
                                preco = float(input(f"Digite o preço {i+1}: R$"))
                                precos.append(preco)
                                break
                            except ValueError:
                                print("Entrada inválida! Digite um valor numérico.")
                    limite = float(input("\nDigite um valor limite: R$"))
                    print(f"\nPreços maiores que R${limite:.2f}:")
                    for p in precos:
                        if p > limite:
                            print(f"R${p:.2f}")
                except ValueError:
                    print("Erro: entrada inválida!")


            case 4:
                """
                Exercício 4 - Números e soma
                """
                # Enunciado:
                # Peça para o usuário informar uma quantidade N de números reais para inserir em uma lista.
                # Crie a lista validando entradas.
                # Mostre os números na ordem inversa usando um laço while.
                # Mostre a soma total dos números.

                try:
                    n = int(input("Quantos números reais deseja inserir? "))
                    numeros = []
                    for i in range(n):
                        while True:
                            try:
                                num = float(input(f"Digite o {i+1}º número: "))
                                numeros.append(num)
                                break
                            except ValueError:
                                print("Entrada inválida!")
                    print("\nNúmeros em ordem inversa:")
                    i = len(numeros) - 1
                    while i >= 0:
                        print(numeros[i])
                        i -= 1
                    print(f"\nSoma total: {sum(numeros):.2f}")
                except ValueError:
                    print("Erro: digite um número inteiro válido.")


            case 5:
                """
                Exercício 5 - Verificação de número na lista
                """
                # Enunciado:
                # Peça ao usuário para informar quantos valores float deseja adicionar a uma lista.
                # Insira os valores com validação.
                # Pergunte ao usuário um número float para verificar se ele está na lista.
                # Mostre a posição do número na lista, ou uma mensagem se não estiver presente.
                # Use laços para fazer a busca.

                try:
                    n = int(input("Quantos valores deseja adicionar? "))
                    valores = []
                    for i in range(n):
                        while True:
                            try:
                                val = float(input(f"Digite o {i+1}º valor: "))
                                valores.append(val)
                                break
                            except ValueError:
                                print("Entrada inválida! Digite um número real.")
                    busca = float(input("Digite um número para verificar: "))
                    encontrado = False
                    for i in range(len(valores)):
                        if valores[i] == busca:
                            print(f"Número encontrado na posição {i}.")
                            encontrado = True
                    if not encontrado:
                        print("Número não encontrado na lista.")
                except ValueError:
                    print("Erro: entrada inválida!")


            case 6:
                """
                Exercício 6 - Alturas acima da média
                """
                # Enunciado:
                # Crie uma lista de alturas float com N elementos informados pelo usuário.
                # Exiba quantas alturas estão acima da média da lista.
                # Mostre essa quantidade ao final.
                # Use laços e listas.

                try:
                    n = int(input("Quantas alturas deseja registrar? "))
                    alturas = []
                    for i in range(n):
                        while True:
                            try:
                                alt = float(input(f"Digite a altura {i+1} (em metros): "))
                                alturas.append(alt)
                                break
                            except ValueError:
                                print("Entrada inválida.")
                    media = sum(alturas) / len(alturas)
                    acima = [a for a in alturas if a > media]
                    print(f"Média das alturas: {media:.2f} m")
                    print(f"Quantidade acima da média: {len(acima)}")
                except ValueError:
                    print("Erro: digite valores numéricos válidos.")


            case 7:
                """
                Exercício 7 - Notas e média
                """
                # Enunciado:
                # Peça ao usuário para informar a quantidade de notas de uma prova.
                # Insira as notas numa lista float com validação.
                # Calcule e mostre:
                # A média das notas
                # Quantas notas são maiores ou iguais à média
                # Use laços para esses cálculos.

                try:
                    n = int(input("Quantas notas deseja inserir? "))
                    notas = []
                    for i in range(n):
                        while True:
                            try:
                                nota = float(input(f"Digite a nota {i+1}: "))
                                notas.append(nota)
                                break
                            except ValueError:
                                print("Entrada inválida.")
                    media = sum(notas) / len(notas)
                    acima = sum(1 for n in notas if n >= media)
                    print(f"Média: {media:.2f}")
                    print(f"Notas >= média: {acima}")
                except ValueError:
                    print("Erro: digite valores válidos.")


            case 8:
                """
                Exercício 8 - Desconto em preços
                """
                # Enunciado:
                # Peça para o usuário digitar preços de vários produtos e armazene em uma lista.
                # Depois, peça para digitar um valor float de desconto.
                # Gere uma nova lista com os preços já descontados, sem modificar a original.
                # Exiba ambas as listas, usando laços para percorrê-las.

                try:
                    n = int(input("Quantos produtos deseja registrar? "))
                    precos = []
                    for i in range(n):
                        while True:
                            try:
                                preco = float(input(f"Digite o preço do produto {i+1}: R$"))
                                precos.append(preco)
                                break
                            except ValueError:
                                print("Entrada inválida.")
                    desconto = float(input("Digite o valor de desconto (%): "))
                    nova_lista = [p - (p * desconto / 100) for p in precos]

                    print("\n--- Lista original ---")
                    for p in precos:
                        print(f"R${p:.2f}")
                    print("\n--- Lista com desconto ---")
                    for p in nova_lista:
                        print(f"R${p:.2f}")
                except ValueError:
                    print("Erro: digite números válidos.")


            case 0:
                print("Encerrando o programa... Até mais!")
                break

            case _:
                print("Opção inválida! Tente novamente.")

    except ValueError:
        print("Erro: digite um número válido.")
