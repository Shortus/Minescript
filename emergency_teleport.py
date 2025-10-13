import minescript
import time
import sys

def lethal_damage(old_health: float, health: float) -> bool:
    """Checks if the last hit did enough damage to kill you the next time."""
    if (health - (old_health - health)) <= 0:
        return True
    else:
        return False


def emergency_teleport(lowest_hp: int, home_num: int, sethome_num: int) -> None:
    """TP's the player if the player is below the specified hearts."""
    old_health = 0
    while True:
        health = minescript.player_health()
        if health <= lowest_hp or lethal_damage(old_health, health):
            minescript.execute(f"/trigger sethome set {sethome_num}")
            time.sleep(0.1)
            minescript.execute(f"/trigger home set {home_num}")
            minescript.echo(f"Use '/trigger home set {sethome_num}' to go back.")
            time.sleep(120)
        old_health = health
        time.sleep(0.1)
        #minescript.echo(minescript.player_health())


if __name__ == "__main__":
    lowest_hp = int(sys.argv[1]) * 2 # Number of hearts at which the TP triggers.
    home_num = int(sys.argv[2]) # Where the player will be TP-d.
    sethome_num = int(sys.argv[3]) # Where the checkpoint will be saved.
    if lowest_hp and home_num and sethome_num:
        minescript.echo(f"At {lowest_hp / 2} hearts you will be TP-d to home {home_num}.")
        minescript.echo(f"Your checkpoint will be saved at home {sethome_num}.")
        emergency_teleport(lowest_hp, home_num, sethome_num)
    else:
        minescript.echo("emergency_teleport [lowest_hp] [home_num] [sethome_num]")