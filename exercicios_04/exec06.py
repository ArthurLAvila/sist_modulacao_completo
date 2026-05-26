def exercicio_06():
    try:
        chovendo = input("Está chovendo? (s/n): ").lower().strip()

        if chovendo in ("s", "n"):
            if chovendo == "s":
                print("Leve um guarda-chuva!")
            else:
                print("Você pode sair sem guarda-chuva.")
        else:
            print("Entrada inválida, responda apenas com 's' ou 'n'.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
