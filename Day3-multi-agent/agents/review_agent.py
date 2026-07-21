import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(

    model="llama-3.3-70b-versatile",

    api_key=os.getenv("GROQ_API_KEY")

)

def review(report):

    prompt = f"""

Review this report.

Improve grammar.

Improve formatting.

Improve clarity.

Report:

{report}

"""

    response = llm.invoke(prompt)

    return response.content