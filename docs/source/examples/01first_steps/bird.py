from flask import Flask # import the Flask module
from flask import render_template # import flask module render_template

app = Flask(__name__) # create instance of the class

@app.route('/') # Flask decorator used to show route, in this case default path
def index():
    return render_template('index.html', title='Home of the')