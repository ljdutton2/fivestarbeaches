from flask import Flask, render_template, request, redirect, url_for
import requests


app = Flask(__name__)
FLASK_APP = app


@app.route('/',methods=['GET'])
def show_home():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/about',methods=['GET'])
def about():
    if request.method == 'GET':
        return render_template('other.html')

@app.route('/featured',methods=['GET'])
def featured():
    if request.method == 'GET':
        return render_template('featured.html')



if __name__ == '__main__':
    app.debug = True
    app.run()