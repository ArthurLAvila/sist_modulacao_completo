def exercicio_15():
    idade = input("Digite sua idade: ").strip()
    carteira = input("Você tem carteira? (s/n): ").strip().lower()
    habilitado = input("Você está habilitado? (s/n): ").strip().lower()

    if idade.isdigit() and carteira in ("s", "n") and habilitado in ("s", "n"):
        idade = int(idade)

        if idade >= 18 and carteira == "s" and habilitado == "s":
            print("Você pode dirigir.")
        else:
            if not idade >= 18:
                print("Não pode dirigir: menor de 18 anos.")
            elif not carteira == "s":
                print("Não pode dirigir: não possui carteira.")
            elif not habilitado == "s":
                print("Não pode dirigir: não está habilitado.")
    else:
        print("Entrada inválida. Verifique os dados digitados.")
