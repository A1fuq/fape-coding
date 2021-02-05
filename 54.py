from mcpi.minecraft import Minecraft
mc =Minecraft.create()
x,y,z,=mc.player.getPos()
a=input('你是誰?')
mc.postToChat('Hello'+a+'今天天氣爛死了 我現在活著喔!')
mc.setBlocks(x,y,z,x+10,y+10,z+10,46)
mc.setBlocks(x+1,y+1,z+1,x+9,y+9,z+9,0)
mc.setBlocks(x,y+6,z,x+10,y+6,z+10,46mc.setBlocks)
#mc.setBlocks(x+2,y+1,z,x+2,y+2,z,0)