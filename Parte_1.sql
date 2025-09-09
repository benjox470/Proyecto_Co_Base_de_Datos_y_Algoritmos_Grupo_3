Drop database if exists Farmacity;
create database Farmacity;
USE Farmacity;

create table Clientes (
	id_cliente int (3) unsigned auto_increment primary key,
    Nombre varchar (50),
    Apellido varchar (50),
    DNI varchar (20),
    historial_compras int(3),
    direccion varchar (200),
    edad  int(3)
);

CREATE table Categorias (
	Id_categoria int(3) unsigned auto_increment primary key,
    descripcion varchar (100)
    
);

create table Medicamentos (
	Id_medicamento int (3) unsigned auto_increment primary key,
    Nombre varchar (50),
    id_cate int (3) unsigned,
    Precio decimal (10,2),
    stock int(3),
    codigo_barra varchar (25),
    foreign key (id_cate) references Categorias (Id_categoria)
);

create table Elementos_gondola (
	Id_gondola int (3) unsigned auto_increment primary key,
    Id_medicamentos int (3) unsigned,
    Descripcion varchar (100),
    foreign key (Id_medicamentos) references Medicamentos (Id_medicamento)
);

create table Elementos_Fondo (
	Id_Fondo int (3) unsigned auto_increment primary key,
    Id_medicamen int (3) unsigned,
    Descripcion varchar (100),
    foreign key (Id_medicamen) references Medicamentos (Id_medicamento)
);


create table Ventas (
	Id_venta int (3) unsigned auto_increment primary key,
    Id_medi int (3) unsigned,
    Id_cli int (3) unsigned,
    receta varchar (100),
    fecha date,
    cantidad int,
    foreign key (Id_medi) references Medicamentos (Id_medicamento),
    foreign key (Id_cli) references Clientes (id_cliente)
);

CREATE table Roles (
	Id_rol int(3) unsigned auto_increment primary key,
    descripcion varchar (100)
    
);

create table Empleados (
	Id_empleado int (3) unsigned auto_increment primary key,
    nombre varchar (50),
    Id_roles int (3) unsigned,
    foreign key (Id_roles) references Roles (Id_rol)
);
