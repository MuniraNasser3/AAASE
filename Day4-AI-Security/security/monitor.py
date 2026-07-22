import os

from datetime import datetime

os.makedirs("logs", exist_ok=True)

def security_log(

    user,

    prompt,

    status,

    reason

):

    with open(

        "logs/security.log",

        "a"

    ) as f:

        f.write(

            f"""

Time: {datetime.now()}

User: {user}

Status: {status}

Reason: {reason}

Prompt: {prompt}

------------------------

"""

        )