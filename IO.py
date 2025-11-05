import mensagens
import mapa
import player
import importlib
import sys

jogando = True

def restart_prompt() -> bool:
    while True:
        resp = input("Gostaria de tentar novamente? (sim/nao)\n> ").strip().lower()
        if (resp == "sim"):
            import leitorJson, mapa, player, mensagens
            importlib.reload(leitorJson)
            importlib.reload(mapa)
            importlib.reload(player)
            importlib.reload(mensagens)
            global jogando
            jogando = True
            print("\nJogo reiniciado.\n")
            return True
        elif (resp == "nao"):
            print("Jogo encerrado.")
            sys.exit(0)
        print("Resposta inválida. Digite 'sim' ou 'nao'.")

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
        desc = mapa.get_description() or ""
        if desc:
            print("\n" + desc)
            
    if not isinstance(info, dict):
        return acao
            
    gives = info.get("gives_item")
    if isinstance(gives, dict):
        new_name = gives.get("name")
        new_desc = gives.get("description", "")
        if new_name:
            added = False
            add_fn = getattr(player, "add_item", None) or getattr(player, "addItem", None)
            if callable(add_fn):
                added = add_fn(new_name, new_desc)
            else:
                inv = player.getInventario()
                max_space = mapa.get_inventory_space()
                if not (len(inv) >= max_space):
                    inv[new_name] = new_desc
                    added = True

            if added:
                print(f"\nVocê recebeu: {new_name}!")

    return acao

def combateMonstro(monsters):
    nome_monster = monsters["name"]
    desc_monster = monsters["description"]
    mensagens.imprimirMonstro(nome_monster,desc_monster)
    mensagem_defeat = monsters["defeat_message"]
    inventario = player.getInventario()
    if (mensagem_defeat == ""):
        pass
    else:
        if inventario:
            retorno = usarItem()
            if retorno != mensagem_defeat:
                print("Você morreu ao tentar enfrentar o monstro!\n")
                print("Fim de jogo.")
                restart_prompt()
                return
        else:
            print("Você morreu ao tentar enfrentar o monstro!\n")
            print("Fim de jogo.")
            restart_prompt()
            return

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