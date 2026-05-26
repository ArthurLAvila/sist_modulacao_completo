def exercicio_09():
    # Peça ao usuário para digitar um número inteiro e um texto.
    # Verifique se o número é par ou ímpar e, se o texto for Python, informe que o número e o 
    # texto são válidos. Caso contrário, informe o tipo do número par ou ímpar e que o texto é 
    # inválido.

    num = input("Digite um número inteiro: ")
    texto = input("Digite um texto qualquer: ")

    if num.lstrip("-").isdigit():  # aceita números negativos também
        num = int(num)
        texto = texto.lower()  # passa pra minúsculo
        if num % 2 == 0:
            tipo = "par"
        else:
            tipo = "ímpar"

        if texto == "python":
            print(f"O número é {tipo} e o texto é válido (Python).")
        else:
            print(f"O número é {tipo}, mas o texto é inválido.")
    else:
        print("Entrada inválida. Digite um número inteiro.")