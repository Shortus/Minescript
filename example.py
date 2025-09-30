import minescript
from minescript import (echo, execute, getblock, player)
import sys
import time
import math

def bedrock_under() -> None:
    """Continuously spawns bedrock underneath you."""
    while True:
        x, y, z = minescript.player_position()
        x, y, z = round(int(x)), round(int(y)), round(int(z))

        minescript.execute(f"setblock {x-1} {y-2} {z-1} bedrock")

def example() -> None:
    """Example from the Minescript official site."""
    # Get the player's position, rounded to the nearest integer:
    x, y, z = [round(p) for p in player().position]

    # Get the type of block directly beneath the player:
    block_type = getblock(x, y - 1, z)
    block_type = block_type.replace("minecraft:", "").split("[")[0]

    sign_text = (
        """{Text1:'{"text":"%s"}',Text2:'{"text":"at"}',Text3:'{"text":"%d %d %d"}'}""" %
        (block_type, x, y - 1, z))

    # Script argument, passed from Minecraft like "example 5"
    rotation = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    if rotation < 0 or rotation > 15:
        raise ValueError(f"Param not an integer between 0 and 15: {rotation}")

    # Create a sign then set text on it:
    execute(f"/setblock {x} {y} {z} minecraft:birch_sign[rotation={rotation}]")
    execute(f"/data merge block {x} {y} {z} {sign_text}")

    # Write a message to the chat that 
    echo(f"Created sign at {x} {y} {z} over {block_type}")

def close_entities() -> None:
    """Displays close entities from you."""
    entity_count = {}
    for entity in minescript.entities():
        entity_count[entity.name] = entity_count.get(entity.name, 0) + 1
    for entity in list(entity_count.items()):
        echo(entity)

def nig_on_bedrock() -> None:
    """Prints Nigga when on bedrock."""
    while True:
        x, y, z = [math.floor(p) for p in player().position]
        block_type = getblock(x, y - 1, z)
        if block_type == "minecraft:bedrock":
            echo("Nigga")
            minescript.execute("kill St_Midget")
            time.sleep(2)
        elif block_type == "minecraft:birch_leaves":
            break


close_entities()