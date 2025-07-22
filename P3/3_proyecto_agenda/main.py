import agenda

def main():
    opcion = True

    while opcion:
        agenda.borrarPantalla()
        opcion = agenda.menu_principal()
        if opcion == "1":
            agenda.agregar_contacto()
            agenda.esperarTecla()
        elif opcion == "2":
            agenda.mostrar_contacto()
            agenda.esperarTecla()
        elif opcion == "3":
            agenda.buscar_contacto()
            agenda.esperarTecla()
        elif opcion == "4":
            agenda.eliminar_contacto()
            agenda.esperarTecla()
        elif opcion == "5":
            agenda.modificar_contacto()
            agenda.esperarTecla()
        elif opcion == "6":
            agenda.borrarPantalla()
            print("Terminaste la ejecución del SW")
            opcion = False
        else:
            input("Opción inválida, vuelva a intentarlo... por favor")

if __name__ == "__main__":
    main()
