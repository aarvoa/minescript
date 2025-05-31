import minescript

minescript.echo("Hello Aarav")
minescript.chat("I am a Bot")

for i in range(0,10):
    x,y,z = minescript.player_position()
    # x,y,z= int(x),int(y),int(z)
    x=int(x)
    y=int(y)
    z=int(z)
    minescript.echo(f"the value of i is {i}")
    minescript.execute(f"setblock {x+i} {y-1} {z} netherite_block")
    minescript.echo(minescript.getblock(x+i,y,z))
