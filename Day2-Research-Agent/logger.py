import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

def log(message):

    with open("logs/execution.log", "a") as f:

        f.write(
            f"{datetime.now()} - {message}\n"
        )