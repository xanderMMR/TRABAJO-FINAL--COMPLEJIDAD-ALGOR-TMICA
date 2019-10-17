import os, sys

os.system("cls")

#Lectura de archivos
with open("TAAR.txt", "r") as archivo:
    lines = archivo.readlines() # coordenadas (x,y,z)
    start = 2 
    end = len(lines)-start # end 
    print(end)
    ID = [None] * end #Letra  N° ids
    anc = [None] * end #ancho --> x 
    alt = [None] * end #alto --> y
    lar = [None] * end # largo --> z 
    cant = [None] * end #cantidad por cada plancha
    
    m = lines[0].split()  #captura Ancho, Alto y Largo
    n = lines[1].split() #Captura la cantidad de planchas
    
    contadorIntroducidos = 0 
    valider = 0 #validador si es que sobrepasa
    
    for start in range(end): 
        x = lines[start+2].split() #comienza desde las planchas
        #print('x{} -->'.format(start+1) + str(x))
        contadorIntroducidos +=  int(x[0])
        
        if contadorIntroducidos > int(n[0]):
            
            print("La cantidad de planchas introducidas no coincide con la cantidad definida")
            valider = 0
            break
        else:
            valider = 1
            ID[start] = x[1] #Guarda la ID
            anc[start] = int(x[2]) #Guarda el ancho
            alt[start] = int(x[3]) #Guarda el alto
            lar[start] = int(x[4]) #Guarda el largo
            cant[start] = int(x[0]) #Guarda la cantidad de cada plancha

if valider == 0 or contadorIntroducidos != int(n[0]):
    print("Saliendo de programa")
    sys.exit()
print(cant,ID,anc,alt,lar)


ancho = int(m[0])
alto = int(m[1])
largo = int(m[2])
cantidad = int(n[0])
anchoCajas = anc
altoCajas = alt
largoCajas = lar

sumatoriaAreaCajas = 0
volumenTotal = ancho * alto * largo
for start in range(end):
    for i in range(int(cant[start])):
        areaCajas = anchoCajas[start] * altoCajas[start] * largoCajas[start]
        sumatoriaAreaCajas += areaCajas

print("Area total", volumenTotal)
print("Area utilizada",sumatoriaAreaCajas)

desperdicio = (sumatoriaAreaCajas * 100) / volumenTotal #sera en porcentaje 

print("El desperdicio fue : {}%".format(100 - desperdicio))


def datos(): #Juntamos los datos
    listaDatos = [None] * contadorIntroducidos
    contador = 0
    for start in range(end):
        for i in range(int(cant[start])):
            listaDatos[contador]=[anc[start],alt[start],lar[start]]
            contador += 1
    return listaDatos
print(datos())


#Transformando ID
newID = [] 
for i in range(end):
    getter = int(cant[i])
    for j in range(getter):
        newID.append(ID[i])
print(newID)
