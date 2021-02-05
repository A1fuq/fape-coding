from mcpi.minecraft import Minecraft
mc=Minecraft.create()
a=0
for i in range(25):
    x,y,z=mc.player.getPos()
    x=x+i
    mc.setBlock(x,y-1,z,57)
mc.setBlocks(x+25,y,z,x+10,y+10,z+10,57)
mc.setBlocks(x+26,y+1,z+1,x+9,y+9,z+9,0)
def plantTree(x,y,z):
    mc.setBlocks(x+1,y+2,z+1,x+3,y+5,z+2,46)
    mc.setBlocks(x+2,y,z+1,x+2,y+4,z+1,17)
    
    
x,y,z=mc.player.getPos()
plantTree(x,y,z)
plantTree(x-5,y,z)