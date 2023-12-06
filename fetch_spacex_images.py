import requests
import argparse

from download_image import download_image


def fetch_spacex_last_launch(id='latest'):
    """Download photos from spaceX."""
    response_to_spacex = requests.get(
        f'https://api.spacexdata.com/v5/launches/{id}')
    response_to_spacex.raise_for_status()
    photos = response_to_spacex.json()['links']['flickr']['original']
    for photo_number, photo in enumerate(photos):
        download_image(photo, name=f'spacex_{photo_number}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download photos of SpaceX launches')
    parser.add_argument(
         '-id', default='latest', help='launch id', required=False)
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)
