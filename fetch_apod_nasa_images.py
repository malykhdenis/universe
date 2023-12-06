import argparse
import os

from dotenv import load_dotenv
import requests

from download_image import download_image


def fetch_apod_nasa_images(nasa_token, images_number=5):
    """Download photos from NASA."""
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
        download_image(photo['url'], name=f'nasa_apod_{photo_number}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download photos from NASA',
    )
    parser.add_argument(
        'images_number',
        default=5,
        help='number of images for downloading',
        nargs='?',
    )
    args = parser.parse_args()
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    fetch_apod_nasa_images(nasa_token, *args)
