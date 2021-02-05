from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getPos()
while True:
mc.spawnEntity(x,y,z,60)