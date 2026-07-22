from graph import graph

topic = input("Research Topic: ")

state = {

    "user": "guest",

    "topic": topic,

    "allowed": False,

    "reason": "",

    "research": [],

    "summary": "",

    "report": ""

}

result = graph.invoke(state)

print()

print("=" * 60)

print("Incoming Request")

print(f"User: {result['user']}")

print(f"Prompt: {result['topic']}")

print()

if result["allowed"]:

    print("[SUCCESS]")

    print()

    print(result["report"])

else:

    print("[BLOCKED]")

    print()

    print(f"Threat detected: {result['reason']}")

print()

print("=" * 60)