import minescript
from minescript import (echo, execute, getblock, player)


def close_entities() -> None:
    """Displays close entities from you."""
    entity_count = {}
    for entity in minescript.entities():
        entity_count[entity.name] = entity_count.get(entity.name, 0) + 1
    for entity in list(entity_count.items()):
        echo(entity)


if __name__ == "__main__":
    close_entities()