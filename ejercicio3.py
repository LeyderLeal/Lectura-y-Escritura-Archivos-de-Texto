import os

name = input("Ingrese el nombre del archivo: ")

if os.path.exists(name):
    buscar = input(f"Ingrese la palabra a encontrar en {name}: ")
    archivo = open(name,"r")
    lineas = archivo.readlines()
    existe = False
    for linea in lineas:
        palabras = linea.strip("\n").split(" ") 
    for palabra in palabras:
        if (palabra==buscar):
            print(f"La palabra {palabra} si existe en el archivo")
            existe = True
            break
        if(existe):
            break
        if(not existe):
            print(f"La palabra {palabra} no existe en el archivo")
        
else: 
    print("El archivo no existe")