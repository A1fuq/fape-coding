from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random,time
while True:
    hits=mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        mc.spawnEntity(x,y+10,z,10)
        
    p=mc.player.getPos()
    x=p.x+random.uniform(-20,20)
    y=p.y+1

    time.sleep(0.0005)