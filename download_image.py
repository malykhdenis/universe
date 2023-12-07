import argparse
from pathlib import Path

import requests


def download_image(url, request_params=None, path='images/', name='image'):
    """Download image to directory."""
    Path(path).mkdir(parents=True, exist_ok=True)
    if request_params is None:
        request_params = {}
    response_content = requests.get(url, request_params)
    response_content.raise_for_status()
    with open(f'{path}{name}.jpeg', 'wb') as file:
        file.write(response_content.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download image to directory',
    )
    parser.add_argument(
        'url',
        help='url',
    )
    parser.add_argument(
        '-request_params',
        help='parametrs for request',
        required=False,
    )
    parser.add_argument(
        '-path',
        help='path for saving file',
        required=False,
        default='images/',
    )
    parser.add_argument(
        '-name',
        help='name for new file',
        required=False,
        default='image',
    )
    args = parser.parse_args()
    download_image(args.url, args.request_params, args.path, args.name)
