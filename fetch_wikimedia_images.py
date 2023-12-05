import os
from pathlib import Path

from dotenv import load_dotenv
from urllib.parse import urlparse, unquote_plus
import requests


def download_image(url, path):
    """Download a photo from a URL at a specific path."""
    path_to_photo = Path(path)
    path_to_photo.mkdir(parents=True, exist_ok=True)
    filename = 'hubble.jpeg'
    headers = {
        'Authorization': f'Bearer {wikimedia_token}',
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


if __name__ == '__main__':
    load_dotenv()
    wikimedia_token = os.getenv("WIKIMEDIA_TOKEN")
