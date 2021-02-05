from mcpi.minecraft import Minecraft
mc=Minecraft.create()

myID=mc.getPlayerEntityId("PLEASEHITME")


while True:
    x,y,z=mc.player.getPos()
    a=mc.getBlock(x,y-1,z)
    print(a)
   

    if a == 57:
        mc.postToTitle(myID,"start?!")
        mc.executeCommand("spawnpoint PLEASEHITME")
    if a == 169:
        mc.executeCommand("kill @e")
    if a == 41:
        mc.executeCommand("spawnpoint PLEASEHITME")
    if a == 133:
        mc.postToTitle(myID,"finish!")
        break

