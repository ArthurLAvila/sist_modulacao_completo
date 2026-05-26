def exercicio_04():
    # Peça ao usuário para digitar a temperatura em graus Celsius e se ele está usando roupas 
    # leves s ou n.
    # Informe se ele pode sair sem casaco, considerando:
    # Se a temperatura é superior a 20°C ou se ele está usando roupas leves.
    # Ou se a temperatura é inferior a 10°C, onde ele deve estar usando casaco


    temp = float(input("Digite a temperatura em celsius: "))
    roupa = input("Digite se você está usando roupas leves? s/n: ").lower()

    if temp.istrip("-").isdigit():
        temp = int(temp)
        # testa temperatuia alta e roupa leve
        if temp > 20 or roupa == "s":
            print("Você pode sair sem casaco hoje ! ")    
        # temperatura amena/ fria -> deve se agasalhar !
        elif(temp <10):
            print("A temperatura está baixa, você deve usar casaco.")
        # temperatura entre 10 e 20 
        else:
            print("Pode ser melhor levar um casaco, dependendo da sua resistência.")
    else:
        print("Entrada inválida. Digite apenas números para a temperatura.")