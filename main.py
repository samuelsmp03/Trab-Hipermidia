import mapa
import mensagens

directions = {"north", "south", "east", "west"}

while True:
    nome = mapa.get_current_room_name()
    print(f"[{nome}]\n")
    mensagens.imprimirDescricaoSala(mapa.get_description())

    exits = mapa.get_exits()
    if exits:
        for d, r in exits.items():
            mensagens.imprimirDestinos(d, r)

    itens = mapa.get_items()
    if itens:
        mensagens.imprimirItens(itens)

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