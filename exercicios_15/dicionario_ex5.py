def exercicio_05():
    """
    Exercício 5 – Dicionário aninhado de alunos e notas
    Autor: Arthur Land Avila
    Data: 10/11/2025
    """

    # Dicionário aninhado
    alunos = {
        "João": {"nota": 8.5},
        "Maria": {"nota": 9.0},
        "Pedro": {"nota": 7.5}
    }

    # Mostra nome e nota de cada aluno
    for nome, info in alunos.items():
        print(f"{nome}: nota {info['nota']}")

    # Calcula a média das notas
    notas = [info["nota"] for info in alunos.values()]
    media = sum(notas) / len(notas)
    print(f"\nMédia das notas: {media:.2f}")
