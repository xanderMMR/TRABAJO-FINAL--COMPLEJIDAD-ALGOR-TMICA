# TRABAJO FINAL COMPLEJIDAD ALGORÍTMICA

Integrantes:

* Brandon Alegría Vivanco - u201615131 
* Joaquín Aguirre Peralta - u201620285 
* Alexander Moisés Meléndez Ríos - u201815920

Profesor: Luis Canaval Sección: CC41

## Índice

*     Introducción
*     Objetivo del Estudiante (Student Outcome)
*     Estado del Arte
*     Aporte
*     Diseño de Aplicativo para Pruebas
*     Validación de Resultados y Discusión
*     Conclusiones y Trabajos Futuros
*     Conclusiones
*     Anexos
*     Bibliografía

• Cubrir totalmente los puntos 1 al 4 del informe y adicionalmente el pseudocódigo de los métodos a utilizar.
## 1. Introducción

La tecnología ha avanzado mucho gracias a la ciencia, este proceso se logra cada vez mas rápido y a grandes pasos por los nuevos descubrimientos e investigaciones que se hacen alrededor del mundo. Uno de los campos que se beneficia de los resultados de la tecnología, es el comercio. Por otro lado, cabe mencionar que existen constantes y crecientes necesidades que van surgiendo sistemáticamente por pedido de la gente, los cuales deben ser saciados mayormente por las empresas. Para poder transportar la mayor cantidad de productos en el menor espacio posible, se acude a las empresas de logística, las cuales comúnmente afrontan situaciones de empaquetamiento en 3 dimensiones. En este trabajo se dará una propuesta para resolver dicho problema; se diseñarán distintos algoritmos basados en la temática el curso de Complejidad Algorítmica para poder resolver el problema del empaquetamiento en 3 dimensiones.

## 2. Objetivo del Estudiante (Student Outcome)

Con este proyecto se buscará aplicar los principios enseñados en el curso de Complejidad Algorítmica. Se emplearán los conocimientos sobre programación y el uso de diversos algoritmos que satisfacer los requisitos propuestos. De la misma manera se le asignarán tareas equitativas a cada estudiante, el cual deberá informarse sobre un algoritmo distinto al de sus compañeros de trabajo, para que todos participen en las tareas de este proyecto y logren el objetivo deseado.

## 3. Estado del Arte: De los algoritmos revisados para el trabajo

Se han estado investigado el uso algoritmos basados en heurísticas de prioridad y otras heurísticas ligadas al empaquetamiento en 2d como en 3d. Dado que éste un problema que no tiene una solución 100% eficiente, lo que se busca es tratar de encontrar una solución aproximada lo más eficiente posible. Sin embargo no es totalmente efectiva, por otro lado puede ayudar a manejar y poner un punto de partida al mejoramiento e implementación de nuevas soluciones de este tipo de problemas.

## 4. Aporte: Demuestra ética profesional en el ejercicio de la profesión (analiza y muestra la importancia de hallar la complejidad algorítmica considerando a los algoritmos como tecnología)

Uno de los algoritmos escogidos para dar solución al Bin Packing 3D es una combinación entre un algoritmo pripio y el Best Fit Algorithm, el cual será explicado a continuación: Para dar marcha a este algoritmo primero se debe ordenar todas las cajas de mayor a menor en cuestión de volumen, luego se colocará por "default" en la posición (0,0,0). Se procede a colocar los siguientes bloques uno por uno. Si algún bloque no puede ser colocado en la posición siguiente, se rota el cubo hasta que quepa en la posición, sin embargo si el bloque es girado en las 6 distintas posiciones y aún así no cabe, se procede a intentar con los siguientes bloque, por lo tanto este bloque anterior se añade a una lista de bloques que se colocarán después de intentar colocar los bloques restantes.

Pseudocódigo:

if ancho_contenedor < alto_contenedor & profundo_contenedor: empacar_por_ancho = True empacar_por_alto = False elif alto_contenedor < ancho_contenedor and profundo_contenedo: empacar_por_ancho = False empacar_por_alto = False elif alto_contenedor < ancho_contenedor: empacar_por_ancho = False empacar_por_alto = True

no_empacados = objetos

do: Empacar = no_empacados no_empacados = {}

//Crear un nuevo contenedor llamado: contenedor_actual, revisar si el objeto a empacar[0] cabe en ese contenedor en la posición (x,y,z)=(0,0,0)
if empacar[0] no cabe: se rota hasta que quepa y se empaque en la posicion (0,0,0) for i=1 in Empacar -1: objeto_actual = Empacar[i] encajo = False

