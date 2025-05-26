areas = {
    "stone room":
        {"description": """The room is dark and musty.
The bed you woke from stands against one wall.
There's a heavy looking floor safe under a small grimy window opposite.
An old paint-chipped door to the east looks like your only exit.""",

         "exits": {"east": "larger room"},

         "searches": {
             "bed": {
                 "text_found": "You find a brass key under the pillow!",
                 "item": "brass key",
                 "searched": False,
                 "text_searched": "Nothing else. Just a nasty dark stain across the sheet."},
             "safe": {
                 "locked": True,
                 "text_locked": "Doesn't budge, it's locked.",
                 "text_unlocked": "you unlock the safe!",
                 "text_found": "You find a revolver!",
                 "item": "revolver",
                 "searched": False,
                 "text_searched": "There's nothing else in here."
             }
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
             "bookshelf": {
                 "text_found": "Just some boring, dusty books.",
                 "item": "",
                 "searched": False,
                 "text_searched": "Still just dust and uninteresting books."},
             "display cabinet": {
                 "locked": True,
                 "required": "brass key",
                 "text_locked": "The display lid is locked closed.",
                 "text_unlocked": "You use the brass key to unlock the cabinet.",
                 "text_found": "You find a signed baseball bat!",
                 "item": "signed baseball bat",
                 "searched": False,
                 "text_searched": "Nothing else in here."},
             "table": {
                 "text_found": "You find a scrawled note.",
                 "item": "scrawled note",
                 "searched": False,
                 "text_searched": "Nothing else of interest."},
         }
},
    "courtyard":
        {"description": """An eerily empty paved courtyard.
A crumbling fountain slouches at the center.""",

         "exits": {"south": "larger room"},

         "searches": {
             "fountain": {
                 "text_found": "You find a small coin.",
                 "item": "small coin",
                 "searched": False,
                 "text_searched": "Nothing else in here."
             }
         }
         }
}



