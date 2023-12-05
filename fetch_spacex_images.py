from pathlib import Path

import requests
import argparse


def fetch_spacex_last_launch():
    """Download photos from spaceX."""
    Path('images').mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Download photos of SpaceX launches')
    parser.add_argument(
         '-id', default='latest', help='launch id', required=False)
    args = parser.parse_args()
    response_to_spacex = requests.get(
        f'https://api.spacexdata.com/v5/launches/{args.id}')
    response_to_spacex.raise_for_status()
    photos = response_to_spacex.json()['links']['flickr']['original']
    for photo_number, photo in enumerate(photos):
        with open(f'images/spacex_{photo_number}.jpeg', 'wb') as file:
            response_content = requests.get(photo)
            response_content.raise_for_status()
            file.write(response_content.content)


if __name__ == '__main__':
    fetch_spacex_last_launch()
