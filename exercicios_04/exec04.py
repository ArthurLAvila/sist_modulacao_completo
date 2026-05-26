def exercicio_04():  
    try:
        idade = input("Digite sua idade: ")
        carteira = input("Você tem carteira de motorista? (s/n): ").lower().strip()

        # Confirma se idade é número válido (aceita positivos) e se carteira é 's' ou 'n'
        if idade.lstrip("-").isdigit() and carteira in ("s", "n"):
            idade = int(idade)

            if idade >= 18 and carteira == "s":
                print("Você pode dirigir.")
            elif idade < 18:
                print("Você ainda não tem idade para dirigir.")
            elif carteira == "n":
                print("Você precisa ter carteira para dirigir.")
        else:
            print("Entrada inválida! Digite uma idade numérica e 's' ou 'n' para carteira.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
