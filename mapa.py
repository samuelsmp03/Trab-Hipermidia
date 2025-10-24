import leitorJson

_raw = leitorJson.data
_rooms = {}
for name, value in _raw.items():
    if name in {"main", "exit", "max_itens", "use"}:
        continue
    _rooms[name] = value

_current = leitorJson.start_room
_exit = leitorJson.exit_room
_inventory_space = leitorJson.inventory_space

def get_inventory_space():
    return _inventory_space

def get_current_room_name():
    return _current

def get_current_room():
    return _rooms[_current]

def get_description():
    room = get_current_room()
    return room.get("description", "")

def get_exits():
    possible_dirs = {"north", "south", "east", "west"}
    room = get_current_room()
    exits = {}
    for d in possible_dirs:
        if d in room:
            exits[d] = room[d]
    return exits

def get_items():
    room = get_current_room()
    itens = room.get("itens")
    if isinstance(itens, dict):
        return dict(itens)
    else:
        return {}

def set_items(itens: dict):
    room = get_current_room()
    room["itens"] = itens

def is_exit():
    if _current == _exit:
        return True
    return False

def move(direction: str) -> bool:
    global _current
    room = get_current_room()
    if direction in room:
        _current = room[direction]
        return True
    return False

def get_room_uses():
    room = get_current_room()
    uses = {}
    for entry in room.get("use", []):
        item = entry.get("item")
        uses[item] = entry
    return uses