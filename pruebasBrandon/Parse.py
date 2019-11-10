# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:22:41 2019

@author: R00t_5layer
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
import random as rnd
import time
from collections import namedtuple
ide='ID'
caja = namedtuple('ID', [ide,'x', 'y', 'w', 'h']) 

G = []
'''
G  = [ID(ID='A', x=0, y=0, w=293, h=200), 
      ID(ID='B', x=293, y=0, w=201, h=200), 
      ID(ID='B', x=494, y=0, w=201, h=200), 
      ID(ID='C', x=0, y=200, w=293, h=200), 
      ID(ID='D', x=293, y=200, w=285, h=200), 
      ID(ID='E', x=0, y=400, w=294, h=200),
      ID(ID='F', x=294, y=400, w=258, h=200), 
      ID(ID='G', x=0, y=600, w=207, h=200),
      ID(ID='G', x=207, y=600, w=207, h=200), 
      ID(ID='H', x=414, y=600, w=230, h=200), 
      ID(ID='I', x=0, y=800, w=283, h=200),
      ID(ID='J', x=283, y=800, w=252, h=200), 
      ID(ID='J', x=0, y=1000, w=252, h=200)]
'''
#     ID(ID='K', x=0, y=1000, )

# C G E E E
G.append(caja(ID='E', x=492, y=0, w=202, h=199))
G.append(caja(ID='C', x=0, y=0, w=492, h=493))
G.append(caja(ID='E', x=441, y=493, w=202, h=199))
G.append(caja(ID='E', x=492, y=199, w=202, h=199))
G.append(caja(ID='G', x=0, y=493, w=441, h=449))

print(G)
f = []

#falta una función que pase de esto [ID(ID='A', x=0, y=0, w=293, h=200), ID(ID='B', x=293, y=0, w=201, h=200)] a 
#                           [ [[0,293], [0,200]] , [[293, 293+201], [0,200]]  ]
        
    
def killerTraps(G): #G = [([], [], []), ([],[],[])]
   
    nG = sorted(G, key = lambda y: y[1][0]) #Ordenamos primero por y, luego si su alto sobrepasa, se agrega a otra linea
    return nG
    
print('----')
print('----')

xAnterior = [0]
yAnterior = [0]
ancho = 719 
alto = 785

def _R00t_5layer_(G) :
    R00t_5layer = []
    
def parser(G, f):
    for i in range(len(G)) :
        xActual = G[i][1] + G[i][3]
        x = [ G[i][1], xActual]
        #x = [G[i][1], xActual]
        yActual = G[i][2] + G[i][4]
        y = [G[i][2], yActual]
        #y = [G[i][2], G[i][5]]
        #xAnterior[0] = xActual
        z = [0, 30]
        #z = [G[i][3],G[i][6]]
        f.append((x,y,z))
    t = killerTraps(f)  
    return t #Hasta acá ya me ordena en y, ahora toca verificar si sobrepasa al alto


    #return f
l = parser(G, f)
print(l)
print('----')
print('----')
def dibujar(g):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    n=6
    arrCajas= g
    arrCajas.insert(0,([0,719],[0,785],[0,60]))
    print('---')
    print(arrCajas)
    print('---')
    print(len(arrCajas))
    
    
    rgb=[None]*n
    #print(rgb)
    
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
dibujar(l)
