import os
from pathlib import Path

from dotenv import load_dotenv
import requests

load_dotenv()

headers = {
  'Authorization': f'Bearer {os.getenv("WIKIMEDIA_TOKEN")}',
}

Path('images').mkdir(parents=True, exist_ok=True)

filename = 'images/hubble.jpeg' 

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

response = requests.get(url, headers=headers)
response.raise_for_status()

with open(filename, 'wb') as file:
  file.write(response.content)