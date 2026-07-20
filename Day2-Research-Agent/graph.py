from typing import TypedDict

from langgraph.graph import StateGraph, END

from search_tool import search_web
from memory import save_sources
from analyzer import analyze, quality_score
from report import save_report
from logger import log

class AgentState(TypedDict):

    query: str

    results: list

    analysis: str

    score: dict

def search_node(state):

    log("Searching...")

    results = search_web(state["query"])

    state["results"] = results

    return state

def memory_node(state):

    log("Saving to ChromaDB")

    save_sources(state["results"])

    return state

def analysis_node(state):

    log("Generating analysis")

    state["analysis"] = analyze(
        state["query"],
        state["results"]
    )

    return state

def score_node(state):

    log("Calculating score")

    state["score"] = quality_score(
        state["results"]
    )

    return state

def report_node(state):

    log("Saving report")

    save_report(
        state["query"],
        state["analysis"]
    )

    return state

builder = StateGraph(AgentState)

builder.add_node("search", search_node)
builder.add_node("memory", memory_node)
builder.add_node("analysis", analysis_node)
builder.add_node("score", score_node)
builder.add_node("report", report_node)

builder.set_entry_point("search")
builder.add_edge("search", "memory")
builder.add_edge("memory", "analysis")
builder.add_edge("analysis", "score")
builder.add_edge("score", "report")
builder.add_edge("report", END)

graph = builder.compile()

def check_sources(state):

    if len(state["results"]) >= 3:
        return "enough"

    return "search_again"

def check_quality(state):

    if state["score"]["overall"] >= 7:
        return "good"

    return "retry"