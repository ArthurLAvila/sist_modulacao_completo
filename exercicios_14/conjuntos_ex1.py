def exercicio_01():
    """ 
        Este exercicio usa um conjunto de números pré definidos, ele adiciona un novo numero neste conjunto pré fabricado
        depois remove dois elementos usando metodos diferentes - remove e discard. ai percorre o conjunto mostrando item por item separadamente.
        
        Autor: Arthur Land Avila  
        Data: 03/11/2025
    """


    # Crie um conjunto com alguns números inteiros pré-definidos.
    # Mostre o conjunto na tela e adicione um novo número.
    # Remova um elemento com .remove() e outro com .discard().
    # Em seguida, percorra o conjunto com um laço for, exibindo cada elemento 
    # separadamente.


    # Cria um conjunto com alguns números inteiros pré-definidos
    numeros = {2, 4, 6, 8, 10}
    print("Conjunto inicial:", numeros)


    # Adiciona um novo número
    numeros.add(12)
    print("Após adicionar o número 12:", numeros)

    # Remove um elemento com .remove() (gera erro se o elemento não existir)
    numeros.remove(4)
    print("Após remover o número 4 com .remove():", numeros)

    # Remove um elemento com .discard() (não gera erro se o elemento não existir)
    numeros.discard(8)
    print("Após remover o número 8 com .discard():", numeros)

    # Percorre o conjunto exibindo cada elemento separadamente
    print("\nElementos do conjunto:")
    for numero in numeros:
        print(numero)