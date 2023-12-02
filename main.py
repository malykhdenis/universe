import os
from pathlib import Path

from dotenv import load_dotenv
from urllib.parse import urlparse, unquote_plus
import requests
import urllib.parse as up

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


def get_format(url):
	"""Get format of the file by url."""
	parse_path = unquote_plus(urlparse(url).path)
	_, file_format = os.path.splitext(parse_path)
	return file_format



if __name__ == '__main__':
	print(get_format('https://example.com/txt/hello%20world.txt?v=9#python'))