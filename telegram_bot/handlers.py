import random
import datetime
import pyjokes
import telebot
import time
import re

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

class GeneralChatHandler:
    def __init__(self):
    # Define a dictionary to map user input to specific replies
        self.reply_dict = {
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
        for key, value in self.reply_dict.items():
            if key in user_input:
                return value
        return "I'm not sure how to respond to that."



class MessageHandler:
    def __init__(self, bot):
        self.bot = bot
        self.user_verification_status = {}

    def generate_addition_question(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
        return f"What is the sum of {num1} and {num2}?", str(correct_answer)

    def handle_new_members(self, message):
        chat_id = message.chat.id
        new_members = message.new_chat_members

        for member in new_members:
            user_id = member.id
            first_name = member.first_name

            # Generate an addition question
            question, correct_answer = self.generate_addition_question()

            # Store the correct answer for verification
            self.user_verification_status[user_id] = correct_answer

            # Send the welcome message with the addition question
            welcome_message = (
                f"Welcome, {first_name}! Thanks for joining!\n"
                f"Please answer the following question within 60 seconds to enter the group:\n\n"
                f"{question}"
            )
            sent_message = self.bot.send_message(chat_id, welcome_message)

            # Set a timer for 60 seconds
            time.sleep(60)

            # Check if the user has provided a correct answer during the time window
            if user_id in self.user_verification_status:
                # Ban the user if they haven't provided a correct answer
                self.bot.kick_chat_member(chat_id, user_id)
                self.bot.send_message(chat_id, f"User {first_name} (@{member.username}) has been banned for failing verification.")
                del self.user_verification_status[user_id]  # Remove user from verification status
            else:
                # Allow the user to send messages
                self.bot.send_message(chat_id, "Verification successful! You can now send messages.")

    def handle_text_messages(self, message):
        user_id = message.from_user.id
        chat_id = message.chat.id

        # Check if the user has been verified
        if user_id in self.user_verification_status:
            # Check if the message contains only numeric values
            if not re.match("^\d+$", message.text.strip()):
                # Delete the message that contains non-numeric values
                self.bot.delete_message(chat_id, message.message_id)
            else:
                # Get the correct answer for the user
                correct_answer = self.user_verification_status[user_id]

                # Check if the user's response is correct
                if message.text.strip() == correct_answer:
                    self.bot.send_message(chat_id, "Verification successful! You can now send messages.")
                    # Allow the user to send other texts by removing them from the verification status
                    del self.user_verification_status[user_id]
                else:
                    self.bot.delete_message(chat_id, message.message_id)
