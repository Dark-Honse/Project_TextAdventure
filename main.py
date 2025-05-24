from helpers import view
from  helpers import move
from helpers import search
from areas import areas

playing = False

player_location = ""
inventory = []

print("Welcome! Ready to play?")
cmd = input("> ").strip().lower()

if cmd in ["yes", "y", "yep", "play"]:
    playing = True
    player_location = "stone room"
    print("You wake up in a dark room.")
else:
    print("Maybe next time. Goodbye!")

while playing:
    cmd = input("> ").strip().lower()
    if cmd == "help":
        print("""List of commands (not extensive):
look around
go [north, east, south, west]
pick up/take [something]
quit/exit - to leave the game""")

    elif cmd in ["look", "look around", "view"]:
        view(player_location, areas)

    elif cmd in ["inventory", "check inventory", "view inventory"]:
        if len(inventory) == 0:
            print("""You have nothing.
Broke ass.""")
        else:
            print("You have:\n" + "\n".join(inventory))

    elif cmd.startswith("go "):
        direction = cmd.split()[1]
        player_location = move(player_location, direction,areas)

    elif cmd.startswith("search "):
        target = cmd.split()[1]
        found_item = search(player_location, target, areas)
        if found_item:
            inventory.append(found_item)



