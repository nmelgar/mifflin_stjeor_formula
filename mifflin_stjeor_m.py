print("Formula Mifflin-St. Jeor para Hombre")

pesoKg = input("¿Cuál es el peso en del paciente en KG?  ")
pesoKg = float(pesoKg)

alturaCm = input("¿Cuál es la altura del paciente en CM?  ")
alturaCm = float(alturaCm)

edad = input("¿Cuál es la edad del paciente?  ")
edad = float(edad)
formula = (10 * (pesoKg)) + (6.25 * (alturaCm)) - (5 * (edad)) + 5
formula = str(formula)

print(f"El MB(Kcal entre Día) del paciente es = " + formula)
print("Siga su dieta :)")

