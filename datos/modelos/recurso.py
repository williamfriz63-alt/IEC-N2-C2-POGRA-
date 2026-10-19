from datos.conexion import base_datos
from peewee import Model, AutoField, CharField, ForeignKeyField
from datos.modelos.noticia import Noticia

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Recurso(BaseModel):
    id_recurso = AutoField()
    url = CharField(max_length=255)
    tipo = CharField(max_length=50)
    noticia = ForeignKeyField(Noticia, index=True)

    class Meta:
        table_name = 'recursos'