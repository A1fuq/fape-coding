from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random,time
a,b,c=mc.player.getPos()
while True:
    hits=mc.events.pollBlockHits()
    if len(hits) > 0:
        hit=hits[0]
        mc.spawnEntity(a+1,b+1,c+1,81)
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.setBlocks(x-1,y,z-1,x+1,y+3,z+1,79)
        mc.player.setPos(x,y+5,z)