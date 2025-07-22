""" 
lista=[
       ["Ruben",10.0,8.9,9.2]
       ["Andres",10.0,10.0,10.0]
       ["Maria",10.0,10.0,10.0]
      ]       
"""
 
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Oprima cualquier tecla para continuar")

def menu_principal():
    print("Sistema de Gestión de calificaciones :::...\n1.Agregar \n2.Mostrar \n3.Calcular el promedio \n4.-buscar \n5.-SALIR")
    opcion = input("Elige una opción (1-4): ")
    return opcion

#nombre y 4 calificaciones
def agregar_calificaciones(lista):
    borrarPantalla()
    print("Agregar Calificaciones")
    nombre = input("Nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
     bandera=True
     while bandera:
        try:
          cal=float(input(f"Calificacion {i}: "))
          if cal>=0 and cal<=10:
           calificaciones.append(cal)
           bandera=False
          else:
           print("Ingrese un valor comprendido entre el 0 y 10")
        except ValueError:
         print("Ingresa un valor numerico")
    lista.append([nombre]+calificaciones)
    print("Accion realizada con exito")

def mostrar_calificaciones(lista):
   borrarPantalla()
   print("Mostar Calificaciones")
   if len(lista)>0:
     print(f"{"Nombre":<15}{"Calif.1":<10}{"Calif.2":<10}{"Calif.3":<10}   ")
     print("-"*50)
     for fila in lista:
       print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
     print("-"*50)
     print(f"Son {len(lista)} alumnos")
   else:
     print("No hay calificaciones en el sistema")

def calcular_promedios(lista):
    borrarPantalla()
    print("Promedios de Alumnos")
    promedio_Total=0
    alumnos=0
    if len(lista)>0:
        print(f"{"Nombre" :<15}{"Promedio":<10}")
        print("-"*30)
        for fila in lista:
          promedio=((fila[1])+(fila[2])+(fila[3]))/3
          print(f"{fila[0]:<15}{promedio:<10}")
          promedio_Total+=promedio
          alumnos+=1
          promedio_clase=promedio_Total/alumnos
        print("-"*30)
        print(f"El promedio del grupo es: {promedio_clase}")
    else:
        print("No hay calificaiones en el sistema")

def buscar_alumno(lista):
    borrarPantalla()
    print("Buscar Alumno")
    nombre = input("Nombre del alumno a buscar: ").upper().strip()
    encontrado = False
    for fila in lista:
        if fila[0] == nombre:
            print(f"Calificaciones de {nombre}: {fila[1]}, {fila[2]}, {fila[3]}")
            encontrado = True
            break
    if not encontrado:
        print(f"No se encontró alumno con el nombre '{nombre}'")
