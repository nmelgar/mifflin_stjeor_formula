print("Formula Mifflin-St. Jeor para Mujer")

pesoKg = input("¿Cuál es el peso en de la paciente en KG?  ")
pesoKg = float(pesoKg)

alturaCm = input("¿Cuál es la altura de la paciente en CM?  ")
alturaCm = float(alturaCm)

edad = input("¿Cuál es la edad de la paciente?  ")
edad = float(edad)
formula = ((10 * (pesoKg)) + (6.25 * (alturaCm)) - (5 * (edad)) - 161)
formula = str(formula)

print(f"El MB(Kcal entre Día) de la paciente es = " + formula)
print("Siga su dieta :)")

