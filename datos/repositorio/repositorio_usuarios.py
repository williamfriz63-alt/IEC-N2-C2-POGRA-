from datos.conexion import base_datos
from datos.modelos.usuario import Usuario
from datos.auxiliar import mensaje_error_orm

database = base_datos()

def listado_usuarios():
    try:
        usuarios = Usuario.select()
        return usuarios
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def guardar_usuario(usuario: Usuario):
    try:
        usuario_nuevo = usuario.save()
        return usuario_nuevo
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def usuario_por_email(email):
    try:
        usuario = Usuario.select().where(Usuario.email == email).first()
        if usuario:
            return usuario
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def usuario_por_id(id_usuario):
    try:
        usuario = Usuario[id_usuario]
        if usuario:
            return usuario
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')