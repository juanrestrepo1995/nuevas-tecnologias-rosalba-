'''9)Tres personas deciden invertir su dinero para fundar una empresa. Cada una
 de ellas invierte una cantidad distinta. Obtener el porcentaje que cada quien
 invierte con respecto a la cantidad total invertida.'''
inversion1=int(input("digite la primero inversion"))
inversion2=int(input("digite la segunda inversion"))
inversion3=int(input("digite su tercer invercion"))
inversiontotal=inversion1+inversion2+inversion3
persona1=inversion1*100/inversiontotal
persona2=inversion2*100/inversiontotal
persona3=inversion3*100/inversiontotal
print("el procentaje que le coreponde a cada uno es:"'\n''primera persona',persona1,'%\n' 'segunda persona ',persona2,'%\n''tercera persona',persona3,'%\n')