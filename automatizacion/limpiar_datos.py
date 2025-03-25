import pandas as pd

# 1️⃣ Cargar el archivo CSV
df = pd.read_csv("empleados.csv")

# 2️⃣ Limpiar espacios en blanco en los nombres de columnas
df.columns = df.columns.str.strip()

# 3️⃣ Filtrar solo empleados activos
df = df[df["Estado"] == "Activo"]

# 4️⃣ Rellenar valores faltantes en "Horas Trabajadas"
# con el promedio del departamento


def promedio(x):
    return x.fillna(x.mean())


agrupar_departamentos = df.groupby("Departamento")
df["Horas Trabajadas"] = agrupar_departamentos["Horas Trabajadas"].transform(
    promedio)

# 5️⃣ Generar un resumen de promedio de horas trabajadas por departamento
reporte = df.groupby("Departamento")["Horas Trabajadas"].mean().reset_index()

# 6️⃣ Guardar el reporte en un archivo Excel
reporte.to_excel("salida.xlsx", sheet_name="Resumen", index=False)

print("✅ Reporte generado exitosamente: 'reporte_horas.xlsx'")
