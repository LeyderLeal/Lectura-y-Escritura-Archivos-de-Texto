try:
    archivo = open("lineas.txt", "a")
    print("Archivo creado")
    lineas = int(input("Ingrese cuantas veces desea repetir la linea de texto: "))
    
    for linea in range (1, lineas + 1):
        archivo.write(f"Linea de texto: {linea} \n")
        
except IOError as error:
    print(error.sterror)