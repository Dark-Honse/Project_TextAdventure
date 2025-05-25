areas = {
    "stone room":
        {"description": """The room is dark and musty.
The bed you woke from stands against one wall.
There's a small grimy window opposite.
An old paint-chipped door to the east looks like your only exit.""",

         "exits": {"east": "larger room"},

         "searches": {
             "bed": {"You find a key!": "key"},
             "window": {"Just dust and grime.": ""},
             "safe": {""}
         }
},
     "larger room":
        {"description": """This room is larger and well lit.
The lighting is even a little warm with
cream and brown wallpaper giving this room a strange
homely atmosphere.
It's even furnished with a comfy 3-piece, bookshelves,
a display cabinet and a varnished table and chairs.
To the north a door leads outside.""",

         "exits": {"west": "stone room", "north": "courtyard"},

         "searches": {
             "bookshelf": {"Just some boring, dusty books.": ""},
             "display cabinet": {"You find a knife!": "knife"},
             "table": {"You find a scrawled note.": "scrawled note"},
         }
},
    "courtyard":
        {"description": """An eerily empty paved courtyard.
A crumbling fountain slouches at the center.""",

         "exits": {"south": "larger room"},

         "searches": {
             "fountain": {"You find a key": "old key"}
         }
         }
}



