def exercicio_11():
    try:
        # Peça nome de usuário e senha.
        usuario = input("Digite o nome de usuário: ").strip()
        senha = input("Digite a senha: ").strip()

        # Se algum estiver vazio
        if not usuario or not senha:
            print("Usuário e senha não podem ser vazios.")
        # Se for admin e senha correta
        elif usuario == "admin" and senha == "1234":
            print("Acesso permitido.")
        # Caso contrário
        else:
            print("Acesso negado.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")