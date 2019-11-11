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
G.append(caja(ID='A', x=317, y=1840, w=401, h=327))
G.append(caja(ID='B', x=0, y=1840, w=317, h=445))
G.append(caja(ID='C', x=0, y=0, w=492, h=493))
G.append(caja(ID='D', x=337, y=2285, w=361, h=308))
G.append(caja(ID='D', x=0, y=2675, w=308, h=361))
G.append(caja(ID='D', x=308, y=2675, w=308, h=361))
G.append(caja(ID='E', x=492, y=0, w=202, h=199))
G.append(caja(ID='E', x=492, y=199, w=202, h=199))
G.append(caja(ID='E', x=441, y=493, w=202, h=199))
G.append(caja(ID='F', x=0, y=2285, w=337, h=390))
G.append(caja(ID='G', x=0, y=493, w=441, h=449))
G.append(caja(ID='G', x=0, y=942, w=441, h=449))
G.append(caja(ID='G', x=0, y=1391, w=441, h=449))

'''
#     ID(ID='K', x=0, y=1000, )

# C G E E E
G.append(caja(ID='E', x=492, y=0, w=202, h=199))
G.append(caja(ID='C', x=0, y=0, w=492, h=493))
G.append(caja(ID='E', x=441, y=493, w=202, h=199))
G.append(caja(ID='E', x=492, y=199, w=202, h=199))
G.append(caja(ID='G', x=0, y=493, w=441, h=449))
'''
print(G[0][2])
f = []

#falta una función que pase de esto [ID(ID='A', x=0, y=0, w=293, h=200), ID(ID='B', x=293, y=0, w=201, h=200)] a 
#                           [ [[0,293], [0,200]] , [[293, 293+201], [0,200]]  ]
        
    
def killerTraps(G): #G = [([], [], []), ([],[],[])]
   
    nG = sorted(G, key = lambda y: y[1][0]) #Ordenamos primero por y, luego si su alto sobrepasa, se agrega a otra linea
    #nG = sorted(G, key = lambda y: y[0][2]) 
    return nG
print('----')
print('----')

xAnterior = [0]
yAnterior = [0]
ancho = 719 
alto = 785

#YA ESTAMOS CERCA, AHORA SOLO TENEMOS QUE CAPTURAR EL MAYOR Y DE LOS PRIMEROS

def _R00t_5layer_(G, alto) :
    for i in range(len(G)) :
        x,y,z = G[i]
        if y[0] > alto or y[1] > alto:
            
            G[1][0] = 30
            G[1][0] = 60

yMayor = [0]
def parser(G, f):
    for i in range(len(G)) :
        xActual = G[i][1] + G[i][3]
        x = [ G[i][1], xActual]
        #x = [G[i][1], xActual]
        yActual = G[i][2] + G[i][4]
        
            
        if G[i][2]>(alto*2) and yActual>(alto*2) :
            zs = 200
            zf = zs + 100
            y = [G[i][2] - yMayor[0]*3, yActual- yMayor[0]*3] 
            
        elif G[i][2]>alto and yActual>alto :
            zs = 100
            zf = zs + 100
            y = [G[i][2] - yMayor[0], yActual- yMayor[0]]  
     
        else :
            zs = 0
            zf = zs + 100
            y = [G[i][2], yActual] 
            yMayor[0] = yActual
        #y = [G[i][2], G[i][5]]
        #xAnterior[0] = xActual
        
        
            
        z = [zs, zf]
        #z = [G[i][3],G[i][6]]
        f.append((x,y,z))
    t = killerTraps(f)  
    return t #Hasta acá ya me ordena en y, ahora toca verificar si sobrepasa al alto


    #return f
print('L')
l = parser(G, f)
print(l)
print('----')
print('----')
def dibujar(g):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    n=13
    arrCajas= g
    arrCajas.insert(0,([0,719],[0,785],[0,752]))
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
