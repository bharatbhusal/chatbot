import datetime
import pyjokes

class MessageHandler:
    def __init__(self):
        self.day_subject = {
            "Monday": [
                "Hacking", "Cryptography", "CLAD", "CLAD", "DAA", "Lunch", "AI", "No class",
            ],
            "Tuesday": [
                "AI", "No Class", "No Class", "No Class", "2D Animation", "Lunch", "AI lab", "AI lab",
            ],
            "Wednesday": [
                "Cryptography", "Hacking", "No Class", "No Class", "DAA", "Lunch", "No Class", "No Class",
            ],
            "Thursday": [
                "No Class", "Ai", "No Class", "No Class", "2D Animation", "Lunch", "Cryptography", "Hacking",
            ],
            "Friday": [
                "Hacking Lab", "Hacking Lab", "2D Animation", "No Class", "DAA", "Lunch", "Design Thinking", "Design Thinking",
            ]
        }

        self.class_time = [
            "8:00-8:50", "9:00-9:50", "10:00-10:50", "11:00-11:50",
            "12:00-12:50", "13:00-13:50", "14:00-14:50", "15:00-15:50",
        ]

    def get_today(self):
        return datetime.date.today().strftime("%A")

    def return_routine(self, day):
        result = f"Routine for {day}:\n"
        for i, each in enumerate(self.day_subject[day], 1):
            result += f"{i}) {each} at {self.class_time[i-1]}\n"
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
        "love you": "Awww, you are the wind below my wings.",
        # Add more user input and corresponding replies here
    }

    def handle_user_input(self, user_input):
        if "joke" in user_input:
            return pyjokes.get_joke(language="en", category="neutral")
        elif "routine" in user_input:
            return self.return_routine(self.get_today())
        else:
            for key, value in self.reply_dict.items():
                if key in user_input:
                    return value
        return "I'm not sure how to respond to that."

    def reply_to_user_message(self, bot, message, reply_message):
        bot.reply_to(message, reply_message)

class BanHandler:
    def ban_user_by_reply(self, bot, message):
        # Ban the user who sent the message being replied to
        user_id = message.from_user.id
        chat_id = message.chat.id
        # bot.ban_chat_member(user_id, chat_id)
        # Replace the print statement with your actual banning logic
        print(f"Banning user with ID {user_id} based on reply.")
        return f"Banned user with ID {user_id} based on reply."

    def ban_user_by_id(self, user_id):
        # Ban the user with the provided user ID
        # Replace the print statement with your actual banning logic
        print(f"Banning user with ID {user_id} based on user ID.")
        return f"Banned user with ID {user_id} based on user ID."

    def ban_user_by_username(self, username):
        # Ban the user with the provided username
        # Replace the print statement with your actual banning logic
        print(f"Banning user with username {username}.")
        return f"Banned user with username {username}."

    def mass_ban_user_by_id(self, user_ids):
        # Ban multiple users by their user IDs
        # Replace the print statement with your actual mass banning logic
        for user_id in user_ids:
            print(f"Banning user with ID {user_id}.")
        return f"Mass banned {len(user_ids)} users by user ID."

    def mass_ban_user_by_username(self, usernames):
        # Ban multiple users by their usernames
        # Replace the print statement with your actual mass banning logic
        for username in usernames:
            print(f"Banning user with username {username}.")
        return f"Mass banned {len(usernames)} users by username."
