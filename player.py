import mapa
tam_inv_max = mapa.get_inventory_space
inventario = {}

def pegarItem(nome_item: str) -> bool:
    itens = mapa.get_items()
    if nome_item in itens and len(inventario) < tam_inv_max():
        inventario[nome_item] = itens[nome_item]
        del itens[nome_item]
        mapa.set_items(itens)
        return True
    return False

def getInventario() -> dict:
    return inventario

def getTamInv() -> int:
    return len(inventario)

def soltarItem(nome_item: str, descricao: str) -> bool:
    if nome_item in inventario:
        itens = mapa.get_items()
        itens[nome_item] = descricao
        mapa.set_items(itens)
        del inventario[nome_item]
        return True
    return False

def usarItem(nome_item: str):
    monster = mapa.get_monsters()
    if nome_item in inventario:
        mapa_uses = mapa.get_room_uses()
        if nome_item in mapa_uses:
            acao = mapa_uses[nome_item].get("description")
            del inventario[nome_item]
            return acao
        if monster:
            defeat_item = monster.get("defeat_item")

            if nome_item == defeat_item:
                nome_monster = monster.get("name")
                defeat_text = monster.get("defeat_message")
                mapa.remove_monster(nome_monster)
                del inventario[defeat_item]
                return defeat_text
    return None
