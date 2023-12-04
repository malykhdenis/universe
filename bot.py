import os

from dotenv import load_dotenv
import telegram

load_dotenv()

bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))

print(bot.get_me())

bot.send_message(text='Hi John!', chat_id=-1002127154538)
