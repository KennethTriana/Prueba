DROP DATABASE IF EXISTS animales;
CREATE DATABASE animales;
USE animales;

CREATE TABLE Usuario(
    Codigo INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    Nombres VARCHAR(50) NOT NULL,
    Apellidos VARCHAR(50) NOT NULL,
    Cedula INT NOT NULL UNIQUE,
    Celular VARCHAR(50) NOT NULL,
    Dirección VARCHAR(100) NOT NULL,
    Localidad VARCHAR(50) NOT NULL,
    Correo VARCHAR(50) NOT NULL,
    Contraseña VARCHAR(50) NOT NULL
);

CREATE TABLE Animal(
    Codigo INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    FechaNacimiento DATETIME NOT NULL,
    Usuario_Cod INT NOT NULL,
    FOREIGN KEY (Usuario_Cod) REFERENCES Usuario(Codigo) ON DELETE CASCADE 
);

CREATE TABLE Adopcion(
    Codigo INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    Fecha DATETIME NOT NULL,
    Descripcion VARCHAR(100) NOT NULL,
    Animal_Cod INT NOT NULL,
    FOREIGN KEY (Animal_Cod) REFERENCES Animal(Codigo) ON DELETE CASCADE
);

-- Inserciones
INSERT INTO Usuario (Nombres, Apellidos, Cedula, Celular, Dirección, Localidad, Correo, Contraseña) 
VALUES ('Juan', 'Pérez', 12345678, '3001234567', 'Calle 10 #20-30', 'Bogotá', 'juan.perez@example.com', 'password123');

INSERT INTO Usuario (Nombres, Apellidos, Cedula, Celular, Dirección, Localidad, Correo, Contraseña) 
VALUES ('María', 'Gómez', 23456789, '3109876543', 'Carrera 50 #15-10', 'Medellín', 'maria.gomez@example.com', 'pass456');

INSERT INTO Usuario (Nombres, Apellidos, Cedula, Celular, Dirección, Localidad, Correo, Contraseña) 
VALUES ('Carlos', 'Rodríguez', 34567890, '3201112233', 'Avenida 80 #22-45', 'Cali', 'carlos.rodriguez@example.com', '123qwerty');

INSERT INTO Usuario (Nombres, Apellidos, Cedula, Celular, Dirección, Localidad, Correo, Contraseña) 
VALUES ('Ana', 'Martínez', 45678901, '3003214567', 'Calle 100 #10-20', 'Barranquilla', 'ana.martinez@example.com', 'abc987');

INSERT INTO Usuario (Nombres, Apellidos, Cedula, Celular, Dirección, Localidad, Correo, Contraseña) 
VALUES ('Luis', 'Fernández', 56789012, '3012223334', 'Carrera 30 #50-60', 'Cartagena', 'luis.fernandez@example.com', 'pass321');


INSERT INTO Animal (Nombre, FechaNacimiento, Usuario_Cod) 
VALUES ('Firulais', '2020-05-12 10:30:00', 1);

INSERT INTO Animal (Nombre, FechaNacimiento, Usuario_Cod) 
VALUES ('Max', '2019-08-21 14:00:00', 2);

INSERT INTO Animal (Nombre, FechaNacimiento, Usuario_Cod) 
VALUES ('Bella', '2021-01-10 08:45:00', 3);

INSERT INTO Animal (Nombre, FechaNacimiento, Usuario_Cod) 
VALUES ('Rocky', '2020-12-05 13:15:00', 4);

INSERT INTO Animal (Nombre, FechaNacimiento, Usuario_Cod) 
VALUES ('Luna', '2018-11-02 16:20:00', 5);


INSERT INTO Adopcion (Fecha, Descripcion, Animal_Cod) 
VALUES ('2023-06-10 09:00:00', 'Adopción de perro mediano', 1);

INSERT INTO Adopcion (Fecha, Descripcion, Animal_Cod) 
VALUES ('2023-07-15 11:30:00', 'Adopción de perro pequeño', 2);

INSERT INTO Adopcion (Fecha, Descripcion, Animal_Cod) 
VALUES ('2023-08-20 14:45:00', 'Adopción de gato', 3);

INSERT INTO Adopcion (Fecha, Descripcion, Animal_Cod) 
VALUES ('2023-09-25 17:00:00', 'Adopción de perro grande', 4);

INSERT INTO Adopcion (Fecha, Descripcion, Animal_Cod) 
VALUES ('2023-10-01 10:15:00', 'Adopción de gato adulto', 5);


-- Consultas Sencillas
SELECT Nombres, Apellidos, Localidad 
FROM Usuario 
WHERE Localidad = 'Bogotá';

SELECT Nombres, Apellidos 
FROM Usuario 
WHERE Celular LIKE '300%';

SELECT Nombres, Apellidos 
FROM Usuario 
WHERE Localidad = (SELECT Localidad FROM Usuario WHERE Cedula = 12345678);


SELECT Nombre 
FROM Animal 
WHERE FechaNacimiento > '2020-01-01';

SELECT Nombre 
FROM Animal 
WHERE Usuario_Cod = 1;

SELECT Nombre 
FROM Animal 
WHERE Codigo > 2;

SELECT Nombre 
FROM Animal 
WHERE FechaNacimiento = (SELECT FechaNacimiento FROM Animal WHERE Nombre = 'Max');


SELECT Codigo, Fecha, Descripcion 
FROM Adopcion 
WHERE Fecha BETWEEN '2023-08-01' AND '2023-08-31';

SELECT Descripcion 
FROM Adopcion 
WHERE Animal_Cod < 3;

SELECT Codigo, Descripcion 
FROM Adopcion 
WHERE Descripcion LIKE '%gato%';

SELECT Descripcion 
FROM Adopcion 
WHERE Animal_Cod IN (SELECT Codigo FROM Animal WHERE FechaNacimiento < '2020-01-01');


-- Consultas Complejas
SELECT u.Nombres, u.Apellidos, a.Nombre AS Animal 
FROM Usuario u
INNER JOIN Animal an ON u.Codigo = an.Usuario_Cod
INNER JOIN Adopcion ad ON an.Codigo = ad.Animal_Cod;

SELECT u.Nombres, u.Apellidos 
FROM Usuario u 
WHERE u.Codigo NOT IN (SELECT Usuario_Cod FROM Animal);


SELECT an.Nombre AS Animal, u.Nombres AS Dueño 
FROM Animal an
INNER JOIN Usuario u ON an.Usuario_Cod = u.Codigo;

SELECT an.Nombre 
FROM Animal an 
WHERE an.Codigo NOT IN (SELECT Animal_Cod FROM Adopcion);


SELECT ad.Codigo AS Adopcion, ad.Descripcion, an.Nombre AS Animal, u.Nombres AS Dueño 
FROM Adopcion ad
INNER JOIN Animal an ON ad.Animal_Cod = an.Codigo
INNER JOIN Usuario u ON an.Usuario_Cod = u.Codigo;

SELECT ad.Codigo AS Adopcion, u.Nombres AS Dueño, u.Localidad, an.Nombre AS Animal 
FROM Adopcion ad
INNER JOIN Animal an ON ad.Animal_Cod = an.Codigo
INNER JOIN Usuario u ON an.Usuario_Cod = u.Codigo
WHERE u.Localidad = 'Bogotá';