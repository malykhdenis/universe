# universe
Photos of space on Telegram

## Как установить

Python3 должен быть уже установлен.
Используй `pip` чтобы установить зависимости:
```
pip install -r requirements.txt
```
Зарегестрировать бота и получить токены можно по ссылкам:

[BotFather](https://t.me/BotFather)

[NASA](https://api.nasa.gov/)

Следующим шагом будет создать файл .env в директории со скриптом и вставить в него свои токены. Например:
```
NASA_TOKEN='*твой токен*'
```
## bot.py

Публикует фото из дирректории images/ в телеграм канале.

### Как пользоваться скриптом
Введи в терминале:
```
python bot.py *время между публикациями в часах(целое число)*
```
По умолчанию время между публикациями - 4 часа.
