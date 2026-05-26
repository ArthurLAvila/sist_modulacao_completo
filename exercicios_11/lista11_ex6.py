def exercicio_06():
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