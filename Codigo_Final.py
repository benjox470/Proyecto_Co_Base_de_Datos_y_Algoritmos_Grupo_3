import mysql.connector
import json
from mysql.connector import errorcode
import time
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
amox="personas alérgicas a la amoxicilina, a otras penicilinas o a antibióticos betalactámicos"
sert="no debe utilizarse en personas con alergia a la sustancia o sus componentes, en menores de 6 años"
peni="personas con antecedentes de alergias graves a este medicamento, especialmente anafilaxia, enfermedad del suero u otras reacciones alérgicas previas."
flux="hipersensibilidad al fármaco y en combinación con inhibidores de la monoaminooxidasa (IMAO), y requiere precaución en varias condiciones médicas y situaciones especiales, incluyendo embarazo, lactancia, enfermedades hepáticas y trastornos psiquiátricos activos."
orfi="hipersensibilidad a las benzodiacepinas, insuficiencia respiratoria grave, apnea del sueño, miastenia gravis y en ciertas condiciones del embarazo y lactancia."
sintrom="sangrado activo, úlceras pépticas, insuficiencia hepática o renal grave, hipersensibilidad al acenocumarol, embarazo y ciertas condiciones médicas que aumentan el riesgo de hemorragia."
nolotil="con alergia al metamizol, antecedentes de agranulocitosis, asma, problemas de médula ósea, porfiria hepática aguda, insuficiencia renal o hepática grave, embarazo en el tercer trimestre y lactancia."
def dar_datos():
    medicamentos=int(input("Ingrese el id del medicamento que se vendio: "))
    clientes = int(input("Ingrese el id del cliente que compro: "))
    empleados = int(input("Ingrese el id del empleado que realizo la venta: "))
    fechas = (input("Ingrese la fecha y hora en la que se hizo la venta: "))
    cantidades=int(input("Ingrese la cantidad del producto que se compro: "))
    if medicamentos==3:
        print (amox)
    elif medicamentos==4:
        print(sert)
    elif medicamentos==6:
        print (peni)
    elif medicamentos==7:
        print (flux)
    elif medicamentos==11:
        print (orfi)
    elif medicamentos==12:
        print (sintrom)
    elif medicamentos==15:
        print(nolotil)
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
def ventas():
    consulta = "select Empleados.Nombre, count(Ventas.Id_venta) from Empleados inner join Ventas on Ventas.Id_Empleados=Empleados.Id_empleado group by Ventas.Id_Empleados;"
    cursor.execute(consulta)
    return cursor.fetchall()
def crear_Archivo_ventas():
    nombre_archivo2 = "Consulta2.json"
    empleadiatos=ventas()
    with open(nombre_archivo2, 'w', encoding='utf-8') as archivo2:
       json.dump(empleadiatos, archivo2, indent=4, ensure_ascii=False)
def sortear_meds():
    consulta="select Nombre, Precio, Stock from medicamentos where Id_Cate= "
    categoria=str(input("Ingrese el id de la categoria que quiera buscar: "))
    consulta=consulta+categoria+" ;"
    cursor.execute(consulta)
    return cursor.fetchall()
def mostrar_sortear():
    A_mostrar=sortear_meds()
    for i in range(len(A_mostrar)):
        print (A_mostrar[i])
def Cod_barras():
    consulta="select Nombre, Precio, Stock,codigo_barra from medicamentos where codigo_barra= "
    barras=str(input("Ingrese el codigo de barras del producto: "))
    consulta=consulta+barras+" ;"
    cursor.execute(consulta)
    return cursor.fetchall()
def mostrar_barras():
    A_mostrar=Cod_barras()
    for i in range(len(A_mostrar)):
        print (A_mostrar[i])
#Dar datos
#Binario
#crear_Archivo_Proximos_Vencer
#crear_Archivo_ventas
#mostrar_sortear
#mostrar_barras
def Menu():
    counter=0
    while counter==0:
        time.sleep(0.25)
        print("////////////////////////////////////////")
        time.sleep(0.25)
        print("//    1. Para registrar ventas     /////")
        time.sleep(0.25)
        print("//    2. Busqueda de producto         //")
        time.sleep(0.25)
        print("///   3. Imprimir productos a vencer  //")
        time.sleep(0.25)
        print("//    4. Imprimir ventas por empleados /")
        time.sleep(0.25)
        print("//    5. Seleccionar Meds por Categoria/")
        time.sleep(0.25)
        print("//    6. Seleccionar Meds por Barras   /")
        time.sleep(0.25)
        print("//    Otro para salir                 //")
        time.sleep(0.25)
        print("////////////////////////////////////////")
        time.sleep(0.25)
        opcion=int (input(""))
        if opcion==1:
            dar_datos()
        elif opcion==2:
            Binario()
        elif opcion==3:
            crear_Archivo_Proximos_Vencer()
            print("Se ha creado el archivo correctamente")
        elif opcion==4:
            crear_Archivo_ventas()
            print("Se ha creado el archivo correctamente")
        elif opcion==5:
            mostrar_sortear()
        elif opcion==6:
            mostrar_barras()
        else:
            print ("Adios que tenga un buen dia")
            break


Menu()
