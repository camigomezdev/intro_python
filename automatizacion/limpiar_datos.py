import pandas as pd

# 1️⃣ Cargar el archivo CSV
df = pd.read_csv("empleados.csv")

# 2️⃣ Limpiar espacios en blanco en los nombres de columnas
df.columns = df.columns.str.strip()

# 3️⃣ Filtrar solo empleados activos
df = df[df["Estado"] == "Activo"]

# 4️⃣ Rellenar valores faltantes en "Horas Trabajadas"
# con el promedio del departamento
df["Horas Trabajadas"] = df.groupby(
    "Departamento")["Horas Trabajadas"].transform(lambda x: x.fillna(x.mean()))

# 5️⃣ Generar un resumen de promedio de horas trabajadas por departamento
reporte = df.groupby("Departamento")["Horas Trabajadas"].mean().reset_index()

# 6️⃣ Guardar el reporte en un archivo Excel
with pd.ExcelWriter("reporte_horas.xlsx") as writer:
    reporte.to_excel(writer, sheet_name="Resumen", index=False)
    df.to_excel(writer, sheet_name="Empleados", index=False)

print("✅ Reporte generado exitosamente: 'reporte_horas.xlsx'")
