"""
Exibe uma saudação usando o nome fornecido ou um valor padrão.

Autor: Arthur Land Avila
Data: 17/11/2025

"""

# Exercício 7:
# Crie uma função saudação que cumprimente o usuário pelo nome
# ou use o valor padrão.

def saudacao(nome="usuário"):
        
    print("Olá,", nome)

# Demonstração
if __name__ == "__main__":
    saudacao()           # usa valor padrão
    saudacao("Arthur")   # usa o nome fornecido
