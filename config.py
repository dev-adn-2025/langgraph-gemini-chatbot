from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from search_web_tavily import search_web
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

memory = MemorySaver()

tools = [search_web]

system_prompt = """Eres un asistente útil y actualizado. Si el usuario te hace una pregunta sobre eventos recientes o cualquier información que pueda no estar en tu conocimiento actual, usa la herramienta `search_web` para buscar en internet y obtener la respuesta. Usa tu conocimiento directo solo si estás seguro de que la respuesta es correcta."""

llm = init_chat_model(
        "google_genai:gemini-2.0-flash-lite", 
    )

llm_with_tools = llm.bind_tools(tools)

graph_config = {"configurable": {"thread_id": "1"}}

