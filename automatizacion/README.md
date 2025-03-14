# 📌 Guía Paso a Paso: Limpieza y Análisis de Datos de Empleados con Python

## 🛠 Instalación de Python y Librerías Necesarias

### 1️⃣ Instalar Python

Si no tienes Python instalado, descárgalo desde la página oficial: 🔗 [Descargar Python](https://www.python.org/downloads/)

Asegúrate de marcar la opción **"Add Python to PATH"** durante la instalación.

### 2️⃣ Crear un Entorno Virtual (Opcional pero Recomendado)

Para evitar conflictos entre librerías, puedes usar un entorno virtual:

```sh
python -m venv env
source env/bin/activate  # En Mac/Linux
env\Scripts\activate  # En Windows
```

### 3️⃣ Instalar las Librerías Necesarias

Ejecuta el siguiente comando para instalar las dependencias:

```sh
pip install pandas openpyxl
```

🔗 [Documentación de Pandas](https://pandas.pydata.org/docs/) 🔗 [Documentación de OpenPyXL](https://openpyxl.readthedocs.io/en/stable/)

---

## 📂 Estructura de Archivos

```plaintext
📁 proyecto_limpieza_datos/
│── 📄 empleados.csv  # Archivo con los datos originales
│── 📄 limpiar_datos.py  # Script para procesar los datos
│── 📄 reporte_horas.xlsx  # Salida con el reporte generado
```

---

## 📊 Archivo de Datos: empleados.csv

Ejemplo de contenido del archivo **empleados.csv**:

```csv
ID,Nombre,Departamento,Horas Trabajadas,Estado
1,Juan Pérez,Ventas,40,Activo
2,María López,Finanzas,35,Activo
3,Carlos Díaz,IT,,Activo
4,Ana Ruiz,RRHH,50,Inactivo
5,Pedro Gómez,IT,45,Activo
```

---

## 📜 Script Python: limpiar\_datos.py

```python
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
```

---

## 🚀 Explicación del Código

1. **Cargamos el archivo CSV** usando `pandas.read_csv()`. Esto nos permite leer los datos y trabajar con ellos en un DataFrame de pandas.
2. **Eliminamos espacios en los nombres de las columnas** para evitar errores de acceso a los datos debido a nombres con espacios.
3. **Filtramos solo los empleados activos** eliminando aquellos que están marcados como "Inactivo", ya que no deben ser considerados en el análisis.
4. **Rellenamos valores nulos** en "Horas Trabajadas" con el promedio del departamento correspondiente. Si un empleado no tiene un registro de horas, se asigna el valor medio de su área.
5. **Calculamos el promedio de horas trabajadas** por departamento agrupando los datos con `groupby()` y aplicando `mean()` para obtener un valor representativo de cada área.
6. **Guardamos el resultado en un archivo Excel** (`reporte_horas.xlsx`) usando `to_excel()`, lo que permite compartir y visualizar los datos fácilmente en otras herramientas como Excel o Google Sheets.
---

## ▶️ Ejecutar el Programa

Para ejecutar el script, usa el siguiente comando en la terminal:

```sh
python limpiar_datos.py
```

Si todo funciona bien, verás este mensaje:

```
✅ Reporte generado exitosamente: 'reporte_horas.xlsx'
```

El archivo **reporte\_horas.xlsx** contendrá el resumen de horas trabajadas por departamento.

---

## 🎯 Conclusión

Con este sencillo script, podemos **automatizar la limpieza y análisis de datos administrativos**, ahorrando tiempo y evitando errores manuales. Puedes expandirlo agregando **gráficos, dashboards o integraciones con bases de datos**. 🚀

🔗 **Recursos Adicionales:**

- [Documentación de Pandas](https://pandas.pydata.org/docs/)
- [Documentación de OpenPyXL](https://openpyxl.readthedocs.io/en/stable/)
