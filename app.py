# [START app]
import logging
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('forms.html')

if __name__ == '__main__':
    app.run()