def exercicio_08():
    """
        Este algoritmo define em qual dia da semana estamos atualmente dependendo do numero que o usuário digitou na entrada. (de 1 a 7 sendo 
        domingo 1 e sabado 7) usando match case :v.
        
        Autor: Arthur Land Avila Data: 03/10/2025
    """

    # Peça ao usuário um número de 1 a 7 e use match case para imprimir o nome do dia da 
    # semana correspondente:

    # Pede um número de 1 a 7
    numero = int(input("Digite um número de 1 a 7: "))

    # Usa match case para exibir o dia da semana correspondente
    match numero:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-feira")
        case 3:
            print("Terça-feira")
        case 4:
            print("Quarta-feira")
        case 5:
            print("Quinta-feira")
        case 6:
            print("Sexta-feira")
        case 7:
            print("Sábado")
        case _:
            print("Número inválido. Digite apenas de 1 a 7.")
