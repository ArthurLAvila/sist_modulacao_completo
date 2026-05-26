def exercicio_01():
    """
    Exercício 1 – Dicionário com informações de uma pessoa
    Autor: Arthur Land Avila
    Data: 10/11/2025
    """

    # Criar um dicionário com informações pessoais.
    # Exibir o dicionário completo e acessar uma chave específica.
    # Adicionar uma nova chave chamada 'profissão' e remover a chave 'cidade'.
    # Percorrer o dicionário mostrando todas as chaves e valores separadamente.


    # Cria o dicionário inicial
    pessoa = {
        "nome": "Arthur",
        "idade": 24,
        "cidade": "São Paulo"
    }

    # Mostra o dicionário completo
    print("Dicionário completo:", pessoa)

    # Acessa uma chave específica
    print(f"Nome da pessoa: {pessoa['nome']}")

    # Adiciona uma nova chave
    pessoa["profissao"] = "Estudante de TI"

    # Remove a chave 'cidade'
    pessoa.pop("cidade")

    # Mostra o dicionário atualizado
    print("\nDicionário atualizado:", pessoa)

    # Percorre o dicionário mostrando cada chave e valor
    print("\n--- Chaves e valores ---")
    for chave, valor in pessoa.items():
        print(f"{chave}: {valor}")
