def exercicio_02():
    """
    Exercício 2
    Peça ao usuário para informar a quantidade de temperaturas.
    Armazene em uma lista com validação.
    Mostre a maior, a menor e a média das temperaturas.
    """


    # Peça ao usuário para informar a quantidade de temperaturas que deseja registrar.
    # Armazene em uma lista as temperaturas informadas com validação.
    # Mostre a maior e a menor temperatura da lista.
    # Calcule e exiba a média das temperaturas.
    # Utilize laços para percorrer a lista.

    temperaturas = []
    try:
        quantidade = int(input("Quantas temperaturas deseja registrar? "))
        for i in range(quantidade):
            while True:
                try:
                    temp = float(input(f"Digite a {i+1}ª temperatura: "))
                    temperaturas.append(temp)
                    break
                except ValueError:
                    print("Digite uma temperatura válida.")
        print(f"\nMaior temperatura: {max(temperaturas)}")
        print(f"Menor temperatura: {min(temperaturas)}")
        media = sum(temperaturas) / len(temperaturas)
        print(f"Média das temperaturas: {media:.2f}")
    except ValueError:
        print("Valor inválido. Digite um número inteiro válido.")
        