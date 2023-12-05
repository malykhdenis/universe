import os
from pathlib import Path

from dotenv import load_dotenv
import requests


def fetch_epic_nasa_images():
    """Download photos of Earth from NASA."""
    Path('images/nasa').mkdir(parents=True, exist_ok=True)
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
        with open(f'images/nasa/nasa_earth_{photo_number}.jpeg', 'wb') as file:
            response_content = requests.get(
                (f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/'
                 f'{day}/png/{name}.png'),
                params=payload,
                )
            response_content.raise_for_status()
            file.write(response_content.content)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    fetch_epic_nasa_images()
