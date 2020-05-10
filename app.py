from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('/landing/index.html', title='Home')

@app.route('/about')
def about():
    return render_template('/landing/about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('/landing/contact.html', title='Contact')