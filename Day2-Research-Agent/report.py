import os

os.makedirs("reports", exist_ok=True)

def save_report(query, analysis):

    filename = "reports/report.md"

    with open(filename, "w", encoding="utf-8") as f:

        f.write(f"# Enterprise Research Report\n\n")

        f.write(f"## Topic\n")

        f.write(query)

        f.write("\n\n")

        f.write(analysis)

    return filename