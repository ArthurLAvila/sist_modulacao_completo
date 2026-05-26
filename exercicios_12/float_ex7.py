def exercicio_07():
    """
    Exercício 7
    Peça ao usuário para informar a quantidade de notas.
    Mostre a média e quantas são maiores ou iguais a ela.
    """

    # Peça ao usuário para informar a quantidade de notas de uma prova.
    # Insira as notas numa lista float com validação.
    # Calcule e mostre:
    # A média das notas
    # Quantas notas são maiores ou iguais a média
    # Use laços para esses cálculos.

    notas = []
    try:
        quantidade = int(input("Quantas notas deseja inserir? "))
        for i in range(quantidade):
            while True:
                try:
                    nota = float(input(f"Digite a {i+1}ª nota: "))
                    notas.append(nota)
                    break
                except ValueError:
                    print("Digite uma nota válida.")
        media = sum(notas) / len(notas)
        acima_media = 0
        for n in notas:
            if n >= media:
                acima_media += 1
        print(f"\nMédia das notas: {media:.2f}")
        print(f"{acima_media} notas são maiores ou iguais à média.")
    except ValueError:
        print("Entrada inválida.")