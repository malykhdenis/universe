from pathlib import Path

import requests
import argparse


def fetch_spacex_last_launch():
    """Download photos from spaceX."""
    Path('images').mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument(
         '-id', default='latest', help='launch id', required=False)
    args = parser.parse_args()
    response_to_spacex = requests.get(
        f'https://api.spacexdata.com/v5/launches/{args.id}')
    response_to_spacex.raise_for_status()
    photos = response_to_spacex.json()['links']['flickr']['original']
    photo_number = 0
    for photo in photos:
        with open(f'images/spacex_{photo_number}.jpeg', 'wb') as file:
            file.write(requests.get(photo).content)
        photo_number += 1


if __name__ == '__main__':
    fetch_spacex_last_launch()
