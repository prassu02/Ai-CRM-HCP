from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from typing import TypedDict
import os
from dotenv import load_dotenv

from tools import log_interaction, summarize_interaction, suggest_next_action

load_dotenv()

llm = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

class AgentState(TypedDict):
    doctor_name: str
    notes: str
    summary: str
    next_action: list   # ✅ FIXED


def agent_node(state: AgentState):
    notes = state["notes"]

    summary = summarize_interaction(llm, notes)
    next_action = suggest_next_action(summary)   # ✅ FIXED

    return {
        "doctor_name": state["doctor_name"],
        "notes": notes,
        "summary": summary,
        "next_action": next_action
    }


def save_node(state: AgentState):
    log_interaction(state)
    return state


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)
    graph.add_node("save", save_node)

    graph.set_entry_point("agent")
    graph.add_edge("agent", "save")

    return graph.compile()