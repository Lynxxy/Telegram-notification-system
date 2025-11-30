import os
from dotenv import load_dotenv
from telegram import Bot
from telegram.ext import Application, MessageHandler, filters

# Загружаем переменные из .env
load_dotenv()

# Получаем токен и chat_id из .env
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Проверка на наличие переменных
if not TOKEN or not CHAT_ID:
    raise ValueError("Токен или chat_id не были найдены в .env файле!")

async def handle_message(update, context):
    """Обработчик текстовых сообщений: бот отправляет фотографию"""
    photo_path = 'src/test_image.png'  # Путь к фотографии, которую будет отправлять бот
    
    print(f"Получено сообщение от {update.message.from_user.username}: {update.message.text}")

    # Отправляем фотографию в ответ на любое сообщение
    await update.message.reply_photo(photo=open(photo_path, 'rb'))

def main():
    """Основная функция для запуска бота"""
    print("Бот запускается...")
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("Бот слушает сообщения...")
    # Запускаем бота
    application.run_polling()

# Запуск бота
if __name__ == '__main__':
    print("Запуск бота...")
    main()
