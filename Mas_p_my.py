import mysql.connector
import json
from mysql.connector import errorcode
import hashlib
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
ConectarBase()
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
