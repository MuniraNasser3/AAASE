import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="research_memory"
)

def save_sources(results):

    for item in results:

        collection.add(

            ids=[item["url"]],

            documents=[item["content"]],

            metadatas=[
                {
                    "title": item["title"],
                    "url": item["url"]
                }
            ]

        )

def search_memory(question):

    return collection.query(
        query_texts=[question],
        n_results=3
    )