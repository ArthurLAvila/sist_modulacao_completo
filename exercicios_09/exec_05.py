def exercicio_05():
    """
        Este algoritmo simula opções de pagamento de uma compra.
        O usuário informa o valor da compra e escolhe entre as opções:
        1 - À vista (10% de desconto)
        2 - Parcelado em 2x (sem juros)
        3 - Parcelado em 3x ou mais (com 10% de juros)
        O programa valida as escolhas, faz os cálculos e permite várias simulações
        até o usuário optar por sair.

        Autor: Arthur Land Avila
        Data: 13/10/2025
    """

    # Crie um programa que simule opções de pagamento para uma compra.
    # O usuário informa o valor da compra.
    # Exiba opções de pagamento para escolher:
    # 1 - À vista desconto de 10%
    # 2 - Parcelado em 2x sem juros
    # 3 - Parcelado em 3x ou mais juros de 10%
    # 4 - Sair
    # Valide a escolha do usuário e o número de parcelas, quando necessário.
    # Calcule e mostre o valor final a ser pago, parcelamento e juros/descontos aplicados.
    # Use controle de fluxo para permitir que o usuário faça várias simulações até escolher sair.


    print("=== Simulador de Opções de Pagamento ===\n")

    while True:
        valor = input("Digite o valor da compra (ou 'sair' para encerrar): ")

        # Permite sair direto
        if valor.lower() == "sair":
            print("\nEncerrando o simulador. ")
            break

        # Valida valor numérico
        if not valor.replace('.', '', 1).isdigit():
            print("Valor inválido! Digite um número positivo.\n")
            continue

        valor = float(valor)

        if valor <= 0:
            print("O valor da compra deve ser maior que zero.\n")
            continue

        print("\n=== Opções de Pagamento ===")
        print("1 - À vista (10% de desconto)")
        print("2 - Parcelado em 2x (sem juros)")
        print("3 - Parcelado em 3x ou mais (10% de juros)")
        print("4 - Sair")

        opcao = input("Escolha a opção de pagamento: ")

        match opcao:
            case "1":
                desconto = valor * 0.10
                total = valor - desconto
                print(f"\nPagamento à vista com 10% de desconto.")
                print(f"Valor original: R${valor:.2f}")
                print(f"Desconto: R${desconto:.2f}")
                print(f"Valor final a pagar: R${total:.2f}\n")

            case "2":
                parcela = valor / 2
                print(f"\nPagamento parcelado em 2x sem juros.")
                print(f"2 parcelas de R${parcela:.2f}")
                print(f"Valor total a pagar: R${valor:.2f}\n")

            case "3":
                parcelas = input("Digite o número de parcelas (mínimo 3): ")
                if not parcelas.isdigit():
                    print("Entrada inválida! Digite um número inteiro.\n")
                    continue

                parcelas = int(parcelas)
                if parcelas < 3:
                    print("Número de parcelas inválido! Deve ser 3 ou mais.\n")
                    continue

                total = valor * 1.10  # 10% de juros
                valor_parcela = total / parcelas
                print(f"\nPagamento parcelado em {parcelas}x com 10% de juros.")
                print(f"Valor total a pagar: R${total:.2f}")
                print(f"Cada parcela: R${valor_parcela:.2f}\n")

            case "4":
                print("\nEncerrando o simulador. ")
                break

            case _:
                print("\nOpção inválida! Tente novamente.\n")
