from dal.db_marcas import mostrar_marcas
from mysql.connector import Error
from dal.conexion import conectar
import os
import pandas as pd
import mysql.connector

def agregar_modelo():
        """
        insertar la marca en la BD
        """
        try:
            conn = conectar()
            if conn is not None:
                cursor = conn.cursor()
                nuevo_modelo = input("Ingrese nueva modelo: ")
                precio = input("Ingrese el precio: ")
                cantidad = input("Ingrese la cantidad: ")
                genero = input("Ingrese el genero (HOMBRE/MUJER/UNISEX): ")
                talla = input("Ingrese la talla: ")
                mostrar_marcas()
                id_marca = input("Ingrese el id de la marca: ")
                sql = "INSERT INTO modelos (nom_modelo, precio, cantidad, genero, talla, id_marca) values (%s,%s,%s,%s,%s,%s)"
                valores = (nuevo_modelo, precio, cantidad, genero, talla, id_marca)
                cursor.execute(sql, valores)
                conn.commit()
                print("Modelo agregada correctamente")
                cursor.close()
                conn.close()
        except Error as e:
            print(F"Error al insertar el modelo {e}")

def mostrar_modelos():
    """
    Conectar a la base de datos, obtener y mostrar modelos en un DataFrame
    """
    os.system("cls")
    try:
        conex = conectar()
        if conex is not None:
            cur = conex.cursor()
            # Ejecutar la consulta
            cur.execute("SELECT * FROM modelos")
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

def eliminar_modelo():
    """
    ELIMINAR EMPLEADOS DE LA BD
    """ 
    try:
        conex = conectar()
        if conex is not None:
            cur = conex.cursor()
            mostrar_modelos()
            # Si la conexión es exitosa, pedir el ID del modelo al usuario
            id_mod = int(input("Ingrese el ID del modelo a eliminar: "))

             # Crear la consulta de eliminación
            sql = "DELETE FROM modelos WHERE id_modelo = %s"
            valores = (id_mod,)

            # Ejecutar la consulta de eliminación
            cur.execute(sql, valores)
            conex.commit()  # Confirmar la transacción

            # Verificar si se eliminó alguna fila
            if cur.rowcount > 0:
                print("Modelo eliminado exitosamente.")
            else:
                print("ID_modelo no encontrado.")

            # Cerrar el cursor y la conexión
            cur.close()
            conex.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
