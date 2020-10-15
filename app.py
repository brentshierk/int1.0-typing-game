from flask import Flask, render_template, redirect,url_for,jsonify,request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import random
DEBUG = True

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

def display_words(words_list):
    pass

def words_per_minute():
    minutes = 1
    seconds  = 0
    words = 102

    wpm = words / minutes 
    print('wpm = ',wpm)

words_per_minute()
        
            

        
       



@app.route('/')
def home_page():
    return render_template('main.html')

@app.route('/about')
def about_page():
    pass

get_file_lines('1000.txt')
display_words(words_list)
if __name__ == '__main__':
    app.run(debug=True)