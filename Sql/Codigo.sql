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

insert into Clientes (nombre,Apellido,DNI,Localidad,telefono) 
values ("Nicolas","Previtalli",23546745,"la paternal",1154367621),
("Lucas","Ambrogio",45008675,"Villa crespo",1123347895),
("sofia","Boselli",42435710,"San Telmo",1165239807),
("Roman","Riquelme",35675982,"Flores",1154329087),
("Alejo","Acosta",23990763,"Caballito",11765100),
("Andres","chamorro",31456001,"Lanus",1112340009),
("Celeste","Ramirez",44545763,"Caballito",1144556723),
("Maria","Suarez",34590763,"Floresta",1198123421),
("Rodrigo","Miranda",22649763,"Balvanera",1165437892),
("Julieta","zanetti",54637201,"Flores",1176893332),
("Luciana","Desimonni",34654987,"Floresta",1145638321),
("Ezequiel","Cerutti",22552225,"Bajo flores",1144339876),
("Damian","Molina",43587322,"Boedo",1144556612),
("Sofia","Acosta",23945763,"Flores",1145632719),
("samuel","fernandez",42531232,"Caballito",1174678901);

create table Categorias (
	Id_Categoria int(3) unsigned auto_increment primary key,
    descripcion varchar (100)
);

insert into Categorias(descripcion) values 
("Analgesicos"),
("Antibioticos"),
("Antiinflamatorios"),
("Antidepresivo"),
("Antihistaminicos"),
("Antiinfecciosos"),
("Antipiréticos"),
("Antialérgicos"),
("Mucolíticos "),
("antitusivos"),
("Antiulcerosos "),
("antiácidos"),
("Antidiarreicos "),
("laxantes"),
("Antimicóticos");


create table Marcas (
	Id_marca int(3) unsigned auto_increment primary key,
    nombre varchar (100)
);

insert into Marcas(nombre) values
("Bayer"),
("Pfizer"),
( "Sanofi"),
( "Roche"),
( "Norvartis"),
("Adermicina"),
("Eucerin"),
("Unesia"),
("Ibupirac"),
("Ubasal"),
("G.U.M."),
("Ibu400"),
("Aztrazeneca"),
("Bristol"),
("Merck");

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
(1,5,'Aspirina', 130.00, 120, '0123456789012', 'NO', '2027-02-20', '2025-02-20'),
(4,6,"Orfidal" , 1000 , 97 ,'0123451282312', "SI" , '2029-12-20' , '2024-01-10' ),
(3,1,"Sintrom", 2500 , 20 , '012339398312' , 'SI' , '2030-06-10' , '2018-12-20'),
(8,5,"Orfidil" , 1233 , 50 , '012339494909' , 'NO' , '2020-12-10' , '2016-06-10'),
(3,9,"Ventonil" , 2334 , 123 , '012339391234' , 'NO' , '2019-02-18' , '2012-06-12'),
(2,6,"Nolotil" , 4000 , 35 , '012333456789' , 'SI' , '2019-02-18' , '2014-12-12');

create table Elementos_gondola (
	Id_gondola int (3) unsigned auto_increment primary key,
    Id_medicamentos int (3) unsigned,
    Descripcion varchar (100),
    foreign key (Id_medicamentos) references Medicamentos (Id_medicamento)
);
-- Los medicamentos que dicen NO 1,2,5,8,9,10,13,14
insert into Elementos_gondola (Id_medicamentos,Descripcion) values
(1,"No requiere receta."),
(2,"No requiere receta."),
(5,"No requiere receta."),
(8,"No requiere receta."),
(9,"No requiere receta."),
(10,"No requiere receta."),
(13,"No requiere receta."),
(14,"No requiere receta.");

create table Elementos_Fondo (
	Id_Fondo int (3) unsigned auto_increment primary key,
    Id_medicamen int (3) unsigned,
    Descripcion varchar (100),
    foreign key (Id_medicamen) references Medicamentos (Id_medicamento)
);

insert into Elementos_Fondo (Id_medicamen,Descripcion) values
(3,"Si requiere receta."),
(4,"Si requiere receta."),
(6,"Si requiere receta."),
(7,"Si requiere receta."),
(11,"Si requiere receta."),
(12,"Si requiere receta."),
(15,"Si requiere receta.");

create table Historial_compras (
	Id_compras int (3) unsigned auto_increment primary key,
    Id_client int (3) unsigned,
    Id_med int (3) unsigned,
    fecha date,
    foreign key (Id_med) references Medicamentos (Id_medicamento),
    foreign key (Id_client) references Clientes (Id_cliente)
);

