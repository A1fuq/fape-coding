from mcpi.minecraft import Minecraft
mc=Minecraft.create()

a=[]
b=[]
c=[]

for i in range(1,4):
    a.append(2*i)
for i in range(1,4):
    b.append(3*i)
for i in range(1,4):
    c.append(4*i)
x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,8,str(a),str(b),str(c))