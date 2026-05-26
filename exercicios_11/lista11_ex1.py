def exercicio_01():
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
