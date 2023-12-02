import os
from pathlib import Path

from dotenv import load_dotenv
import requests

load_dotenv()


def download_image(url, path):
	"""Download a photo from a URL at a specific path."""
	path_to_photo = Path(path)
	path_to_photo.mkdir(parents=True, exist_ok=True)
	filename = 'hubble.jpeg'
	headers = {
  		'Authorization': f'Bearer {os.getenv("WIKIMEDIA_TOKEN")}',
	}
	response = requests.get(url, headers=headers)
	response.raise_for_status()
	with open(f'{path_to_photo}/{filename}', 'wb') as file:
  		file.write(response.content)


if __name__ == '__main__':
	url = input('url: ')
	path = input('path: ')
	download_image(url, path)