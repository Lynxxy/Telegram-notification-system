# Telegram Notification Bot

Бот для Telegram, который при получении любого текстового сообщения — отвечает фотографией.

## Что это

- Бот на Python с использованием библиотеки `python-telegram-bot`.  
- Приём текстовых сообщений и автоматическая отправка заранее заданной фотографии.  
- Всё конфигурируется через `.env`: токен бота и `chat_id`.  

## Как запустить

1. Клонируйте репозиторий:
    ```bash
     git clone https://github.com/Lynxxy/Telegram-notification-system.git
    cd Telegram-notification-system

2. Установите зависимости:

    pip install -r requirements.txt

3. Создайте файл .env в корне проекта с переменными:

    TELEGRAM_BOT_TOKEN=ваш_токен_бота
    TELEGRAM_CHAT_ID=ваш_chat_id

4. Запустите бота:

    python bot.py
    
5. Напишите боту любое сообщение — он должен ответить изображением.