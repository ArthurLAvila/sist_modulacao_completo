def exercicio_06():
    """
    Cria um conjunto de numeros criado pelo usuario em um conjunto não lista ou tupla.
    Passa o conjunto parta o formato de lista usando add em uma lista criada já no inicio do codigo.
    Ordena os valores em crescente, e mostra a lista em um print.
    Converte a lista para um outro conjunto agora ordenado. 

    Autor: Arthur Land Avila  
    Data: 03/11/2025
    """

# Exercício 6
# Crie um conjunto com números digitados pelo usuário.
# Em seguida, converta o conjunto em uma lista, ordene os valores e mostre a lista 
# ordenada.
# Depois, converta novamente a lista em conjunto e mostre o resultado.


# Criação do conjunto com números digitados pelo usuário
conjunto_numeros = set()

# Coleta dos números
for _ in range(5):
    numero = int(input("Digite um número: "))
    conjunto_numeros.add(numero)

# Converte o conjunto para uma lista e ordena
lista_ordenada = list(conjunto_numeros)
lista_ordenada.sort()

print("Lista ordenada:", lista_ordenada)

# Converte novamente a lista em conjunto
novo_conjunto = set(lista_ordenada)
print("Conjunto final:", novo_conjunto)
