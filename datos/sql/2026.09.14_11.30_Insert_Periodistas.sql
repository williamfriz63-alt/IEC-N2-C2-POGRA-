INSERT INTO periodista (usuario, especialidad, rut) VALUES
(
    (SELECT id_usuario FROM usuario WHERE email = 'cmendoza@noticias.cl'),
    'Política y Economía',
    '15.342.111-K'
),
(
    (SELECT id_usuario FROM usuario WHERE email = 'alopez@noticias.cl'),
    'Tecnología y Ciencia',
    '17.890.222-3'
);