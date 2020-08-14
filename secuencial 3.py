'''La presión, el volumen y la temperatura de una masa de aire se relacionan por la formula:
			masa = (presión * volumen)/(0.37 * (temperatura + 460))
'''
presion=float(input("digite la presion"))
volumen=float(input("digite el volumen"))
temperatura=float(input("digite la temperatura"))
masa=(presion * volumen)/(0.37 * (temperatura + 460))
print("la masa del aire es:",masa)

