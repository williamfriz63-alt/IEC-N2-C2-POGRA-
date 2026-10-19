from datos.conexion import base_datos
from datos.modelos.periodista import Periodista
from datos.modelos.categoria import Categoria
from peewee import Model, AutoField, CharField, TextField, DateField, ForeignKeyField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Noticia(BaseModel):
    id_noticia = AutoField()
    titulo = CharField(max_length=255)
    contenido = TextField()
    fecha_creacion = DateField(null=True)
    fecha_publicacion = DateField(null=True)
    estado = CharField(max_length=50)
    periodista = ForeignKeyField(Periodista, index=True)
    categoria = ForeignKeyField(Categoria, index=True, null=True)

    class Meta:
        table_name = 'noticias'