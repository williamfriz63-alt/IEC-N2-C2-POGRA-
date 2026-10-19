INSERT INTO noticia (titulo, contenido, fecha_creacion, estado, id_periodista) VALUES
(
    'Avances en Inteligencia Artificial 2026',
    'Detalles e impacto de las nuevas herramientas de automatización en la industria...',
    STR_TO_DATE('01/10/2026', '%d/%m/%Y'),
    'Publicada',
    (SELECT id_periodista FROM periodista LIMIT 1)
);

UPDATE noticia SET id_periodista = 1 WHERE id_noticia = 1;