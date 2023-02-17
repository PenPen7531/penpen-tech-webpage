from flask import Flask, render_template, redirect, request



app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")



@app.route('/hobbies')
def hobbies():
    return render_template("hobbies.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)