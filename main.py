from pruebas import pruebas, pruebasSinGraficar, estacionesAleatorias

#Prueba 1

pruebas("Observatorio" ,"Ciudad Azteca")

#Prueba 2

pruebas("Indios Verdes","Velodromo")

#Prueba 3

pruebas("El Rosario","Tasqueña")


"""

numPruebas = 100000
n = 0


while n < numPruebas:
    n = n+1
    inicioAleatorio, finalAleatorio = estacionesAleatorias()
    completitud = pruebasSinGraficar(inicioAleatorio,finalAleatorio)
    if completitud is not True:
        break

if completitud:
    print(f"Cumple para #{n} pruebas")
else:
    print(f"No cumple para #{n} pruebas")

"""

