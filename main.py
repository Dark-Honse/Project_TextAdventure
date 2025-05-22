from areas import areas
from helpers import player_view

playing = False

player_location = "stone room"

cmd = input("> ").strip().lower()

if cmd == "look around":
    player_view(player_location, areas)

