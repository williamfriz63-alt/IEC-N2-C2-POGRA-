from datos.conexion import base_datos
from datos.modelos.noticia import Noticia
from datos.auxiliar import mensaje_error_orm

database = base_datos()

def listado_noticias():
    try:
        # Trae todas las noticias con estado 'publicada' o activas
        noticias = Noticia.select().where(Noticia.estado == 'publicada')
        return noticias
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def guardar_noticia(noticia: Noticia):
    try:
        noticia_nueva = noticia.save()
        return noticia_nueva
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def noticia_por_titulo(titulo):
    try:
        # Busca noticias cuyo título contenga el texto buscado
        noticias = Noticia.select().where(Noticia.titulo.contains(titulo))
        if noticias:
            return noticias
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def noticia_por_id(id_noticia):
    try:
        noticia = Noticia[id_noticia]
        if noticia:
            return noticia
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')