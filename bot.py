import os

from dotenv import load_dotenv
import telegram

load_dotenv()

bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))

print(bot.get_me())

channel_id = -1002127154538

bot.send_message(chat_id=channel_id, text='This is NASA!')

bot.send_photo(
    chat_id=channel_id,
    photo='https://apod.nasa.gov/apod/image/2107/LRVBPIX3M82Crop1024.jpg',
)
