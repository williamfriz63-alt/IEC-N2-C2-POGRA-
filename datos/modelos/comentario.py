from datos.conexion import base_datos
from peewee import Model, AutoField, TextField, DateField, ForeignKeyField
from datos.modelos.lector import Lector
from datos.modelos.noticia import Noticia

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Comentario(BaseModel):
    id_comentario = AutoField()
    contenido = TextField()
    fecha = DateField(null=True)
    lector = ForeignKeyField(Lector, backref='comentarios', index=True)
    noticia = ForeignKeyField(Noticia, backref='comentarios', index=True)

    class Meta:
        table_name = 'comentarios'