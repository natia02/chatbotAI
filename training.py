import json
import random
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
from sklearn.preprocessing import LabelEncoder
import pickle

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()


class Training:
    def __init__(self):
        self.words = []
        self.classes = []
        self.documents = []
        self.ignore_words = list("!@#$%^&*?")
        self.data_file = 'data/intents.json'  # Update path
        self.intents = None
        self.le = LabelEncoder()

    def load_intents(self):
        with open(self.data_file, 'r') as file:
            self.intents = json.load(file)

    def save_intents(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.intents, file, indent=2)  # Use indent=2 for pretty formatting

    def build(self):
        try:
            self.load_intents()  # Load existing intents
            for intent in self.intents['intents']:
                for pattern in intent['patterns']:
                    w = word_tokenize(pattern)
                    self.words.extend(w)
                    self.documents.append((w, intent['tag']))
                    if intent['tag'] not in self.classes:
                        self.classes.append(intent['tag'])

            self.words = sorted(
                list(set(map(lemmatizer.lemmatize, filter(lambda x: x not in self.ignore_words, self.words)))))
            self.classes = sorted(list(set(self.classes)))

            self.training = []
            self.output_empty = [0] * len(self.classes)

            for doc in self.documents:
                bag = []
                pattern_words = doc[0]
                pattern_words = list(map(lemmatizer.lemmatize, pattern_words))
                for w in self.words:
                    bag.append(1) if w in pattern_words else bag.append(0)
                output_row = list(self.output_empty)
                output_row[self.classes.index(doc[1])] = 1
                self.training.append([bag, output_row])

            random.shuffle(self.training)
            self.training = np.array(self.training, dtype=object)
            train_x = np.array(list(self.training[:, 0]))
            train_y = np.array(list(self.training[:, 1]))

            self.model = Sequential()
            self.model.add(Dense(128, input_shape=(train_x.shape[1],), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))

            sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
            self.model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

            self.model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)
            self.model.save('data/chatbot_model.h5')

            pickle.dump({'words': self.words, 'classes': self.classes}, open("data/training_data", "wb"))

            # Example of how to add a new intent
            new_intent = {
                "tag": "new_intent_tag",
                "patterns": ["new pattern 1", "new pattern 2"],
                "responses": ["response 1", "response 2"]
            }
            self.intents['intents'].append(new_intent)

            # Save updated intents to intents.json
            self.save_intents()

            print("Training completed successfully.")
        except Exception as e:
            print(f"An error occurred during training: {str(e)}")
