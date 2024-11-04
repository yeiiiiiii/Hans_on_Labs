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
            print('\n (❌) No se permiten códigos negativos.')
            return False
        return True
    except ValueError:
        print('\n (❌) El código debe contener solo números.')
        return False
    
def registrar_vehiculo():

    codigo=input("\n ➔ Ingrese el c͟o͟d͟i͟g͟o͟ del vehículo ( 🏷️ ) : ")
    if not validaciones_codigos(codigo):
        return
    marca=input("\n ➔ Ingrese la m͟a͟r͟c͟a͟ del vehículo ( 📦 ) : ")
    modelo=input("\n ➔ Ingrese el m͟o͟d͟e͟l͟o͟ del vehículo ( 🛒 ) : ")
    
    try:
        print("\n ➔ Ingrese el año de lanzamiento del vehículo ( 🗓️ ) : ")
        anio = int(input())
    except ValueError:
        print("\n (❌) El año debe ser un número entero.")
        return

    vehiculos = cargar_vehiculos()
    
    for v in vehiculos:
        if v["codigo"] == codigo:
            print("\n (❌) Ya existe un vehículo con ese código")
            return

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
    vehiculos = cargar_vehiculos()
    if not vehiculos:
        print("\n (❌) No hay vehículos registrados.")
    else:
        print("\n--- Vehículos en exhibición ---")
        for v in vehiculos:
            print("\n           ﹔🚖﹒info ﹗")
            print(f"c͟o͟d͟i͟g͟o͟: {v['codigo']}, m͟a͟r͟c͟a͟: {v['marca']}, m͟o͟d͟e͟l͟o͟: {v['modelo']}, 🕑 Año: {v['anio']}")

    # Guardar el listado en un archivo
    with open("listado_vehiculos.txt", "w") as file:
        for v in vehiculos:
            print("\n           ﹔🚖﹒info ﹗")
            file.write(f"c͟o͟d͟i͟g͟o͟: {v['codigo']}, m͟a͟r͟c͟a͟: {v['marca']}, m͟o͟d͟e͟l͟o͟: {v['modelo']}, 🕑 Año: {v['anio']}\n")
    print("\n ( ✔️ ) Listado guardado exitosamente ")
