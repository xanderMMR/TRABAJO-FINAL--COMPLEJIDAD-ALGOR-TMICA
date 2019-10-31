import matplotlib.pyplot as from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
import random as rnd
import time
fig = plt.figure()
ax = fig.gca(projection='3d')
n=10
arrCajas=[]

for i in range (n):
    xc=i+10
    posX=rnd.randint(i,10000)
    posY=rnd.randint(i,10000)
    posZ=rnd.randint(i,10000)
    lenX=rnd.randint(1,30)
    lenY=rnd.randint(1,30)
    lenZ=rnd.randint(1,30)
    x=[posX,lenX]
    y=[posY,lenY]
    z=[posZ,lenZ]
    if posX>lenX:
        x=[lenX,posX]
    if posY>lenY:
        y=[lenY,posY]
    if posZ>lenZ:
        z=[lenZ,posZ]
    arrCajas.append([x,y,z])


rgb=[None]*n
print(rgb)

for i in range(n):
    r=rnd.randint(0,1)
    g=rnd.randint(0,1)
    b=rnd.randint(0,1)
    rgb[i]=[r,g,b]
        
for k in range (n):
    for s, e in combinations(np.array(list(product(arrCajas[k][0],arrCajas[k][1],arrCajas[k][2]))), 2):
        if np.sum(np.abs(s-e)) == arrCajas[k][0][1]-arrCajas[k][0][0] or np.sum(np.abs(s-e)) == arrCajas[k][1][1]-arrCajas[k][1][0] or np.sum(np.abs(s-e)) == arrCajas[k][2][1]-arrCajas[k][2][0] :
            ax.plot3D(*zip(s,e), color=rgb[k])
plt.show()
