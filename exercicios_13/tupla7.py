def exercicio_07():
    """
    Lista de Exercícios – Tuplas
    Autor: Arthur Land Avila
    Data: 28/10/2025

    """

    # Peça ao usuário para informar uma quantidade de notas (float).
    # Armazene-as em uma tupla.
    # Calcule e exiba a média das notas e quantas estão acima ou iguais à média.

    try:
        quantidade = int(input("\nQuantas notas deseja inserir? "))
        notas = []
        for i in range(quantidade):
            while True:
                nota = input(f"Digite a nota {i + 1}: ").replace(",", ".")
                try:
                    nota_float = float(nota)
                    notas.append(nota_float)
                    break
                except ValueError:
                    print("Erro: valor inválido. Digite uma nota numérica.")
        notas_tupla = tuple(notas)
        media = sum(notas_tupla) / len(notas_tupla)
        acima_media = sum(1 for n in notas_tupla if n >= media)
        print(f"\nNotas: {notas_tupla}")
        print(f"Média: {media:.2f}")
        print(f"Notas acima ou iguais à média: {acima_media}")
    except ValueError:
        print("Erro: entrada inválida!")
