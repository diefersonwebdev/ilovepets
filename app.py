# -*- coding: cp1252 -*-
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!!!</h1> <h2>Finalmente conseguir fazer Deploy nessa porra KKK </h2>"

if __name__ == "__main__":
    app.run(debug=True, port=33507)
