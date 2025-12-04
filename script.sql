USE tienda_virtual;
CREATE TABLE usuarios(
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    telefono VARCHAR(20),
    direccion VARCHAR(150),
    ciudad VARCHAR(100),
    provincia VARCHAR(100),
    pais VARCHAR(100)
);
INSERT INTO usuarios (email, password, nombre, apellido, telefono, direccion, ciudad, provincia, pais)
VALUES 
('monica1@gmail.com', '78910', 'Monica', 'Ruiz', '0119754238', '25 de Mayo 465', 'Tartagal', 'Salta', 'Argentina'),
('ricardo2@gmail.com', '123456', 'Ricardo', 'Sosa', '1122667598', 'Alberdi 321', 'Rio Cuarto', 'Córdoba', 'Argentina'),
('daniela44@gmail.com', '33756ef', 'Daniela', 'Cabral', '3589924452', 'Calle 5 236', 'Lima', 'Buenos Aires', 'Argentina'),
('fran88@gmail.com', '01122pr', 'Francisco', 'Araoz', '38784428007', 'Belgrano 776', 'La Banda', 'Santiago del Estero', 'Argentina'),
('vivi09gmail.com', '50037xm', 'Viviana', 'Gutierrez', '343567821', 'Mendoza 444', 'San pedro', 'Jujuy', 'Argentina');
UPDATE usuarios
SET password = '221133'
WHERE id = 1
UPDATE usuarios
SET telefono = '35877652219', direccion = 'Mariano Moreno 444'
WHERE id = 1;
DELETE FROM usuarios
WHERE id = 2;
