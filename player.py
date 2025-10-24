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