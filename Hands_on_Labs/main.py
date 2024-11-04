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
            print("\n . . . . ﹒ᶻz﹒🚝﹒𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝗮𝗿 𝗩͟𝗲͟𝗵͟𝗶͟𝗰͟𝘂͟𝗹͟𝗼͟ ! . . . . . .")
            registrar_vehiculo()
        elif opcion == '2':
            print("\n . . . . ﹒ᶻz﹒💰﹒𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝗮𝗿 𝗩͟𝗲͟𝗻͟𝘁͟𝗮͟𝘀͟ ! . . . . . .")
            registrar_venta()
        elif opcion == '3':
            print("\n . . . . ﹒ᶻz﹒📝﹒𝗟𝗶𝘀𝘁𝗮𝗿 𝗩͟𝗲͟𝗵͟𝗶͟𝗰͟𝘂͟𝗹͟𝗼͟𝘀͟ ! . . . . . .")
            listar_vehiculos()
        elif opcion == '4':
            print("\n . . . . ﹒ᶻz﹒📇﹒𝗚𝗲𝗻𝗲𝗿𝗮𝗿 𝗥͟𝗲͟𝗽͟𝗼͟𝗿͟𝘁͟𝗲͟ ! . . . . . .")
            generar_reporte_ventas()
        elif opcion == '5':
            print("\n 🚪 . . . Saliendo del programa ")
            break
        else:
            print("\n (❌) Opción no permitida, es del 1 al 5")

menu()
