def exercicio_07():
    """
    Exercício 7 - Notas e média
    """
    # Enunciado:
    # Peça ao usuário para informar a quantidade de notas de uma prova.
    # Insira as notas numa lista float com validação.
    # Calcule e mostre:
    # A média das notas
    # Quantas notas são maiores ou iguais à média
    # Use laços para esses cálculos.

    try:
        n = int(input("Quantas notas deseja inserir? "))
        notas = []
        for i in range(n):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i+1}: "))
                    notas.append(nota)
                    break
                except ValueError:
                    print("Entrada inválida.")
        media = sum(notas) / len(notas)
        acima = sum(1 for n in notas if n >= media)
        print(f"Média: {media:.2f}")
        print(f"Notas >= média: {acima}")
    except ValueError:
        print("Erro: digite valores válidos.")