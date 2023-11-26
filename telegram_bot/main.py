# main.py
from config import load_environment, get_bot
from handlers import get_today, handle_user_input, reply_to_user_message

def main():
    load_environment()
    bot = get_bot()


    @bot.message_handler(func=lambda message: True)
    def handle_messages(message):
        user_input = message.text
        reply_message = handle_user_input(user_input)
        reply_to_user_message(bot, message, reply_message)

    print("The bot is live")
    bot.infinity_polling()

if __name__ == "__main__":
    main()
