from modulos.ventas_reporte import*
from modulos.registros_lista import*
def menu():

    while True:
        print(" . . . . . . . . . 𝗠𝗲𝗻𝘂 𝗣𝗿𝗶𝗻𝗰𝗶𝗽𝗮𝗹 . . . . . . . . . . ")
        print(" . 𝟏. Registrar v͟e͟h͟i͟c͟u͟l͟o͟ en exhibición ( 🚘 )      . ")
        print(" . 𝟐. Registrar venta d͟i͟a͟r͟i͟a͟ ( 💸 )                . ")
        print(" . 𝟑. l͟i͟s͟t͟a͟ de vehículos en exhibición ( 📜 )      . ")
        print(" . 𝟒. Reporte de ventas por m͟e͟s͟ ( 📊 )             . ")
        print(" . 𝟓. Salir ( 🚫 )                                 . ")
        print(" . . . . . . . . . . . . . . . . . . . . . . . . . .  ")
        print(" . S͟e͟l͟e͟c͟c͟i͟o͟n͟e͟ u͟n͟a͟ o͟p͟c͟i͟o͟n͟ ! !")
        opcion=input(" ❓ = ")
        
        if opcion == '1':
            registrar_vehiculo()
        elif opcion == '2':
            registrar_venta()
        elif opcion == '3':
            listar_vehiculos()
        elif opcion == '4':
            generar_reporte_ventas()
        elif opcion == '5':
            print("🚪 . . . Saliendo del programa ")
            break
        else:
            print("Opción no permitida, es del 1 al 5")

menu()
