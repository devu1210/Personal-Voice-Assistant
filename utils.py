import re

def normalize(text):
    text = text.lower().strip()

    text = re.sub(r"[^\w\s]", "", text)

    text = re.sub(r"\s+", " ", text)

    return text

import re

def extract_city(text):
    text = text.lower()

    patterns = [
        r"city is (.+)",
        r"weather in (.+)",
        r"weather of (.+)",
        r"in (.+)",
        r"for (.+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).title()

    return text.title()