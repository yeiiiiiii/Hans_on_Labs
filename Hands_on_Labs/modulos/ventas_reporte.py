import json
from datetime import datetime
from modulos.registros_lista import cargar_vehiculos

def cargar_ventas():
        try:
            with open("ventas.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

def guardar_ventas(ventas):
        with open("ventas.json", "w") as file:
            json.dump(ventas, file, indent=4)

def registrar_venta():
    modelo=input("\n ➔ Por favor ingrese el m͟o͟d͟e͟l͟o͟ del vehículo vendido ( 🛒 ) : ")
    
    #Se cargan los modelos existentes 
    vehiculos = cargar_vehiculos()
    modelos_registrados = {v["modelo"] for v in vehiculos}

    #Se valida si el modelo existe en los modelos registrados
    if modelo not in modelos_registrados:
        print("\n (❌) Error: El modelo ingresado no está registrado.")
        return

    try:
        fecha = input("\n ➔ Ingrese la fecha de la venta por favor (YYYY-MM-DD) 📅 : ")
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        print("\n (❌) Fecha incorrecta, la fecha debe ser así: ejemplo (2024-10-23)")
        return

    try:
        print("\n ➔ Ingrese la c͟a͟n͟t͟i͟d͟a͟d͟ vendida ( 🗃️ ) : ")
        cantidad = int(input())
        if cantidad <= 0:
            print("\n (❌) La cantidad no debe ser negativa ni cero.")
            return
    except ValueError:
        print("\n (❌) La cantidad debe ser un número entero.")
        return

    ventas = cargar_ventas()
        
    venta = {
            "modelo": modelo,
            "fecha": fecha,
            "cantidad": cantidad
        }

    ventas.append(venta)
    guardar_ventas(ventas)
    print("\n (❌) Venta registrada exitosamente")


def generar_reporte_ventas():
        ventas = cargar_ventas()
        if not ventas:
            print("\n (❌) No hay ventas registradas.")
            return

        reporte_mensual = {}
        
        for venta in ventas:
            fecha = datetime.strptime(venta["fecha"], "%Y-%m-%d")
            mes_anio = fecha.strftime("%Y-%m")
            
            if mes_anio not in reporte_mensual:
                reporte_mensual[mes_anio] = {}
            
            if venta["modelo"] not in reporte_mensual[mes_anio]:
                reporte_mensual[mes_anio][venta["modelo"]] = 0
            
            reporte_mensual[mes_anio][venta["modelo"]] += venta["cantidad"]
        
        # Guardar el reporte en un archivo
        with open("reporte_ventas_mensual.txt", "w") as file:
            for mes_anio, modelos in reporte_mensual.items():
                print("\n           ﹔📋﹒reporte ﹗")
                file.write(f"--- Mes: {mes_anio} ---\n")
                for modelo, cantidad in modelos.items():
                    file.write(f"Modelo: {modelo}, Cantidad Vendida: {cantidad}\n")
                file.write("\n")
        
        print("\n ( ✔️ ) Reporte mensual de ventas generado exitosamente")

#