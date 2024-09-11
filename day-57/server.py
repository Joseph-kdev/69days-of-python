from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", number=random_number, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"
    
    gender_response = requests.get(gender_url).json()
    gender = gender_response["gender"]
    
    age_response = requests.get(age_url).json()
    age = age_response["age"]
    
    return render_template("hello.html", name=name, gender=gender, age=age)


@app.route("/blog")
def get_blogs():
    blogs_url = f"https://api.npoint.io/c790b4d5cab58020d391"
    blog_posts = requests.get(blogs_url).json()
    
    return render_template("blog.html", posts=blog_posts)

if __name__ == "__main__":
    app.run(debug=True)