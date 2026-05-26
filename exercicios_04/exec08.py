def exercicio_08():        
    try:
        txt = input("Digite um texto: ").strip()

        if not txt:  # texto vazio ou só espaços
            print("Você não digitou nada.")
        elif len(txt) > 10:
            print("Texto maior que 10 caracteres.")
        else:
            print("Texto com 10 ou menos caracteres.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")