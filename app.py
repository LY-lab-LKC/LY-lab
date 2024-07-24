import requests
from flask import Flask, flash, redirect, render_template, request, session
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secret import sender_email, sender_password, receiver_email

app = Flask(__name__)
app.debug = True



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/group")
def group():
    return render_template("group.html")

@app.route("/publication")
def publication():
    return render_template("publication.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        port = 465
        smtp_server = "smtp.gmail.com"
        Fname = request.form.get("Fname")
        Lname = request.form.get("Lname")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        mail = MIMEMultipart("alternative")
        mail["Subject"] = subject
        mail["From"] = sender_email
        mail["To"] = receiver_email
        
        text = "Name : " + Fname + " " + Lname + "\nEmail : " + email + "\n" + message

        mail.attach(MIMEText(text, "plain"))
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, mail.as_string())
            server.quit()

        return render_template("contact.html")
    else:
        return render_template("contact.html")


if __name__ == "__main__":
    app.run( debug=True)