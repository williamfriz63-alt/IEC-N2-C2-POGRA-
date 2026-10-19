INSERT INTO noticia_categoria (id_noticia, id_categoria) VALUES 
(
    (SELECT id_noticia FROM noticia WHERE titulo LIKE '%Inteligencia Artificial%' LIMIT 1),
    (SELECT id_categoria FROM categoria WHERE nombre = 'Tecnología' LIMIT 1)
);