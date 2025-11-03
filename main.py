import mapa
import IO
from mensagens import imprimirDescricaoSala, imprimirDestinos, imprimirItens

directions = {"north", "south", "east", "west","up","down"}

while True:

    IO.descreveSala() # Descreve a sala atual

    if mapa.is_exit():
        print("\nVocê encontrou a saída! Parabéns!")
        break
    
    movimento = input("\nVocê deseja ir para uma direção(direcao), realizar uma ação relacionada a item(acao) ou sair do jogo(sair)? \n> ").lower().strip()
    
    if movimento == "sair":
        print("Jogo encerrado.")
        break

    elif movimento == 'direcao':
        IO.movimento()

    elif movimento == 'acao':
        acao_item = input("\nVocê deseja 'pegar','soltar' ou 'usar' um item ou 'listar' seu inventário? ").lower().strip()
        if acao_item == 'pegar':
            IO.pegarItem()

        elif acao_item == 'soltar':
            IO.soltarItem()

        elif acao_item == 'listar':
            IO.imprimirInventario()

        elif acao_item == 'usar':
            IO.usarItem()
        else:
            print("Comando inválido.")
    else:
        print("Comando inválido.")
