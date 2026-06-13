# using-http-request.py

import json
import os

import requests

LM_STUDIO_BASE_URL = os.getenv(
    "LM_STUDIO_BASE_URL",
    "http://localhost:1234"
)

response = requests.post(
    f"{LM_STUDIO_BASE_URL}/v1/chat/completions",
    json={
        "model": "google/gemma-4-e4b",
        "messages": [
            {
                "role": "user",
                "content": "Explain what an LLM is in 3 sentences."
            }
        ]
    },
    timeout=180
)

response.raise_for_status()

print(
    response.json()["choices"][0]["message"]["content"]
)
