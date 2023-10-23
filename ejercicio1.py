try:
    archivo = open("personas.txt", "a")
    print("Archivo creado")
    nombre = input("Ingrese un nombre: ")
    archivo.write(f"{nombre}\n")
    archivo.close()
    
except IOError as error:
    print(error.sterror)