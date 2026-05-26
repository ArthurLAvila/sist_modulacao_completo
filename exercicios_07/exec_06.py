def exercicio_06():
    """
        Este algoritmo escolhe o turno de acordo com a letra digitada pelo usuário, usando match case.
        
        Autor: Arthur Land Avila Data: 03/10/2025
    """

    # Peça ao usuário uma letra representando o turno:
    # M = Bom dia!
    # T = Boa tarde!
    # N = Boa noite!
    # Outra letra = Turno inválido.

    turno = input(f"Digite o turno correspondente (M/T/N) ").upper()

    match turno:
        case "M":
            print("Bom Dia ! ")
        case "T":
            print("Boa Tarde ! ")
        case "N":
            print("Boa Noite ! ")
        case _:
            print("Turno invalido ! ")            