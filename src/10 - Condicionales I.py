def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion


print("Programa de evaluación de notas de alumnos")
print(evaluacion(4))
print(evaluacion(7))
n = evaluacion(int(input("Introduce la nota: ")))
print("El alumno está " + n)
