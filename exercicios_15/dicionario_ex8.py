def exercicio_08():
    """
    Exercício 8 – Estoques de duas lojas
    Autor: Arthur Land Avila
    Data: 10/11/2025
    """

    loja1 = {"arroz": 20, "feijão": 15, "macarrão": 10, "açúcar": 8}
    loja2 = {"feijão": 12, "açúcar": 10, "café": 18, "leite": 25}

    # Mostra os produtos que ambas vendem e os exclusivos
    comuns = loja1.keys() & loja2.keys()
    exclusivos1 = loja1.keys() - loja2.keys()
    exclusivos2 = loja2.keys() - loja1.keys()

    # Soma dos estoques (onde produtos se repetem, soma os valores)
    estoque_total = loja1.copy()
    for produto, quantidade in loja2.items():
        estoque_total[produto] = estoque_total.get(produto, 0) + quantidade

    print(f"Produtos em comum: {comuns}")
    print(f"Exclusivos da loja 1: {exclusivos1}")
    print(f"Exclusivos da loja 2: {exclusivos2}")
    print(f"\nEstoque total combinado: {estoque_total}")
