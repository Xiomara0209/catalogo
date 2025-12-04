CREATE DATABASE tienda_virtual;
USE tienda_virtual;
CREATE TABLE usuario_tienda(
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    telefono VARCHAR(20),
    direccion VARCHAR(150),
    ciudad VARCHAR(100),
    provincia VARCHAR(100),
    pais VARCHAR(100)
);
INSERT INTO usuario_tienda (email, contraseña, nombre, apellido, telefono, direccion, ciudad, provincia, pais)
VALUES 
('monica1@gmail.com', '78910', 'Monica', 'Ruiz', '0119754238', '25 de Mayo 465', 'Tartagal', 'Salta', 'Argentina'),
('ricardo2@gmail.com', '123456', 'Ricardo', 'Sosa', '1122667598', 'Alberdi 321', 'Rio Cuarto', 'Córdoba', 'Argentina'),
('daniela44@gmail.com', '33756ef', 'Daniela', 'Cabral', '3589924452', 'Calle 5 236', 'Lima', 'Buenos Aires', 'Argentina'),
('fran88@gmail.com', '01122pr', 'Francisco', 'Araoz', '38784428007', 'Belgrano 776', 'La Banda', 'Santiago del Estero', 'Argentina'),
('maxi99@gmail.com', '50037xm', 'Maximiliano', 'Gutierrez', '343567821', 'Mendoza 444', 'San pedro', 'Jujuy', 'Argentina');
UPDATE usuario_tienda
SET contraseña = '221133'
WHERE id = 1;
UPDATE usuario_tienda
SET telefono = '35877652219', direccion = 'Mariano Moreno 444'
WHERE id = 1;
DELETE FROM usuario_tienda
WHERE id = 2;
