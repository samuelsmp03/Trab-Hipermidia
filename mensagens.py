import random
import mapa
from player import getInventario, getTamInv
#Traduzir direções para português
def retornaDirecaoPT(direcao:str):
    if direcao == "north":
        return "norte"
    elif direcao == "south":
        return "sul"
    elif direcao == "east":
        return "leste"
    elif direcao == "west":
        return "oeste"
    elif direcao == "up":
        return "alto"
    elif direcao == "down":
        return "baixo"
    return

#Imprimir destinos com variações   
def imprimirDestinos(direcao:str, destino:str):
    direcao = retornaDirecaoPT(direcao)
    num_random = random.choice([1, 2, 3])
    if num_random == 1:
        print(f"Você avista {determinaArtigoEmFrases(destino)}{destino} ao {direcao}.\n")
    elif num_random == 2:
        print(f"Há um caminho para {determinaArtigoEmFrases(destino)}{destino} seguindo pelo {direcao}.\n")
    else:
        print(f"Seguindo para o {direcao}, você encontrará {determinaArtigoEmFrases(destino)}{destino}.\n")
    return

#Imprimir descrição da sala com variações
def imprimirDescricaoSala(descricao:str):
    print(f"{descricao}\n")
    return

def determinaArtigoEmFrases(frase:str) -> bool:
    palavras = frase.split()
    if not palavras:
        primeira_palavra = frase
    else:
        primeira_palavra = palavras[0]
    if primeira_palavra.endswith("a") or primeira_palavra.endswith("ã") or primeira_palavra.endswith("dade") or primeira_palavra.endswith("ção"):
        return "a "
    return "o "

def verificaPalavraFeminina(palavra: str) -> str:
    if not palavra:
        return ""
    p = palavra.lower()
    if p.endswith(("a", "ã")) or p.endswith("dade") or p.endswith("ção"):
        return "a "
    return " "
    
#Imprimir itens com variações
def imprimirItens(itens:dict):
    if not itens:
        return
    for nome_item, desc in itens.items():
        nome_item = nome_item
        #desc = desc.capitalize()
        num_random = random.choice([1, 2, 3])
        artigo = verificaPalavraFeminina(nome_item)
        if num_random == 1:
            print(f"Você observa um{artigo}[{nome_item}], ao se aproximar, você nota mais detalhes: {desc}")
        elif num_random == 2:
            print(f"Um{artigo}[{nome_item}] está aqui. Chegando mais perto, você nota alguns detalhes: {desc}")
        else:
            print(f"Há um{artigo}[{nome_item}] neste local. Vendo com calma, {desc}")
    return

def imprimirInventario():
    inventario = getInventario()
    tam_inv = getTamInv()
    if tam_inv == 0:
        print("Seu inventário está vazio.")
        return
    print("Itens no seu inventário:")
    print(f"\nSeu inventário possui {tam_inv} itens e pode armazenar mais {mapa.get_inventory_space() - tam_inv} itens.\n")
    for nome_item, desc in inventario.items():
        nome_item = nome_item
        desc = desc.capitalize()
        print(f"- [{nome_item}]: {desc}")
    return

def imprimirMonstro(monstro: str,desc: str):
    num_random = random.choice([1, 2, 3])
    if num_random == 1:
        print(f"Cuidado! Há um monstro chamado [{monstro}] aqui!\n")
    elif num_random == 2:
        print(f"Um perigoso monstro conhecido como [{monstro}] está presente nesta sala!\n")
    else:
        print(f"Atenção! Você se depara com um monstro denominado [{monstro}]!\n")

    print(desc + "\n")
    return
'''
def checarEImprimirUsos():
    uses = mapa.get_room_uses()
    inv = getInventario()
    if not uses:
        return
    for item, info in uses.items():
        if item in inv:
            texto = info.get("description")
            return(texto)
'''