import minescript
import sys
import time
 
def format_block_name(block_name: str) -> str:
    """Formats the inputed block name into minecraft:block_name."""
    block_name = block_name.lower()
    block_name.replace(" ", "_")
    block_name = "minecraft:" + block_name
 

    return block_name
 
def sort_closest(position_list: list) -> int:
    """Sorts the list from closest to farthest."""
    ...
 
def radar(scope: int, block_name: str) -> None:
    """Searches for the inputed block in the inputed radius."""
    block_positions = []
    formatted_block_name = format_block_name(block_name)
    px, py, pz = [int(p) for p in minescript.player().position]
    #minescript.execute(f"/setblock {px} {py - 1} {pz} minecraft:stripped_cherry_wood")

    #minescript.echo(px, py, pz)
    sx, sy, sz = px - scope, py - scope, pz - scope
    #minescript.echo(formatted_block_name)
    #minescript.echo(sx, sy, sz)
    #minescript.execute(f"/setblock {sx} {sy} {sz} minecraft:stripped_cherry_wood")
    counter = 0
    sxn, syn, szn = sx, sy, sz
    for x in range(scope * 2):
        syn = sy
        #minescript.echo("Working x")
        for y in range(scope * 2):
            szn = sz
            for z in range(scope * 2):
                found_block_name = minescript.getblock(sxn, syn, szn)
                #minescript.echo(found_block_name)
                #minescript.echo(sx, sy, sz)
                #minescript.echo(found_block_name == formatted_block_name)
                #minescript.execute(f"/setblock {sxn} {syn} {szn} minecraft:stripped_cherry_wood")
                if found_block_name == formatted_block_name:
                    block_positions.append([sxn, syn, szn])
                #time.sleep(1)
                counter += 1
                szn += 1
            syn += 1
        sxn += 1
    #minescript.echo(counter)
    #minescript.echo(sxn, syn, szn)
    #minescript.execute(f"/setblock {sxn} {syn} {szn} minecraft:stripped_cherry_wood")

    #block_positions.sort(key=sort_closest)
    for position in block_positions:
        minescript.echo(position)
    minescript.echo("Done")
 
 
if __name__ == "__main__":
    scope = int(sys.argv[1])
    block_name = sys.argv[2]
    radar(scope, block_name)