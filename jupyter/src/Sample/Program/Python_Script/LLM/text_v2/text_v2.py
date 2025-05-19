# Import libraries
import sys
import os
from pathlib import Path

# Third-party libraries
from openai import OpenAI

# Custom libraries
from mylib.keys.openrouter import keys_settings

# Model name
model_name = "anthropic/claude-3.7-sonnet"

# Environment settings
work_dir = Path(__file__).parent
prompt_dir = work_dir / "prompt"

# system_prompt
system_prompt_path = prompt_dir / "system_prompt.md"
system_prompt = system_prompt_path.read_text(encoding="utf-8")

# user_prompt
user_prompt_path = prompt_dir / "user_prompt.md"
user_prompt = user_prompt_path.read_text(encoding="utf-8")

# output settings
output_dir = work_dir / "output"
output_path = output_dir / "response.md"
output_dir.mkdir(exist_ok=True)  # Create output directory if it doesn't exist

# Initialize OpenAI client
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=keys_settings.AK,
)

completion = client.chat.completions.create(
  model=model_name,
  messages=[
    {
      "role": "system",
      "content": system_prompt
    },
    {
      "role": "user",
      "content": user_prompt
    },
  ]
)

response_content = completion.choices[0].message.content

# Save response to file
output_path.write_text(response_content, encoding="utf-8")
print(f"Response saved to {output_path}")
