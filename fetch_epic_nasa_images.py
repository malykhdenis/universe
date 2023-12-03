import os
from pathlib import Path

from dotenv import load_dotenv
import requests

load_dotenv()


def fetch_epic_nasa_images():
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
            file.write(requests.get(
                (f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/'
                 f'{day}/png/{name}.png'),
                params=payload,
                ).content)
        photo_number += 1


if __name__ == '__main__':
    fetch_epic_nasa_images()
