from datos.conexion import base_datos
from datos.modelos.categoria import Categoria

database = base_datos()

def listado_categorias():
    listado_categorias = Categoria.select()
    return listado_categorias

def obtener_categoria_nombre():
    print('GG')

def guardar_categoria():
    print('GG')

def actualizar_categoria():
    print('GG')

def eliminar_categoria():
    print('GG')