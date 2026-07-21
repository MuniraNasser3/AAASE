from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.manager_agent import manage
from agents.research_agent import research
from agents.summary_agent import summarize
from agents.writing_agent import write_report
from agents.review_agent import review

from report import save_report
from logger import log

class AgentState(TypedDict):

    topic: str

    research: list

    summary: str

    report: str

def manager_node(state):

    log("Manager Agent")

    return manage(state)

def research_node(state):

    log("Research Agent")

    state["research"] = research(
        state["topic"]
    )

    return state

def summary_node(state):

    log("Summary Agent")

    state["summary"] = summarize(
        state["research"]
    )

    return state

def writing_node(state):

    log("Writing Agent")

    state["report"] = write_report(
        state["summary"]
    )

    return state

def review_node(state):

    log("Review Agent")

    state["report"] = review(
        state["report"]
    )

    return state

def save_node(state):

    log("Saving Report")

    save_report(
        state["report"]
    )

    return state

builder = StateGraph(AgentState)

builder.add_node(
    "manager",
    manager_node
)

builder.add_node(
    "research",
    research_node
)

builder.add_node(
    "summary",
    summary_node
)

builder.add_node(
    "writing",
    writing_node
)

builder.add_node(
    "review",
    review_node
)

builder.add_node(
    "save",
    save_node
)

builder.set_entry_point(
    "manager"
)

builder.add_edge(
    "manager",
    "research"
)

builder.add_edge(
    "research",
    "summary"
)

builder.add_edge(
    "summary",
    "writing"
)

builder.add_edge(
    "writing",
    "review"
)

builder.add_edge(
    "review",
    "save"
)

builder.add_edge(
    "save",
    END
)

graph = builder.compile()