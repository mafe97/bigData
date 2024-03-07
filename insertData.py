import csv

# Nombre del archivo CSV de entrada y salida
archivo_entrada = 'archivo_unificado_graduados.csv'
archivo_salida = 'archivo_programas.csv'

# Índices de las columnas que deseas extraer (0-indexed)
columnas_necesarias = [17, 18, 19, 20]

# Lista para almacenar las filas seleccionadas
filas_seleccionadas = []

# Leer el archivo CSV original y extraer las columnas necesarias
with open(archivo_entrada, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    for row in reader:
        # Crear una nueva fila con las columnas seleccionadas
        nueva_fila = [row[i] for i in columnas_necesarias]
        filas_seleccionadas.append(nueva_fila)

# Escribir las filas seleccionadas en un nuevo archivo CSV
with open(archivo_salida, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Escribir el encabezado si es necesario
    # writer.writerow(["Columna1", "Columna2", "Columna3"])  # Reemplazar con los nombres de tus columnas
    
    # Escribir las filas seleccionadas
    writer.writerows(filas_seleccionadas)

print(f'Se han extraído las columnas necesarias en {archivo_salida}.')
