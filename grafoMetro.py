import json

with open("mapaMetro.json","r",encoding="utf-8") as file:
    data = json.load(file)

mapaMetro = data["mapaMetro"]





metro = {}

for linea in mapaMetro.values():
    for i in range(len(linea)):
        estacion = linea[i]

        if estacion not in metro:
            metro[estacion] = []

       
        if i > 0:
            vecino = linea[i-1]
            if vecino not in metro[estacion]:
                metro[estacion].append(vecino)

       
        if i < len(linea) - 1:
            vecino = linea[i+1]
            if vecino not in metro[estacion]:
                metro[estacion].append(vecino)

