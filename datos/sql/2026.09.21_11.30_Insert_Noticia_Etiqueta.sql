INSERT INTO noticia_etiqueta (id_noticia, id_etiqueta) VALUES 
(
    (SELECT id_noticia FROM noticia WHERE titulo LIKE '%Inteligencia Artificial%' LIMIT 1),
    (SELECT id_etiqueta FROM etiqueta WHERE nombre = 'Innovación' LIMIT 1)
),
(
    (SELECT id_noticia FROM noticia WHERE titulo LIKE '%Inteligencia Artificial%' LIMIT 1),
    (SELECT id_etiqueta FROM etiqueta WHERE nombre = 'Tendencia' LIMIT 1)
);