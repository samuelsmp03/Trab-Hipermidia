import mapa
import IO
from mensagens import imprimirDescricaoSala, imprimirDestinos, imprimirItens, imprimirInventario

directions = {"north", "south", "east", "west"}

while True:
    nome = mapa.get_current_room_name()
    print(f"[{nome}]\n")
    imprimirDescricaoSala(mapa.get_description())

    if mapa.is_exit():
        print("\nVocê encontrou a saída! Parabéns!")
        break

    exits = mapa.get_exits()
    if exits:
        for d, r in exits.items():
            imprimirDestinos(d, r)

    itens = mapa.get_items()
    if itens:
        imprimirItens(itens)

    movimento = input("\nVocê deseja ir para uma direção(direcao), realizar uma ação relacionada a item(acao) ou sair do jogo(sair)? \n> ").lower().strip()
    
    if movimento == "sair":
        print("Jogo encerrado.")
        break

    elif movimento == 'direcao':
        IO.movimento()

    elif movimento == 'acao':
        acao_item = input("\nVocê deseja 'pegar' ou 'soltar' um item ou 'listar' seu inventário? ").lower().strip()
        if acao_item == 'pegar':
            IO.pegarItem()

        elif acao_item == 'soltar':
            IO.soltarItem()

        elif acao_item == 'listar':
            IO.imprimirInventario()

        else:
            print("Comando inválido.")
    else:
        print("Comando inválido.")