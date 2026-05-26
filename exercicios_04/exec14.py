def exercicio_14():
    # Peça uma resposta s ou n para as perguntas: Está chovendo? e Está frio?
    # Informe se não está chovendo ou não está frio

    chovendo = input("Está chovendo? (s/n): ").strip().lower()
    frio = input("Está frio? (s/n): ").strip().lower()

    if chovendo in ("s", "n") and frio in ("s", "n"):
        if chovendo == "s" and frio == "s":
            print("Está chovendo e está frio.")
        else:
            print("Não está chovendo ou não está frio.")
    else:
        print("Entrada inválida. Responda apenas com 's' ou 'n'.")