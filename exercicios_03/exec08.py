def exercicio_08():
    try:
        senha = input("Digite uma senha: ")

        if len(senha) < 8:
            print("Senha inválida: deve ter pelo menos 8 caracteres.")
        elif any(c.islower() for c in senha):
            print("Senha válida!")
        else:
            print("Senha inválida: deve conter pelo menos uma letra minúscula.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

    print("-" * 30)