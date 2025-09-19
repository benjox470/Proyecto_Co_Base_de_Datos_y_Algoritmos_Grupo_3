insert into Categorias(Id_Categoria,descripcion) values 
(1,"Analgesicos"),
(2, "Antibioticos"),
(3, "Antiinflamatorios"),
(4, "Antidepresivo"),
(5, "Antihistaminicos");

insert into Marcas(Id_marca,nombre) values
(1,"Bayer"),
(2,"Pfizer"),
(3, "Sanofi"),
(4, "Roche"),
(5, "Norvartis");

insert into Medicamentos (Id_medicamento,Id_Cate,id_marc,Nombre,Precio,stock,codigo_barra,receta,fecha_caducidad,fecha_produccion)values
(1,1,1,"Paracetamol",150.50,100,"123456789123","No","2026-05-20","2024-05-20"),
(2,3,1,"Ibuprofeno", 220.00, 80, "2345678901234", "NO", "2026-06-15", "2024-06-15"),
(3,2,2,"Amoxicilina", 350.00, 50, "3456789012345", "SI", "2026-07-10", "2024-07-10"),
(4,4,2,"Sertralina", 500.00, 40, '4567890123456', "SI", "2026-08-05", "2024-08-05"),
(5,5,3,"Loratadina", 180.75, 70, "5678901234567", 'NO', '2026-09-01', '2024-09-01'),
(6,2,3,'Penicilina', 400.00, 60, '6789012345678', 'SI', '2026-10-12', '2024-10-12'),
(7,4,4,'Fluoxetina', 520.00, 30, '7890123456789', 'SI', '2026-11-03', '2024-11-03'),
(8,3,4,'Diclofenaco', 260.00, 55, '8901234567890', 'NO', '2026-12-25', '2024-12-25'),
(9,5,5,'Cetirizina', 200.00, 90, '9012345678901', 'NO', '2027-01-15', '2025-01-15'),
(10,1,5,'Aspirina', 130.00, 120, '0123456789012', 'NO', '2027-02-20', '2025-02-20');