import json
with open("file.json", "r") as f:
   data = json.load(f)


current_room = data["main"]
exit_room = data["exit"]


while True:
   room = data[current_room]
   print("\nVocê está em:", current_room)


   for key in room.keys():
       if key == "description":
           print(room[key])
           continue
       print(key +":"+room[key])


   if current_room == exit_room:
       print("\nVocê encontrou a saída! Parabéns!")
       break


   move = input("Digite a direção (north, south, east, west) ou 'sair' para encerrar: \n>").lower().strip()
   if move == "sair":
       print("Jogo encerrado.")
       break


   if move in room:
       current_room = room[move]
   else:
       print("Direção inválida! Tente novamente.")