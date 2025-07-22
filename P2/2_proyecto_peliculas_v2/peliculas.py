"""dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)
pelicula = {
    "nombre": "",
    "categoria": "",
    "clasificacion": "",
    "genero": "",
    "idioma": ""
}
"""

pelicula = {}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")
    
def crearPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Películas ::.\n")
    pelicula.update({"nombre": input("Ingresa el nombre: ").upper().strip()})
    #pelicula["nombre"]=input("\n Ingresa el nombre:").upper().strip
    pelicula.update({"categoria": input("Ingresa la categoría: ").upper().strip()})
    pelicula.update({"clasificacion": input("Ingresa la clasificación: ").upper().strip()})
    pelicula.update({"genero": input("Ingresa el género: ").upper().strip()})
    pelicula.update({"idioma": input("Ingresa el idioma: ").upper().strip()})
    input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o Mostrar la Película ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i}: {pelicula[i]}")
    else:
        print("\t..:: No hay películas en el sistema ::..\n")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar o Quitar TODAS las Películas ::.\n")
    if len(pelicula)>0:
       resp = input("¿Deseas quitar o borrar todas las películas del sistema? (Si/No): ").lower().strip()
    if resp == "si":
        pelicula.clear()
        input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    else:
        print("\t ..:: No hay peliculas en el sistema ::.. ")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Característica a Películas ::.\n")
    atributo = input("Ingresa el nombre de la nueva característica a la película: ").lower().strip()
    valor_atributo = input("Ingresa el valor de la nueva característica de la película: ").upper().strip()
    #pelicula.update({atributo:valor_atributo})
    pelicula[atributo]=valor_atributo
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    
""" 1-.borrar pantalla. 2-.modifica el valor de algo que ya existe los valores actuales son nombre nombre 3-.desas
 modificar el valor de la caracteristica nombre con si o no depues 4-.ingresa ahora el nuevo valor 5-.operacion
   realizada con exito y 6-.continua con la siguiente caracteristcia """
def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Característica de Películas ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
         print(f"\t{i}: {pelicula[i]}")
        resp = input(f"¿Deseas modificar el valor de la caracteristica de: {i} ? (Si/No): ").lower().strip()
        if resp == "si":
         pelicula[i] = input(f"\nIngresa el nuevo valor de la caracteristcia {i}: ").upper().strip()
         print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
        else:
            print("\n\t\t::: La característica no existe :::")
    else:
        print("\t..:: No hay películas en el sistema ::..")


#
def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar Característica de Películas ::.\n")
    print("valores actuales:")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i}: {pelicula[i]}")
        resp = input(f"¿Deseas borrar alguna caracteristica? (Si/No): ").lower().strip()
        if resp == "si":
         atributo = input("\nIngresa el nombre de la característica que deseas borrar: ").lower().strip()
         if atributo in pelicula:
            del pelicula[atributo]
            print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
         else:
            print("\n\t\t::: La característica no existe :::")
    else:
        print("\t..:: No hay películas en el sistema ::..")




