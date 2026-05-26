def exercicio_05():
    try:
        idade = input("Digite a sua idade: ")

        if idade.isdigit():
            idade = int(idade)

            if 0 <= idade <= 4:
                print("Categoria: Bebê")
            elif 5 <= idade <= 12:
                print("Categoria: Criança")
            elif 13 <= idade <= 17:
                print("Categoria: Adolescente")
            elif 18 <= idade <= 59:
                print("Categoria: Adulto")
            else:
                print("Categoria: Idoso")
        else:
            print("Entrada inválida! Digite apenas números inteiros positivos.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

    print("-" * 30)