import os
from flask import Flask, render_template, redirect, request
from email.message import EmailMessage
import ssl
import smtplib

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

        return render_template("contact.html")
    
    else:
        name = request.form.get("name")
        
        email = request.form.get('email')
        
        comment = request.form.get('comment')

        

        subject = f"PenPen.tech New Email from {name}, {email}"
        body = f"Name: {name}\nEmail: {email}\n{comment}"
        print(body)
        
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

        
        return render_template('contact.html')

@app.route('/hobbies')
def hobbies():
    return render_template("hobbies.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)