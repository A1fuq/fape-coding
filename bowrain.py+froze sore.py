from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random,time
while True:
    hits=mc.events.pollBlockHits()
    if len(hits) > 0:
        hit=hits[0]
        x,y,z=hits.pos.x,hits.pos.y,hits.pos.z
        mc.setBlocks(x-2,y,z,x+2,y+1,z+4,79)
    hits=mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        for i in range(50):
            mc.spawnEntity(x+random.randrange(-4,4),y+20,z+random.randrange(-4,4),10)

