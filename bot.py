import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

# Загружаем переменные из .env
load_dotenv()

# Получаем токен и chat_id из .env
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Проверка на наличие переменных
if not TOKEN or not CHAT_ID:
    raise ValueError("Токен или chat_id не были найдены в .env файле!")

async def start(update, context):
    """Обработчик команды /start"""
    await update.message.reply_text('Привет, мир!')

async def main():
    # Инициализируем асинхронного бота
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Отправляем сообщение
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="Привет, мир!")

    # Запускаем бота
    await application.run_polling()

# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
