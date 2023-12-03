import os
from pathlib import Path

from dotenv import load_dotenv
from urllib.parse import urlparse, unquote_plus
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


def get_format(url):
	"""Get format of the file by url."""
	parse_path = unquote_plus(urlparse(url).path)
	_, file_format = os.path.splitext(parse_path)
	return file_format


def download_nasa_images():
	"""Download photos from NASA."""
	Path('images/nasa').mkdir(parents=True, exist_ok=True)
	payload = {
		'api_key': os.getenv('NASA_TOKEN'),
		'count': 30,
	}
	response_nasa = requests.get(
		'https://api.nasa.gov/planetary/apod',
		params=payload
	)
	response_nasa.raise_for_status()
	photos = response_nasa.json()
	photo_number = 0
	for photo in photos:
		with open(f'images/nasa/nasa_apod_{photo_number}.jpeg', 'wb') as file:
  			file.write(requests.get(photo['url']).content)
		photo_number += 1


def download_epic_photo():
	"""Download photos of Earth from NASA."""
	Path('images/nasa').mkdir(parents=True, exist_ok=True)
	payload = {
		'api_key': os.getenv('NASA_TOKEN'),
	}
	response = requests.get(
		'https://api.nasa.gov/EPIC/api/natural/images',
		params=payload
	)
	response.raise_for_status()
	photos = response.json()
	photo_number = 0
	for photo in photos:
		name = photo['image']
		date = photo['date'].split()[0]
		year, month, day = date.split('-')
		with open(f'images/nasa/nasa_earth_{photo_number}.jpeg', 'wb') as file:
  			file.write(
				requests.get(
					f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{name}.png',
					params=payload
				).content)
		photo_number += 1


if __name__ == '__main__':
	download_epic_photo()