def exercicio_01():
    """

        Este algoritmo pede para o usuário digitar vários números inteiros positivos,
        e só para quando ele decidir encerrar.

        O programa valida se o número digitado é positivo e inteiro.
        Cada número é classificado em categorias entre pequeno, medio e grande. E o sistema conta
        quantos números ficaram em cada uma delas.

        Durante o processo, ele também soma todos os números digitados e no final
        calcula a média deles, mostrando uma mensagem personalizada de acordo com o valor.

        Além disso, o programa verifica se existe algum número que seja múltiplo de todos os outros.

        No final, é mostrado um resumo com:
        - Quantos números tem em cada categoria;
        - A soma total;
        - A média;
        - E se existe um número que é múltiplo de todos.

        O usuário pode decidir a cada passo se quer continuar digitando ou encerrar o programa.

        Autor: Arthur Land Avila
        
        Data: 13/10/2025

    """

    # Crie um programa que receba uma sequência de números inteiros positivos fornecidos 
    # pelo usuário, até que ele decida encerrar a entrada.
    # Valide as entradas para garantir que apenas números inteiros positivos sejam aceitos.
    # Para cada número recebido, classifique-o em categorias definidas por você.
    # Conte quantos números pertencem a cada categoria e acumule a soma total dos números.
    # Ao final, calcule a média dos números e exiba uma mensagem personalizada baseada 
    # nesse valor.
    # Verifique se existe algum número na sequência que seja múltiplo de todos os outros 
    # números.
    # Apresente um resumo final que inclua as contagens por categoria, a soma, a média e o 
    # resultado da verificação de múltiplos.
    # Permita que o usuário decida, a cada passo, se deseja continuar fornecendo números ou 
    # encerrar o processo.

    soma = 0
    contador = 0

    pequenos = 0
    medios = 0
    grandes = 0

    # Variáveis auxiliares para verificar múltiplos
    possivel_multiplo = 0
    todos_sao_divisores = True

    continuar = "s"

    while continuar == "s":
        numero_str = input("Digite um número inteiro positivo: ")

        # Validação
        if not numero_str.isdigit():
            print("Entrada inválida! Digite apenas números inteiros positivos.")
            continue

        numero = int(numero_str)
        if numero <= 0:
            print("O número deve ser positivo.")
            continue

        # Atualiza soma e contador
        soma += numero
        contador += 1

        # Classificação em categorias
        if numero <= 10:
            categoria = "pequeno"
            pequenos += 1
        elif numero <= 50:
            categoria = "médio"
            medios += 1
        else:
            categoria = "grande"
            grandes += 1

        print("O número", numero, "é considerado", categoria)

        # Verificação de múltiplo de todos
        if contador == 1:
            possivel_multiplo = numero
        else:
            if possivel_multiplo % numero != 0:
                todos_sao_divisores = False

        continuar = input("Deseja continuar? (s/n): ").lower()

    # Após o loop
    if contador == 0:
        print("Nenhum número foi digitado.")
    else:
        media = soma / contador

        print("\n===== RESUMO FINAL =====")
        print("Total de números digitados:", contador)
        print("Pequenos (1 a 10):", pequenos)
        print("Médios (11 a 50):", medios)
        print("Grandes (51+):", grandes)
        print("Soma total:", soma)
        print("Média:", round(media, 2))

        # Mensagem personalizada baseada na média
        match media:
            case m if m < 10:
                print("A média é baixa.")
            case m if m <= 50:
                print("A média é moderada.")
            case _:
                print("A média é alta.")

        # Resultado da verificação de múltiplos
        if todos_sao_divisores:
            print("Existe um número que é múltiplo de todos os outros:", possivel_multiplo)
        else:
            print("Não existe número que seja múltiplo de todos os outros.")