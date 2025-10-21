import mapa
from mensagens import imprimirDescricaoSala, imprimirDestinos, imprimirItens,imprimirInventario
from player import pegarItem, soltarItem,getInventario, getTamInv

directions = {"north", "south", "east", "west"}

while True:
    nome = mapa.get_current_room_name()
    print(f"[{nome}]\n")
    imprimirDescricaoSala(mapa.get_description())

    exits = mapa.get_exits()
    if exits:
        for d, r in exits.items():
            imprimirDestinos(d, r)

    itens = mapa.get_items()
    if itens:
        imprimirItens(itens)

    if mapa.is_exit():
        print("\nVocê encontrou a saída! Parabéns!")
        break

    movimento = input("\nVocê deseja ir para uma direção(direcao), realizar uma ação relacionada a item(acao) ou sair do jogo(sair)? \n> ").lower().strip()
    if movimento == "sair":
        print("Jogo encerrado.")
        break
    elif movimento == 'direcao':
        movimento = input("\nDigite a direção (north, south, east, west): ").lower().strip()
        if movimento in directions:
            if not mapa.move(movimento):
                print("Direção inválida! Tente novamente.")

    elif movimento == 'acao':
        acao_item = input("\nVocê deseja 'pegar' ou 'soltar' um item ou 'listar' seu inventário? ").lower().strip()
        if acao_item == 'pegar':
            item_nome = input("Digite o nome do item que deseja pegar: ").strip()
            if not pegarItem(item_nome):
                print("\nNão foi possível pegar o item :(. Verifique se ele está na sala ou se há espaço no inventário.\n")
            else:
                print(f"\nVocê pegou o item: {item_nome}!!!")

        elif acao_item == 'soltar':
            item_nome = input("\nDigite o nome do item que deseja soltar: ").strip()
            if item_nome in getInventario():
                item_desc = getInventario()[item_nome]
                soltarItem(item_nome,item_desc)
                print(f"Você soltou o item: {item_nome}")
            else:
                print("Item não encontrado no inventário.")
                continue

        elif acao_item == 'listar':
            imprimirInventario()

        else:
            print("Comando inválido.")
    else:
        print("Comando inválido.")