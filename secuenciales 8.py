'''8)Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra
los tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer la
ruta en una semana cualquiera.'''
tiem_lu=float(input("digite el tiempo del lunes"))
tiem_mie=float(input("digite el tiempo del miercoles"))
tiem_vier=float(input("digite el tiempo del viernes"))
tiem_total=tiem_lu+tiem_mie+tiem_vier
promedio=tiem_total/3
print("el promedio en recorrer la ruta en la semna es de:",promedio,'minutos',)