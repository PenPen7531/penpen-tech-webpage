import os
from flask import Flask, render_template, redirect, request
from email.message import EmailMessage
import ssl
import smtplib
import json
from spotify import getTop10

app = Flask(__name__)

email_sender = "penpentech000@gmail.com"
email_password = "xiwknwzqmyutqelt"
email_receiver = "jeffmkwang@gmail.com"



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods = ["GET", "POST"])
def contact():

    if request.method == "GET":

        return render_template("contact.html", success = None)
    
    else:
        name = str(request.form.get("name"))
        name = name.capitalize()
        
        email = request.form.get('email')
        
        comment = request.form.get('comment')

        

        subject = f"PenPen.tech New Email from {name}"
        body = f"Name: {name}\n\nEmail: {email}\n\nMessage: {comment}"
        

        # Email Stuff
        em = EmailMessage()
        em['From'] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)

        # SSL
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        
        return render_template('contact.html', success = "true")

@app.route('/hobbies')
def hobbies():
    getTop10()
    with open("top10_data.json", 'r') as f:
        data = json.load(f)
    
    return render_template("hobbies.html", spotify = data)

@app.route("/experience")
def experience():
    return render_template("experience.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)