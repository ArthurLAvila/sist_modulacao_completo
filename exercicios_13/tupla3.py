def exercicio_03():
    """
    Lista de Exercícios – Tuplas
    Autor: Arthur Land Avila
    Data: 28/10/2025

    """

    # Crie uma tupla com valores numéricos inseridos pelo usuário (float).
    # Mostre o tamanho da tupla, o maior e o menor valor e a soma total.

    try:
        quantidade = int(input("\nQuantos números deseja inserir? "))
        valores = []
        for i in range(quantidade):
            while True:
                valor = input(f"Digite o valor {i + 1}: ").replace(",", ".")
                try:
                    valor_float = float(valor)
                    valores.append(valor_float)
                    break
                except ValueError:
                    print("Erro: valor inválido. Digite um número real.")
        tupla_valores = tuple(valores)
        print(f"\nTupla criada: {tupla_valores}")
        print(f"Tamanho: {len(tupla_valores)}")
        print(f"Maior: {max(tupla_valores)} | Menor: {min(tupla_valores)} | Soma: {sum(tupla_valores)}")
    except ValueError:
        print("Erro: entrada inválida!")