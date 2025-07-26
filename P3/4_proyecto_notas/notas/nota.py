from conexionBD import *

def crear(usuario_id,titulo,descripcion):
    try:
        cursor.execute("insert into notas (usuario_id,titulo,descripcion,fecha) value(%s,%s,%s,NOW())",(usuario_id,titulo,descripcion))
        conexion.commit()
        return True
    except:
        return False  

def mostrar(usuario_id):
    try:
       cursor.execute("select * from notas where usuario_id=%s",(usuario_id,))
       return cursor.fetchall() 
    except:
       return []

def cambiar(id,titulo,descripcion):
    try:
        cursor.execute("update notas set titulo=%s,descripcion=%s,fecha=now() where id=%s",(titulo,descripcion,id))
        conexion.commit()
        return True
    except:
        return False
    
def borrar(id):
    try:
        cursor.execute("delete from notas where id=%s",(id,))
        conexion.commit()
        return True
    except:
        return False

