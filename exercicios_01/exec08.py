def exercicio_08():
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    media = sum(notas) / 4
    print(f"A média das notas é: {media}")