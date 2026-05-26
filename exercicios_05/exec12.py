def exercicio_12():
    # Peça para o usuário digitar dois números inteiros.
    # Informe se pelo menos um deles é maior que 100 e ambos são ímpares
    # ou se ambos são menores que 10 e divisíveis por 3.

    num1 = input("Digite o primeiro número inteiro: ")
    num2 = input("Digite o segundo número inteiro: ")
    # tira numeros negativos e verifica que são inteiros 
    if num1.lstrip("-").isdigit() and num2.lstrip("-").isdigit():
        num1 = int(num1)
        num2 = int(num2)
        # duas condições: 1 - o primeiro ou o segundo número é maior que 100  e os dois são impares 2- os dois numeros são menores que 10 e eles são divisiveis por 3. 
        cond1 = (num1 > 100 or num2 > 100) and (num1 % 2 != 0 and num2 % 2 != 0)
        cond2 = (num1 < 10 and num2 < 10) and (num1 % 3 == 0 and num2 % 3 == 0)
        # aceita qualquqer uma das duas condições 
        if cond1 or cond2:
            print("As condições foram atendidas ")
        else:
            print("As condições NÃO foram atendidas ")
    else:
        print("Entrada inválida. Digite apenas números inteiros.")
