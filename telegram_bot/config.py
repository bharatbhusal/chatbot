# config.py
from dotenv import load_dotenv
import os
import telebot

def load_environment():
    if load_dotenv():
        print("Environment variables loaded successfully")
    else:
        print("Bot token not found")

def get_bot():
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    return telebot.TeleBot(BOT_TOKEN)
