import csv

# Nombre del archivo CSV de entrada y salida
input_csv_file = 'archivo_programas.csv'
output_sql_file = 'output_programas.sql'

# Función para procesar y formatear una fila del CSV
def format_row(row):
    formatted_row = "("

    for value in row:
        # Si el valor es de tipo texto, enciérralo en comillas simples
        if isinstance(value, str):
            formatted_row += f"'{value}',"
        else:
            formatted_row += f"{value},"

    # Elimina la coma adicional al final y agrega un punto y coma
    formatted_row = formatted_row.rstrip(', ') + "),\n"

    return formatted_row

# Procesamiento principal
try:
    with open(input_csv_file, 'r', encoding='utf-8') as input_file, open(output_sql_file, 'w', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        
        # Lee la cabecera del archivo CSV
        header = next(reader)
        
        # Escribe la estructura del INSERT en el archivo SQL
        output_file.write(f"INSERT INTO tu_tabla ({', '.join(header)}) VALUES\n")

        # Procesa cada fila y escribe en el archivo SQL
        for row in reader:
            formatted_row = format_row(row)
            output_file.write(formatted_row)

    print(f"Archivo SQL generado correctamente: {output_sql_file}")

except Exception as e:
    print(f"Error: {e}")
