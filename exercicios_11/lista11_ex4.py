def exercicio_04():
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