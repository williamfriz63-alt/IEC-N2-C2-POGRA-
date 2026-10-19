from datos.conexion import base_datos
from peewee import Model, AutoField, DateField, IntegerField, SQL
# Opcional: puedes relacionarlo con Usuario si tienes la clase creada
database = base_datos()
defecto = "DEFAULT 1"

class BaseModel(Model):
    class Meta:
        database = database

class Lector(BaseModel):
    id_lector = AutoField()
    usuario = IntegerField(index=True)
    fecha_registro = DateField(null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'lectores'