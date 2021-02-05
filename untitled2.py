from mcpi.minecraft import Minecraft
mc=Minecraft.create()

for i in range(25):
    x,y,z=mc.player.getPos()
    x=x+i
    mc.setBlock(x,y-1,z,57)
mc.setBlocks(x+25,y,z,x+10,y+10,z+10,57)
mc.setBlocks(x+26,y+1,z+1,x+9,y+9,z+9,0)