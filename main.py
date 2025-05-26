from helpers import view, move, search, getsafecode
from areas import areas

safe_code = getsafecode()

playing = False
safe_locked = True

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

    elif cmd in ["quit", "exit", "quit game"]:
        playing = False
        print("Thanks for playing! Goodbye!")

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
        target = cmd.split(maxsplit=1)[1]
        found_item = search(player_location, target, areas, inventory)
        if found_item and found_item not in inventory:
            inventory.append(found_item)

    elif cmd == "sleep":
        print("You go to sleep")
        playing = False
        print("The end.")

    elif cmd in ["read note", "view note", "examine note", "inspect note"]:
        if "scrawled note" in inventory:
            print(f"""It looks hastily written. It reads:
Do NOT let him out until we get the next shipment.
He's unstable at the minute. Stay safe.
P.S. The safe code is {safe_code}
-P""")
        else:
            print("What note?")

    elif cmd in ["examine safe", "unlock safe", "use safe code"]:
        if player_location == "stone room":
            while True:
                print("Enter code: ")
                attempt = input("> ")
                if attempt == safe_code:
                    areas["stone room"]["searches"]["safe"]["locked"] = False
                    print("The lock clicks..")
                    break
                elif attempt in ["leave", "stop", "exit"]:
                    print("You turn away from the safe.")
                    break
                else:
                    print("Nothing happens.")
        else:
            print("There's no safe here.")

    else:
        print("I don't understand that.")


