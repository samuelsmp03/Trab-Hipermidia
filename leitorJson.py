import json
with open("file.json", "r", encoding = "utf-8") as f:
   data = json.load(f)

start_room = data.get("main")
exit_room = data.get("exit")
inventory_space = data.get("max_itens", None)