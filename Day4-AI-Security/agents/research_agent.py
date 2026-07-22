import os

from dotenv import load_dotenv

from tavily import TavilyClient

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def research(topic):

    response = client.search(

        query=topic,

        max_results=5,

        search_depth="advanced"

    )

    return response["results"]