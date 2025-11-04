import mensagens
import mapa
import player

def pegarItem():
    item_nome = input("Digite o nome do item que deseja pegar: ").strip()
    if not player.pegarItem(item_nome):
        print("\nNão foi possível pegar o item :(. Verifique se ele está na sala ou se há espaço no inventário.\n")
    else:
        print(f"\nVocê pegou o item: {item_nome}!!!")
        #if (mensagens.checarEImprimirUsos() is not None):
            #print(mensagens.checarEImprimirUsos())

def soltarItem():
    item_nome = input("\nDigite o nome do item que deseja soltar: ").strip()
    if item_nome in player.getInventario():
        item_desc = player.getInventario()[item_nome]
        player.soltarItem(item_nome,item_desc)
        print(f"Você soltou o item: {item_nome}")
    else:
        print("Item não encontrado no inventário.")

def usarItem():
    item_nome = input("\nDigite o nome do item que deseja usar: ").strip()
    acao = player.usarItem(item_nome)
    if(acao != None):
        print('\n'+acao +'\n')
        
    uses = mapa.get_room_uses()
    info = uses.get(item_nome)
    changed = mapa.apply_use_effects_for_item(item_nome)
    if changed:
        print("\n" + mapa.get_description())

    return acao

def combateMonstro(monsters):
    nome_monster = monsters["name"]
    desc_monster = monsters["description"]
    mensagens.imprimirMonstro(nome_monster,desc_monster)
    mensagem_defeat = monsters["defeat_message"]
    inventario = player.getInventario()
    if inventario:
        retorno = usarItem()
        if retorno != mensagem_defeat:
            print("Você morreu ao tentar enfrentar o monstro!\n")
            print("Fim de jogo.")
            exit()
    else:
        print("Você morreu ao tentar enfrentar o monstro!\n")
        print("Fim de jogo.")
        exit()

def descreveSala():
    nome_sala = mapa.get_current_room_name()
    print(f"[{nome_sala}]\n")
    descricao = mapa.get_description()
    itens = mapa.get_items()
    uses = mapa.get_room_uses()

    mensagens.imprimirDescricaoSala(descricao)
    monsters = mapa.get_monsters()

    if monsters:
        combateMonstro(monsters)

    if itens:
        mensagens.imprimirItens(itens)

    exits = mapa.get_exits()
    if exits:
        for d, r in exits.items():
            mensagens.imprimirDestinos(d, r)
            #if (mensagens.checarEImprimirUsos() is not None):
                #print(mensagens.checarEImprimirUsos())

def imprimirInventario():
    mensagens.imprimirInventario()

def movimento():
    directions = {"north", "south", "east", "west","down","up"}
    movimento = input("\nDigite a direção (north, south, east, west, up, down): ").lower().strip()
    if movimento in directions:
        if not mapa.move(movimento):
            print("Direção inválida! Tente novamente.")
