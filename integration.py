import pandas as pd

print("Inicio del proceso.")
# Paso 1: Lee los datos de cada libro de Excel
excel_files = ['graduados_2018_act.xlsx', 'graduados_2019_act.xlsx', 'graduados_2020_act.xlsx', 'graduados_2021_act.xlsx']
dfs = [pd.read_excel(file) for file in excel_files]

print("Lectura de datos.")

# Paso 2: Concatena los DataFrames en uno solo
merged_df = pd.concat(dfs, ignore_index=True)

print("Concatenado okay.")

# Paso 3: Guarda el nuevo DataFrame en un nuevo libro de Excel
merged_df.to_excel('archivo_unificado_graduados.xlsx', index=False)

print("Datos unificados y guardados en archivo_unificado_graduados.xlsx")

#ASIGNACION DE ANIOS
# import pandas as pd
# from datetime import datetime, timedelta

# print("Inicio de proceso")
# # Paso 1: Lee el libro de Excel existente
# archivo_excel = 'graduados_2018_act.xlsx'
# df = pd.read_excel(archivo_excel)

# print("Lectura del libro de excel.")

# # Paso 2: Genera rango especificado
# # fecha_fin = datetime(2021, 12, 31)
# # rango_fechas = [fecha_inicio + timedelta(days=x) for x in range((fecha_fin-fecha_inicio).days + 1)]

# # Paso 3: Longitud del rango de fechas coincide con la longitud total de filas en el DataFrame (40524)
# # rango_fechas *= len(df) // len(rango_fechas) + 1
# # rango_fechas = rango_fechas[:len(df)]
# df['Anio'] = 2018
# print("Columna creada.")

# # Paso 4: Formatea la nueva columna con el formato deseado
# # df['Fecha'] = df['Fecha'].dt.strftime('%m-%d-%Y')

# # print("Formato de fecha okay.")

# # Paso 5: Guarda el DataFrame actualizado en el mismo libro de Excel
# new_excel_file_path = 'graduados_2018_act1.xlsx'
# df.to_excel(new_excel_file_path, index=False)

# print("Columna de fecha agregada y libro de Excel actualizado.")
