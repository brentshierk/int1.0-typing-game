from flask import Flask, render_template, redirect,url_for,jsonify,request
from bson.objectid import ObjectId
import random
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config.from_object(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/final_project"
mongo = PyMongo(app)


"""
read 1000.txt and return list of strings
"""
def get_file_lines(filename):
    filename = open('static/1000.txt', 'r')
    lines = filename.readlines()
    words_list = []
    for i in range(len(lines)):
        words_list.append(lines[i].strip('\n'))
    return words_list

words_list = get_file_lines('static/1000.txt')

def words_per_minute():
    minutes = 1
    #seconds  = 0
    words = 102
    wpm = words / minutes 
    return wpm



    


@app.route('/', methods=['GET','POST'])
def home_page():
    words_list
    list_strings = random.sample(words_list,50)
    prompt = ' '.join(list_strings)
    if request.method =='POST':

        context = {
            'prompt' : prompt,
            'typed_words': request.form.get('typed_words')
        }
        #typing game input is taken and split into strings of single words.
        typed_input = context['typed_words']
        split_input = typed_input.split()
        #split prompt into a list of strings to compare to split input
        given_prompt = context['prompt']
        split_prompt = given_prompt.split(' ')
        compare_list = list(set(split_input) & set(split_prompt))
        print(split_input,'-------------------',split_prompt)

    return render_template('scores.html',**context)



# @app.route('/',methods=['GET', 'POST'])
# def calculations_on_home():
    
   
#     if request.method == 'POST':
#         new_userInput = {
#             'typed_words': request.form.get('typed_words')
#         }
#         alter = new_userInput['typed_words']
#         splitAlter = alter.split()
        

#         #print(new_userInput)
#     return render_template('scores.html',**new_userInput)

#@app.route('/')
# def typing_auccuracy(prompt):
    

#     context = {
#         'prompt' : prompt
#     }

#     return render_template('main.html',**context)







words_per_minute()
get_file_lines('1000.txt')
if __name__ == '__main__':
    app.run(debug=True)