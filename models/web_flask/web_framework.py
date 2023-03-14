#!/usr/bin/python3
'''
Diet Buddy Webframework
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_diet_buddy():
    return ("Hello Diet Bud!")

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
