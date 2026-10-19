from datos.repositorio.repositorio_noticias import listado_noticias, guardar_noticia, noticia_por_titulo
from prettytable import PrettyTable
from datos.modelos.noticia import Noticia

def cargar_noticias(tabla: PrettyTable):
    noticias = listado_noticias()
    tabla.field_names = ['Id', 'Título', 'Fecha', 'Estado']

    if noticias:
        for noticia in noticias:
            tabla.add_row([noticia.id_noticia, noticia.titulo, noticia.fecha_publicacion, noticia.estado])

    return tabla

def buscar_noticias_por_titulo(tabla: PrettyTable, titulo):
    noticias = noticia_por_titulo(titulo)
    tabla.field_names = ['Id', 'Título', 'Fecha', 'Estado']

    if noticias:
        for noticia in noticias:
            tabla.add_row([noticia.id_noticia, noticia.titulo, noticia.fecha_publicacion, noticia.estado])

    return tabla

def crear_nueva_noticia(titulo, contenido, fecha_creacion, estado, periodista_id, categoria_id):
    nueva_noticia = Noticia()
    nueva_noticia.titulo = titulo
    nueva_noticia.contenido = contenido
    nueva_noticia.fecha_creacion = fecha_creacion
    nueva_noticia.estado = estado
    nueva_noticia.periodista = periodista_id
    nueva_noticia.categoria = categoria_id
    
    resultado = guardar_noticia(nueva_noticia)
    if resultado == 1:
        print(f'Se ha guardado la noticia "{nueva_noticia.titulo}" exitosamente.')