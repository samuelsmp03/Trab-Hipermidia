import mensagens
import mapa
import player

def pegarItem():
    item_nome = input("Digite o nome do item que deseja pegar: ").strip()
    if not player.pegarItem(item_nome):
        print("\nNão foi possível pegar o item :(. Verifique se ele está na sala ou se há espaço no inventário.\n")
    else:
        print(f"\nVocê pegou o item: {item_nome}!!!")

def soltarItem():
    item_nome = input("\nDigite o nome do item que deseja soltar: ").strip()
    if item_nome in player.getInventario():
        item_desc = player.getInventario()[item_nome]
        player.soltarItem(item_nome,item_desc)
        print(f"Você soltou o item: {item_nome}")
    else:
        print("Item não encontrado no inventário.")

def imprimirInventario():
    mensagens.imprimirInventario()

def movimento():
    directions = {"north", "south", "east", "west"}
    movimento = input("\nDigite a direção (north, south, east, west): ").lower().strip()
    if movimento in directions:
        if not mapa.move(movimento):
            print("Direção inválida! Tente novamente.")