import argparse
import os
import random
import time

from dotenv import load_dotenv
import telegram


def public_image(telegram_token, telegram_channel_id):
    """Public in Telegram channel random image from folder images/."""
    bytes_in_megabyte = 1_048_567
    max_file_size = 20  # Maximum size of file for uploading in Telegram in MB
    bot = telegram.Bot(telegram_token)
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
        if os.path.getsize(path_to_file) / bytes_in_megabyte > max_file_size:
            continue
        with open(f'{path_to_file}', 'rb') as photo:
            bot.send_photo(
                chat_id=telegram_channel_id,
                photo=photo,
            )
        time.sleep(3600 * args.hours)


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
    public_image(telegram_token, telegram_channel_id)
