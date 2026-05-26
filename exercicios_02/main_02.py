from .imports import *



def main_02():
    while True:
        print("\n Menu - Exercícios 2 ")
        print("1 - Exercício 1")
        print("2 - Exercício 2")
        print("3 - Exercício 3")
        print("4 - Exercício 4")
        print("5 - Exercício 5")
        print("6 - Exercício 6")
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
            case "0":
                print("Saindo do menu de exercícios 2...")
                break
            case _:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main_02()