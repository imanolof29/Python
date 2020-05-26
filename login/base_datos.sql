CREATE TABLE Usuarios (
  id int(3)  NOT NULL AUTO_INCREMENT,
  nombreusuario varchar(15) NOT NULL,
  nombre varchar(15),
  apellido varchar(15),
  correo varchar(30) NOT NULL,
  contrasena varchar(15) NOT NULL,
  PRIMARY KEY (id)
);
