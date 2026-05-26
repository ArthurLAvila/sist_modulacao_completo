
def exercicio_04():
    try:
        temp = input("Digite a temperatura em Celsius: ")

        if temp.replace(".", "", 1).lstrip("-").isdigit():
            temp = float(temp)

            if temp <= 10:
                print("Muito frio")
            elif temp <= 20:
                print("Frio")
            elif temp <= 25:
                print("Agradável")
            elif temp <= 30:
                print("Quente")
            else:
                print("Muito quente")
        else:
            print("Valor inválido! Digite um número válido (ex: 23 ou 18.5).")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
    
    print("-" * 30)
