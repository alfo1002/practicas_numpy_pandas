import polars as pl

#lazy_dataf = pl.read_csv('datos_empleados.csv')
#print(lazy_dataf)

lazy_dataf = pl.scan_csv('datos_empleados.csv')
lazy_dataf.limit(25).sink_parquet('datos_empleados.parquet') # Save to Parquet format
pl_dataf = pl.read_parquet('datos_empleados.parquet') # Read from Parquet format
print(pl_dataf)

#listar solo dos columnas
#print(pl_dataf.select(['empleado', 'sueldo']))

#seleccionar todas las columnas
#print(pl_dataf.select(pl.all()))
#print(pl_dataf.select(pl.col('*')))

#excluir una columna
#print(pl_dataf.select(pl.exclude('email')))


#Operaciones de restricción
# filtrar empleados de Sistemas
#print(pl_dataf.filter(pl.col('area') == 'Sistemas'))

# Agrupar y contar por area
print(pl_dataf.group_by('area').agg(pl.count(), pl.col('sueldo').min().alias('min sueldo'), pl.col('sueldo').max().alias('max sueldo'), pl.col('sueldo').mean().alias('sueldo_promedio')))