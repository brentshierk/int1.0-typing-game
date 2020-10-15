from flask import Flask, render_template, redirect,url_for,jsonify,request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

DEBUG = True

app = Flask(__name__)

app.config.from_object(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/final_project"
mongo = PyMongo(app)

@app.route('/')
def home_page():
    return render_template('main.html')

@app.route('/about')
def about_page():
    pass

if __name__ == '__main__':
    app.run(debug=True)
