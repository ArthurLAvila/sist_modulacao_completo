from .imports import * 
def main_11():
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
            case "0":
                print("Saindo do menu de exercícios 1...")
                break
            case _:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main_11()