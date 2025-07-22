#proyecto 1 
# Crear un proyecto que permita Gestionar (Administrar) peliculas, colocar un menu de opciones para agregar, eliminar, modificar,consultar y buscar peliculas. 

#Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar una dict para almacenar los atributos o caracteristicas (nombre,categoria,clasificacion,genero,idioma) de las peliculas
# 3.- Utilizar e implementar una BD relacional en MySQL  

import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Buscar \n\t\t 5.- Modificar \n\t\t 6.- SALIR ")
    opcion=input("\n\t\t Elige una opción: ").upper()

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
            peliculas.buscarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "6":
            opcion=False  
            peliculas.borrarPantalla()  
            print("\n\t\tTerminaste la ejecucion del SW")
        case _: 
            opcion=True
            input("\n\t\tOpción invalida vuelva a intentarlo ... por favor") 
             