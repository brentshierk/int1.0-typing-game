from flask import Flask, render_template, redirect,url_for,jsonify,request
from bson.objectid import ObjectId
import random
DEBUG = True

app = Flask(__name__)

app.config.from_object(__name__)


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


@app.route('/')
def home_page():
    words_list
    list_strings = random.sample(words_list,50)
    prompt = ' '.join(list_strings)

    context = {
        'prompt' : prompt
    }

    return render_template('main.html',**context)

@app.route('/about')
def about_page():
    pass
words_per_minute()
get_file_lines('1000.txt')
if __name__ == '__main__':
    app.run(debug=True)