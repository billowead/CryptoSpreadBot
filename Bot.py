import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я CryptoSpreadBot. Напиши /spread для примера.")

def spread(update: Update, context: CallbackContext):
    update.message.reply_text("Спред BTC/USDT между Binance и Coinbase: 2.5%")

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        print("Ошибка: TELEGRAM_TOKEN не задан!")
        return

    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("spread", spread))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
