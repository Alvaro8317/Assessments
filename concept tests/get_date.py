from datetime import datetime

fecha_datetime = datetime(2023, 9, 14, 10, 30, 0)

# Formatear la fecha y hora sin la "Z" al final
fecha_formateada = fecha_datetime.strftime('%Y-%m-%dT%H:%M:%S')

# Imprimir la fecha formateada
print("Fecha original", fecha_datetime)
print("Fecha formateada:", fecha_formateada)
