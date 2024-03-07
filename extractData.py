import psycopg2
from psycopg2 import sql
import csv

# Variables globales
error_con = False
id_pais   = 57  # Código ISO Colombia

# Parámetros de conexión a la base de datos local
v_host     = "localhost"
v_port     = "5432"
v_database = "bigdataStructure"
v_user     = "postgres"
v_password = "postgres"


# Datos para la inserción
datos_insercion = [
   
]

# Sentencia SQL para la inserción
sentencia_insert = sql.SQL("INSERT INTO instituciones_educacion_superior VALUES {codigo_institucion, nombre_institucion,id_sector_ies_codigo_departamento_ies, departamento_ies,codigo_municipio_ies, municipio_ies}").format(
    sql.SQL(',').join(map(sql.Literal, datos_insercion))
)

# Realizar la conexión y la inserción
try:
    conexion = psycopg2.connect(**parametros_conexion)
    cursor = conexion.cursor()
    
    # Ejecutar la sentencia SQL de inserción
    cursor.execute(sentencia_insert)
    
    # Confirmar la transacción
    conexion.commit()
    
    print("Datos insertados exitosamente.")
except Exception as error:
    print("Error durante la inserción:", error)
finally:
    # Cerrar la conexión
    if conexion:
        conexion.close()
        print("Conexión cerrada.")
