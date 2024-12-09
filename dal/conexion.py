import mysql.connector
from mysql.connector import Error

def conectar():
    '''
    
    establece la conexion a la bd ayudantia
    '''

    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            database = "kickstock",
            user = "root"
            #password=""
        )
    except mysql.connector.Error as e:
        print(f"Hubo un error al conectar a la BD {e}")
    else:
        if conexion.is_connected():
            return conexion
        return None