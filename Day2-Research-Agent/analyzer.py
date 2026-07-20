import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze(query, results):

    text = ""

    for r in results:
        text += f"""
Title:
{r['title']}

Content:
{r['content']}

"""

    prompt = f"""

You are a research analyst.

Research Topic:
{query}

Sources:

{text}

Write:

- Executive Summary

- Key Findings

- Recommendations

"""

    response = llm.invoke(prompt)

    return response.content

def quality_score(results):

    score = min(len(results) * 2, 10)

    return {
        "coverage": score,
        "overall": score
    }