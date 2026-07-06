CREATE DATABASE usuarios_db;
USE usuarios_db;

CREATE TABLE tipo_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    tipo_usuario INT NOT NULL,
    FOREIGN KEY (tipo_usuario) REFERENCES tipo_usuario(id)
);