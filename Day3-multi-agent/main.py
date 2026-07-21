from graph import graph

topic = input("Research Topic: ")

state = {

    "topic": topic,

    "research": [],

    "summary": "",

    "report": ""

}

result = graph.invoke(state)

print("\nFinal Report\n")

print(result["report"])