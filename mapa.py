import leitorJson

_current = leitorJson.start_room
_exit = leitorJson.exit_room
_inventory_space = leitorJson.inventory_space

def get_inventory_space():
    return _inventory_space

def get_current_room_name():
    return _current

def get_current_room():
    return leitorJson.rooms[_current]

def get_description():
    room = get_current_room()
    return room.get("description", "")

def get_exits():
    possible_dirs = {"north", "south", "east", "west", "up", "down"}
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

_opens_executed = set()

def apply_use_effects_for_item(item: str) -> bool:
    room_name = get_current_room_name()
    uses = get_room_uses()
    info = uses.get(item)

    key = (room_name, item)
    if key in _opens_executed:
        return False

    changed = False
    room = get_current_room()

    adds = info.get("adds_exit")
    if adds is not None:
        for d, dest in adds.items():
            if d not in room:
                room[d] = dest
                changed = True
            
        new_desc = info.get("newDesc")
        if new_desc is not None:
            room["description"] = new_desc

        if changed:
            _opens_executed.add((room_name, item))

        return changed
    return False
