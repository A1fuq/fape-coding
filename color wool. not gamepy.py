from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random 
for i in range(10):
    x,y,z=mc.player.getPos()
    x=x+i
    for j in range(50):
        color=random.randrange(0,16)
        z+=1
        mc.setBlock(x,y-1,z,35,color)