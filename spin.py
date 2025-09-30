import minescript
from minescript import (echo, execute, getblock, player)
import sys


def spin(numb_spins: int, spin_speed: int) -> None:
    """Spins around."""
    x, y = minescript.player_orientation()
    echo(x, y)
    for i in range(int((numb_spins * 360) / spin_speed) + 1):
        minescript.player_set_orientation((x + (spin_speed * i)), y)
    minescript.player_set_orientation((x + (numb_spins * 360)), y)


if __name__ == "__main__":
    numb_spins = int(sys.argv[1])
    spin_speed = int(sys.argv[2])
    spin(numb_spins, spin_speed)