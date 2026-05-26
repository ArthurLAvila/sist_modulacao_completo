def exercicio_13():
    # Peça ao usuário para digitar o mês atual e o mês de nascimento.
    # Informe se ele completou aniversário neste ano:
    # Se o mês atual for maior que o mês de nascimento ou se o mês for o mesmo e o dia já passou.

    # input da data atual e do aniverário 
    mes_atual = input("Digite o mês atual (1-12): ")
    dia_atual = input("Digite o dia atual (1-31): ")
    mes_nasc = input("Digite o mês de nascimento (1-12): ")
    dia_nasc = input("Digite o dia de nascimento (1-31): ")

    #tratamento das variaveis 
    if mes_atual.isdigit() and dia_atual.isdigit() and mes_nasc.isdigit() and dia_nasc.isdigit():
        mes_atual = int(mes_atual)
        dia_atual = int(dia_atual)
        mes_nasc = int(mes_nasc)
        dia_nasc = int(dia_nasc)
        # teste se ja fez aniverário se já passou o mes do aniversaior e se for o mes do aniversário ele checa o dia 
        if (mes_atual > mes_nasc) or (mes_atual == mes_nasc and dia_atual >= dia_nasc):
            print("Você já fez aniversário neste ano ")
        else:
            print("Você ainda não fez aniversário neste ano ")
    else:
        print("Entrada inválida. Digite apenas números inteiros.")