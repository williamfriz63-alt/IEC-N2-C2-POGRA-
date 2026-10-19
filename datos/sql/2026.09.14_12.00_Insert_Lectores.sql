INSERT INTO lector (id_usuario, fecha_registro) VALUES
(
    (SELECT id_usuario FROM usuario WHERE email = 'jperez@gmail.com'),
    STR_TO_DATE('15/09/2026', '%d/%m/%Y')
);