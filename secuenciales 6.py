'''6)En un hospital existen tres áreas: Ginecología, Pediatría, Traumatologia.
El presupuesto anual del hospital se reparte conforme a la sig. tabla:
Área		Porcentaje del presupuesto
Ginecología			40%
Traumatologia			30%
Pediatría			30%
Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal.
'''
pres_anual=int(input("¿cual es el presupuesto anual?"))
ginec=pres_anual*0.40
traum=pres_anual*0.30
pedia=pres_anual*0.30
print("el tottal de presupuesto para cada una es de:""\n",'ginecologia',ginec,"\n"'tarumatologia',traum,"\n"'pediatria',pedia,)