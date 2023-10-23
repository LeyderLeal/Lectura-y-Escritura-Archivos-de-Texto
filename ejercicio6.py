import os

archivo=None
contactos=[]

def crearArchivo():
    """_summary_: Crea el archivo contactos.txt sino existe
    """
    if (not os.path.exists("contactos.txt")):        
        archivo = open("contactos.txt","w",encoding="UTF-8")
        

def existeContacto(identificacion,correo):
    """_summary_
        Función que verifica si ya existe un contacto
        de acuerdo a la identificación o correo
    Args:
        identificacion (str): Número de documento de identidad
        correo (str): correo electrónico del contacto

    Returns:
        booleano: True o False dependiendo si existe o no
    """
    existe=False
    for contacto in contactos:
        if (contacto[0]==identificacion or contacto[3]==correo):
            existe=True
            break
    return existe       
    

def obtenerContactos():
    archivo = open("contactos.txt","r",encoding="UTF-8")
    filas = archivo.readlines()  
    contactos.clear()  
    for fila in filas:
        contacto = fila.strip("\n").split(",")
        contactos.append(contacto)
        
def listarContactos(): 
    os.system ("cls")
    print("LISTA DE CONTACTOS REGISTRADOS\n")  
    obtenerContactos()     
    contador=1
    for contacto in contactos:
        print(f"Datos del Contacto No {contador}")
        print(f"Identificación: {contacto[0]}")
        print(f"Nombres: {contacto[1]}")
        print(f"Apellidos: {contacto[2]}")
        print(f"Correo: {contacto[3]}")
        print(f"Genero: {contacto[4]}")
        print()
        contador +=1
        
def consultarPorIdentificacion():    
    obtenerContactos()
    print("CONSULTAR CONTACTO POR IDENTIFICACIÓN")
    identificacion = input("Ingrese identificación de contacto a consultar: ")
    for contacto in contactos:
        if(contacto[0]==identificacion):
            print(f"Nombres: {contacto[1]}")
            print(f"Apellidos: {contacto[2]}")
            print(f"Correo: {contacto[3]}")
            print(f"Genero: {contacto[4]}")
            break        
    else:
        print("No existe contacto con esa identificación...")
    
def agregarContacto():
    os.system ("cls")
    print("PROCESO AGREGAR CONTACTO")
    archivo = open("contactos.txt","a",encoding="UTF-8")
    identificacion = input("Ingrese Identificación del Contacto: ")
    nombres = input("Ingrese Nombre(s) del Contacto: ")
    apellidos = input("Ingrese apellido(s) del Contacto: ")
    correo = input("Ingrese Correo del Contacto: ")
    while(True):
        genero = input("Ingrese Genero del Contacto (Femenino/Masculino): ").upper()
        if(genero == "FEMENINO" or genero=="MASCULINO"):
            break
        else:
            print("Debe volver a ingresar el genero...")
            
    existe = existeContacto(identificacion,correo)
    if(existe):
        print("Ya existe una persona con esa identificación o correo")
    else:
        contacto = f"{identificacion},{nombres},{apellidos},{correo},{genero}\n"
        archivo.write(contacto)
        archivo.close()
        print("Contacto Agregado Correctamente...")
    
def menu():
    while(True):
        os.system ("cls")
        print("\t\tGESTIÓN CONTACTOS")
        print("\t1. Agregar")
        print("\t2. Consultar Por Identificación")
        print("\t3. Listar")
        print("\t4. Salir")
        opcion = int(input("Ingrese opcion(1-4): "))
        if(opcion==1):
            agregarContacto()
        elif(opcion==2):
            consultarPorIdentificacion()
        elif(opcion==3):
            listarContactos()
        elif(opcion==4):
            print("Va a salir de la aplicación")
            break
        else:
            print("Opción no valida...")
            
        input("Presione Enter para Continuar")
        
crearArchivo()
menu()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    