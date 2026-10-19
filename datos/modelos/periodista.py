from datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField, SQL
from datos.modelos.usuario import Usuario  # O si prefieres usar ForeignKeyField

database = base_datos()
defecto = "DEFAULT 1"

class BaseModel(Model):
    class Meta:
        database = database

class Periodista(BaseModel):
    id_periodista = AutoField()
    usuario = IntegerField(index=True)  # O ForeignKeyField(Usuario, index=True)
    especialidad = CharField(max_length=100, null=True)
    rut = CharField(max_length=12, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'periodistas'