from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition
from config import llm_with_tools, memory, tools, system_prompt
# from config import llm, memory, tools
from state import State

from langchain_core.messages import SystemMessage

def build_graph() -> StateGraph:
    graph_builder = StateGraph(State)

    def chatbot(state: State):
        response = llm_with_tools.invoke([SystemMessage(content=system_prompt)] + state["messages"])
        return {"messages": [response]}

    graph_builder.add_node("chatbot", chatbot)
    
    tool_node = ToolNode(tools)
    graph_builder.add_node("tools", tool_node)

    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_conditional_edges("chatbot", tools_condition)
    graph_builder.add_edge("tools", "chatbot")

    return graph_builder.compile(checkpointer=memory)

