""" proyecto-3
# -Crear-un-proyecto que permita Gestionar (Administrar) calificaciones, colocar un-menu-de-opciones para agregar, 
# mostrar y calcular el promedio de calificaciones..
# Notas:
# 1.--Utilizar funciones y mandar llamar desde otro archivo
# 2.--Utilizar lista para almacenar el nombre y 3 califciaciones de los alumnos
"""

import calificaciones

def main():
    opcion = True
    datos = []
    
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperarTecla()
            case "4":
                calificaciones.buscar_alumno(datos)
                calificaciones.esperarTecla()
            case "5":
                opcion = False
                calificaciones.borrarPantalla()
                print("Terminaste la ejecución del SW")
            case _:
                input("Opción inválida, vuelva a intentarlo... por favor")

if __name__ == "__main__":
    main()
