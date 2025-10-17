import leitorJson

_raw = leitorJson.data
_rooms = {}
for name, value in _raw.items():
    if name in {"main", "exit", "max_itens"}:
        continue
    _rooms[name] = value

_current = leitorJson.start_room
_exit = leitorJson.exit_room
_inventory_space = leitorJson.inventory_space

def get_current_room_name():
    return _current

def get_current_room():
    return _rooms[_current]

def get_description():
    return get_current_room().get("description", "")

def get_exits():
    possible_dirs = {"north", "south", "east", "west"}
    room = get_current_room()
    return {d: room[d] for d in possible_dirs if d in room}

def get_items():
    itens = get_current_room().get("itens")
    return itens if isinstance(itens, dict) else {}

def is_exit():
    return _current == _exit

def move(direction: str) -> bool:
    global _current
    room = get_current_room()
    if direction in room:
        _current = room[direction]
        return True
    return False