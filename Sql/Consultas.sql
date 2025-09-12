select Medicamentos.nombre as "Nombre de Medicamento", count(Historial_compras.Id_compras) as "Compras totales"
from Medicamentos
inner join Historial_compras on  Historial_compras.Id_med=Medicamentos.Id_medicamento
where  "Compras totales">5;

Select Nombre as "Medicamento critico", stock as "Stock del medicamento"
from Medicamentos
where stock<10;

select Clientes.nombre as "Nombre de clientes", count(Historial_compras.Id_compras) as "Compras totales"
from Clientes
inner join Historial_compras on  Historial_compras.Id_client=Clientes.Id_cliente
where  "Compras totales">5;
