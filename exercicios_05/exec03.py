def exercicio_03():
    # Peça para o usuário digitar o ano atual e o ano de nascimento.
    # Verifique se ele já fez aniversário neste ano, considerando:
    # Se o mês atual já passou do mês de nascimento ou se o mês é o mesmo e o dia já passou.
    # Se ele fez aniversário ou não, e calcule sua idade, mas apenas se ele tiver pelo menos 18 
    # anos e seu aniversário já ocorreu neste ano.


    dia_atual = input("Digite o ano atual: ")
    mes_atual = input("Digite o ano atual: ")
    ano_atual = input("Digite o ano atual: ")

    dia_nasc = input("Digite o dia de seu nascimento: ")
    mes_nasc = input("Digite o mes de seu nascimento: ")
    ano_nasc = input("Digite o ano de seu nascimento: ")

    # Verificação se são números
    if (ano_atual.isdigit() and mes_atual.isdigit() and dia_atual.isdigit() and
        ano_nasc.isdigit() and mes_nasc.isdigit() and dia_nasc.isdigit()):
        
        ano_atual = int(ano_atual)
        mes_atual = int(mes_atual)
        dia_atual = int(dia_atual)
        ano_nasc = int(ano_nasc)
        mes_nasc = int(mes_nasc)
        dia_nasc = int(dia_nasc)

        # Verifica se já fez aniversário/ comparação do atual vs dia do aniversário
        fez_aniversario = (mes_atual > mes_nasc) or (mes_atual == mes_nasc and dia_atual >= dia_nasc)

        idade = ano_atual - ano_nasc

        if fez_aniversario and idade >= 18:
            print(f"Você já fez aniversário este ano e tem {idade} anos.")
        elif not fez_aniversario:
            print("Você ainda não fez aniversário este ano.")
        else:
            print("Você tem menos de 18 anos.")
    else:
        print("Entrada inválida. Digite apenas números.")