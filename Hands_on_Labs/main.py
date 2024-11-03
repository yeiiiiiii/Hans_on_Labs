from modulos.ventas_reporte import*
from modulos.registros_lista import*
def menu():

    while True:
        print("\n----- Menú Principal -----")
        print("1. Registrar vehículo en exhibición")
        print("2. Registrar venta diaria")
        print("3. Lista de vehículos en exhibición")
        print("4. Reporte de ventas por mes")
        print("5. Salir")
        print("Seleccione una opción")
        opcion=input("--> ")
        
        if opcion == '1':
            registrar_vehiculo()
        elif opcion == '2':
            registrar_venta()
        elif opcion == '3':
            listar_vehiculos()
        elif opcion == '4':
            generar_reporte_ventas()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no permitida, es del 1 al 5")

menu()
