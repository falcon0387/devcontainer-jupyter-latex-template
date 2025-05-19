# Import libraries
import sys
import os

# Third-party libraries
from openai import OpenAI
from pathlib import Path
import base64

# Custom libraries
from mylib.keys.openrouter import keys_settings

# Model name
model_name = "openai/gpt-4.1"

# Environment settings
work_dir = Path(__file__).parent
prompt_dir = work_dir / "prompt"

# system_prompt
system_prompt_path = prompt_dir / "system_prompt.md"
system_prompt = system_prompt_path.read_text(encoding="utf-8")

# user_prompt
user_prompt_path = prompt_dir / "user_prompt.md"
user_image_path = prompt_dir / "user_image.png"
user_prompt = user_prompt_path.read_text(encoding="utf-8")

# output settings
output_dir = work_dir / "output"
output_path = output_dir / "response.md"
output_dir.mkdir(exist_ok=True)  # Create output directory if it doesn't exist

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image(user_image_path)

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
      "content": [
        {
          "type": "text",
          "text": user_prompt
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    },
  ]
)

response_content = completion.choices[0].message.content

# Save response to file
output_path.write_text(response_content, encoding="utf-8")
print(f"Response saved to {output_path}")
