import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(

    model="llama-3.3-70b-versatile",

    api_key=os.getenv("GROQ_API_KEY")

)

def summarize(results):

    text = ""

    for r in results:

        text += f"""

Title:

{r["title"]}

Content:

{r["content"]}

"""

    prompt = f"""

Summarize the following research.

{text}

"""

    response = llm.invoke(prompt)

    return response.content