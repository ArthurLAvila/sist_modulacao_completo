def exercicio_07():
    # Peça ao usuário para digitar um número e um texto.
    # Informe se o número digitado é divisível por 3 e o texto contém a palavra Python.
    # Se não, informe que a condição não foi atendida.
    # Se o número não for divisível por 3, verifique se o texto contém a palavra "programação".

    num = input("Digite um número: ")
    txt = input("Digite um texto: ")

    if num.isdigit():  
        num = int(num)
        txt = txt.lower()
        # numero divisivel por 3 e texto tem a palavra python em algum lugar python 
        if num % 3 == 0 and "Python" in txt:
            print("O número é divisível por 3 e o texto contém a palavra Python.")
        # numero não é divisivel por 3 e está escrito programação em vez de python em algum lugar no texto digitado
        elif num % 3 != 0 and "programação" in txt:
            print("O número não é divisível por 3, mas o texto contém a palavra 'programação'.")
        else:
            print("A condição não foi atendida.")
    else:
        print("Entrada inválida. Digite um número inteiro válido.")