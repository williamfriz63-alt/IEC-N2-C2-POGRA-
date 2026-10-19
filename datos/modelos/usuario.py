from datos.conexion import base_datos
from peewee import Model, AutoField, CharField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Usuario(BaseModel):
    id_usuario = AutoField()
    nombre = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    contrasena = CharField(max_length=255)

    class Meta:
        table_name = 'usuarios'