import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path(__file__).parent / 'keys.env'
load_dotenv(dotenv_path)

AK = os.environ.get('api_key_openrouter')
