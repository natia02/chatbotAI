import json
import random
import pickle
import numpy as np
from keras.utils import pad_sequences
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
context = {}


class Testing:
    def __init__(self):
        try:
            self.intents = json.loads(open('data/intents.json').read())
            data = pickle.load(open("data/training_data", "rb"))
            self.words = data['words']
            self.classes = data['classes']
            self.model = load_model('data/chatbot_model.h5')
            self.ERROR_THRESHOLD = 0.4
            self.ignore_words = list("!@#$%^&*?")
            self.max_sequence_length = len(self.words)  # Ensure this matches the training input shape
        except Exception as e:
            print(f"Error initializing Testing: {str(e)}")

    def clean_up_sentence(self, sentence):
        sentence_words = word_tokenize(sentence.lower())
        sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
        return [word for word in sentence_words if word not in self.ignore_words]

    def wordvector(self, sentence):
        sentence_words = self.clean_up_sentence(sentence)

        vector = np.zeros(len(self.words))

        for word in sentence_words:
            if word in self.words:
                vector[self.words.index(word)] = 1

        vector = pad_sequences([vector], maxlen=self.max_sequence_length, padding='post', truncating='post')
        return vector

    def classify(self, sentence):
        vector = self.wordvector(sentence)
        prediction = self.model.predict(vector)[0]
        results = [[i, r] for i, r in enumerate(prediction) if r > self.ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def response(self, sentence, userid='123', show_details=False):
        results = self.classify(sentence)
        if results:
            for i in self.intents['intents']:
                if i['tag'] == self.classes[results[0][0]]:
                    if 'context_set' in i:
                        context[userid] = i['context_set']
                    if not 'context_filter' in i or (
                            userid in context and 'context_filter' in i and i['context_filter'] == context[userid]):
                        response = random.choice(i['responses'])
                        return response
        return "Sorry, I don't understand that."
