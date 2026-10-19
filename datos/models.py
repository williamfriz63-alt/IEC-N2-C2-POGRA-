from peewee import Model, CharField, DateField, AutoField, IntegerField, TextField, ForeignKeyField, SQL
from datos.conexion import conectar_db

database = conectar_db()
defecto = "DEFAULT 1"

class BaseModel(Model):
    class Meta:
        database = database

# ----------------------------------------------------------------------
# 1. USUARIOS Y SUS ROLES (Herencia de Usuario -> Periodista / Lector)
# ----------------------------------------------------------------------

class Usuario(BaseModel):
    id_usuario = AutoField()
    nombre = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    contrasena = CharField(max_length=255)

    class Meta:
        table_name = 'usuarios'

class Periodista(BaseModel):
    # Relación uno a uno / Herencia con Usuario
    usuario = ForeignKeyField(Usuario, backref='periodista_perfil', on_delete='CASCADE')
    especialidad = CharField(max_length=100)
    rut = CharField(max_length=12)

    class Meta:
        table_name = 'periodistas'

class Lector(BaseModel):
    # Relación uno a uno / Herencia con Usuario
    usuario = ForeignKeyField(Usuario, backref='lector_perfil', on_delete='CASCADE')
    fecha_registro = DateField()

    class Meta:
        table_name = 'lectores'

# ----------------------------------------------------------------------
# 2. CATEGORÍAS Y ETIQUETAS
# ----------------------------------------------------------------------

class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre = CharField(max_length=100)
    descripcion = TextField()

    class Meta:
        table_name = 'categorias'

class Etiqueta(BaseModel):
    id_etiqueta = AutoField()
    nombre = CharField(max_length=50)

    class Meta:
        table_name = 'etiquetas'

# ----------------------------------------------------------------------
# 3. NOTICIA Y RECURSOS
# ----------------------------------------------------------------------

class Noticia(BaseModel):
    id_noticia = AutoField()
    titulo = CharField(max_length=255)
    contenido = TextField()
    fecha_creacion = DateField()
    fecha_publicacion = DateField(null=True)
    estado = CharField(max_length=50)  # ej: 'borrador', 'en_revision', 'publicada'
    
    # Claves foráneas asociadas según tu UML
    periodista = ForeignKeyField(Periodista, backref='noticias_redactadas')
    categoria = ForeignKeyField(Categoria, backref='noticias', null=True)

    class Meta:
        table_name = 'noticias'

class Recurso(BaseModel):
    id_recurso = AutoField()
    url = CharField(max_length=255)
    tipo = CharField(max_length=50)  # ej: 'imagen', 'video', 'audio'
    noticia = ForeignKeyField(Noticia, backref='recursos')

    class Meta:
        table_name = 'recursos'

# ----------------------------------------------------------------------
# 4. COMENTARIOS E INTERACCIONES
# ----------------------------------------------------------------------

class Comentario(BaseModel):
    id_comentario = AutoField()
    contenido = TextField()
    fecha = DateField()
    
    # Relaciones del UML (Un Lector publica un comentario en una Noticia)
    lector = ForeignKeyField(Lector, backref='comentarios')
    noticia = ForeignKeyField(Noticia, backref='comentarios')

    class Meta:
        table_name = 'comentarios'

# ----------------------------------------------------------------------
# 5. TABLA INTERMEDIA (Relación Muchos a Muchos entre Noticia y Etiqueta)
# ----------------------------------------------------------------------

class NoticiaEtiqueta(BaseModel):
    noticia = ForeignKeyField(Noticia, backref='etiquetas_asociadas')
    etiqueta = ForeignKeyField(Etiqueta, backref='noticias_asociadas')

    class Meta:
        table_name = 'noticias_etiquetas'