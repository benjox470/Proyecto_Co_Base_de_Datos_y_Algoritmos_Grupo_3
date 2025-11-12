import mysql.connector
import json
from mysql.connector import errorcode
import time
import datetime
cursor = None
cnx = None
#conectarbase: Conecta con la base de datos
def conectarBase():
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

#consultainsertar: Se usa de base para hacer los inserts a la tabla ventas
def consultaInsertar(meds,clients,employes,datexd, cuantity):
    # meds: El id del medicamento
    #clients: El id del cliente
    #employes: El id del empleado
    #datexd: La fecha de la compra con la hora
    #cuantity: La cantidad del producto comprado
    #sql: El insert a la base de datos
    sql = "INSERT INTO Ventas (Id_medicamentos,Id_Clientes,Id_Empleados,Fecha_yhora,cantidad)VALUES( %s, %s, %s, %s,%s)"
    cursor.execute(sql,(meds,clients,employes,datexd,cuantity))
    cnx.commit()
    return cursor.lastrowid

#aplicar_contra_indicaciones: tiene la tabla con las contraindicaciones base.
def aplicar_contra_indicaciones():
    #lista: donde se van a almacenar los diccionarios
    #contraindicaciones=donde se guardan las contraindicaciones
    #ids:donde se guardan los ids
    #medicamento: diccionario base para crear los demas
    lista=[]
    contraindicaciones=["personas alérgicas a la amoxicilina, a otras penicilinas o a antibióticos betalactámicos","no debe utilizarse en personas con alergia a la sustancia o sus componentes, en menores de 6 años",
                        "personas con antecedentes de alergias graves a este medicamento, especialmente anafilaxia, enfermedad del suero u otras reacciones alérgicas previas.","hipersensibilidad al fármaco y en combinación con inhibidores de la monoaminooxidasa (IMAO), y requiere precaución en varias condiciones médicas y situaciones especiales, incluyendo embarazo, lactancia, enfermedades hepáticas y trastornos psiquiátricos activos.",
                        "hipersensibilidad a las benzodiacepinas, insuficiencia respiratoria grave, apnea del sueño, miastenia gravis y en ciertas condiciones del embarazo y lactancia.",
                        "sangrado activo, úlceras pépticas, insuficiencia hepática o renal grave, hipersensibilidad al acenocumarol, embarazo y ciertas condiciones médicas que aumentan el riesgo de hemorragia.",
                        "con alergia al metamizol, antecedentes de agranulocitosis, asma, problemas de médula ósea, porfiria hepática aguda, insuficiencia renal o hepática grave, embarazo en el tercer trimestre y lactancia."
                        ]
    ids=[3,4,6,7,11,12,15]
    for i in range(len(ids)):
        medicamento = {
            "id": ids[i],
            "contraindicacion": contraindicaciones[i]
        }
        lista.append(medicamento)
    return lista

#add_contraindicaciones: Permite añadir contraindicaciones
def add_contraindicaciones(Lista_original):
    #ids: El id del medicamento a volver diccionario
    #contraindicaciones: la contraindicacion del medicamento
    #Lista_original: El diccionario original
    ids=int(input("Ingrese el id del medicamento: "))
    contraindicaciones=input("Ingrese la contraindicacion: ")
    medicamento = {
        "id": ids,
        "contraindicacion": contraindicaciones
    }
    Lista_original.append(medicamento)
    return Lista_original

#dar_datos: Aqui el cajero da los datos para usando de base consulta insertar se hace un registro para la base de datos
def dar_datos(Diccionario):
    #medicament: El id del medicamento
    #clientes: El id del cliente
    #empleados: El id del empleado
    #fechas: La fecha y la hora de la venta
    #cantidades: La cantidad del producto vendido
    #Diccionario: Contiene la lista de diccionarios con las contraindicaciones
    try:
        medicament=int(input("Ingrese el id del medicamento que se vendio: "))
        clientes = int(input("Ingrese el id del cliente que compro: "))
        empleados = int(input("Ingrese el id del empleado que realizo la venta: "))
        fechas = datetime.datetime.now()
        cantidades=int(input("Ingrese la cantidad del producto que se compro: "))
        for i in range (len(Diccionario)):
            if Diccionario[i]["id"]==medicament:
                print (f"El medicamento seleccionado cuenta con la siguiente contraindicacion: {Diccionario[i]['contraindicacion']}")
        consultaInsertar(medicament,clientes,empleados,fechas,cantidades)
    except Exception:
        print ("Se ha equivocado en introducir los datos. Porfavor reintente la inserción")

#medicamentos: Realiza una consulta para tener todo el diccionario de medicamentos
def medicamentos():
    #consulta: La consulta a la base de datos para tener los registros de la tabla medicamentos
    consulta="select * from Medicamentos;"
    cursor.execute(consulta)
    return cursor.fetchall()

#binario: Realiza una busqueda binaria usando de base el diccionario de la funcion medicamentos
def binario():
    #Medsca: tiene los resultados de medicamentos, contando los registros
    #longitud: contiene el largo del diccionario de los medicamentos
    # Mitad: Es la mitad entera de la cantidad de registros
    # ingrese: El Id del medicamento a ver, se le resta 1 ya que al pasar de sql a python
    #el primer registro de sql tiene valor de 1  mientras que en python es 0
    Medsca=medicamentos()
    longitud=len(Medsca)
    Mitad=longitud//2
    ingrese=(int(input("Ingrese el id del medicamento el cual quiera verificar: ")))-1
    if ingrese<Mitad:
        for i in range (Mitad):
            if i==ingrese:
                print (f"Este es el medicamento respectivo{Medsca[ingrese]}")
                break
    else:
        for x in range (Mitad,longitud):
            if x==ingrese:
                print (f"Este es el medicamento respectivo{Medsca[ingrese]}")
                break

