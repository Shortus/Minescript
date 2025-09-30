import minescript
from minescript import (echo, execute, getblock, player)
import time


def proximity_hit() -> None:
    """While in proximity of an enemy the player retargets to it and hits it once, 
    waits for cooldown of weapon and hits again, 
    always returning to the original player viewing position."""

    RANGE = 2

    BAD_ENTITIES = ["Zombie",
                    "Baby Zombie", 
                    "Creeper",
                    "Baby Creeper", 
                    "Skeleton",
                    "Baby Skeleton",
                    "Spider",
                    "Necromancer",
                    "Blitz",
                    "Sheep"
                    ]

    def is_close(num: int, target: int, tolerance: int) -> bool:
            """Returns if a number is close to another number."""
            return abs(num - target) <= tolerance

    while True:
        x, y, z = [p for p in player().position]
        for entitie in minescript.entities()[1:]:
            e_x, e_y, e_z = [p for p in entitie.position]
            if is_close(e_x, x, RANGE) and is_close(e_y, y, RANGE) and is_close(e_z, z, RANGE) and entitie.name in BAD_ENTITIES:
                x_o, y_o = minescript.player_orientation()
                minescript.player_look_at(e_x, e_y + 1, e_z)
                minescript.player_press_attack(True)
                minescript.player_press_attack(False)
                time.sleep(0.3)
                minescript.player_set_orientation(x_o, y_o)
                time.sleep(1)


if __name__ == "__main__":
     proximity_hit()