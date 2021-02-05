from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random,time
while True:
    hits=mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.setBlock(x,y,z,46)
        mc.setBlock(x+1,y,z,76)
        mc.setBlock(x,y,z+1,76)
        mc.setBlock(x,y,z-1,76)
        mc.setBlock(x-1,y,z,76)
        mc.setBlock(x,y-1,z,1)
        mc.setBlock(x,y-1,z+1,1)
        mc.setBlock(x,y,z+1,76)
        
    p=mc.player.getPos()
    x=p.x+random.uniform(-20,20)
    y=p.y+1
    z=p.z+random.uniform(-20,20)

    time.sleep(0.0005)