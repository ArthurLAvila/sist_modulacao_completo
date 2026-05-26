"""
Recebe nome, idade e cidade e exibe essas informações formatadas.

Autor: Arthur Land Avila
Data: 17/11/2025

"""

# Exercício 9:
# Crie uma função mostrar_dados que receba informações como
# nome, idade, cidade e exiba na tela.

def mostrar_dados(nome, idade, cidade):
    
    print("Nome:", nome)
    print("Idade:", idade)
    print("Cidade:", cidade)

# Demonstração
if __name__ == "__main__":
    # exemplo com entrada do usuário
    nome = input("Digite o nome: ")
    try:
        idade = int(input("Digite a idade: "))
    except ValueError:
        idade = 0
    cidade = input("Digite a cidade: ")
    mostrar_dados(nome, idade, cidade)
