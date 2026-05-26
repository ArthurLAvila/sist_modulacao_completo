from .imports import *

def main_08():
    while True:
        print("\n Menu - Exercícios 1 ")
        print("1 - Exercício 1")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                exercicio_01()    
            case "0":
                print("Saindo do menu de exercícios 1...")
                break
            case _:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main_08()