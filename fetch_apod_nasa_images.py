import os
from pathlib import Path

from dotenv import load_dotenv
import requests

NUMBER_IMG = 30  # number of images for downloading


def fetch_apod_nasa_images():
    """Download photos from NASA."""
    Path('images/nasa').mkdir(parents=True, exist_ok=True)
    payload = {
        'api_key': nasa_token,
        'count': NUMBER_IMG,
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


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    fetch_apod_nasa_images()
