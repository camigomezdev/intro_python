# 🚀 Guía Paso a Paso: Uso de un Agente con LangChain y OpenAI

Este documento explica cómo instalar, configurar y ejecutar un script en Python que utiliza **LangChain** para interactuar con modelos de OpenAI y procesar datos desde un archivo CSV.

---

## 🛠 Instalación de Dependencias

Antes de ejecutar el script, es necesario instalar las librerías requeridas. Ejecuta el siguiente comando en la terminal:

```sh
pip install pandas langchain langchain_openai langchain_core
```

Si aún no tienes una **clave API de OpenAI**, regístrate y obtén una en:
🔗 [https://platform.openai.com/signup](https://platform.openai.com/signup)

---

## 📂 Estructura del Proyecto

```plaintext
📁 mi_proyecto/
│── 📄 datos.csv  # Archivo con datos de empleados
│── 📄 agent.py   # Script con el agente basado en LangChain
```

---

## 📜 Explicación del Código

### 1️⃣ Importación de Librerías
```python
import os
import getpass
import pandas as pd
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
```
🔹 **Explicación:** Se importan las librerías necesarias para manipular datos, usar LangChain y conectar con OpenAI.

---

### 2️⃣ Configuración de la API Key
```python
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key:")
```
🔹 **Nota:** Se requiere una API key creada previamente en [OpenAI platform](https://platform.openai.com/api-keys)

---

### 3️⃣ Creación de Herramientas (Tools) para el Agente

#### 📌 Función para Leer un Archivo CSV
```python
@tool
def read_csv(file_path: str) -> str:
    """Lee un archivo CSV."""
    try:
        df = pd.read_csv(file_path)
        return df.to_string()
    except Exception as e:
        return f"Error al leer el archivo: {str(e)}"
```
🔹 **Explicación:** Define una herramienta `read_csv` para leer y devolver todas las filas de un archivo CSV.

#### 📌 Función para sacar el Promedio Números de una Lista
```python
@tool
def promedio(numbers: list) -> int:
    """Promedio los numeros de una lista.
    Args:
        numbers (list): Lista de numeros a sacar el promedio.
    """
    return sum(numbers) // len(numbers)
```
🔹 **Explicación:** Define una herramienta `promedio` que recibe una lista de números y devuelve el promedio de ellos.

---

### 4️⃣ Creación del Agente LangChain
```python
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=os.getenv("OPENAI_API_KEY")
)
```
🔹 **Explicación:** Se inicializa el modelo de OpenAI para que el agente pueda procesar peticiones.

---

### 5️⃣ Configuración del Agente y su Ejecución
```python
prompt = hub.pull("hwchase17/openai-tools-agent")

tools = [read_csv, promedio]
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)
```
🔹 **Explicación:**
- Se obtiene un prompt base desde `LangChain Hub`.
- Se registran las herramientas (`read_csv` y `promedio`).
- Se crea un agente con las herramientas y el modelo LLM de OpenAI.

---

### 6️⃣ Invocación del Agente con una Petición
```python
ai_msg = agent_executor.invoke(
    {"input": "Dime el promedio de las edades del contenido del archivo datos.csv"})

print("---- Respuesta del Agente ----")
print(ai_msg["output"])
```
🔹 **Explicación:**
- Se le pide al agente que lea el archivo **datos.csv** y calcule el promedio de las edades en el contenido.
- Se imprime la respuesta generada por el agente.

---

## ▶️ Ejecución del Script

Para ejecutar el script, abre la terminal y ejecuta:
```sh
python agent.py
```
Si la API Key no está configurada, te pedirá que la ingreses manualmente.

---

## 🎯 Conclusión

Este script demuestra cómo utilizar **LangChain** y **OpenAI** para procesar datos dinámicamente. Puedes expandirlo para manejar más consultas, mejorar el formato de salida o integrarlo con bases de datos y sistemas externos. 🚀

🔹 **Recursos adicionales:**
- [LangChain - Documentación](https://python.langchain.com/)
- [OpenAI API](https://platform.openai.com/docs/)

