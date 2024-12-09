from dal.conexion import conectar
import os
import pandas as pd
import mysql.connector

def mostrar_tipo_calzado():
    """
    Conectar a la base de datos, obtener y mostrar los tipos en un DataFrame
    """
    os.system("cls")
    try:
        conex = conectar()
        if conex is not None:
            cur = conex.cursor()
            # Ejecutar la consulta
            cur.execute("SELECT * FROM tipo_calzado")
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
