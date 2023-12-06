import os

from dotenv import load_dotenv
import requests

from download_image import download_image


def fetch_epic_nasa_images(nasa_token):
    """Download photos of Earth from NASA."""
    payload = {
        'api_key': nasa_token,
    }
    response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural/images',
        params=payload
    )
    response.raise_for_status()
    photos = response.json()
    for photo_number, photo in enumerate(photos):
        name = photo['image']
        date = photo['date'].split()[0]
        year, month, day = date.split('-')
        download_image(
            (f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/'
             f'{day}/png/{name}.png'),
            request_params=payload,
            name=f'nasa_earth_{photo_number}',
        )


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    fetch_epic_nasa_images(nasa_token)
