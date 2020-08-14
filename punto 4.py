'''	4) Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
Dicha calificación se compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final '''
c1=4.5
c2=5
c3=3
ef=4
tf=2.3
prom = (c1 + c2 + c3)/3
porcentajeparc = prom * 0.55
porcentajeexfin = ef * 0.30
porctrafin = tf * 0.15
cf = porcentajeparc + porcentajeexfin + porctrafin
print('su colificacion final es de:', cf)

