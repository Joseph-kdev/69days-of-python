from flask import Flask, render_template, request
import requests
from post import Post
import smtplib
import ssl
from email.message import EmailMessage

app = Flask(__name__)

DATA_SOURCE = "https://api.npoint.io/a51b7b87232739be5dfc"

blogs = []
blogs_data = requests.get(DATA_SOURCE).json()

for blog in blogs_data:
    blogs.append(blog)

@app.route('/')
def home():
    return render_template("index.html", blogs = blogs)

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def post(index):
    picked_blog = None
    for blog in blogs:
        if blog["id"] == index:
            picked_blog = blog
        
    return render_template("post.html", index = index, blog_piece = picked_blog)

@app.route("/contact", methods=["POST", "GET"])
def receive_data():
    if request.method == "GET":
        return render_template("contact.html", msg_sent = False)
    else:
        data = request.form
        print(data["name"], data["email"], data["phone"], data["message"])
        email_sender = data["email"]
        email_password = ""
        email_receiver = ""
        
        #set the subject and body
        subject = "New Message"
        body = f"{data['message']}, reach me through {data['phone']}"
        
        em = EmailMessage()
        em['From'] = email_sender
        em["To"] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        
        # add ssl
        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        
        return render_template("contact.html", msg_sent = True)

if __name__ == "__main__":
    app.run(debug=True)