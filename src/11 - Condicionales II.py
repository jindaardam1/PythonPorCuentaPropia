print("Verificación de edad")

edad_usuario = int(input("Introduce tu edad: "))

if edad_usuario < 18:
    print("No puedes pasar.")
elif edad_usuario > 120:
    print("La edad es incorrecta.")
else:
    print("Puedes pasar.")

print("El programa ha finalizado.")
