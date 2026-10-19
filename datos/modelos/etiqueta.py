from datos.conexion import base_datos
from peewee import Model, AutoField, CharField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Etiqueta(BaseModel):
    id_etiqueta = AutoField()
    nombre = CharField(max_length=50)

    class Meta:
        table_name = 'etiquetas'