for p=0 in (0:2) k=0 while k < len(Contenedor_actual) and not encajo = False: objeto_del_contenedor = contenedor_actual.objeto[k] if ancho_caja: pivot = p elif ancho_caja: switch p: calcular pivote p para altura
else: switch p: calcular pivote p para anchura

switch pivote: case 0 : Escoger (pivoteX, pivoteY, pivoteZ) como esquina inferior derecha de atrás del objeto_de_contenedor: break case 1 : Escoger (pivotX, pivovY, pivotZ ) como la esquina inferior izquierda del objeto_de_contenedor: break case : Escoger (pivotX, pivovY, pivotZ ) como la esquina supeior izquierda del objeto_de_contenedor: break if objetos_actuales <= Contenedor_actual in position(pivotX, pivotY, pivotZ): //Empacar el objeto actual en el contenedor actual en la positión (pivotX, pivotY,pivotZ) fitted=true else: //intentar rotar el objeto do: rotar Objeto_actualRotate currenItem while Objeto_principal no entra en Contenedor_principal en la posición(pivotX,pivotY) and no todas las rotaciones del objeto_actual están hechas if Objeto_actual puede ser empaquetado en Caja_actual en la posición (pivotX, pivotY, pivotZ): Empacar el Objeto_actual en Contenedor actual en posicion pivoteX, pivoteY ,pivoteZ encajo = True else: Restaurar el Objeto_actual a su posición rotación original: if (encajo == False): objeto_actual.append(lista_de_no_empacados): while No_empacado tiene al menos 1: //objeto está en el

## 5. Diseño de Aplicativo para Pruebas:
 Presenta pseudocódigo de algoritmos que resuelvan el problema tratado, y demuestra responsabilidad en el diseño, implementación y validación de la solución y casos de prueba.

## 6. Validación de Resultados y Discusión: 
Muestra tablas comparativas del consumo de recursos de memoria y tiempo.

## 7. Conclusiones y Trabajos Futuros: 
•	Impacto global	: El impacto global, es un poco regular, ya que el algoritmo no es que sea tan revolucionario, solo es una solución intermedia y un poco óptima, por lo que a nivel global, no cambia mucho las cosas, solo mejora los conocimientos y es un punto de partida para desarrollar una solución más eficiente y mas eficaz. De cierta forma esta solución mejora tanto en términos ambientales, económicos  y sociales a las empresas y personas.						
•	Impacto ambiental: Teniendo en cuenta que es una solución parcial y se asemeja mucho a la exacta, tenemos una eficiencia energetica en los sistemas de cómputo, menos consumo de energía, lo que conlleva a un ahorro de energía y menos riesgo para el planeta
•	Impacto económico: Actúa de forma positiva en cuanto a las empresas, que ya no gastarán tanto en máquinas super avanzadas, o quizá en empleados, pero afecta de manera negativa también a las personas despedidas, o personas que dejarán de desarrollar las máquinas avanzadas.
•	Impacto social: Esta solución podría conllevar a la realización de mejoras en un futuro, por lo que tiene un impacto social grande, ya que varias personas están esmeradas en encontrar solución 100% exacta a este problema, por lo que generará un gran movimiento de masas para seguir mejorando estos algoritmos parciales


## 8. Conclusiones 
Para el desarrollo de este proyecto se tuvo que pensar mucho en la forma de desarrollarlo, desde leer heurísticas hasta tener que buscar soluciones mucho más avanzadas, si bien es cierto, no existe solución 100% efectiva para este problema. Para soluciones pequeñas no es tan dificil su solución, por lo que su el hardware en ese caso no es tan importante, sin embargo, para soluciones con mucho más datos, se necesita hardware muy potente, ya que se verán muchos más estados, también depende mucho de los datos ingresados. La ventaja de usar backtracking es que puedes ver cada estado que puede generar cada rectángulo y en cierta forma encontrarás una solución, y básicamente probarás cada combinación hasta encontrar la que resuelva el problema (usa brute force en muchos casos). Pero la desventaja significativa es esa misma, que se usan muchos recursos para probar todas las soluciones y encontrar una, se podría mejorar con Threads, ya que de esa forma sería un poco más rápida la tarea de buscar los lugares perfectos para posicionar los rectángulos. La ventaja de usar Greedy es que ayuda a que el backtracking no realice tantas operaciones, lo que mejora de cierta forma su eficiencia, pero sigue sin encontrar una solución exacta.
## 9. Anexos
10. Bibliografía
