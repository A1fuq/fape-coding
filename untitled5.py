from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random,time
while True:
    hits=mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        for i in range(100):
            mc.spawnEntity(x+random.randrange(-3,3),y+10,z+random.randrange(-3,3),10)
        
        