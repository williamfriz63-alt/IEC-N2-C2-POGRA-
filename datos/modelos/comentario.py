from peewee import *
from datos.conexion import db
from datos.modelos.noticia import Noticia  # Relación con la noticia
# Ajusta la importación del usuario/lector según cómo lo hayas nombrado en tus modelos

class BaseModel(Model):
    class Meta:
        database = db

class Comentario(BaseModel):
    id = AutoField(primary_key=True)
    contenido = TextField(null=False)
    fecha_publicacion = DateTimeField(null=False)
    noticia = ForeignKeyField(Noticia, backref='comentarios', on_delete='CASCADE')
    # Si vinculas directamente al usuario o lector:
    # usuario = ForeignKeyField(Usuario, backref='comentarios', on_delete='CASCADE')

    class Meta:
        table_name = 'comentario'