#proximos_a_vencer: Realiza una consulta conteniendo los datos de los medicamentos proximos a vencer
def proximos_a_vencer():
    #consulta: Selecciona los 3 medicamentos mas cercanos a vencer de la tabla sql
    consulta="select * from Medicamentos order by fecha_caducidad ASC limit 3;"
    cursor.execute(consulta)
    return cursor.fetchall()

#crear_Archivo_Proximos_Vencer: Crea un archivo json con los datos de proximo a vencer
def crear_Archivo_Proximos_Vencer():
    #nombre_archivo: El nombre del archivo a crear en formato json
    #Meds_prox_a_vencer: Es el diccionario generado por la funcion proximos a vencer, el cual despues vuelve
    #todos sus valores a str para poderlos pasar al formato
    nombre_archivo = "Consulta1.json"
    Meds_prox_a_vencer = proximos_a_vencer()
    Meds_prox_a_vencer=str(Meds_prox_a_vencer)
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
       json.dump(Meds_prox_a_vencer, archivo, indent=4, ensure_ascii=False)

#ventas: obtiene los datos de cuantas ventas se realizo por empleado
def ventas():
    #consulta: seleciona los vendedores con su total de ventas
    consulta = "select Empleados.Nombre, count(Ventas.Id_venta) from Empleados inner join Ventas on Ventas.Id_Empleados=Empleados.Id_empleado group by Ventas.Id_Empleados;"
    cursor.execute(consulta)
    return cursor.fetchall()

#crear_Archivo_ventas: Crea un archivo json con los datos de ventas
def crear_Archivo_ventas():
    #nombre_archivo2: El nombre del archivo a crear en formato json
    #empleadiatos: Es el diccionario generado por la funcion ventas
    nombre_archivo2 = "Consulta2.json"
    empleadiatos=ventas()
    with open(nombre_archivo2, 'w', encoding='utf-8') as archivo2:
       json.dump(empleadiatos, archivo2, indent=4, ensure_ascii=False)

#sortear_meds: Se buscan medicamentos segun su categoria
def sortear_meds():
    #consulta: es la que selecciona los datos de la tabla medicamentos por id de categoria
    #se completa despues de recibir el id de la categoria. Por eso se ve sin los datos y ;
    #Categoria: El id de la categoria seleccionada, el cual despues se agrega a la variable consulta
    #junto con ; para ejecutarla
    consulta="select Nombre, Precio, Stock from medicamentos where Id_Cate= "
    categoria=input("Ingrese el id de la categoria que quiera buscar: ")
    consulta=consulta+categoria+" ;"
    cursor.execute(consulta)
    return cursor.fetchall()

#mostrar_sortear: Se muestran los resultados de sortear_meds
def mostrar_sortear():
    #A_mostrar: Contiene el diccionario generado por sortear_meds, que despues de muestra linea
    #por linea separado.
    A_mostrar=sortear_meds()
    for i in range(len(A_mostrar)):
        print (A_mostrar[i])

#cod_barras: Se buscan medicamentos segun su codigo de barras
def cod_barras():
    #consulta: Es la funcion que muestra los medicamentos segun su codigo de barras, le falta ese
    #dato ya que el cajero lo inserta y despues se añade.
    #barras: Es el codigo de barras que inserta el cajero, despues de escribirse se le añade a la variable
    #consulta junto con ; para ejecutar
    consulta="select Nombre, Precio, Stock,codigo_barra from medicamentos where codigo_barra= "
    barras=input("Ingrese el codigo de barras del producto: ")
    consulta=consulta+barras+" ;"
    cursor.execute(consulta)
    return cursor.fetchall()

#mostrar_barras: Se muestran los datos de cod_barras
def mostrar_barras():
    #A_mostrar: Muestra el diccionario del medicamento obtenido despues de haberlo buscado por
    #codigo de barra en la funcion cod_barras
    A_mostrar=cod_barras()
    print (A_mostrar)

def cargar_datos_json():
    try:
        with open("Contraindicaciones.json", 'r', encoding='utf-8') as archivo:
            datos_cargados = json.load(archivo)
        print ("Se ha cargado las contraindicaciones del archivo local")
        return datos_cargados
    except Exception:
        contraindications=aplicar_contra_indicaciones()
        print ("La carga ha fallado, se restaurara la copia predeterminada")
        return contraindications


#menu: Es el menu que contiene todas las funciones llamadas
def menu():
    #counter: Es lo que permite que se repita indefinidamente, cambia de valor al terminarse de ejecutar
    #el programa
    #opcion: La seleccion del cajero para ver que es lo que requiere hacer
    #contraindicaciones:Cuenta con el diccionario de contraindicaciones
    conectarBase()
    counter=True
    contraindicaciones = cargar_datos_json()
    while counter==True:
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
        print ("//   7. Para añadir contraindicaciones/")
        time.sleep(0.25)
        print("//    Otro para salir                 //")
        time.sleep(0.25)
        print("////////////////////////////////////////")
        time.sleep(0.25)
        opcion=int (input(""))
        if opcion==1:
            dar_datos(contraindicaciones)
        elif opcion==2:
            binario()
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
        elif opcion==7:
            contraindicaciones=add_contraindicaciones(contraindicaciones)
            with open("Contraindicaciones.json", 'w', encoding='utf-8') as archivo:
                json.dump(contraindicaciones, archivo, indent=4, ensure_ascii=False)
        else:
            with open("Contraindicaciones.json", 'w', encoding='utf-8') as archivo:
                json.dump(contraindicaciones, archivo, indent=4, ensure_ascii=False)
            if cnx.is_connected():
                cnx.close()
            print ("Adios que tenga un buen dia")
            counter=False
menu()
