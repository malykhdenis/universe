import os
from pathlib import Path

import requests

Path("images").mkdir(parents=True, exist_ok=True)

headers = {
  'Authorization': f'Bearer {os.environ["WIKIMEDIA_TOKEN"]}',
}

filename = 'hubble.jpeg'
url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

response = requests.get(url, headers=headers)
response.raise_for_status()

with open(filename, 'wb') as file:
  file.write(response.content)