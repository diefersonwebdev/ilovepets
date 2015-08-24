from flask import Flask, render_template
from wtforms import Form, BooleanField, TextField, PasswordField, validators

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
	return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
