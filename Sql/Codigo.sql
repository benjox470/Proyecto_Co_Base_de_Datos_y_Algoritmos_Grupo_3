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

create table Medicamentos (
	Id_medicamento int (3) unsigned auto_increment primary key,
    Id_Cate int(3) unsigned ,
    Nombre varchar (50),
    Precio decimal (10,2),
    stock int(3),
    codigo_barra varchar (25),
    receta enum ("SI","NO"),
    fecha_caducidad date,
    fecha_produccion date,
    foreign key (Id_Cate) references Categorias (Id_Categoria)
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
