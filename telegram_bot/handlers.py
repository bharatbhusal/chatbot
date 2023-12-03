import datetime
import pyjokes

class RoutineHandler:
    def __init__(self):
        self.day_subject = {
            "Monday": [
                ("Hacking", "8:00-8:50"),
                ("Cryptography", "9:00-9:50"),
                ("CLAD", "10:00-10:50"),
                ("CLAD", "11:00-11:50"),
                ("DAA", "12:00-12:50"),
                ("Lunch", "13:00-13:50"),
                ("AI", "14:00-14:50"),
                ("No class", "15:00-15:50"),
            ],
            "Tuesday": [
                ("AI", "8:00-8:50"),
                ("No Class", "9:00-9:50"),
                ("No Class", "10:00-10:50"),
                ("No Class", "11:00-11:50"),
                ("2D Animation", "12:00-12:50"),
                ("Lunch", "13:00-13:50"),
                ("AI lab", "14:00-14:50"),
                ("AI lab", "15:00-15:50"),
            ],
            "Wednesday": [
                ("Cryptography", "8:00-8:50"),
                ("Hacking", "9:00-9:50"),
                ("No Class", "10:00-10:50"),
                ("No Class", "11:00-11:50"),
                ("DAA", "12:00-12:50"),
                ("Lunch", "13:00-13:50"),
                ("No Class", "14:00-14:50"),
                ("No Class", "15:00-15:50"),
            ],
            "Thursday": [
                ("No Class", "8:00-8:50"),
                ("Ai", "9:00-9:50"),
                ("No Class", "10:00-10:50"),
                ("No Class", "11:00-11:50"),
                ("2D Animation", "12:00-12:50"),
                ("Lunch", "13:00-13:50"),
                ("Cryptography", "14:00-14:50"),
                ("Hacking", "15:00-15:50"),
            ],
            "Friday": [
                ("Hacking Lab", "8:00-8:50"),
                ("Hacking Lab", "9:00-9:50"),
                ("2D Animation", "10:00-10:50"),
                ("No Class", "11:00-11:50"),
                ("DAA", "12:00-12:50"),
                ("Lunch", "13:00-13:50"),
                ("Design Thinking", "14:00-14:50"),
                ("Design Thinking", "15:00-15:50"),
            ]
        }

    def get_today(self):
        return datetime.date.today().strftime("%A")

    def return_routine(self):
        today = self.get_today()
        # today = "Monday"
        try:
            subjects = self.day_subject[today]
        except KeyError:
            return f"Routine not available for {today}."
        
        result = f"Routine for {today}:\n"
        for i, (subject, class_time) in enumerate(self.day_subject[today], 1):
            result += f"{i}) {subject} at {class_time}\n"
        return result


class JokeHandler:
    def get_joke(self):
        try:
            return pyjokes.get_joke(language="en", category="neutral")
        except Exception as e:
            return "Joker is on leave."

class ChatHandler:
    def __init__(self):
        # Use instances of other handlers
        self.routine_handler = RoutineHandler()
        self.joke_handler = JokeHandler()

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
        "love you": "Awww, you are the wind below my wings.",
        # Add more user input and corresponding replies here
    }

    def handle_user_input(self, user_input):
        if "joke" in user_input:
            return self.joke_handler.get_joke()
        elif "routine" in user_input:
            return self.routine_handler.return_routine(self.routine_handler.get_today())
        else:
            for key, value in self.reply_dict.items():
                if key in user_input:
                    return value
        return "I'm not sure how to respond to that."
