INSERT INTO comentario (contenido, fecha, id_lector, id_noticia) VALUES 
(
    'Excelente artículo sobre IA, muy lolazo siiii.',
    STR_TO_DATE('02/10/2026', '%d/%m/%Y'),
    (SELECT id_lector FROM lector LIMIT 1),
    (SELECT id_noticia FROM noticia WHERE titulo LIKE '%Inteligencia Artificial%' LIMIT 1)
);

UPDATE comentario SET id_lector = 1 WHERE id_comentario = 1;