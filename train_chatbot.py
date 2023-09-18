import json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import numpy as np

# Load the dataset from dataset.json
with open('dataset.json', 'r') as file:
    data = json.load(file)

# Extract patterns and responses
patterns = []
responses = []

for pair in data['pairs']:
    for pattern in pair['patterns']:
        patterns.append(pattern.lower())  # Add patterns
        responses.append(pair['responses'][0])  # Add responses

# Tokenize the patterns
tokenizer = Tokenizer(oov_token='<OOV>')
tokenizer.fit_on_texts(patterns)
word_index = tokenizer.word_index

# Create sequences and pad them
sequences = tokenizer.texts_to_sequences(patterns)
padded_sequences = pad_sequences(sequences, maxlen=20, padding='post', truncating='post')

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(len(word_index) + 1, 128),
    tf.keras.layers.LSTM(128),
    tf.keras.layers.Dense(len(responses), activation='softmax')
])

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
X = np.array(padded_sequences)
y = np.array([responses.index(response) for response in responses])
model.fit(X, y, epochs=500, verbose=1)

# Save the model
model.save('chatbot_model')
