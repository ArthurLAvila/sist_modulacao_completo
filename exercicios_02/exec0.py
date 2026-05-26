def exercicio_0():
    frase = input("Digite uma frase: ")
    caractere = input("Digite o caractere a ser removido: ")

    resultado = frase.replace(caractere, "")
    print("Resultado:", resultado)