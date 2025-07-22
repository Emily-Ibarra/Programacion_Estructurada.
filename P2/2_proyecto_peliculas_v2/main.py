"""# proyecto-1-
# -Crear-un-proyecto que permita Gestionar (Administrar) peliculas, colocar un-menu-de-opciones para agregar, eliminar, modificar-y-consultar-peliculas..
# Notas:
# 1.--Utilizar funciones y mandar llamar desde otro archivo
# 2.--Utilizar dict para almacenar los siguientes atributos: (nombre, categoria, clasificacion, genero, idioma)
# de las peliculas
"""

import peliculas

opcion = True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON:::....\n\t\t..::: Sistema de Gestión de Peliculas.:::...\n\n\t\t-1.--Crear--\n\t\t-2.--Borrar--\n\t\t-3.--Mostrar--\n\t\t-4.--Agregar Caracteristicas--\n\t\t-5.--Modificar Caracteristicas--\n\t\t-6.--Borrar Caracteristicas--\n\t\t-7.--SALIR--")
    opcion = input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.agregarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion = False
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            opcion = True
            input("\n\tOpción inválida, vuelva a intentarlo.... por favor")
