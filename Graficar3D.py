import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
fig = plt.figure()
ax = fig.gca(projection='3d')

 
#draw cube
r = [0,10]
q=[10,20]
 
#for s, e in combinations(np.array(list(product(r,r,r))), 2):
 #   if np.sum(np.abs(s-e)) == 10:
  #      ax.plot3D(*zip(s,e), color="b")
#for s, e in combinations(np.array(list(product(q,[0,10],[0,10]))), 2):
 #   if np.sum(np.abs(s-e)) == 10:
 #       ax.plot3D(*zip(s,e), color="r")
#for s, e in combinations(np.array(list(product(q,[0,10],[10,20]))), 2):
 #   if np.sum(np.abs(s-e)) == 10:
  #      ax.plot3D(*zip(s,e), color="r")
ap=[[0,20],[0,10],[0,20]]
ab=[[7,10],[4,7],[4,17]]
for s, e in combinations(np.array(list(product(ap[0],ap[1],ap[2]))), 2):
    if np.sum(np.abs(s-e)) == ap[0][1]-ap[0][0] or np.sum(np.abs(s-e)) == ap[1][1]-ap[1][0] or np.sum(np.abs(s-e)) == ap[2][1]-ap[2][0] :
        ax.plot3D(*zip(s,e), color="y")
for s, e in combinations(np.array(list(product(ab[0],ab[1],ab[2]))), 2):
    if np.sum(np.abs(s-e)) == ab[0][1]-ab[0][0] or np.sum(np.abs(s-e)) == ab[1][1]-ab[1][0] or np.sum(np.abs(s-e)) == ab[2][1]-ab[2][0] :
        ax.plot3D(*zip(s,e), color="r")
for s, e in combinations(np.array(list(product([1,3],[2,3],[4,6]))), 2):
    if np.sum(np.abs(s-e)) == 3-1 or np.sum(np.abs(s-e)) == 1-ap[1][0] or np.sum(np.abs(s-e)) == 2 :
        ax.plot3D(*zip(s,e), color="g")
for s, e in combinations(np.array(list(product([15,17],[6,10],[10,20]))), 2):
    if np.sum(np.abs(s-e)) == 2 or np.sum(np.abs(s-e)) == 4 or np.sum(np.abs(s-e)) == 10 :
        ax.plot3D(*zip(s,e), color="b")
 
plt.show()
