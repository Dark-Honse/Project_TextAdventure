

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



def search(location, target, areas):
    searches = areas[location].get("searches", {})
    if target in searches:
        result = list(searches[target].items())[0]
        message, item = result
        print(message)
        return item
    else:
        print("You don't find anything.")
        return ""

