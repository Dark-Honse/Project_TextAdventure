from helpers import view
from areas import areas

playing = False

player_location = ""

print("Welcome! Ready to play?")
cmd = input("> ").strip().lower()

if cmd in ["yes", "y", "yep"]:
    playing = True
    player_location = "stone room"
else:
    print("Maybe next time. Goodbye!")

while playing:
    print("You wake up in a dark room.")
    cmd = input("> ").strip().lower()
    if cmd in ["look", "look around", "view"]:
        view(player_location, areas)
