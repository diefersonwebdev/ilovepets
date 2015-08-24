# -*- coding: cp1252 -*-
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!!!</h1> <span>Finalmente conseguir fazer Deploy nessa porra õ/ </span>"

if __name__ == "__main__":
    app.run(debug=True, port=33507)
