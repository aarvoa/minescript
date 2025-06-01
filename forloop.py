import minescript as ms

ms.echo("scanning for player pos")
x,y,z= ms.player_position()
x,y,z= int(x),int(y),int(z)

for i in range(0,10):
    ms.execute(f"setblock {x+i} {y} {z} oak_planks")
ms.echo("program is done")