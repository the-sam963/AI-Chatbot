import re
from tabnanny import verbose
from data import DataLib
import random
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

lemmatizer = WordNetLemmatizer()
patterns, responses = DataLib()

words = pickle.load(open('model/words.pkl', 'rb'))
classes = pickle.load(open('model/classes.pkl', 'rb'))
model = load_model('model/model.h5')


def get_response_list(responses, classes):
    response_list = []
    for cls in classes:
        res_per_class = []
        for i in range(len(responses)):
            if responses.iloc[i][1] == cls:
                res_per_class.append(responses.iloc[i][0])
            
        response_list.append({'class': cls, 'response': res_per_class})
    return response_list






def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word)  for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words= clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1

    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    print(res)
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda  x:x[1], reverse=True)
    predicted_class = []
    for r in results:
        predicted_class.append({'tag': classes[r[0]], 'probability': str(r[1])})
    return predicted_class


def get_response(_predicted_class, _response):
    tag = _predicted_class[0]['tag']
    response_list = get_response_list(_response, classes)
    response_of_predicted_class =  []
    
    for item in response_list:
        if item['class'] == tag:
            response_of_predicted_class = item['response']
    
    result = random.choice(response_of_predicted_class)
    return result

predicted_class = predict_class('hi')
res = get_response(predicted_class, responses)
print("| Bot:", res)

while True:
    message = input("| You: ")
    if message == "bye" or message == "Goodbye":
        # predicted_class = predict_class(message)
        # res = get_response(predicted_class, responses)
        print("| Bot:", "Bye, see you again")
        print("|===================== The Program End here! =====================|")
        exit()

    else:
        predicted_class = predict_class(message)
        res = get_response(predicted_class, responses)
        print("| Bot:", res)

