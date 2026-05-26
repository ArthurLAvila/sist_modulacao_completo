def exercicio_02():
    """
    Lista de Exercícios – Tuplas
    Autor: Arthur Land Avila
    Data: 28/10/2025

    """

    # Peça ao usuário para informar quantos nomes deseja inserir.
    # Solicite os nomes um por um e armazene em uma tupla.
    # Mostre a tupla criada e exiba cada nome em uma linha usando um laço for.
    


    try:
        quantidade = int(input("\nQuantos nomes deseja inserir? "))
        nomes_lista = []
        for i in range(quantidade):
            nome = input(f"Digite o nome {i + 1}: ").strip()
            if not nome.isalpha():
                print("Aviso: o nome contém caracteres não alfabéticos, mas será aceito.")
            nomes_lista.append(nome)
        nomes = tuple(nomes_lista)
        print(f"\nTupla criada: {nomes}")
        print("Nomes informados:")
        for nome in nomes:
            print("-", nome)
    except ValueError:
        print("Erro: digite apenas números válidos para a quantidade!")