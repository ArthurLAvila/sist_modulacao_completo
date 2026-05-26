def exercicio_06():
    """
    Exercício 6
    Crie uma lista de alturas e exiba quantas estão acima da média.
    """

    # Crie uma lista de alturas float com N elementos informados pelo usuário.
    # Exiba quantas alturas estão acima da média da lista.
    # Mostre essa quantidade ao final.
    # Use laços e listas.


    alturas = []
    try:
        quantidade = int(input("Quantas alturas deseja registrar? "))
        for i in range(quantidade):
            while True:
                try:
                    a = float(input(f"Digite a {i+1}ª altura: "))
                    alturas.append(a)
                    break
                except ValueError:
                    print("Digite uma altura válida.")
        media = sum(alturas) / len(alturas)
        acima = 0
        for a in alturas:
            if a > media:
                acima += 1
        print(f"\nMédia das alturas: {media:.2f}")
        print(f"{acima} alturas estão acima da média.")
    except ValueError:
        print("Entrada inválida.")