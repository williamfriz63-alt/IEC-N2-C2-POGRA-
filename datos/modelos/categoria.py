from datos.conexion import base_datos
from peewee import Model, AutoField, CharField, TextField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre = CharField(max_length=100)
    descripcion = TextField(null=True)

    class Meta:
        table_name = 'categorias'
        