import os
import getpass
import pandas as pd
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass(
        "Enter your OpenAI API key:")


@tool
def read_csv(file_path: str) -> str:
    """Lee un archivo CSV."""
    try:
        df = pd.read_csv(file_path)
        return df.to_string()
    except Exception as e:
        return f"Error al leer el archivo: {str(e)}"


@tool
def promedio(numbers: list) -> int:
    """Promedio los numeros de una lista.
    Args:
        numbers (list): Lista de numeros a sacar el promedio.
    """
    return sum(numbers) // len(numbers)


# Let's declare a llm instance and invoke it.
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=os.getenv("OPENAI_API_KEY")
)

print("----")
prompt = hub.pull("hwchase17/openai-tools-agent")


tools = [read_csv, promedio]
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)
ai_msg = agent_executor.invoke(
    {"input": "Dime el promedio de las edades del contenido del archivo datos.csv"})


print("---- Respuesta del Agente ----")
print(ai_msg["output"])
