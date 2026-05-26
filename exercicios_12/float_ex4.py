def exercicio_04():
    """
    Exercício 4
    Peça para o usuário informar N números reais.
    Mostre os números na ordem inversa e a soma total.
    """


    # Peça para o usuário informar uma quantidade N de números reais para inserir em uma 
    # lista.
    # Crie a lista validando entradas.
    # Mostre os números na ordem inversa usando um laço while.
    # Mostre a soma total dos números.

    lista = []
    try:
        quantidade = int(input("Quantos números deseja inserir? "))
        for i in range(quantidade):
            while True:
                try:
                    num = float(input(f"Digite o {i+1}º número: "))
                    lista.append(num)
                    break
                except ValueError:
                    print("Digite um número real válido.")
        print("\nNúmeros em ordem inversa:")
        i = len(lista) - 1
        while i >= 0:
            print(lista[i])
            i -= 1
        print(f"Soma total dos números: {sum(lista)}")
    except ValueError:
        print("Entrada inválida.")