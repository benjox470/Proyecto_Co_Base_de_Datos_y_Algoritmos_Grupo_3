select Medicamentos.Nombre, sum(Ventas.cantidad) as "Cantidad total"
from Medicamentos
Inner join Ventas on Ventas.Id_medicamentos=Medicamentos.Id_medicamento
group by Id_medicamento
order by "Cantidad total" DESC
limit 5;

Select Nombre as "Medicamento critico", stock as "Stock del medicamento"
from Medicamentos
where stock<10;

select Clientes.nombre as "Nombre de clientes", count(Historial_compras.Id_compras) as "Compras totales"
from Clientes
inner join Historial_compras on  Historial_compras.Id_client=Clientes.Id_cliente
group by Historial_compras.Id_client
having  "Compras totales">5;

select *
from Empleados;

select Elementos_gondola.Descripcion , Medicamentos.Nombre
from Elementos_gondola
inner join Medicamentos on  Medicamentos.Id_medicamento=Elementos_gondola.Id_medicamentos;
