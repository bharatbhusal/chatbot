# handlers.py
import datetime
import pyjokes

day_subject = {
    "Monday": [
        "Hacking",
        "Cryptography",
        "CLAD",
        "CLAD",
        "DAA",
        "Lunch",
        "AI",
        "No class",
    ],
    "Tuesday": [
        "AI",
        "No Class",
        "No Class",
        "No Class",
        "2D Animation",
        "Lunch",
        "AI lab",
        "AI lab",
    ],
    "Wedneshday": [
        "Cryptography",
        "Hacking",
        "No Class",
        "No Class",
        "DAA",
        "Lunch",
        "No Class",
        "No Class",
    ],
    "Thrusday": [
        "No Class",
        "Ai",
        "No Class",
        "No Class",
        "2D Animation",
        "Lunch",
        "Cryptography",
        "Hacking",
    ],
    "Friday": [
        "Hacking Lab",
        "Hacking Lab",
        "2D Animation",
        "No Class",
        "DAA",
        "Lunch",
        "Design Thinking",
        "Design Thinking",
    ]}


class_time = ["8:00-8:50",
            "9:00-9:50",
            "10:00-10:50",
            "11:00-11:50",
            "12:00-12:50",
            "13:00-13:50",
            "14:00-14:50",
            "15:00-15:50",]



def get_today():
    return datetime.date.today().strftime("%A")

def return_routine(day):
    result = f"Routine for {day}:\n"
    for i, each in enumerate(day_subject[day], 1):
        result += f"{i}) {each} at {class_time[i-1]}\n"
    return result


# Define a dictionary to map user input to specific replies
reply_dict = {
    "creator": "LeCal is my creator",
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi! How are you?",
    "how are you": "I'm just a bot, but I'm here to help!",
    "good morning": "Good morning! 🌞",
    "good night": "Good night! 🌙",
    "thank you": "You're welcome! 😊",
    "bye": "Goodbye! Have a great day!",
    "routine": return_routine(get_today()),
    "love you": "Awww, you are the wind below my wings."
    # Add more user input and corresponding replies here
}

# Define a function to handle user input and provide replies
def handle_user_input(user_input):
    if "joke" in user_input:
        return pyjokes.get_joke(language="en", category="neutral")
    else:
        for key, value in reply_dict.items():
            if key in user_input.lower():
                # print(key, value)
                return (value)
    return "I'm not sure how to respond to that."

def reply_to_user_message(bot, message, reply_message):
    bot.reply_to(message, reply_message)
