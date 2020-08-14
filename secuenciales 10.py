'''10)	Un alumno desea saber cual será su promedio general en las tres materias mas
difíciles que cursa y cual será el promedio que obtendrá en cada una de ellas.
Estas materias se evalúan como se muestra a continuación:

La calificación de Matemáticas se obtiene de la sig. manera:
Examen 90%
Promedio de tareas 10%
En esta materia se pidió un total de tres tareas.

La calificación de Física se obtiene de la sig. manera:
Examen 80%
Promedio de tareas 20%
En esta materia se pidió un total de dos tareas.

La calificación de Química se obtiene de la sig. manera:
Examen 85%
Promedio de tareas 15%
En esta materia se pidió un promedio de tres tareas.
'''

materia=(input("digite la materia"))
examen=float(input("digite la nota del examen"))
tarea1=float(input("digite la nota de la tarea1"))
tarea2=float(input("digite la nota de la tarea2"))
tarea3=float(input("digite la nota de la tarea3"))
notatotal=0.90*examen+0.10*(tarea1+tarea2+tarea3)/3
print("el promedio de matematicas es:",notatotal)


materia=(input("digite la materia"))
examen=float(input("digite la nota del examen"))
tarea1=float(input("digite la nota de la tarea1"))
tarea2=float(input("digite la nota de la tarea2"))
notatotal=0.80*examen+0.20*(tarea1+tarea2)/2
print("el promedio de fisica es:",notatotal)


materia=(input("digite la materia"))
examen=float(input("digite la nota del examen"))
tarea1=float(input("digite la nota de la tarea1"))
tarea2=float(input("digite la nota de la tarea2"))
tarea3=float(input("digite la nota de la tarea3"))
notatotal=0.85*examen+0.15*(tarea1+tarea2+tarea3)/3
print("el promedio de quimica es:",notatotal)