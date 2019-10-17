import random, sys


#nombre
nRandom = ""
cantLetras = 5
for _ in range(5):
    strTemp = str(chr(random.randint(65, 91)))
    nRandom = nRandom + strTemp

initX = random.randint(700, 800)
initY = random.randint(700, 800)
initZ = random.randint(700, 800)

coordenadas = str(initX) + " " + str(initY) + " " + str(initZ)

print(coordenadas)

volumenTotal= initX * initY * initZ
areaSuma = 0
chInit = 65

print(chr(chInit))

totalCant = random.randint(5, 15)

print(totalCant)
coordenadas = coordenadas + "\n" + str(totalCant) + "\n"
contadorInterno = 0

#generar datos aleatorios
for i in range(totalCant):
    temp1 = random.randint(100, 200)
    temp2 = random.randint(100, 200)
    temp3 = random.randint(100, 200)
    print(temp1, temp2, temp3)
    cantidad = random.randint(1, 3)
    contadorInterno += cantidad
    if contadorInterno <= totalCant:
        areaTemp = temp1 * temp2 * temp3 * cantidad
        if areaTemp >= volumenTotal:
            print("Una de las tablas creadas ha sido más grande que la plancha")
            sys.exit()
        areaSuma += areaTemp
        if areaSuma != volumenTotal:
            streng = str( str(cantidad) + " " + chr(chInit + i)) + " " + str(temp1) + " " + str(temp2) + " " + str(temp3) + "\n"
            coordenadas += streng


file = open("./" + nRandom + ".txt", "w")
print("Archivo creado ---> " + nRandom + ".txt")
try:
    file.write(coordenadas)
except ValueError:
    print("Error")
file.close()
