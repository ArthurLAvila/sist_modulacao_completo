"""
Função recursiva que inverte uma string.

Autor: Arthur Land Avila
Data: 17/11/2025

"""
# Exercício 20:
# Crie uma função recursiva para inverter uma string.

def inverter_string(texto):

    if texto == "":
        return ""
    return inverter_string(texto[1:]) + texto[0]


frase = input("Digite uma frase: ")
print("Invertida:", inverter_string(frase))
