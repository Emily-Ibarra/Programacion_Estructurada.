import funciones
from usuarios import usuario
from notas import nota
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            # password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            regresar=usuario.registrar(nombre,apellidos,email,password)
            if regresar:
                print(f"{nombre} {apellidos} se registro correctamente con el e-mail: {email}")
            else:
                print(f"Por favor intentelo de nuevo ... no fue posible realizar el registro en este momento ...")    
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            lista_usuario=usuario.iniciar_sesion(email,password)
            if lista_usuario:
               menu_notas(lista_usuario[0],lista_usuario[1],lista_usuario[2])
            else:
                print(f"...El E-mail y/o contraseña son incorrectos ... por favor intentalo nuevamente")
                funciones.esperarTecla()   
              
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respuesta=nota.crear(usuario_id,titulo,descripcion)
            if respuesta:
                print(f"Se creo la nota {titulo} con exito")
            else:
                print(f"No fue posible crear la nota, intentalo nuevamente ...")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print(f"\n\tMostrar las Notas")
                print(f"{'ID':<10}{'Titulo':<15}{'Descripción':<30}{'Fecha':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                  print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<30}{fila[4]}")
                print(f"-"*80)
            else:
                print(f"\n\t..No existen notas para este usuario ..")      
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print(f"\n\tMostrar las Notas")
                print(f"{'ID':<10}{'Titulo':<15}{'Descripción':<30}{'Fecha':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                  print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<30}{fila[4]}")
                print(f"-"*80)
                resp = input("¿Deseas cambiar alguna nota? (Si/No)").lower()
                if resp == "si":    
                    print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
                    id = input("\t \t ID de la nota a actualizar: ")
                    titulo = input("\t Nuevo título: ")
                    descripcion = input("\t Nueva descripción: ")
                    #Agregar codigo
                    respuesta=nota.cambiar(id,titulo,descripcion)
                    if respuesta:
                        print(f"Se actualizo la nota {titulo} con exito")
                    else:
                        print(f"No fue posible actualizar la nota, intentalo nuevamente ...")
            else:
                print(f"\n\t..No existen notas para este usuario ..")
        elif opcion == '4' or opcion=="borrar":
            funciones.borrarPantalla()
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print(f"\n\tMostrar las Notas")
                print(f"{'ID':<10}{'Titulo':<15}{'Descripción':<30}{'Fecha':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                  print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<30}{fila[4]}")
                print(f"-"*80)
                resp = input("¿Deseas borrar alguna nota? (Si/No)").lower()
                if resp == "si":    
                  print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
                  id = input("\t \t ID de la nota a eliminar: ")
                  #Agregar codigo
                  respuesta=nota.borrar(id)
                  if respuesta:
                    print(f"Se borro la nota {id} con exito")
                  else:
                    print(f"No fue posible borrar la nota, intentalo nuevamente ...")
            else:
                print(f"\n\t..No existen notas para este usuario ..")
            funciones.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


