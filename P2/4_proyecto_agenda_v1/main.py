import agenda

def main():
    opcion = True
    agenda_contactos= {}

    while opcion:
        agenda.borrarPantalla()
        opcion = agenda.menu_principal()
        if opcion == "1":
            agenda.agregar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "2":
            agenda.mostrar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "3":
            agenda.buscar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "4":
            agenda.eliminar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "5":
            agenda.modificar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "6":
            agenda.borrarPantalla()
            print("Terminaste la ejecución del SW")
            opcion = False
        elif opcion == "7":
            agenda.borrarPantalla()
            print("Terminaste la ejecución del SW")
            opcion = False
        else:
            input("Opción inválida, vuelva a intentarlo... por favor")

if __name__ == "__main__":
    main()

