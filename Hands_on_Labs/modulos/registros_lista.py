import json

    #Carga la lista de vehículos desde un archivo JSON llamado 'vehiculos.json'.
    
    #Returns: 
    # list: Una lista de vehículos si el archivo existe, o una lista vacía si no se encuentra el archivo.
    
def cargar_vehiculos():
    try:
        with open("vehiculos.json", "r") as file:
            return json.load(file)  #cargar y devolver los datos desde el archivo json
    except FileNotFoundError:
        return []    #retornar una lista vacia si el archivo no existe

def guardar_vehiculos(vehiculos):
    
   
    #Guarda la lista de vehículos en un archivo json llamado 'vehiculos.json'.
    
    #Args:
        #vehiculos (list): La lista de vehículos a guardar en el archivo.
    

    with open("vehiculos.json", "w") as file:
        json.dump(vehiculos, file, indent=4)  #guarda la sangria con 4 espacios

def validaciones_codigos(codigo):

    #Valida que el código del vehículo sea un número positivo.
    #Args:
        #codigo (str): El código del vehículo como cadena de texto.
    #Returns:
        #bool: True si el código es válido, False en caso contrario.

    try:
        codigo_num = int(codigo) #Intentar convertir el código a un entero
        if codigo_num < 0:
            print('\n (❌) No se permiten códigos negativos.')
            return False
        return True
    except ValueError:
        print('\n (❌) El código debe contener solo números.')
        return False
    
def registrar_vehiculo():

    #Registra un nuevo vehículo solicitando al usuario el código, marca, modelo y año.
    #Realiza validaciones y guarda el vehículo si es válido y único.
    
    codigo=input("\n ➔ Ingrese el c͟o͟d͟i͟g͟o͟ del vehículo ( 🏷️ ) : ")
    if not validaciones_codigos(codigo):
        return                  # Salir si el código no es válido
    marca=input("\n ➔ Ingrese la m͟a͟r͟c͟a͟ del vehículo ( 📦 ) : ")
    modelo=input("\n ➔ Ingrese el m͟o͟d͟e͟l͟o͟ del vehículo ( 🛒 ) : ")
    
    try:
        print("\n ➔ Ingrese el año de lanzamiento del vehículo ( 🗓️ ) : ")
        anio = int(input())     # Intentar convertir el año a un número entero
    except ValueError:
        print("\n (❌) El año debe ser un número entero.")
        return

    vehiculos = cargar_vehiculos()
   
    # Verificar si ya existe un vehículo con el mismo código
    for v in vehiculos:
        if v["codigo"] == codigo:
            print("\n (❌) Ya existe un vehículo con ese código")
            return
    # Crear un diccionario con los datos del vehículo y guardarlo
    vehiculo = {
        "codigo": codigo,
        "marca": marca,
        "modelo": modelo,
        "anio": anio
    }

    vehiculos.append(vehiculo)
    guardar_vehiculos(vehiculos)
    print("\n ( ✔️ ) Vehículo registrado exitosamente.")

def listar_vehiculos():
    
    #Lista todos los vehículos registrados y guarda la lista en un archivo de texto
    #si no hay vehículos, muestra un mensaje indicándolo.
    
    vehiculos = cargar_vehiculos()
    if not vehiculos:
        print("\n (❌) No hay vehículos registrados.")
    else:
        print("\n--- Vehículos en exhibición ---")# Imprimir los detalles de cada vehículo
        for v in vehiculos:
            print("\n           ﹔🚖﹒info ﹗")
            print(f"c͟o͟d͟i͟g͟o͟: {v['codigo']}, m͟a͟r͟c͟a͟: {v['marca']}, m͟o͟d͟e͟l͟o͟: {v['modelo']}, 🕑 Año: {v['anio']}")

    # Guardar el listado en un archivo
    with open("listado_vehiculos.txt", "w") as file:
        for v in vehiculos:
            print("\n           ﹔🚖﹒info ﹗")
            file.write(f"c͟o͟d͟i͟g͟o͟: {v['codigo']}, m͟a͟r͟c͟a͟: {v['marca']}, m͟o͟d͟e͟l͟o͟: {v['modelo']}, 🕑 Año: {v['anio']}\n")
    print("\n ( ✔️ ) Listado guardado exitosamente ")
