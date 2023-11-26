# main.py
from config import load_environment, get_bot
from handlers import MessageHandler

def main():
    load_environment()
    bot = get_bot()
    message_handler = MessageHandler()


    @bot.message_handler(func=lambda message: True)
    def handle_messages(message):
        user_input = message.text.lower()
        if "leca" in user_input:
            reply_message = message_handler.handle_user_input(user_input)
            message_handler.reply_to_user_message(bot, message, reply_message)

    print("The bot is live")
    bot.infinity_polling()

if __name__ == "__main__":
    main()
