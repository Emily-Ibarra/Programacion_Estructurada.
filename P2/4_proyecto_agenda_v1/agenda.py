import os

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t\t🔹 Oprima cualquier tecla para continuar...")

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

def agregar_contacto(agenda):
    borrarPantalla()
    print("➕ Agregar Contacto")

    nombre = input("👤 Nombre: ").strip().upper()
    telefono = input("📞 Teléfono: ").strip()
    correo = input("\📧 Correo: ").strip().lower()
    domicilio = input("🏠 Domicilio: ").strip().upper()

    if nombre in agenda:
        print("\t\❗ Este contacto ya existe")
    else:
        agenda[nombre] = {
            "telefono": telefono,
            "correo": correo,
            "domicilio": domicilio
        }
        print("\t✅ Acción Realizada con éxito")

def mostrar_contacto(agenda):
    borrarPantalla()
    print("📋 Lista de Contactos")

    if not agenda:
        print("📭 No hay contactos en la Agenda")
    else:
        print("\n\t{:<5} {:>20} {:>15} {:>25} {:>20}".format("No.", "Nombre", "Teléfono", "Correo", "Domicilio"))
        print("\t\t" + "-" * 90)
        for i, (nombre, datos) in enumerate(agenda.items(), start=1):
            print("\t\t{:<5} {:>20} {:>15} {:>25} {:>20}".format(
                i, nombre, datos["telefono"], datos["correo"], datos["domicilio"]
            ))
        print("" + "-" * 90)

def buscar_contacto(agenda):
    borrarPantalla()
    print("\t\t🔍 Buscar Contacto")

    if not agenda:
        print("📭 No hay contactos en la Agenda")
    else:
        nombre = input("👤 Nombre del contacto a buscar: ").strip().upper()
        encontrados = {n: d for n, d in agenda.items() if nombre in n}

        if encontrados:
            for nombre, datos in encontrados.items():
                print(f"\n\t📇 Nombre: {nombre}")
                print(f"\t📞 Teléfono: {datos['telefono']}")
                print(f"\t📧 E-mail: {datos['correo']}")
                print(f"\t🏠 Domicilio: {datos['domicilio']}")
        else:
            print("\t❗ Este contacto no existe")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("🗑️ Eliminar Contacto")

    if not agenda:
        print("\t\t📭 No hay contactos en la Agenda")
    else:
        nombre = input("\t\t👤 Nombre del contacto a buscar: ").strip().upper()
        if nombre in agenda:
            datos = agenda[nombre]
            print(f"\n\t📇 Nombre: {nombre}")
            print(f"\t📞 Teléfono: {datos['telefono']}")
            print(f"\t📧 E-mail: {datos['correo']}")
            print(f"\t🏠 Domicilio: {datos['domicilio']}")
            resp = input("\t❓ ¿Deseas eliminar los valores? (Sí/No): ").lower().strip()
            if resp == "si":
                agenda.pop(nombre)
                print("\t✅ Acción Realizada con éxito")
        else:
            print("\t❗ Este contacto no existe")

def modificar_contacto(agenda):
    borrarPantalla()
    print("\t✏️ Modificar Contacto")

    if not agenda:
        print("\t📭 No hay contactos en la Agenda")
    else:
        nombre = input("\t\t👤 Nombre del contacto a buscar: ").strip().upper()
        if nombre in agenda:
            datos = agenda[nombre]
            print(f"\n\t📇 Nombre: {nombre}")
            print(f"\t📞 Teléfono: {datos['telefono']}")
            print(f"\t📧 E-mail: {datos['correo']}")
            print(f"\t🏠 Domicilio: {datos['domicilio']}")
            resp = input("\t❓ ¿Deseas cambiar los valores? (Sí/No): ").lower().strip()
            if resp == "si":
                nuevo_tel = input("\t📞 Teléfono: ").strip()
                nuevo_email = input("\t📧 E-mail: ").strip().lower()
                nuevo_dom = input("\t🏠 Domicilio: ").strip().upper()
                agenda[nombre] = {
                    "telefono": nuevo_tel,
                    "correo": nuevo_email,
                    "domicilio": nuevo_dom
                }
                print("\t✅ Acción Realizada con éxito")
        else:
            print("\t❗ Este contacto no existe")