insert into Historial_compras (Id_client,Id_med,fecha)
values(1,5,"2025-6-21"),
(4,9,"2025-6-17"),
(6,2,"2025-6-14"),
(7,5,"2025-6-14"),
(1,5,"2025-6-14"),
(4,8,"2025-6-12"),
(1,3,"2025-6-12"),
(2,2,"2025-6-10"),
(6,9,"2025-6-8"),
(1,5,"2025-6-7"),
(4,15,"2025-6-7"),
(6,6,"2025-6-6"),
(13,3,"2025-6-5"),
(1,5,"2025-6-1"),
(4,14,"2025-5-30");


create table Roles (
	Id_rol int(3) unsigned auto_increment primary key,
    descripcion varchar (100)
);

insert into Roles(descripcion) values
("Limpieza"),
("Seguridad"),
("Especialista en sistemas de gestion farmaceutica"),
("Ventas"),
("Encargado de inventario"),
("Analista de datos clinicos"),
("Gerente de farmacia"),
("Especialista en atencion al cliente farmaceutica"),
("Coordinador de compras"),
("Farmaceutico"),
("Bioquimico"),
("Asistente administrativo"),
("Soporte tecnico"),
("Analista de datos clinicos"),
("Recepcionista de pedidos");

create table sectores (
	id_sector int (3) unsigned auto_increment primary key,
    nombre varchar (100)
);

insert into sectores(nombre) values
("Deposito de medicamentos"),
("Laboratorio de formulacion magistral"),
("Sala de control de calidad"),
("Frente"),
("Area de facturacion y convenios"),
("Sala de reuniones o capacitacion"),
("Oficina de administracion"),
("Area de recursos humanos"),
("Departamento de compras"),
("Sector de refrigeracion"),
("Zona de productos vencidos o en cuarentena"),
("Area de recepcion de mercaderia"),
("Sector de devoluciones"),
("Sector de almacenamiento de psicotropicos"),
("Sala de preparacion de pedidos");
create table Empleados (
	Id_empleado int(3) unsigned auto_increment primary key,
    Id_role int(3) unsigned,
    Nombre varchar (50),
    Sueldo decimal (10,2),
    Sector int (3) unsigned,
    foreign key (Id_role) references Roles (Id_rol),
    foreign key (Sector) references sectores (id_sector)
);

insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(1, "Norberto González", 2500.1, 1);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(2, "Ana María Soldano", 2100.22, 2);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(3, "Marcos Alonso De las Nieves", 1905.12, 3);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(4, "Gonzalo Agustín Celman", 2410.0, 4);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(5, "Juana Sofía Meza", 1420.66, 5);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(6, "Lucio Sepeda", 3000.50, 6);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(7, "Manuela Castillo", 1780.0, 7);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(8, "Manuela Castillo", 2850.0, 8);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(9, "Miguel Velázquez", 2000.3, 9);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(10, "Carmen María Blázquez", 3000.12, 10);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(11, "Denis Ferrandis", 2390.1, 11);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(12, "Ana Isabel Gabasa", 2005.44, 12);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(13, "Juan Francisco Torres", 1600.33, 13);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(14, "Yasmin Alcaide", 2300.33, 14);
insert into Empleados(Id_role, Nombre, Sueldo, Sector)
values(15, "Eric García", 1802.14, 15);

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

insert into Ventas(Id_medicamentos,Id_Clientes,Id_Empleados,Fecha_yhora,cantidad)
values (8,4,4,"2025-9-23 15:30:45",2), 
(3,4,4,"2025-9-23 9:02:10",1),
(6,2,4,"2025-9-22 4:39:42",1),
(9,3,4,"2025-9-20 14:24:05",2),
(10,15,4,"2025-9-20 13:51:04",2),
(13,9,4,"2025-9-20 11:26:25",1),
(3,5,4,"2025-9-20 09:37:35",3),
(6,7,4,"2025-9-19 20:42:01",1),
(14,11,4,"2025-9-19 20:26:32",1),
(11,5,4,"2025-9-19 18:12:49",2),
(9,8,4,"2025-9-19 16:40:32",2),
(4,14,4,"2025-9-18 19:12:03",1),
(4,1,4,"2025-9-18 17:54:11",4),
(3,6,4,"2025-9-18 13:12:13",1),
(6,5,4,"2025-9-17 11:56:54",2);
