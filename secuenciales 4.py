'''	4)Calcular el numero de pulsaciones que una persona debe tener por
cada 10 segundos de ejercicio, si la formula es:
			num. pulsaciones = (220 - edad)/10
'''
pulsa_por_min=int(input("digine el numero de pulsaciones"))
edad=int(input("digite la edad de la persona"))
num_pulsaciones=(pulsa_por_min-edad)/10
print("la cantidad de pulsaciones es de:",num_pulsaciones)
