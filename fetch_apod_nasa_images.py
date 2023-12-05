import os
from pathlib import Path

from dotenv import load_dotenv
import requests

NUMBER_IMG = 5  # number of images for downloading


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
    for photo_number, photo in enumerate(photos):
        with open(f'images/nasa/nasa_apod_{photo_number}.jpeg', 'wb') as file:
            response_content = requests.get(photo['url'])
            response_content.raise_for_status()
            file.write(response_content.content)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    fetch_apod_nasa_images()
