'''2) Un vendedor recibe un sueldo base mas un 10 % extra por comisión de sus ventas, el vendedor
desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y
el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.'''

sb=870000
v1=100000
v2=300000
v3=500000
tot_vta = v1 + v2 + v3
com = tot_vta * 0.10
tpag = sb + com
print('su sueldo neto:', tpag, 'tu comicion', com)

