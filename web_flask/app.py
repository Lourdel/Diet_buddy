#!/usr/bin/python3

"""Module implements flask application"""

from flask import Flask, render_template


app = Flask(__name__)
app.debug = True

@app.route("/", strict_slashes=False)
def food_gallery():
    """renders food gallery"""
    return render_template("gallery.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
