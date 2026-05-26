def exercicio_05():
    """
    Lista de Exercícios – Tuplas
    Autor: Arthur Land Avila
    Data: 28/10/2025

    """

    # Crie uma tupla com valores inteiros e mostre-a.
    # Converta a tupla em uma lista, adicione um novo número informado pelo usuário,
    # e depois converta novamente para tupla.
    # Exiba a nova tupla final.

    valores_tupla = (3, 7, 12, 25)
    print(f"\nTupla original: {valores_tupla}")
    try:
        novo_numero = int(input("Digite um novo número para adicionar: "))
        valores_lista = list(valores_tupla)
        valores_lista.append(novo_numero)
        nova_tupla = tuple(valores_lista)
        print(f"Nova tupla: {nova_tupla}")
    except ValueError:
        print("Erro: digite apenas um número inteiro válido!")