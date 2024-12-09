from clases.marcas import Marcas as mar
from mysql.connector import Error
from dal.conexion import conectar
import os
import pandas as pd
import mysql.connector

def agregar_marca():
        """
        insertar la marca en la BD
        """
        try:
            conn = conectar()
            if conn is not None:
                cursor = conn.cursor()
                nom_marca= input("Ingrese nueva marca: ")
                sql = "INSERT INTO marcas (nom_marca) values (%s)"
                valores = (nom_marca,)
                cursor.execute(sql, valores)
                conn.commit()
                print("Marca agregada correctamente")
                cursor.close()
                conn.close()
        except Error as e:
            print(F"Error al insertar la marca {e}")

def mostrar_marcas():
    """
    Conectar a la base de datos, obtener y mostrar marcas en un DataFrame
    """
    os.system("cls")
    try:
        conex = conectar()
        if conex is not None:
            cur = conex.cursor()
            # Ejecutar la consulta
            cur.execute("SELECT * FROM marcas")
            # Obtener los resultados y convertirlos en un DataFrame
            resultados = cur.fetchall()
            columnas = [col[0] for col in cur.description]  # Obtener los nombres de las columnas
            df = pd.DataFrame(resultados, columns=columnas)

        # Mostrar el DataFrame
            print(df)

        # Cerrar la conexión
            cur.close()
            conex.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
