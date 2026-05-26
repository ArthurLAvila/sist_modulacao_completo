def exercicio_08():
    # Peça para o usuário digitar o horário atual em formato de 24h.
    # Informe se ele está no intervalo do período da manhã das 6h às 12h, período da tarde das 
    # 12h às 18h, ou período da noite das 18h às 6h.

    #hora em format (24)
    hora = input("Digite o horario atual(24hr): ")
    if hora.isdigit():
        hora = int(hora)
    # entre 6 e 12 
    if hora >= 6 and hora <= 12:
        print("Você está no periodo da tarde!")
    #entre 12 e 18 
    elif(hora > 12 and hora <= 18):
        print("Você está no periodo da noite!")    
    else:
        print("Digite um valor de hora valido")   