from modulos.ventas_reporte import*
from modulos.registros_lista import*
def menu():

    while True:
        print(" . . . . . . . . . 𝗠𝗲𝗻𝘂 𝗣𝗿𝗶𝗻𝗰𝗶𝗽𝗮𝗹 . . . . . . . . . ")
        print(" . 𝟏. Registrar vehículo en exhibición            . ")
        print(" . 𝟐. Registrar venta diaria                      . ")
        print(" . 𝟑. Lista de vehículos en exhibición            . ")
        print(" . 𝟒. Reporte de ventas por mes                   . ")
        print(" . 𝟓. Salir                                       . ")
        print(" . . . . . . . . . . . . . . . . . . . . . . . . .  ")
        print(" . Seleccione una opción")
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
