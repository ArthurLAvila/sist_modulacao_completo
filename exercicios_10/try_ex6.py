def exercicio_06():
    """
        Este algoritmo divide o número 100 por um número que o usuário inseriu. Ele mostra quando o programa concluiu e 
        mostra uma mensagem de erro se alguma coisa não foi inserida corretamente como o numero 0 pois essa divisão não existe 
        ou se ele botar uma letra ou mais.

        Autor: Arthur Land Avila
        Data: 16/10/2025
    """


    # Faça um programa que divide 100 por um número fornecido pelo usuário. Sempre exiba a 
    # mensagem Tentativa concluída, independentemente de erro.


    try:
        numero = float(input("Digite um número: "))
        resultado = 100 / numero
        print(f"\n100 dividido por {numero} é igual a {resultado:.2f}.")
    except ValueError:
        print("\nErro: Por favor, digite um número válido.")
    except ZeroDivisionError:
        print("\nErro: Não é possível dividir por zero.")
    finally:
        print("\nTentativa concluída.")
        
        