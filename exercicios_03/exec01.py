def exercicio_01():
    try:
        nota = float(input("Digite uma nota de 0 a 10: "))
        nota = abs(nota)
        nota = round(nota, 1)

        if nota > 10:
            print(f"{nota} → Nota inválida! Digite um valor entre 0 e 10.")
        elif nota < 5:
            print(f"{nota} → Reprovado")
        elif nota <= 6.9:
            print(f"{nota} → Recuperação")
        else:
            print(f"{nota} → Aprovado")

    except ValueError:
        print("Erro: digite um número válido (ex: 7.5, 6.0, etc.)")

    print("-" * 30)