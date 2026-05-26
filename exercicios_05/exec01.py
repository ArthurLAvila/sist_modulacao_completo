def exercicio_01():
    # Peça para o usuário digitar sua idade, seu salário e o número de anos de experiência.
    # Verifique e informe se ele se qualifica para uma vaga de emprego que exige:
    # Idade maior ou igual a 30 e salário maior ou igual a 4000.
    # Ou se ele tem mais de 10 anos de experiência, independente da idade e salário

    idade = input("Digite a sua idade: ")
    sal = input("Digite seu salário: ")
    xp = input("Digite quantos anos de experiência você possui: ")

    # confirma se está usando digitos numericos e passa pra inteiros
    if idade.isdigit() and sal.isdigit() and xp.isdigit():
        idade = int(idade)
        salario = int(sal)
        xp = int(xp) #xp = experiencia
        # condição de entrada para a vaga 
        if (idade >= 30 and salario >= 4000) or (xp > 10):
            print("Você se qualifica para a vaga.")
        else:
            print("Você NÃO se qualifica para a vaga.")
    else:
        print("Entrada inválida. Digite valores numéricos.")