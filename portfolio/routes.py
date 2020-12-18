from flask import render_template
from portfolio import app


@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')
