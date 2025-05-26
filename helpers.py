import random

def view(location, areas):
    """print the player's view."""
    print(areas[location]["description"])

def move(location, direction, areas):
    exits = areas[location]["exits"]
    if direction in exits:
     new_location = exits[direction]
     print(f"You move {direction} to {new_location}.")
     return new_location
    else:
        print("You can't go that way.")
        return location



def search(location, target, areas, inventory):
    searches = areas[location].get("searches", {})
    if target not in searches:
        print("You don't see that in here.")
        return ""
    obj = searches[target]
    if obj.get("searched"):
        print(obj.get("text_searched"))
        return ""
    if obj.get("locked"):
        key_needed = obj.get("required")
        if key_needed in inventory:
            obj["locked"] = False
            print(obj.get("text_unlocked"))
        else:
            print(obj.get("text_locked"))
            return ""
    print(obj.get("text_found"))
    item = obj.get("item", "")
    obj["searched"] = True
    return item

def getsafecode():
    numbers = list("0123456789")
    random.shuffle(numbers)
    safe_code = ""
    for i in range(4):
        safe_code += str(numbers[i])
    return safe_code
