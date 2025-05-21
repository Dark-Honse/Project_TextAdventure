from areas import areas
from helpers import player_view

playing = False

cmd = input("> ").strip().lower()

if cmd == "look around":
    player_view("larger room", areas)

