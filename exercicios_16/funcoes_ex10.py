"""
Exercício 10: Função resumo que lista itens e informações adicionais.

Autor: Arthur Land Avila
Data: 17/11/2025

"""
# Exercício 10:
# Crie uma função resumo que liste itens e informações adicionais
# de maneira organizada.

def resumo(itens, **info):
    """
    Exibe uma lista de itens e informações adicionais passadas por kwargs.
    'itens' deve ser um iterável (lista, tupla).
    'info' contém pares chave=valor com informações extras.
    """
    print("=== RESUMO ===")
    print("Itens:")
    for item in itens:
        print("-", item)

    if info:
        print("\nInformações adicionais:")
        for chave, valor in info.items():
            print(f"{chave.capitalize()}: {valor}")

# Demonstração
if __name__ == "__main__":
    itens_exemplo = ["Livro", "Caneta", "Caderno"]
    resumo(itens_exemplo, dono="Arthur", quantidade=3)
