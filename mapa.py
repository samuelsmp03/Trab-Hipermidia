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
    desc = room.get("description")
    if isinstance(desc, str):
        return desc
    else:
        return ""

def get_exits():
    possible_dirs = {"north", "south", "east", "west", "up", "down"}
    room = get_current_room()
    exits = {}
    for d in possible_dirs:
        if d in room:
            exits[d] = room[d]
    return exits

def get_monsters():
    room = get_current_room()

    monster_obj = room.get("monster") 
    
    if isinstance(monster_obj, dict):
        return monster_obj 
    else:
        return None
    
def add_monster(monster_name: str, monster_info: dict, defeat_item: str, defeat_text: str):
    room = get_current_room()
    new_monster = {
        "name": monster_name,
        "info": monster_info,
        "defeat_item": defeat_item,
        "defeat_text": defeat_text
    }
    room["monster"] = new_monster
    print(f"Monstro '{monster_name}' adicionado à sala.")
    return True

def remove_monster(monster_name: str):
    room = get_current_room()
    monster_obj = room.get("monster")

    if isinstance(monster_obj, dict) and monster_obj.get("name") == monster_name:
        
        room["monster"] = None 
        return True
    else:
        return False

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

_opposite = {"north": "south", "south": "north", "east": "west", "west": "east", "up": "down", "down": "up"}

def apply_use_effects_for_item(item: str) -> bool:
    room_name = get_current_room_name()
    uses = get_room_uses()
    info = uses.get(item)
    
    if not isinstance(info, dict):
        return False

    key = (room_name, item)
    if key in _opens_executed:
        return False

    changed = False
    room = get_current_room()

    adds = info.get("adds_exit") or {}
    removes = info.get("removes_exit") or {}

    if isinstance(adds, dict):
        for d, dest in adds.items():
            if d not in room:
                room[d] = dest
                changed = True

    if isinstance(removes, dict):
        for d, expected_dest in removes.items():
            if d in room:
                actual_dest = room.get(d)
                if expected_dest in (None, "") or expected_dest == actual_dest:
                    del room[d]
                    changed = True
                    _rooms = globals().get("_rooms")
                    if isinstance(_rooms, dict) and actual_dest in _rooms:
                        rev = _opposite.get(d)
                        if rev and _rooms[actual_dest].get(rev) == room_name:
                            del _rooms[actual_dest][rev]

    new_desc = info.get("newDesc")
    if (new_desc != room.get("description")):
        room["description"] = new_desc
        changed = True

    if changed:
        _opens_executed.add((room_name, item))

    return changed