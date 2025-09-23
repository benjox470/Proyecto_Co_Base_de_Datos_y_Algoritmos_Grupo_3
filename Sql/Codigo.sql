drop database if exists Farmacity;
create database Farmacity;
Use Farmacity;

create table Clientes (
	Id_cliente int(3) unsigned auto_increment primary key,
    Nombre varchar (50),
    Apellido varchar (50),
    DNI int(11),
    Localidad varchar (200),
    telefono int(11)
);

create table Categorias (
	Id_Categoria int(3) unsigned auto_increment primary key,
    descripcion varchar (100)
);

insert into Categorias(descripcion) values 
("Analgesicos"),
("Antibioticos"),
( "Antiinflamatorios"),
( "Antidepresivo"),
( "Antihistaminicos");

create table Marcas (
	Id_marca int(3) unsigned auto_increment primary key,
    nombre varchar (100)
);

insert into Marcas(nombre) values
("Bayer"),
("Pfizer"),
( "Sanofi"),
( "Roche"),
( "Norvartis");

create table Medicamentos (
	Id_medicamento int (3) unsigned auto_increment primary key,
    Id_Cate int(3) unsigned ,
	id_marc int (3) unsigned,
    Nombre varchar (50),
    Precio decimal (10,2),
    stock int(3),
    codigo_barra varchar (25),
    receta enum ("SI","NO"),
    fecha_caducidad date,
    fecha_produccion date,
    foreign key (Id_Cate) references Categorias (Id_Categoria),
	foreign key (id_marc) references Marcas (Id_marca)
);

insert into Medicamentos (Id_Cate,id_marc,Nombre,Precio,stock,codigo_barra,receta,fecha_caducidad,fecha_produccion)values
(1,1,"Paracetamol",150.50,100,"123456789123","NO","2026-05-20","2024-05-20"),
(3,1,"Ibuprofeno", 220.00, 80, "2345678901234", "NO", "2026-06-15", "2024-06-15"),
(2,2,"Amoxicilina", 350.00, 50, "3456789012345", "SI", "2026-07-10", "2024-07-10"),
(4,2,"Sertralina", 500.00, 40, '4567890123456', "SI", "2026-08-05", "2024-08-05"),
(5,3,"Loratadina", 180.75, 70, "5678901234567", 'NO', '2026-09-01', '2024-09-01'),
(2,3,'Penicilina', 400.00, 60, '6789012345678', 'SI', '2026-10-12', '2024-10-12'),
(4,4,'Fluoxetina', 520.00, 30, '7890123456789', 'SI', '2026-11-03', '2024-11-03'),
(3,4,'Diclofenaco', 260.00, 55, '8901234567890', 'NO', '2026-12-25', '2024-12-25'),
(5,5,'Cetirizina', 200.00, 90, '9012345678901', 'NO', '2027-01-15', '2025-01-15'),
(1,5,'Aspirina', 130.00, 120, '0123456789012', 'NO', '2027-02-20', '2025-02-20');


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

create table Historial_compras (
	Id_compras int (3) unsigned auto_increment primary key,
    Id_client int (3) unsigned,
    Id_med int (3) unsigned,
    fecha date,
    foreign key (Id_med) references Medicamentos (Id_medicamento),
    foreign key (Id_client) references Clientes (Id_cliente)
);

create table Roles (
	Id_rol int(3) unsigned auto_increment primary key,
    descripcion varchar (100)
);

create table Empleados (
	Id_empleado int(3) unsigned auto_increment primary key,
    Id_role int(3) unsigned,
    Nombre varchar (50),
    Sueldo decimal (10,2),
    Sector varchar (200),
    foreign key (Id_role) references Roles (Id_rol)
);

create table Ventas (
	Id_venta int(3) unsigned auto_increment primary key,
    Id_medicamentos int(3) unsigned,
    Id_clientes int(3) unsigned,
    Id_empleados int(3) unsigned,
    Fecha_yhora datetime,
    cantidad int (4),
    foreign key (Id_medicamentos) references Medicamentos (Id_medicamento),
    foreign key (Id_clientes) references Clientes (Id_cliente),
    foreign key (Id_empleados) references Empleados (Id_empleado)
);
