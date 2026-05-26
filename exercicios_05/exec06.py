def exercicio_06():
    # Peça ao usuário para digitar duas palavras e uma opção de E ou OU.
    # Se a opção for E, verifique se ambas as palavras têm mais de 5 caracteres e não são iguais.
    # Se a opção for OU, verifique se pelo menos uma das palavras tem mais de 5 caracteres ou
    # se são iguais.

    palavra1 = input("Digite uma palavra: ")
    palavra2 = input("Digite uma segunda palavra: ")

    opcao = input("Digite uma opção: (e/ou)").lower()    
    #primeiro caso "e"
    if opcao == "e":
        # tamanho da palavra1 maior que 5 e da 2 tamb & palavra 1 e 2 são diferentes 
        if len(palavra1) > 5 and len(palavra2) > 5 and palavra1 != palavra2:
            print("Suas palavras são diferentes e maiores que 5 caracteres.")
        else:
            print("Pelo menos uma das palavras não tem mais que 5 caracteres ou elas são iguais.")
        #segundo caso "ou"
    elif opcao == "ou":
        # tamanho da palavra 1 maior que 5 ou a palavra 2 é maior que 5 || as palavras são iguais !
        if len(palavra1) > 5 or len(palavra2) > 5 or palavra1 == palavra2:
            print("Pelo menos uma das palavras tem mais de 5 caracteres ou elas são iguais.")
        else:
            print("Nenhuma palavra tem mais de 5 caracteres e elas são diferentes.")

    else:
        print("Opção incorreta.")