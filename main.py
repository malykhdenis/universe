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


def get_format(url):
    """Get format of the file by url."""
    parse_path = unquote_plus(urlparse(url).path)
    _, file_format = os.path.splitext(parse_path)
    return file_format


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
