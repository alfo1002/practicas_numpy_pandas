import pandas as pd
import numpy as np


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[0].sum())


# Pandas
# Lectura de un archivo CSV
data = pd.read_csv('datos_empleados.csv')
print(data.head())

print(data.dropna()) # Elimina filas con valores NaN

# iloc lista index
# Acceso a la primera fila y columna 'fecha_nacimiento'
#print(data.iloc[0]['fecha_nacimiento']) 

# listar solo los empleados con fecha de nacimiento posterior a 1990
#print(data[data['fecha_nacimiento'] > '2004-01-01'])

# listar empleados con fecha de nacimiento posterior a 2004
#print(data.query('fecha_nacimiento > "2004-01-01"'))

# listar empleados con fecha de nacimiento posterior a 2004 y salario mayor a 900
#print(data.query('fecha_nacimiento > "2004-01-01" and sueldo >= 1000'))

# Filtrar empleados con email de Gmail])
#print(data[data['email'].str.endswith('@gmail.com')])

#print(data[data['email'].str.endswith('@empresa.com')])  # negar con ~data['email'].str.endswith('@empresa.com')

# Filtrar por área
#print(data[data['area'].isin(['Talento Human0', 'Ventas'])])

#agrupar por área y contar el número de empleados en cada área
#print(data.groupby('area')['area'].count())  

# agrupar por área y contar el número de empleados con sueldo mayor a 800 y ordenar de mayor a menor
#print(data[data['sueldo'] > 800].groupby('area')['area'].count().sort_values(ascending=False))  

# Obtener empleados que tengna email null
#print(data[data['email'].isnull()])

# Obtener el empleado con el sueldo más alto
#print(data.loc[data['sueldo'].idxmax()])
#print(data['sueldo'].max())

# Obtener el empleado con el sueldo más bajo
#print(data.loc[data['sueldo'].idxmin()])
#print(data['sueldo'].min())

# Calcular el sueldo promedio
#print(data['sueldo'].mean())  

# Listar áreas únicas
print(data['area'].unique())  
