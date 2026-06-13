# using-openai-sdk.py

import os

from openai import OpenAI

LM_STUDIO_BASE_URL = os.getenv(
    "LM_STUDIO_BASE_URL",
    "http://localhost:1234"
)

client = OpenAI(
    base_url=f"{LM_STUDIO_BASE_URL}/v1",
    api_key="lm-studio"
)

response = client.chat.completions.create(
    model="google/gemma-4-e4b",
    messages=[
        {
            "role": "user",
            "content": "Explain what an LLM is in 3 sentences."
        }
    ]
)

print(response.choices[0].message.content)
