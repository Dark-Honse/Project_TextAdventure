

def player_view(location: str, areas: dict) -> None:
    """print the player's view."""

    print("\n" + areas[location]["description"])