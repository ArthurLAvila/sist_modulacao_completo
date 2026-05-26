def exercicio_05():    
    # Peça para o usuário digitar a nota de uma prova de 0 a 10 e o número de faltas.
    # Informe se o aluno está aprovado, reprovado ou em recuperação, considerando:
    # Aprovado se a nota for maior ou igual a 7 e faltas menores ou iguais a 3.
    # Em recuperação se a nota for maior ou igual a 5, mas menor que 7, ou se a quantidade de 
    # faltas for maior que 3, mas menor ou igual a 5.
    # Reprovado se a nota for menor que 5 e as faltas forem maiores que 5.


    # Entrada de dados
    nota = input("Digite a nota do aluno (0 a 10): ")
    faltas = input("Digite o número de faltas: ")
    #tira o ponto da nota em decimal e passa pra inteiro positivo, confirma se faltas é digito 
    if nota.replace(".", "", 1).isdigit() and faltas.isdigit():
        nota = float(nota)
        faltas = int(faltas)
    # nota entre 7 e 10 e faltas menor igual a 3 
        if nota >= 7 and faltas <= 3:
            print("Aluno aprovado ")
        #nota entre 5 e 6.9 e faltas meior que 3 e menor igual a 5     
        elif (5 <= nota < 7) or (3 < faltas <= 5):
            print("Aluno em recuperação ")
            #nota a baixo de 5 e faltas maior que 5
        elif nota < 5 and faltas > 5:
            print("Aluno reprovado ")
        else:
            print("A situação do aluno não se encaixa nas regras definidas.")
    else:
        print("Entrada inválida. Digite apenas números válidos.")
