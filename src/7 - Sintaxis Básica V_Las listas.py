lista = [6, 9, 10, 236, 1, "hola", True]
miLista = ["Jagoba", "María", "Pepe", "Marta", "Antonio"]
miLista2 = ["Paula", "Rubén"]
print(miLista[2])
print(miLista[-1])
print(miLista[0:3])
print(miLista[:3])
print(miLista[1:3])
print(miLista[2:len(miLista)])
miLista.append("Sandra")  # Añadir algo a la lista
print(miLista)
miLista.insert(2, "Mario")
print(miLista)
miLista.extend(["Ana", "Lucía"])
print(miLista)
print(miLista.index("Jagoba"))
print("Jagoba" in miLista)
miLista.append(5)
miLista.append(True)
print(miLista)
miLista.remove("Pepe")
print(miLista)
miLista.pop()
print(miLista)
miLista3 = miLista + miLista2
print(miLista3)
miLista3 = miLista3 * 2
print(miLista3)
