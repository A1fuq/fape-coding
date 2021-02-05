
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

myID=mc.getPlayerEntityId("PLEASEHITME")

x,y,z=mc.player.getPos()
mc.setBlocks(x,y,z,x+15,y+25,z+15,1)
mc.setBlocks(x+1,y+1,z+1,x+14,y+24,z+14,0)
mc.setBlocks(x+3,y+1,z,x+3,y+2,z,0)
mc.setBlocks(x,y+25,z,x+15,y+25,z+15,0)

mc.setBlock(x+12,y+1,z+1,166)
mc.setBlock(x+1,y+1,z+11,54)
mc.setBlock(x+1,y+1,z+12,57)


while True:
    x,y,z=mc.player.getPos()
    a=mc.getBlock(x,y-1,z)
    print(a)
   
    if a == 57:
        mc.postToTitle(myID,"i can't start")
    elif a == 166:
        mc.postToTitle(myID,"start?!")
        mc.executeCommand
        break
    elif a == 1:
        mc.executeCommand("kill @e")

