# main.py
from config import load_environment, get_bot
from handlers import  JokeHandler, RoutineHandler

def main():
    """
    Main function to start the Telegram bot.
    """
    try:
        # Load environment variables
        load_environment()

        # Get a bot instance
        bot = get_bot()

        # Create instances of handlers
        joke_handler = JokeHandler()
        routine_handler = RoutineHandler()
        
        @bot.message_handler(func=lambda message: "joke" in message.text.lower())
        def handle_joke_replies(message):
            """
            Handle incoming messages containing the word "joke".
            """
            reply_message = joke_handler.get_joke()
            bot.reply_to(message, reply_message)
        
        
        # Register message handler
        @bot.message_handler(func=lambda message: "routine" in message.text.lower())
        def handle_routine_replies(message):
            """
            Handle incoming messages containing the word "routine".
            """
            reply_message = routine_handler.return_routine()
            bot.reply_to(message, reply_message)



        print("The bot is live")

        # Start infinite polling
        bot.infinity_polling()

    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
