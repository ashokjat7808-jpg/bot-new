import telebot
from flask import Flask, request

TOKEN = "8789588958:AAFmBXyEgd4zlAjDrjhD8zLS7qqhFzyYAGA"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot chal raha hai 🚀")

@app.route('/')
def home():
    return "Bot is running"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://bot-new.onrender.com/" + TOKEN)
    app.run(host="0.0.0.0", port=10000)
