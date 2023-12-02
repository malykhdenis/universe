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


def fetch_spacex_last_launch():
	"""Download photos from spaceX."""
	Path('images').mkdir(parents=True, exist_ok=True)
	response_to_spacex = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
	response_to_spacex.raise_for_status()
	photos = response_to_spacex.json()['links']['flickr']['original']
	photo_number = 0
	for photo in photos:
		with open(f'images/spacex_{photo_number}.jpeg', 'wb') as file:
  			file.write(requests.get(photo).content)
		photo_number += 1


if __name__ == '__main__':
	fetch_spacex_last_launch()