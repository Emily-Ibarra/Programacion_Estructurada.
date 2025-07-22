
peliculas= []

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")

def agregarPeliculas():
    borrarPantalla()
    print("\n\t\t.::Agregar Películas::.\n\t")
    peliculas.append(input("\nIngresa el nombre: ").upper().strip())
    print("\n\t:::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!\n\t")
def consultarPeliculas():
    borrarPantalla()
    print("\n\t\t.::Consultar o Mostrar TODAS las Películas::.\n\t")
    if len(peliculas) > 0:
        for i in range(0, len(peliculas)):
            print(f"\n\t{i+1}: {peliculas[i]}")
    else:
        print("\n\t.::No hay películas en el sistema::.\n\t")

def vaciarPeliculas():
    borrarPantalla()
    print("\n\t\t.::Limpiar o Borrar TODAS las Películas::.\n\t")
    resp = input("¿Deseas borrar todas las películas? (Si/No)\n\t").lower()
    if resp == "si":
        peliculas.clear()
        print("\n\t:::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!:::\n\t")
def borrarPelicula():
    borrarPantalla()
    print("\n\t\t.::Borrar Una Película::.\n\t")
    peliculabuscar = input("\n\t\t.::Dame el nombre de la película a borrar::.\n\t").upper().strip()
    if peliculabuscar in peliculas:
        resp = input("\n\t\t.::Se encontró la película::.\n\t\t.::¿Está seguro de borrar el registro de la película? (Si/No)::.\n\t").upper().strip()
        if resp == "SI":
            peliculas.remove(peliculabuscar)
            print(f"\n\tLa película se borró con éxito")
    else:
        print("\n\t.::No se encontró alguna película con este nombre, lo siento::.\n\t")