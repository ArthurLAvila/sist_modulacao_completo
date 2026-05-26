from. imports import*

def main_16():
    while True:
        print("\n Menu - Exercícios 1 ")
        print("1 - Exercício 1")
        print("2 - Exercício 2")
        print("3 - Exercício 3")
        print("4 - Exercício 4")
        print("5 - Exercício 5")
        print("6 - Exercício 6")
        print("7 - Exercício 7")
        print("8 - Exercício 8")
        print("9 - Exercício 9")
        print("10 - Exercício 10")
        print("11 - Exercício 11")
        print("12 - Exercício 12")
        print("13 - Exercício 13")
        print("14 - Exercício 14")
        print("15 - Exercício 15")
        print("16 - Exercício 16")
        print("17 - Exercício 17")
        print("18 - Exercício 18")
        print("19 - Exercício 19")
        print("20 - Exercício 20")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                exercicio_01()
            case "2":
                exercicio_02()
            case "3":
                exercicio_03()
            case "4":
                exercicio_04()
            case "5":
                exercicio_05()
            case "6":
                exercicio_06()
            case "7":
                exercicio_07()
            case "8":
                exercicio_08()
            case "9":
                exercicio_09()
            case "10":
                exercicio_10()
            case "11":
                exercicio_11()
            case "12":
                exercicio_12()
            case "13":
                exercicio_13()
            case "14":
                exercicio_14()
            case "15":
                exercicio_15()                
            case "16":
                exercicio_16()
            case "17":
                exercicio_17()
            case "18":
                exercicio_18()
            case "19":
                exercicio_19()
            case "20":
                exercicio_20()                        
            case "0":
                print("Saindo do menu de exercícios 1...")
                break
            case _:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main_16()