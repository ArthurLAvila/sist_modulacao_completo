def exercicio_13():
    """
        Este algoritmo faz um jogo em loop com a função jogo() que fica perguntando se o numero que foi digitado é de 0 a 100 e se a palavra for igual a python sem ser case sensitive. 
        Se ele errou uma das duas ele fica mandando outro jogo até que ele vença.

        Autor: Arthur Land Avila Data: 18/09/2025
    """

    # Crie um programa que peça ao usuário para digitar um número e uma palavra. O programa 
    # deve verificar se o número digitado é maior que 10 e se a palavra é "Python". Se ambos 
    # forem verdadeiros, imprima "Você acertou os dois!". Caso contrário, imprima "Tente 
    # novamente".


    #Aqui eu fiz uma recursiva por que pareceu valido
    def jogo(): #Define função jogo()
        valor = int(input("Digite um número de 0 a 100: ")) #entra um valor inteiro 
        palavra = input("Digite uma linguagem de programação: ") #entra uma linguagem de programação qualquer 

        palavra_lower = palavra.lower() #Converte a palavra com algum caracter maiusculo para 

        if valor > 10: # Testa valor digitado maior que 10 
            if palavra_lower == "python": #Palavra digitada  igual a python 
                print("Você acertou !!!") # se os dois casos coincidirem ele da true e mostra que venceu o jogo 
                print("FIM DE JOGO")
            else:
                print("Tente novamente :( ") #caso erre a palavra ele mostra que errou na tela e chama o jogo novemente até acertar as duas propostas 
                jogo() 
        else:
            print("Tente novamente :( ") # se o valor for menor que 10 já de inincio ele erra e chama a função jogo novemente 
            jogo() 

    jogo()
