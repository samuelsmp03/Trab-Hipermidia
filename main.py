import mapa

directions = {"north", "south", "east", "west"}

while True:
    nome = mapa.get_current_room_name()
    print("\nVocê está em:", nome)
    print(f" ", mapa.get_description())

    exits = mapa.get_exits()
    if exits:
        print("\nSaídas:")
        for d, r in exits.items():
            print(f"  {d}: {r}")

    itens = mapa.get_items()
    if itens:
        print("\nItens:")
        for nome_item, desc in itens.items():
            print(f"  {nome_item}: {desc}")

    if mapa.is_exit():
        print("\nVocê encontrou a saída! Parabéns!")
        break

    move = input("\nDigite a direção (north, south, east, west) ou 'sair' para encerrar: \n> ").lower().strip()
    if move == "sair":
        print("Jogo encerrado.")
        break

    if move in directions:
        if not mapa.move(move):
            print("Direção inválida! Tente novamente.")
    else:
        print("Comando inválido.")