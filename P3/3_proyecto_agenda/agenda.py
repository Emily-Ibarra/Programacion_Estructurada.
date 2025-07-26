import os
import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t\t🔹 Oprima cualquier tecla para continuar...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",  
            database="bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def menu_principal():
    print("\n" + "=" * 70)
    print("\t\t📇  SISTEMA DE GESTIÓN DE CONTACTOS 📇")
    print("=" * 70)
    print("\n\t\t1 - ➕ Agregar Contacto")
    print("\t\t2 - 📋 Mostrar Todos los Contactos")
    print("\t\t3 - 🔍 Buscar Contacto")
    print("\t\t4 - 🗑️ Eliminar Contacto")
    print("\t\t5 - ✏️ Modificar Contacto")
    print("\t\t6 - 🚪 Salir")
    print("\n" + "=" * 70)
    return input("\t\t🔹 Elige una opción (1-6): ").strip()

def agregar_contacto():
    borrarPantalla()
    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return
    
    print("➕ Agregar Contacto")
    nombre = input("👤 Nombre: ").strip().upper()
    telefono = input("📞 Teléfono: ").strip()
    correo = input("📧 Correo: ").strip().lower()
    domicilio = input("🏠 Domicilio: ").strip().upper()

    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO contactos (nombre, telefono, correo, domicilio) VALUES (%s, %s, %s, %s)"
        val = (nombre, telefono, correo, domicilio)
        cursor.execute(sql, val)
        conexion.commit()
        print("\t✅ Contacto agregado con éxito.")
    except mysql.connector.IntegrityError:
        print("\t❗ El contacto ya existe.")
    except Error as e:
        print(f"Error al agregar contacto: {e}")
    finally:
        cursor.close()
        conexion.close()

def mostrar_contacto():
    borrarPantalla()
    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM contactos")
        registros = cursor.fetchall()
        
        if registros:
            print("📋 Lista de Contactos\n")
            print(f"{'ID':<5} {'Nombre':<20} {'Teléfono':<15} {'Correo':<30} {'Domicilio':<25}")
            print("-" * 95)
            for reg in registros:
                print(f"{reg[0]:<5} {reg[1]:<20} {reg[2]:<15} {reg[3]:<30} {reg[4]:<25}")
        else:
            print("📭 No hay contactos en la agenda.")
    except Error as e:
        print(f"Error al mostrar contactos: {e}")
    finally:
        cursor.close()
        conexion.close()

def buscar_contacto():
    borrarPantalla()
    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return
    
    nombre = input("👤 Nombre del contacto a buscar: ").strip().upper()

    try:
        cursor = conexion.cursor()
        sql = "SELECT * FROM contactos WHERE nombre LIKE %s"
        val = ("%" + nombre + "%",)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        
        if registros:
            print(f"\n📇 Resultados para '{nombre}':\n")
            print(f"{'ID':<5} {'Nombre':<20} {'Teléfono':<15} {'Correo':<30} {'Domicilio':<25}")
            print("-" * 95)
            for reg in registros:
                print(f"{reg[0]:<5} {reg[1]:<20} {reg[2]:<15} {reg[3]:<30} {reg[4]:<25}")
        else:
            print("\t❗ No se encontró el contacto.")
    except Error as e:
        print(f"Error al buscar contacto: {e}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_contacto():
    borrarPantalla()
    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return
    
    nombre = input("👤 Nombre del contacto a eliminar: ").strip().upper()

    try:
        cursor = conexion.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registro = cursor.fetchone()
        
        if registro:
            print(f"\n📇 Nombre: {registro[1]}")
            print(f"📞 Teléfono: {registro[2]}")
            print(f"📧 Correo: {registro[3]}")
            print(f"🏠 Domicilio: {registro[4]}")
            resp = input("\n❓ ¿Deseas eliminar este contacto? (Sí/No): ").lower().strip()
            if resp == "si":
                sql_delete = "DELETE FROM contactos WHERE id = %s"
                cursor.execute(sql_delete, (registro[0],))
                conexion.commit()
                print("\t✅ Contacto eliminado.")
        else:
            print("\t❗ El contacto no existe.")
    except Error as e:
        print(f"Error al eliminar contacto: {e}")
    finally:
        cursor.close()
        conexion.close()

def modificar_contacto():
    borrarPantalla()
    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return
    
    nombre = input("👤 Nombre del contacto a modificar: ").strip().upper()

    try:
        cursor = conexion.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registro = cursor.fetchone()

        if registro:
            print(f"\n📇 Nombre: {registro[1]}")
            print(f"📞 Teléfono: {registro[2]}")
            print(f"📧 Correo: {registro[3]}")
            print(f"🏠 Domicilio: {registro[4]}")
            resp = input("\n❓ ¿Deseas modificar este contacto? (Sí/No): ").lower().strip()
            if resp == "si":
                nuevo_nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ").strip().upper()
                nuevo_telefono = input("Nuevo teléfono (dejar en blanco para no cambiar): ").strip()
                nuevo_correo = input("Nuevo correo (dejar en blanco para no cambiar): ").strip().lower()
                nuevo_domicilio = input("Nuevo domicilio (dejar en blanco para no cambiar): ").strip().upper()

                # Si queda vacío, usar valor anterior
                if not nuevo_nombre:
                    nuevo_nombre = registro[1]
                if not nuevo_telefono:
                    nuevo_telefono = registro[2]
                if not nuevo_correo:
                    nuevo_correo = registro[3]
                if not nuevo_domicilio:
                    nuevo_domicilio = registro[4]

                sql_update = """
                    UPDATE contactos
                    SET nombre = %s, telefono = %s, correo = %s, domicilio = %s
                    WHERE id = %s
                """
                val_update = (nuevo_nombre, nuevo_telefono, nuevo_correo, nuevo_domicilio, registro[0])
                cursor.execute(sql_update, val_update)
                conexion.commit()
                print("\t✅ Contacto modificado.")
        else:
            print("\t❗ El contacto no existe.")
    except Error as e:
        print(f"Error al modificar contacto: {e}")
    finally:
        cursor.close()
        conexion.close()
