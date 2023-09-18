import json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import numpy as np
import random  # Import the random module

# Load the model
model = tf.keras.models.load_model('chatbot_model')

# Load the dataset from dataset.json
with open('dataset.json', 'r') as file:
    data = json.load(file)

# Extract patterns and responses
patterns = []
responses = []

for pair in data['pairs']:
    for pattern in pair['patterns']:
        patterns.append(pattern.lower())  # Add patterns
        responses.append(pair['responses'])  # Add responses as lists

# Tokenize the patterns
tokenizer = Tokenizer(oov_token='<OOV>')
tokenizer.fit_on_texts(patterns)
word_index = tokenizer.word_index

# Function to predict a random response from the array of responses
def predict_response(text):
    text = text.lower()
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=20, padding='post', truncating='post')
    predicted_probs = model.predict(np.array(padded_sequence))[0]
    predicted_response_index = np.argmax(predicted_probs)
    
    # Get a random response from the array of responses
    random_response = random.choice(responses[predicted_response_index])
    
    return random_response

# Main chat loop
print("Chatbot: Hello! How can I assist you today? (Type 'exit' to end)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = predict_response(user_input)
    print("Chatbot:", response)
