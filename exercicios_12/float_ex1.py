def exercicio_01():
    """
    Exercício 1
    Peça ao usuário para informar quantos números reais deseja inserir em uma lista.
    Solicite os números um por um validando entrada float.
    Mostre a lista criada e exiba os números um por um.
    """

    # Peça ao usuário para informar quantos números reais deseja inserir em uma lista.
    # Solicite os números um por um validando entrada float.
    # Mostre a lista criada.
    # Exiba os números um por um usando um laço for.


    numeros = []
    try:
        quantidade = int(input("Quantos números reais deseja inserir? "))
        for i in range(quantidade):
            while True:
                try:
                    num = float(input(f"Digite o {i+1}º número: "))
                    numeros.append(num)
                    break
                except ValueError:
                    print("Entrada inválida! Digite um número real.")
        print("\nLista criada:", numeros)
        print("Números digitados:")
        for n in numeros:
            print(n)
    except ValueError:
        print("Valor inválido. Digite um número inteiro válido.")