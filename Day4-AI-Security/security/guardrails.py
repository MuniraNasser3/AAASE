THREATS = [

    "ignore previous instructions",

    "forget previous instructions",

    "developer message",

    "system prompt",

    "jailbreak",

    "bypass",

    "disable safety",

    "act as"

]

def security_check(prompt):

    text = prompt.lower()

    for threat in THREATS:

        if threat in text:

            return False, threat

    return True, None