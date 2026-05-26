def exercicio_12():    
    try:
        nota = input("Digite a nota (0 a 10): ")
        faltas = input("Digite o número de faltas: ")

        # Verifica se as entradas são válidas
        if nota.replace(".", "", 1).isdigit() and faltas.isdigit():
            nota = float(nota)
            faltas = int(faltas)

            if nota > 10 or nota < 0:
                print("Nota inválida! Deve estar entre 0 e 10.")
            elif nota >= 7 and faltas <= 3:
                print("Aprovado")
            elif 5 <= nota <= 6.9 and 4 <= faltas <= 5:
                print("Recuperação")
            elif nota < 5 and faltas >= 6:
                print("Reprovado")
            else:
                print("Situação indefinida dentro dos parâmetros informados.")
        else:
            print("Entrada inválida. Digite valores numéricos válidos.")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
