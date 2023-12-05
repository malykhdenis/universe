import argparse
import os
import random
import time

from dotenv import load_dotenv
import telegram


def public_image():
    """Public random image from folder images/."""
    parser = argparse.ArgumentParser(
        description='Public image from image/')
    parser.add_argument(
            'hours',
            nargs='?',
            default=4,
            type=int,
            help='hours of delay',
    )
    args = parser.parse_args()
    path, dirs, images = tuple(os.walk('images/'))[0]
    while True:
        path_to_file = os.path.join(path, random.choice(images))
        if os.path.getsize(path_to_file) / 1_048_567 > 20:
            continue
        bot.send_photo(
            chat_id=telegram_channel_id,
            photo=open(f'{path_to_file}', 'rb'),
        )
        time.sleep(3600 * args.hours)


if __name__ == '__main__':
    load_dotenv()
    bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))
    telegram_channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
    public_image()
