diccionario = {"España": "Madrid", "Italia": "Roma", "Alemania": "Berlín", "Japón": "Tokio"}
print(diccionario["Japón"])
print(diccionario)
diccionario["Portugal"] = "Oporto"  # Está mal
diccionario["Portugal"] = "Lisboa"  # Corregido
print(diccionario)
del diccionario["Alemania"]
print(diccionario)
segundoDiccionario = {"Corea del sur": "Seúl", 24: "Hola"}
print(segundoDiccionario)
tupla = ["España", "Portugual", "Japón"]
dicConTupla = {tupla[0]: "Madrid", tupla[1]: "Lisboa", tupla[2]: "Tokio"}
print(dicConTupla)
dicValorTupla = {"Paises": tupla}
print(dicValorTupla)
dicConValorDic = {"Paises con capitales": diccionario}
print(dicConValorDic)
# Métodos importantes
print(diccionario.keys())
print(diccionario.values())
print(len(diccionario))
