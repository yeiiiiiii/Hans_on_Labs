import json

def cargar_vehiculos():
    try:
        with open("vehiculos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_vehiculos(vehiculos):
    with open("vehiculos.json", "w") as file:
        json.dump(vehiculos, file, indent=4)

def validaciones_codigos(codigo):
    try:
        codigo_num = int(codigo)
        if codigo_num < 0:
            print('No se permiten códigos negativos.')
            return False
        return True
    except ValueError:
        print('El código debe contener solo números.')
        return False
    
def registrar_vehiculo():

    print("Ingrese el código del vehículo")
    codigo=input("--> ")
    if not validaciones_codigos(codigo):
        return
    print("Ingrese la marca del vehículo")
    marca=input("--> ")
    print("Ingrese el modelo del vehículo")
    modelo=input("--> ")
    
    try:
        print("Ingrese el año de lanzamiento del vehículo")
        anio = int(input())
    except ValueError:
        print("El año debe ser un número entero.")
        return

    vehiculos = cargar_vehiculos()
    
    for v in vehiculos:
        if v["codigo"] == codigo:
            print("Ya existe un vehículo con ese código")
            return

    vehiculo = {
        "codigo": codigo,
        "marca": marca,
        "modelo": modelo,
        "anio": anio
    }

    vehiculos.append(vehiculo)
    guardar_vehiculos(vehiculos)
    print("Vehículo registrado exitosamente.")

def listar_vehiculos():
    vehiculos = cargar_vehiculos()
    if not vehiculos:
        print("No hay vehículos registrados.")
    else:
        print("\n--- Vehículos en exhibición ---")
        for v in vehiculos:
            print(f"Código: {v['codigo']}, Marca: {v['marca']}, Modelo: {v['modelo']}, Año: {v['anio']}")

    # Guardar el listado en un archivo
    with open("listado_vehiculos.txt", "w") as file:
        for v in vehiculos:
            file.write(f"Código: {v['codigo']}, Marca: {v['marca']}, Modelo: {v['modelo']}, Año: {v['anio']}\n")
    print("Listado guardado exitosamente ")
