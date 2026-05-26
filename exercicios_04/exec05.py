def exercicio_05():  
    try:
        dinheiro = input("Você tem dinheiro? (s/n): ").lower().strip()
        convite = input("Você tem convite? (s/n): ").lower().strip()

        # Verifica se entradas são válidas
        if dinheiro in ("s", "n") and convite in ("s", "n"):
            if dinheiro == "s" or convite == "s":
               print("Você pode entrar no evento.")
            else:
                print("Você NÃO pode entrar no evento.")
        else:
            print("Entrada inválida! Digite apenas 's' ou 'n'.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
