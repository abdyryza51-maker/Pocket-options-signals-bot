
import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Не задан токен бота BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    keyboard.row("Выбрать пару")
    keyboard.row("5 секунд", "15 секунд")
    keyboard.row("1 минута", "5 минут")

    bot.send_message(
        message.chat.id,
        "Привет! Я бот сигналов Pocket Option OTC.\n"
        "Выбери время или нажми «Выбрать пару».\n\n"
        "Важно: реальные котировки OTC пока не подключены.",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Выбрать пару":
        bot.reply_to(
            message,
            "Выбор OTC-пар пока не подключён."
        )
    elif message.text in [
        "5 секунд", "15 секунд",
        "1 минута", "5 минут"
    ]:
        bot.reply_to(
            message,
            "Для времени: " + message.text + "\n"
            "Реальный анализ OTC пока не подключён, "
            "поэтому достоверный сигнал сейчас недоступен."
        )
    else:
        bot.reply_to(
            message,
            "Нажми /start, чтобы открыть меню."
        )

bot.infinity_polling()
