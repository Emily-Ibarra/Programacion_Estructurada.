""" 
crear un proyecto que permita adeministar peliculas colocar un menu de opciones para agregar, 
eliminar, modificar, consulatar, buscar y basicar peliculas. 
notas: 
1.- utilizar funciones y llamar desde otro archivo 
2.- utilizar listas para almacenar los nombres de las pelciulas 

"""
import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar  \n\t\t 2.- Borrar \n\t\t 3.- Modificar \n\t\t 4.- Mostrar \n\t\t 5.- Buscar \n\t\t 6.- Limpiar \n\t\t 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPelicula()
            peliculas.esperarTecla()
        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.consultarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion = False    
            peliculas.borrarPantalla()
            print("\n\t\t\ Terminaste la ejecución del sistema.")
        case _:
            opcion=True
            input("Opción inválida, vuelva a intentarlo... Presione Enter.")