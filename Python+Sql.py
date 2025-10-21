import mysql.connector
import json
from mysql.connector import errorcode

cursor = None
cnx = None

def ConectarBase():
    global cnx, cursor
    try:
        cnx = mysql.connector.connect(user="root", password="", host="Localhost", database="Farmacity")
        cursor = cnx.cursor(dictionary=True)
        print('Conexión establecida')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuario o contraseña incorrectos!')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('La base de datos no existe!')
        else:
            print(err)
def ConsultaInsertar(meds,clients,employes,datexd, cuantity):
    sql = "INSERT INTO Ventas (Id_medicamentos,Id_Clientes,Id_Empleados,Fecha_yhora,cantidad)VALUES( %s, %s, %s, %s,%s)"
    cursor.execute(sql,(meds,clients,employes,datexd,cuantity))
    cnx.commit()
    return cursor.lastrowid
ConectarBase()
def dar_datos():
    medicamentos=int(input("Ingrese el id del mdeicamento que se vendio: "))
    clientes = int(input("Ingrese el id del cliente que compro: "))
    empleados = int(input("Ingrese el id del empleado que realizo la venta: "))
    fechas = (input("Ingrese la fecha y hora en la que se hizo la venta: "))
    cantidades=int(input("Ingrese la cantidad del producto que se compro: "))
    ConsultaInsertar(medicamentos,clientes,empleados,fechas,cantidades)
def Medicamentos():
    consulta="select * from Medicamentos;"
    cursor.execute(consulta)
    return cursor.fetchall()
def Binario():
    Medsca=Medicamentos()
    longitud=len(Medsca)
    Mitad=longitud//2
    ingrese=(int(input("Ingrese el id del ID el cual quiera verificar: ")))-1
    if ingrese<=Mitad:
        for i in range (Mitad):
            if i==ingrese:
                print (f"Este es el medicamento respectivo{Medsca[ingrese]}")
                break
    else:
        for x in range (Mitad,longitud):
            if x==ingrese:
                print (f"Este es el medicamento respectivo{Medsca[ingrese]}")
                break
Binario()
def proximos_a_vencer():
    consulta="select * from Medicamentos order by fecha_caducidad ASC limit 3;"
    cursor.execute(consulta)
    return cursor.fetchall()
def crear_Archivo_Proximos_Vencer():
    nombre_archivo = "Consulta1.json"
    Meds_prox_a_vencer = proximos_a_vencer()
    for x in range (len(Meds_prox_a_vencer)):
        Meds_prox_a_vencer[x]["Precio"] = int(Meds_prox_a_vencer[x]["Precio"])
        Meds_prox_a_vencer[x]["fecha_caducidad"]=str(Meds_prox_a_vencer[x]["fecha_caducidad"])
        Meds_prox_a_vencer[x]["fecha_produccion"] = str(Meds_prox_a_vencer[x]["fecha_produccion"])
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
       json.dump(Meds_prox_a_vencer, archivo, indent=4, ensure_ascii=False)
crear_Archivo_Proximos_Vencer()
def ventas():
    consulta = "select Empleados.Nombre, count(Ventas.Id_venta) from Empleados inner join Ventas on Ventas.Id_Empleados=Empleados.Id_empleado group by Ventas.Id_Empleados;"
    cursor.execute(consulta)
    return cursor.fetchall()
def crear_Archivo_ventas():
    nombre_archivo2 = "Consulta2.json"
    empleadiatos=ventas()
    with open(nombre_archivo2, 'w', encoding='utf-8') as archivo2:
       json.dump(empleadiatos, archivo2, indent=4, ensure_ascii=False)
crear_Archivo_ventas()
