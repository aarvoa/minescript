import minescript as ms

ms.chat("Hello Welcome to my server!")


inv = ms.player_inventory()
for i in inv:
    ms.echo(i.item, i.count)