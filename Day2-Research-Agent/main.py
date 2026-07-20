from graph import graph

query = input("Research topic: ")

state = {
    "query": query,
    "results": [],
    "analysis": "",
    "score": {}
}

result = graph.invoke(state)

print("\n========== AI ANALYSIS ==========\n")
print(result["analysis"])

print("\n========== QUALITY SCORE ==========\n")
print(result["score"])

print("\nReport saved in reports/report.md")