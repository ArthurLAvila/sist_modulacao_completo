def exercicio_14():
    """
        Este algoritmo testa se as duas palavras forem a mesma mesmo com cases diferentes [´maisuculas e minusculas].

        Autor: Arthur Land Avila Data: 18/09/2025
    # """

    # Crie um programa que peça ao usuário para digitar duas palavras, uma em maiúsculas e a 
    # outra em minúsculas. O programa deve comparar essas palavras e exibir se elas são iguais 
    # ou diferentes, levando em conta a diferença entre letras maiúsculas e minúsculas.

    #entrada de uma palavra maiuscula e uma minuscula 
    palavra_maiuscula = input("Digite uma palavra em MAIÚSCULAS: ")
    palavra_minuscula = input("Digite uma palavra em minúsculas: ")

    #teste se as palavras sãom iguais sem ser case sensitive
    if palavra_maiuscula == palavra_minuscula:
        print("As palavras são iguais")
    else:
        print("As palavras são diferentes")
