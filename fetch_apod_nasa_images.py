import os
from pathlib import Path

from dotenv import load_dotenv
import requests


def fetch_apod_nasa_images(nasa_token, images_number=5):
    """Download photos from NASA."""
    Path('images/nasa').mkdir(parents=True, exist_ok=True)
    payload = {
        'api_key': nasa_token,
        'count': images_number,  # number of images for downloading
    }
    response_nasa = requests.get(
        'https://api.nasa.gov/planetary/apod',
        params=payload
    )
    response_nasa.raise_for_status()
    photos = response_nasa.json()
    for photo_number, photo in enumerate(photos):
        response_content = requests.get(photo['url'])
        response_content.raise_for_status()
        with open(f'images/nasa/nasa_apod_{photo_number}.jpeg', 'wb') as file:
            file.write(response_content.content)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    fetch_apod_nasa_images(nasa_token)
