import os
from pathlib import Path

from dotenv import load_dotenv
import requests

load_dotenv()


def download_image(url, path, filename):
	"""Download a photo from a URL at a specific path."""
	path_to_photo = Path(path)
	path_to_photo.mkdir(parents=True, exist_ok=True)
	response = requests.get(url)
	response.raise_for_status()
	with open(f'{path_to_photo}/{filename}.jpeg', 'wb') as file:
  		file.write(response.content)


if __name__ == '__main__':
	response = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
	response.raise_for_status()
	photos = response.json()['links']['flickr']['original']
	photo_number = 0
	for photo in photos:
		download_image(photo, 'images', f'spacex_{photo_number}')
		photo_number += 1