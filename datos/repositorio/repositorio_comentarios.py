from datos.conexion import base_datos
from datos.modelos.comentario import Comentario
from datos.auxiliar import mensaje_error_orm

database = base_datos()

def listado_comentarios_por_noticia(id_noticia):
    try:
        # Busca los comentarios asociados a una noticia específica
        comentarios = Comentario.select().where(Comentario.noticia == id_noticia)
        return comentarios
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def guardar_comentario(comentario: Comentario):
    try:
        comentario_nuevo = comentario.save()
        return comentario_nuevo
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def eliminar_comentario(id_comentario):
    try:
        comentario = Comentario[id_comentario]
        if comentario:
            comentario.delete_instance()
            return True
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')