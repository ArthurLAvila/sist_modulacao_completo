def exercicio_07():
    """
    Exercício 7 – Produtos e preços
    Autor: Arthur Land Avila
    Data: 10/11/2025
    """

    produtos = {
        "mouse": 50,
        "teclado": 120,
        "monitor": 800,
        "fone": 200
    }

    # Calcula os valores solicitados
    mais_caro = max(produtos, key=produtos.get)
    mais_barato = min(produtos, key=produtos.get)
    total = sum(produtos.values())

    print(f"Produto mais caro: {mais_caro} (R${produtos[mais_caro]:.2f})")
    print(f"Produto mais barato: {mais_barato} (R${produtos[mais_barato]:.2f})")
    print(f"Total dos preços: R${total:.2f}")
    print(f"Quantidade de produtos: {len(produtos)}")
