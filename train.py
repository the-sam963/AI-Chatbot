from data import DataLib, get_dataset
import random
import pickle
import json
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD



lemmatizer = WordNetLemmatizer()
patterns, responses = get_dataset()

words = []
classes = []
documents = []
ignore_letters = ['?', '!',',','.']


for i in range(patterns.shape[0]):
    pattern = patterns.iloc[i][0]
    tag = patterns.iloc[i][1]
    
    word_list = nltk.word_tokenize(pattern)
    words.extend(word_list)
    documents.append((word_list, tag))
    if tag not in classes:
        classes.append(tag)
        
        
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))
classes = sorted(set(classes))



pickle.dump(words, open('model/words.pkl', 'wb'))
pickle.dump(classes, open('model/classes.pkl', 'wb'))



training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty) 
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training, dtype=object)

train_x = list(training[:, 0])
train_y = list(training[:, 1])



# Brain
# Brain
# Brain
# Brain

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
history = model.fit(np.array(train_x), np.array(train_y), epochs=20, batch_size=5, verbose=1)
model.save('model/model.h5', history)

print('Done')