areas = {
    "stone room":
        {"description": """The room is dark and musty.
The bed you woke from stands against one wall.
There's a small grimy window opposite.
An old paint-chipped door looks like your only exit.""",
         "items": ["revolver"],
         "exits": {"east": "larger room"}
},
     "larger room":
        {"description": """This room is larger and well lit.
The lighting is even a little warm with
cream and brown wallpaper giving this room a strange
homely atmosphere.
It's even furnished with a comfy 3-piece, bookshelves,
a display cabinet and a varnished table and chairs.""",
         "items": ["cricket bat", "scrawled note", "torch"],
         "exits": {"west": "stone room", "north": "courtyard"}
         },
    "courtyard":
        {"description": """An eerily empty paved courtyard.
A crumbling fountain slouches at the center.""",
         "items": ["silver key"],
         "exits": {"south": "larger room"}}
}



