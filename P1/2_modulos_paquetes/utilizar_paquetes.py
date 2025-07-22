from paquete1 import modulos

print(modulos.saludar("Daniel Contreras Ruano"))

modulos.borrarPantalla()
nom,tel=modulos.solicitarDatos2()
print(f"\n\t.:: Agenda Telefonica ::. \n\t\t Telefono:{tel}")
modulos.espereTecla()