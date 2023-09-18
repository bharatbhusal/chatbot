from dotenv import load_dotenv
import os
import telebot
import datetime
# Load environment variables from .env file
if load_dotenv():
    print("Environment variables loaded successfully")
else:
    print("Bot token not found")

# Get the bot token from the environment variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Define a decorator function to register command handlers


def command_handler(command):
    def decorator(func):
        @bot.message_handler(commands=[command])
        def wrapped(message):
            func(message)
        return func
    return decorator

# Define command handlers using the decorator


@command_handler('start')
@command_handler('hello')
def handle_start_hello(message):
    bot.reply_to(message, "Howdy, how are you doing?")

# Define additional command handlers using the decorator


@command_handler('customcommand')
def handle_custom_command(message):
    bot.reply_to(message, "This is a custom command handler.")


routine_time = ["8:00-8:50",
                "9:00-9:50",
                "10:00-10:50",
                "11:00-11:50",
                "12:00-12:50",
                "13:00-13:50",
                "14:00-14:50",
                "15:00-15:50",]

routine_subjects = {
    "0": [
        "Hacking",
        "Cryptography",
        "CLAD",
        "CLAD",
        "DAA",
        "Lunch",
        "AI",
        "No class",
    ],
    "1": [
        "AI",
        "No Class",
        "No Class",
        "No Class",
        "2D Animation",
        "Lunch",
        "AI lab",
        "AI lab",
    ],
    "2": [
        "Cryptography",
        "Hacking",
        "No Class",
        "No Class",
        "DAA",
        "Lunch",
        "No Class",
        "No Class",
    ],
    "3": [
        "No Class",
        "Ai",
        "No Class",
        "No Class",
        "2D Animation",
        "Lunch",
        "Cryptography",
        "Hacking",
    ],
    "4": [
        "Hacking Lab",
        "Hacking Lab",
        "2D Animation",
        "No Class",
        "DAA",
        "Lunch",
        "Design Thinking",
        "Design Thinking",
    ],
}

# Get today's date
today = datetime.date.today()

# structure a string to return a routine.


def return_string(day_num):
    if day_num == 0:
        day = "Monday"
    elif day_num == 1:
        day = "Tuesday"
    elif day_num == 2:
        day = "Wednesday"
    elif day_num == 3:
        day = "Thrusday"
    elif day_num == 4:
        day = "Friday"

    result = f"Routine for {day}:\n"
    for i, each in enumerate(routine_subjects[str(day_num)], 1):
        result += f"{i}) {each} at {routine_time[i-1]} in bla\n"
    return result


# Define a dictionary to map user input to specific replies
reply_dict = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm here to help!",
    "good morning": "Good morning! 🌞",
    "good night": "Good night! 🌙",
    "thank you": "You're welcome! 😊",
    "bye": "Goodbye! Have a great day!",
    "routine": return_string(today.weekday()),
    # Add more user input and corresponding replies here
}

# Define a function to handle user input and provide replies


def handle_user_input(user_input):
    for key, value in reply_dict.items():
        if key in user_input.lower():
            # print(key, value)
            return (value)
    return "I'm not sure how to respond to that."


# Define a message handler to reply based on user input


@bot.message_handler(func=lambda message: True)
def reply_to_user_message(message):
    user_input = message.text
    reply_message = handle_user_input(user_input)
    bot.reply_to(message, reply_message)


# Start the bot's polling loop
if __name__ == "__main__":
    print("The bot is live")
    bot.infinity_polling()
