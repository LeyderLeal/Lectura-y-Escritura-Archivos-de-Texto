import os

nameArchivo = input("Ingrese el nombre del archivo: ")

if os.path.exists(nameArchivo):
    archivo = open(nameArchivo, "r")
    with open(nameArchivo) as archivo:
        for linea in archivo:
            print(f"{linea}")