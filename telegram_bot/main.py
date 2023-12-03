# main.py
import random
import telebot
from config import load_environment, get_bot
from handlers import  JokeHandler, RoutineHandler, GeneralChatHandler, MessageHandler

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
        general_chat_handler = GeneralChatHandler()
        message_handler = MessageHandler(bot)
        
        # Register joke message handler
        @bot.message_handler(func=lambda message: "joke" in message.text.lower())
        def handle_joke_replies(message):
            """
            Handle incoming messages containing the word "joke".
            """
            reply_message = joke_handler.get_joke()
            bot.reply_to(message, reply_message)
        
        # Register routine message handler
        @bot.message_handler(func=lambda message: "routine" in message.text.lower())
        def handle_routine_replies(message):
            """
            Handle incoming messages containing the word "routine".
            """
            reply_message = routine_handler.return_routine()
            bot.reply_to(message, reply_message)
        
        # Register general message handler
        @bot.message_handler(func=lambda message: "leca" in message.text.lower())
        def handle_routine_replies(message):
            """
            Handle incoming messages containing the word "leca".
            """
            reply_message = general_chat_handler.handle_user_input(message.text)
            bot.reply_to(message, reply_message)


         
# =-======================-======================-======================-=====================

        # Register welcome message handler
        @bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
        def handle_new_members(message):
            message_handler.handle_new_members(message)

        # Register message handler for non-command messages
        @bot.message_handler(func=lambda message: True, content_types=['text'])
        def handle_text_messages(message):
            message_handler.handle_text_messages(message)


        # # Function to generate random numbers for incorrect options
        # def generate_random_numbers():
        #     options = [str(random.randint(1, 100)), str(random.randint(1, 100))]
        #     return options

        # # Register welcome message handler
        # @bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
        # def handle_new_members(message):
        #     chat_id = message.chat.id
        #     new_members = message.new_chat_members

        #     for member in new_members:
        #         user_id = member.id
        #         first_name = member.first_name
        #         username = member.username

        #         # Restrict all permissions for the new member
        #         bot.restrict_chat_member(chat_id, user_id,
        #                                 can_send_messages=False,
        #                                 can_send_media_messages=False,
        #                                 can_send_polls=False,
        #                                 can_send_other_messages=False,
        #                                 can_add_web_page_previews=False,
        #                                 can_change_info=False,
        #                                 can_invite_users=False,
        #                                 can_pin_messages=False)

        #         # Generate random numbers for incorrect options
        #         incorrect_options = generate_random_numbers()

        #         # Correct answer
        #         correct_answer = str(random.randint(1, 100))

        #         # Shuffle the options
        #         options = [correct_answer] + incorrect_options
        #         random.shuffle(options)

        #         # Create keyboard markup with three buttons
        #         markup = telebot.types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        #         for option in options:
        #             markup.add(telebot.types.KeyboardButton(option))

        #         # Do something with the new member information
        #         print(f"New member joined: {first_name} (@{username}), ID: {user_id}")

        #         # Send the welcome message with buttons
        #         welcome_message = (
        #             f"Welcome, {first_name}! Thanks for joining! "
        #             f"Please answer the following question to enter the group.\n"
        #             f"What is the correct answer?\n"
        #         )
        #         bot.send_message(chat_id, welcome_message, reply_markup=markup)




# =-======================-======================-======================-=====================
        # Register farewale message handler
        @bot.message_handler(func=lambda message: message.chat.type in ['group', 'supergroup'], content_types=['left_chat_member'])
        def handle_left_member(message):
            chat_id = message.chat.id
            left_member = message.left_chat_member

            user_id = left_member.id
            first_name = left_member.first_name
            username = left_member.username
           
            # Do something with the left member information
            print(f"Member left: {first_name} (@{username}), ID: {user_id}")

            # You can send a farewell message or perform other actions here
            farewell_message = f"Goodbye, {first_name}! We'll miss you!"
            bot.send_message(chat_id, farewell_message)


        
        print("The bot is live")

        # Start infinite polling
        bot.infinity_polling()

    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
