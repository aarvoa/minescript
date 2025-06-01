import minescript as ms

ms.echo("scanning for player pos")
x,y,z= ms.player_position()
x,y,z= int(x),int(y),int(z)

for i in range(0,10):
    if i%2 ==0:
        ms.execute(f"setblock {x+i} {y} {z} oak_planks")
    elif i%5 == 0:
        ms.execute(f"setblock {x + i} {y} {z} diamond_block")
    else:
        ms.execute(f"setblock {x + i} {y} {z} netherite_block")

for i in range(0,10):
    if i%2 ==0:
        ms.execute(f"setblock {x} {y+i} {z} oak_planks")
    elif i%5 == 0:
        ms.execute(f"setblock {x} {y+i} {z} diamond_block")
    else:
        ms.execute(f"setblock {x} {y+i} {z} netherite_block")
ms.echo("program is done")