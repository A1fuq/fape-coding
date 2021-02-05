from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random,time
x,y,z=mc.getPos()
while True:
    hits=mc.events.pollBlockHits()
    if len(hits) > 0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.setBlocks(x+3,y,z+2,x+5,y+1,z+3,79)
        mc.player.setPos(x,y+5,z)