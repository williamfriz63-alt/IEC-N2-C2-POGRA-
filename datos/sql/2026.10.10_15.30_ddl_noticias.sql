create database Plataforma_de_noticias;

use Plataforma_de_noticias;

-- 1. Tabla Base: Usuario
CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL
);

-- 2. Herencia: Periodista
CREATE TABLE Periodista (
    id_usuario INT PRIMARY KEY,
    especialidad VARCHAR(100),
    rut VARCHAR(20) UNIQUE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
);

-- 3. Herencia: Lector
CREATE TABLE Lector (
    id_usuario INT PRIMARY KEY,
    fecha_registro DATE NOT NULL DEFAULT (CURRENT_DATE),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
);

-- 4. Tabla Categoria
CREATE TABLE Categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- 5. Tabla Etiqueta
CREATE TABLE Etiqueta (
    id_etiqueta INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- 6. Tabla Noticia
CREATE TABLE Noticia (
    id_noticia INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_creacion DATE NOT NULL DEFAULT (CURRENT_DATE),
    fecha_publicacion DATE,
    estado VARCHAR(30) DEFAULT 'Borrador',
    id_periodista INT NOT NULL,
    FOREIGN KEY (id_periodista) REFERENCES Periodista(id_usuario) ON DELETE CASCADE
);

-- 7. Tabla Recurso
CREATE TABLE Recurso (
    id_recurso INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(500) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    id_noticia INT NOT NULL,
    FOREIGN KEY (id_noticia) REFERENCES Noticia(id_noticia) ON DELETE CASCADE
);

-- 8. Tabla Comentario
CREATE TABLE Comentario (
    id_comentario INT AUTO_INCREMENT PRIMARY KEY,
    contenido TEXT NOT NULL,
    fecha DATE NOT NULL DEFAULT (CURRENT_DATE),
    id_lector INT NOT NULL,
    id_noticia INT NOT NULL,
    FOREIGN KEY (id_lector) REFERENCES Lector(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_noticia) REFERENCES Noticia(id_noticia) ON DELETE CASCADE
);

-- 9. Relación N:M Noticia-Categoria
CREATE TABLE Noticia_Categoria (
    id_noticia INT NOT NULL,
    id_categoria INT NOT NULL,
    PRIMARY KEY (id_noticia, id_categoria),
    FOREIGN KEY (id_noticia) REFERENCES Noticia(id_noticia) ON DELETE CASCADE,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria) ON DELETE CASCADE
);

-- 10. Relación N:M Noticia-Etiqueta
CREATE TABLE Noticia_Etiqueta (
    id_noticia INT NOT NULL,
    id_etiqueta INT NOT NULL,
    PRIMARY KEY (id_noticia, id_etiqueta),
    FOREIGN KEY (id_noticia) REFERENCES Noticia(id_noticia) ON DELETE CASCADE,
    FOREIGN KEY (id_etiqueta) REFERENCES Etiqueta(id_etiqueta) ON DELETE CASCADE
);