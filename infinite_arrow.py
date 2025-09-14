import minescript as ms

while True:
    inv = ms.player_inventory()
    for i in inv: #{apple,orange,wood,axe}
        if i.item=="minecraft:arrow":
            ms.echo(i)
            ms.echo(f"Checking arrows {i.count}")
            if i.count < 64:
                dif= 64-i.count
                ms.echo(f"Filling Arrows {dif}")
                ms.execute(f"give @s minecraft:arrow {dif}",True)
                i.count=64
                ms.echo(f"new count is {i.count}")
i