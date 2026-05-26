def exercicio_10():
    # Peça ao usuário para digitar o valor de uma compra e o tipo de pagamento à vista ou 
    # parcelado.
    # Se a compra for superior a R$500,00 e o pagamento for parcelado, aplique um desconto 
    # de 10%. Caso contrário, aplique um desconto de 5% se o pagamento for à vista. Informe o 
    # valor final após o desconto

    valor = input("Digite o valor de uma compra: ")
    pagamento = input("Digite o tipo de pagamento (à vista/parcelado): ")

    if valor.replace(".", "", 1).isdigit():  # aceita números com decimal
        valor = float(valor)
        # se for maior que 500 o valor aplica um desconto de 10 por cento 
        if valor > 500 and pagamento == "parcelado":
            desconto = valor * 0.10
            valor_final = valor - desconto
            print(f"Desconto de 10% aplicado. Valor final: R${valor_final:.2f}")
        # se for ainda maior que 500 e for a vista aplica um desconto de só 5 por cento
        elif pagamento == "à vista":
            desconto = valor * 0.05
            valor_final = valor - desconto
            print(f"Desconto de 5% aplicado. Valor final: R${valor_final:.2f}")
        # se não for acima de 500 reais ele não da desconto
        else:
            print(f"Sem desconto. Valor final: R${valor:.2f}")
    else:
        print("Valor inválido. Digite apenas números.")