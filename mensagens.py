import random
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
    num_random = random.choice([1, 2, 3])
    if num_random == 1:
        print(f"Um(a) explêndido: {descricao}")
    elif num_random == 2:
        print(f"Você observa: {descricao}")
    else:
        print(f"Um(a) sofisticado: {descricao}")
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

def verificaPalavraFeminina(palavra:str) -> bool:
    if palavra.endswith("a") or palavra.endswith("ã") or palavra.endswith("dade") or palavra.endswith("ção"):
        return "a "
    return
    
#Imprimir itens com variações
def imprimirItens(itens:dict):
    if not itens:
        return
    for nome_item, desc in itens.items():
        nome_item = nome_item
        desc = desc.capitalize()
        num_random = random.choice([1, 2, 3])
        if num_random == 1:
            print(f"Você observa um{verificaPalavraFeminina(nome_item)}[{nome_item}], ao se aproximar você nota mais detalhes:{desc}")
        elif num_random == 2:
            print(f"Um{verificaPalavraFeminina(nome_item)}[{nome_item}] está aqui. Chegando mais perto, você nota alguns detalhes: {desc}")
        else:
            print(f"Há um{verificaPalavraFeminina(nome_item)}[{nome_item}] neste local. Vendo com calma, você percebe que é um(a): {desc}")
    return

def imprimirInventario():
    inventario = getInventario()
    tam_inv = getTamInv()
    if tam_inv == 0:
        print("Seu inventário está vazio.")
        return
    print("Itens no seu inventário:")
    print(f"\nSeu inventário possui {tam_inv} itens")
    for nome_item, desc in inventario.items():
        nome_item = nome_item
        desc = desc.capitalize()
        print(f"- [{nome_item}]: {desc}")
    return