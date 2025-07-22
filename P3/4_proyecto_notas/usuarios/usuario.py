from conexionBD import *
import datetime

def registrar(nombre,apelldio,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        sql="insert into usuarios (nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s)"
        val=(nombre,apelldio,email,contrasena,fecha)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False
def iniciar_sesion(email,contrasena):
    try:
        fecha=datetime.datetime.now()
        sql="select * from usuarios "
        val=(email,contrasena)
        cursor.execute(sql,val)
        registro=cursor.fetchone()
        if registro:
             return registro
        else:
            return None
    except:
        return None