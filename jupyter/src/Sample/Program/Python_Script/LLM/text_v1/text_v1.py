# Import libraries
import sys
import os

# Third-party libraries
from openai import OpenAI

# Custom libraries
from mylib.keys.openrouter import keys_settings

model_name = "anthropic/claude-3.7-sonnet"

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=keys_settings.AK,
)

completion = client.chat.completions.create(
  model=model_name,
  messages=[
    {
      "role": "user",
      "content": "こんにちは"
    }
  ]
)
print(completion.choices[0].message.content)
