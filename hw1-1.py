from mcpi.minecraft import Minecraft
import time
mc =Minecraft.create()
a=-5
b=81
c=-7.5
mc.player.setPos(a,b,c)
Position =mc.player.getPos()
x = Position.x
y = Position.y
z = Position.z
time.sleep(10)
mc.player.setPos(x,y,z)