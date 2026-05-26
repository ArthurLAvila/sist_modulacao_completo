def exercicio_11():
    # Peça ao usuário para digitar seu nome, idade e se está com documentos em mãos s ou n.
    # Informe se ele pode votar nas eleições:
    # Se tiver 16 anos ou mais e tiver documentos.
    # Ou se tiver 18 anos ou mais, independente dos documentos, ele já está autorizado a votar.


    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    documentos = input("Está com documentos em mãos? (s/n): ").lower()

    if idade.isdigit():
        idade = int(idade)
        # tem mais de 16 anos e esta com o documento ou já é maior de idade - 18 anos 
        if (idade >= 16 and documentos == "s") or idade >= 18:
            print(f"{nome}, você pode votar nas eleições ")
        else:
            print(f"{nome}, você NÃO pode votar nas eleições ")
    else:
        print("Idade inválida, digite apenas números.")