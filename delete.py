from data import DataLib
import pickle
patterns, responses = DataLib()

words = pickle.load(open('model/words.pkl', 'rb'))
classes = pickle.load(open('model/classes.pkl', 'rb'))


response_list = []
for cls in classes:
    
    res_per_class = []
    for i in range(len(responses)):
        if responses.iloc[i][1] == cls:
            res_per_class.append(responses.iloc[i][0])
            
    response_list.append({'class': cls, 'response': res_per_class})


for item in response_list:
    if item['class'] == 'name':
        print(item['response'])
        pass
    elif item['class'] == 'greeting':
        print(item['response'])
        pass
    
# for item in response_list:
#    print(response_list)