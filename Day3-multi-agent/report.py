import os

os.makedirs("reports", exist_ok=True)

def save_report(report):

    with open("reports/report.md", "w", encoding="utf-8") as f:

        f.write(report)