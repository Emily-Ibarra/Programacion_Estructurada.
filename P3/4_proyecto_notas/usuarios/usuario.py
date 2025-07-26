from conexionBD import *
import datetime
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre,apellidos,email,contrasena):
    try:
       fecha=datetime.datetime.now()
       contrasena=hash_password(contrasena)
       sql="insert into usuarios (nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s)"
       val=(nombre,apellidos,email,contrasena,fecha)
       cursor.execute(sql,val)
       conexion.commit()
       return True
    except:
        return False    
    
def iniciar_sesion(email,contrasena):
    try:
       contrasena=hash_password(contrasena)
       sql="select * from usuarios where email=%s and password=%s"
       val=(email,contrasena)
       cursor.execute(sql,val)
       registro=cursor.fetchone()
       if registro:
           return registro
       else:
           return None
    except:
        return None    