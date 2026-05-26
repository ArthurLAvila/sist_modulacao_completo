def exercicio_02():
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