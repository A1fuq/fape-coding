from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randrange
color=randrange(0,16)
myID=mc.getPlayerEntityId("PLEASEHITME")

while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        
        if data>color:
            mc.postToChat('f***')
        elif data<color:
            mc.postToChat('b****')
        else:
            mc.setBlock(hit.pos,57)
            mc.postToTitle(myID,'阿不就很了不起!')
            break